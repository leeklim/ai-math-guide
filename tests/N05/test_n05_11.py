from __future__ import annotations

import unittest

import torch

from labs.N05 import n05_11_toy_tokenizer as example


class ToyTokenizerTest(unittest.TestCase):
    def test_fixed_segmentation_ids_and_round_trip(self) -> None:
        values = example.compute()
        self.assertEqual(values["tokens"], ["<bos>", "deep", "learn", "ing", "math", "<eos>"])
        torch.testing.assert_close(values["token_ids"], torch.tensor([1, 3, 4, 5, 6, 2]))
        self.assertEqual(values["decoded"], "deep learning math")

    def test_unknown_word_uses_unknown_token(self) -> None:
        values = example.compute("deep mystery")
        self.assertEqual(values["tokens"], ["<bos>", "deep", "<unk>", "<eos>"])
        self.assertEqual(values["decoded"], "deep <unk>")


if __name__ == "__main__":
    unittest.main()
