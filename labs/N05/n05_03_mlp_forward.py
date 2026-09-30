"""N05-03: compute a two-layer MLP with explicit tensor operations."""

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


EXAMPLE_ID = "n05_03_mlp_forward"
SPEC = ResourceSpec(
    batch_size=2,
    sequence_length=1,
    model_dimension=3,
    transformer_layers=0,
    attention_heads=0,
    vocabulary_size=0,
    parameter_count=13,
    training_steps=0,
)


def compute() -> dict[str, torch.Tensor]:
    configure_runtime()
    assert_within_limits(SPEC)
    inputs = torch.tensor(
        [[1.0, 2.0], [-1.0, 3.0]], dtype=torch.float32, requires_grad=True
    )
    weight_1 = torch.tensor(
        [[1.0, 0.0], [0.0, 1.0], [1.0, -1.0]],
        dtype=torch.float32,
        requires_grad=True,
    )
    bias_1 = torch.tensor([0.5, -0.5, 0.0], dtype=torch.float32, requires_grad=True)
    weight_2 = torch.tensor([[2.0, -1.0, 0.5]], dtype=torch.float32, requires_grad=True)
    bias_2 = torch.tensor([0.25], dtype=torch.float32, requires_grad=True)

    pre_activation = inputs @ weight_1.T + bias_1
    hidden = torch.relu(pre_activation)
    output = hidden @ weight_2.T + bias_2
    loss = output.sum()
    loss.backward()
    return {
        "inputs": inputs,
        "weight_1": weight_1,
        "bias_1": bias_1,
        "pre_activation": pre_activation,
        "hidden": hidden,
        "weight_2": weight_2,
        "bias_2": bias_2,
        "output": output,
        "loss": loss,
    }


def run_example() -> dict[str, Any]:
    started = time.perf_counter()
    tensors = compute()
    compute_seconds = time.perf_counter() - started
    result = {
        "example_id": EXAMPLE_ID,
        "seed": SEED,
        "dtype": str(tensors["inputs"].dtype),
        "shapes": {name: tensor_shape(value) for name, value in tensors.items()},
        "values": {
            name: tensor_values(value)
            for name, value in tensors.items()
            if name in {"pre_activation", "hidden", "output", "loss"}
        },
        "gradients": {
            "inputs": tensor_values(tensors["inputs"].grad),
            "weight_1": tensor_values(tensors["weight_1"].grad),
            "bias_1": tensor_values(tensors["bias_1"].grad),
            "weight_2": tensor_values(tensors["weight_2"].grad),
            "bias_2": tensor_values(tensors["bias_2"].grad),
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
            f"pre_activation shape={result['shapes']['pre_activation']} value={result['values']['pre_activation']}",
            f"hidden shape={result['shapes']['hidden']} value={result['values']['hidden']}",
            f"output shape={result['shapes']['output']} value={result['values']['output']}",
            f"loss={result['values']['loss']}",
            f"weight_1.grad={result['gradients']['weight_1']}",
            f"weight_2.grad={result['gradients']['weight_2']}",
            f"inputs.grad={result['gradients']['inputs']}",
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
