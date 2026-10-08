from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("mmi_translation_audit", ROOT / "scripts" / "concepts.py")
assert SPEC is not None and SPEC.loader is not None
CONCEPTS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CONCEPTS)
REAL_INVENTORY = CONCEPTS.translation_inventory


class TranslationAuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.source = self.root / "lesson.md"
        self.translation = self.root / "translations/en/lesson.md"
        self.source.write_text("한국어 원문\n", encoding="utf-8")
        self.translation.parent.mkdir(parents=True)
        self.translation.write_text("English source.\n", encoding="utf-8")
        for target, value in (("ROOT", self.root), ("TRANSLATION_AUDIT_PATH", self.root / "audit.csv")):
            self.enterContext(patch.object(CONCEPTS, target, value))
        self.enterContext(patch.object(CONCEPTS, "translation_inventory", return_value={"M00-01": "lesson.md"}))
        CONCEPTS.initialize_translation_audit()

    def record(self, status: str = "reviewed") -> dict[str, int]:
        if status == "verified":
            CONCEPTS.record_translation("M00-01", "reviewed", "independent-reviewer", "Conditions and examples compared.")
        return CONCEPTS.record_translation("M00-01", status, "independent-reviewer", "Conditions and examples compared.")

    def test_source_inventory_has_199_lessons_and_seven_reader_documents(self) -> None:
        with patch.object(CONCEPTS, "ROOT", ROOT):
            documents = REAL_INVENTORY()
            self.assertEqual(len(documents), 206)
            self.assertEqual(sum(path.startswith("part-") for path in documents.values()), 199)

    def test_existing_file_is_not_automatically_reviewed(self) -> None:
        summary = CONCEPTS.validate_translations()
        self.assertEqual(summary["present"], 1)
        self.assertEqual(summary["unreviewed"], 1)
        with self.assertRaises(CONCEPTS.ConceptAuditError):
            CONCEPTS.validate_translations(require_verified=True)

    def test_review_is_not_html_verification(self) -> None:
        summary = self.record()
        self.assertEqual(summary["reviewed"], 1)
        self.assertEqual(summary["verified"], 0)
        with self.assertRaises(CONCEPTS.ConceptAuditError):
            CONCEPTS.validate_translations(require_verified=True)
        self.record("verified")
        self.assertEqual(CONCEPTS.validate_translations(require_verified=True)["verified"], 1)

    def test_either_source_change_makes_review_stale(self) -> None:
        for path in (self.source, self.translation):
            with self.subTest(path=path):
                self.record("verified")
                original = path.read_text(encoding="utf-8")
                path.write_text(original + "changed\n", encoding="utf-8")
                summary = CONCEPTS.validate_translations()
                self.assertEqual(summary["stale"], 1)
                self.assertEqual(summary["verified"], 0)
                with self.assertRaises(CONCEPTS.ConceptAuditError):
                    CONCEPTS.validate_translations(require_verified=True)
                path.write_text(original, encoding="utf-8")

    def test_initializer_preserves_prior_review(self) -> None:
        self.record("verified")
        before = CONCEPTS.TRANSLATION_AUDIT_PATH.read_bytes()
        CONCEPTS.initialize_translation_audit()
        self.assertEqual(before, CONCEPTS.TRANSLATION_AUDIT_PATH.read_bytes())

    def test_html_verification_cannot_refresh_a_missing_or_stale_review(self) -> None:
        with self.assertRaisesRegex(CONCEPTS.ConceptAuditError, "fresh independent review"):
            CONCEPTS.record_translation("M00-01", "verified", "html-reviewer", "Rendered page checked.")
        self.record()
        self.translation.write_text("Edited after review.\n", encoding="utf-8")
        before = CONCEPTS.TRANSLATION_AUDIT_PATH.read_bytes()
        with self.assertRaisesRegex(CONCEPTS.ConceptAuditError, "fresh independent review"):
            CONCEPTS.record_translation("M00-01", "verified", "html-reviewer", "Rendered page checked.")
        self.assertEqual(before, CONCEPTS.TRANSLATION_AUDIT_PATH.read_bytes())

    def test_pairing_paths_and_duplicate_ids_are_rejected(self) -> None:
        original = CONCEPTS.read_translation_rows()
        for rows in ([original[0], dict(original[0])], [{**original[0], "translation_en_path": "../outside.md"}]):
            with self.subTest(rows=rows):
                CONCEPTS.write_translation_rows(rows)
                with self.assertRaises(CONCEPTS.ConceptAuditError):
                    CONCEPTS.validate_translations()
        CONCEPTS.write_translation_rows(original)

    def test_review_requires_evidence_and_actual_source(self) -> None:
        for reviewer, notes in (("", "Compared"), ("reviewer", "")):
            with self.assertRaises(CONCEPTS.ConceptAuditError):
                CONCEPTS.record_translation("M00-01", "reviewed", reviewer, notes)
        self.translation.unlink()
        with self.assertRaises(CONCEPTS.ConceptAuditError):
            self.record()

    def test_hash_normalizes_line_endings_but_not_content(self) -> None:
        before = CONCEPTS.translation_hash(self.translation)
        self.translation.write_bytes(b"English source.\r\n")
        self.assertEqual(before, CONCEPTS.translation_hash(self.translation))
        self.translation.write_text("Different source.\n", encoding="utf-8")
        self.assertNotEqual(before, CONCEPTS.translation_hash(self.translation))


if __name__ == "__main__":
    unittest.main()
