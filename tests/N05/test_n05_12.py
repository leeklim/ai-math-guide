from __future__ import annotations

import unittest

import torch

from labs.N05 import n05_12_embedding_unembedding as example
from labs.N05.common import ATOL, RTOL


class EmbeddingUnembeddingTest(unittest.TestCase):
    def test_lookup_and_unembedding_shapes_values(self) -> None:
        tensors = example.compute()
        torch.testing.assert_close(tensors["hidden"], torch.tensor([[1., 0., 0.], [0., 0., 1.]]), rtol=RTOL, atol=ATOL)
        torch.testing.assert_close(tensors["logits"], torch.tensor([[1., 0., 0., -1.], [0., 0., 1., .5]]), rtol=RTOL, atol=ATOL)
        self.assertEqual(tensors["probabilities"].shape, torch.Size([2, 4]))
        torch.testing.assert_close(tensors["probabilities"].sum(dim=-1), torch.ones(2), rtol=RTOL, atol=ATOL)

    def test_only_selected_embedding_rows_receive_gradient(self) -> None:
        tensors = example.compute()
        gradient = tensors["embedding"].grad
        self.assertGreater(torch.linalg.vector_norm(gradient[0]).item(), 0.0)
        self.assertGreater(torch.linalg.vector_norm(gradient[2]).item(), 0.0)
        torch.testing.assert_close(gradient[1], torch.zeros(3), rtol=RTOL, atol=ATOL)
        torch.testing.assert_close(gradient[3], torch.zeros(3), rtol=RTOL, atol=ATOL)


if __name__ == "__main__":
    unittest.main()
