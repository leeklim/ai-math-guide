from __future__ import annotations

import unittest

import torch

from labs.N05 import n05_09_tensor_shape_dtype as example
from labs.N05.common import ATOL, RTOL


class TensorShapeDtypeTest(unittest.TestCase):
    def test_affine_shapes_values_and_broadcast_gradient(self) -> None:
        tensors = example.compute()
        self.assertEqual(tensors["affine"].shape, torch.Size([2, 2]))
        self.assertEqual(tensors["expanded"].shape, torch.Size([2, 1, 3]))
        torch.testing.assert_close(tensors["affine"], torch.tensor([[-1.75, 2.5], [-1.75, 7.0]]), rtol=RTOL, atol=ATOL)
        torch.testing.assert_close(tensors["input_gradient"], torch.tensor([[1.5, 0.5, -0.5], [1.5, 0.5, -0.5]]), rtol=RTOL, atol=ATOL)

    def test_dtype_changes_cancellation_result(self) -> None:
        tensors = example.compute()
        self.assertEqual(tensors["cancellation32"].dtype, torch.float32)
        self.assertEqual(tensors["cancellation64"].dtype, torch.float64)
        self.assertEqual(tensors["cancellation32"].item(), 0.0)
        self.assertEqual(tensors["cancellation64"].item(), 1.0)


if __name__ == "__main__":
    unittest.main()
