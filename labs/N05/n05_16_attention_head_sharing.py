"""N05-16: compare key-value head sharing in MHA, MQA, and GQA."""

from __future__ import annotations

import argparse
import json
import time
from typing import Any

import torch

from labs.N05.common import SEED, ResourceSpec, assert_within_limits, configure_runtime, tensor_shape, tensor_values


EXAMPLE_ID = "n05_16_attention_head_sharing"
SPEC = ResourceSpec(1, 2, 8, 0, 4, 0, 0, 0)


def expand_kv(kv: torch.Tensor, query_heads: int) -> torch.Tensor:
    if query_heads % kv.shape[1] != 0:
        raise ValueError("query head count must be divisible by key-value head count")
    return kv.repeat_interleave(query_heads // kv.shape[1], dim=1)


def compute() -> dict[str, torch.Tensor]:
    configure_runtime(); assert_within_limits(SPEC)
    query = torch.arange(16, dtype=torch.float32).reshape(1, 4, 2, 2)
    mha_kv = torch.arange(16, dtype=torch.float32).reshape(1, 4, 2, 2)
    mqa_kv = torch.arange(4, dtype=torch.float32).reshape(1, 1, 2, 2)
    gqa_kv = torch.arange(8, dtype=torch.float32).reshape(1, 2, 2, 2)
    mha_expanded = expand_kv(mha_kv, 4)
    mqa_expanded = expand_kv(mqa_kv, 4)
    gqa_expanded = expand_kv(gqa_kv, 4)
    return {"query": query, "mha_kv": mha_kv, "mqa_kv": mqa_kv, "gqa_kv": gqa_kv, "mha_expanded": mha_expanded, "mqa_expanded": mqa_expanded, "gqa_expanded": gqa_expanded, "kv_elements": torch.tensor([2 * mha_kv.numel(), 2 * mqa_kv.numel(), 2 * gqa_kv.numel()])}


def run_example() -> dict[str, Any]:
    started = time.perf_counter(); tensors = compute()
    result = {"example_id": EXAMPLE_ID, "seed": SEED, "dtype": str(tensors["query"].dtype), "shapes": {name: tensor_shape(value) for name, value in tensors.items()}, "values": {name: tensor_values(value) for name, value in tensors.items()}, "gradients": {}, "resources": SPEC.to_dict(), "compute_seconds": time.perf_counter() - started}
    result["stdout"] = "\n".join((f"seed={SEED} dtype={result['dtype']} device=cpu", f"query.shape={result['shapes']['query']}", f"MHA KV shape={result['shapes']['mha_kv']} expanded={result['shapes']['mha_expanded']}", f"MQA KV shape={result['shapes']['mqa_kv']} expanded={result['shapes']['mqa_expanded']}", f"GQA KV shape={result['shapes']['gqa_kv']} expanded={result['shapes']['gqa_expanded']}", f"K+V element counts MHA/MQA/GQA={result['values']['kv_elements']}"))
    return result


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--json", action="store_true"); args = parser.parse_args(); result = run_example(); print(json.dumps(result, ensure_ascii=False) if args.json else result["stdout"]); return 0


if __name__ == "__main__": raise SystemExit(main())
