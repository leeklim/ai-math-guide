#!/usr/bin/env python3
"""Validate the isolated CUDA environment without downloading a model."""

from __future__ import annotations

import json
import platform
import subprocess
import sys
import time
from pathlib import Path

import numpy as np
import torch
import transformers


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / ".build" / "gpu" / "environment.json"
EXPECTED = {
    "python": (3, 12),
    "numpy": "2.5.3",
    "torch": "2.13.0",
    "transformers": "5.17.0",
}


def nvidia_smi() -> dict[str, object]:
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


def main() -> int:
    if sys.version_info[:2] != EXPECTED["python"]:
        raise RuntimeError(f"Python version mismatch: {sys.version_info[:2]}")
    versions = {
        "python": platform.python_version(),
        "numpy": np.__version__,
        "torch": torch.__version__,
        "transformers": transformers.__version__,
        "cuda_runtime": torch.version.cuda,
    }
    for package in ("numpy", "transformers"):
        if versions[package] != EXPECTED[package]:
            raise RuntimeError(f"{package} version mismatch: {versions[package]}")
    if not versions["torch"].startswith(EXPECTED["torch"]):
        raise RuntimeError(f"torch version mismatch: {versions['torch']}")
    if not torch.cuda.is_available():
        raise RuntimeError("torch.cuda.is_available() is false")

    gpu = nvidia_smi()
    if gpu["memory_free_mib"] < 6144:
        raise RuntimeError(f"available VRAM is below 6 GiB: {gpu['memory_free_mib']} MiB")

    torch.use_deterministic_algorithms(True)
    torch.manual_seed(20261001)
    torch.cuda.manual_seed_all(20261001)
    device = torch.device("cuda:0")
    torch.cuda.empty_cache()
    warmup = torch.zeros(1, device=device)
    del warmup
    torch.cuda.reset_peak_memory_stats()

    started = time.perf_counter()
    left = torch.tensor([[1.0, 2.0], [3.0, 4.0]], device=device, requires_grad=True)
    right = torch.tensor([[0.5, -1.0], [2.0, 1.5]], device=device)
    output = left @ right
    output.square().sum().backward()
    first = output.detach().cpu()
    first_gradient = left.grad.detach().cpu().clone()

    left_2 = left.detach().clone().requires_grad_(True)
    output_2 = left_2 @ right
    output_2.square().sum().backward()
    if not torch.equal(first, output_2.detach().cpu()):
        raise RuntimeError("deterministic matmul check failed")
    if not torch.equal(first_gradient, left_2.grad.detach().cpu()):
        raise RuntimeError("deterministic autograd check failed")

    elapsed = time.perf_counter() - started
    if elapsed > 120:
        raise RuntimeError(f"GPU diagnostic exceeded 120 seconds: {elapsed:.3f}")
    payload = {
        "schema_version": 1,
        "status": "passed",
        "versions": versions,
        "gpu": gpu,
        "compute_capability": list(torch.cuda.get_device_capability(device)),
        "matmul": first.tolist(),
        "gradient": first_gradient.tolist(),
        "deterministic_algorithms": torch.are_deterministic_algorithms_enabled(),
        "peak_allocated_bytes": int(torch.cuda.max_memory_allocated(0)),
        "elapsed_seconds": elapsed,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
