from __future__ import annotations

import unittest

import torch

from labs.N05 import n05_04_activation_gating as example
from labs.N05.common import ATOL, RTOL


class ActivationGatingTest(unittest.TestCase):
    def test_activation_values_and_local_gradients(self) -> None:
        tensors = example.compute()
        torch.testing.assert_close(
            tensors["relu"], torch.tensor([0.0, 0.0, 1.0]), rtol=RTOL, atol=ATOL
        )
        torch.testing.assert_close(
            tensors["sigmoid"],
            torch.tensor([0.26894143, 0.5, 0.73105860]),
            rtol=RTOL,
            atol=ATOL,
        )
        torch.testing.assert_close(
            tensors["gelu"],
            torch.tensor([-0.15865529, 0.0, 0.84134471]),
            rtol=RTOL,
            atol=ATOL,
        )
        torch.testing.assert_close(
            tensors["silu_gradient"],
            torch.tensor([0.07232948, 0.5, 0.92767054]),
            rtol=RTOL,
            atol=ATOL,
        )

    def test_gate_outputs_match_elementwise_products(self) -> None:
        tensors = example.compute()
        torch.testing.assert_close(
            tensors["glu_output"],
            torch.tensor([0.53788286, -0.5, 0.36552930]),
            rtol=RTOL,
            atol=ATOL,
        )
        torch.testing.assert_close(
            tensors["swiglu_output"],
            torch.tensor([-0.53788286, 0.0, 0.36552930]),
            rtol=RTOL,
            atol=ATOL,
        )


if __name__ == "__main__":
    unittest.main()
