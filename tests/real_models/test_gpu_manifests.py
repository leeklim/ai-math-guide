from __future__ import annotations

import json
import os
import unittest
from pathlib import Path

from labs.real_models.common import RESULTS_DIR, ROOT, load_registries, sha256_file, validate_manifest_shape


@unittest.skipUnless(os.environ.get("AI_MATH_VALIDATE_GPU") == "1", "local GPU artifacts are optional in CPU CI")
class GpuManifestTests(unittest.TestCase):
    def test_all_registered_manifests_and_artifacts(self) -> None:
        models, experiments, artifact_limit = load_registries()
        for experiment_id, experiment in experiments.items():
            manifest_path = RESULTS_DIR / experiment_id / "manifest.json"
            self.assertTrue(manifest_path.exists(), experiment_id)
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            validate_manifest_shape(manifest)
            self.assertEqual(manifest["status"], "passed")
            self.assertEqual(manifest["experiment_id"], experiment_id)
            self.assertEqual(manifest["lesson_id"], experiment["lesson_id"])
            model = models[str(experiment["model_key"])]
            self.assertEqual(manifest["model"]["repository"], model["repository"])
            self.assertEqual(manifest["model"]["requested_revision"], model["revision"])
            self.assertTrue(manifest["model"]["resolved_sha"])
            self.assertLessEqual(manifest["resources"]["peak_allocated_bytes"], model["peak_vram_limit_bytes"])
            self.assertLessEqual(manifest["resources"]["artifact_bytes"], artifact_limit)
            self.assertTrue(all(manifest["assertions"].values()))
            for artifact in manifest["artifacts"]:
                artifact_path = ROOT / artifact["path"]
                self.assertTrue(artifact_path.exists())
                self.assertEqual(sha256_file(artifact_path), artifact["sha256"])


if __name__ == "__main__":
    unittest.main()
