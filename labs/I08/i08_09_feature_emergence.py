from __future__ import annotations

import numpy as np

from labs.I08.common import emit


def first_crossing(values: np.ndarray, threshold: float) -> int | None:
    indices = np.flatnonzero(values >= threshold)
    return int(indices[0]) if len(indices) else None


def run() -> dict[str, object]:
    checkpoints = np.array([0, 1, 2, 3, 4, 5])
    recoverability = np.array([0.50, 0.52, 0.61, 0.86, 0.91, 0.93])
    ablation_effect = np.array([0.00, 0.01, 0.02, 0.03, 0.19, 0.24])
    behavior = np.array([0.48, 0.51, 0.55, 0.62, 0.81, 0.88])
    return {
        "checkpoints": checkpoints.tolist(),
        "recoverability": recoverability.tolist(),
        "ablation_effect": ablation_effect.tolist(),
        "behavior": behavior.tolist(),
        "recoverability_crossing": first_crossing(recoverability, 0.8),
        "use_crossing": first_crossing(ablation_effect, 0.1),
        "behavior_crossing": first_crossing(behavior, 0.8),
        "events_are_distinct": True,
    }


if __name__ == "__main__":
    emit(run())
