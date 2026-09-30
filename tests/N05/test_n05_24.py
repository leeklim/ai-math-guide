from __future__ import annotations

import unittest

import torch

from labs.N05 import n05_24_cot_observation as example
from labs.N05.common import ATOL, RTOL


class CotObservationTest(unittest.TestCase):
    def test_different_hidden_coordinates_can_give_identical_logits(self) -> None:
        tensors = example.compute()
        self.assertFalse(torch.equal(tensors["hidden_a"], tensors["hidden_b"]))
        torch.testing.assert_close(
            tensors["logits_a"], tensors["logits_b"], rtol=RTOL, atol=ATOL
        )
        self.assertEqual(tensors["maximum_logit_difference"].item(), 0.0)

    def test_identical_logits_give_identical_greedy_observations(self) -> None:
        tensors = example.compute()
        torch.testing.assert_close(
            tensors["generated_tokens_a"], tensors["generated_tokens_b"]
        )
        torch.testing.assert_close(
            tensors["generated_tokens_a"], torch.tensor([1, 0])
        )


if __name__ == "__main__":
    unittest.main()

