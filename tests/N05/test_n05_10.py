from __future__ import annotations

import unittest

import torch

from labs.N05 import n05_10_jvp_vjp as example
from labs.N05.common import ATOL, RTOL


class JvpVjpTest(unittest.TestCase):
    def test_jacobian_matches_hand_calculation(self) -> None:
        tensors = example.compute()
        torch.testing.assert_close(tensors["output"], torch.tensor([6.0, 7.0]), rtol=RTOL, atol=ATOL)
        torch.testing.assert_close(tensors["jacobian"], torch.tensor([[3.0, 2.0], [4.0, 1.0]]), rtol=RTOL, atol=ATOL)

    def test_function_transforms_match_explicit_products(self) -> None:
        tensors = example.compute()
        torch.testing.assert_close(tensors["jvp"], torch.tensor([1.0, 3.0]), rtol=RTOL, atol=ATOL)
        torch.testing.assert_close(tensors["vjp"], torch.tensor([2.0, 3.0]), rtol=RTOL, atol=ATOL)
        torch.testing.assert_close(tensors["jvp"], tensors["explicit_jvp"], rtol=RTOL, atol=ATOL)
        torch.testing.assert_close(tensors["vjp"], tensors["explicit_vjp"], rtol=RTOL, atol=ATOL)


if __name__ == "__main__":
    unittest.main()
