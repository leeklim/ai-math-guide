from __future__ import annotations

import unittest

import torch

from labs.N05 import n05_15_causal_attention as example
from labs.N05.common import ATOL, RTOL


class CausalAttentionTest(unittest.TestCase):
    def test_mask_probability_and_output(self) -> None:
        t = example.compute()
        self.assertTrue(torch.isneginf(t["masked_scores"][0, 1]))
        torch.testing.assert_close(t["attention_weights"].sum(dim=-1), torch.ones(2), rtol=RTOL, atol=ATOL)
        torch.testing.assert_close(t["attention_weights"][0], torch.tensor([1., 0.]), rtol=RTOL, atol=ATOL)
        torch.testing.assert_close(t["output"], torch.tensor([[2., 1.], [5.9991746, 1.9997936]]), rtol=RTOL, atol=ATOL)


if __name__ == "__main__": unittest.main()
