from __future__ import annotations

import numpy as np

from labs.I06.common import SEED, emit


def soft_threshold(x: np.ndarray, threshold: float) -> np.ndarray:
    return np.sign(x) * np.maximum(np.abs(x) - threshold, 0.0)


def run() -> dict[str, object]:
    rng = np.random.default_rng(SEED)
    dictionary = rng.normal(size=(5, 8))
    dictionary /= np.linalg.norm(dictionary, axis=0, keepdims=True)
    true_codes = np.zeros((24, 8))
    for row in true_codes:
        indices = rng.choice(8, size=2, replace=False)
        row[indices] = rng.normal(size=2)
    x = true_codes @ dictionary.T
    codes = np.zeros_like(true_codes)
    step = 1.0 / np.linalg.norm(dictionary, ord=2) ** 2
    penalty = 0.03
    for _ in range(100):
        gradient = (codes @ dictionary.T - x) @ dictionary
        codes = soft_threshold(codes - step * gradient, step * penalty)
    reconstruction = codes @ dictionary.T
    return {
        "reconstruction_mse": float(np.mean((x - reconstruction) ** 2)),
        "active_fraction": float(np.mean(np.abs(codes) > 1e-3)),
        "true_active_fraction": float(np.mean(true_codes != 0.0)),
        "objective": float(0.5 * np.mean((x - reconstruction) ** 2) + penalty * np.mean(np.abs(codes))),
    }


if __name__ == "__main__":
    emit(run())
