"""N05-22: compare full causal inference with tokenwise KV caching."""

from __future__ import annotations

import argparse
import json
import time
from typing import Any

import torch

from labs.N05.common import (
    SEED,
    ResourceSpec,
    assert_within_limits,
    configure_runtime,
    tensor_shape,
    tensor_values,
)
from labs.N05.tiny_decoder import TinyDecoderLM, parameter_count


EXAMPLE_ID = "n05_22_kv_cache"
SPEC = ResourceSpec(1, 4, 4, 1, 1, 16, 300, 0)


def compute() -> dict[str, torch.Tensor]:
    configure_runtime()
    assert_within_limits(SPEC)
    model = TinyDecoderLM()
    model.eval()
    input_ids = torch.tensor([[1, 4, 2, 7]])
    with torch.no_grad():
        full_logits, _, _ = model(input_ids)
        past_key_values = None
        step_logits = []
        cache_lengths = []
        for position in range(input_ids.shape[1]):
            current = input_ids[:, position : position + 1]
            logits, past_key_values, _ = model(current, past_key_values)
            step_logits.append(logits)
            cache_lengths.append(past_key_values[0][0].shape[-2])
        cached_logits = torch.cat(step_logits, dim=1)
    return {
        "input_ids": input_ids,
        "full_logits": full_logits,
        "cached_logits": cached_logits,
        "maximum_absolute_difference": (full_logits - cached_logits).abs().max(),
        "cache_lengths": torch.tensor(cache_lengths),
        "final_key_cache": past_key_values[0][0],
        "final_value_cache": past_key_values[0][1],
        "parameter_count": torch.tensor(parameter_count(model)),
    }


def run_example() -> dict[str, Any]:
    started = time.perf_counter()
    tensors = compute()
    result = {
        "example_id": EXAMPLE_ID,
        "seed": SEED,
        "dtype": str(tensors["full_logits"].dtype),
        "shapes": {name: tensor_shape(value) for name, value in tensors.items()},
        "values": {name: tensor_values(value) for name, value in tensors.items()},
        "gradients": {},
        "resources": SPEC.to_dict(),
        "compute_seconds": time.perf_counter() - started,
    }
    result["stdout"] = "\n".join(
        (
            f"seed={SEED} dtype={result['dtype']} device=cpu",
            f"input_ids={result['values']['input_ids']}",
            f"full_logits.shape={result['shapes']['full_logits']}",
            f"cached_logits.shape={result['shapes']['cached_logits']}",
            f"cache_lengths={result['values']['cache_lengths']}",
            f"final_key_cache.shape={result['shapes']['final_key_cache']}",
            f"max_abs_difference={result['values']['maximum_absolute_difference']}",
        )
    )
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = run_example()
    print(json.dumps(result, ensure_ascii=False) if args.json else result["stdout"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
