from __future__ import annotations

import unittest

import torch

from labs.N05 import n05_18_normalization_order as example
from labs.N05.common import ATOL, RTOL


class NormalizationOrderTest(unittest.TestCase):
    def test_layer_norm_and_rms_norm_invariants(self) -> None:
        tensors = example.compute()
        torch.testing.assert_close(
            tensors["layer_norm"].mean(dim=-1),
            torch.zeros(2),
            rtol=RTOL,
            atol=2e-6,
        )
        torch.testing.assert_close(
            (tensors["rms_norm"] ** 2).mean(dim=-1),
            torch.ones(2),
            rtol=2e-6,
            atol=2e-6,
        )
        self.assertGreater(tensors["rms_norm"][0].mean().item(), 0.0)

    def test_pre_norm_and_post_norm_order_changes_output(self) -> None:
        tensors = example.compute()
        self.assertFalse(
            torch.allclose(
                tensors["pre_norm_output"], tensors["post_norm_output"]
            )
        )
        torch.testing.assert_close(
            tensors["post_norm_output"],
            tensors["rms_norm"],
            rtol=2e-6,
            atol=2e-6,
        )


if __name__ == "__main__":
    unittest.main()

