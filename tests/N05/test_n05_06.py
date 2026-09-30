from __future__ import annotations

import unittest

import torch

from labs.N05 import n05_06_backpropagation as example
from labs.N05.common import ATOL, RTOL


class BackpropagationTest(unittest.TestCase):
    def test_forward_values(self) -> None:
        tensors = example.compute()
        expected = {"z": 1.0, "h": 1.0, "prediction": 3.0, "loss": 4.0}
        for name, value in expected.items():
            with self.subTest(tensor=name):
                torch.testing.assert_close(
                    tensors[name], torch.tensor(value), rtol=RTOL, atol=ATOL
                )

    def test_reverse_mode_gradients_match_chain_rule(self) -> None:
        tensors = example.compute()
        expected = {
            "prediction": 4.0,
            "h": 12.0,
            "z": 24.0,
            "x": 24.0,
            "w": 48.0,
            "b": 24.0,
            "v": 4.0,
            "c": 4.0,
        }
        for name, value in expected.items():
            with self.subTest(tensor=name):
                torch.testing.assert_close(
                    tensors[name].grad, torch.tensor(value), rtol=RTOL, atol=ATOL
                )


if __name__ == "__main__":
    unittest.main()
