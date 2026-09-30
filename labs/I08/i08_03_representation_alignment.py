from __future__ import annotations

import numpy as np

from labs.I08.common import SEED, emit, linear_cka


def run() -> dict[str, object]:
    rng = np.random.default_rng(SEED)
    x = rng.normal(size=(24, 3))
    q, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    y = x @ q
    u, _, vt = np.linalg.svd(y.T @ x)
    rotation = u @ vt
    aligned = y @ rotation
    return {
        "unaligned_rmse": float(np.sqrt(np.mean((x - y) ** 2))),
        "aligned_rmse": float(np.sqrt(np.mean((x - aligned) ** 2))),
        "linear_cka": linear_cka(x, y),
        "orthogonal_alignment": True,
    }


if __name__ == "__main__":
    emit(run())
