#!/usr/bin/env python3
"""Build the initial concept-level revision inventory from lesson structure."""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / "revision" / "concept-audit.csv"
VISUAL_AUDIT_PATH = ROOT / "revision" / "visual-audit.csv"
MANIFEST_PATH = ROOT / "figures" / "manifest.json"
LESSON_ROOTS = (
    ROOT / "part-1-foundations",
    ROOT / "part-2-neural-computation",
    ROOT / "part-3-interpretability",
    ROOT / "part-4-advanced",
)
PRESERVED_LESSONS = {"M02-05", "M03-11", "N05-15"}
FIELDNAMES = (
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
)
FRONTMATTER_ID_RE = re.compile(r'^id:\s*"(?P<id>[A-Z0-9-]+)"\s*$', re.MULTILINE)
FRONTMATTER_TITLE_RE = re.compile(r'^title:\s*"(?P<title>[^"]+)"\s*$', re.MULTILINE)
H2_RE = re.compile(r"^## (?P<title>.+?)\s*$", re.MULTILINE)
CORE_RE = re.compile(r"^핵심 개념(?:\s+\d+)?(?:\.\s*)?(?P<title>.*)$")
NUMBERED_RE = re.compile(r"^\d+\.\s*(?P<title>.+)$")
PROCEDURE_RE = re.compile(r"^해독 절차\s+\d+\.\s*(?P<title>.+)$")
GOAL_BULLET_RE = re.compile(r"^-\s+(?P<goal>.+?)\s*$", re.MULTILINE)
EXCLUDED_CONTENT_WORDS = (
    "실습",
    "실험",
    "예제",
    "연습문제",
    "근거와 갱신 경계",
    "단원 요약",
    "통과 기준",
    "다음 단원",
    "다음 단계",
    "집필자 점검표",
)
VISUAL_KEYWORDS = (
    "공간",
    "벡터",
    "행렬",
    "그래프",
    "경로",
    "흐름",
    "변환",
    "방향",
    "분포",
    "구조",
    "위치",
    "거리",
    "정렬",
    "투영",
    "회전",
    "개입",
    "회로",
    "attention",
    "activation",
    "gradient",
    "Jacobian",
    "spectrum",
)
VISUAL_CONCEPT_OVERRIDES = {
    "M00-03": (1,),
    "M00-04": (1, 2),
    "M00-05": (4,),
    "M00-06": (2,),
    "M00-07": (3,),
    "M00-08": (1, 5),
    "M00-09": (1, 8),
    "M00-10": (3,),
    "M01-01": (5,),
    "M01-02": (2, 4),
    "M01-03": (1, 3),
    "M01-04": (2, 5),
    "M01-05": (2,),
    "M01-06": (1, 2),
    "M01-07": (1, 3),
    "M01-08": (2, 7),
    "M01-09": (2, 4),
    "M01-10": (2, 4),
    "M01-11": (3, 4, 5),
    "M01-12": (1, 3),
    "M01-13": (3, 4),
    "M02-01": (3, 5),
    "M02-02": (3, 4),
    "M02-03": (4, 6),
    "M02-04": (3, 4),
    "M02-06": (3, 6),
    "M02-07": (1, 5, 6),
    "M02-08": (1, 3, 5),
    "M02-09": (3, 4, 5),
    "M02-10": (2, 3, 4),
    "M02-11": (1, 4, 5),
    "M02-12": (3, 5),
    "M02-13": (2, 5, 6),
    "M02-14": (1, 4, 7),
    "M02-15": (2, 5),
    "M03-01": (3,),
    "M03-02": (1, 3),
    "M03-03": (1, 2, 3),
    "M03-04": (3, 4),
    "M03-05": (1, 2, 3),
    "M03-06": (2, 6),
    "M03-07": (1, 3, 5),
    "M03-08": (1, 4),
    "M03-09": (1, 4),
    "M03-10": (1, 2, 5),
    "M03-12": (3, 5, 6),
    "M03-13": (1, 2, 7),
    "M03-14": (3, 4, 5),
    "M03-15": (2, 6),
    "M04-01": (2, 3),
    "M04-02": (1, 4),
    "M04-03": (1, 3),
    "M04-04": (1, 4, 6),
    "M04-05": (1, 2, 4),
    "M04-06": (1, 5, 6),
    "M04-07": (2, 3),
    "M04-08": (5, 6),
    "M04-09": (1, 4),
    "M04-10": (2, 6),
    "M04-11": (1, 3),
    "M04-12": (2, 4),
    "M04-13": (1, 5),
    "M04-14": (2, 5),
    "M04-15": (3, 6),
    "M04-16": (1, 3),
    "M04-17": (2, 5),
}


