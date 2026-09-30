#!/usr/bin/env python3
"""Prepare and validate the private-review MkDocs site."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


ROOT = Path(__file__).resolve().parents[1]
BUILD_ROOT = ROOT / ".build"
DOCS_DIR = BUILD_ROOT / "docs"
SITE_DIR = BUILD_ROOT / "site"
CONFIG_PATH = BUILD_ROOT / "mkdocs.yml"
BASE_CONFIG = ROOT / "site" / "mkdocs.base.yml"

STAGE_COUNTS = {
    "M00": 10,
    "M01": 13,
    "M02": 15,
    "M03": 15,
    "M04": 17,
}

STAGE_TITLES = {
    "M00": "M00 수식 읽기",
    "M01": "M01 변화와 미적분",
    "M02": "M02 벡터와 행렬",
    "M03": "M03 추상선형대수와 행렬미분",
    "M04": "M04 확률·통계·정보이론",
    "N05": "N05 신경망 계산",
    "I06": "I06 표현 해석",
    "I07": "I07 귀인·인과·기계론",
    "I08": "I08 학습 동역학",
}

N05_PLANNED_COUNT = 28
N05_REGISTRY_PATH = ROOT / "labs" / "N05" / "examples.json"
POST_N05_STAGE_SPECS = {
    "I06": {"part": 3, "planned_count": 15, "directory": "part-3-interpretability/I06"},
    "I07": {"part": 3, "planned_count": 17, "directory": "part-3-interpretability/I07"},
    "I08": {"part": 3, "planned_count": 13, "directory": "part-3-interpretability/I08"},
}
GPU_EXPERIMENT_REGISTRY_PATH = ROOT / "labs" / "real_models" / "experiments.json"
GPU_MODEL_REGISTRY_PATH = ROOT / "labs" / "real_models" / "models.json"
GPU_RUNNER_PATH = ROOT / "labs" / "real_models" / "run_pythia.py"

INTERNAL_DOCS = {
    "00-PROJECT-SPEC.md",
    "02-STYLE-AND-NOTATION.md",
    "03-PROGRESS.md",
}

SEARCH_TERMS = {
    "자코비안": "M03-11",
    "특이값분해": "M02-13",
    "상호정보량": "M04-14",
    "연쇄법칙": "M01-06",
    "calibration": "M04-15",
}

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
FRONTMATTER_RE = re.compile(r"\A---\s*\r?\n(.*?)\r?\n---\s*\r?\n", re.DOTALL)
H1_RE = re.compile(r"^# (.+)$", re.MULTILINE)
CHECKLIST_HEADING_RE = re.compile(r"^##\s+집필자 점검표\s*$")
SPOKEN_READING_CHECKLIST = (
    "Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 "
    "기계적 직역을 포함하지 않는다."
)
HANGUL_RE = re.compile(r"[가-힣ㄱ-ㅎㅏ-ㅣ]")
MECHANICAL_READING_PATTERNS = (
    re.compile(r"\b(?:below|under)\s+(?:[a-z]|one|two|three|\d+)\b", re.IGNORECASE),
    re.compile(r"\bupper\s+(?:[a-z]|one|two|three|\d+)\b", re.IGNORECASE),
    re.compile(r"\b(?:express|exp(?:\s+of)?)\s+x\b", re.IGNORECASE),
    re.compile(r"\b(?:open|close)\s+parenthes(?:is|es)\b", re.IGNORECASE),
)


class SiteError(RuntimeError):
    """Raised when a source or generated-site invariant fails."""


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def load_n05_example_registry() -> dict[str, dict[str, object]]:
    data = json.loads(read_text(N05_REGISTRY_PATH))
    if data.get("schema_version") != 1 or not isinstance(data.get("examples"), list):
        raise SiteError("N05 example registry schema가 잘못됐다")

    registry: dict[str, dict[str, object]] = {}
    example_ids: set[str] = set()
    for entry in data["examples"]:
        if not isinstance(entry, dict):
            raise SiteError("N05 example registry entry가 object가 아니다")
        lesson_id = str(entry.get("lesson_id", ""))
        example_id = str(entry.get("example_id", ""))
        source = str(entry.get("source", ""))
        if not re.fullmatch(r"N05-\d{2}", lesson_id):
            raise SiteError(f"N05 registry lesson ID가 잘못됐다: {lesson_id}")
        if not re.fullmatch(r"n05_\d{2}_[a-z0-9_]+", example_id):
            raise SiteError(f"N05 registry example ID가 잘못됐다: {example_id}")
        if lesson_id in registry or example_id in example_ids:
            raise SiteError(f"N05 registry entry가 중복됐다: {lesson_id}/{example_id}")
        source_path = (ROOT / source).resolve()
        if not source_path.is_relative_to(ROOT) or not source_path.exists():
            raise SiteError(f"N05 registry source가 없거나 안전하지 않다: {source}")
        registry[lesson_id] = {"example_id": example_id, "source_path": source_path}
        example_ids.add(example_id)
    return registry


def load_gpu_registries() -> tuple[dict[str, dict[str, object]], dict[str, dict[str, object]]]:
    experiment_data = json.loads(read_text(GPU_EXPERIMENT_REGISTRY_PATH))
    model_data = json.loads(read_text(GPU_MODEL_REGISTRY_PATH))
    if experiment_data.get("schema_version") != 1 or model_data.get("schema_version") != 1:
        raise SiteError("GPU registry schema가 잘못됐다")
    experiments: dict[str, dict[str, object]] = {}
    models: dict[str, dict[str, object]] = {}
    for model in model_data.get("models", []):
        model_key = str(model.get("model_key", ""))
        if not model_key or model_key in models:
            raise SiteError(f"GPU model registry key가 없거나 중복됐다: {model_key}")
        models[model_key] = model
    for experiment in experiment_data.get("experiments", []):
        experiment_id = str(experiment.get("experiment_id", ""))
        if not re.fullmatch(r"[a-z0-9_]+", experiment_id) or experiment_id in experiments:
            raise SiteError(f"GPU experiment ID가 잘못됐거나 중복됐다: {experiment_id}")
        if str(experiment.get("model_key", "")) not in models:
            raise SiteError(f"GPU experiment의 model key가 없다: {experiment_id}")
        experiments[experiment_id] = experiment
    return models, experiments


def parse_frontmatter(path: Path, text: str) -> dict[str, object]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise SiteError(f"frontmatter가 없다: {path.relative_to(ROOT)}")
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise SiteError(f"frontmatter 형식이 잘못됐다: {path.relative_to(ROOT)}")
    return data


def split_markdown_table_row(line: str) -> list[str]:
    """Split a pipe table row without treating math or code pipes as separators."""
    content = line.strip()[1:-1]
    cells: list[str] = []
    start = 0
    in_math = False
    in_code = False
    for index, char in enumerate(content):
        escaped = index > 0 and content[index - 1] == "\\"
        if char == "`" and not escaped:
            in_code = not in_code
        elif char == "$" and not in_code and not escaped:
            in_math = not in_math
        elif char == "|" and not in_math and not in_code and not escaped:
            cells.append(content[start:index].strip())
            start = index + 1
    cells.append(content[start:].strip())
    return cells


def lint_english_readings(
    sources: list[tuple[Path, str]] | None = None,
) -> tuple[list[str], int, int]:
    """Validate notation-table readings and return issues, table count, and cell count."""
    if sources is None:
        foundation_sources = [
            (path, read_text(path))
            for path in sorted(ROOT.glob("part-*/M??/M??-*.md"))
        ]
        n05_sources = [
            (path, read_text(path))
            for path in sorted(ROOT.glob("part-2-neural-computation/N05/N05-*.md"))
        ]
        post_n05_sources = [
            (path, read_text(path))
            for path in sorted(ROOT.glob("part-3-interpretability/I??/I??-*.md"))
        ]
        sources = foundation_sources + n05_sources + post_n05_sources

    issues: list[str] = []
    entries: dict[str, list[tuple[str, Path, int]]] = {}
    table_count = 0
    cell_count = 0

    for path, text in sources:
        lines = text.splitlines()
        file_table_count = 0
        for index, line in enumerate(lines):
            if not line.startswith("|"):
                continue
            header = split_markdown_table_row(line)
            if not header or header[0] not in {"기호·용어", "표기·용어"}:
                continue

            file_table_count += 1
            table_count += 1
            if len(header) < 2 or header[1] != "Common spoken reading":
                actual = header[1] if len(header) > 1 else "<missing>"
                issues.append(
                    f"{path}:{index + 1}: second header={actual!r}, "
                    "expected='Common spoken reading'"
                )
                continue

            row_index = index + 2
            while row_index < len(lines) and lines[row_index].startswith("|"):
                cells = split_markdown_table_row(lines[row_index])
                location = f"{path}:{row_index + 1}"
                if len(cells) < 2:
                    issues.append(f"{location}: Common spoken reading cell is missing")
                    row_index += 1
                    continue

                symbol = cells[0]
                raw_reading = cells[1]
                cell_count += 1
                match = re.fullmatch(r"`([^`]+)`", raw_reading)
                if not match:
                    issues.append(
                        f"{location}: Common spoken reading must be nonempty and fully wrapped in backticks"
                    )
                    reading = raw_reading.strip("`")
                else:
                    reading = match.group(1)

                if HANGUL_RE.search(reading):
                    issues.append(f"{location}: Common spoken reading contains Hangul: {reading!r}")
                elif any(char.isalpha() and not char.isascii() for char in reading):
                    issues.append(
                        f"{location}: Common spoken reading contains non-English letters: {reading!r}"
                    )
                for pattern in MECHANICAL_READING_PATTERNS:
                    if pattern.search(reading):
                        issues.append(
                            f"{location}: mechanical or incorrect reading pattern: {reading!r}"
                        )
                        break
                entries.setdefault(symbol, []).append((reading, path, row_index + 1))
                row_index += 1

        if file_table_count == 0:
            issues.append(f"{path}: notation table is missing")
        if SPOKEN_READING_CHECKLIST not in text:
            issues.append(f"{path}: Common spoken reading checklist item is missing")

    for symbol, uses in entries.items():
        readings = {reading for reading, _, _ in uses}
        if len(readings) <= 1:
            continue
        details = "; ".join(
            f"{path}:{line}={reading!r}" for reading, path, line in uses
        )
        issues.append(f"inconsistent Common spoken reading for {symbol}: {details}")

    return issues, table_count, cell_count


def discover_lessons() -> list[dict[str, object]]:
    lessons: list[dict[str, object]] = []
    seen_ids: set[str] = set()
    issues: list[str] = []

    for stage, expected_count in STAGE_COUNTS.items():
        stage_dir = ROOT / "part-1-foundations" / stage
        paths = sorted(stage_dir.glob(f"{stage}-*.md"))
        if len(paths) != expected_count:
            issues.append(f"{stage} file count={len(paths)}, expected={expected_count}")

        for expected_number, path in enumerate(paths, start=1):
            text = read_text(path)
            meta = parse_frontmatter(path, text)
            lesson_id = str(meta.get("id", ""))
            title = str(meta.get("title", ""))
            expected_id = f"{stage}-{expected_number:02d}"

            if lesson_id != expected_id:
                issues.append(f"ID order mismatch: {path.name} -> {lesson_id}, expected={expected_id}")
            if path.stem != lesson_id and not path.stem.startswith(f"{lesson_id}-"):
                issues.append(f"filename/ID mismatch: {path.name} -> {lesson_id}")
            if lesson_id in seen_ids:
                issues.append(f"duplicate ID: {lesson_id}")
            seen_ids.add(lesson_id)

            h1_matches = H1_RE.findall(text)
            expected_h1 = f"{lesson_id}. {title}"
            if h1_matches != [expected_h1]:
                issues.append(f"H1 mismatch: {lesson_id}")

            checklist_count = len(
                re.findall(r"^##\s+집필자 점검표\s*$", text, flags=re.MULTILINE)
            )
            if checklist_count != 1:
                issues.append(f"checklist count: {lesson_id}={checklist_count}")

            display_open = len(re.findall(r"^\\\[$", text, flags=re.MULTILINE))
            display_close = len(re.findall(r"^\\\]$", text, flags=re.MULTILINE))
            if display_open != display_close:
                issues.append(f"display math mismatch: {lesson_id}={display_open}/{display_close}")

            for line_number, line in enumerate(text.splitlines(), start=1):
                if len(re.findall(r"(?<!\\)\$", line)) % 2:
                    issues.append(f"inline math mismatch: {lesson_id}:{line_number}")
                    break

            for href in LINK_RE.findall(text):
                local_path = href.split("#", 1)[0]
                if not local_path or urlsplit(local_path).scheme:
                    continue
                target = (path.parent / unquote(local_path)).resolve()
                if not target.exists():
                    issues.append(f"broken source link: {lesson_id} -> {href}")

            lessons.append(
                {
                    "id": lesson_id,
                    "title": title,
                    "stage": stage,
                    "path": path,
                    "relative_path": path.relative_to(ROOT).as_posix(),
                }
            )

    foundation_sources = [
        (path, read_text(path))
        for path in sorted(ROOT.glob("part-1-foundations/M??/M??-*.md"))
    ]
    reading_issues, reading_tables, reading_cells = lint_english_readings(foundation_sources)
    issues.extend(reading_issues)
    if reading_tables != 70:
        issues.append(f"foundation reading table count={reading_tables}, expected=70")
    if reading_cells != 463:
        issues.append(f"foundation reading cell count={reading_cells}, expected=463")

    if len(lessons) != 70:
        issues.append(f"total lesson count={len(lessons)}, expected=70")
    if issues:
        raise SiteError("source audit 실패:\n- " + "\n- ".join(issues))
    return lessons


def discover_n05_lessons() -> list[dict[str, object]]:
    stage_dir = ROOT / "part-2-neural-computation" / "N05"
    paths = sorted(stage_dir.glob("N05-*.md"))
    registry = load_n05_example_registry()
    issues: list[str] = []
    lessons: list[dict[str, object]] = []
    written_ids: set[str] = set()

    if len(paths) > N05_PLANNED_COUNT:
        issues.append(f"N05 file count={len(paths)}, planned maximum={N05_PLANNED_COUNT}")

    for expected_number, path in enumerate(paths, start=1):
        text = read_text(path)
        meta = parse_frontmatter(path, text)
        lesson_id = str(meta.get("id", ""))
        written_ids.add(lesson_id)
        title = str(meta.get("title", ""))
        expected_id = f"N05-{expected_number:02d}"

        if lesson_id != expected_id:
            issues.append(f"N05 prefix gap or ID order mismatch: {path.name} -> {lesson_id}, expected={expected_id}")
        if meta.get("part") != 2 or meta.get("stage") != "N05":
            issues.append(f"N05 frontmatter part/stage mismatch: {path.name}")
        if path.stem != lesson_id and not path.stem.startswith(f"{lesson_id}-"):
            issues.append(f"N05 filename/ID mismatch: {path.name} -> {lesson_id}")

        h1_matches = H1_RE.findall(text)
        if h1_matches != [f"{lesson_id}. {title}"]:
            issues.append(f"N05 H1 mismatch: {lesson_id}")
        if len(re.findall(r"^##\s+집필자 점검표\s*$", text, flags=re.MULTILINE)) != 1:
            issues.append(f"N05 checklist count is not one: {lesson_id}")

        display_open = len(re.findall(r"^\\\[$", text, flags=re.MULTILINE))
        display_close = len(re.findall(r"^\\\]$", text, flags=re.MULTILINE))
        if display_open != display_close:
            issues.append(f"N05 display math mismatch: {lesson_id}={display_open}/{display_close}")
        for line_number, line in enumerate(text.splitlines(), start=1):
            if len(re.findall(r"(?<!\\)\$", line)) % 2:
                issues.append(f"N05 inline math mismatch: {lesson_id}:{line_number}")
                break

        for href in LINK_RE.findall(text):
            local_path = href.split("#", 1)[0]
            if not local_path or urlsplit(local_path).scheme:
                continue
            target = (path.parent / unquote(local_path)).resolve()
            if not target.exists():
                issues.append(f"broken N05 source link: {lesson_id} -> {href}")

        example_spec = registry.get(lesson_id)
        expected_example = str(example_spec["example_id"]) if example_spec else None
        markers = re.findall(r"<!--\s*N05_EXAMPLE:\s*([a-z0-9_]+)\s*-->", text)
        if expected_example and markers != [expected_example]:
            issues.append(
                f"N05 example marker mismatch: {lesson_id}={markers}, expected={[expected_example]}"
            )
        if not expected_example and markers:
            issues.append(f"N05 unregistered example marker: {lesson_id}={markers}")

        lessons.append(
            {
                "id": lesson_id,
                "title": title,
                "stage": "N05",
                "path": path,
                "relative_path": path.relative_to(ROOT).as_posix(),
            }
        )

    n05_sources = [(path, read_text(path)) for path in paths]
    unwritten_registry_ids = sorted(set(registry) - written_ids)
    if unwritten_registry_ids:
        issues.append("N05 registry points to unwritten lessons: " + ", ".join(unwritten_registry_ids))
    reading_issues, reading_tables, _ = lint_english_readings(n05_sources)
    issues.extend(reading_issues)
    if reading_tables != len(paths):
        issues.append(f"N05 reading table count={reading_tables}, lesson count={len(paths)}")
    if issues:
        raise SiteError("N05 source audit 실패:\n- " + "\n- ".join(issues))
    return lessons


def discover_post_n05_stage(stage: str) -> list[dict[str, object]]:
    spec = POST_N05_STAGE_SPECS[stage]
    stage_dir = ROOT / str(spec["directory"])
    paths = sorted(stage_dir.glob(f"{stage}-*.md")) if stage_dir.exists() else []
    _, experiments = load_gpu_registries()
    expected_by_lesson: dict[str, list[str]] = {}
    for experiment_id, experiment in experiments.items():
        lesson_id = str(experiment.get("lesson_id", ""))
        expected_by_lesson.setdefault(lesson_id, []).append(experiment_id)

    issues: list[str] = []
    lessons: list[dict[str, object]] = []
    written_ids: set[str] = set()
    if len(paths) > int(spec["planned_count"]):
        issues.append(
            f"{stage} file count={len(paths)}, planned maximum={spec['planned_count']}"
        )

    for expected_number, path in enumerate(paths, start=1):
        text = read_text(path)
        meta = parse_frontmatter(path, text)
        lesson_id = str(meta.get("id", ""))
        title = str(meta.get("title", ""))
        expected_id = f"{stage}-{expected_number:02d}"
        written_ids.add(lesson_id)

        if lesson_id != expected_id:
            issues.append(
                f"{stage} prefix gap or ID order mismatch: {path.name} -> {lesson_id}, expected={expected_id}"
            )
        if meta.get("part") != spec["part"] or meta.get("stage") != stage:
            issues.append(f"{stage} frontmatter part/stage mismatch: {path.name}")
        if path.stem != lesson_id and not path.stem.startswith(f"{lesson_id}-"):
            issues.append(f"{stage} filename/ID mismatch: {path.name} -> {lesson_id}")
        if H1_RE.findall(text) != [f"{lesson_id}. {title}"]:
            issues.append(f"{stage} H1 mismatch: {lesson_id}")
        if len(re.findall(r"^##\s+집필자 점검표\s*$", text, flags=re.MULTILINE)) != 1:
            issues.append(f"{stage} checklist count is not one: {lesson_id}")

        display_open = len(re.findall(r"^\\\[$", text, flags=re.MULTILINE))
        display_close = len(re.findall(r"^\\\]$", text, flags=re.MULTILINE))
        if display_open != display_close:
            issues.append(f"{stage} display math mismatch: {lesson_id}={display_open}/{display_close}")
        for line_number, line in enumerate(text.splitlines(), start=1):
            if len(re.findall(r"(?<!\\)\$", line)) % 2:
                issues.append(f"{stage} inline math mismatch: {lesson_id}:{line_number}")
                break
        for href in LINK_RE.findall(text):
            local_path = href.split("#", 1)[0]
            if not local_path or urlsplit(local_path).scheme:
                continue
            target = (path.parent / unquote(local_path)).resolve()
            if not target.exists():
                issues.append(f"broken {stage} source link: {lesson_id} -> {href}")

        markers = re.findall(r"<!--\s*GPU_EXPERIMENT:\s*([a-z0-9_]+)\s*-->", text)
        expected_markers = expected_by_lesson.get(lesson_id, [])
        if markers != expected_markers:
            issues.append(
                f"GPU experiment marker mismatch: {lesson_id}={markers}, expected={expected_markers}"
            )
        lessons.append(
            {
                "id": lesson_id,
                "title": title,
                "stage": stage,
                "path": path,
                "relative_path": path.relative_to(ROOT).as_posix(),
            }
        )

    registry_ids = {
        lesson_id for lesson_id in expected_by_lesson if lesson_id.startswith(f"{stage}-")
    }
    missing_registry_lessons = sorted(registry_ids - written_ids)
    if missing_registry_lessons:
        issues.append(
            f"GPU registry points to unwritten {stage} lessons: " + ", ".join(missing_registry_lessons)
        )
    sources = [(path, read_text(path)) for path in paths]
    reading_issues, reading_tables, _ = lint_english_readings(sources)
    issues.extend(reading_issues)
    if reading_tables != len(paths):
        issues.append(f"{stage} reading table count={reading_tables}, lesson count={len(paths)}")
    if issues:
        raise SiteError(f"{stage} source audit 실패:\n- " + "\n- ".join(issues))
    return lessons


def discover_all_lessons() -> list[dict[str, object]]:
    lessons = discover_lessons() + discover_n05_lessons()
    for stage in POST_N05_STAGE_SPECS:
        lessons.extend(discover_post_n05_stage(stage))
    return lessons


def remove_h2_sections(text: str, section_names: set[str], *, required: bool = False) -> str:
    lines = text.splitlines(keepends=True)
    output: list[str] = []
    removed: set[str] = set()
    index = 0

    while index < len(lines):
        match = re.match(r"^##\s+(.+?)\s*$", lines[index].rstrip("\r\n"))
        if not match or match.group(1) not in section_names:
            output.append(lines[index])
            index += 1
            continue

        removed.add(match.group(1))
        index += 1
        while index < len(lines):
            if re.match(r"^#{1,2}\s+", lines[index]):
                break
            index += 1

    if required and removed != section_names:
        missing = ", ".join(sorted(section_names - removed))
        raise SiteError(f"제거할 H2 section을 찾지 못했다: {missing}")
    return "".join(output).rstrip() + "\n"


def prepare_homepage() -> str:
    source = read_text(ROOT / "README.md")
    source = remove_h2_sections(source, {"기준 문서", "현재 상태"}, required=True)
    return (
        source.rstrip()
        + "\n\n## 읽기 시작\n\n"
        + "- [전체 학습경로](curriculum.md)\n"
        + "- [첫 단원: 수, 변수와 상수](part-1-foundations/M00/M00-01-numbers-variables.md)\n"
        + "- [용어집](glossary.md)\n"
    )


def strip_editor_checklist(text: str, lesson_id: str) -> str:
    if len(re.findall(r"^##\s+집필자 점검표\s*$", text, flags=re.MULTILINE)) != 1:
        raise SiteError(f"집필자 점검표 section 수가 1이 아니다: {lesson_id}")
    return remove_h2_sections(text, {"집필자 점검표"}, required=True)


def enable_markdown_in_details(text: str, lesson_id: str) -> str:
    details_count = text.count("<details>")
    converted = text.replace("<details>", '<details markdown="1">')
    if converted.count('<details markdown="1">') != details_count:
        raise SiteError(f"details Markdown 변환에 실패했다: {lesson_id}")
    return converted


def add_search_alias(text: str, lesson_id: str) -> str:
    if lesson_id != "M03-11":
        return text
    lines = text.splitlines(keepends=True)
    for index, line in enumerate(lines):
        if line.startswith("# "):
            lines.insert(index + 1, "\n<span class=\"search-alias\">자코비안 야코비안</span>\n")
            return "".join(lines)
    raise SiteError("M03-11 H1 뒤에 검색 별칭을 넣지 못했다")


def expand_n05_example(text: str, lesson_id: str) -> str:
    example_spec = load_n05_example_registry().get(lesson_id)
    if example_spec is None:
        return text
    example_id = str(example_spec["example_id"])
    marker = f"<!-- N05_EXAMPLE: {example_id} -->"
    if text.count(marker) != 1:
        raise SiteError(f"N05 example marker 수가 1이 아니다: {lesson_id}")

    source_path = Path(str(example_spec["source_path"]))
    result_path = BUILD_ROOT / "n05" / "results" / f"{example_id}.json"
    if not source_path.exists():
        raise SiteError(f"N05 code source가 없다: {source_path.relative_to(ROOT)}")
    if not result_path.exists():
        raise SiteError(
            f"N05 실행 결과가 없다: {result_path.relative_to(ROOT)}; "
            "scripts/run_n05_examples.py를 먼저 실행하라"
        )

    source = read_text(source_path).rstrip()
    source_hash = hashlib.sha256(source_path.read_bytes()).hexdigest()
    result = json.loads(read_text(result_path))
    if result.get("source_sha256") != source_hash:
        raise SiteError(f"N05 code와 실행 결과의 source hash가 다르다: {example_id}")
    required = {
        "stdout",
        "shapes",
        "gradients",
        "seed",
        "python_version",
        "torch_version",
        "numpy_version",
        "device",
        "resources",
        "compute_seconds",
        "process_seconds",
        "command",
        "figure_paths",
    }
    missing = sorted(required - result.keys())
    if missing:
        raise SiteError(f"N05 실행 결과 field 누락: {example_id} -> {', '.join(missing)}")
    for figure_path in result["figure_paths"]:
        if not (ROOT / str(figure_path)).exists():
            raise SiteError(f"N05 생성 그림이 없다: {figure_path}")

    resources = result["resources"]
    generated = f"""<!-- N05_SOURCE_SHA256: {example_id} {source_hash} -->

