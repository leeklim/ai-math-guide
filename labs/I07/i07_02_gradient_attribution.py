from __future__ import annotations

import torch

from labs.I07.common import emit


def run() -> dict[str, object]:
    x = torch.tensor([2.0, 3.0, 1.0], requires_grad=True)
    score = x[0] * x[1] + x[2].square()
    score.backward()
    gradient = x.grad.detach()
    gradient_times_input = gradient * x.detach()
    return {
        "score": float(score.detach()),
        "gradient": gradient.tolist(),
        "gradient_times_input": gradient_times_input.tolist(),
        "gradient_times_input_sum": float(gradient_times_input.sum()),
    }


if __name__ == "__main__":
    emit(run())
