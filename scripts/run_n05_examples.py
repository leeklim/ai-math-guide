#!/usr/bin/env python3
"""Run the required N05 examples under fixed CPU budgets."""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT_DIR = ROOT / ".build" / "n05" / "results"
EXAMPLE_TIMEOUT_SECONDS = 10
SUITE_TIMEOUT_SECONDS = 120
SUITE_TARGET_SECONDS = 30
EXAMPLES = (
    ("n05_01_tensor_graph", ROOT / "labs" / "N05" / "n05_01_tensor_graph.py"),
    ("n05_02_single_neuron", ROOT / "labs" / "N05" / "n05_02_single_neuron.py"),
    ("n05_03_mlp_forward", ROOT / "labs" / "N05" / "n05_03_mlp_forward.py"),
)


def source_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    suite_started = time.perf_counter()
    import_started = time.perf_counter()
    import numpy as np
    import torch
    import_seconds = time.perf_counter() - import_started

    if torch.version.cuda is not None:
        raise RuntimeError("N05 examples require the pinned CPU-only PyTorch build")

    RESULT_DIR.mkdir(parents=True, exist_ok=True)
    environment = os.environ.copy()
    environment.update(
        {
            "OMP_NUM_THREADS": "1",
            "MKL_NUM_THREADS": "1",
            "OPENBLAS_NUM_THREADS": "1",
            "NUMEXPR_NUM_THREADS": "1",
            "PYTHONPATH": str(ROOT),
        }
    )

    results: list[dict[str, object]] = []
    for example_id, source_path in EXAMPLES:
        if time.perf_counter() - suite_started >= SUITE_TIMEOUT_SECONDS:
            raise TimeoutError(
                f"N05 example suite exceeded {SUITE_TIMEOUT_SECONDS} seconds before {example_id}"
            )
        process_started = time.perf_counter()
        try:
            completed = subprocess.run(
                [sys.executable, str(source_path), "--json"],
                cwd=ROOT,
                env=environment,
                check=True,
                capture_output=True,
                text=True,
                encoding="utf-8",
                timeout=EXAMPLE_TIMEOUT_SECONDS,
            )
        except subprocess.TimeoutExpired as error:
            raise TimeoutError(
                f"{example_id} exceeded the {EXAMPLE_TIMEOUT_SECONDS}-second hard timeout"
            ) from error
        process_seconds = time.perf_counter() - process_started
        payload = json.loads(completed.stdout)
        if payload.get("example_id") != example_id:
            raise RuntimeError(f"example ID mismatch for {source_path}")
        payload.update(
            {
                "python_version": ".".join(map(str, sys.version_info[:3])),
                "torch_version": torch.__version__,
                "numpy_version": np.__version__,
                "device": "cpu",
                "torch_import_seconds": import_seconds,
                "process_seconds": process_seconds,
                "source_path": source_path.relative_to(ROOT).as_posix(),
                "source_sha256": source_sha256(source_path),
                "command": f".venv\\Scripts\\python.exe {source_path.relative_to(ROOT).as_posix()}",
                "figure_paths": [],
            }
        )
        (RESULT_DIR / f"{example_id}.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        results.append(payload)
        print(
            f"{example_id}: compute={payload['compute_seconds']:.6f}s "
            f"process={process_seconds:.6f}s parameters={payload['resources']['parameter_count']}"
        )

    suite_seconds = time.perf_counter() - suite_started
    if suite_seconds > SUITE_TIMEOUT_SECONDS:
        raise TimeoutError(f"N05 example suite exceeded {SUITE_TIMEOUT_SECONDS} seconds")
    summary = {
        "example_count": len(results),
        "torch_import_seconds": import_seconds,
        "suite_seconds": suite_seconds,
        "suite_target_seconds": SUITE_TARGET_SECONDS,
        "suite_target_met": suite_seconds <= SUITE_TARGET_SECONDS,
        "example_timeout_seconds": EXAMPLE_TIMEOUT_SECONDS,
        "suite_timeout_seconds": SUITE_TIMEOUT_SECONDS,
        "intra_op_threads": 1,
        "inter_op_threads": 1,
    }
    (RESULT_DIR / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
