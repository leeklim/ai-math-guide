from __future__ import annotations

import numpy as np

from labs.I07.common import emit, finite_difference


def score(x: np.ndarray) -> float:
    return float(x[0] * x[1] + x[2] ** 2)


def run() -> dict[str, object]:
    x = np.array([2.0, 3.0, 1.0])
    gradient = finite_difference(score, x)
    baseline = np.zeros_like(x)
    removal_effects = [score(x) - score(np.where(np.arange(3) == index, baseline, x)) for index in range(3)]
    return {
        "input": x.tolist(),
        "score": score(x),
        "local_gradient": gradient.tolist(),
        "zero_baseline_removal_effects": removal_effects,
        "same_ranking": list(np.argsort(-np.abs(gradient))) == list(np.argsort(-np.abs(removal_effects))),
    }


if __name__ == "__main__":
    emit(run())
