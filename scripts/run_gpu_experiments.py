#!/usr/bin/env python3
"""Run registered GPU experiments in isolated processes with hard timeouts."""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from labs.real_models.common import load_registries


def main() -> int:
    models, experiments, _ = load_registries()
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--all", action="store_true")
    group.add_argument("--experiment", action="append", choices=list(experiments))
    args = parser.parse_args()
    selected = list(experiments) if args.all else args.experiment
    suite_started = time.perf_counter()

    for experiment_id in selected:
        experiment = experiments[experiment_id]
        timeout = int(models[str(experiment["model_key"])]["timeout_seconds"])
        command = [sys.executable, "-m", "labs.real_models.run_pythia", experiment_id]
        print(f"running {experiment_id} timeout={timeout}s", flush=True)
        try:
            result = subprocess.run(command, text=True, capture_output=True, timeout=timeout, check=False)
        except subprocess.TimeoutExpired:
            print(f"timeout: {experiment_id}", file=sys.stderr)
            return 1
        if result.stdout:
            print(result.stdout, end="")
        if result.stderr:
            print(result.stderr, end="", file=sys.stderr)
        if result.returncode != 0:
            return result.returncode
        if time.perf_counter() - suite_started > 1200:
            print("GPU suite exceeded 1200 seconds", file=sys.stderr)
            return 1
    print(f"GPU suite passed in {time.perf_counter() - suite_started:.3f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
