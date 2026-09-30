"""N05-07: take one mini-batch gradient-descent step."""

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


EXAMPLE_ID = "n05_07_minibatch_gradient_descent"
SPEC = ResourceSpec(
    batch_size=2,
    sequence_length=1,
    model_dimension=1,
    transformer_layers=0,
    attention_heads=0,
    vocabulary_size=0,
    parameter_count=2,
    training_steps=1,
)


def compute() -> dict[str, torch.Tensor]:
    configure_runtime()
    assert_within_limits(SPEC)
    inputs = torch.tensor([1.0, 2.0], dtype=torch.float32)
    targets = torch.tensor([3.0, 5.0], dtype=torch.float32)
    weight = torch.tensor(0.0, dtype=torch.float32, requires_grad=True)
    bias = torch.tensor(0.0, dtype=torch.float32, requires_grad=True)
    learning_rate = torch.tensor(0.1, dtype=torch.float32)

    predictions = weight * inputs + bias
    residuals = predictions - targets
    per_sample_losses = residuals.square()
    loss = per_sample_losses.mean()
    loss.backward()

    per_sample_weight_gradients = 2.0 * residuals.detach() * inputs
    per_sample_bias_gradients = 2.0 * residuals.detach()
    weight_gradient = weight.grad.detach().clone()
    bias_gradient = bias.grad.detach().clone()
    updated_weight = weight.detach() - learning_rate * weight_gradient
    updated_bias = bias.detach() - learning_rate * bias_gradient
    updated_predictions = updated_weight * inputs + updated_bias
    updated_loss = (updated_predictions - targets).square().mean()
    return {
        "inputs": inputs,
        "targets": targets,
        "weight": weight,
        "bias": bias,
        "learning_rate": learning_rate,
        "predictions": predictions,
        "residuals": residuals,
        "per_sample_losses": per_sample_losses,
        "loss": loss,
        "per_sample_weight_gradients": per_sample_weight_gradients,
        "per_sample_bias_gradients": per_sample_bias_gradients,
        "weight_gradient": weight_gradient,
        "bias_gradient": bias_gradient,
        "updated_weight": updated_weight,
        "updated_bias": updated_bias,
        "updated_predictions": updated_predictions,
        "updated_loss": updated_loss,
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
        "values": {name: tensor_values(value) for name, value in tensors.items()},
        "gradients": {
            "weight": tensor_values(tensors["weight_gradient"]),
            "bias": tensor_values(tensors["bias_gradient"]),
            "per_sample_weight": tensor_values(tensors["per_sample_weight_gradients"]),
            "per_sample_bias": tensor_values(tensors["per_sample_bias_gradients"]),
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
            f"predictions={result['values']['predictions']} targets={result['values']['targets']}",
            f"per_sample_losses={result['values']['per_sample_losses']} mean_loss={result['values']['loss']}",
            f"per_sample_weight_gradients={result['gradients']['per_sample_weight']}",
            f"weight.grad={result['gradients']['weight']} bias.grad={result['gradients']['bias']}",
            f"updated_weight={result['values']['updated_weight']} updated_bias={result['values']['updated_bias']}",
            f"updated_predictions={result['values']['updated_predictions']} updated_loss={result['values']['updated_loss']}",
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
