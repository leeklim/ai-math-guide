from __future__ import annotations

import unittest

import torch

from labs.N05 import n05_08_adamw_state as example
from labs.N05.common import ATOL, RTOL


class AdamwStateTest(unittest.TestCase):
    def test_momentum_step_tracks_a_buffer(self) -> None:
        tensors = example.compute()
        torch.testing.assert_close(
            tensors["gradient"], torch.tensor(3.0), rtol=RTOL, atol=ATOL
        )
        torch.testing.assert_close(
            tensors["momentum_buffer"], torch.tensor(3.0), rtol=RTOL, atol=ATOL
        )
        torch.testing.assert_close(
            tensors["momentum_parameter"], torch.tensor(1.7), rtol=RTOL, atol=ATOL
        )

    def test_adamw_moments_bias_correction_and_decay(self) -> None:
        tensors = example.compute()
        expected = {
            "first_moment": 0.3,
            "second_moment": 0.008999884,
            "corrected_first_moment": 3.0,
            "corrected_second_moment": 9.0,
            "adaptive_update": 0.1,
            "decay_update": 0.002,
            "adamw_parameter": 1.898,
        }
        for name, value in expected.items():
            with self.subTest(tensor=name):
                torch.testing.assert_close(
                    tensors[name], torch.tensor(value), rtol=RTOL, atol=ATOL
                )
        self.assertEqual(tensors["step"].item(), 1)


if __name__ == "__main__":
    unittest.main()
