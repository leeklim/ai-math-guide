from __future__ import annotations

import numpy as np

from labs.I07.common import emit


def score(x: np.ndarray) -> float:
    return float(1.5 * x[0] + x[0] * x[1] + 0.25 * x[2] ** 2)


def effects(x: np.ndarray, baseline: np.ndarray) -> np.ndarray:
    output = score(x)
    values = []
    for index in range(len(x)):
        perturbed = x.copy()
        perturbed[index] = baseline[index]
        values.append(output - score(perturbed))
    return np.array(values)


def run() -> dict[str, object]:
    x = np.array([2.0, 3.0, 1.0])
    zero_effects = effects(x, np.zeros(3))
    mean_effects = effects(x, np.array([1.0, 1.0, 1.0]))
    return {
        "score": score(x),
        "zero_baseline_effects": zero_effects.tolist(),
        "mean_baseline_effects": mean_effects.tolist(),
        "baseline_changes_effect": bool(not np.allclose(zero_effects, mean_effects)),
    }


if __name__ == "__main__":
    emit(run())
