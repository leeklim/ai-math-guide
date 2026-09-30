from __future__ import annotations

import numpy as np

from labs.I06.common import SEED, emit, linear_cka, rsa_correlation


def run() -> dict[str, object]:
    rng = np.random.default_rng(SEED)
    x = rng.normal(size=(48, 6))
    rotation, _ = np.linalg.qr(rng.normal(size=(6, 6)))
    aligned = x @ rotation + rng.normal(scale=0.03, size=x.shape)
    unrelated = rng.normal(size=(48, 9))
    return {
        "cka_aligned": linear_cka(x, aligned),
        "cka_unrelated": linear_cka(x, unrelated),
        "rsa_aligned": rsa_correlation(x, aligned),
        "rsa_unrelated": rsa_correlation(x, unrelated),
        "sample_count": len(x),
    }


if __name__ == "__main__":
    emit(run())
