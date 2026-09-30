from __future__ import annotations

import unittest

import torch

from labs.N05 import n05_23_decoding as example
from labs.N05.common import ATOL, RTOL


class DecodingTest(unittest.TestCase):
    def test_temperature_changes_entropy_without_changing_order(self) -> None:
        tensors = example.compute()
        cold_entropy, hot_entropy = tensors["temperature_entropy"]
        self.assertLess(cold_entropy.item(), hot_entropy.item())
        self.assertEqual(tensors["cold_probability"].argmax().item(), 0)
        self.assertEqual(tensors["hot_probability"].argmax().item(), 0)

    def test_truncation_is_renormalized_and_sampling_is_reproducible(self) -> None:
        tensors = example.compute()
        for name in ("top_k_probability", "top_p_probability"):
            probability = tensors[name]
            torch.testing.assert_close(
                probability.sum(), torch.tensor(1.0), rtol=RTOL, atol=ATOL
            )
            self.assertEqual(torch.count_nonzero(probability).item(), 2)
        self.assertEqual(tensors["greedy_token"].item(), 0)
        self.assertEqual(tensors["sampled_token"].item(), 1)


if __name__ == "__main__":
    unittest.main()

