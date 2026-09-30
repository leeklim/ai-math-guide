"""N05-05: compute stable softmax and cross-entropy from logits."""

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


EXAMPLE_ID = "n05_05_softmax_cross_entropy"
SPEC = ResourceSpec(
    batch_size=1,
    sequence_length=1,
    model_dimension=3,
    transformer_layers=0,
    attention_heads=0,
    vocabulary_size=3,
    parameter_count=0,
    training_steps=0,
)


def compute() -> dict[str, torch.Tensor]:
    configure_runtime()
    assert_within_limits(SPEC)
    logits = torch.tensor([2.0, 1.0, 0.0], dtype=torch.float32, requires_grad=True)
    shifted_logits = logits - logits.max().detach()
    exponentials = torch.exp(shifted_logits)
    partition = exponentials.sum()
    probabilities = exponentials / partition
    target = torch.tensor(0)
    loss = -torch.log(probabilities[target])
    loss.backward()
    translated_probabilities = torch.softmax(logits.detach() + 100.0, dim=0)
    return {
        "logits": logits,
        "shifted_logits": shifted_logits,
        "exponentials": exponentials,
        "partition": partition,
        "probabilities": probabilities,
        "target": target,
        "loss": loss,
        "logit_gradient": logits.grad,
        "translated_probabilities": translated_probabilities,
    }


def run_example() -> dict[str, Any]:
    started = time.perf_counter()
    tensors = compute()
    compute_seconds = time.perf_counter() - started
    result = {
        "example_id": EXAMPLE_ID,
        "seed": SEED,
        "dtype": str(tensors["logits"].dtype),
        "shapes": {name: tensor_shape(value) for name, value in tensors.items()},
        "values": {name: tensor_values(value) for name, value in tensors.items()},
        "gradients": {"logits": tensor_values(tensors["logit_gradient"])},
        "resources": SPEC.to_dict(),
        "compute_seconds": compute_seconds,
    }
    result["stdout"] = format_output(result)
    return result


def format_output(result: dict[str, Any]) -> str:
    return "\n".join(
        (
            f"seed={result['seed']} dtype={result['dtype']} device=cpu",
            f"logits={result['values']['logits']}",
            f"shifted_logits={result['values']['shifted_logits']}",
            f"probabilities={result['values']['probabilities']}",
            f"cross_entropy={result['values']['loss']}",
            f"logits.grad={result['gradients']['logits']}",
            f"softmax(logits + 100)={result['values']['translated_probabilities']}",
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
