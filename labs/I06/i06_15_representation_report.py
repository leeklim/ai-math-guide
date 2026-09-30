from __future__ import annotations

import numpy as np

from labs.I06.common import (
    SEED,
    emit,
    fit_linear_probe,
    linear_cka,
    probe_accuracy,
    representation_fixture,
    split_indices,
)


def run() -> dict[str, object]:
    x, labels = representation_fixture()
    train, test = split_indices(len(x))
    probe = fit_linear_probe(x[train], labels[train])
    test_accuracy = probe_accuracy(probe, x[test], labels[test])
    shuffled = labels.copy()
    np.random.default_rng(SEED + 3).shuffle(shuffled)
    control = fit_linear_probe(x[train], shuffled[train])
    control_accuracy = probe_accuracy(control, x[test], shuffled[test])
    rotation, _ = np.linalg.qr(np.random.default_rng(SEED + 4).normal(size=(x.shape[1], x.shape[1])))
    condition_difference = x[labels == 1].mean(axis=0) - x[labels == 0].mean(axis=0)
    return {
        "data": {"samples": len(x), "dimension": x.shape[1], "train": len(train), "test": len(test)},
        "statistics": {"condition_mean_difference_l2": float(np.linalg.norm(condition_difference))},
        "probe": {"test_accuracy": test_accuracy, "control_accuracy": control_accuracy, "selectivity": test_accuracy - control_accuracy},
        "stability": {"orthogonal_rotation_cka": linear_cka(x, x @ rotation)},
        "claim": "the label is linearly recoverable in this synthetic held-out sample; use and causality were not tested",
    }


if __name__ == "__main__":
    emit(run())
