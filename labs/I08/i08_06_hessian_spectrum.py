from __future__ import annotations

import numpy as np

from labs.I08.common import emit


def run() -> dict[str, object]:
    hessian = np.diag([4.0, 1.0, -0.5])
    eigenvalues = np.linalg.eigvalsh(hessian)
    vector = np.array([1.0, 2.0, -1.0])
    hvp = hessian @ vector
    rayleigh = float(vector @ hvp / (vector @ vector))
    return {
        "eigenvalues": eigenvalues.tolist(),
        "largest_eigenvalue": float(eigenvalues[-1]),
        "negative_curvature_present": bool(eigenvalues[0] < 0.0),
        "hessian_vector_product": hvp.tolist(),
        "rayleigh_quotient": rayleigh,
    }


if __name__ == "__main__":
    emit(run())