def section(text: str, heading: str) -> str:
    match = re.search(rf"^## {re.escape(heading)}\s*$", text, re.MULTILINE)
    if not match:
        return ""
    end = re.search(r"^## ", text[match.end() :], re.MULTILINE)
    stop = match.end() + end.start() if end else len(text)
    return text[match.end() : stop]


def plain_text(value: str) -> str:
    value = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", value)
    value = value.replace("**", "").replace("`", "")
    value = re.sub(r"\s+", " ", value).strip()
    return value.rstrip(".")


def lesson_concepts(text: str, lesson_title: str) -> list[tuple[str, str]]:
    headings = [match.group("title").strip() for match in H2_RE.finditer(text)]
    goals = [plain_text(match.group("goal")) for match in GOAL_BULLET_RE.finditer(section(text, "학습 목표"))]

    specific: list[tuple[str, str]] = []
    generic_core = False
    for heading in headings:
        core = CORE_RE.match(heading)
        if not core:
            continue
        title = plain_text(core.group("title"))
        if title:
            specific.append((title, heading))
        else:
            generic_core = True
    if specific:
        return specific

    try:
        start = headings.index("기호와 용어") + 1
    except ValueError:
        start = 0
    try:
        stop = headings.index("흔한 오해", start)
    except ValueError:
        stop = len(headings)
    content_headings = headings[start:stop]

    procedures: list[tuple[str, str]] = []
    for heading in content_headings:
        match = PROCEDURE_RE.match(heading)
        if match:
            procedures.append((plain_text(match.group("title")), heading))
    if procedures:
        return procedures

    numbered: list[tuple[str, str]] = []
    for heading in content_headings:
        match = NUMBERED_RE.match(heading)
        if not match or any(word in heading for word in EXCLUDED_CONTENT_WORDS):
            continue
        numbered.append((plain_text(match.group("title")), heading))
    if numbered:
        return numbered

    if generic_core and goals:
        return [(goal, "학습 목표; 핵심 개념") for goal in goals]

    content: list[tuple[str, str]] = []
    for heading in content_headings:
        if heading == "핵심 개념" or any(word in heading for word in EXCLUDED_CONTENT_WORDS):
            continue
        content.append((plain_text(heading), heading))
    if content:
        return content
    if goals:
        return [(goal, "학습 목표; 통과 기준") for goal in goals]
    return [(lesson_title, "단원 제목; 통과 기준")]


def load_visual_audit() -> dict[str, dict[str, str]]:
    with VISUAL_AUDIT_PATH.open(encoding="utf-8", newline="") as handle:
        return {row["lesson_id"]: row for row in csv.DictReader(handle)}


def load_existing_rows() -> dict[str, list[dict[str, str]]]:
    rows: dict[str, list[dict[str, str]]] = defaultdict(list)
    with AUDIT_PATH.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            rows[row["lesson_id"]].append(row)
    return rows


def load_manifest_assets() -> dict[str, list[str]]:
    data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    assets: dict[str, list[str]] = defaultdict(list)
    for entry in data["figures"]:
        assets[str(entry["lesson_id"])].append(str(entry["asset"]))
    return assets


def candidate_lessons() -> list[tuple[str, str, Path]]:
    lessons: list[tuple[str, str, Path]] = []
    for root in LESSON_ROOTS:
        for path in root.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            id_match = FRONTMATTER_ID_RE.search(text)
            title_match = FRONTMATTER_TITLE_RE.search(text)
            if id_match and title_match:
                lessons.append((id_match.group("id"), title_match.group("title"), path))
    return sorted(lessons)


