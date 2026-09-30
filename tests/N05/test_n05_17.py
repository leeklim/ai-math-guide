from __future__ import annotations

import unittest

import torch

from labs.N05 import n05_17_residual_stream as example
from labs.N05.common import ATOL, RTOL


class ResidualStreamTest(unittest.TestCase):
    def test_updates_are_added_to_the_same_stream(self) -> None:
        tensors = example.compute()
        torch.testing.assert_close(
            tensors["residual_mid"],
            tensors["residual_in"] + tensors["attention_update"],
            rtol=RTOL,
            atol=ATOL,
        )
        torch.testing.assert_close(
            tensors["residual_out"],
            tensors["residual_mid"] + tensors["mlp_update"],
            rtol=RTOL,
            atol=ATOL,
        )
        torch.testing.assert_close(
            tensors["residual_out"],
            torch.tensor([[1.375, -0.125], [3.0, 0.75]]),
            rtol=RTOL,
            atol=ATOL,
        )

    def test_gradient_contains_skip_and_sublayer_paths(self) -> None:
        tensors = example.compute()
        torch.testing.assert_close(
            tensors["input_gradient"],
            torch.tensor([[1.875, 0.625], [1.875, 0.625]]),
            rtol=RTOL,
            atol=ATOL,
        )


if __name__ == "__main__":
    unittest.main()

