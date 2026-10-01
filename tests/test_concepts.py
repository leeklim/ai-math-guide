from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("mmi_concepts", ROOT / "scripts" / "concepts.py")
assert SPEC is not None and SPEC.loader is not None
CONCEPTS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CONCEPTS)


class ConceptAuditTests(unittest.TestCase):
    def test_pilot_concept_rows_are_valid(self) -> None:
        summary = CONCEPTS.validate_audit()
        self.assertEqual(summary["concepts"], 20)
        self.assertEqual(summary["lessons"], 3)
        self.assertEqual(summary["visual_concepts"], 14)


if __name__ == "__main__":
    unittest.main()