#### 실제 실행 코드

```python
{source}
```

#### 실행 명령

```powershell
{result['command']}
```

#### 실제 실행 결과

```text
{result['stdout']}
```

#### 자동 확인 기록

| 항목 | 값 |
|---|---|
| shape | `{json.dumps(result['shapes'], ensure_ascii=False, sort_keys=True)}` |
| gradient | `{json.dumps(result['gradients'], ensure_ascii=False, sort_keys=True)}` |
| seed | `{result['seed']}` |
| 환경 | Python `{result['python_version']}`, PyTorch `{result['torch_version']}`, NumPy `{result['numpy_version']}` |
| device | `{result['device']}` |
| parameter | `{resources['parameter_count']}` |
| 학습 step | `{resources['training_steps']}` |
| 계산시간 | `{result['compute_seconds']:.6f}`초 |
| process 시작 포함 | `{result['process_seconds']:.6f}`초 |
"""
    return text.replace(marker, generated.rstrip())


def expand_gpu_experiments(text: str, lesson_id: str) -> str:
    models, experiments = load_gpu_registries()
    lesson_experiments = [
        (experiment_id, experiment)
        for experiment_id, experiment in experiments.items()
        if experiment.get("lesson_id") == lesson_id
    ]
    include_results = os.environ.get("AI_MATH_GPU_RESULTS") == "1"
    for experiment_id, experiment in lesson_experiments:
        marker = f"<!-- GPU_EXPERIMENT: {experiment_id} -->"
        if text.count(marker) != 1:
            raise SiteError(f"GPU experiment marker 수가 1이 아니다: {lesson_id}/{experiment_id}")
        model = models[str(experiment["model_key"])]
        command = (
            ".venv-gpu\\Scripts\\python.exe -m "
            f"labs.real_models.run_pythia {experiment_id}"
        )
        source_hash = hashlib.sha256(GPU_RUNNER_PATH.read_bytes()).hexdigest()
        generated = f"""<!-- GPU_SOURCE_SHA256: {experiment_id} {source_hash} -->

