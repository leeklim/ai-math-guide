"""N05-06: trace backpropagation through a scalar computation graph."""

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


EXAMPLE_ID = "n05_06_backpropagation"
SPEC = ResourceSpec(
    batch_size=1,
    sequence_length=1,
    model_dimension=1,
    transformer_layers=0,
    attention_heads=0,
    vocabulary_size=0,
    parameter_count=4,
    training_steps=0,
)


def compute() -> dict[str, torch.Tensor]:
    configure_runtime()
    assert_within_limits(SPEC)
    x = torch.tensor(2.0, dtype=torch.float32, requires_grad=True)
    w = torch.tensor(1.0, dtype=torch.float32, requires_grad=True)
    b = torch.tensor(-1.0, dtype=torch.float32, requires_grad=True)
    v = torch.tensor(3.0, dtype=torch.float32, requires_grad=True)
    c = torch.tensor(0.0, dtype=torch.float32, requires_grad=True)
    target = torch.tensor(1.0, dtype=torch.float32)

    z = w * x + b
    h = z.square()
    prediction = v * h + c
    loss = (prediction - target).square()
    z.retain_grad()
    h.retain_grad()
    prediction.retain_grad()
    loss.backward()
    return {
        "x": x,
        "w": w,
        "b": b,
        "v": v,
        "c": c,
        "target": target,
        "z": z,
        "h": h,
        "prediction": prediction,
        "loss": loss,
    }


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
        "gradients": {
            name: tensor_values(tensors[name].grad)
            for name in ("prediction", "h", "z", "x", "w", "b", "v", "c")
        },
        "resources": SPEC.to_dict(),
        "compute_seconds": compute_seconds,
    }
    result["stdout"] = format_output(result)
    return result


def format_output(result: dict[str, Any]) -> str:
    return "\n".join(
        (
            f"seed={result['seed']} dtype={result['dtype']} device=cpu",
            f"z={result['values']['z']} h={result['values']['h']}",
            f"prediction={result['values']['prediction']} loss={result['values']['loss']}",
            f"prediction.grad={result['gradients']['prediction']}",
            f"h.grad={result['gradients']['h']} z.grad={result['gradients']['z']}",
            f"w.grad={result['gradients']['w']} b.grad={result['gradients']['b']}",
            f"x.grad={result['gradients']['x']} v.grad={result['gradients']['v']} c.grad={result['gradients']['c']}",
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
