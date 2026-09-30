from __future__ import annotations

from labs.I08.common import emit


def momentum_path(gradients: list[float], beta: float = 0.8, learning_rate: float = 0.1) -> tuple[float, float]:
    theta = 0.0
    velocity = 0.0
    for gradient in gradients:
        velocity = beta * velocity + gradient
        theta -= learning_rate * velocity
    return theta, velocity


def run() -> dict[str, object]:
    gradients = [1.0, -0.5, 2.0, -1.5]
    forward_theta, forward_velocity = momentum_path(gradients)
    reverse_theta, reverse_velocity = momentum_path(list(reversed(gradients)))
    return {
        "gradient_multiset_equal": True,
        "forward_final_theta": forward_theta,
        "reverse_final_theta": reverse_theta,
        "forward_velocity": forward_velocity,
        "reverse_velocity": reverse_velocity,
        "order_changes_path": abs(forward_theta - reverse_theta) > 1e-9,
    }


if __name__ == "__main__":
    emit(run())
