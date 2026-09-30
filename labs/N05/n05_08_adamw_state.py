"""N05-08: compare momentum state with one explicit AdamW step."""

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


EXAMPLE_ID = "n05_08_adamw_state"
SPEC = ResourceSpec(
    batch_size=1,
    sequence_length=1,
    model_dimension=1,
    transformer_layers=0,
    attention_heads=0,
    vocabulary_size=0,
    parameter_count=1,
    training_steps=1,
)


def compute() -> dict[str, torch.Tensor]:
    configure_runtime()
    assert_within_limits(SPEC)
    parameter = torch.tensor(2.0, dtype=torch.float32, requires_grad=True)
    target = torch.tensor(0.5, dtype=torch.float32)
    learning_rate = torch.tensor(0.1, dtype=torch.float32)
    momentum_coefficient = torch.tensor(0.9, dtype=torch.float32)
    beta_1 = torch.tensor(0.9, dtype=torch.float32)
    beta_2 = torch.tensor(0.999, dtype=torch.float32)
    weight_decay = torch.tensor(0.01, dtype=torch.float32)
    epsilon = torch.tensor(1e-8, dtype=torch.float32)
    step = torch.tensor(1)

    loss = (parameter - target).square()
    loss.backward()
    gradient = parameter.grad.detach().clone()

    previous_momentum_buffer = torch.tensor(0.0)
    momentum_buffer = momentum_coefficient * previous_momentum_buffer + gradient
    momentum_parameter = parameter.detach() - learning_rate * momentum_buffer

    previous_first_moment = torch.tensor(0.0)
    previous_second_moment = torch.tensor(0.0)
    first_moment = beta_1 * previous_first_moment + (1.0 - beta_1) * gradient
    second_moment = beta_2 * previous_second_moment + (1.0 - beta_2) * gradient.square()
    corrected_first_moment = first_moment / (1.0 - beta_1.pow(step))
    corrected_second_moment = second_moment / (1.0 - beta_2.pow(step))
    adaptive_update = learning_rate * corrected_first_moment / (
        corrected_second_moment.sqrt() + epsilon
    )
    decay_update = learning_rate * weight_decay * parameter.detach()
    adamw_parameter = parameter.detach() - adaptive_update - decay_update
    return {
        "parameter": parameter,
        "target": target,
        "loss": loss,
        "gradient": gradient,
        "learning_rate": learning_rate,
        "momentum_coefficient": momentum_coefficient,
        "momentum_buffer": momentum_buffer,
        "momentum_parameter": momentum_parameter,
        "step": step,
        "first_moment": first_moment,
        "second_moment": second_moment,
        "corrected_first_moment": corrected_first_moment,
        "corrected_second_moment": corrected_second_moment,
        "adaptive_update": adaptive_update,
        "decay_update": decay_update,
        "adamw_parameter": adamw_parameter,
    }


def run_example() -> dict[str, Any]:
    started = time.perf_counter()
    tensors = compute()
    compute_seconds = time.perf_counter() - started
    result = {
        "example_id": EXAMPLE_ID,
        "seed": SEED,
        "dtype": str(tensors["parameter"].dtype),
        "shapes": {name: tensor_shape(value) for name, value in tensors.items()},
        "values": {name: tensor_values(value) for name, value in tensors.items()},
        "gradients": {"parameter": tensor_values(tensors["gradient"])},
        "resources": SPEC.to_dict(),
        "compute_seconds": compute_seconds,
    }
    result["stdout"] = format_output(result)
    return result


def format_output(result: dict[str, Any]) -> str:
    return "\n".join(
        (
            f"seed={result['seed']} dtype={result['dtype']} device=cpu",
            f"parameter={result['values']['parameter']} loss={result['values']['loss']} gradient={result['gradients']['parameter']}",
            f"momentum_buffer={result['values']['momentum_buffer']} momentum_parameter={result['values']['momentum_parameter']}",
            f"first_moment={result['values']['first_moment']} second_moment={result['values']['second_moment']}",
            f"corrected_first_moment={result['values']['corrected_first_moment']} corrected_second_moment={result['values']['corrected_second_moment']}",
            f"adaptive_update={result['values']['adaptive_update']} decay_update={result['values']['decay_update']}",
            f"adamw_parameter={result['values']['adamw_parameter']} step={result['values']['step']}",
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
