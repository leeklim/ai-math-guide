from __future__ import annotations

import numpy as np

from labs.I08.common import emit


def run() -> dict[str, object]:
    x = np.array([[-2.0], [-1.0], [0.0], [1.0], [2.0]])
    w_in_a = np.array([[1.0], [-2.0]])
    w_out_a = np.array([3.0, -1.0])
    permutation = np.array([1, 0])
    w_in_b = w_in_a[permutation]
    w_out_b = w_out_a[permutation]
    output_a = np.maximum(x @ w_in_a.T, 0.0) @ w_out_a
    output_b = np.maximum(x @ w_in_b.T, 0.0) @ w_out_b
    theta_a = np.concatenate([w_in_a.ravel(), w_out_a])
    theta_b = np.concatenate([w_in_b.ravel(), w_out_b])
    return {
        "parameter_l2": float(np.linalg.norm(theta_a - theta_b)),
        "function_rmse": float(np.sqrt(np.mean((output_a - output_b) ** 2))),
        "same_function_on_grid": bool(np.allclose(output_a, output_b)),
        "symmetry": "hidden-unit permutation",
    }


if __name__ == "__main__":
    emit(run())
