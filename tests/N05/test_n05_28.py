from __future__ import annotations

import unittest

import torch

from labs.N05 import n05_28_token_path as example
from labs.N05.common import ATOL, RTOL


class TokenPathTest(unittest.TestCase):
    def test_selected_token_residual_path_is_complete(self) -> None:
        tensors = example.compute()
        for name in (
            "embedding",
            "attention_input",
            "attention_update",
            "residual_mid",
            "mlp_input",
            "mlp_update",
            "residual_out",
            "final_norm",
            "embedding_gradient",
        ):
            self.assertEqual(tensors[name].shape, torch.Size([4]))
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

    def test_logit_gradient_and_cache_are_consistent(self) -> None:
        tensors = example.compute()
        self.assertEqual(tensors["logits"].shape, torch.Size([16]))
        self.assertEqual(tensors["predicted_token"].item(), 15)
        self.assertGreater(tensors["embedding_gradient"].norm().item(), 0.0)
        self.assertEqual(tensors["full_key_cache"].shape, torch.Size([1, 1, 4, 4]))
        self.assertEqual(
            tensors["full_value_cache"].shape, torch.Size([1, 1, 4, 4])
        )
        self.assertLess(tensors["cached_logit_maximum_difference"].item(), 2e-7)


if __name__ == "__main__":
    unittest.main()

