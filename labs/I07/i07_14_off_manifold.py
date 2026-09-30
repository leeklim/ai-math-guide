from __future__ import annotations

import numpy as np

from labs.I07.common import emit


def downstream(hidden: np.ndarray) -> float:
    return float(hidden[0] + hidden[1] + 4.0 * hidden[0] * hidden[1])


def distance_to_manifold(hidden: np.ndarray) -> float:
    return float(abs(hidden[0] - hidden[1]) / np.sqrt(2.0))


def run() -> dict[str, object]:
    clean = np.array([1.0, 1.0])
    valid_counterfactual = np.array([-1.0, -1.0])
    coordinate_patch = np.array([1.0, -1.0])
    return {
        "clean_output": downstream(clean),
        "valid_counterfactual_output": downstream(valid_counterfactual),
        "coordinate_patch_output": downstream(coordinate_patch),
        "clean_distance_to_manifold": distance_to_manifold(clean),
        "patch_distance_to_manifold": distance_to_manifold(coordinate_patch),
    }


if __name__ == "__main__":
    emit(run())
