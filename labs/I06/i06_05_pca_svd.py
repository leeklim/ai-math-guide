from __future__ import annotations

import numpy as np

from labs.I06.common import SEED, emit


def run() -> dict[str, object]:
    rng = np.random.default_rng(SEED)
    latent = rng.normal(size=(40, 2))
    mixing = rng.normal(size=(2, 6))
    x = latent @ mixing + rng.normal(scale=0.05, size=(40, 6))
    centered = x - x.mean(axis=0, keepdims=True)
    u, singular_values, vt = np.linalg.svd(centered, full_matrices=False)
    rank_two = (u[:, :2] * singular_values[:2]) @ vt[:2]
    explained = singular_values**2 / np.sum(singular_values**2)
    return {
        "shape": list(x.shape),
        "singular_values": singular_values.round(6).tolist(),
        "top_two_explained_variance": float(explained[:2].sum()),
        "rank_two_relative_error": float(np.linalg.norm(centered - rank_two) / np.linalg.norm(centered)),
    }


if __name__ == "__main__":
    emit(run())
