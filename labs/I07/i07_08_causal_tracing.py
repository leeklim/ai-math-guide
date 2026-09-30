from __future__ import annotations

import numpy as np

from labs.I07.common import emit


def run_model(tokens: np.ndarray, patch: tuple[int, int, float] | None = None) -> float:
    states = np.zeros((3, 2))
    states[0] = tokens
    states[1, 0] = states[0, 0]
    states[1, 1] = 0.5 * states[0, 0] + states[0, 1]
    states[2, 0] = states[1, 0]
    states[2, 1] = states[1].sum()
    if patch is not None:
        layer, token, value = patch
        states[layer, token] = value
        if layer <= 1:
            states[2, 0] = states[1, 0]
            states[2, 1] = states[1].sum()
    return float(states[2, 1])


def run() -> dict[str, object]:
    clean = np.array([2.0, 1.0])
    corrupt = np.array([-1.0, 1.0])
    clean_values = {(0, 0): 2.0, (0, 1): 1.0, (1, 0): 2.0, (1, 1): 2.0}
    clean_score = run_model(clean)
    corrupt_score = run_model(corrupt)
    recovery = np.zeros((2, 2))
    for (layer, token), value in clean_values.items():
        patched = run_model(corrupt, (layer, token, value))
        recovery[layer, token] = (patched - corrupt_score) / (clean_score - corrupt_score)
    best = np.unravel_index(int(np.argmax(recovery)), recovery.shape)
    return {
        "clean_score": clean_score,
        "corrupt_score": corrupt_score,
        "recovery_map": recovery.tolist(),
        "best_layer_token": [int(index) for index in best],
    }


if __name__ == "__main__":
    emit(run())
