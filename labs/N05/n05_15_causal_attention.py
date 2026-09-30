"""N05-15: compute causal scaled dot-product attention."""

from __future__ import annotations

import argparse
import json
import math
import time
from typing import Any

import torch

from labs.N05.common import SEED, ResourceSpec, assert_within_limits, configure_runtime, tensor_shape, tensor_values
from labs.N05.n05_14_qkv import compute as compute_qkv


EXAMPLE_ID = "n05_15_causal_attention"
SPEC = ResourceSpec(1, 2, 2, 0, 1, 0, 12, 0)


def compute() -> dict[str, torch.Tensor]:
    configure_runtime(); assert_within_limits(SPEC)
    qkv = compute_qkv(); query, key, value = qkv["query"], qkv["key"], qkv["value"]
    scaled_scores = query @ key.T / math.sqrt(query.shape[-1])
    causal_mask = torch.triu(torch.ones(2, 2, dtype=torch.bool), diagonal=1)
    masked_scores = scaled_scores.masked_fill(causal_mask, float("-inf"))
    attention_weights = torch.softmax(masked_scores, dim=-1)
    output = attention_weights @ value
    return {"query": query, "key": key, "value": value, "scaled_scores": scaled_scores, "causal_mask": causal_mask, "masked_scores": masked_scores, "attention_weights": attention_weights, "output": output}


def run_example() -> dict[str, Any]:
    started = time.perf_counter(); tensors = compute()
    result = {"example_id": EXAMPLE_ID, "seed": SEED, "dtype": str(tensors["query"].dtype), "shapes": {name: tensor_shape(value) for name, value in tensors.items()}, "values": {name: tensor_values(value) for name, value in tensors.items()}, "gradients": {}, "resources": SPEC.to_dict(), "compute_seconds": time.perf_counter() - started}
    result["stdout"] = "\n".join((f"seed={SEED} dtype={result['dtype']} device=cpu", f"scaled_scores={result['values']['scaled_scores']}", f"causal_mask={result['values']['causal_mask']}", f"attention_weights={result['values']['attention_weights']}", f"output={result['values']['output']}"))
    return result


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--json", action="store_true"); args = parser.parse_args(); result = run_example(); print(json.dumps(result, ensure_ascii=False) if args.json else result["stdout"]); return 0


if __name__ == "__main__": raise SystemExit(main())
