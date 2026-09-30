from __future__ import annotations

import numpy as np

from labs.I07.common import emit


def run() -> dict[str, object]:
    components = {
        "embedding": np.array([1.0, 0.0, 0.5]),
        "attention": np.array([0.0, 1.5, -0.5]),
        "mlp": np.array([0.5, -0.5, 1.0]),
    }
    logit_direction = np.array([1.0, 2.0, -1.0])
    contributions = {name: float(value @ logit_direction) for name, value in components.items()}
    residual = sum(components.values())
    direct_logit = float(residual @ logit_direction)
    return {
        "component_contributions": contributions,
        "contribution_sum": float(sum(contributions.values())),
        "direct_logit": direct_logit,
        "decomposition_error": float(abs(sum(contributions.values()) - direct_logit)),
        "includes_final_nonlinearity": False,
    }


if __name__ == "__main__":
    emit(run())
