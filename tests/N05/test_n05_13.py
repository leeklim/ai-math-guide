from __future__ import annotations

import unittest

import torch

from labs.N05 import n05_13_rope as example
from labs.N05.common import ATOL, RTOL


class RopeTest(unittest.TestCase):
    def test_rotation_values_and_norm_preservation(self) -> None:
        tensors = example.compute()
        torch.testing.assert_close(tensors["rotated"][0], tensors["vectors"][0], rtol=RTOL, atol=ATOL)
        torch.testing.assert_close(tensors["rotated"][1], torch.tensor([0.54030234, 0.84147096, -0.00999983, 0.99994999]), rtol=RTOL, atol=ATOL)
        torch.testing.assert_close(tensors["rotated_norms"], tensors["original_norms"], rtol=RTOL, atol=ATOL)

    def test_dot_product_depends_on_relative_position(self) -> None:
        tensors = example.compute()
        torch.testing.assert_close(tensors["same_position_dot"], tensors["original_dot"], rtol=RTOL, atol=ATOL)
        torch.testing.assert_close(tensors["relative_dot"], torch.tensor(1.54025233), rtol=RTOL, atol=ATOL)


if __name__ == "__main__":
    unittest.main()
