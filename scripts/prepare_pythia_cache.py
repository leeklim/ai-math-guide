#!/usr/bin/env python3
"""Resolve immutable Pythia revisions and prepare the local Hugging Face cache."""

from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from huggingface_hub import HfApi, snapshot_download

from labs.real_models.common import CACHE_DIR, GPU_BUILD_DIR, directory_size, load_registries


def main() -> int:
    models, _, _ = load_registries()
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="all", choices=["all", *models])
    args = parser.parse_args()
    selected = list(models.values()) if args.model == "all" else [models[args.model]]
    api = HfApi()
    rows: list[dict[str, object]] = []
    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    for model in selected:
        started = time.perf_counter()
        info = api.model_info(model["repository"], revision=model["revision"])
        resolved_sha = str(info.sha)
        snapshot_download(
            repo_id=model["repository"],
            revision=resolved_sha,
            cache_dir=CACHE_DIR,
            allow_patterns=["*.json", "*.safetensors", "*.model", "*.txt", "tokenizer*"],
        )
        cache_bytes = directory_size(CACHE_DIR)
        if cache_bytes > 12 * 1024**3:
            raise RuntimeError(f"required Pythia cache exceeds 12 GiB: {cache_bytes}")
        rows.append(
            {
                "model_key": model["model_key"],
                "repository": model["repository"],
                "revision": model["revision"],
                "resolved_sha": resolved_sha,
                "status": "prepared",
                "download_seconds": time.perf_counter() - started,
                "cache_bytes_after": cache_bytes,
            }
        )
        print(f"prepared {model['repository']}@{resolved_sha} cache_bytes={cache_bytes}")

    manifest_path = GPU_BUILD_DIR / "cache-manifest.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "created_utc": datetime.now(timezone.utc).isoformat(),
                "cache_budget_bytes": 12 * 1024**3,
                "models": rows,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
