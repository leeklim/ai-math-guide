"""N05-24: show that identical generated tokens do not identify hidden coordinates."""

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


EXAMPLE_ID = "n05_24_cot_observation"
SPEC = ResourceSpec(1, 2, 2, 0, 1, 3, 12, 0)


def compute() -> dict[str, torch.Tensor]:
    configure_runtime()
    assert_within_limits(SPEC)
    hidden_a = torch.tensor([[1.0, 2.0], [2.0, 1.0]])
    coordinate_swap = torch.tensor([[0.0, 1.0], [1.0, 0.0]])
    hidden_b = hidden_a @ coordinate_swap
    unembedding_a = torch.tensor([[1.0, 0.0], [0.0, 1.0], [-1.0, 1.0]])
    unembedding_b = unembedding_a @ coordinate_swap
    logits_a = hidden_a @ unembedding_a.T
    logits_b = hidden_b @ unembedding_b.T
    generated_tokens_a = logits_a.argmax(dim=-1)
    generated_tokens_b = logits_b.argmax(dim=-1)
    return {
        "hidden_a": hidden_a,
        "hidden_b": hidden_b,
        "unembedding_a": unembedding_a,
        "unembedding_b": unembedding_b,
        "logits_a": logits_a,
        "logits_b": logits_b,
        "generated_tokens_a": generated_tokens_a,
        "generated_tokens_b": generated_tokens_b,
        "maximum_logit_difference": (logits_a - logits_b).abs().max(),
    }


def run_example() -> dict[str, Any]:
    started = time.perf_counter()
    tensors = compute()
    result = {
        "example_id": EXAMPLE_ID,
        "seed": SEED,
        "dtype": str(tensors["hidden_a"].dtype),
        "shapes": {name: tensor_shape(value) for name, value in tensors.items()},
        "values": {name: tensor_values(value) for name, value in tensors.items()},
        "gradients": {},
        "resources": SPEC.to_dict(),
        "compute_seconds": time.perf_counter() - started,
    }
    result["stdout"] = "\n".join(
        (
            f"seed={SEED} dtype={result['dtype']} device=cpu",
            f"hidden_a={result['values']['hidden_a']}",
            f"hidden_b={result['values']['hidden_b']}",
            f"logits_a={result['values']['logits_a']}",
            f"logits_b={result['values']['logits_b']}",
            f"generated_tokens_a={result['values']['generated_tokens_a']}",
            f"generated_tokens_b={result['values']['generated_tokens_b']}",
            f"max_logit_difference={result['values']['maximum_logit_difference']}",
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

