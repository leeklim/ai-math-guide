from __future__ import annotations

import unittest

import torch

from labs.N05 import n05_01_tensor_graph as example
from labs.N05.common import ATOL, RTOL


class TensorGraphTest(unittest.TestCase):
    def test_values_shapes_dtype_and_gradient(self) -> None:
        tensors = example.compute()
        self.assertEqual(tensors["x"].shape, torch.Size([2]))
        self.assertEqual(tensors["product"].shape, torch.Size([2]))
        self.assertEqual(tensors["output"].shape, torch.Size([]))
        self.assertEqual(tensors["x"].dtype, torch.float32)
        torch.testing.assert_close(
            tensors["product"], torch.tensor([3.0, 8.0]), rtol=RTOL, atol=ATOL
        )
        torch.testing.assert_close(
            tensors["output"], torch.tensor(11.0), rtol=RTOL, atol=ATOL
        )
        torch.testing.assert_close(
            tensors["x"].grad, torch.tensor([3.0, 4.0]), rtol=RTOL, atol=ATOL
        )

    def test_fixed_seed_is_reproducible(self) -> None:
        first = example.run_example()
        second = example.run_example()
        self.assertEqual(first["values"], second["values"])
        self.assertEqual(first["gradients"], second["gradients"])


if __name__ == "__main__":
    unittest.main()
