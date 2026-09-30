from __future__ import annotations

import unittest

import torch

from labs.N05 import n05_21_language_model_objective as example
from labs.N05.common import ATOL, RTOL


class LanguageModelObjectiveTest(unittest.TestCase):
    def test_labels_are_the_input_shifted_one_position(self) -> None:
        tensors = example.compute()
        torch.testing.assert_close(tensors["labels"], tensors["input_ids"][:, 1:])
        self.assertEqual(tensors["prediction_logits"].shape, torch.Size([1, 3, 16]))

    def test_loss_and_gradient_are_finite(self) -> None:
        tensors = example.compute()
        torch.testing.assert_close(
            tensors["loss"],
            torch.tensor(2.1689312),
            rtol=RTOL,
            atol=ATOL,
        )
        self.assertTrue(torch.isfinite(tensors["embedding_gradient_norm"]))
        self.assertGreater(tensors["embedding_gradient_norm"].item(), 0.0)


if __name__ == "__main__":
    unittest.main()

