from __future__ import annotations

import importlib.util
import csv
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


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
    def check_sample(self, updates: dict[str, str], **options: bool) -> dict[str, int]:
        row = dict.fromkeys(SEED.FIELDNAMES, "")
        row.update(
            lesson_id="M00-03", concept_id="C01", concept_name="함수의 조건",
            evidence_source="정의", explanation_action="expanded",
            visual_required="yes", visual_question="대응을 어떻게 나타내는가",
            visual_form="대응도", planned_asset="figures/assets/M00/M00-03-c01-visual.svg",
            status="drafting", rationale="입력과 출력의 대응",
            explanation_status="verified", explanation_gap="정의의 두 조건을 압축했다",
            revised_sections="정의", explanation_role="두 조건의 뜻을 풀었다",
            verification_result="그림 없이 두 조건을 구분할 수 있다",
        )
        row.update(updates)
        with tempfile.TemporaryDirectory() as directory:
            audit = Path(directory) / "audit.csv"
            with audit.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=SEED.FIELDNAMES)
                writer.writeheader()
                writer.writerow(row)
            with patch.object(CONCEPTS, "AUDIT_PATH", audit), patch.object(
                CONCEPTS, "lesson_sources", return_value={"M00-03": "## 정의\n본문\n### 시각적 직관\n그림"}
            ):
                return CONCEPTS.validate_audit(**options)

    def test_full_concept_inventory_is_valid(self) -> None:
        summary = CONCEPTS.validate_audit()
        self.assertGreater(summary["concepts"], 500)
        self.assertEqual(summary["lessons"], 199)
        self.assertGreater(summary["visual_concepts"], 150)
        self.assertGreaterEqual(summary["explanations_verified"], 14)
        self.assertGreaterEqual(summary["explanation_lessons_verified"], 3)

    def test_explanation_gate_does_not_require_finished_figures(self) -> None:
        summary = self.check_sample({}, require_explanations=True)
        self.assertEqual(summary["explanation_lessons_verified"], 1)
        with self.assertRaisesRegex(CONCEPTS.ConceptAuditError, "행이 verified가 아니다"):
            self.check_sample({}, require_verified=True)

    def test_integrated_completion_requires_explanation_verification(self) -> None:
        with self.assertRaisesRegex(CONCEPTS.ConceptAuditError, "본문 검증이 빠졌다"):
            self.check_sample({"status": "verified", "explanation_status": "planned"})

    def test_pending_explanations_fail_the_explanation_gate(self) -> None:
        with self.assertRaisesRegex(CONCEPTS.ConceptAuditError, "본문이 verified가 아니다"):
            self.check_sample({"explanation_status": "planned"}, require_explanations=True)

    def test_verified_explanations_require_concrete_evidence(self) -> None:
        for field in ("explanation_gap", "revised_sections", "explanation_role", "verification_result"):
            with self.subTest(field=field), self.assertRaisesRegex(
                CONCEPTS.ConceptAuditError, "본문 검증 근거가 비어 있다"
            ):
                self.check_sample({field: " "})

    def test_body_evidence_cannot_point_to_a_missing_or_visual_section(self) -> None:
        for heading in ("없는 절", "시각적 직관"):
            with self.subTest(heading=heading), self.assertRaises(CONCEPTS.ConceptAuditError):
                self.check_sample({"revised_sections": heading})

    def test_e0_can_keep_sufficient_text_with_evidence(self) -> None:
        self.check_sample({"explanation_action": "verified", "explanation_gap": "없음: 정의의 조건을 설명했다"})

    def test_seed_preserves_explanation_reviews_outside_the_fixed_pilot(self) -> None:
        for review in ({"explanation_status": "drafting"}, {"explanation_gap": "정의와 수식의 연결 누락"}):
            row = {"lesson_id": "M00-06", "status": "planned", "explanation_status": "planned", **review}
            with self.subTest(review=review), patch.object(
                SEED, "candidate_lessons", return_value=[("M00-06", "합", Path("unused"))]
            ), patch.object(SEED, "load_existing_rows", return_value={"M00-06": [row]}):
                self.assertEqual(SEED.build_rows(), [row])

    def test_seed_leaves_the_current_audit_unchanged(self) -> None:
        with SEED.AUDIT_PATH.open(encoding="utf-8", newline="") as handle:
            current = list(csv.DictReader(handle))
        self.assertEqual(SEED.build_rows(), current)

    def test_foundation_visual_choices_are_explicit(self) -> None:
        visual_audit = SEED.load_visual_audit()
        expected = {
            lesson_id
            for lesson_id, row in visual_audit.items()
            if lesson_id.startswith(("M00-", "M01-", "M02-", "M03-", "M04-"))
            and row["visual_grade"] != "V0"
        }
        covered = set(SEED.VISUAL_CONCEPT_OVERRIDES) | SEED.PRESERVED_LESSONS
        self.assertFalse(expected - covered)
        self.assertEqual(SEED.VISUAL_CONCEPT_OVERRIDES["M02-01"], (3, 5))
        self.assertEqual(SEED.VISUAL_CONCEPT_OVERRIDES["M03-07"], (1, 3, 5))
        self.assertEqual(SEED.VISUAL_CONCEPT_OVERRIDES["M04-04"], (1, 4, 6))


if __name__ == "__main__":
    unittest.main()
