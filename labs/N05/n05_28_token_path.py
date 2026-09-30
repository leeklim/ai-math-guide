"""N05-28: trace one token from ID to logit, gradient, and KV cache."""

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


EXAMPLE_ID = "n05_28_token_path"
SPEC = ResourceSpec(1, 4, 4, 1, 1, 16, 300, 0)
TOKEN_INDEX = 2


def compute() -> dict[str, torch.Tensor]:
    configure_runtime()
    assert_within_limits(SPEC)
    model = TinyDecoderLM()
    model.eval()
    input_ids = torch.tensor([[1, 4, 2, 7]])
    logits, key_values, trace = model(input_ids)
    trace["embedding"].retain_grad()
    predicted_token = logits[0, TOKEN_INDEX].argmax()
    selected_logit = logits[0, TOKEN_INDEX, predicted_token]
    model.zero_grad(set_to_none=True)
    selected_logit.backward()
    embedding_gradient = trace["embedding"].grad[0, TOKEN_INDEX].detach().clone()

    with torch.no_grad():
        past_key_values = None
        incremental_logits = []
        for position in range(input_ids.shape[1]):
            step_logits, past_key_values, _ = model(
                input_ids[:, position : position + 1], past_key_values
            )
            incremental_logits.append(step_logits)
        cached_logits = torch.cat(incremental_logits, dim=1)

    return {
        "input_ids": input_ids,
        "selected_input_id": input_ids[0, TOKEN_INDEX],
        "embedding": trace["embedding"][0, TOKEN_INDEX].detach(),
        "attention_input": trace["block_0_attention_input"][0, TOKEN_INDEX].detach(),
        "attention_update": trace["block_0_attention_update"][0, TOKEN_INDEX].detach(),
        "residual_mid": trace["block_0_residual_mid"][0, TOKEN_INDEX].detach(),
        "mlp_input": trace["block_0_mlp_input"][0, TOKEN_INDEX].detach(),
        "mlp_update": trace["block_0_mlp_update"][0, TOKEN_INDEX].detach(),
        "residual_out": trace["block_0_residual_out"][0, TOKEN_INDEX].detach(),
        "final_norm": trace["final_norm"][0, TOKEN_INDEX].detach(),
        "logits": logits[0, TOKEN_INDEX].detach(),
        "predicted_token": predicted_token.detach(),
        "selected_logit": selected_logit.detach(),
        "embedding_gradient": embedding_gradient,
        "full_key_cache": key_values[0][0].detach(),
        "full_value_cache": key_values[0][1].detach(),
        "cached_logit_maximum_difference": (
            logits.detach() - cached_logits
        ).abs().max(),
        "parameter_count": torch.tensor(parameter_count(model)),
    }


def run_example() -> dict[str, Any]:
    started = time.perf_counter()
    tensors = compute()
    result = {
        "example_id": EXAMPLE_ID,
        "seed": SEED,
        "dtype": str(tensors["embedding"].dtype),
        "shapes": {name: tensor_shape(value) for name, value in tensors.items()},
        "values": {name: tensor_values(value) for name, value in tensors.items()},
        "gradients": {
            "embedding": tensor_values(tensors["embedding_gradient"])
        },
        "resources": SPEC.to_dict(),
        "compute_seconds": time.perf_counter() - started,
    }
    result["stdout"] = "\n".join(
        (
            f"seed={SEED} dtype={result['dtype']} device=cpu token_index={TOKEN_INDEX}",
            f"input_id={result['values']['selected_input_id']} embedding={result['values']['embedding']}",
            f"attention_update={result['values']['attention_update']}",
            f"residual_mid={result['values']['residual_mid']}",
            f"mlp_update={result['values']['mlp_update']}",
            f"residual_out={result['values']['residual_out']}",
            f"predicted_token={result['values']['predicted_token']} selected_logit={result['values']['selected_logit']}",
            f"d_selected_logit/d_embedding={result['gradients']['embedding']}",
            f"key_cache.shape={result['shapes']['full_key_cache']}",
            f"cached_logit_max_diff={result['values']['cached_logit_maximum_difference']}",
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
