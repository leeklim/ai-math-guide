from __future__ import annotations

from labs.I07.common import emit


def mediator(treatment: float) -> float:
    return 2.0 * treatment


def outcome(treatment: float, mediated: float) -> float:
    return treatment + 3.0 * mediated


def run() -> dict[str, object]:
    m0, m1 = mediator(0.0), mediator(1.0)
    y0 = outcome(0.0, m0)
    y1 = outcome(1.0, m1)
    direct = outcome(1.0, m0) - outcome(0.0, m0)
    indirect = outcome(1.0, m1) - outcome(1.0, m0)
    return {
        "total_effect": y1 - y0,
        "controlled_direct_effect": direct,
        "mediated_effect_at_treatment_1": indirect,
        "additive_decomposition_error": abs((direct + indirect) - (y1 - y0)),
    }


if __name__ == "__main__":
    emit(run())