#### 실제 모델 실험 계약

| 항목 | 값 |
|---|---|
| experiment | `{experiment_id}` |
| 코드 원본 | `labs/real_models/run_pythia.py` |
| model | `{model['repository']}` |
| requested revision | `{model['revision']}` |
| mode | `{experiment['mode']}` |
| hook | `gpt_neox.layers.{experiment['layer']}.mlp.dense_4h_to_h`, `{experiment['token']}` token |
| sequence 상한 | `{experiment['sequence_length']}` |
| peak VRAM 상한 | `{int(model['peak_vram_limit_bytes']) / 1024**3:.1f} GiB` |
| 실행 timeout | `{model['timeout_seconds']}초` |

```powershell
{command}
```
"""
        if not include_results:
            generated += "\n> 로컬 GPU 결과가 삽입되지 않음. 위 명령으로 고정된 실험을 재현할 수 있다.\n"
            text = text.replace(marker, generated.rstrip())
            continue

        manifest_path = BUILD_ROOT / "gpu" / "results" / experiment_id / "manifest.json"
        if not manifest_path.exists():
            raise SiteError(f"요청한 로컬 GPU manifest가 없다: {experiment_id}")
        manifest = json.loads(read_text(manifest_path))
        required = {
            "schema_version", "experiment_id", "lesson_id", "status", "source", "model",
            "inputs", "hook", "resources", "artifacts", "assertions", "summary", "failure",
        }
        missing = sorted(required - manifest.keys())
        if missing:
            raise SiteError(f"GPU manifest field 누락: {experiment_id} -> {', '.join(missing)}")
        if manifest.get("status") != "passed" or manifest.get("failure") is not None:
            raise SiteError(f"GPU manifest가 통과 상태가 아니다: {experiment_id}")
        if manifest.get("experiment_id") != experiment_id or manifest.get("lesson_id") != lesson_id:
            raise SiteError(f"GPU manifest identity가 다르다: {experiment_id}")
        if manifest["source"].get("sha256") != source_hash:
            raise SiteError(f"GPU runner와 manifest source hash가 다르다: {experiment_id}")
        if manifest["model"].get("repository") != model["repository"]:
            raise SiteError(f"GPU manifest model이 다르다: {experiment_id}")
        if manifest["model"].get("requested_revision") != model["revision"]:
            raise SiteError(f"GPU manifest revision이 다르다: {experiment_id}")
        if not manifest["model"].get("resolved_sha"):
            raise SiteError(f"GPU manifest resolved SHA가 없다: {experiment_id}")
        for artifact in manifest["artifacts"]:
            artifact_path = (ROOT / str(artifact["path"])).resolve()
            if not artifact_path.is_relative_to(BUILD_ROOT.resolve()) or not artifact_path.exists():
                raise SiteError(f"GPU artifact path가 없거나 안전하지 않다: {experiment_id}")
            if hashlib.sha256(artifact_path.read_bytes()).hexdigest() != artifact.get("sha256"):
                raise SiteError(f"GPU artifact hash가 다르다: {experiment_id}")
        serialized = json.dumps(manifest, ensure_ascii=False)
        if str(ROOT) in serialized:
            raise SiteError(f"GPU manifest에 absolute project path가 있다: {experiment_id}")

        resources = manifest["resources"]
        summary = json.dumps(manifest["summary"], ensure_ascii=False, sort_keys=True, indent=2)
        generated += f"""

