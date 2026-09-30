from __future__ import annotations

import unittest

import torch

from labs.N05 import n05_26_gradient_intervention as example
from labs.N05.common import ATOL, RTOL


class GradientInterventionTest(unittest.TestCase):
    def test_selected_activation_gradient_is_collected(self) -> None:
        tensors = example.compute()
        self.assertEqual(tensors["activation"].shape, torch.Size([4]))
        self.assertEqual(tensors["activation_gradient"].shape, torch.Size([4]))
        torch.testing.assert_close(
            tensors["activation_gradient"],
            torch.tensor([-0.5703850, -0.5502910, 0.3825905, -0.2382722]),
            rtol=RTOL,
            atol=ATOL,
        )

    def test_zero_intervention_changes_the_matched_target(self) -> None:
        tensors = example.compute()
        self.assertNotEqual(tensors["actual_change"].item(), 0.0)
        self.assertLess(
            abs(
                tensors["actual_change"].item()
                - tensors["first_order_change"].item()
            ),
            0.005,
        )


if __name__ == "__main__":
    unittest.main()

