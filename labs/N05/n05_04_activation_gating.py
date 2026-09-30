"""N05-04: compare activation functions and explicit gates."""

from __future__ import annotations

import argparse
import json
import time
from typing import Any

import torch
import torch.nn.functional as F

from labs.N05.common import (
    SEED,
    ResourceSpec,
    assert_within_limits,
    configure_runtime,
    tensor_shape,
    tensor_values,
)


EXAMPLE_ID = "n05_04_activation_gating"
SPEC = ResourceSpec(
    batch_size=1,
    sequence_length=3,
    model_dimension=3,
    transformer_layers=0,
    attention_heads=0,
    vocabulary_size=0,
    parameter_count=0,
    training_steps=0,
)


def compute() -> dict[str, torch.Tensor]:
    configure_runtime()
    assert_within_limits(SPEC)
    inputs = torch.tensor([-1.0, 0.0, 1.0], dtype=torch.float32, requires_grad=True)

    relu = torch.relu(inputs)
    sigmoid = torch.sigmoid(inputs)
    gelu = F.gelu(inputs)
    silu = F.silu(inputs)
    relu_gradient = torch.autograd.grad(relu.sum(), inputs, retain_graph=True)[0]
    sigmoid_gradient = torch.autograd.grad(sigmoid.sum(), inputs, retain_graph=True)[0]
    gelu_gradient = torch.autograd.grad(gelu.sum(), inputs, retain_graph=True)[0]
    silu_gradient = torch.autograd.grad(silu.sum(), inputs)[0]

    content = torch.tensor([2.0, -1.0, 0.5], dtype=torch.float32)
    gate_pre_activation = torch.tensor([-1.0, 0.0, 1.0], dtype=torch.float32)
    sigmoid_gate = torch.sigmoid(gate_pre_activation)
    glu_output = content * sigmoid_gate
    silu_gate = F.silu(gate_pre_activation)
    swiglu_output = content * silu_gate

    return {
        "inputs": inputs,
        "relu": relu,
        "sigmoid": sigmoid,
        "gelu": gelu,
        "silu": silu,
        "relu_gradient": relu_gradient,
        "sigmoid_gradient": sigmoid_gradient,
        "gelu_gradient": gelu_gradient,
        "silu_gradient": silu_gradient,
        "content": content,
        "gate_pre_activation": gate_pre_activation,
        "sigmoid_gate": sigmoid_gate,
        "glu_output": glu_output,
        "silu_gate": silu_gate,
        "swiglu_output": swiglu_output,
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
            name: tensor_values(tensors[name])
            for name in (
                "relu_gradient",
                "sigmoid_gradient",
                "gelu_gradient",
                "silu_gradient",
            )
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
            f"input={result['values']['inputs']}",
            f"relu={result['values']['relu']} grad={result['gradients']['relu_gradient']}",
            f"sigmoid={result['values']['sigmoid']} grad={result['gradients']['sigmoid_gradient']}",
            f"gelu={result['values']['gelu']} grad={result['gradients']['gelu_gradient']}",
            f"silu={result['values']['silu']} grad={result['gradients']['silu_gradient']}",
            f"glu_output={result['values']['glu_output']}",
            f"swiglu_output={result['values']['swiglu_output']}",
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
