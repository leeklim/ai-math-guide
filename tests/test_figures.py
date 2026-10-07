from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("mmi_figures", ROOT / "scripts" / "figures.py")
assert SPEC is not None and SPEC.loader is not None
FIGURES = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(FIGURES)


class FigureAuditTests(unittest.TestCase):
    def test_manifest_assets_and_lesson_references_match(self) -> None:
        summary = FIGURES.validate_manifest(reproduce=False)
        self.assertGreaterEqual(summary["figures"], 21)
        self.assertEqual(summary["lesson_references"], summary["figures"])
        self.assertGreaterEqual(summary["generated_plots"], 3)


if __name__ == "__main__":
    unittest.main()
