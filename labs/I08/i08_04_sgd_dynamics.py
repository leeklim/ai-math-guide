from __future__ import annotations

import math

from labs.I08.common import emit


def run() -> dict[str, object]:
    learning_rate = 0.1
    steps = 20
    theta = 2.0
    trajectory = [theta]
    for _ in range(steps):
        theta -= learning_rate * theta
        trajectory.append(theta)
    flow = 2.0 * math.exp(-learning_rate * steps)
    return {
        "learning_rate": learning_rate,
        "steps": steps,
        "discrete_final": theta,
        "gradient_flow_at_matching_time": flow,
        "absolute_gap": abs(theta - flow),
        "loss_monotone": all(abs(trajectory[i + 1]) <= abs(trajectory[i]) for i in range(steps)),
    }


if __name__ == "__main__":
    emit(run())
