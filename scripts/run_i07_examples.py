#!/usr/bin/env python3
"""Run I07 CPU examples and record source-bound results."""

from __future__ import annotations

import hashlib
import json
import platform
import subprocess
import sys
import time
from pathlib import Path

import numpy as np
import torch


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "labs" / "I07" / "examples.json"
RESULT_DIR = ROOT / ".build" / "i07" / "results"
EXAMPLE_TIMEOUT_SECONDS = 10
SUITE_TIMEOUT_SECONDS = 120


def load_examples() -> list[dict[str, str]]:
    data = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1 or not isinstance(data.get("examples"), list):
        raise RuntimeError("I07 example registry schema is invalid")
    examples: list[dict[str, str]] = []
    lesson_ids: set[str] = set()
    example_ids: set[str] = set()
    for raw in data["examples"]:
        entry = {key: str(raw[key]) for key in ("lesson_id", "example_id", "module", "source")}
        if entry["lesson_id"] in lesson_ids or entry["example_id"] in example_ids:
            raise RuntimeError(f"duplicate I07 registry entry: {entry}")
        source = (ROOT / entry["source"]).resolve()
        if not source.is_relative_to(ROOT) or not source.exists():
            raise RuntimeError(f"invalid I07 source: {entry['source']}")
        lesson_ids.add(entry["lesson_id"])
        example_ids.add(entry["example_id"])
        examples.append(entry)
    return examples


def main() -> int:
    examples = load_examples()
    RESULT_DIR.mkdir(parents=True, exist_ok=True)
    suite_started = time.perf_counter()
    rows: list[dict[str, object]] = []
    for entry in examples:
        started = time.perf_counter()
        result = subprocess.run(
            [sys.executable, "-m", entry["module"]], cwd=ROOT, capture_output=True,
            text=True, timeout=EXAMPLE_TIMEOUT_SECONDS, check=False,
        )
        elapsed = time.perf_counter() - started
        if result.returncode != 0:
            raise RuntimeError(f"{entry['example_id']} failed:\n{result.stderr}")
        try:
            output = json.loads(result.stdout)
        except json.JSONDecodeError as error:
            raise RuntimeError(f"{entry['example_id']} did not print one JSON object") from error
        source = ROOT / entry["source"]
        payload = {
            "schema_version": 1, "lesson_id": entry["lesson_id"], "example_id": entry["example_id"],
            "source": entry["source"], "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
            "command": f".venv\\Scripts\\python.exe -m {entry['module']}", "stdout": result.stdout.rstrip(),
            "output": output, "python_version": platform.python_version(), "torch_version": torch.__version__,
            "numpy_version": np.__version__, "device": "cpu", "process_seconds": elapsed,
        }
        (RESULT_DIR / f"{entry['example_id']}.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        rows.append({"example_id": entry["example_id"], "seconds": elapsed})
        print(f"{entry['example_id']}: process={elapsed:.6f}s")
        if time.perf_counter() - suite_started > SUITE_TIMEOUT_SECONDS:
            raise RuntimeError("I07 CPU suite exceeded 120 seconds")
    summary = {"example_count": len(rows), "suite_seconds": time.perf_counter() - suite_started, "examples": rows}
    (RESULT_DIR.parent / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
