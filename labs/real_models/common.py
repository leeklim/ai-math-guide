"""Registry and manifest helpers that do not import GPU libraries."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
MODEL_REGISTRY = ROOT / "labs" / "real_models" / "models.json"
EXPERIMENT_REGISTRY = ROOT / "labs" / "real_models" / "experiments.json"
MANIFEST_SCHEMA = ROOT / "labs" / "real_models" / "manifest_schema.json"
CACHE_DIR = ROOT / ".cache" / "huggingface"
GPU_BUILD_DIR = ROOT / ".build" / "gpu"
RESULTS_DIR = GPU_BUILD_DIR / "results"
ACTIVATIONS_DIR = GPU_BUILD_DIR / "activations"


def read_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"JSON root must be an object: {path}")
    return data


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def sha256_json(value: Any) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return sha256_bytes(payload.encode("utf-8"))


def directory_size(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(item.stat().st_size for item in path.rglob("*") if item.is_file())


def load_registries() -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]], int]:
    model_data = read_json(MODEL_REGISTRY)
    experiment_data = read_json(EXPERIMENT_REGISTRY)
    if model_data.get("schema_version") != 1 or experiment_data.get("schema_version") != 1:
        raise ValueError("unsupported real-model registry schema")

    models = {str(item["model_key"]): item for item in model_data["models"]}
    experiments = {str(item["experiment_id"]): item for item in experiment_data["experiments"]}
    if len(models) != len(model_data["models"]):
        raise ValueError("duplicate model_key")
    if len(experiments) != len(experiment_data["experiments"]):
        raise ValueError("duplicate experiment_id")

    for experiment_id, experiment in experiments.items():
        model_key = str(experiment.get("model_key", ""))
        if model_key not in models:
            raise ValueError(f"unknown model_key in {experiment_id}: {model_key}")
        model = models[model_key]
        if int(experiment["sequence_length"]) > int(model["sequence_limit"]):
            raise ValueError(f"sequence limit exceeded: {experiment_id}")
        if model["repository"].endswith("-v0") or "7b" in model["repository"].lower():
            raise ValueError(f"forbidden model family: {model['repository']}")
        if model["revision"] != "step143000":
            raise ValueError(f"unpinned Pythia revision: {model['repository']}")
        if model_key == "pythia-410m" and experiment["mode"] != "inference":
            raise ValueError("Pythia 410M must remain inference-only")

    artifact_limit = int(experiment_data["artifact_limit_bytes"])
    if artifact_limit > 256 * 1024 * 1024:
        raise ValueError("artifact limit exceeds 256 MiB")
    return models, experiments, artifact_limit


def validate_manifest_shape(manifest: dict[str, Any]) -> None:
    schema = read_json(MANIFEST_SCHEMA)
    missing = [name for name in schema["required"] if name not in manifest]
    if missing:
        raise ValueError("manifest fields missing: " + ", ".join(missing))
    if manifest["schema_version"] != 1 or manifest["status"] not in {"passed", "failed"}:
        raise ValueError("manifest schema/status is invalid")
