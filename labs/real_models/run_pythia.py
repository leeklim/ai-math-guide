"""Run one pinned Pythia experiment and write a provenance-rich manifest."""

from __future__ import annotations

import argparse
import json
import platform
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import torch
import transformers
from transformers import AutoTokenizer, GPTNeoXForCausalLM

from labs.real_models.common import (
    ACTIVATIONS_DIR,
    CACHE_DIR,
    GPU_BUILD_DIR,
    RESULTS_DIR,
    ROOT,
    directory_size,
    load_registries,
    sha256_file,
    sha256_json,
    validate_manifest_shape,
)


PROMPTS = [
    {"text": "Paris is the capital city of", "condition": "place"},
    {"text": "Berlin is the capital city of", "condition": "place"},
    {"text": "Rome is the capital city of", "condition": "place"},
    {"text": "Madrid is the capital city of", "condition": "place"},
    {"text": "A robin is a kind of", "condition": "animal"},
    {"text": "A salmon is a kind of", "condition": "animal"},
    {"text": "A tiger is a kind of", "condition": "animal"},
    {"text": "A sparrow is a kind of", "condition": "animal"},
]

PATCHING_PROMPTS = [
    {"text": "The capital of France is", "condition": "clean", "answer": " Paris"},
    {"text": "The capital of Germany is", "condition": "corrupt", "answer": " Berlin"},
]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def git_commit() -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, check=True, capture_output=True, text=True, timeout=10
    )
    return result.stdout.strip()


def gpu_snapshot() -> dict[str, object]:
    command = [
        "nvidia-smi",
        "--query-gpu=name,driver_version,memory.total,memory.free",
        "--format=csv,noheader,nounits",
    ]
    result = subprocess.run(command, check=True, capture_output=True, text=True, timeout=10)
    name, driver, total, free = [part.strip() for part in result.stdout.splitlines()[0].split(",")]
    return {
        "name": name,
        "driver": driver,
        "memory_total_mib": int(total),
        "memory_free_mib": int(free),
    }


def cache_entry(repository: str, revision: str) -> dict[str, object]:
    path = GPU_BUILD_DIR / "cache-manifest.json"
    if not path.exists():
        raise RuntimeError("cache manifest가 없다. scripts/prepare_pythia_cache.py를 먼저 실행하라")
    data = json.loads(path.read_text(encoding="utf-8"))
    for entry in data.get("models", []):
        if entry.get("repository") == repository and entry.get("revision") == revision:
            if entry.get("status") != "prepared":
                raise RuntimeError(f"cache preparation did not pass: {repository}")
            return entry
    raise RuntimeError(f"model is missing from cache manifest: {repository}@{revision}")


def hook_module(model: GPTNeoXForCausalLM, layer: int) -> torch.nn.Module:
    layers = model.gpt_neox.layers
    if layer < 0 or layer >= len(layers):
        raise RuntimeError(f"hook layer {layer} is outside 0..{len(layers) - 1}")
    return layers[layer].mlp.dense_4h_to_h


def input_rows_for_experiment(experiment: dict[str, Any]) -> list[dict[str, str]]:
    if experiment["mode"] == "activation_patching":
        return PATCHING_PROMPTS
    if experiment["model_key"] in {"pythia-160m", "pythia-410m"}:
        return PROMPTS
    return PROMPTS[:1]


