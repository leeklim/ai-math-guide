"""N05-12: map token IDs to embeddings and hidden states to logits."""

from __future__ import annotations

import argparse
import json
import time
from typing import Any

import torch
import torch.nn.functional as F

from labs.N05.common import SEED, ResourceSpec, assert_within_limits, configure_runtime, tensor_shape, tensor_values


EXAMPLE_ID = "n05_12_embedding_unembedding"
SPEC = ResourceSpec(1, 2, 3, 0, 0, 4, 28, 0)


def compute() -> dict[str, torch.Tensor]:
    configure_runtime(); assert_within_limits(SPEC)
    token_ids = torch.tensor([0, 2])
    targets = torch.tensor([1, 3])
    embedding = torch.tensor([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.], [1., 1., 0.]], requires_grad=True)
    unembedding = torch.tensor([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.], [-1., .5, .5]], requires_grad=True)
    bias = torch.zeros(4, requires_grad=True)
    hidden = embedding[token_ids]
    logits = hidden @ unembedding.T + bias
    probabilities = torch.softmax(logits, dim=-1)
    loss = F.cross_entropy(logits, targets)
    loss.backward()
    return {"token_ids": token_ids, "targets": targets, "embedding": embedding, "unembedding": unembedding, "bias": bias, "hidden": hidden, "logits": logits, "probabilities": probabilities, "loss": loss}


def run_example() -> dict[str, Any]:
    started = time.perf_counter(); tensors = compute()
    result = {"example_id": EXAMPLE_ID, "seed": SEED, "dtype": str(tensors["embedding"].dtype), "shapes": {name: tensor_shape(value) for name, value in tensors.items()}, "values": {name: tensor_values(value) for name, value in tensors.items()}, "gradients": {"embedding": tensor_values(tensors["embedding"].grad), "unembedding": tensor_values(tensors["unembedding"].grad), "bias": tensor_values(tensors["bias"].grad)}, "resources": SPEC.to_dict(), "compute_seconds": time.perf_counter() - started}
    result["stdout"] = "\n".join((f"seed={SEED} dtype={result['dtype']} device=cpu", f"token_ids={result['values']['token_ids']} hidden={result['values']['hidden']}", f"logits={result['values']['logits']}", f"probabilities={result['values']['probabilities']}", f"loss={result['values']['loss']}", f"embedding.grad={result['gradients']['embedding']}"))
    return result


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--json", action="store_true"); args = parser.parse_args()
    result = run_example(); print(json.dumps(result, ensure_ascii=False) if args.json else result["stdout"]); return 0


if __name__ == "__main__":
    raise SystemExit(main())
