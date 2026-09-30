from __future__ import annotations

from labs.I07.common import emit


def model(x: float, observed_h: float | None = None) -> tuple[float, float]:
    h = 2.0 * x if observed_h is None else observed_h
    return h, h + x


def run() -> dict[str, object]:
    h_one, y_one = model(1.0)
    h_two, y_two = model(2.0)
    _, intervened = model(2.0, observed_h=h_one)
    return {
        "observed": {"x1": [h_one, y_one], "x2": [h_two, y_two]},
        "do_h_from_x1_while_x_is_2": intervened,
        "observational_change": y_two - y_one,
        "intervention_effect_at_x2": intervened - y_two,
    }


if __name__ == "__main__":
    emit(run())
