"""N05-23: compare greedy, temperature, top-k, and top-p decoding."""

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


EXAMPLE_ID = "n05_23_decoding"
SPEC = ResourceSpec(1, 1, 4, 0, 1, 4, 0, 0)


def top_k_distribution(logits: torch.Tensor, k: int) -> torch.Tensor:
    threshold = torch.topk(logits, k).values[-1]
    filtered = logits.masked_fill(logits < threshold, float("-inf"))
    return torch.softmax(filtered, dim=-1)


def top_p_distribution(logits: torch.Tensor, probability_mass: float) -> torch.Tensor:
    sorted_logits, sorted_indices = torch.sort(logits, descending=True)
    sorted_probability = torch.softmax(sorted_logits, dim=-1)
    cumulative = sorted_probability.cumsum(dim=-1)
    remove = cumulative > probability_mass
    remove[1:] = remove[:-1].clone()
    remove[0] = False
    sorted_logits = sorted_logits.masked_fill(remove, float("-inf"))
    filtered = torch.full_like(logits, float("-inf"))
    filtered.scatter_(0, sorted_indices, sorted_logits)
    return torch.softmax(filtered, dim=-1)


def entropy(probability: torch.Tensor) -> torch.Tensor:
    positive = probability > 0
    return -(probability[positive] * probability[positive].log()).sum()


def compute() -> dict[str, torch.Tensor]:
    configure_runtime()
    assert_within_limits(SPEC)
    logits = torch.tensor([2.0, 1.5, 0.0, -1.0])
    probability = torch.softmax(logits, dim=-1)
    cold_probability = torch.softmax(logits / 0.5, dim=-1)
    hot_probability = torch.softmax(logits / 2.0, dim=-1)
    top_k_probability = top_k_distribution(logits, 2)
    top_p_probability = top_p_distribution(logits, 0.75)
    generator = torch.Generator().manual_seed(SEED)
    sampled_token = torch.multinomial(top_p_probability, 1, generator=generator)
    return {
        "logits": logits,
        "probability": probability,
        "greedy_token": logits.argmax().reshape(1),
        "cold_probability": cold_probability,
        "hot_probability": hot_probability,
        "temperature_entropy": torch.stack(
            (entropy(cold_probability), entropy(hot_probability))
        ),
        "top_k_probability": top_k_probability,
        "top_p_probability": top_p_probability,
        "sampled_token": sampled_token,
    }


def run_example() -> dict[str, Any]:
    started = time.perf_counter()
    tensors = compute()
    result = {
        "example_id": EXAMPLE_ID,
        "seed": SEED,
        "dtype": str(tensors["logits"].dtype),
        "shapes": {name: tensor_shape(value) for name, value in tensors.items()},
        "values": {name: tensor_values(value) for name, value in tensors.items()},
        "gradients": {},
        "resources": SPEC.to_dict(),
        "compute_seconds": time.perf_counter() - started,
    }
    result["stdout"] = "\n".join(
        (
            f"seed={SEED} dtype={result['dtype']} device=cpu",
            f"logits={result['values']['logits']}",
            f"softmax={result['values']['probability']}",
            f"greedy_token={result['values']['greedy_token']}",
            f"entropy temperature=0.5/2.0={result['values']['temperature_entropy']}",
            f"top_k_2={result['values']['top_k_probability']}",
            f"top_p_0.75={result['values']['top_p_probability']}",
            f"sampled_token={result['values']['sampled_token']}",
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

