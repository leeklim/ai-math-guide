from __future__ import annotations

import unittest

import torch

from labs.N05 import n05_22_kv_cache as example


class KvCacheTest(unittest.TestCase):
    def test_cached_logits_match_full_causal_logits(self) -> None:
        tensors = example.compute()
        torch.testing.assert_close(
            tensors["cached_logits"],
            tensors["full_logits"],
            rtol=1e-5,
            atol=2e-7,
        )
        self.assertLess(tensors["maximum_absolute_difference"].item(), 2e-7)

    def test_cache_grows_along_the_sequence_axis(self) -> None:
        tensors = example.compute()
        torch.testing.assert_close(
            tensors["cache_lengths"], torch.tensor([1, 2, 3, 4])
        )
        self.assertEqual(tensors["final_key_cache"].shape, torch.Size([1, 1, 4, 4]))
        self.assertEqual(
            tensors["final_value_cache"].shape, torch.Size([1, 1, 4, 4])
        )


if __name__ == "__main__":
    unittest.main()

