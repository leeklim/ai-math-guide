from __future__ import annotations

import importlib.util
import os
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[2]


def load_site_module():
    spec = importlib.util.spec_from_file_location("ai_math_site", ROOT / "scripts" / "site.py")
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load scripts/site.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CpuSiteGpuIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.site = load_site_module()

    def test_i06_prefix_and_gpu_markers(self) -> None:
        lessons = self.site.discover_post_n05_stage("I06")
        self.assertEqual(
            [lesson["id"] for lesson in lessons],
            [f"I06-{number:02d}" for number in range(1, 16)],
        )

    def test_i07_prefix_and_example_registry(self) -> None:
        lessons = self.site.discover_post_n05_stage("I07")
        registry = self.site.load_stage_example_registry("I07")
        self.assertEqual(
            [lesson["id"] for lesson in lessons],
            [f"I07-{number:02d}" for number in range(1, 18)],
        )
        self.assertEqual(set(registry), {lesson["id"] for lesson in lessons})

    def test_i08_prefix_and_example_registry(self) -> None:
        lessons = self.site.discover_post_n05_stage("I08")
        registry = self.site.load_stage_example_registry("I08")
        self.assertEqual(
            [lesson["id"] for lesson in lessons],
            [f"I08-{number:02d}" for number in range(1, 14)],
        )
        self.assertEqual(set(registry), {lesson["id"] for lesson in lessons})

    def test_cpu_expansion_uses_placeholder_without_results(self) -> None:
        lessons = [
            lesson
            for stage in ("I06", "I07", "I08")
            for lesson in self.site.discover_post_n05_stage(stage)
        ]
        _, experiments = self.site.load_gpu_registries()
        experiment_lessons = {str(experiment["lesson_id"]) for experiment in experiments.values()}
        with patch.dict(os.environ, {}, clear=False):
            os.environ.pop("AI_MATH_GPU_RESULTS", None)
            for lesson in lessons:
                source = Path(lesson["path"]).read_text(encoding="utf-8")
                expanded = self.site.expand_gpu_experiments(source, str(lesson["id"]))
                self.assertNotIn("<!-- GPU_EXPERIMENT:", expanded)
                if lesson["id"] in experiment_lessons:
                    self.assertIn("로컬 GPU 결과가 삽입되지 않음", expanded)

    def test_cpu_site_module_has_no_gpu_library_dependency(self) -> None:
        source = (ROOT / "scripts" / "site.py").read_text(encoding="utf-8")
        self.assertNotIn("import torch", source)
        self.assertNotIn("from transformers", source)
        self.assertNotIn("from_pretrained(", source)


if __name__ == "__main__":
    unittest.main()
