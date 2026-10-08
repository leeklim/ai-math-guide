#!/usr/bin/env python3
"""Validate the concept-level revision audit."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / "revision" / "concept-audit.csv"
MANIFEST_PATH = ROOT / "figures" / "manifest.json"
TRANSLATION_AUDIT_PATH = ROOT / "revision" / "translation-audit.csv"
TRANSLATION_FIELDS = (
    "document_id", "source_ko_path", "translation_en_path",
    "reviewed_source_sha256", "reviewed_translation_sha256",
    "status", "reviewer", "review_notes",
)
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
    "explanation_status",
    "explanation_gap",
    "revised_sections",
    "explanation_role",
    "verification_result",
}


class ConceptAuditError(RuntimeError):
    """Raised when the concept audit violates its schema."""


def lesson_sources() -> dict[str, str]:
    found: dict[str, str] = {}
    for root in LESSON_ROOTS:
        for path in root.rglob("*.md"):
            source = path.read_text(encoding="utf-8")
            match = FRONTMATTER_ID_RE.search(source)
            if match:
                found[match.group("id")] = source
    return found


def manifest_assets() -> set[str]:
    data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    return {str(entry["asset"]) for entry in data["figures"]}


def translation_inventory() -> dict[str, str]:
    documents: dict[str, str] = {}
    for path in sorted(ROOT.glob("part-*/*/*.md")):
        match = FRONTMATTER_ID_RE.search(path.read_text(encoding="utf-8"))
        if match:
            document_id = match.group("id")
            if document_id in documents:
                raise ConceptAuditError(f"duplicate translation source ID: {document_id}")
            documents[document_id] = path.relative_to(ROOT).as_posix()
    documents.update({
        "HOME": "README.md", "CURRICULUM": "01-CURRICULUM.md",
        "GLOSSARY": "04-GLOSSARY.md",
        "N05-ARCHITECTURE": "05-N05-ARCHITECTURE-BASELINE.md",
        "N05-ENVIRONMENT": "N05-ENVIRONMENT.md", "GPU-ENVIRONMENT": "GPU-ENVIRONMENT.md",
        "PRIVACY": "PRIVACY.md",
    })
    return documents


def translation_hash(path: Path) -> str:
    return hashlib.sha256(path.read_text(encoding="utf-8").replace("\r\n", "\n").encode("utf-8")).hexdigest()


def read_translation_rows() -> list[dict[str, str]]:
    with TRANSLATION_AUDIT_PATH.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != TRANSLATION_FIELDS:
            raise ConceptAuditError("translation audit columns do not match the schema")
        return list(reader)


def write_translation_rows(rows: list[dict[str, str]]) -> None:
    TRANSLATION_AUDIT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with TRANSLATION_AUDIT_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=TRANSLATION_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def initialize_translation_audit() -> dict[str, int]:
    if TRANSLATION_AUDIT_PATH.exists():
        return validate_translations()
    rows = []
    for document_id, source in translation_inventory().items():
        row = dict.fromkeys(TRANSLATION_FIELDS, "")
        row.update(document_id=document_id, source_ko_path=source,
                   translation_en_path=f"translations/en/{source}", status="planned")
        rows.append(row)
    write_translation_rows(rows)
    return validate_translations()


def record_translation(document_id: str, status: str, reviewer: str, notes: str) -> dict[str, int]:
    if status not in {"drafted", "reviewed", "verified"} or not reviewer.strip() or not notes.strip():
        raise ConceptAuditError("recording a translation requires status, reviewer and concrete notes")
    validate_translations()
    rows = read_translation_rows()
    row = next((row for row in rows if row["document_id"] == document_id), None)
    if row is None:
        raise ConceptAuditError(f"unknown translation ID: {document_id}")
    source = ROOT / row["source_ko_path"]
    translation = ROOT / row["translation_en_path"]
    if not translation.exists():
        raise ConceptAuditError(f"missing English source: {row['translation_en_path']}")
    if status == "verified" and (
        row["status"] not in {"reviewed", "verified"}
        or row["reviewed_source_sha256"] != translation_hash(source)
        or row["reviewed_translation_sha256"] != translation_hash(translation)
    ):
        raise ConceptAuditError(f"HTML verification requires a fresh independent review: {document_id}")
    row.update(status=status, reviewer=reviewer.strip(), review_notes=notes.strip())
    if status == "reviewed":
        row.update(reviewed_source_sha256=translation_hash(source),
                   reviewed_translation_sha256=translation_hash(translation))
    elif status == "drafted":
        row.update(reviewed_source_sha256="", reviewed_translation_sha256="")
    write_translation_rows(rows)
    return validate_translations()


def validate_translations(*, require_verified: bool = False) -> dict[str, int]:
    inventory = translation_inventory()
    rows = read_translation_rows()
    issues: list[str] = []
    seen: set[str] = set()
    present = reviewed = verified = stale = 0
    for row in rows:
        document_id = row["document_id"]
        source = inventory.get(document_id)
        if source is None or document_id in seen:
            issues.append(f"unknown or duplicate translation ID: {document_id}")
            continue
        seen.add(document_id)
        if row["source_ko_path"] != source or row["translation_en_path"] != f"translations/en/{source}":
            issues.append(f"translation pairing path mismatch: {document_id}")
            continue
        status = row["status"]
        if status not in {"planned", "drafted", "reviewed", "verified"}:
            issues.append(f"invalid translation status: {document_id}/{status}")
        translation = ROOT / row["translation_en_path"]
        exists = translation.is_file()
        present += exists
        if status != "planned" and (not exists or not row["reviewer"].strip() or not row["review_notes"].strip()):
            issues.append(f"translation status lacks file/reviewer/evidence: {document_id}")
        if status in {"reviewed", "verified"}:
            hashes = (row["reviewed_source_sha256"], row["reviewed_translation_sha256"])
            if not all(re.fullmatch(r"[0-9a-f]{64}", value) for value in hashes):
                issues.append(f"reviewed translation lacks valid hashes: {document_id}")
            elif not exists or hashes != (translation_hash(ROOT / source), translation_hash(translation)):
                stale += 1
            else:
                reviewed += 1
                verified += status == "verified"
    if seen != set(inventory):
        issues.append(f"translation audit inventory mismatch: missing={sorted(set(inventory) - seen)}")
    if require_verified and (verified != len(inventory) or stale):
        issues.append(f"translations are not fully verified: verified={verified}/{len(inventory)}, stale={stale}")
    if issues:
        raise ConceptAuditError("translation audit failed:\n- " + "\n- ".join(issues))
    return {"documents": len(inventory), "present": present, "missing": len(inventory) - present,
            "reviewed": reviewed, "verified": verified, "unreviewed": present - reviewed, "stale": stale}


def validate_audit(
    *, require_verified: bool = False, require_explanations: bool = False
) -> dict[str, int]:
    issues: list[str] = []
    with AUDIT_PATH.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        columns = set(reader.fieldnames or [])
        if columns != REQUIRED_COLUMNS:
            missing = sorted(REQUIRED_COLUMNS - columns)
            extra = sorted(columns - REQUIRED_COLUMNS)
            raise ConceptAuditError(f"concept audit 열이 맞지 않는다: missing={missing}, extra={extra}")
        rows = list(reader)

    sources = lesson_sources()
    known_lessons = set(sources)
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
        if row["explanation_status"] not in {"planned", "drafting", "verified"}:
            issues.append(f"{line_number}행 explanation_status가 잘못됐다")
        if row["status"] == "verified" and row["explanation_status"] != "verified":
            issues.append(f"{line_number}행 통합 완료에 본문 검증이 빠졌다: {key}")
        if require_explanations and row["explanation_status"] != "verified":
            issues.append(f"{line_number}행 본문이 verified가 아니다: {key}")
        if row["explanation_status"] == "verified":
            for field in ("explanation_gap", "revised_sections", "explanation_role", "verification_result"):
                if not row[field].strip():
                    issues.append(f"{line_number}행 본문 검증 근거가 비어 있다: {field}/{key}")
            headings = set(re.findall(r"^#{2,3} (.+?)\s*$", sources.get(row["lesson_id"], ""), re.MULTILINE))
            for heading in filter(None, (value.strip() for value in row["revised_sections"].split(";"))):
                if heading not in headings:
                    issues.append(f"{line_number}행 본문 절이 없다: {heading}/{key}")
                if heading in {"시각적 직관", "연습문제", "집필자 점검표"}:
                    issues.append(f"{line_number}행 본문 설명 근거로 사용할 수 없는 절이다: {heading}/{key}")
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
    return {
        "concepts": len(rows),
        "lessons": len(covered_lessons),
        "visual_concepts": visual_rows,
        "explanations_verified": sum(row["explanation_status"] == "verified" for row in rows),
        "explanation_lessons_verified": sum(
            all(row["explanation_status"] == "verified" for row in rows if row["lesson_id"] == lesson_id)
            for lesson_id in covered_lessons
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("check", "init-translations", "check-translations", "record-translation"))
    parser.add_argument("--require-verified", action="store_true")
    parser.add_argument("--require-explanations", action="store_true")
    parser.add_argument("--document-id")
    parser.add_argument("--status", choices=("drafted", "reviewed", "verified"))
    parser.add_argument("--reviewer")
    parser.add_argument("--notes")
    args = parser.parse_args()
    try:
        if args.command == "init-translations":
            summary = initialize_translation_audit()
        elif args.command == "check-translations":
            summary = validate_translations(require_verified=args.require_verified)
        elif args.command == "record-translation":
            summary = record_translation(args.document_id, args.status, args.reviewer or "", args.notes or "")
        else:
            summary = validate_audit(
                require_verified=args.require_verified, require_explanations=args.require_explanations
            )
        print(json.dumps(summary, ensure_ascii=False))
    except (ConceptAuditError, OSError, KeyError, json.JSONDecodeError) as error:
        print(str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
