from __future__ import annotations

import json
from typing import Any, Callable

import numpy as np


SEED = 20261001


def finite_difference(function: Callable[[np.ndarray], float], x: np.ndarray, step: float = 1e-5) -> np.ndarray:
    gradient = np.zeros_like(x, dtype=float)
    for index in range(len(x)):
        offset = np.zeros_like(x, dtype=float)
        offset[index] = step
        gradient[index] = (function(x + offset) - function(x - offset)) / (2.0 * step)
    return gradient


def emit(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
