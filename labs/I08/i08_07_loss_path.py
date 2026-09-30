from __future__ import annotations

import numpy as np

from labs.I08.common import emit


def loss(points: np.ndarray) -> np.ndarray:
    return (np.sum(points**2, axis=1) - 1.0) ** 2


def run() -> dict[str, object]:
    alpha = np.linspace(0.0, 1.0, 101)
    straight = np.column_stack([1.0 - 2.0 * alpha, np.zeros_like(alpha)])
    angle = np.pi * alpha
    curved = np.column_stack([np.cos(angle), np.sin(angle)])
    return {
        "endpoint_loss": [float(loss(straight[[0]])[0]), float(loss(straight[[-1]])[0])],
        "straight_path_max_loss": float(loss(straight).max()),
        "curved_path_max_loss": float(loss(curved).max()),
        "same_endpoints": bool(np.allclose(straight[[0, -1]], curved[[0, -1]])),
    }


if __name__ == "__main__":
    emit(run())
