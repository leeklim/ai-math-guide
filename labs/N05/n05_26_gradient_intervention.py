"""N05-26: collect an activation gradient and prepare a matched intervention."""

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
from labs.N05.tiny_decoder import TinyDecoderLM, parameter_count


EXAMPLE_ID = "n05_26_gradient_intervention"
SPEC = ResourceSpec(1, 4, 4, 1, 1, 16, 300, 0)
TOKEN_INDEX = 2
POSITIVE_TOKEN = 0
NEGATIVE_TOKEN = 1


def compute() -> dict[str, torch.Tensor]:
    configure_runtime()
    assert_within_limits(SPEC)
    model = TinyDecoderLM()
    model.eval()
    input_ids = torch.tensor([[1, 4, 2, 7]])
    capture: dict[str, torch.Tensor] = {}

    def retain_output(
        _module: torch.nn.Module,
        _inputs: tuple[torch.Tensor, ...],
        output: torch.Tensor,
    ) -> None:
        output.retain_grad()
        capture["output"] = output

    handle = model.blocks[0].mlp.down.register_forward_hook(retain_output)
    logits, _, _ = model(input_ids)
    target = (
        logits[0, TOKEN_INDEX, POSITIVE_TOKEN]
        - logits[0, TOKEN_INDEX, NEGATIVE_TOKEN]
    )
    model.zero_grad(set_to_none=True)
    target.backward()
    activation = capture["output"][0, TOKEN_INDEX].detach().clone()
    activation_gradient = capture["output"].grad[0, TOKEN_INDEX].detach().clone()
    handle.remove()

    def zero_selected_token(
        _module: torch.nn.Module,
        _inputs: tuple[torch.Tensor, ...],
        output: torch.Tensor,
    ) -> torch.Tensor:
        changed = output.clone()
        changed[0, TOKEN_INDEX] = 0
        return changed

    intervention_handle = model.blocks[0].mlp.down.register_forward_hook(
        zero_selected_token
    )
    with torch.no_grad():
        intervened_logits, _, _ = model(input_ids)
        intervened_target = (
            intervened_logits[0, TOKEN_INDEX, POSITIVE_TOKEN]
            - intervened_logits[0, TOKEN_INDEX, NEGATIVE_TOKEN]
        )
    intervention_handle.remove()

    perturbation = -activation
    first_order_change = activation_gradient @ perturbation
    actual_change = intervened_target - target.detach()
    return {
        "input_ids": input_ids,
        "activation": activation,
        "activation_gradient": activation_gradient,
        "baseline_target": target.detach(),
        "intervened_target": intervened_target,
        "perturbation": perturbation,
        "first_order_change": first_order_change,
        "actual_change": actual_change,
        "parameter_count": torch.tensor(parameter_count(model)),
    }


def run_example() -> dict[str, Any]:
    started = time.perf_counter()
    tensors = compute()
    result = {
        "example_id": EXAMPLE_ID,
        "seed": SEED,
        "dtype": str(tensors["activation"].dtype),
        "shapes": {name: tensor_shape(value) for name, value in tensors.items()},
        "values": {name: tensor_values(value) for name, value in tensors.items()},
        "gradients": {
            "selected_activation": tensor_values(tensors["activation_gradient"])
        },
        "resources": SPEC.to_dict(),
        "compute_seconds": time.perf_counter() - started,
    }
    result["stdout"] = "\n".join(
        (
            f"seed={SEED} dtype={result['dtype']} device=cpu",
            f"target=logit[{POSITIVE_TOKEN}]-logit[{NEGATIVE_TOKEN}] token_index={TOKEN_INDEX}",
            f"activation={result['values']['activation']}",
            f"activation_gradient={result['gradients']['selected_activation']}",
            f"baseline_target={result['values']['baseline_target']}",
            f"intervened_target={result['values']['intervened_target']}",
            f"first_order_change={result['values']['first_order_change']}",
            f"actual_change={result['values']['actual_change']}",
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

