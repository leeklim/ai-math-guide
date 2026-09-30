from __future__ import annotations

import numpy as np

from labs.I07.common import emit


def output(components: np.ndarray) -> float:
    return float(components[0] + components[1] + 0.2 * components[2])


def run() -> dict[str, object]:
    samples = np.array([[1.0, 1.0, 1.0], [1.0, 0.8, -1.0], [0.7, 1.0, 0.5]])
    intact = np.array([output(row) for row in samples])
    effects = []
    for index in range(samples.shape[1]):
        ablated = samples.copy()
        ablated[:, index] = 0.0
        effects.append(float(np.mean(intact - np.array([output(row) for row in ablated]))))
    joint = samples.copy()
    joint[:, :2] = 0.0
    joint_effect = float(np.mean(intact - np.array([output(row) for row in joint])))
    return {
        "mean_single_component_effects": effects,
        "joint_effect_first_two": joint_effect,
        "single_effect_sum": effects[0] + effects[1],
        "same_baseline_used": True,
    }


if __name__ == "__main__":
    emit(run())
