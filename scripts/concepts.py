#!/usr/bin/env python3
"""Validate the concept-level revision audit."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / "revision" / "concept-audit.csv"
MANIFEST_PATH = ROOT / "figures" / "manifest.json"
LESSON_ROOTS = (
    ROOT / "part-1-foundations",
    ROOT / "part-2-neural-computation",
    ROOT / "part-3-interpretability",
    ROOT / "part-4-advanced",
)
FRONTMATTER_ID_RE = re.compile(r'^id:\s*"(?P<id>[A-Z0-9-]+)"\s*$', re.MULTILINE)
REQUIRED_COLUMNS = {
    "lesson_id",
    "concept_id",
    "concept_name",
    "evidence_source",
    "explanation_action",
    "visual_required",
    "visual_question",
    "visual_form",
    "planned_asset",
    "status",
    "rationale",
}


class ConceptAuditError(RuntimeError):
    """Raised when the concept audit violates its schema."""


def lesson_ids() -> set[str]:
    found: set[str] = set()
    for root in LESSON_ROOTS:
        for path in root.rglob("*.md"):
            match = FRONTMATTER_ID_RE.search(path.read_text(encoding="utf-8"))
            if match:
                found.add(match.group("id"))
    return found


def manifest_assets() -> set[str]:
    data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    return {str(entry["asset"]) for entry in data["figures"]}


def validate_audit(*, require_verified: bool = False) -> dict[str, int]:
    issues: list[str] = []
    with AUDIT_PATH.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        columns = set(reader.fieldnames or [])
        if columns != REQUIRED_COLUMNS:
            missing = sorted(REQUIRED_COLUMNS - columns)
            extra = sorted(columns - REQUIRED_COLUMNS)
            raise ConceptAuditError(f"concept audit 열이 맞지 않는다: missing={missing}, extra={extra}")
        rows = list(reader)

    known_lessons = lesson_ids()
    known_assets = manifest_assets()
    seen: set[tuple[str, str]] = set()
    covered_lessons: set[str] = set()
    visual_rows = 0

    for line_number, row in enumerate(rows, start=2):
        key = (row["lesson_id"], row["concept_id"])
        if key in seen:
            issues.append(f"{line_number}행 concept key가 중복됐다: {key}")
        seen.add(key)
        covered_lessons.add(row["lesson_id"])
        if row["lesson_id"] not in known_lessons:
            issues.append(f"{line_number}행 단원이 존재하지 않는다: {row['lesson_id']}")
        if row["explanation_action"] not in {"verified", "expanded", "restructured"}:
            issues.append(f"{line_number}행 explanation_action이 잘못됐다")
        if row["visual_required"] not in {"yes", "no"}:
            issues.append(f"{line_number}행 visual_required가 잘못됐다")
        if row["status"] not in {"planned", "drafting", "verified"}:
            issues.append(f"{line_number}행 status가 잘못됐다")
        if require_verified and row["status"] != "verified":
            issues.append(f"{line_number}행이 verified가 아니다: {key}")
        if row["visual_required"] == "yes":
            visual_rows += 1
            if not row["visual_question"] or not row["visual_form"] or not row["planned_asset"]:
                issues.append(f"{line_number}행 필수 시각화 정보가 비어 있다: {key}")
            for asset in row["planned_asset"].split(";"):
                expected_prefix = f"figures/assets/{row['lesson_id'].rsplit('-', 1)[0]}/"
                if not asset.startswith(expected_prefix) or not asset.endswith(".svg"):
                    issues.append(f"{line_number}행 planned asset 경로가 잘못됐다: {asset}")
                if row["status"] == "verified" and asset not in known_assets:
                    issues.append(f"{line_number}행 asset이 manifest에 없다: {asset}")
        elif row["planned_asset"]:
            issues.append(f"{line_number}행 V0 concept에 asset이 있다: {key}")
        if not row["concept_name"] or not row["evidence_source"] or not row["rationale"]:
            issues.append(f"{line_number}행 필수 설명이 비어 있다: {key}")

    missing_lessons = sorted(known_lessons - covered_lessons)
    extra_lessons = sorted(covered_lessons - known_lessons)
    if missing_lessons:
        issues.append(f"개념 대장에서 빠진 단원이 있다: {missing_lessons}")
    if extra_lessons:
        issues.append(f"개념 대장에 알 수 없는 단원이 있다: {extra_lessons}")

    by_lesson: dict[str, list[str]] = {}
    for row in rows:
        by_lesson.setdefault(row["lesson_id"], []).append(row["concept_id"])
    for lesson_id, concept_ids in by_lesson.items():
        expected = [f"C{index:02d}" for index in range(1, len(concept_ids) + 1)]
        if concept_ids != expected:
            issues.append(f"{lesson_id} concept_id가 C01부터 연속되지 않는다: {concept_ids}")

    if issues:
        raise ConceptAuditError("concept audit 실패:\n- " + "\n- ".join(issues))
    return {"concepts": len(rows), "lessons": len(covered_lessons), "visual_concepts": visual_rows}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("check",))
    parser.add_argument("--require-verified", action="store_true")
    args = parser.parse_args()
    try:
        summary = validate_audit(require_verified=args.require_verified)
        print(json.dumps(summary, ensure_ascii=False))
    except (ConceptAuditError, OSError, KeyError, json.JSONDecodeError) as error:
        print(str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