#### 검증된 로컬 GPU 결과

```text
{summary}
```

| 검증 항목 | 값 |
|---|---|
| resolved model SHA | `{manifest['model']['resolved_sha']}` |
| source SHA-256 | `{manifest['source']['sha256']}` |
| peak allocated VRAM | `{int(resources['peak_allocated_bytes']) / 1024**3:.3f} GiB` |
| artifact 크기 | `{resources['artifact_bytes']} bytes` |
| 실행시간 | `{manifest['timestamps']['seconds']:.3f}초` |
"""
        text = text.replace(marker, generated.rstrip())
    return text


def build_nav(lessons: list[dict[str, object]]) -> list[dict[str, object]]:
    nav: list[dict[str, object]] = [
        {"홈": "index.md"},
        {"전체 학습경로": "curriculum.md"},
        {"N05 실행 환경": "N05-ENVIRONMENT.md"},
        {"N05 아키텍처 기준": "05-N05-ARCHITECTURE-BASELINE.md"},
        {"GPU·Pythia 실행 환경": "GPU-ENVIRONMENT.md"},
    ]
    for stage in STAGE_COUNTS:
        stage_items: list[dict[str, str]] = []
        for lesson in lessons:
            if lesson["stage"] != stage:
                continue
            label = f"{lesson['id']} {lesson['title']}"
            stage_items.append({label: str(lesson["relative_path"])})
        nav.append({STAGE_TITLES[stage]: stage_items})
    n05_items: list[dict[str, str]] = []
    for lesson in lessons:
        if lesson["stage"] != "N05":
            continue
        label = f"{lesson['id']} {lesson['title']}"
        n05_items.append({label: str(lesson["relative_path"])})
    if n05_items:
        nav.append({STAGE_TITLES["N05"]: n05_items})
    for stage in POST_N05_STAGE_SPECS:
        stage_items: list[dict[str, str]] = []
        for lesson in lessons:
            if lesson["stage"] != stage:
                continue
            label = f"{lesson['id']} {lesson['title']}"
            stage_items.append({label: str(lesson["relative_path"])})
        if stage_items:
            nav.append({STAGE_TITLES[stage]: stage_items})
    nav.append({"용어집": "glossary.md"})
    return nav


def assert_safe_build_root() -> None:
    root = ROOT.resolve()
    build = BUILD_ROOT.resolve()
    if build.parent != root or build.name != ".build":
        raise SiteError(f"안전하지 않은 build path: {build}")


def prepare() -> None:
    lessons = discover_all_lessons()
    assert_safe_build_root()
    if DOCS_DIR.exists():
        shutil.rmtree(DOCS_DIR)
    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)
    if CONFIG_PATH.exists():
        CONFIG_PATH.unlink()
    DOCS_DIR.mkdir(parents=True)

    write_text(DOCS_DIR / "index.md", prepare_homepage())
    write_text(DOCS_DIR / "curriculum.md", read_text(ROOT / "01-CURRICULUM.md"))
    write_text(DOCS_DIR / "N05-ENVIRONMENT.md", read_text(ROOT / "N05-ENVIRONMENT.md"))
    write_text(DOCS_DIR / "GPU-ENVIRONMENT.md", read_text(ROOT / "GPU-ENVIRONMENT.md"))
    write_text(
        DOCS_DIR / "05-N05-ARCHITECTURE-BASELINE.md",
        read_text(ROOT / "05-N05-ARCHITECTURE-BASELINE.md"),
    )
    write_text(DOCS_DIR / "glossary.md", read_text(ROOT / "04-GLOSSARY.md"))

    for lesson in lessons:
        source_path = lesson["path"]
        if not isinstance(source_path, Path):
            raise SiteError("lesson path type 오류")
        text = strip_editor_checklist(read_text(source_path), str(lesson["id"]))
        text = enable_markdown_in_details(text, str(lesson["id"]))
        text = add_search_alias(text, str(lesson["id"]))
        text = expand_n05_example(text, str(lesson["id"]))
        text = expand_gpu_experiments(text, str(lesson["id"]))
        destination = DOCS_DIR / str(lesson["relative_path"])
        write_text(destination, text)

    assets_source = ROOT / "site" / "assets"
    shutil.copytree(assets_source, DOCS_DIR / "assets")

    config = yaml.safe_load(read_text(BASE_CONFIG))
    config["docs_dir"] = "docs"
    config["site_dir"] = "site"
    config["nav"] = build_nav(lessons)
    write_text(CONFIG_PATH, yaml.safe_dump(config, allow_unicode=True, sort_keys=False))

    print(f"prepared lessons={len(lessons)} docs_dir={DOCS_DIR}")


class LinkCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.urls: list[str] = []
        self.details_count = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "details":
            self.details_count += 1
        attribute = "href" if tag in {"a", "link"} else "src" if tag in {"img", "script"} else None
        if not attribute:
            return
        values = dict(attrs)
        value = values.get(attribute)
        if value:
            self.urls.append(value)


def flatten_nav_paths(nav: list[object]) -> list[str]:
    paths: list[str] = []
    for item in nav:
        if isinstance(item, str):
            paths.append(item)
        elif isinstance(item, dict):
            for value in item.values():
                if isinstance(value, str):
                    paths.append(value)
                elif isinstance(value, list):
                    paths.extend(flatten_nav_paths(value))
    return paths


def output_html_for(markdown_relative_path: str) -> Path:
    relative = Path(markdown_relative_path)
    if relative.name == "index.md":
        return SITE_DIR / relative.with_suffix(".html")
    return SITE_DIR / relative.with_suffix("") / "index.html"


def resolve_generated_url(page: Path, url: str) -> Path | None:
    parsed = urlsplit(url)
    if parsed.scheme or parsed.netloc or not parsed.path:
        return None
    path = unquote(parsed.path)
    if path.startswith("/ai-math-guide/"):
        target = SITE_DIR / path.removeprefix("/ai-math-guide/")
    elif path.startswith("/"):
        target = SITE_DIR / path.lstrip("/")
    else:
        target = page.parent / path
    target = target.resolve()
    if path.endswith("/") or target.is_dir():
        target = target / "index.html"
    return target


def validate() -> None:
    foundation_lessons = discover_lessons()
    n05_lessons = discover_n05_lessons()
    post_n05_lessons = [
        lesson
        for stage in POST_N05_STAGE_SPECS
        for lesson in discover_post_n05_stage(stage)
    ]
    n05_registry = load_n05_example_registry()
    _, gpu_experiments = load_gpu_registries()
    lessons = foundation_lessons + n05_lessons + post_n05_lessons
    issues: list[str] = []
    _, reading_table_count, reading_cell_count = lint_english_readings()

    if not CONFIG_PATH.exists() or not SITE_DIR.exists():
        raise SiteError("prepare와 MkDocs build를 먼저 실행해야 한다")

    staged_foundations = sorted(
        (DOCS_DIR / "part-1-foundations").glob("M0[0-4]/M0[0-4]-*.md")
    )
    staged_n05 = sorted(
        (DOCS_DIR / "part-2-neural-computation" / "N05").glob("N05-*.md")
    )
    staged_post_n05 = [
        path
        for stage, spec in POST_N05_STAGE_SPECS.items()
        for path in sorted((DOCS_DIR / str(spec["directory"])).glob(f"{stage}-*.md"))
    ]
    staged_lessons = staged_foundations + staged_n05 + staged_post_n05
    if len(staged_foundations) != 70:
        issues.append(f"staged foundation lesson count={len(staged_foundations)}, expected=70")
    if len(staged_n05) != len(n05_lessons):
        issues.append(f"staged N05 lesson count={len(staged_n05)}, expected={len(n05_lessons)}")
    if len(staged_post_n05) != len(post_n05_lessons):
        issues.append(
            f"staged post-N05 lesson count={len(staged_post_n05)}, expected={len(post_n05_lessons)}"
        )

    original_checklists = sum(
        len(re.findall(r"^##\s+집필자 점검표\s*$", read_text(Path(str(lesson["path"]))), flags=re.MULTILINE))
        for lesson in lessons
    )
    if original_checklists != len(lessons):
        issues.append(
            f"original checklist count={original_checklists}, expected={len(lessons)}"
        )

    staged_text = "\n".join(read_text(path) for path in DOCS_DIR.rglob("*.md"))
    staged_reading_headers = staged_text.count("| Common spoken reading |")
    if staged_reading_headers != len(lessons):
        issues.append(
            f"staged Common spoken reading headers={staged_reading_headers}, "
            f"expected={len(lessons)}"
        )
    if "집필자 점검표" in staged_text:
        issues.append("staging에 집필자 점검표가 남았다")
    if "<details>" in staged_text:
        issues.append("staging에 Markdown 처리가 꺼진 details가 남았다")

    for internal in INTERNAL_DOCS:
        if (DOCS_DIR / internal).exists():
            issues.append(f"internal doc staged: {internal}")

    config = yaml.safe_load(read_text(CONFIG_PATH))
    nav_paths = flatten_nav_paths(config.get("nav", []))
    lesson_nav_paths = [path for path in nav_paths if re.match(r"part-1-foundations/M0[0-4]/M0[0-4]-", path)]
    if len(lesson_nav_paths) != 70 or len(set(lesson_nav_paths)) != 70:
        issues.append(f"lesson nav count/unique={len(lesson_nav_paths)}/{len(set(lesson_nav_paths))}")
    n05_nav_paths = [
        path for path in nav_paths if re.match(r"part-2-neural-computation/N05/N05-", path)
    ]
    if len(n05_nav_paths) != len(n05_lessons) or len(set(n05_nav_paths)) != len(n05_lessons):
        issues.append(
            f"N05 nav count/unique={len(n05_nav_paths)}/{len(set(n05_nav_paths))}, "
            f"expected={len(n05_lessons)}"
        )
    post_nav_paths = [
        path for path in nav_paths if re.match(r"part-3-interpretability/I0[6-8]/I0[6-8]-", path)
    ]
    if len(post_nav_paths) != len(post_n05_lessons) or len(set(post_nav_paths)) != len(post_n05_lessons):
        issues.append(
            f"post-N05 nav count/unique={len(post_nav_paths)}/{len(set(post_nav_paths))}, "
            f"expected={len(post_n05_lessons)}"
        )

    for lesson in n05_lessons:
        lesson_id = str(lesson["id"])
        example_spec = n05_registry.get(lesson_id)
        if example_spec is None:
            continue
        example_id = str(example_spec["example_id"])
        source_path = Path(str(example_spec["source_path"]))
        source = read_text(source_path).rstrip()
        staged_path = DOCS_DIR / str(lesson["relative_path"])
        staged_source = read_text(staged_path)
        if f"```python\n{source}\n```" not in staged_source:
            issues.append(f"staged code differs from source: {lesson_id}")
        result_path = BUILD_ROOT / "n05" / "results" / f"{example_id}.json"
        if not result_path.exists():
            issues.append(f"generated result missing: {example_id}")

    include_gpu_results = os.environ.get("AI_MATH_GPU_RESULTS") == "1"
    for lesson in post_n05_lessons:
        lesson_id = str(lesson["id"])
        staged_source = read_text(DOCS_DIR / str(lesson["relative_path"]))
        for experiment_id, experiment in gpu_experiments.items():
            if experiment.get("lesson_id") != lesson_id:
                continue
            source_hash = hashlib.sha256(GPU_RUNNER_PATH.read_bytes()).hexdigest()
            if f"GPU_SOURCE_SHA256: {experiment_id} {source_hash}" not in staged_source:
                issues.append(f"GPU source hash marker missing from staging: {lesson_id}/{experiment_id}")
            placeholder = "로컬 GPU 결과가 삽입되지 않음"
            if include_gpu_results and placeholder in staged_source:
                issues.append(f"GPU result mode still has placeholder: {lesson_id}/{experiment_id}")
            if not include_gpu_results and placeholder not in staged_source:
                issues.append(f"CPU build is missing GPU placeholder: {lesson_id}/{experiment_id}")

    missing_pages: list[str] = []
    lesson_html_paths: list[Path] = []
    for lesson in lessons:
        page = output_html_for(str(lesson["relative_path"]))
        lesson_html_paths.append(page)
        if not page.exists():
            missing_pages.append(str(lesson["id"]))
    if missing_pages:
        issues.append("missing lesson HTML: " + ", ".join(missing_pages))

    for path in (
        SITE_DIR / "index.html",
        SITE_DIR / "curriculum" / "index.html",
        SITE_DIR / "N05-ENVIRONMENT" / "index.html",
        SITE_DIR / "05-N05-ARCHITECTURE-BASELINE" / "index.html",
        SITE_DIR / "GPU-ENVIRONMENT" / "index.html",
        SITE_DIR / "glossary" / "index.html",
    ):
        if not path.exists():
            issues.append(f"missing public page: {path.relative_to(SITE_DIR)}")

    html_paths = sorted(SITE_DIR.rglob("*.html"))
    combined_html = "\n".join(read_text(path) for path in html_paths)
    html_reading_headers = combined_html.count("<th>Common spoken reading</th>")
    if html_reading_headers != len(lessons):
        issues.append(
            f"HTML Common spoken reading headers={html_reading_headers}, expected={len(lessons)}"
        )
    for spoken_reading in (
        "the exponential of x",
        "partial f over partial x",
        "the gradient of f with respect to x",
        "the Jacobian of f at x",
        "P of A given B",
        "the expectation of X",
        "K L divergence from p to q",
    ):
        if f"<code>{spoken_reading}</code>" not in combined_html:
            issues.append(f"spoken reading missing from HTML: {spoken_reading}")
    if "집필자 점검표" in combined_html:
        issues.append("generated HTML에 집필자 점검표가 남았다")
    for lesson in n05_lessons:
        lesson_id = str(lesson["id"])
        example_spec = n05_registry.get(lesson_id)
        if example_spec is None:
            continue
        example_id = str(example_spec["example_id"])
        source_path = Path(str(example_spec["source_path"]))
        source_hash = hashlib.sha256(source_path.read_bytes()).hexdigest()
        marker = f"N05_SOURCE_SHA256: {example_id} {source_hash}"
        page = output_html_for(str(lesson["relative_path"]))
        if page.exists() and marker not in read_text(page):
            issues.append(f"N05 source hash marker missing from HTML: {lesson_id}")
    for lesson in post_n05_lessons:
        lesson_id = str(lesson["id"])
        page = output_html_for(str(lesson["relative_path"]))
        page_text = read_text(page) if page.exists() else ""
        for experiment_id, experiment in gpu_experiments.items():
            if experiment.get("lesson_id") != lesson_id:
                continue
            source_hash = hashlib.sha256(GPU_RUNNER_PATH.read_bytes()).hexdigest()
            marker = f"GPU_SOURCE_SHA256: {experiment_id} {source_hash}"
            if marker not in page_text:
                issues.append(f"GPU source hash marker missing from HTML: {lesson_id}/{experiment_id}")
    for internal in INTERNAL_DOCS:
        if internal in combined_html:
            issues.append(f"generated HTML에 internal filename이 남았다: {internal}")

    source_details = sum(read_text(Path(str(lesson["path"]))).count("<details>") for lesson in lessons)
    html_details = 0
    broken_urls: list[str] = []
    for page in html_paths:
        collector = LinkCollector()
        collector.feed(read_text(page))
        html_details += collector.details_count
        for url in collector.urls:
            target = resolve_generated_url(page, url)
            if target is not None and not target.exists():
                broken_urls.append(f"{page.relative_to(SITE_DIR)} -> {url}")
    if html_details != source_details:
        issues.append(f"details count source/html={source_details}/{html_details}")
    if broken_urls:
        issues.append("broken generated links/assets:\n  " + "\n  ".join(broken_urls[:30]))

    arithmatex_count = combined_html.count('class="arithmatex"')
    if arithmatex_count == 0:
        issues.append("arithmatex wrapper가 생성되지 않았다")

    search_path = SITE_DIR / "search" / "search_index.json"
    search_hits: dict[str, list[str]] = {}
    if not search_path.exists():
        issues.append("search index가 없다")
    else:
        search_data = json.loads(read_text(search_path))
        documents = search_data.get("docs", [])
        for term, expected_id in SEARCH_TERMS.items():
            hits = [
                str(document.get("location", ""))
                for document in documents
                if term.casefold()
                in f"{document.get('title', '')} {document.get('text', '')}".casefold()
            ]
            search_hits[term] = hits
            if not hits:
                issues.append(f"search term missing: {term} -> {expected_id}")

    summary = {
        "source_lessons": len(lessons),
        "foundation_lessons": len(foundation_lessons),
        "n05_written_lessons": len(n05_lessons),
        "n05_planned_lessons": N05_PLANNED_COUNT,
        "post_n05_written_lessons": len(post_n05_lessons),
        "post_n05_by_stage": {
            stage: sum(lesson["stage"] == stage for lesson in post_n05_lessons)
            for stage in POST_N05_STAGE_SPECS
        },
        "staged_lessons": len(staged_lessons),
        "generated_lesson_pages": sum(path.exists() for path in lesson_html_paths),
        "spoken_reading_tables": reading_table_count,
        "spoken_reading_cells": reading_cell_count,
        "html_spoken_reading_headers": html_reading_headers,
        "broken_links_or_assets": len(broken_urls),
        "source_details": source_details,
        "generated_details": html_details,
        "arithmatex_wrappers": arithmatex_count,
        "checklist_exposure": combined_html.count("집필자 점검표"),
        "n05_generated_results": sum(
            (
                BUILD_ROOT
                / "n05"
                / "results"
                / f"{str(example_spec['example_id'])}.json"
            ).exists()
            for example_spec in n05_registry.values()
        ),
        "gpu_result_mode": include_gpu_results,
        "gpu_registered_experiments": len(gpu_experiments),
        "search_hits": {term: len(hits) for term, hits in search_hits.items()},
    }
    write_text(BUILD_ROOT / "validation.json", json.dumps(summary, ensure_ascii=False, indent=2) + "\n")

    if issues:
        raise SiteError("generated-site validation 실패:\n- " + "\n- ".join(issues))
    print(json.dumps(summary, ensure_ascii=False, indent=2))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("audit", "prepare", "validate"))
    args = parser.parse_args()
    try:
        if args.command == "audit":
            foundation_lessons = discover_lessons()
            n05_lessons = discover_n05_lessons()
            post_n05_lessons = [
                lesson
                for stage in POST_N05_STAGE_SPECS
                for lesson in discover_post_n05_stage(stage)
            ]
            lessons = foundation_lessons + n05_lessons + post_n05_lessons
            _, table_count, cell_count = lint_english_readings()
            print(
                "source audit passed: "
                f"lessons={len(lessons)} foundations={len(foundation_lessons)} "
                f"n05={len(n05_lessons)}/{N05_PLANNED_COUNT} reading_tables={table_count} "
                f"post_n05={len(post_n05_lessons)} reading_cells={cell_count}"
            )
        elif args.command == "prepare":
            prepare()
        else:
            validate()
    except SiteError as error:
        print(str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
