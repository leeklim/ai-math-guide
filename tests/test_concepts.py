from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("mmi_concepts", ROOT / "scripts" / "concepts.py")
assert SPEC is not None and SPEC.loader is not None
CONCEPTS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CONCEPTS)
SEED_SPEC = importlib.util.spec_from_file_location(
    "mmi_seed_concepts", ROOT / "scripts" / "seed_concept_audit.py"
)
assert SEED_SPEC is not None and SEED_SPEC.loader is not None
SEED = importlib.util.module_from_spec(SEED_SPEC)
SEED_SPEC.loader.exec_module(SEED)


class ConceptAuditTests(unittest.TestCase):
    def test_full_concept_inventory_is_valid(self) -> None:
        summary = CONCEPTS.validate_audit()
        self.assertGreater(summary["concepts"], 500)
        self.assertEqual(summary["lessons"], 199)
        self.assertGreater(summary["visual_concepts"], 150)

    def test_foundation_visual_choices_are_explicit(self) -> None:
        visual_audit = SEED.load_visual_audit()
        expected = {
            lesson_id
            for lesson_id, row in visual_audit.items()
            if lesson_id.startswith(("M00-", "M01-", "M02-", "M03-", "M04-"))
            and row["visual_grade"] != "V0"
            and lesson_id not in SEED.PRESERVED_LESSONS
        }
        self.assertEqual(expected, set(SEED.VISUAL_CONCEPT_OVERRIDES))
        self.assertEqual(SEED.VISUAL_CONCEPT_OVERRIDES["M02-01"], (3, 5))
        self.assertEqual(SEED.VISUAL_CONCEPT_OVERRIDES["M03-07"], (1, 3, 5))
        self.assertEqual(SEED.VISUAL_CONCEPT_OVERRIDES["M04-04"], (1, 4, 6))


if __name__ == "__main__":
    unittest.main()
