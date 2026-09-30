"""N05-27: distinguish model, buffer, optimizer, and training-step state."""

from __future__ import annotations

import argparse
import copy
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


EXAMPLE_ID = "n05_27_checkpoint_state"
SPEC = ResourceSpec(1, 4, 4, 1, 1, 16, 300, 1)


def compute() -> dict[str, torch.Tensor]:
    configure_runtime()
    assert_within_limits(SPEC)
    model = TinyDecoderLM()
    optimizer = torch.optim.AdamW(model.parameters(), lr=0.01, weight_decay=0.0)
    input_ids = torch.tensor([[1, 4, 2, 7]])
    embedding_before = model.embedding.weight.detach().clone()

    logits, _, _ = model(input_ids)
    loss = functional.cross_entropy(
        logits[:, :-1].reshape(-1, model.config.vocabulary_size),
        input_ids[:, 1:].reshape(-1),
    )
    optimizer.zero_grad(set_to_none=True)
    loss.backward()
    optimizer.step()

    model_state = copy.deepcopy(model.state_dict())
    optimizer_state = copy.deepcopy(optimizer.state_dict())
    model.eval()
    with torch.no_grad():
        reference_logits, _, _ = model(input_ids)

    reloaded_model = TinyDecoderLM()
    load_result = reloaded_model.load_state_dict(model_state, strict=True)
    reloaded_model.eval()
    with torch.no_grad():
        reloaded_logits, _, _ = reloaded_model(input_ids)

    first_optimizer_state = next(iter(optimizer_state["state"].values()))
    return {
        "loss_before_step": loss.detach(),
        "embedding_update_norm": (
            model.embedding.weight.detach() - embedding_before
        ).norm(),
        "model_state_entries": torch.tensor(len(model_state)),
        "parameter_entries": torch.tensor(len(list(model.named_parameters()))),
        "buffer_entries": torch.tensor(len(list(model.named_buffers()))),
        "optimizer_parameter_states": torch.tensor(len(optimizer_state["state"])),
        "optimizer_slots_per_parameter": torch.tensor(len(first_optimizer_state)),
        "optimizer_step": first_optimizer_state["step"].detach().clone(),
        "missing_keys": torch.tensor(len(load_result.missing_keys)),
        "unexpected_keys": torch.tensor(len(load_result.unexpected_keys)),
        "maximum_reload_difference": (
            reference_logits - reloaded_logits
        ).abs().max(),
        "training_step": torch.tensor(1),
        "parameter_count": torch.tensor(parameter_count(model)),
    }


def run_example() -> dict[str, Any]:
    started = time.perf_counter()
    tensors = compute()
    result = {
        "example_id": EXAMPLE_ID,
        "seed": SEED,
        "dtype": str(tensors["loss_before_step"].dtype),
        "shapes": {name: tensor_shape(value) for name, value in tensors.items()},
        "values": {name: tensor_values(value) for name, value in tensors.items()},
        "gradients": {},
        "resources": SPEC.to_dict(),
        "compute_seconds": time.perf_counter() - started,
    }
    result["stdout"] = "\n".join(
        (
            f"seed={SEED} dtype={result['dtype']} device=cpu",
            f"training_step={result['values']['training_step']}",
            f"model_state_entries={result['values']['model_state_entries']}",
            f"parameter_entries={result['values']['parameter_entries']} buffer_entries={result['values']['buffer_entries']}",
            f"optimizer_parameter_states={result['values']['optimizer_parameter_states']}",
            f"optimizer_slots_per_parameter={result['values']['optimizer_slots_per_parameter']}",
            f"embedding_update_norm={result['values']['embedding_update_norm']}",
            f"max_reload_difference={result['values']['maximum_reload_difference']}",
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

