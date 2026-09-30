from __future__ import annotations

import numpy as np

from labs.I08.common import emit


def ridge_fit(x: np.ndarray, y: np.ndarray, regularization: float) -> float:
    return float((x @ y) / (x @ x + len(x) * regularization))


def run() -> dict[str, object]:
    x = np.array([-2.0, -1.0, 1.0, 2.0, 3.0])
    y = np.array([-4.1, -1.8, 2.2, 3.9, 8.5])
    regularization = 0.2
    theta = ridge_fit(x, y, regularization)
    hessian = float(np.mean(x**2) + regularization)
    approximate = []
    exact = []
    for index in range(len(x)):
        gradient = (theta * x[index] - y[index]) * x[index]
        approximate.append(float(gradient / ((len(x) - 1) * hessian)))
        keep = np.arange(len(x)) != index
        exact.append(ridge_fit(x[keep], y[keep], regularization) - theta)
    correlation = float(np.corrcoef(approximate, exact)[0, 1])
    return {
        "theta": theta,
        "hessian": hessian,
        "approximate_leave_one_out_change": approximate,
        "exact_leave_one_out_change": exact,
        "rank_correlation_proxy": correlation,
        "local_approximation": True,
    }


if __name__ == "__main__":
    emit(run())
