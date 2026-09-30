from __future__ import annotations

import unittest

import torch

from labs.N05 import n05_05_softmax_cross_entropy as example
from labs.N05.common import ATOL, RTOL


class SoftmaxCrossEntropyTest(unittest.TestCase):
    def test_stable_softmax_and_loss(self) -> None:
        tensors = example.compute()
        torch.testing.assert_close(
            tensors["shifted_logits"],
            torch.tensor([0.0, -1.0, -2.0]),
            rtol=RTOL,
            atol=ATOL,
        )
        torch.testing.assert_close(
            tensors["probabilities"],
            torch.tensor([0.66524094, 0.24472848, 0.09003057]),
            rtol=RTOL,
            atol=ATOL,
        )
        torch.testing.assert_close(
            tensors["loss"], torch.tensor(0.40760598), rtol=RTOL, atol=ATOL
        )
        torch.testing.assert_close(
            tensors["probabilities"].sum(), torch.tensor(1.0), rtol=RTOL, atol=ATOL
        )

    def test_gradient_and_translation_invariance(self) -> None:
        tensors = example.compute()
        torch.testing.assert_close(
            tensors["logit_gradient"],
            torch.tensor([-0.33475906, 0.24472848, 0.09003057]),
            rtol=RTOL,
            atol=ATOL,
        )
        torch.testing.assert_close(
            tensors["probabilities"],
            tensors["translated_probabilities"],
            rtol=RTOL,
            atol=ATOL,
        )


if __name__ == "__main__":
    unittest.main()
