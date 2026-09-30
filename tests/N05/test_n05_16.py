from __future__ import annotations

import unittest

import torch

from labs.N05 import n05_16_attention_head_sharing as example


class AttentionHeadSharingTest(unittest.TestCase):
    def test_all_variants_expand_to_query_head_shape(self) -> None:
        t = example.compute()
        for name in ("mha_expanded", "mqa_expanded", "gqa_expanded"):
            self.assertEqual(t[name].shape, torch.Size([1, 4, 2, 2]))
        torch.testing.assert_close(t["mqa_expanded"][:, 0], t["mqa_expanded"][:, 3])
        torch.testing.assert_close(t["gqa_expanded"][:, 0], t["gqa_expanded"][:, 1])
        torch.testing.assert_close(t["gqa_expanded"][:, 2], t["gqa_expanded"][:, 3])

    def test_kv_element_counts_reflect_head_sharing(self) -> None:
        t = example.compute()
        torch.testing.assert_close(t["kv_elements"], torch.tensor([32, 8, 16]))


if __name__ == "__main__": unittest.main()
