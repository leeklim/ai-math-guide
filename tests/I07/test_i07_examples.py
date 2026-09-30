from __future__ import annotations

import json
import unittest
from pathlib import Path

from labs.I07.i07_01_sensitivity_attribution import run as run_01
from labs.I07.i07_02_gradient_attribution import run as run_02
from labs.I07.i07_03_integrated_gradients import run as run_03
from labs.I07.i07_04_perturbation_attribution import run as run_04
from labs.I07.i07_05_observation_intervention import run as run_05
from labs.I07.i07_06_ablation import run as run_06
from labs.I07.i07_07_activation_patching import run as run_07
from labs.I07.i07_08_causal_tracing import run as run_08
from labs.I07.i07_09_path_patching import run as run_09
from labs.I07.i07_10_residual_logit_attribution import run as run_10
from labs.I07.i07_11_circuit_graph import run as run_11
from labs.I07.i07_12_necessity_sufficiency import run as run_12
from labs.I07.i07_13_mediation_counterfactual import run as run_13
from labs.I07.i07_14_off_manifold import run as run_14
from labs.I07.i07_15_controls_statistics import run as run_15
from labs.I07.i07_16_cot_faithfulness import run as run_16
from labs.I07.i07_17_circuit_report import run as run_17


ROOT = Path(__file__).resolve().parents[2]


class I07ExampleTests(unittest.TestCase):
    def test_registry_covers_i07_01_through_17(self) -> None:
        data = json.loads((ROOT / "labs" / "I07" / "examples.json").read_text(encoding="utf-8"))
        self.assertEqual(
            [entry["lesson_id"] for entry in data["examples"]],
            [f"I07-{number:02d}" for number in range(1, 18)],
        )

    def test_sensitivity_and_gradient_values(self) -> None:
        self.assertEqual(run_01()["score"], 7.0)
        self.assertEqual(run_02()["gradient"], [3.0, 2.0, 2.0])

    def test_integrated_gradients_completeness_and_baseline_dependence(self) -> None:
        result = run_03()
        self.assertLess(result["zero_completeness_error"], 0.05)
        self.assertLess(result["one_completeness_error"], 0.05)
        self.assertTrue(result["baseline_changes_attribution"])

    def test_perturbation_depends_on_baseline(self) -> None:
        self.assertTrue(run_04()["baseline_changes_effect"])

    def test_observation_and_intervention_differ(self) -> None:
        result = run_05()
        self.assertNotEqual(result["observational_change"], result["intervention_effect_at_x2"])

    def test_ablation_reports_joint_effect(self) -> None:
        result = run_06()
        self.assertGreater(result["joint_effect_first_two"], result["mean_single_component_effects"][0])

    def test_activation_patch_recovers_clean_score(self) -> None:
        result = run_07()
        self.assertAlmostEqual(result["patched_score"], result["clean_score"])
        self.assertAlmostEqual(result["recovery_fraction"], 1.0)

    def test_causal_trace_localizes_effect(self) -> None:
        result = run_08()
        self.assertEqual(result["best_layer_token"], [1, 0])
        self.assertGreater(result["recovery_map"][1][0], result["recovery_map"][1][1])

    def test_path_and_node_patch_are_not_the_same_intervention(self) -> None:
        result = run_09()
        self.assertLess(result["edge_effect"], result["total_node_effect"])

    def test_residual_attribution_is_additive_before_nonlinearity(self) -> None:
        result = run_10()
        self.assertLess(result["decomposition_error"], 1e-12)
        self.assertFalse(result["includes_final_nonlinearity"])

    def test_circuit_graph_is_acyclic(self) -> None:
        self.assertTrue(run_11()["is_acyclic"])

    def test_necessity_and_sufficiency_are_separate(self) -> None:
        result = run_12()
        self.assertFalse(result["a_individually_necessary"])
        self.assertTrue(result["a_sufficient_in_empty_baseline"])
        self.assertTrue(result["redundancy_present"])

    def test_mediation_decomposition(self) -> None:
        self.assertLess(run_13()["additive_decomposition_error"], 1e-12)

    def test_off_manifold_patch_is_detected(self) -> None:
        result = run_14()
        self.assertGreater(result["patch_distance_to_manifold"], result["clean_distance_to_manifold"])

    def test_controls_use_paired_experimental_units(self) -> None:
        result = run_15()
        self.assertTrue(result["paired_design"])
        self.assertEqual(result["experimental_unit_count"], 8)
        self.assertGreater(result["paired_effect_mean"], 0.2)

    def test_cot_faithfulness_uses_intervention(self) -> None:
        result = run_16()
        self.assertTrue(result["faithful_model_answer_change"])
        self.assertFalse(result["post_hoc_model_answer_change"])

    def test_capstone_has_controls_and_bounded_claim(self) -> None:
        result = run_17()
        self.assertEqual(result["experimental_units"], 64)
        self.assertTrue(result["complete_for_defined_graph"])
        self.assertIn("synthetic", result["claim"])


if __name__ == "__main__":
    unittest.main()
