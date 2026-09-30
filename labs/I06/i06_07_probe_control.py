from __future__ import annotations

import numpy as np

from labs.I06.common import SEED, emit, fit_linear_probe, probe_accuracy, representation_fixture, split_indices


def run() -> dict[str, object]:
    x, labels = representation_fixture()
    train, test = split_indices(len(x))
    real_probe = fit_linear_probe(x[train], labels[train], ridge=0.1)
    real_accuracy = probe_accuracy(real_probe, x[test], labels[test])
    shuffled = labels.copy()
    np.random.default_rng(SEED + 2).shuffle(shuffled)
    control_probe = fit_linear_probe(x[train], shuffled[train], ridge=0.1)
    control_accuracy = probe_accuracy(control_probe, x[test], shuffled[test])
    return {
        "real_test_accuracy": real_accuracy,
        "control_test_accuracy": control_accuracy,
        "selectivity": real_accuracy - control_accuracy,
        "same_probe_dimension": len(real_probe) == len(control_probe),
    }


if __name__ == "__main__":
    emit(run())
