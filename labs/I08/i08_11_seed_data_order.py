from __future__ import annotations

import numpy as np

from labs.I08.common import SEED, emit


def run() -> dict[str, object]:
    rng = np.random.default_rng(SEED)
    seed_effect = rng.normal(0.0, 0.03, size=8)
    method_effect = 0.08 + rng.normal(0.0, 0.01, size=8)
    baseline = 0.70 + seed_effect
    treatment = baseline + method_effect
    paired = treatment - baseline
    unpaired_standard_error = float(np.sqrt(baseline.var(ddof=1) / 8 + treatment.var(ddof=1) / 8))
    paired_standard_error = float(paired.std(ddof=1) / np.sqrt(8))
    return {
        "seed_count": 8,
        "paired_effect_mean": float(paired.mean()),
        "paired_standard_error": paired_standard_error,
        "unpaired_standard_error": unpaired_standard_error,
        "paired_is_more_precise": paired_standard_error < unpaired_standard_error,
        "seed_and_data_order_must_be_recorded": True,
    }


if __name__ == "__main__":
    emit(run())
