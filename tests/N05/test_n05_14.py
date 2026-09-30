from __future__ import annotations

import unittest

import torch

from labs.N05 import n05_14_qkv as example
from labs.N05.common import ATOL, RTOL


class QkvTest(unittest.TestCase):
    def test_projection_values_and_shapes(self) -> None:
        t = example.compute()
        for name in ("query", "key", "value", "scores"):
            self.assertEqual(t[name].shape, torch.Size([2, 2]))
        torch.testing.assert_close(t["query"], torch.tensor([[1., 2.], [3., 4.]]), rtol=RTOL, atol=ATOL)
        torch.testing.assert_close(t["key"], torch.tensor([[3., -1.], [7., -1.]]), rtol=RTOL, atol=ATOL)
        torch.testing.assert_close(t["value"], torch.tensor([[2., 1.], [6., 2.]]), rtol=RTOL, atol=ATOL)
        torch.testing.assert_close(t["scores"], torch.tensor([[1., 5.], [5., 17.]]), rtol=RTOL, atol=ATOL)


if __name__ == "__main__": unittest.main()
