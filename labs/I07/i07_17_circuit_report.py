from __future__ import annotations

import numpy as np

from labs.I07.common import SEED, emit


def circuit(x: np.ndarray, keep_copy: bool = True, keep_gate: bool = True) -> np.ndarray:
    copy_path = x[:, 0] if keep_copy else np.zeros(len(x))
    gate_path = x[:, 0] * x[:, 1] if keep_gate else np.zeros(len(x))
    return copy_path + gate_path


def run() -> dict[str, object]:
    rng = np.random.default_rng(SEED)
    x = rng.choice(np.array([-1.0, 1.0]), size=(64, 2))
    intact = circuit(x)
    without_copy = circuit(x, keep_copy=False)
    without_gate = circuit(x, keep_gate=False)
    without_both = circuit(x, keep_copy=False, keep_gate=False)
    copy_effect = np.abs(intact - without_copy)
    gate_effect = np.abs(intact - without_gate)
    joint_effect = np.abs(intact - without_both)
    random_control = np.abs(intact - circuit(x[:, ::-1], keep_copy=False))
    return {
        "behavior": "signed score from copy and gated paths",
        "experimental_units": len(x),
        "nodes": ["input_0", "input_1", "copy_path", "gate_path", "output"],
        "mean_copy_ablation_effect": float(copy_effect.mean()),
        "mean_gate_ablation_effect": float(gate_effect.mean()),
        "mean_joint_ablation_effect": float(joint_effect.mean()),
        "mean_random_control_effect": float(random_control.mean()),
        "complete_for_defined_graph": bool(np.allclose(intact, (intact - without_gate) + (intact - without_copy))),
        "claim": "two specified paths are causally implicated in this synthetic behavior",
    }


if __name__ == "__main__":
    emit(run())
