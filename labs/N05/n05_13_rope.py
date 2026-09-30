"""N05-13: rotate two-dimensional feature pairs with RoPE."""

from __future__ import annotations

import argparse
import json
import time
from typing import Any

import torch

from labs.N05.common import SEED, ResourceSpec, assert_within_limits, configure_runtime, tensor_shape, tensor_values


EXAMPLE_ID = "n05_13_rope"
SPEC = ResourceSpec(1, 2, 4, 0, 0, 0, 0, 0)


def apply_rope(vectors: torch.Tensor, positions: torch.Tensor) -> torch.Tensor:
    frequencies = torch.tensor([1.0, 0.01])
    angles = positions[:, None] * frequencies[None, :]
    pairs = vectors.reshape(vectors.shape[0], 2, 2)
    first, second = pairs[..., 0], pairs[..., 1]
    rotated = torch.stack((first * angles.cos() - second * angles.sin(), first * angles.sin() + second * angles.cos()), dim=-1)
    return rotated.reshape_as(vectors)


def compute() -> dict[str, torch.Tensor]:
    configure_runtime(); assert_within_limits(SPEC)
    vectors = torch.tensor([[1., 0., 0., 1.], [1., 0., 0., 1.]])
    positions = torch.tensor([0., 1.])
    rotated = apply_rope(vectors, positions)
    same_position = apply_rope(vectors, torch.tensor([1., 1.]))
    return {"vectors": vectors, "positions": positions, "rotated": rotated, "original_norms": torch.linalg.vector_norm(vectors, dim=-1), "rotated_norms": torch.linalg.vector_norm(rotated, dim=-1), "original_dot": vectors[0] @ vectors[1], "relative_dot": rotated[0] @ rotated[1], "same_position_dot": same_position[0] @ same_position[1]}


def run_example() -> dict[str, Any]:
    started = time.perf_counter(); tensors = compute()
    result = {"example_id": EXAMPLE_ID, "seed": SEED, "dtype": str(tensors["vectors"].dtype), "shapes": {name: tensor_shape(value) for name, value in tensors.items()}, "values": {name: tensor_values(value) for name, value in tensors.items()}, "gradients": {}, "resources": SPEC.to_dict(), "compute_seconds": time.perf_counter() - started}
    result["stdout"] = "\n".join((f"seed={SEED} dtype={result['dtype']} device=cpu", f"positions={result['values']['positions']}", f"rotated={result['values']['rotated']}", f"original_norms={result['values']['original_norms']} rotated_norms={result['values']['rotated_norms']}", f"original_dot={result['values']['original_dot']} relative_dot={result['values']['relative_dot']}", f"same_position_dot={result['values']['same_position_dot']}"))
    return result


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--json", action="store_true"); args = parser.parse_args()
    result = run_example(); print(json.dumps(result, ensure_ascii=False) if args.json else result["stdout"]); return 0


if __name__ == "__main__":
    raise SystemExit(main())
