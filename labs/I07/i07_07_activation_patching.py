from __future__ import annotations

import numpy as np

from labs.I07.common import emit


W_IN = np.array([[1.0, -0.5], [0.5, 1.0]])
W_OUT = np.array([1.2, -0.4])


def hidden(x: np.ndarray) -> np.ndarray:
    return np.tanh(W_IN @ x)


def score_from_hidden(h: np.ndarray) -> float:
    return float(W_OUT @ h)


def run() -> dict[str, object]:
    clean = np.array([2.0, 0.5])
    corrupted = np.array([-1.0, 0.5])
    clean_hidden = hidden(clean)
    corrupt_hidden = hidden(corrupted)
    clean_score = score_from_hidden(clean_hidden)
    corrupt_score = score_from_hidden(corrupt_hidden)
    patched_score = score_from_hidden(clean_hidden)
    recovery = (patched_score - corrupt_score) / (clean_score - corrupt_score)
    return {
        "clean_score": clean_score,
        "corrupt_score": corrupt_score,
        "patched_score": patched_score,
        "recovery_fraction": float(recovery),
        "patched_object": "full hidden vector",
    }


if __name__ == "__main__":
    emit(run())
