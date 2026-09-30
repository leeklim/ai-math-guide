from __future__ import annotations

import unittest

import torch

from labs.N05 import n05_02_single_neuron as example
from labs.N05.common import ATOL, RTOL


class SingleNeuronTest(unittest.TestCase):
    def test_forward_and_gradients_match_hand_calculation(self) -> None:
        tensors = example.compute()
        self.assertEqual(tensors["x"].shape, torch.Size([2]))
        self.assertEqual(tensors["pre_activation"].shape, torch.Size([]))
        self.assertEqual(tensors["x"].dtype, torch.float32)
        torch.testing.assert_close(
            tensors["pre_activation"], torch.tensor(2.0), rtol=RTOL, atol=ATOL
        )
        torch.testing.assert_close(
            tensors["activation"], torch.tensor(2.0), rtol=RTOL, atol=ATOL
        )
        torch.testing.assert_close(tensors["loss"], torch.tensor(1.0), rtol=RTOL, atol=ATOL)
        torch.testing.assert_close(
            tensors["weight"].grad, torch.tensor([4.0, -2.0]), rtol=RTOL, atol=ATOL
        )
        torch.testing.assert_close(
            tensors["bias"].grad, torch.tensor(2.0), rtol=RTOL, atol=ATOL
        )
        torch.testing.assert_close(
            tensors["x"].grad, torch.tensor([3.0, 1.0]), rtol=RTOL, atol=ATOL
        )

    def test_parameter_count(self) -> None:
        self.assertEqual(example.SPEC.parameter_count, 3)


if __name__ == "__main__":
    unittest.main()
