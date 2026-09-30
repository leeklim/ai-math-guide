"""N05-01: trace values, shapes, and dependencies in a small tensor graph."""

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


EXAMPLE_ID = "n05_01_tensor_graph"
SPEC = ResourceSpec(
    batch_size=1,
    sequence_length=2,
    model_dimension=2,
    transformer_layers=0,
    attention_heads=0,
    vocabulary_size=0,
    parameter_count=0,
    training_steps=0,
)


def compute() -> dict[str, torch.Tensor]:
    configure_runtime()
    assert_within_limits(SPEC)
    x = torch.tensor([1.0, 2.0], dtype=torch.float32, requires_grad=True)
    w = torch.tensor([3.0, 4.0], dtype=torch.float32)
    product = x * w
    output = product.sum()
    output.backward()
    return {"x": x, "w": w, "product": product, "output": output}


def run_example() -> dict[str, Any]:
    started = time.perf_counter()
    tensors = compute()
    compute_seconds = time.perf_counter() - started
    result = {
        "example_id": EXAMPLE_ID,
        "seed": SEED,
        "dtype": str(tensors["x"].dtype),
        "shapes": {name: tensor_shape(value) for name, value in tensors.items()},
        "values": {name: tensor_values(value) for name, value in tensors.items()},
        "gradients": {"x": tensor_values(tensors["x"].grad)},
        "resources": SPEC.to_dict(),
        "compute_seconds": compute_seconds,
    }
    result["stdout"] = format_output(result)
    return result


def format_output(result: dict[str, Any]) -> str:
    return "\n".join(
        (
            f"seed={result['seed']} dtype={result['dtype']} device=cpu",
            f"x shape={result['shapes']['x']} value={result['values']['x']}",
            f"w shape={result['shapes']['w']} value={result['values']['w']}",
            f"product shape={result['shapes']['product']} value={result['values']['product']}",
            f"output shape={result['shapes']['output']} value={result['values']['output']}",
            f"x.grad={result['gradients']['x']}",
        )
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = run_example()
    print(json.dumps(result, ensure_ascii=False) if args.json else result["stdout"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
