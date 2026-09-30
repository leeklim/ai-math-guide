from __future__ import annotations

import numpy as np

from labs.I06.common import emit


def run() -> dict[str, object]:
    angles = np.deg2rad([0.0, 120.0, 240.0])
    dictionary = np.stack([np.cos(angles), np.sin(angles)], axis=0)
    gram = dictionary.T @ dictionary
    coefficients = np.array([1.0, 0.0, 0.8])
    representation = dictionary @ coefficients
    decoded = dictionary.T @ representation
    return {
        "feature_count": 3,
        "representation_dimension": 2,
        "gram_matrix": gram.round(6).tolist(),
        "true_coefficients": coefficients.tolist(),
        "naive_dot_decoding": decoded.round(6).tolist(),
        "interference_l2": float(np.linalg.norm(decoded - coefficients)),
    }


if __name__ == "__main__":
    emit(run())
