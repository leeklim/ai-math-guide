"""N05-20: assemble and trace the instructional tiny decoder block."""

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


EXAMPLE_ID = "n05_20_decoder_block"
SPEC = ResourceSpec(1, 3, 4, 1, 1, 16, 300, 0)


def compute() -> dict[str, torch.Tensor]:
    configure_runtime()
    assert_within_limits(SPEC)
    model = TinyDecoderLM()
    input_ids = torch.tensor([[1, 4, 2]])
    logits, key_values, trace = model(input_ids)
    shape_table = torch.tensor(
        [
            trace["embedding"].shape[-1],
            trace["block_0_attention_update"].shape[-1],
            trace["block_0_mlp_update"].shape[-1],
            logits.shape[-1],
        ]
    )
    return {
        "input_ids": input_ids,
        "embedding": trace["embedding"],
        "attention_update": trace["block_0_attention_update"],
        "residual_mid": trace["block_0_residual_mid"],
        "mlp_update": trace["block_0_mlp_update"],
        "residual_out": trace["block_0_residual_out"],
        "logits": logits,
        "key_cache": key_values[0][0],
        "value_cache": key_values[0][1],
        "shape_table": shape_table,
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
        "gradients": {},
        "resources": SPEC.to_dict(),
        "compute_seconds": time.perf_counter() - started,
    }
    result["stdout"] = "\n".join(
        (
            f"seed={SEED} dtype={result['dtype']} device=cpu",
            f"input_ids.shape={result['shapes']['input_ids']}",
            f"embedding.shape={result['shapes']['embedding']}",
            f"attention_update.shape={result['shapes']['attention_update']}",
            f"mlp_update.shape={result['shapes']['mlp_update']}",
            f"logits.shape={result['shapes']['logits']}",
            f"key_cache.shape={result['shapes']['key_cache']}",
            f"parameter_count={result['values']['parameter_count']}",
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

