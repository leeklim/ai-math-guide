from __future__ import annotations

import unittest

import torch

from labs.N05 import n05_20_decoder_block as example
from labs.N05.common import ATOL, RTOL


class DecoderBlockTest(unittest.TestCase):
    def test_trace_shapes_follow_the_block_contract(self) -> None:
        tensors = example.compute()
        self.assertEqual(tensors["embedding"].shape, torch.Size([1, 3, 4]))
        self.assertEqual(tensors["attention_update"].shape, tensors["embedding"].shape)
        self.assertEqual(tensors["mlp_update"].shape, tensors["embedding"].shape)
        self.assertEqual(tensors["logits"].shape, torch.Size([1, 3, 16]))
        self.assertEqual(tensors["key_cache"].shape, torch.Size([1, 1, 3, 4]))
        self.assertEqual(tensors["parameter_count"].item(), 300)

    def test_residual_additions_are_visible_in_the_trace(self) -> None:
        tensors = example.compute()
        torch.testing.assert_close(
            tensors["residual_mid"],
            tensors["embedding"] + tensors["attention_update"],
            rtol=RTOL,
            atol=ATOL,
        )
        torch.testing.assert_close(
            tensors["residual_out"],
            tensors["residual_mid"] + tensors["mlp_update"],
            rtol=RTOL,
            atol=ATOL,
        )


if __name__ == "__main__":
    unittest.main()

