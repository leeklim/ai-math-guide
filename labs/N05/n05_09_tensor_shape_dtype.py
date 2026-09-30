"""N05-09: connect tensor shapes, broadcasting, dtype, and gradients."""

from __future__ import annotations

import argparse
import json
import time
from typing import Any

import torch

from labs.N05.common import SEED, ResourceSpec, assert_within_limits, configure_runtime, tensor_shape, tensor_values


EXAMPLE_ID = "n05_09_tensor_shape_dtype"
SPEC = ResourceSpec(2, 1, 3, 0, 0, 0, 8, 0)


def compute() -> dict[str, torch.Tensor]:
    configure_runtime()
    assert_within_limits(SPEC)
    inputs = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], requires_grad=True)
    weight = torch.tensor([[1.0, 0.0, -1.0], [0.5, 0.5, 0.5]])
    bias = torch.tensor([0.25, -0.5])
    affine = inputs @ weight.T + bias
    affine.sum().backward()
    expanded = inputs.detach().unsqueeze(1)
    cancellation32 = torch.tensor([1e8, 1.0, -1e8], dtype=torch.float32).sum()
    cancellation64 = torch.tensor([1e8, 1.0, -1e8], dtype=torch.float64).sum()
    return {
        "inputs": inputs,
        "weight": weight,
        "bias": bias,
        "affine": affine,
        "input_gradient": inputs.grad,
        "expanded": expanded,
        "cancellation32": cancellation32,
        "cancellation64": cancellation64,
    }


def run_example() -> dict[str, Any]:
    started = time.perf_counter()
    tensors = compute()
    result = {
        "example_id": EXAMPLE_ID,
        "seed": SEED,
        "dtype": str(tensors["inputs"].dtype),
        "shapes": {name: tensor_shape(value) for name, value in tensors.items()},
        "values": {name: tensor_values(value) for name, value in tensors.items()},
        "gradients": {"inputs": tensor_values(tensors["input_gradient"])},
        "resources": SPEC.to_dict(),
        "compute_seconds": time.perf_counter() - started,
    }
    result["stdout"] = format_output(result)
    return result


def format_output(result: dict[str, Any]) -> str:
    return "\n".join((
        f"seed={result['seed']} dtype={result['dtype']} device=cpu",
        f"inputs.shape={result['shapes']['inputs']} weight.shape={result['shapes']['weight']} bias.shape={result['shapes']['bias']}",
        f"affine.shape={result['shapes']['affine']} affine={result['values']['affine']}",
        f"inputs.grad={result['gradients']['inputs']}",
        f"unsqueeze shape={result['shapes']['expanded']}",
        f"float32 cancellation sum={result['values']['cancellation32']}",
        f"float64 cancellation sum={result['values']['cancellation64']}",
    ))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = run_example()
    print(json.dumps(result, ensure_ascii=False) if args.json else result["stdout"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
