"""N05-25: collect one token activation with a removable forward hook."""

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


EXAMPLE_ID = "n05_25_activation_hook"
SPEC = ResourceSpec(1, 4, 4, 1, 1, 16, 300, 0)


def compute() -> dict[str, torch.Tensor]:
    configure_runtime()
    assert_within_limits(SPEC)
    model = TinyDecoderLM()
    model.eval()
    input_ids = torch.tensor([[1, 4, 2, 7]])
    captures: list[torch.Tensor] = []
    full_shapes: list[tuple[int, ...]] = []

    def capture_token(
        _module: torch.nn.Module,
        _inputs: tuple[torch.Tensor, ...],
        output: torch.Tensor,
    ) -> None:
        full_shapes.append(tuple(output.shape))
        captures.append(output[0, 2].detach().cpu().clone())

    handle = model.blocks[0].mlp.down.register_forward_hook(capture_token)
    with torch.no_grad():
        logits_with_hook, _, _ = model(input_ids)
    calls_before_removal = len(captures)
    handle.remove()
    with torch.no_grad():
        logits_after_removal, _, _ = model(input_ids)

    selected = captures[0]
    return {
        "input_ids": input_ids,
        "logits_with_hook": logits_with_hook,
        "logits_after_removal": logits_after_removal,
        "selected_activation": selected,
        "hook_output_shape": torch.tensor(full_shapes[0]),
        "calls_before_removal": torch.tensor(calls_before_removal),
        "calls_after_removal": torch.tensor(len(captures)),
        "selected_bytes": torch.tensor(selected.numel() * selected.element_size()),
        "selected_requires_grad": torch.tensor(selected.requires_grad),
        "parameter_count": torch.tensor(parameter_count(model)),
    }


def run_example() -> dict[str, Any]:
    started = time.perf_counter()
    tensors = compute()
    result = {
        "example_id": EXAMPLE_ID,
        "seed": SEED,
        "dtype": str(tensors["selected_activation"].dtype),
        "shapes": {name: tensor_shape(value) for name, value in tensors.items()},
        "values": {name: tensor_values(value) for name, value in tensors.items()},
        "gradients": {},
        "resources": SPEC.to_dict(),
        "compute_seconds": time.perf_counter() - started,
    }
    result["stdout"] = "\n".join(
        (
            f"seed={SEED} dtype={result['dtype']} device=cpu",
            "module=blocks.0.mlp.down token_index=2",
            f"hook_output_shape={result['values']['hook_output_shape']}",
            f"selected_activation={result['values']['selected_activation']}",
            f"selected_bytes={result['values']['selected_bytes']}",
            f"calls_before/after_removal={result['values']['calls_before_removal']}/{result['values']['calls_after_removal']}",
            f"selected_requires_grad={result['values']['selected_requires_grad']}",
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
