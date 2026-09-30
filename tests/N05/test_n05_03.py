from __future__ import annotations

import unittest

import torch

from labs.N05 import n05_03_mlp_forward as example
from labs.N05.common import ATOL, RTOL


class MlpForwardTest(unittest.TestCase):
    def test_forward_shapes_and_values(self) -> None:
        tensors = example.compute()
        self.assertEqual(tensors["inputs"].shape, torch.Size([2, 2]))
        self.assertEqual(tensors["pre_activation"].shape, torch.Size([2, 3]))
        self.assertEqual(tensors["hidden"].shape, torch.Size([2, 3]))
        self.assertEqual(tensors["output"].shape, torch.Size([2, 1]))
        self.assertEqual(tensors["inputs"].dtype, torch.float32)
        torch.testing.assert_close(
            tensors["pre_activation"],
            torch.tensor([[1.5, 1.5, -1.0], [-0.5, 2.5, -4.0]]),
            rtol=RTOL,
            atol=ATOL,
        )
        torch.testing.assert_close(
            tensors["hidden"],
            torch.tensor([[1.5, 1.5, 0.0], [0.0, 2.5, 0.0]]),
            rtol=RTOL,
            atol=ATOL,
        )
        torch.testing.assert_close(
            tensors["output"], torch.tensor([[1.75], [-2.25]]), rtol=RTOL, atol=ATOL
        )

    def test_gradients_match_hand_calculation(self) -> None:
        tensors = example.compute()
        torch.testing.assert_close(
            tensors["weight_1"].grad,
            torch.tensor([[2.0, 4.0], [0.0, -5.0], [0.0, 0.0]]),
            rtol=RTOL,
            atol=ATOL,
        )
        torch.testing.assert_close(
            tensors["bias_1"].grad, torch.tensor([2.0, -2.0, 0.0]), rtol=RTOL, atol=ATOL
        )
        torch.testing.assert_close(
            tensors["weight_2"].grad, torch.tensor([[1.5, 4.0, 0.0]]), rtol=RTOL, atol=ATOL
        )
        torch.testing.assert_close(
            tensors["bias_2"].grad, torch.tensor([2.0]), rtol=RTOL, atol=ATOL
        )
        torch.testing.assert_close(
            tensors["inputs"].grad,
            torch.tensor([[2.0, -1.0], [0.0, -1.0]]),
            rtol=RTOL,
            atol=ATOL,
        )

    def test_parameter_count(self) -> None:
        self.assertEqual(example.SPEC.parameter_count, 13)


if __name__ == "__main__":
    unittest.main()
