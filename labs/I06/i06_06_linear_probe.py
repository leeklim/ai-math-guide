from __future__ import annotations

from labs.I06.common import emit, fit_linear_probe, probe_accuracy, representation_fixture, split_indices


def run() -> dict[str, object]:
    x, labels = representation_fixture()
    train, test = split_indices(len(x))
    weights = fit_linear_probe(x[train], labels[train], ridge=0.1)
    return {
        "train_count": int(len(train)),
        "test_count": int(len(test)),
        "weight_shape": list(weights.shape),
        "train_accuracy": probe_accuracy(weights, x[train], labels[train]),
        "test_accuracy": probe_accuracy(weights, x[test], labels[test]),
    }


if __name__ == "__main__":
    emit(run())
