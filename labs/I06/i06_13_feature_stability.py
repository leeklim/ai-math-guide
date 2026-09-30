from __future__ import annotations

import itertools

import numpy as np

from labs.I06.common import SEED, emit


def run() -> dict[str, object]:
    rng = np.random.default_rng(SEED)
    first = rng.normal(size=(7, 5))
    first /= np.linalg.norm(first, axis=0, keepdims=True)
    permutation = np.array([2, 4, 0, 1, 3])
    signs = np.array([1.0, -1.0, 1.0, -1.0, 1.0])
    second = first[:, permutation] * signs + rng.normal(scale=0.02, size=(7, 5))
    second /= np.linalg.norm(second, axis=0, keepdims=True)
    similarities = np.abs(first.T @ second)
    best_order = max(itertools.permutations(range(5)), key=lambda order: sum(similarities[i, order[i]] for i in range(5)))
    matched = np.array([similarities[i, best_order[i]] for i in range(5)])
    return {
        "naive_diagonal_similarity": float(np.diag(similarities).mean()),
        "matched_mean_similarity": float(matched.mean()),
        "matched_min_similarity": float(matched.min()),
        "matching": list(best_order),
    }


if __name__ == "__main__":
    emit(run())
