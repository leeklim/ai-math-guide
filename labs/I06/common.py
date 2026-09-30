from __future__ import annotations

import json
from typing import Any

import numpy as np


SEED = 20261001


def representation_fixture(n: int = 80, d: int = 8) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(SEED)
    labels = np.tile(np.array([0, 1]), n // 2)
    rng.shuffle(labels)
    latent = 2.0 * labels - 1.0
    x = rng.normal(0.0, 0.7, size=(n, d))
    x[:, 0] += 1.4 * latent
    x[:, 1] += 0.7 * latent
    return x, labels


def split_indices(n: int) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(SEED + 1)
    order = rng.permutation(n)
    cut = int(0.75 * n)
    return order[:cut], order[cut:]


def fit_linear_probe(x: np.ndarray, y: np.ndarray, ridge: float = 0.1) -> np.ndarray:
    design = np.column_stack([np.ones(len(x)), x])
    penalty = np.eye(design.shape[1]) * ridge
    penalty[0, 0] = 0.0
    target = 2.0 * y - 1.0
    return np.linalg.solve(design.T @ design + penalty, design.T @ target)


def probe_accuracy(weights: np.ndarray, x: np.ndarray, y: np.ndarray) -> float:
    design = np.column_stack([np.ones(len(x)), x])
    predictions = (design @ weights >= 0.0).astype(int)
    return float(np.mean(predictions == y))


def center(x: np.ndarray) -> np.ndarray:
    return x - x.mean(axis=0, keepdims=True)


def linear_cka(x: np.ndarray, y: np.ndarray) -> float:
    x_centered = center(x)
    y_centered = center(y)
    numerator = np.linalg.norm(x_centered.T @ y_centered, ord="fro") ** 2
    denominator = np.linalg.norm(x_centered.T @ x_centered, ord="fro")
    denominator *= np.linalg.norm(y_centered.T @ y_centered, ord="fro")
    return float(numerator / denominator)


def pairwise_distances(x: np.ndarray) -> np.ndarray:
    differences = x[:, None, :] - x[None, :, :]
    return np.sqrt(np.sum(differences * differences, axis=-1))


def rsa_correlation(x: np.ndarray, y: np.ndarray) -> float:
    upper = np.triu_indices(len(x), k=1)
    x_distances = pairwise_distances(x)[upper]
    y_distances = pairwise_distances(y)[upper]
    return float(np.corrcoef(x_distances, y_distances)[0, 1])


def emit(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
