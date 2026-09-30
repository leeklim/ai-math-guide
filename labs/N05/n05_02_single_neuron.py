"""N05-02: compute one ReLU neuron and its gradients directly."""

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


EXAMPLE_ID = "n05_02_single_neuron"
SPEC = ResourceSpec(
    batch_size=1,
    sequence_length=1,
    model_dimension=2,
    transformer_layers=0,
    attention_heads=0,
    vocabulary_size=0,
    parameter_count=3,
    training_steps=0,
)


def compute() -> dict[str, torch.Tensor]:
    configure_runtime()
    assert_within_limits(SPEC)
    x = torch.tensor([2.0, -1.0], dtype=torch.float32, requires_grad=True)
    weight = torch.tensor([1.5, 0.5], dtype=torch.float32, requires_grad=True)
    bias = torch.tensor(-0.5, dtype=torch.float32, requires_grad=True)
    pre_activation = torch.dot(weight, x) + bias
    activation = torch.relu(pre_activation)
    loss = (activation - 1.0).square()
    loss.backward()
    return {
        "x": x,
        "weight": weight,
        "bias": bias,
        "pre_activation": pre_activation,
        "activation": activation,
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
            "x": tensor_values(tensors["x"].grad),
            "weight": tensor_values(tensors["weight"].grad),
            "bias": tensor_values(tensors["bias"].grad),
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
            f"pre_activation={result['values']['pre_activation']}",
            f"activation={result['values']['activation']}",
            f"loss={result['values']['loss']}",
            f"weight.grad={result['gradients']['weight']}",
            f"bias.grad={result['gradients']['bias']}",
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