def run_activation_patch(
    model: GPTNeoXForCausalLM,
    tokenizer: Any,
    experiment: dict[str, Any],
) -> tuple[np.ndarray, None, dict[str, Any]]:
    captured: dict[str, torch.Tensor] = {}
    patch_value: torch.Tensor | None = None
    calls = 0

    def patch_hook(
        _module: torch.nn.Module,
        _inputs: tuple[torch.Tensor, ...],
        output: torch.Tensor,
    ) -> torch.Tensor | None:
        nonlocal calls
        calls += 1
        if patch_value is None:
            captured["output"] = output
            return None
        patched = output.clone()
        patched[:, -1, :] = patch_value.to(device=output.device, dtype=output.dtype)
        captured["output"] = patched
        return patched

    def forward(text: str) -> tuple[torch.Tensor, torch.Tensor, int]:
        captured.clear()
        encoded = tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            max_length=int(experiment["sequence_length"]),
        )
        input_ids = encoded["input_ids"].to("cuda")
        attention_mask = encoded.get("attention_mask")
        if attention_mask is not None:
            attention_mask = attention_mask.to("cuda")
        with torch.no_grad():
            outputs = model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)
        observed = captured.get("output")
        if observed is None or observed.ndim != 3:
            raise RuntimeError("patching hook did not capture a (batch, token, hidden) tensor")
        return observed[0, -1].detach(), outputs.logits[0, -1].detach(), int(input_ids.shape[1])

    handle = hook_module(model, int(experiment["layer"])).register_forward_hook(patch_hook)
    try:
        clean_activation, clean_logits, clean_length = forward(PATCHING_PROMPTS[0]["text"])
        corrupt_activation, corrupt_logits, corrupt_length = forward(PATCHING_PROMPTS[1]["text"])
        target_ids = tokenizer(PATCHING_PROMPTS[0]["answer"], add_special_tokens=False)["input_ids"]
        foil_ids = tokenizer(PATCHING_PROMPTS[1]["answer"], add_special_tokens=False)["input_ids"]
        if len(target_ids) != 1 or len(foil_ids) != 1:
            raise RuntimeError("patching target and foil must each be one token")
        target_id, foil_id = int(target_ids[0]), int(foil_ids[0])

        def metric(logits: torch.Tensor) -> float:
            return float((logits[target_id] - logits[foil_id]).float().cpu())

        patch_value = clean_activation
        patched_activation, patched_logits, patched_length = forward(PATCHING_PROMPTS[1]["text"])
    finally:
        handle.remove()

    clean_metric = metric(clean_logits)
    corrupt_metric = metric(corrupt_logits)
    patched_metric = metric(patched_logits)
    denominator = clean_metric - corrupt_metric
    if abs(denominator) < 1e-8:
        raise RuntimeError("clean and corrupt contrastive metrics are indistinguishable")
    activations = torch.stack(
        [clean_activation, corrupt_activation, patched_activation]
    ).float().cpu().numpy()
    summary = {
        "sample_count": 3,
        "activation_shape": list(activations.shape),
        "hook_calls": calls,
        "sequence_lengths": [clean_length, corrupt_length, patched_length],
        "target_token": tokenizer.decode([target_id]),
        "foil_token": tokenizer.decode([foil_id]),
        "clean_metric": clean_metric,
        "corrupt_metric": corrupt_metric,
        "patched_metric": patched_metric,
        "recovery_fraction": (patched_metric - corrupt_metric) / denominator,
        "metric_definition": "Paris-minus-Berlin next-token logit",
    }
    return activations, None, summary


def run_forward_set(
    model: GPTNeoXForCausalLM,
    tokenizer: Any,
    experiment: dict[str, Any],
) -> tuple[np.ndarray, np.ndarray | None, dict[str, Any]]:
    if experiment["mode"] == "activation_patching":
        return run_activation_patch(model, tokenizer, experiment)
    selected: list[np.ndarray] = []
    selected_gradient: np.ndarray | None = None
    calls = 0
    captured: dict[str, torch.Tensor] = {}
    gradient_mode = False

    def capture(_module: torch.nn.Module, _inputs: tuple[torch.Tensor, ...], output: torch.Tensor) -> torch.Tensor | None:
        nonlocal calls
        calls += 1
        if gradient_mode:
            observed = output.detach().requires_grad_(True)
            captured["output"] = observed
            return observed
        captured["output"] = output
        return None

    module = hook_module(model, int(experiment["layer"]))
    handle = module.register_forward_hook(capture)
    sequence_lengths: list[int] = []
    top_tokens: list[str] = []
    margin_value: float | None = None
    try:
        prompt_rows = input_rows_for_experiment(experiment)
        for index, row in enumerate(prompt_rows):
            encoded = tokenizer(
                row["text"],
                return_tensors="pt",
                truncation=True,
                max_length=int(experiment["sequence_length"]),
            )
            input_ids = encoded["input_ids"].to("cuda")
            attention_mask = encoded.get("attention_mask")
            if attention_mask is not None:
                attention_mask = attention_mask.to("cuda")
            sequence_lengths.append(int(input_ids.shape[1]))
            gradient_mode = experiment["mode"] == "selected_activation_gradient" and index == 0
            captured.clear()

            context = torch.enable_grad() if gradient_mode else torch.no_grad()
            with context:
                outputs = model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)
                observed = captured.get("output")
                if observed is None or observed.ndim != 3:
                    raise RuntimeError("hook did not capture a (batch, token, hidden) tensor")
                token_index = int(input_ids.shape[1]) - 1
                activation = observed[0, token_index].detach().float().cpu().numpy()
                selected.append(activation)
                last_logits = outputs.logits[0, token_index]
                top = torch.topk(last_logits, k=2)
                top_tokens.append(tokenizer.decode([int(top.indices[0])]))
                if gradient_mode:
                    margin = top.values[0] - top.values[1]
                    margin_value = float(margin.detach().cpu())
                    margin.backward()
                    if observed.grad is None:
                        raise RuntimeError("selected activation gradient was not retained")
                    selected_gradient = observed.grad[0, token_index].detach().float().cpu().numpy()
    finally:
        handle.remove()

    activations = np.stack(selected)
    prompt_rows = input_rows_for_experiment(experiment)
    conditions = [row["condition"] for row in prompt_rows]
    norms = np.linalg.norm(activations, axis=1)
    summary: dict[str, Any] = {
        "sample_count": int(activations.shape[0]),
        "activation_shape": list(activations.shape),
        "hook_calls": calls,
        "sequence_lengths": sequence_lengths,
        "top_tokens": top_tokens,
        "activation_norm_mean": float(norms.mean()),
        "activation_norm_variance": float(norms.var(ddof=1)) if len(norms) > 1 else 0.0,
        "activation_norm_min": float(norms.min()),
        "activation_norm_max": float(norms.max()),
        "logit_margin": margin_value,
    }
    if len(conditions) > 1:
        place = activations[np.array(conditions) == "place"].mean(axis=0)
        animal = activations[np.array(conditions) == "animal"].mean(axis=0)
        summary["condition_mean_difference_l2"] = float(np.linalg.norm(place - animal))
    if selected_gradient is not None:
        summary["gradient_l2"] = float(np.linalg.norm(selected_gradient))
    if experiment["model_key"] == "pythia-410m":
        reference_path = ACTIVATIONS_DIR / "pythia_160m_activation_dataset" / "selected.npz"
        if not reference_path.exists():
            raise RuntimeError("160M activation dataset is required before the 410M comparison")
        with np.load(reference_path) as reference_file:
            reference = reference_file["activations"].astype(np.float64)
        current = activations.astype(np.float64)
        if reference.shape[0] != current.shape[0]:
            raise RuntimeError("160M and 410M comparison sample counts differ")
        reference -= reference.mean(axis=0, keepdims=True)
        current -= current.mean(axis=0, keepdims=True)
        numerator = np.linalg.norm(reference.T @ current, ord="fro") ** 2
        denominator = np.linalg.norm(reference.T @ reference, ord="fro")
        denominator *= np.linalg.norm(current.T @ current, ord="fro")
        reference_distances = np.sqrt(np.sum((reference[:, None] - reference[None, :]) ** 2, axis=-1))
        current_distances = np.sqrt(np.sum((current[:, None] - current[None, :]) ** 2, axis=-1))
        upper = np.triu_indices(len(reference), k=1)
        summary["linear_cka_with_160m"] = float(numerator / denominator)
        summary["rsa_distance_correlation_with_160m"] = float(
            np.corrcoef(reference_distances[upper], current_distances[upper])[0, 1]
        )
    return activations, selected_gradient, summary


