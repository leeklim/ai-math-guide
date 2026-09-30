"""N05-19: compare dense SwiGLU computation with top-1 expert routing."""

from __future__ import annotations

import argparse
import json
import time
from typing import Any

import torch
import torch.nn.functional as functional

from labs.N05.common import (
    SEED,
    ResourceSpec,
    assert_within_limits,
    configure_runtime,
    tensor_shape,
    tensor_values,
)


EXAMPLE_ID = "n05_19_mlp_routing"
SPEC = ResourceSpec(1, 3, 2, 1, 1, 0, 32, 0)


def compute() -> dict[str, torch.Tensor]:
    configure_runtime()
    assert_within_limits(SPEC)
    tokens = torch.tensor([[2.0, -1.0], [-1.0, 2.0], [1.0, 1.0]])

    gate_weight = torch.tensor([[1.0, 0.0], [0.0, 1.0]])
    up_weight = torch.tensor([[1.0, 1.0], [1.0, -1.0]])
    down_weight = torch.tensor([[1.0, 0.5], [-0.5, 1.0]])
    gate = functional.silu(tokens @ gate_weight.T)
    up = tokens @ up_weight.T
    swiglu_hidden = gate * up
    dense_output = swiglu_hidden @ down_weight.T

    router_weight = torch.tensor([[1.0, 0.0], [0.0, 1.0]])
    router_logits = tokens @ router_weight.T
    router_probability = torch.softmax(router_logits, dim=-1)
    selected_expert = router_probability.argmax(dim=-1)
    expert_weights = torch.stack((torch.eye(2), -torch.eye(2)))
    expert_candidates = torch.einsum("td,edh->teh", tokens, expert_weights)
    selected_output = expert_candidates[
        torch.arange(tokens.shape[0]), selected_expert
    ]
    selected_probability = router_probability.gather(
        1, selected_expert.unsqueeze(1)
    )
    routed_output = selected_probability * selected_output

    return {
        "tokens": tokens,
        "swiglu_hidden": swiglu_hidden,
        "dense_output": dense_output,
        "router_logits": router_logits,
        "router_probability": router_probability,
        "selected_expert": selected_expert,
        "selected_output": selected_output,
        "routed_output": routed_output,
    }


def run_example() -> dict[str, Any]:
    started = time.perf_counter()
    tensors = compute()
    result = {
        "example_id": EXAMPLE_ID,
        "seed": SEED,
        "dtype": str(tensors["tokens"].dtype),
        "shapes": {name: tensor_shape(value) for name, value in tensors.items()},
        "values": {name: tensor_values(value) for name, value in tensors.items()},
        "gradients": {},
        "resources": SPEC.to_dict(),
        "compute_seconds": time.perf_counter() - started,
    }
    result["stdout"] = "\n".join(
        (
            f"seed={SEED} dtype={result['dtype']} device=cpu",
            f"tokens={result['values']['tokens']}",
            f"SwiGLU hidden={result['values']['swiglu_hidden']}",
            f"dense output={result['values']['dense_output']}",
            f"router probability={result['values']['router_probability']}",
            f"selected expert={result['values']['selected_expert']}",
            f"routed output={result['values']['routed_output']}",
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
