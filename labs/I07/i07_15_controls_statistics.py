from __future__ import annotations

import numpy as np

from labs.I07.common import SEED, emit


def run() -> dict[str, object]:
    rng = np.random.default_rng(SEED)
    treatment = np.array([0.42, 0.35, 0.51, 0.39, 0.46, 0.33, 0.48, 0.41])
    matched_control = np.array([0.08, 0.11, 0.05, 0.14, 0.07, 0.10, 0.09, 0.12])
    paired = treatment - matched_control
    bootstrap = np.array([
        rng.choice(paired, size=len(paired), replace=True).mean() for _ in range(2000)
    ])
    signs = rng.choice(np.array([-1.0, 1.0]), size=(4096, len(paired)))
    null_means = (signs * paired).mean(axis=1)
    p_value = float((np.sum(np.abs(null_means) >= abs(paired.mean())) + 1) / (len(null_means) + 1))
    return {
        "paired_effect_mean": float(paired.mean()),
        "bootstrap_95_interval": np.quantile(bootstrap, [0.025, 0.975]).tolist(),
        "sign_flip_p_value": p_value,
        "experimental_unit_count": len(paired),
        "paired_design": True,
    }


if __name__ == "__main__":
    emit(run())
