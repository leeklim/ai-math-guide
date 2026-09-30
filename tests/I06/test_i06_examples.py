from __future__ import annotations

import json
import unittest
from pathlib import Path

from labs.I06.i06_04_neuron_basis import run as run_04
from labs.I06.i06_05_pca_svd import run as run_05
from labs.I06.i06_06_linear_probe import run as run_06
from labs.I06.i06_07_probe_control import run as run_07
from labs.I06.i06_08_similarity import run as run_08
from labs.I06.i06_09_feature_visualization import run as run_09
from labs.I06.i06_10_superposition import run as run_10
from labs.I06.i06_11_sparse_coding import run as run_11
from labs.I06.i06_12_sparse_autoencoder import run as run_12
from labs.I06.i06_13_feature_stability import run as run_13
from labs.I06.i06_14_claim_ledger import run as run_14
from labs.I06.i06_15_representation_report import run as run_15


ROOT = Path(__file__).resolve().parents[2]


class I06ExampleTests(unittest.TestCase):
    def test_registry_covers_i06_04_through_15(self) -> None:
        data = json.loads((ROOT / "labs" / "I06" / "examples.json").read_text(encoding="utf-8"))
        self.assertEqual(
            [entry["lesson_id"] for entry in data["examples"]],
            [f"I06-{number:02d}" for number in range(4, 16)],
        )

    def test_neuron_basis_rotation_preserves_geometry(self) -> None:
        result = run_04()
        self.assertLess(result["pairwise_distance_max_error"], 1e-10)
        self.assertNotEqual(result["original_best_coordinate"], result["rotated_best_coordinate"])

    def test_pca_recovers_low_rank_structure(self) -> None:
        result = run_05()
        self.assertGreater(result["top_two_explained_variance"], 0.99)
        self.assertLess(result["rank_two_relative_error"], 0.05)

    def test_probe_and_control(self) -> None:
        probe = run_06()
        control = run_07()
        self.assertGreaterEqual(probe["test_accuracy"], 0.9)
        self.assertGreater(control["selectivity"], 0.3)
        self.assertTrue(control["same_probe_dimension"])

    def test_similarity_distinguishes_aligned_data(self) -> None:
        result = run_08()
        self.assertGreater(result["cka_aligned"], result["cka_unrelated"])
        self.assertGreater(result["rsa_aligned"], result["rsa_unrelated"])

    def test_feature_visualization_orders_scores(self) -> None:
        result = run_09()
        self.assertEqual(len(result["top_indices"]), 5)
        self.assertGreater(min(result["top_scores"]), max(result["bottom_scores"]))

    def test_superposition_has_interference(self) -> None:
        result = run_10()
        self.assertGreater(result["feature_count"], result["representation_dimension"])
        self.assertGreater(result["interference_l2"], 0.0)

    def test_sparse_coding_reconstructs_with_sparse_codes(self) -> None:
        result = run_11()
        self.assertLess(result["reconstruction_mse"], 0.002)
        self.assertLess(result["active_fraction"], 0.7)

    def test_sae_reports_reconstruction_sparsity_and_dead_features(self) -> None:
        result = run_12()
        self.assertLess(result["reconstruction_mse"], 0.03)
        self.assertGreaterEqual(result["mean_l0"], 0.0)
        self.assertGreaterEqual(result["dead_features"], 0)
        self.assertEqual(result["training_steps"], 50)

    def test_feature_matching_recovers_permutation(self) -> None:
        result = run_13()
        self.assertGreater(result["matched_mean_similarity"], 0.99)
        self.assertGreater(result["matched_mean_similarity"], result["naive_diagonal_similarity"])

    def test_claim_ledger_stops_at_recoverable(self) -> None:
        self.assertEqual(run_14()["allowed_claim"], "recoverable")

    def test_report_contains_controls_and_bounded_claim(self) -> None:
        result = run_15()
        self.assertIn("control_accuracy", result["probe"])
        self.assertIn("not tested", result["claim"])


if __name__ == "__main__":
    unittest.main()