def visual_indices(
    lesson_id: str, concepts: list[tuple[str, str]], visual_grade: str
) -> set[int]:
    requested = {"V0": 0, "V1": 1, "V2": 2, "V3": 3}[visual_grade]
    requested = min(requested, len(concepts))
    if lesson_id in VISUAL_CONCEPT_OVERRIDES:
        chosen = {index - 1 for index in VISUAL_CONCEPT_OVERRIDES[lesson_id]}
        if visual_grade == "V0" and chosen:
            raise ValueError(
                f"{lesson_id}: V0 lesson cannot select visual concepts"
            )
        if visual_grade != "V0" and len(chosen) < requested:
            raise ValueError(
                f"{lesson_id}: {visual_grade} needs at least {requested} visual concepts, "
                f"but the override selects {len(chosen)}"
            )
        if chosen and max(chosen) >= len(concepts):
            raise ValueError(
                f"{lesson_id}: visual concept override exceeds {len(concepts)} concepts"
            )
        return chosen
    scored = []
    for index, (name, _) in enumerate(concepts):
        score = sum(keyword.lower() in name.lower() for keyword in VISUAL_KEYWORDS)
        scored.append((-score, index))
    return {index for _, index in sorted(scored)[:requested]}


def explanation_action(grade: str) -> str:
    if grade == "E0":
        return "verified"
    if grade in {"E1", "E2"}:
        return "expanded"
    return "restructured"


def planned_asset(stage: str, lesson_id: str, concept_id: str) -> str:
    return f"figures/assets/{stage}/{lesson_id}-{concept_id.lower()}-visual.svg"


def build_rows() -> list[dict[str, str]]:
    visual_audit = load_visual_audit()
    existing_rows = load_existing_rows()
    manifest_assets = load_manifest_assets()
    output: list[dict[str, str]] = []

    for lesson_id, lesson_title, path in candidate_lessons():
        if lesson_id in PRESERVED_LESSONS:
            output.extend(existing_rows[lesson_id])
            continue
        text = path.read_text(encoding="utf-8")
        concepts = lesson_concepts(text, lesson_title)
        lesson_plan = visual_audit[lesson_id]
        visual_set = visual_indices(lesson_id, concepts, lesson_plan["visual_grade"])
        known_assets = manifest_assets.get(lesson_id, [])
        used_assets = 0

        for index, (name, evidence) in enumerate(concepts):
            concept_id = f"C{index + 1:02d}"
            needs_visual = index in visual_set
            asset = ""
            if needs_visual:
                if used_assets < len(known_assets):
                    asset = known_assets[used_assets]
                else:
                    asset = planned_asset(lesson_plan["stage"], lesson_id, concept_id)
                used_assets += 1
            action = explanation_action(lesson_plan["explanation_grade"])
            if needs_visual:
                question = f"{name}에서 비교해야 할 대상과 변화를 어떻게 한 장면에서 추적하는가"
                rationale = (
                    f"{lesson_plan['visual_grade']} 진단에 따라 {lesson_plan['planned_visual']}를 사용해 "
                    "대상·변환·결과를 분리해 확인한다."
                )
            else:
                question = ""
                rationale = (
                    "현재 정의·수식·예제의 연결을 점검하고 "
                    f"{lesson_plan['explanation_grade']} 범위에서 필요한 설명만 보강한다."
                )
            output.append(
                {
                    "lesson_id": lesson_id,
                    "concept_id": concept_id,
                    "concept_name": name,
                    "evidence_source": f"{evidence}; 학습 목표; 통과 기준",
                    "explanation_action": action,
                    "visual_required": "yes" if needs_visual else "no",
                    "visual_question": question,
                    "visual_form": lesson_plan["planned_visual"] if needs_visual else "",
                    "planned_asset": asset,
                    "status": "planned",
                    "rationale": rationale,
                }
            )
    return output


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("summary", "write"))
    args = parser.parse_args()
    rows = build_rows()
    summary = {
        "concepts": len(rows),
        "lessons": len({row["lesson_id"] for row in rows}),
        "visual_concepts": sum(row["visual_required"] == "yes" for row in rows),
        "preserved_lessons": len(PRESERVED_LESSONS),
    }
    if args.command == "write":
        with AUDIT_PATH.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=FIELDNAMES, quoting=csv.QUOTE_ALL)
            writer.writeheader()
            writer.writerows(rows)
    print(json.dumps(summary, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
