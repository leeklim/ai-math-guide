from __future__ import annotations

import unittest

import torch

from labs.N05 import n05_07_minibatch_gradient_descent as example
from labs.N05.common import ATOL, RTOL


class MinibatchGradientDescentTest(unittest.TestCase):
    def test_batch_mean_matches_mean_of_per_sample_gradients(self) -> None:
        tensors = example.compute()
        torch.testing.assert_close(
            tensors["per_sample_weight_gradients"],
            torch.tensor([-6.0, -20.0]),
            rtol=RTOL,
            atol=ATOL,
        )
        torch.testing.assert_close(
            tensors["per_sample_bias_gradients"],
            torch.tensor([-6.0, -10.0]),
            rtol=RTOL,
            atol=ATOL,
        )
        torch.testing.assert_close(
            tensors["weight_gradient"],
            tensors["per_sample_weight_gradients"].mean(),
            rtol=RTOL,
            atol=ATOL,
        )
        torch.testing.assert_close(
            tensors["bias_gradient"],
            tensors["per_sample_bias_gradients"].mean(),
            rtol=RTOL,
            atol=ATOL,
        )

    def test_one_update_reduces_this_batch_loss(self) -> None:
        tensors = example.compute()
        torch.testing.assert_close(tensors["loss"], torch.tensor(17.0), rtol=RTOL, atol=ATOL)
        torch.testing.assert_close(
            tensors["updated_weight"], torch.tensor(1.3), rtol=RTOL, atol=ATOL
        )
        torch.testing.assert_close(
            tensors["updated_bias"], torch.tensor(0.8), rtol=RTOL, atol=ATOL
        )
        torch.testing.assert_close(
            tensors["updated_loss"], torch.tensor(1.685), rtol=RTOL, atol=ATOL
        )
        self.assertLess(tensors["updated_loss"].item(), tensors["loss"].item())


if __name__ == "__main__":
    unittest.main()
