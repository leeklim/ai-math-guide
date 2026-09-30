from __future__ import annotations

import unittest

from labs.real_models.common import MANIFEST_SCHEMA, load_registries, read_json


class RealModelRegistryTests(unittest.TestCase):
    def test_pinned_model_policy(self) -> None:
        models, experiments, artifact_limit = load_registries()
        self.assertEqual(len(models), 8)
        self.assertEqual(len(experiments), 10)
        self.assertLessEqual(artifact_limit, 256 * 1024 * 1024)
        for model in models.values():
            self.assertEqual(model["dtype"], "float16")
            self.assertNotIn("-v0", model["repository"])
            self.assertNotIn("7b", model["repository"].lower())

    def test_i08_trajectory_has_exact_six_revisions(self) -> None:
        models, experiments, _ = load_registries()
        trajectory = [experiment for experiment in experiments.values() if experiment["lesson_id"] == "I08-13"]
        self.assertEqual(
            [models[experiment["model_key"]]["revision"] for experiment in trajectory],
            ["step0", "step1000", "step10000", "step50000", "step100000", "step143000"],
        )
        self.assertTrue(all(experiment["mode"] == "checkpoint_probe" for experiment in trajectory))

    def test_410m_is_inference_only(self) -> None:
        _, experiments, _ = load_registries()
        scale = experiments["pythia_410m_scale_smoke"]
        self.assertEqual(scale["model_key"], "pythia-410m")
        self.assertEqual(scale["mode"], "inference")

    def test_i07_patching_uses_160m(self) -> None:
        _, experiments, _ = load_registries()
        patching = experiments["pythia_160m_activation_patching"]
        self.assertEqual(patching["model_key"], "pythia-160m")
        self.assertEqual(patching["mode"], "activation_patching")

    def test_manifest_schema_lists_provenance_fields(self) -> None:
        schema = read_json(MANIFEST_SCHEMA)
        required = set(schema["required"])
        self.assertTrue(
            {"source", "model", "inputs", "hook", "resources", "artifacts", "assertions"}.issubset(required)
        )


if __name__ == "__main__":
    unittest.main()
