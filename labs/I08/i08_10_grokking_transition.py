from __future__ import annotations

import numpy as np

from labs.I08.common import emit


def run() -> dict[str, object]:
    steps = np.array([0, 100, 200, 400, 800, 1200, 1600])
    train_accuracy = np.array([0.10, 0.72, 0.99, 1.00, 1.00, 1.00, 1.00])
    test_accuracy = np.array([0.10, 0.12, 0.14, 0.18, 0.31, 0.79, 0.97])
    overfit_step = int(steps[np.flatnonzero(train_accuracy >= 0.99)[0]])
    generalization_step = int(steps[np.flatnonzero(test_accuracy >= 0.90)[0]])
    return {
        "steps": steps.tolist(),
        "train_accuracy": train_accuracy.tolist(),
        "test_accuracy": test_accuracy.tolist(),
        "overfit_step": overfit_step,
        "generalization_step": generalization_step,
        "delay_steps": generalization_step - overfit_step,
        "sampling_can_change_apparent_abruptness": True,
    }


if __name__ == "__main__":
    emit(run())
