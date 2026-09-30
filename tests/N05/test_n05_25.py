from __future__ import annotations

import unittest

import torch

from labs.N05 import n05_25_activation_hook as example
from labs.N05.common import ATOL, RTOL


class ActivationHookTest(unittest.TestCase):
    def test_hook_collects_only_the_selected_token(self) -> None:
        tensors = example.compute()
        self.assertEqual(tensors["hook_output_shape"].tolist(), [1, 4, 4])
        self.assertEqual(tensors["selected_activation"].shape, torch.Size([4]))
        self.assertEqual(tensors["selected_bytes"].item(), 16)
        self.assertFalse(tensors["selected_requires_grad"].item())

    def test_read_only_hook_preserves_output_and_is_removed(self) -> None:
        tensors = example.compute()
        torch.testing.assert_close(
            tensors["logits_with_hook"],
            tensors["logits_after_removal"],
            rtol=RTOL,
            atol=ATOL,
        )
        self.assertEqual(tensors["calls_before_removal"].item(), 1)
        self.assertEqual(tensors["calls_after_removal"].item(), 1)


if __name__ == "__main__":
    unittest.main()

