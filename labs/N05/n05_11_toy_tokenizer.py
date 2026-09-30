"""N05-11: tokenize and decode a sentence with a fixed toy vocabulary."""

from __future__ import annotations

import argparse
import json
import time
from typing import Any

import torch

from labs.N05.common import SEED, ResourceSpec, assert_within_limits, configure_runtime, tensor_shape, tensor_values


EXAMPLE_ID = "n05_11_toy_tokenizer"
SPEC = ResourceSpec(1, 6, 1, 0, 0, 7, 0, 0)
VOCABULARY = {"<unk>": 0, "<bos>": 1, "<eos>": 2, "deep": 3, "learn": 4, "ing": 5, "math": 6}
ID_TO_TOKEN = {index: token for token, index in VOCABULARY.items()}


def tokenize(text: str) -> list[str]:
    pieces: list[str] = ["<bos>"]
    for word in text.lower().split():
        if word == "learning":
            pieces.extend(("learn", "ing"))
        elif word in VOCABULARY:
            pieces.append(word)
        else:
            pieces.append("<unk>")
    pieces.append("<eos>")
    return pieces


def decode(token_ids: list[int]) -> str:
    words: list[str] = []
    for token_id in token_ids:
        token = ID_TO_TOKEN[token_id]
        if token in {"<bos>", "<eos>"}:
            continue
        if token == "ing" and words:
            words[-1] += token
        else:
            words.append(token)
    return " ".join(words)


def compute(text: str = "deep learning math") -> dict[str, Any]:
    configure_runtime()
    assert_within_limits(SPEC)
    tokens = tokenize(text)
    token_ids = torch.tensor([VOCABULARY[token] for token in tokens], dtype=torch.long)
    attention_mask = torch.ones_like(token_ids)
    return {"text": text, "tokens": tokens, "token_ids": token_ids, "attention_mask": attention_mask, "decoded": decode(token_ids.tolist())}


def run_example() -> dict[str, Any]:
    started = time.perf_counter()
    values = compute()
    result = {
        "example_id": EXAMPLE_ID, "seed": SEED, "dtype": str(values["token_ids"].dtype),
        "shapes": {name: tensor_shape(values[name]) for name in ("token_ids", "attention_mask")},
        "values": {"text": values["text"], "tokens": values["tokens"], "token_ids": tensor_values(values["token_ids"]), "attention_mask": tensor_values(values["attention_mask"]), "decoded": values["decoded"]},
        "gradients": {}, "resources": SPEC.to_dict(), "compute_seconds": time.perf_counter() - started,
    }
    result["stdout"] = "\n".join((f"seed={SEED} dtype={result['dtype']} device=cpu", f"text={values['text']}", f"tokens={values['tokens']}", f"token_ids={result['values']['token_ids']}", f"attention_mask={result['values']['attention_mask']}", f"decoded={values['decoded']}"))
    return result


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--json", action="store_true"); args = parser.parse_args()
    result = run_example(); print(json.dumps(result, ensure_ascii=False) if args.json else result["stdout"]); return 0


if __name__ == "__main__":
    raise SystemExit(main())
