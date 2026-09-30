"""N05-17: trace two updates through a residual stream."""

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


EXAMPLE_ID = "n05_17_residual_stream"
SPEC = ResourceSpec(1, 2, 2, 1, 1, 0, 8, 0)


def compute() -> dict[str, torch.Tensor]:
    configure_runtime()
    assert_within_limits(SPEC)
    residual_in = torch.tensor([[1.0, -1.0], [2.0, 0.0]], requires_grad=True)
    attention_weight = torch.tensor([[0.5, 0.0], [0.0, -0.5]])
    mlp_weight = torch.tensor([[0.0, 0.25], [0.25, 0.0]])

    attention_update = residual_in @ attention_weight.T
    residual_mid = residual_in + attention_update
    mlp_update = residual_mid @ mlp_weight.T
    residual_out = residual_mid + mlp_update
    loss = residual_out.sum()
    (input_gradient,) = torch.autograd.grad(loss, residual_in)

    return {
        "residual_in": residual_in,
        "attention_update": attention_update,
        "residual_mid": residual_mid,
        "mlp_update": mlp_update,
        "residual_out": residual_out,
        "input_gradient": input_gradient,
    }


def run_example() -> dict[str, Any]:
    started = time.perf_counter()
    tensors = compute()
    result = {
        "example_id": EXAMPLE_ID,
        "seed": SEED,
        "dtype": str(tensors["residual_in"].dtype),
        "shapes": {name: tensor_shape(value) for name, value in tensors.items()},
        "values": {name: tensor_values(value) for name, value in tensors.items()},
        "gradients": {"residual_in": tensor_values(tensors["input_gradient"])},
        "resources": SPEC.to_dict(),
        "compute_seconds": time.perf_counter() - started,
    }
    result["stdout"] = "\n".join(
        (
            f"seed={SEED} dtype={result['dtype']} device=cpu",
            f"residual_in={result['values']['residual_in']}",
            f"attention_update={result['values']['attention_update']}",
            f"residual_mid={result['values']['residual_mid']}",
            f"mlp_update={result['values']['mlp_update']}",
            f"residual_out={result['values']['residual_out']}",
            f"d_loss/d_residual_in={result['gradients']['residual_in']}",
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

