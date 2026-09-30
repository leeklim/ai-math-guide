from __future__ import annotations

from labs.I07.common import emit


def behavior(a: float, b: float) -> float:
    return max(a, b)


def run() -> dict[str, object]:
    intact = behavior(1.0, 1.0)
    ablate_a = behavior(0.0, 1.0)
    ablate_b = behavior(1.0, 0.0)
    ablate_both = behavior(0.0, 0.0)
    restore_a_only = behavior(1.0, 0.0)
    return {
        "intact": intact,
        "ablate_a": ablate_a,
        "ablate_b": ablate_b,
        "ablate_both": ablate_both,
        "restore_a_only": restore_a_only,
        "a_individually_necessary": ablate_a < intact,
        "a_sufficient_in_empty_baseline": restore_a_only == intact,
        "redundancy_present": ablate_a == intact and ablate_b == intact and ablate_both < intact,
    }


if __name__ == "__main__":
    emit(run())
