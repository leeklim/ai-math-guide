from __future__ import annotations

import numpy as np

from labs.I06.common import SEED, emit, representation_fixture


def run() -> dict[str, object]:
    x, labels = representation_fixture(n=20, d=6)
    direction = np.array([1.0, 0.5, 0.0, 0.0, 0.0, 0.0])
    direction /= np.linalg.norm(direction)
    scores = x @ direction
    top = np.argsort(scores)[-5:][::-1]
    bottom = np.argsort(scores)[:5]
    return {
        "seed": SEED,
        "top_indices": top.tolist(),
        "top_scores": scores[top].round(6).tolist(),
        "top_positive_label_fraction": float(labels[top].mean()),
        "bottom_indices": bottom.tolist(),
        "bottom_scores": scores[bottom].round(6).tolist(),
    }


if __name__ == "__main__":
    emit(run())
