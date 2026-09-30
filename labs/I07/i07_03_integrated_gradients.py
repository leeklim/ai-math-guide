from __future__ import annotations

import torch

from labs.I07.common import emit


def integrated_gradients(x: torch.Tensor, baseline: torch.Tensor, steps: int = 200) -> torch.Tensor:
    total = torch.zeros_like(x)
    for alpha in torch.linspace(0.0, 1.0, steps):
        point = (baseline + alpha * (x - baseline)).detach().requires_grad_(True)
        score = point[0] * point[1] + point[2].square()
        total += torch.autograd.grad(score, point)[0]
    return (x - baseline) * total / steps


def run() -> dict[str, object]:
    x = torch.tensor([2.0, 3.0, 1.0])
    zero = torch.zeros(3)
    one = torch.ones(3)
    ig_zero = integrated_gradients(x, zero)
    ig_one = integrated_gradients(x, one)
    score = lambda value: value[0] * value[1] + value[2].square()
    return {
        "zero_baseline_attribution": ig_zero.tolist(),
        "zero_completeness_error": float(abs(ig_zero.sum() - (score(x) - score(zero)))),
        "one_baseline_attribution": ig_one.tolist(),
        "one_completeness_error": float(abs(ig_one.sum() - (score(x) - score(one)))),
        "baseline_changes_attribution": bool(not torch.allclose(ig_zero, ig_one)),
    }


if __name__ == "__main__":
    emit(run())
