from __future__ import annotations

import unittest

import torch

from labs.N05 import n05_19_mlp_routing as example
from labs.N05.common import ATOL, RTOL


class MlpRoutingTest(unittest.TestCase):
    def test_swiglu_shapes_and_values(self) -> None:
        tensors = example.compute()
        self.assertEqual(tensors["swiglu_hidden"].shape, torch.Size([3, 2]))
        self.assertEqual(tensors["dense_output"].shape, torch.Size([3, 2]))
        torch.testing.assert_close(
            tensors["swiglu_hidden"][2],
            torch.tensor([1.4621172, 0.0]),
            rtol=RTOL,
            atol=ATOL,
        )

    def test_top_one_router_selects_one_expert_per_token(self) -> None:
        tensors = example.compute()
        torch.testing.assert_close(
            tensors["router_probability"].sum(dim=-1),
            torch.ones(3),
            rtol=RTOL,
            atol=ATOL,
        )
        torch.testing.assert_close(
            tensors["selected_expert"], torch.tensor([0, 1, 0])
        )
        torch.testing.assert_close(
            tensors["routed_output"][2],
            torch.tensor([0.5, 0.5]),
            rtol=RTOL,
            atol=ATOL,
        )


if __name__ == "__main__":
    unittest.main()

