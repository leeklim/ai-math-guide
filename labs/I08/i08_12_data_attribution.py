from __future__ import annotations

import numpy as np

from labs.I08.common import emit


def run() -> dict[str, object]:
    learning_rates = np.array([0.1, 0.05, 0.02])
    train_gradients = np.array([[1.0, 0.0], [0.5, 0.5], [-0.2, 1.0]])
    test_gradients = np.array([[0.8, 0.2], [0.4, 0.6], [0.1, 0.9]])
    contributions = learning_rates * np.sum(train_gradients * test_gradients, axis=1)
    return {
        "checkpoint_contributions": contributions.tolist(),
        "tracin_score": float(contributions.sum()),
        "all_helpful": bool(np.all(contributions > 0.0)),
        "requires_saved_checkpoints": True,
        "is_retraining_ground_truth": False,
    }


if __name__ == "__main__":
    emit(run())
