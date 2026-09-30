"""N05-10: compare a Jacobian with JVP and VJP products."""

from __future__ import annotations

import argparse
import json
import time
from typing import Any

import torch

from labs.N05.common import SEED, ResourceSpec, assert_within_limits, configure_runtime, tensor_shape, tensor_values


EXAMPLE_ID = "n05_10_jvp_vjp"
SPEC = ResourceSpec(1, 1, 2, 0, 0, 0, 0, 0)


def function(inputs: torch.Tensor) -> torch.Tensor:
    x_1, x_2 = inputs.unbind()
    return torch.stack((x_1 * x_2, x_1.square() + x_2))


def compute() -> dict[str, torch.Tensor]:
    configure_runtime()
    assert_within_limits(SPEC)
    inputs = torch.tensor([2.0, 3.0])
    tangent = torch.tensor([1.0, -1.0])
    cotangent = torch.tensor([2.0, -1.0])
    output, jvp = torch.func.jvp(function, (inputs,), (tangent,))
    _, vjp_function = torch.func.vjp(function, inputs)
    vjp = vjp_function(cotangent)[0]
    jacobian = torch.func.jacrev(function)(inputs)
    return {
        "inputs": inputs,
        "output": output,
        "jacobian": jacobian,
        "tangent": tangent,
        "jvp": jvp,
        "cotangent": cotangent,
        "vjp": vjp,
        "explicit_jvp": jacobian @ tangent,
        "explicit_vjp": cotangent @ jacobian,
    }


def run_example() -> dict[str, Any]:
    started = time.perf_counter()
    tensors = compute()
    result = {
        "example_id": EXAMPLE_ID,
        "seed": SEED,
        "dtype": str(tensors["inputs"].dtype),
        "shapes": {name: tensor_shape(value) for name, value in tensors.items()},
        "values": {name: tensor_values(value) for name, value in tensors.items()},
        "gradients": {"jvp": tensor_values(tensors["jvp"]), "vjp": tensor_values(tensors["vjp"])},
        "resources": SPEC.to_dict(),
        "compute_seconds": time.perf_counter() - started,
    }
    result["stdout"] = format_output(result)
    return result


def format_output(result: dict[str, Any]) -> str:
    return "\n".join((
        f"seed={result['seed']} dtype={result['dtype']} device=cpu",
        f"input={result['values']['inputs']} output={result['values']['output']}",
        f"jacobian={result['values']['jacobian']}",
        f"tangent={result['values']['tangent']} JVP={result['values']['jvp']}",
        f"cotangent={result['values']['cotangent']} VJP={result['values']['vjp']}",
        f"explicit_JVP={result['values']['explicit_jvp']} explicit_VJP={result['values']['explicit_vjp']}",
    ))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = run_example()
    print(json.dumps(result, ensure_ascii=False) if args.json else result["stdout"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