def execute(experiment_id: str) -> dict[str, Any]:
    models, experiments, artifact_limit = load_registries()
    if experiment_id not in experiments:
        raise ValueError(f"unknown experiment: {experiment_id}")
    experiment = experiments[experiment_id]
    model_spec = models[str(experiment["model_key"])]
    source_path = Path(__file__).resolve()
    start_wall = utc_now()
    start = time.perf_counter()
    before = gpu_snapshot()
    if int(before["memory_free_mib"]) < 6144:
        raise RuntimeError(f"available VRAM is below 6 GiB: {before['memory_free_mib']} MiB")
    if directory_size(CACHE_DIR) > 12 * 1024**3:
        raise RuntimeError("required model cache exceeds 12 GiB")

    cache = cache_entry(str(model_spec["repository"]), str(model_spec["revision"]))
    resolved_sha = str(cache["resolved_sha"])
    torch.manual_seed(int(experiment["seed"]))
    torch.cuda.manual_seed_all(int(experiment["seed"]))
    torch.use_deterministic_algorithms(True)
    torch.cuda.empty_cache()
    warmup = torch.zeros(1, device="cuda")
    del warmup
    torch.cuda.reset_peak_memory_stats()

    tokenizer = AutoTokenizer.from_pretrained(
        model_spec["repository"],
        revision=resolved_sha,
        cache_dir=CACHE_DIR,
        local_files_only=True,
        trust_remote_code=False,
    )
    model = GPTNeoXForCausalLM.from_pretrained(
        model_spec["repository"],
        revision=resolved_sha,
        cache_dir=CACHE_DIR,
        local_files_only=True,
        trust_remote_code=False,
        dtype=torch.float16,
    )
    model.eval().requires_grad_(False).to("cuda")
    config = model.config.to_dict()
    activations, gradient, summary = run_forward_set(model, tokenizer, experiment)

    artifact_dir = ACTIVATIONS_DIR / experiment_id
    artifact_dir.mkdir(parents=True, exist_ok=True)
    artifact_path = artifact_dir / "selected.npz"
    arrays = {"activations": activations}
    if gradient is not None:
        arrays["gradient"] = gradient
    np.savez_compressed(artifact_path, **arrays)
    artifact_bytes = artifact_path.stat().st_size
    if artifact_bytes > artifact_limit:
        artifact_path.unlink(missing_ok=True)
        raise RuntimeError(f"artifact exceeds limit: {artifact_bytes} > {artifact_limit}")

    peak = int(torch.cuda.max_memory_allocated())
    if peak > int(model_spec["peak_vram_limit_bytes"]):
        raise RuntimeError(f"peak VRAM exceeds model limit: {peak}")
    duration = time.perf_counter() - start
    if duration > int(model_spec["timeout_seconds"]):
        raise RuntimeError(f"execution exceeded timeout: {duration:.3f}s")
    after = gpu_snapshot()
    del model, tokenizer
    torch.cuda.empty_cache()

    input_rows = input_rows_for_experiment(experiment)
    artifact_relative = artifact_path.relative_to(ROOT).as_posix()
    manifest: dict[str, Any] = {
        "schema_version": 1,
        "experiment_id": experiment_id,
        "lesson_id": experiment["lesson_id"],
        "status": "passed",
        "source": {
            "path": source_path.relative_to(ROOT).as_posix(),
            "sha256": sha256_file(source_path),
            "git_commit": git_commit(),
        },
        "command": f".venv-gpu\\Scripts\\python.exe -m labs.real_models.run_pythia {experiment_id}",
        "timestamps": {"started_utc": start_wall, "finished_utc": utc_now(), "seconds": duration},
        "versions": {
            "python": platform.python_version(),
            "torch": torch.__version__,
            "transformers": transformers.__version__,
            "numpy": np.__version__,
            "cuda_runtime": torch.version.cuda,
        },
        "gpu": {"before": before, "after": after, "compute_capability": list(torch.cuda.get_device_capability())},
        "model": {
            "repository": model_spec["repository"],
            "requested_revision": model_spec["revision"],
            "resolved_sha": resolved_sha,
            "tokenizer_repository": model_spec["repository"],
            "tokenizer_resolved_sha": resolved_sha,
            "config_sha256": sha256_json(config),
            "trust_remote_code": False,
        },
        "seed": int(experiment["seed"]),
        "determinism": {"algorithms_enabled": torch.are_deterministic_algorithms_enabled()},
        "dtype": str(model_spec["dtype"]),
        "mode": experiment["mode"],
        "inputs": {
            "source": "fixed prompts embedded in labs/real_models/run_pythia.py",
            "sha256": sha256_json(input_rows),
            "batch_size": 1,
            "sequence_limit": int(experiment["sequence_length"]),
            "sample_count": len(input_rows),
        },
        "hook": {
            "module": f"gpt_neox.layers.{experiment['layer']}.mlp.dense_4h_to_h",
            "layer": int(experiment["layer"]),
            "token": experiment["token"],
            "component": experiment["component"],
        },
        "resources": {
            "peak_allocated_bytes": peak,
            "peak_limit_bytes": int(model_spec["peak_vram_limit_bytes"]),
            "free_vram_before_mib": int(before["memory_free_mib"]),
            "free_vram_after_mib": int(after["memory_free_mib"]),
            "artifact_bytes": artifact_bytes,
            "artifact_limit_bytes": artifact_limit,
            "timeout_seconds": int(model_spec["timeout_seconds"]),
        },
        "artifacts": [
            {
                "path": artifact_relative,
                "sha256": sha256_file(artifact_path),
                "bytes": artifact_bytes,
                "arrays": {name: {"shape": list(value.shape), "dtype": str(value.dtype)} for name, value in arrays.items()},
            }
        ],
        "summary": summary,
        "assertions": {
            "finite_activations": bool(np.isfinite(activations).all()),
            "gradient_contract_met": (
                experiment["mode"] != "selected_activation_gradient"
                or gradient is not None
                and bool(np.isfinite(gradient).all() and np.linalg.norm(gradient) > 0)
            ),
            "within_vram_limit": peak <= int(model_spec["peak_vram_limit_bytes"]),
            "within_artifact_limit": artifact_bytes <= artifact_limit,
            "inference_only_410m": experiment["model_key"] != "pythia-410m" or gradient is None,
        },
        "failure": None,
    }
    if not all(bool(value) for value in manifest["assertions"].values()):
        raise RuntimeError(f"experiment assertions failed: {manifest['assertions']}")
    validate_manifest_shape(manifest)
    result_dir = RESULTS_DIR / experiment_id
    result_dir.mkdir(parents=True, exist_ok=True)
    (result_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("experiment_id")
    args = parser.parse_args()
    try:
        manifest = execute(args.experiment_id)
    except Exception as error:
        print(f"{type(error).__name__}: {error}", file=sys.stderr)
        return 1
    print(json.dumps({"experiment_id": manifest["experiment_id"], "summary": manifest["summary"]}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
