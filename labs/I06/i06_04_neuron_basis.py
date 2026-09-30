from __future__ import annotations

import numpy as np

from labs.I06.common import SEED, emit, pairwise_distances


def run() -> dict[str, object]:
    rng = np.random.default_rng(SEED)
    signal = rng.normal(size=60)
    activations = rng.normal(scale=0.25, size=(60, 4))
    activations[:, 0] += signal
    rotation, _ = np.linalg.qr(rng.normal(size=(4, 4)))
    rotated = activations @ rotation
    original_correlation = np.abs(np.corrcoef(activations.T, signal)[-1, :-1])
    rotated_correlation = np.abs(np.corrcoef(rotated.T, signal)[-1, :-1])
    distance_error = np.max(np.abs(pairwise_distances(activations) - pairwise_distances(rotated)))
    return {
        "original_best_coordinate": int(np.argmax(original_correlation)),
        "original_best_correlation": float(original_correlation.max()),
        "rotated_best_coordinate": int(np.argmax(rotated_correlation)),
        "rotated_best_correlation": float(rotated_correlation.max()),
        "pairwise_distance_max_error": float(distance_error),
    }


if __name__ == "__main__":
    emit(run())
