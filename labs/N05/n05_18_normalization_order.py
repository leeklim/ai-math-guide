"""N05-18: compare LayerNorm, RMSNorm, pre-norm, and post-norm."""

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


EXAMPLE_ID = "n05_18_normalization_order"
SPEC = ResourceSpec(1, 2, 3, 1, 1, 0, 0, 0)
EPSILON = 1e-6


def layer_norm(x: torch.Tensor) -> torch.Tensor:
    mean = x.mean(dim=-1, keepdim=True)
    variance = ((x - mean) ** 2).mean(dim=-1, keepdim=True)
    return (x - mean) / torch.sqrt(variance + EPSILON)


def rms_norm(x: torch.Tensor) -> torch.Tensor:
    mean_square = (x**2).mean(dim=-1, keepdim=True)
    return x / torch.sqrt(mean_square + EPSILON)


def compute() -> dict[str, torch.Tensor]:
    configure_runtime()
    assert_within_limits(SPEC)
    residual = torch.tensor([[1.0, 2.0, 3.0], [-1.0, 0.0, 1.0]])
    normalized_layer = layer_norm(residual)
    normalized_rms = rms_norm(residual)

    def sublayer(x: torch.Tensor) -> torch.Tensor:
        return 0.5 * x

    pre_norm_output = residual + sublayer(normalized_rms)
    post_norm_output = rms_norm(residual + sublayer(residual))
    return {
        "residual": residual,
        "layer_norm": normalized_layer,
        "rms_norm": normalized_rms,
        "pre_norm_output": pre_norm_output,
        "post_norm_output": post_norm_output,
    }


def run_example() -> dict[str, Any]:
    started = time.perf_counter()
    tensors = compute()
    result = {
        "example_id": EXAMPLE_ID,
        "seed": SEED,
        "dtype": str(tensors["residual"].dtype),
        "shapes": {name: tensor_shape(value) for name, value in tensors.items()},
        "values": {name: tensor_values(value) for name, value in tensors.items()},
        "gradients": {},
        "resources": SPEC.to_dict(),
        "compute_seconds": time.perf_counter() - started,
    }
    result["stdout"] = "\n".join(
        (
            f"seed={SEED} dtype={result['dtype']} device=cpu epsilon={EPSILON}",
            f"input={result['values']['residual']}",
            f"LayerNorm={result['values']['layer_norm']}",
            f"RMSNorm={result['values']['rms_norm']}",
            f"pre_norm_output={result['values']['pre_norm_output']}",
            f"post_norm_output={result['values']['post_norm_output']}",
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

