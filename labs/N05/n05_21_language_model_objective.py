"""N05-21: compute a shifted next-token cross-entropy objective."""

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
from labs.N05.tiny_decoder import TinyDecoderLM, parameter_count


EXAMPLE_ID = "n05_21_language_model_objective"
SPEC = ResourceSpec(1, 4, 4, 1, 1, 16, 300, 0)


def compute() -> dict[str, torch.Tensor]:
    configure_runtime()
    assert_within_limits(SPEC)
    model = TinyDecoderLM()
    input_ids = torch.tensor([[1, 4, 2, 7]])
    logits, _, _ = model(input_ids)
    prediction_logits = logits[:, :-1, :]
    labels = input_ids[:, 1:]
    loss = functional.cross_entropy(
        prediction_logits.reshape(-1, model.config.vocabulary_size),
        labels.reshape(-1),
    )
    model.zero_grad(set_to_none=True)
    loss.backward()
    embedding_gradient_norm = model.embedding.weight.grad.norm()
    return {
        "input_ids": input_ids,
        "prediction_logits": prediction_logits,
        "labels": labels,
        "loss": loss,
        "embedding_gradient_norm": embedding_gradient_norm,
        "parameter_count": torch.tensor(parameter_count(model)),
    }


def run_example() -> dict[str, Any]:
    started = time.perf_counter()
    tensors = compute()
    result = {
        "example_id": EXAMPLE_ID,
        "seed": SEED,
        "dtype": str(tensors["prediction_logits"].dtype),
        "shapes": {name: tensor_shape(value) for name, value in tensors.items()},
        "values": {name: tensor_values(value) for name, value in tensors.items()},
        "gradients": {
            "embedding_norm": tensor_values(tensors["embedding_gradient_norm"])
        },
        "resources": SPEC.to_dict(),
        "compute_seconds": time.perf_counter() - started,
    }
    result["stdout"] = "\n".join(
        (
            f"seed={SEED} dtype={result['dtype']} device=cpu",
            f"input_ids={result['values']['input_ids']}",
            f"prediction_logits.shape={result['shapes']['prediction_logits']}",
            f"labels={result['values']['labels']}",
            f"mean_cross_entropy={result['values']['loss']}",
            f"embedding_gradient_norm={result['gradients']['embedding_norm']}",
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

