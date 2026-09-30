"""N05-14: project hidden states into query, key, and value tensors."""

from __future__ import annotations

import argparse
import json
import time
from typing import Any

import torch

from labs.N05.common import SEED, ResourceSpec, assert_within_limits, configure_runtime, tensor_shape, tensor_values


EXAMPLE_ID = "n05_14_qkv"
SPEC = ResourceSpec(1, 2, 2, 0, 1, 0, 12, 0)


def compute() -> dict[str, torch.Tensor]:
    configure_runtime(); assert_within_limits(SPEC)
    hidden = torch.tensor([[1., 2.], [3., 4.]])
    weight_q = torch.eye(2)
    weight_k = torch.tensor([[1., 1.], [1., -1.]])
    weight_v = torch.tensor([[2., 0.], [0., .5]])
    query = hidden @ weight_q.T
    key = hidden @ weight_k.T
    value = hidden @ weight_v.T
    scores = query @ key.T
    return {"hidden": hidden, "weight_q": weight_q, "weight_k": weight_k, "weight_v": weight_v, "query": query, "key": key, "value": value, "scores": scores}


def run_example() -> dict[str, Any]:
    started = time.perf_counter(); tensors = compute()
    result = {"example_id": EXAMPLE_ID, "seed": SEED, "dtype": str(tensors["hidden"].dtype), "shapes": {name: tensor_shape(value) for name, value in tensors.items()}, "values": {name: tensor_values(value) for name, value in tensors.items()}, "gradients": {}, "resources": SPEC.to_dict(), "compute_seconds": time.perf_counter() - started}
    result["stdout"] = "\n".join((f"seed={SEED} dtype={result['dtype']} device=cpu", f"hidden={result['values']['hidden']}", f"query={result['values']['query']}", f"key={result['values']['key']}", f"value={result['values']['value']}", f"raw_scores={result['values']['scores']}"))
    return result


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--json", action="store_true"); args = parser.parse_args(); result = run_example(); print(json.dumps(result, ensure_ascii=False) if args.json else result["stdout"]); return 0


if __name__ == "__main__": raise SystemExit(main())
