from __future__ import annotations

import json
import unittest
from pathlib import Path

from labs.I08.i08_01_checkpoint_design import run as run_01
from labs.I08.i08_02_parameter_function_distance import run as run_02
from labs.I08.i08_03_representation_alignment import run as run_03
from labs.I08.i08_04_sgd_dynamics import run as run_04
from labs.I08.i08_05_minibatch_optimizer_state import run as run_05
from labs.I08.i08_06_hessian_spectrum import run as run_06
from labs.I08.i08_07_loss_path import run as run_07
from labs.I08.i08_08_influence_function import run as run_08
from labs.I08.i08_09_feature_emergence import run as run_09
from labs.I08.i08_10_grokking_transition import run as run_10
from labs.I08.i08_11_seed_data_order import run as run_11
from labs.I08.i08_12_data_attribution import run as run_12
from labs.I08.i08_13_feature_lifecycle import run as run_13


ROOT = Path(__file__).resolve().parents[2]


class I08ExampleTests(unittest.TestCase):
    def test_registry_covers_i08_01_through_13(self) -> None:
        data = json.loads((ROOT / "labs" / "I08" / "examples.json").read_text(encoding="utf-8"))
        self.assertEqual([entry["lesson_id"] for entry in data["examples"]], [f"I08-{number:02d}" for number in range(1, 14)])

    def test_checkpoint_contract_has_six_ordered_revisions(self) -> None:
        result = run_01()
        self.assertEqual(result["checkpoint_count"], 6)
        self.assertTrue(result["strictly_increasing"])

    def test_parameter_distance_can_change_without_function_distance(self) -> None:
        result = run_02()
        self.assertGreater(result["parameter_l2"], 0.0)
        self.assertLess(result["function_rmse"], 1e-12)

    def test_alignment_recovers_rotated_representation(self) -> None:
        result = run_03()
        self.assertGreater(result["unaligned_rmse"], 0.1)
        self.assertLess(result["aligned_rmse"], 1e-12)
        self.assertAlmostEqual(result["linear_cka"], 1.0)

    def test_discrete_gradient_descent_tracks_flow(self) -> None:
        result = run_04()
        self.assertTrue(result["loss_monotone"])
        self.assertLess(result["absolute_gap"], 0.04)

    def test_minibatch_order_changes_momentum_path(self) -> None:
        self.assertTrue(run_05()["order_changes_path"])

    def test_hessian_reports_negative_curvature(self) -> None:
        result = run_06()
        self.assertTrue(result["negative_curvature_present"])
        self.assertEqual(result["largest_eigenvalue"], 4.0)

    def test_loss_barrier_depends_on_path(self) -> None:
        result = run_07()
        self.assertTrue(result["same_endpoints"])
        self.assertGreater(result["straight_path_max_loss"], 0.9)
        self.assertLess(result["curved_path_max_loss"], 1e-20)

    def test_influence_is_local_approximation(self) -> None:
        result = run_08()
        self.assertTrue(result["local_approximation"])
        self.assertGreater(result["rank_correlation_proxy"], 0.9)

    def test_feature_events_are_separate(self) -> None:
        result = run_09()
        self.assertTrue(result["events_are_distinct"])
        self.assertLess(result["recoverability_crossing"], result["use_crossing"])

    def test_grokking_trace_has_delayed_generalization(self) -> None:
        self.assertGreater(run_10()["delay_steps"], 0)

    def test_paired_seed_design_is_more_precise(self) -> None:
        self.assertTrue(run_11()["paired_is_more_precise"])

    def test_tracin_is_not_retraining_ground_truth(self) -> None:
        result = run_12()
        self.assertGreater(result["tracin_score"], 0.0)
        self.assertFalse(result["is_retraining_ground_truth"])

    def test_capstone_separates_four_claims(self) -> None:
        result = run_13()
        self.assertEqual(result["checkpoint_count"], 6)
        self.assertEqual(result["separate_claim_columns"], ["formation", "recoverability", "use", "behavior"])


if __name__ == "__main__":
    unittest.main()
