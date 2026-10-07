#!/usr/bin/env python3
"""Prepare and validate the private-review MkDocs site."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from html.parser import HTMLParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml
import markdown


ROOT = Path(__file__).resolve().parents[1]
BUILD_ROOT = ROOT / ".build"
DOCS_DIR = BUILD_ROOT / "docs"
SITE_DIR = BUILD_ROOT / "site"
CONFIG_PATH = BUILD_ROOT / "mkdocs.yml"
BASE_CONFIG = ROOT / "site" / "mkdocs.base.yml"
CONTENT_ROOT = ROOT
LANGUAGE = "ko"
ALLOW_PARTIAL = False
PUBLIC_ROOT = "https://leeklim.github.io/ai-math-guide/"
PUBLIC_PATH = "/ai-math-guide/"
PUBLIC_DOCUMENTS = {
    "README.md": "index.md",
    "01-CURRICULUM.md": "curriculum.md",
    "04-GLOSSARY.md": "glossary.md",
    "N05-ENVIRONMENT.md": "N05-ENVIRONMENT.md",
    "GPU-ENVIRONMENT.md": "GPU-ENVIRONMENT.md",
    "05-N05-ARCHITECTURE-BASELINE.md": "05-N05-ARCHITECTURE-BASELINE.md",
}
EN_STAGE_TITLES = {
    "M00": "M00 Reading mathematical notation",
    "M01": "M01 Change and calculus",
    "M02": "M02 Vectors and matrices",
    "M03": "M03 Abstract linear algebra and matrix calculus",
    "M04": "M04 Probability, statistics, and information theory",
    "N05": "N05 Neural computation",
    "I06": "I06 Interpreting representations",
    "I07": "I07 Attribution, causality, and mechanisms",
    "I08": "I08 Learning dynamics",
    "A09-GEO": "A09-GEO Differential geometry and representation spaces",
    "A09-DYN": "A09-DYN Dynamical systems and stochastic processes",
    "A09-SYM": "A09-SYM Groups, symmetry, and representation alignment",
    "A09-LRN": "A09-LRN Statistical learning theory",
    "A09-KER": "A09-KER Kernels, function spaces, and operators",
    "A09-RMT": "A09-RMT Random matrices and high-dimensional statistics",
    "A09-CAU": "A09-CAU Advanced causal inference",
}
EN_SPOKEN_READING_CHECKLIST = (
    "Common spoken reading uses actual English academic speech, without Korean "
    "transliteration or mechanical descriptions of symbol placement."
)

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
    "A09-GEO": "A09-GEO 미분기하학과 표현공간",
    "A09-DYN": "A09-DYN 동역학계와 확률과정",
    "A09-SYM": "A09-SYM 군론·대칭성과 표현 정렬",
    "A09-LRN": "A09-LRN 통계학습이론",
    "A09-KER": "A09-KER Kernel·함수공간·operator",
    "A09-RMT": "A09-RMT Random matrix·고차원 통계",
    "A09-CAU": "A09-CAU 고급 인과추론",
}

N05_PLANNED_COUNT = 28
N05_REGISTRY_PATH = ROOT / "labs" / "N05" / "examples.json"
POST_N05_STAGE_SPECS = {
    "I06": {"part": 3, "planned_count": 15, "directory": "part-3-interpretability/I06"},
    "I07": {"part": 3, "planned_count": 17, "directory": "part-3-interpretability/I07"},
    "I08": {"part": 3, "planned_count": 13, "directory": "part-3-interpretability/I08"},
    "A09-GEO": {"part": 4, "planned_count": 8, "directory": "part-4-advanced/A09-GEO"},
    "A09-DYN": {"part": 4, "planned_count": 8, "directory": "part-4-advanced/A09-DYN"},
    "A09-SYM": {"part": 4, "planned_count": 8, "directory": "part-4-advanced/A09-SYM"},
    "A09-LRN": {"part": 4, "planned_count": 8, "directory": "part-4-advanced/A09-LRN"},
    "A09-KER": {"part": 4, "planned_count": 8, "directory": "part-4-advanced/A09-KER"},
    "A09-RMT": {"part": 4, "planned_count": 8, "directory": "part-4-advanced/A09-RMT"},
    "A09-CAU": {"part": 4, "planned_count": 8, "directory": "part-4-advanced/A09-CAU"},
}
GPU_EXPERIMENT_REGISTRY_PATH = ROOT / "labs" / "real_models" / "experiments.json"
GPU_MODEL_REGISTRY_PATH = ROOT / "labs" / "real_models" / "models.json"
GPU_RUNNER_PATH = ROOT / "labs" / "real_models" / "run_pythia.py"
STAGE_EXAMPLE_REGISTRY_PATHS = {
    "I06": ROOT / "labs" / "I06" / "examples.json",
    "I07": ROOT / "labs" / "I07" / "examples.json",
    "I08": ROOT / "labs" / "I08" / "examples.json",
}

INTERNAL_DOCS = {
    "00-PROJECT-SPEC.md",
    "02-STYLE-AND-NOTATION.md",
    "03-PROGRESS.md",
}

SEARCH_TERMS = {
    "자코비안": "M03-11",
    "특이값분해": "M02-13",
    "상호정보량": "04-GLOSSARY.md",
    "mutual information": "M04-14",
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


def select_language(language: str, *, allow_partial: bool = False, isolated: bool = False) -> None:
    """Select content/output locations without moving the shared repository root."""
    global LANGUAGE, ALLOW_PARTIAL, CONTENT_ROOT, DOCS_DIR, SITE_DIR, CONFIG_PATH
    if language not in {"ko", "en"} or (allow_partial and language != "en"):
        raise SiteError("--allow-partial is only available with --lang en")
    LANGUAGE, ALLOW_PARTIAL = language, allow_partial
    CONTENT_ROOT = ROOT if language == "ko" else ROOT / "translations" / "en"
    locale_build = BUILD_ROOT / language if language == "en" or isolated else BUILD_ROOT
    DOCS_DIR, SITE_DIR = locale_build / "docs", locale_build / "site"
    CONFIG_PATH = locale_build / "mkdocs.yml"


def checklist_title() -> str:
    return "Author checklist" if LANGUAGE == "en" else "집필자 점검표"


def page_url(relative: str) -> str:
    path = Path(relative)
    return "" if path.name == "index.md" else path.with_suffix("").as_posix() + "/"


def english_pages() -> list[str]:
    root = ROOT / "translations" / "en"
    pages = [page_url(target) for source, target in PUBLIC_DOCUMENTS.items() if (root / source).is_file()]
    pages.extend(page_url(path.relative_to(root).as_posix()) for path in root.glob("part-*/*/*.md"))
    if ALLOW_PARTIAL and "" not in pages:
        pages.append("")  # Explicit preview landing page, not a translated lesson.
    return sorted(set(pages))


def localized_config() -> dict[str, object]:
    config = yaml.safe_load(read_text(BASE_CONFIG))
    config["theme"]["custom_dir"] = Path(os.path.relpath(ROOT / "site" / "overrides", CONFIG_PATH.parent)).as_posix()
    config["extra"]["bilingual"] = {
        "root": PUBLIC_PATH, "en_pages": english_pages(),
        "partial_preview": LANGUAGE == "en" and ALLOW_PARTIAL,
    }
    if LANGUAGE == "en":
        config["site_name"] = "Mathematics and Methods for Model Interpretability"
        config["site_description"] = "Mathematics for reading AI papers and designing model interpretability experiments"
        config["site_url"] = PUBLIC_ROOT + "en/"
        config["theme"]["language"] = "en"
        for palette in config["theme"]["palette"]:
            palette["toggle"]["name"] = (
                "Switch to dark mode" if palette["scheme"] == "default" else "Switch to light mode"
            )
        config["extra"]["consent"].update({
            "title": "Visitor analytics consent",
            "description": (
                "The site uses Google Analytics 4 to understand visits and page usage. "
                "If you consent, visit information is sent to Google and analytics cookies are used. "
                "Select the checkbox below and choose Accept to allow analytics. "
                "You can reject analytics and still read every lesson. "
                "Change your choice using Analytics cookie settings in the footer. "
                '<a href="https://policies.google.com/privacy?hl=en" target="_blank" rel="noopener">Google Privacy Policy</a>'
            ),
        })
        config["extra"]["consent"]["cookies"]["analytics"]["name"] = "Visitor analytics (Google Analytics 4)"
        config["copyright"] = '<a href="#__consent">Analytics cookie settings</a>'
        config["plugins"] = [{"search": {"lang": "en"}}]
    return config


def source_snapshot(lessons: list[dict[str, object]]) -> dict[str, object]:
    sources = [Path(lesson["path"]) for lesson in lessons]
    sources.extend(CONTENT_ROOT / source for source in PUBLIC_DOCUMENTS if (CONTENT_ROOT / source).is_file())
    sources.extend([BASE_CONFIG, Path(__file__).resolve()])
    sources.extend((ROOT / "site" / "page-metadata").glob("*.json"))
    sources.extend(path for directory in (ROOT / "site" / "assets", ROOT / "site" / "overrides", ROOT / "figures" / "assets") for path in directory.rglob("*") if path.is_file())
    registries: dict[str, object] = {}
    stages = {str(lesson["stage"]) for lesson in lessons if "stage" in lesson}
    for stage in stages & {"N05", "I06", "I07", "I08"}:
        registry = load_n05_example_registry() if stage == "N05" else load_stage_example_registry(stage)
        for lesson in lessons:
            lesson_id = str(lesson["id"])
            if lesson.get("stage") != stage or lesson_id not in registry:
                continue
            entry = registry[lesson_id]
            code = Path(str(entry["source_path"]))
            registries[lesson_id] = {**entry, "source_path": code.relative_to(ROOT).as_posix()}
            sources.extend([code, BUILD_ROOT / stage.lower() / "results" / f"{entry['example_id']}.json"])
    gpu_results = os.environ.get("AI_MATH_GPU_RESULTS") == "1"
    models, experiments = load_gpu_registries()
    lesson_ids = {str(lesson["id"]) for lesson in lessons if "id" in lesson}
    for experiment_id, experiment in experiments.items():
        if experiment["lesson_id"] not in lesson_ids:
            continue
        registries[experiment_id] = {"experiment": experiment, "model": models[str(experiment["model_key"])]}
        sources.append(GPU_RUNNER_PATH)
        if gpu_results:
            manifest = BUILD_ROOT / "gpu" / "results" / experiment_id / "manifest.json"
            sources.append(manifest)
            if manifest.exists():
                for artifact in json.loads(read_text(manifest))["artifacts"]:
                    path = (ROOT / str(artifact["path"])).resolve()
                    if not path.is_relative_to(BUILD_ROOT.resolve()):
                        raise SiteError(f"unsafe GPU artifact path: {experiment_id}")
                    sources.append(path)
    return {
        "language": LANGUAGE, "partial_preview": ALLOW_PARTIAL,
        "english_pages": english_pages(), "gpu_result_mode": gpu_results, "consumed_registries": registries,
        "sources": {path.relative_to(ROOT).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None for path in set(sources)},
    }


def assert_current_sources(lessons: list[dict[str, object]]) -> None:
    snapshot = CONFIG_PATH.parent / "source-snapshot.json"
    if not snapshot.exists() or json.loads(read_text(snapshot)) != source_snapshot(lessons):
        raise SiteError("locale staging is stale; run prepare and strict build again")


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


def load_stage_example_registry(stage: str) -> dict[str, dict[str, object]]:
    registry_path = STAGE_EXAMPLE_REGISTRY_PATHS.get(stage)
    if registry_path is None:
        return {}
    data = json.loads(read_text(registry_path))
    if data.get("schema_version") != 1 or not isinstance(data.get("examples"), list):
        raise SiteError(f"{stage} example registry schema가 잘못됐다")
    registry: dict[str, dict[str, object]] = {}
    example_ids: set[str] = set()
    for entry in data["examples"]:
        lesson_id = str(entry.get("lesson_id", ""))
        example_id = str(entry.get("example_id", ""))
        module = str(entry.get("module", ""))
        source = str(entry.get("source", ""))
        if not re.fullmatch(rf"{stage}-\d{{2}}", lesson_id):
            raise SiteError(f"{stage} registry lesson ID가 잘못됐다: {lesson_id}")
        if not re.fullmatch(rf"{stage.lower()}_\d{{2}}_[a-z0-9_]+", example_id):
            raise SiteError(f"{stage} registry example ID가 잘못됐다: {example_id}")
        if lesson_id in registry or example_id in example_ids:
            raise SiteError(f"{stage} registry entry가 중복됐다: {lesson_id}/{example_id}")
        source_path = (ROOT / source).resolve()
        if not source_path.is_relative_to(ROOT) or not source_path.exists():
            raise SiteError(f"{stage} registry source가 없거나 안전하지 않다: {source}")
        registry[lesson_id] = {
            "example_id": example_id,
            "module": module,
            "source_path": source_path,
        }
        example_ids.add(example_id)
    return registry


def load_i06_example_registry() -> dict[str, dict[str, object]]:
    return load_stage_example_registry("I06")


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


def find_raw_math_pipes_in_tables(path: Path, text: str) -> list[str]:
    """Find unescaped pipes that Markdown would split even though they are inside math."""
    issues: list[str] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not line.startswith("|"):
            continue
        in_math = False
        in_code = False
        for index, char in enumerate(line):
            escaped = index > 0 and line[index - 1] == "\\"
            if char == "`" and not escaped:
                in_code = not in_code
            elif char == "$" and not in_code and not escaped:
                in_math = not in_math
            elif char == "|" and in_math and not in_code and not escaped:
                issues.append(
                    f"{path}:{line_number}:{index + 1}: "
                    "unescaped raw pipe inside table math"
                )
    return issues


def lint_english_readings(
    sources: list[tuple[Path, str]] | None = None,
    *, language: str | None = None,
) -> tuple[list[str], int, int]:
    """Validate notation-table readings and return issues, table count, and cell count."""
    language = language or LANGUAGE
    if sources is None and language == "en":
        sources = [(path, read_text(path)) for path in sorted(CONTENT_ROOT.glob("part-*/*/*.md"))]
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
        post_n05_sources.extend(
            (path, read_text(path))
            for path in sorted(ROOT.glob("part-4-advanced/A09-*/A09-*-*.md"))
        )
        sources = foundation_sources + n05_sources + post_n05_sources

    issues: list[str] = []
    entries: dict[str, list[tuple[str, Path, int]]] = {}
    table_count = 0
    cell_count = 0

    for path, text in sources:
        issues.extend(find_raw_math_pipes_in_tables(path, text))
        lines = text.splitlines()
        file_table_count = 0
        original_column_count = None
        source_path = path.resolve()
        if language == "en" and source_path.is_relative_to(CONTENT_ROOT.resolve()):
            original = ROOT / source_path.relative_to(CONTENT_ROOT.resolve())
            if original.is_file():
                for original_line in read_text(original).splitlines():
                    original_header = split_markdown_table_row(original_line)
                    if original_header and original_header[0] in {"기호·용어", "표기·용어"}:
                        original_column_count = len(original_header)
                        break
        for index, line in enumerate(lines):
            if not line.startswith("|"):
                continue
            header = split_markdown_table_row(line)
            first_headers = {"Symbol or term"} if language == "en" else {"기호·용어", "표기·용어"}
            if not header or header[0] not in first_headers:
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
            if language == "en":
                if len(header) not in {3, 4} or header[2] not in {"Meaning", "Meaning in this lesson"} or any(not cell or HANGUL_RE.search(cell) for cell in header[2:]):
                    issues.append(f"{path}:{index + 1}: English notation-table headers differ from the standard")
                if original_column_count is not None and len(header) != original_column_count:
                    issues.append(f"{path}:{index + 1}: English notation-table column count differs from the Korean source")

            row_index = index + 2
            while row_index < len(lines) and lines[row_index].startswith("|"):
                cells = split_markdown_table_row(lines[row_index])
                location = f"{path}:{row_index + 1}"
                if language == "en" and len(cells) != len(header):
                    issues.append(f"{location}: English notation-table row width differs from its header")
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
        required_check = EN_SPOKEN_READING_CHECKLIST if language == "en" else SPOKEN_READING_CHECKLIST
        if required_check not in text:
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


def discover_english_stage(stage: str, directory: str) -> list[dict[str, object]]:
    """Audit actual translations against the unchanged Korean lesson inventory."""
    lessons: list[dict[str, object]] = []
    issues: list[str] = []
    originals = sorted((ROOT / directory).glob(f"{stage}-*.md"))
    known = {path.name for path in originals}
    for extra in (CONTENT_ROOT / directory).glob("*.md"):
        if extra.name not in known:
            issues.append(f"unknown English lesson: {extra.relative_to(CONTENT_ROOT)}")
    for original in originals:
        relative = original.relative_to(ROOT).as_posix()
        path = CONTENT_ROOT / relative
        if not path.exists():
            if not ALLOW_PARTIAL:
                issues.append(f"missing English lesson: {relative}")
            continue
        source, text = read_text(original), read_text(path)
        ko_meta, meta = parse_frontmatter(original, source), parse_frontmatter(path, text)
        lesson_id, title = str(ko_meta["id"]), str(meta.get("title", ""))
        for field in ("id", "part", "stage", "prerequisites"):
            if meta.get(field) != ko_meta.get(field):
                issues.append(f"English frontmatter differs: {lesson_id}/{field}")
        if meta.get("status") != "complete":
            issues.append(f"English source status is not complete: {lesson_id}")
        if not title or HANGUL_RE.search(title) or H1_RE.findall(text) != [f"{lesson_id}. {title}"]:
            issues.append(f"English title/H1 mismatch: {lesson_id}")
        if len(re.findall(r"^##\s+Author checklist\s*$", text, re.MULTILINE)) != 1:
            issues.append(f"English Author checklist count is not one: {lesson_id}")
        if source.count("<details>") != text.count("<details>"):
            issues.append(f"English solution count differs: {lesson_id}")
        if text.count("<summary>Show solution</summary>") != text.count("<details>"):
            issues.append(f"English solution summaries differ: {lesson_id}")
        headings = lambda value: re.findall(r"^(#{2,4})\s", value, re.MULTILINE)
        if headings(source) != headings(text):
            issues.append(f"English heading structure differs: {lesson_id}")
        images = lambda value: re.findall(r"!\[[^\]]*\]\(([^)]+)\)", value)
        if images(source) != images(text):
            issues.append(f"English figure paths/order differ: {lesson_id}")
        markers = lambda value: re.findall(r"<!--\s*((?:N05|I06|I07|I08)_EXAMPLE|GPU_EXPERIMENT):\s*([^>]+?)\s*-->", value)
        if markers(source) != markers(text):
            issues.append(f"English example markers differ: {lesson_id}")
        if len(re.findall(r"^\\\[$", text, re.MULTILINE)) != len(re.findall(r"^\\\]$", text, re.MULTILINE)):
            issues.append(f"English display math mismatch: {lesson_id}")
        for number, line in enumerate(text.splitlines(), 1):
            if len(re.findall(r"(?<!\\)\$", line)) % 2:
                issues.append(f"English inline math mismatch: {lesson_id}:{number}")
                break
        for href in LINK_RE.findall(strip_editor_checklist(text, lesson_id)):
            parsed = urlsplit(href)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            shared = (original.parent / unquote(parsed.path)).resolve()
            if not shared.is_relative_to(ROOT) or not shared.exists():
                issues.append(f"broken English source link: {lesson_id} -> {href}")
            elif shared.suffix == ".md" and not ALLOW_PARTIAL:
                if not (CONTENT_ROOT / shared.relative_to(ROOT)).exists():
                    issues.append(f"English link points to untranslated document: {lesson_id} -> {href}")
        lessons.append({"id": lesson_id, "title": title, "stage": stage, "path": path, "relative_path": relative})
    sources = [(Path(lesson["path"]), read_text(Path(lesson["path"]))) for lesson in lessons]
    reading_issues, tables, _ = lint_english_readings(sources, language="en")
    issues.extend(reading_issues)
    for lesson in lessons:
        original = ROOT / str(lesson["relative_path"])
        ko_rows = spoken_reading_rows(read_text(original), language="ko")
        en_rows = spoken_reading_rows(read_text(Path(lesson["path"])), language="en")
        if len(ko_rows) != len(en_rows) or any(
            ko_reading != en_reading or (
                re.findall(r"\$[^$]*\$|\\\(.*?\\\)", ko_symbol) != re.findall(r"\$[^$]*\$|\\\(.*?\\\)", en_symbol)
                if HANGUL_RE.search(ko_symbol) else ko_symbol != en_symbol
            )
            for (ko_symbol, ko_reading), (en_symbol, en_reading) in zip(ko_rows, en_rows)
        ):
            issues.append(f"English symbols/spoken readings differ: {lesson['id']}")
        diagnostics = find_korean_prose(Path(lesson["path"]), read_text(Path(lesson["path"])))
        if diagnostics:
            print("English prose review required:\n  " + "\n  ".join(diagnostics), file=sys.stderr)
    if tables != len(lessons):
        issues.append(f"English reading table count={tables}, expected={len(lessons)}")
    if issues:
        raise SiteError("English source audit failed:\n- " + "\n- ".join(issues))
    return lessons


def spoken_reading_rows(text: str, *, language: str) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    in_table = False
    for line in text.splitlines():
        if not line.startswith("|"):
            in_table = False
            continue
        cells = split_markdown_table_row(line)
        if cells and cells[0] in ({"Symbol or term"} if language == "en" else {"기호·용어", "표기·용어"}):
            in_table = True
        elif in_table and len(cells) > 1 and not re.fullmatch(r":?-+:?", cells[0]):
            rows.append((cells[0], cells[1]))
    return rows


def find_korean_prose(path: Path, text: str) -> list[str]:
    """Report residual Korean outside code/stdout; intentional quotations need review."""
    text = FRONTMATTER_RE.sub(lambda match: "\n" * match.group(0).count("\n"), text, count=1)
    diagnostics: list[str] = []
    fence: str | None = None
    hidden = False
    for number, line in enumerate(text.splitlines(), 1):
        marker = re.match(r"\s*(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)[0]
            fence = None if fence == token else fence or token
            continue
        if fence:
            continue
        if re.fullmatch(r"##\s+Author checklist\s*", line):
            hidden = True
        elif re.match(r"#{1,2}\s", line):
            hidden = False
        if not hidden and HANGUL_RE.search(line):
            name = path.relative_to(CONTENT_ROOT).as_posix() if path.is_relative_to(CONTENT_ROOT) else path.name
            diagnostics.append(f"{name}:{number}: {line.strip()[:180]}")
    return diagnostics


def discover_lessons() -> list[dict[str, object]]:
    if LANGUAGE == "en":
        return [lesson for stage in STAGE_COUNTS for lesson in discover_english_stage(stage, f"part-1-foundations/{stage}")]
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
    if LANGUAGE == "en":
        return discover_english_stage("N05", "part-2-neural-computation/N05")
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
    if LANGUAGE == "en":
        return discover_english_stage(stage, str(spec["directory"]))
    stage_dir = ROOT / str(spec["directory"])
    paths = sorted(stage_dir.glob(f"{stage}-*.md")) if stage_dir.exists() else []
    _, experiments = load_gpu_registries()
    cpu_registry = load_stage_example_registry(stage)
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
        cpu_spec = cpu_registry.get(lesson_id)
        expected_cpu = [str(cpu_spec["example_id"])] if cpu_spec else []
        cpu_markers = re.findall(rf"<!--\s*{stage}_EXAMPLE:\s*([a-z0-9_]+)\s*-->", text)
        if cpu_markers != expected_cpu:
            issues.append(
                f"{stage} example marker mismatch: {lesson_id}={cpu_markers}, expected={expected_cpu}"
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
    missing_cpu_lessons = sorted(set(cpu_registry) - written_ids)
    if missing_cpu_lessons:
        issues.append(
            f"{stage} registry points to unwritten lessons: " + ", ".join(missing_cpu_lessons)
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
        fence_marker: str | None = None
        while index < len(lines):
            fence = re.match(r"^ {0,3}(`{3,}|~{3,})", lines[index])
            if fence:
                marker = fence.group(1)
                if fence_marker is None:
                    fence_marker = marker
                elif (
                    marker[0] == fence_marker[0]
                    and len(marker) >= len(fence_marker)
                    and not lines[index][fence.end():].strip()
                ):
                    fence_marker = None
            elif fence_marker is None and re.match(r"^#{1,2}\s+", lines[index]):
                break
            index += 1

    if required and removed != section_names:
        missing = ", ".join(sorted(section_names - removed))
        raise SiteError(f"제거할 H2 section을 찾지 못했다: {missing}")
    return "".join(output).rstrip() + "\n"


def prepare_homepage() -> str:
    if LANGUAGE == "en":
        path = CONTENT_ROOT / "README.md"
        if not path.exists():
            if not ALLOW_PARTIAL:
                raise SiteError("missing English public document: README.md")
            return (
                "# Mathematics and Methods for Model Interpretability\n\n"
                "This is a partial English preview. Only the translated lessons are included. "
                "Untranslated links open the Korean edition; no Korean lesson is presented as an English translation.\n\n"
                f"[Read the Korean edition]({PUBLIC_PATH})\n"
            )
        return read_text(path)
    source = read_text(ROOT / "README.md")
    source = remove_h2_sections(source, {"기준 문서", "현재 상태", "로컬 HTML 검수"}, required=True)
    return (
        source.rstrip()
        + "\n\n## 읽기 시작\n\n"
        + "- [전체 학습경로](curriculum.md)\n"
        + "- [첫 단원: 수, 변수와 상수](part-1-foundations/M00/M00-01-numbers-variables.md)\n"
        + "- [용어집](glossary.md)\n"
    )


def strip_editor_checklist(text: str, lesson_id: str) -> str:
    title = checklist_title()
    if len(re.findall(rf"^##\s+{re.escape(title)}\s*$", text, flags=re.MULTILINE)) != 1:
        raise SiteError(f"집필자 점검표 section 수가 1이 아니다: {lesson_id}")
    return remove_h2_sections(text, {title}, required=True)


def enable_markdown_in_details(text: str, lesson_id: str) -> str:
    details_count = text.count("<details>")
    converted = text.replace("<details>", '<details markdown="1">')
    if converted.count('<details markdown="1">') != details_count:
        raise SiteError(f"details Markdown 변환에 실패했다: {lesson_id}")
    return converted


def add_search_alias(text: str, lesson_id: str) -> str:
    if LANGUAGE == "en" or lesson_id != "M03-11":
        return text
    lines = text.splitlines(keepends=True)
    for index, line in enumerate(lines):
        if line.startswith("# "):
            lines.insert(index + 1, "\n<span class=\"search-alias\">자코비안 야코비안</span>\n")
            return "".join(lines)
    raise SiteError("M03-11 H1 뒤에 검색 별칭을 넣지 못했다")


def localize_execution_prose(text: str) -> str:
    """Translate generated labels, never executable code or actual stdout."""
    if LANGUAGE != "en":
        return text
    labels = {
        "#### 실제 실행 코드": "#### Executed source code",
        "#### 실행 명령": "#### Run command",
        "#### 실제 실행 결과": "#### Actual execution output",
        "#### 자동 확인 기록": "#### Automated verification record",
        "#### 실제 모델 실험 계약": "#### Real-model experiment contract",
        "#### 검증된 로컬 GPU 결과": "#### Verified local GPU results",
        "| 자동 확인 항목 | 값 |": "| Automated check | Value |",
        "| 검증 항목 | 값 |": "| Verified item | Value |",
        "| 항목 | 값 |": "| Item | Value |",
        "| 환경 |": "| Environment |",
        "| 학습 step |": "| Training steps |",
        "| 계산시간 |": "| Compute time |",
        "| process 시작 포함 |": "| Including process startup |",
        "| 코드 원본 |": "| Source code |",
        "| sequence 상한 |": "| Sequence limit |",
        "| peak VRAM 상한 |": "| Peak VRAM limit |",
        "| 실행 timeout |": "| Execution timeout |",
        "| artifact 크기 |": "| Artifact size |",
        "| 실행시간 |": "| Execution time |",
        "로컬 GPU 결과가 삽입되지 않음. 위 명령으로 고정된 실험을 재현할 수 있다.":
            "Local GPU results are not included. The command above reproduces the fixed experiment.",
    }
    parts = re.split(r"(```[^\n]*\n.*?```)", text, flags=re.DOTALL)
    for index in range(0, len(parts), 2):
        for original, translation in labels.items():
            parts[index] = parts[index].replace(original, translation)
        parts[index] = re.sub(r"(?<=`)초(?=\s*\|)", " seconds", parts[index])
        parts[index] = re.sub(r"(?<=\d)초(?=`\s*\|)", " seconds", parts[index])
    return "".join(parts)


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
    return text.replace(marker, localize_execution_prose(generated).rstrip())


def expand_stage_example(text: str, lesson_id: str) -> str:
    stage = lesson_id.split("-", 1)[0]
    example_spec = load_stage_example_registry(stage).get(lesson_id)
    if example_spec is None:
        return text
    example_id = str(example_spec["example_id"])
    marker = f"<!-- {stage}_EXAMPLE: {example_id} -->"
    if text.count(marker) != 1:
        raise SiteError(f"{stage} example marker 수가 1이 아니다: {lesson_id}")
    source_path = Path(str(example_spec["source_path"]))
    result_path = BUILD_ROOT / stage.lower() / "results" / f"{example_id}.json"
    if not result_path.exists():
        raise SiteError(
            f"{stage} 실행 결과가 없다: {result_path.relative_to(ROOT)}; "
            f"scripts/run_{stage.lower()}_examples.py를 먼저 실행하라"
        )
    source = read_text(source_path).rstrip()
    source_hash = hashlib.sha256(source_path.read_bytes()).hexdigest()
    result = json.loads(read_text(result_path))
    if result.get("source_sha256") != source_hash:
        raise SiteError(f"{stage} code와 실행 결과의 source hash가 다르다: {example_id}")
    required = {
        "stdout", "output", "command", "python_version", "torch_version",
        "numpy_version", "device", "process_seconds",
    }
    missing = sorted(required - result.keys())
    if missing:
        raise SiteError(f"{stage} 실행 결과 field 누락: {example_id} -> {', '.join(missing)}")
    generated = f"""<!-- {stage}_SOURCE_SHA256: {example_id} {source_hash} -->

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

| 자동 확인 항목 | 값 |
|---|---|
| 환경 | Python `{result['python_version']}`, PyTorch `{result['torch_version']}`, NumPy `{result['numpy_version']}` |
| device | `{result['device']}` |
| process 시작 포함 | `{result['process_seconds']:.6f}`초 |
"""
    return text.replace(marker, localize_execution_prose(generated).rstrip())


def expand_i06_example(text: str, lesson_id: str) -> str:
    return expand_stage_example(text, lesson_id)


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
            text = text.replace(marker, localize_execution_prose(generated).rstrip())
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
        text = text.replace(marker, localize_execution_prose(generated).rstrip())
    return text


def load_page_metadata(lessons: list[dict[str, object]], *, require_complete: bool = False) -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    expected = {str(lesson["relative_path"]) for lesson in lessons} | set(PUBLIC_DOCUMENTS)
    for path in sorted((ROOT / "site" / "page-metadata").glob("*.json")):
        for relative, descriptions in json.loads(read_text(path)).items():
            if relative in result or relative not in expected:
                raise SiteError(f"duplicate or unknown page metadata: {relative}")
            if set(descriptions) != {"ko", "en"} or any(not isinstance(value, str) or not value.strip() for value in descriptions.values()):
                raise SiteError(f"invalid bilingual page description: {relative}")
            result[relative] = descriptions
    if require_complete and set(result) != expected:
        raise SiteError(f"page descriptions incomplete: {len(result)}/{len(expected)}; missing={sorted(expected - set(result))}")
    return result


def markdown_renderer() -> markdown.Markdown:
    extensions, configs = [], {}
    for entry in yaml.safe_load(read_text(BASE_CONFIG))["markdown_extensions"]:
        if isinstance(entry, str):
            extensions.append(entry)
        else:
            for name, config in entry.items():
                extensions.append(name)
                configs[name] = config
    return markdown.Markdown(extensions=extensions, extension_configs=configs)


def prepare_reader_markdown(text: str, relative: str, lessons: list[dict[str, object]], descriptions: dict[str, dict[str, str]]) -> str:
    """Change public labels without altering reviewed manuscripts or old anchors."""
    front = FRONTMATTER_RE.match(text)
    metadata = (yaml.safe_load(front.group(1)) or {}) if front else {}
    body = text[front.end():] if front else text
    renderer = markdown_renderer()
    renderer.convert(body)
    def flatten(tokens: list[dict]) -> list[str]:
        return [anchor for token in tokens for anchor in [token["id"], *flatten(token["children"])]]
    anchors = iter(flatten(renderer.toc_tokens))
    by_id = {str(lesson["id"]): lesson for lesson in lessons}
    current = next((lesson for lesson in lessons if lesson["relative_path"] == relative), None)
    stages = EN_STAGE_TITLES if LANGUAGE == "en" else STAGE_TITLES
    labels = {key: value.split(" ", 1)[1] for key, value in stages.items()}
    labels["A09"] = "Optional advanced topics" if LANGUAGE == "en" else "선택 심화"
    lesson_token = r"(?:A09-[A-Z]{3}|[MNI]\d{2})-\d{2}"
    range_pattern = rf"({lesson_token})\s*[~–—-]\s*({lesson_token}|\d{{2}})"
    id_pattern = re.compile(rf"(?<![A-Za-z0-9_/-])(?:{range_pattern}|A09-[A-Z]{{3}}(?:-\d{{2}})?|[MNI]\d{{2}}(?:-\d{{2}})?|A09)(?![A-Za-z0-9_/-])")
    def replace_ids(value: str, *, links: bool = True) -> str:
        def label(key: str) -> str:
            if key not in by_id:
                return labels.get(key, key)
            lesson = by_id[key]
            title = str(lesson["title"])
            if not links:
                return title
            origin = DOCS_DIR / PUBLIC_DOCUMENTS.get(relative, relative)
            href = Path(os.path.relpath(DOCS_DIR / str(lesson["relative_path"]), origin.parent)).as_posix()
            return f"[{title}]({href})"
        def replace(match: re.Match[str]) -> str:
            key = match.group(0)
            interval = re.fullmatch(range_pattern, key)
            if interval:
                first, last = interval.groups()
                if len(last) == 2:
                    last = first.rsplit("-", 1)[0] + "-" + last
                if first not in by_id or last not in by_id:
                    return key
                return f"{label(first)} through {label(last)}" if LANGUAGE == "en" else f"{label(first)}부터 {label(last)}까지"
            return label(key)
        return id_pattern.sub(replace, value)
    protected = re.compile(r"<!--.*?-->|!?\[[^\]]*\]\([^)]*\)|`+[^`\n]*`+|\$\$.*?\$\$|\$[^$\n]+\$|\\\[.*?\\\]|\\\(.*?\\\)", re.DOTALL)
    def inline(value: str, *, links: bool = True) -> str:
        output, start = [], 0
        for match in protected.finditer(value):
            output.append(replace_ids(value[start:match.start()], links=links))
            token = match.group(0)
            if token.startswith("["):
                label, href = re.match(r"\[([^\]]*)\]\(([^)]*)\)", token).groups()
                for key in sorted([*by_id, *labels], key=len, reverse=True):
                    if label == key:
                        label = replace_ids(key, links=False)
                        break
                    if label.startswith(key + " "):
                        label = label[len(key):].lstrip(" .:–—-")
                        break
                token = f"[{replace_ids(label, links=False)}]({href})"
            elif token.startswith("`") and id_pattern.fullmatch(token.strip("`")):
                token = replace_ids(token.strip("`"), links=links)
            output.append(token)
            start = match.end()
        output.append(replace_ids(value[start:], links=links))
        return "".join(output)
    lines, fence, math_block, drop_id_column = [], None, None, False
    for line in body.splitlines():
        fence_match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence_match:
            if fence is None:
                fence = (fence_match.group(1), fence_match.group(2).strip())
            elif fence_match.group(1)[0] == fence[0][0] and len(fence_match.group(1)) >= len(fence[0]) and not fence_match.group(2).strip():
                fence = None
            lines.append(line)
            continue
        if fence:
            if relative == "01-CURRICULUM.md" and fence[1] == "text":
                line = re.sub(r"(?:A09-[A-Z]{3}|[MNI]\d{2}|A09)\s+(?=[^\s→↓─┐├┘·-])", lambda match: " " * len(match.group(0)), line)
                line = replace_ids(line, links=False)
            lines.append(line)
            continue
        if line.strip() in {r"\[", "$$"} and math_block is None:
            math_block = r"\]" if line.strip() == r"\[" else "$$"
        elif math_block and line.strip() == math_block:
            math_block = None
            lines.append(line)
            continue
        if math_block:
            lines.append(line)
            continue
        heading = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading:
            anchor = next(anchors)
            title = str(current["title"]) if current and heading.group(1) == "#" else heading.group(2)
            if not current or heading.group(1) != "#":
                title = re.sub(r"(?:A09-[A-Z]{3}|[MNI]\d{2}|A09)\.\s+", "", title)
                title = inline(title, links=False)
            if not re.search(r"\{\s*#", title):
                title += " { #" + anchor + " }"
            lines.append(heading.group(1) + " " + title)
            continue
        if relative == "01-CURRICULUM.md" and line.startswith("|"):
            cells = split_markdown_table_row(line)
            if cells and cells[0].strip() == "ID":
                drop_id_column = True
            if drop_id_column:
                lesson = by_id.get(cells[0].strip()) if cells else None
                cells = cells[1:]
                if lesson and cells and "](" not in cells[0]:
                    cells[0] = f"[{cells[0].strip()}]({lesson['relative_path']})"
                line = "| " + " | ".join(cell.strip() for cell in cells) + " |"
        else:
            drop_id_column = False
        if relative == "01-CURRICULUM.md" and re.match(r"^- (?:단원 ID는|Lesson IDs\b|Lesson identifiers\b)", line):
            continue
        lines.append(inline(line))
    if relative in descriptions:
        metadata["description"] = descriptions[relative][LANGUAGE]
    if current:
        index = lessons.index(current)
        metadata["learning_lesson"] = True
        for key, offset in (("learning_previous", -1), ("learning_next", 1)):
            neighbor = lessons[index + offset] if 0 <= index + offset < len(lessons) else None
            metadata[key] = {"title": neighbor["title"], "url": page_url(str(neighbor["relative_path"]))} if neighbor else None
    return "---\n" + yaml.safe_dump(metadata, allow_unicode=True, sort_keys=False) + "---\n\n" + "\n".join(lines).rstrip() + "\n"


def build_nav(lessons: list[dict[str, object]]) -> list[dict[str, object]]:
    titles = EN_STAGE_TITLES if LANGUAGE == "en" else STAGE_TITLES
    def nav_path(source: str) -> str:
        target = PUBLIC_DOCUMENTS[source]
        if LANGUAGE == "en" and ALLOW_PARTIAL and not (CONTENT_ROOT / source).exists():
            return PUBLIC_PATH + page_url(target)
        return target
    nav: list[dict[str, object]] = [
        {"Home" if LANGUAGE == "en" else "홈": "index.md"},
        {"Learning path" if LANGUAGE == "en" else "전체 학습경로": nav_path("01-CURRICULUM.md")},
    ]
    parts = (
        ("Part 1: Mathematical foundations", "제1부 · 기초 수학", list(STAGE_COUNTS)),
        ("Part 2: Neural networks and Transformers", "제2부 · 신경망과 Transformer", ["N05"]),
        ("Part 3: Model interpretability", "제3부 · 모델 해석", ["I06", "I07", "I08"]),
        ("Part 4: Optional advanced topics", "제4부 · 선택 심화", [stage for stage in POST_N05_STAGE_SPECS if stage.startswith("A09-")]),
    )
    for english, korean, stages in parts:
        modules = []
        for stage in stages:
            items = [{str(lesson["title"]): str(lesson["relative_path"])} for lesson in lessons if lesson["stage"] == stage]
            if items:
                modules.append({titles[stage].split(" ", 1)[1]: items})
        if modules:
            nav.append({english if LANGUAGE == "en" else korean: modules})
    nav.append({"Reference materials" if LANGUAGE == "en" else "참고자료": [
        {"Glossary" if LANGUAGE == "en" else "용어집": nav_path("04-GLOSSARY.md")},
        {"CPU execution environment" if LANGUAGE == "en" else "CPU 실행 환경": nav_path("N05-ENVIRONMENT.md")},
        {"Architecture and source baseline" if LANGUAGE == "en" else "아키텍처와 자료 기준": nav_path("05-N05-ARCHITECTURE-BASELINE.md")},
        {"GPU and Pythia environment" if LANGUAGE == "en" else "GPU·Pythia 실행 환경": nav_path("GPU-ENVIRONMENT.md")},
    ]})
    return nav


def rewrite_partial_links(text: str, relative_source: str) -> str:
    """Keep missing translations explicit links to the local Korean edition."""
    if LANGUAGE != "en":
        return text
    def replace(match: re.Match[str]) -> str:
        label_text, href = match.groups()
        label = "[" + label_text + "]"
        parsed = urlsplit(href)
        if parsed.scheme or parsed.netloc or not parsed.path or not parsed.path.endswith(".md"):
            return match.group(0)
        shared = (ROOT / relative_source).parent / unquote(parsed.path)
        shared = shared.resolve()
        if not shared.is_relative_to(ROOT) or not shared.exists():
            return match.group(0)  # The source audit reports the actual error.
        source = shared.relative_to(ROOT).as_posix()
        target = PUBLIC_DOCUMENTS.get(source, source)
        if (CONTENT_ROOT / source).exists():
            rewritten = Path(os.path.relpath(DOCS_DIR / target, (DOCS_DIR / PUBLIC_DOCUMENTS.get(relative_source, relative_source)).parent)).as_posix()
        elif ALLOW_PARTIAL:
            rewritten = PUBLIC_PATH + page_url(target)
            label = label[:-1] + " (Korean; not yet translated)]"
        else:
            raise SiteError(f"missing English link target: {relative_source} -> {source}")
        if parsed.fragment:
            rewritten += "#" + parsed.fragment
        return f"{label}({rewritten})"
    return re.sub(r"(?<!!)\[([^\]]*)\]\(([^)]+)\)", replace, text)


def assert_safe_build_root() -> None:
    root = ROOT.resolve()
    build = BUILD_ROOT.resolve()
    if build.parent != root or build.name != ".build":
        raise SiteError(f"안전하지 않은 build path: {build}")


def prepare() -> None:
    lessons = discover_all_lessons()
    descriptions = load_page_metadata(lessons)
    initial_snapshot = source_snapshot(lessons)
    assert_safe_build_root()
    if LANGUAGE == "en":
        for source in PUBLIC_DOCUMENTS:
            if not (CONTENT_ROOT / source).is_file() and not ALLOW_PARTIAL:
                raise SiteError(f"missing English public document: {source}")
    if not DOCS_DIR.resolve().is_relative_to(BUILD_ROOT.resolve()) or not SITE_DIR.resolve().is_relative_to(BUILD_ROOT.resolve()):
        raise SiteError("unsafe locale build path")
    if DOCS_DIR.exists():
        shutil.rmtree(DOCS_DIR)
    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)
    if CONFIG_PATH.exists():
        CONFIG_PATH.unlink()
    DOCS_DIR.mkdir(parents=True)

    write_text(DOCS_DIR / "index.md", rewrite_partial_links(prepare_reader_markdown(prepare_homepage(), "README.md", lessons, descriptions), "README.md"))
    for source, target in PUBLIC_DOCUMENTS.items():
        if source == "README.md" or not (CONTENT_ROOT / source).exists():
            continue
        text = read_text(CONTENT_ROOT / source)
        write_text(DOCS_DIR / target, rewrite_partial_links(prepare_reader_markdown(text, source, lessons, descriptions), source))

    for lesson in lessons:
        source_path = lesson["path"]
        if not isinstance(source_path, Path):
            raise SiteError("lesson path type 오류")
        text = strip_editor_checklist(read_text(source_path), str(lesson["id"]))
        text = enable_markdown_in_details(text, str(lesson["id"]))
        text = add_search_alias(text, str(lesson["id"]))
        text = expand_n05_example(text, str(lesson["id"]))
        text = expand_stage_example(text, str(lesson["id"]))
        text = expand_gpu_experiments(text, str(lesson["id"]))
        text = prepare_reader_markdown(text, str(lesson["relative_path"]), lessons, descriptions)
        text = rewrite_partial_links(text, str(lesson["relative_path"]))
        destination = DOCS_DIR / str(lesson["relative_path"])
        write_text(destination, text)

    assets_source = ROOT / "site" / "assets"
    shutil.copytree(assets_source, DOCS_DIR / "assets")

    figure_assets_source = ROOT / "figures" / "assets"
    if figure_assets_source.exists():
        shutil.copytree(figure_assets_source, DOCS_DIR / "figures" / "assets")

    config = localized_config()
    config["docs_dir"] = "docs"
    config["site_dir"] = "site"
    config["nav"] = build_nav(lessons)
    config["extra"]["start_page"] = page_url(str(lessons[0]["relative_path"])) if lessons else ""
    if source_snapshot(lessons) != initial_snapshot:
        raise SiteError("locale sources changed during prepare; run prepare again")
    write_text(CONFIG_PATH, yaml.safe_dump(config, allow_unicode=True, sort_keys=False))
    write_text(CONFIG_PATH.parent / "source-snapshot.json", json.dumps(initial_snapshot, ensure_ascii=False, indent=2) + "\n")

    print(f"prepared lessons={len(lessons)} docs_dir={DOCS_DIR}")


class LinkCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.urls: list[str] = []
        self.details_count = 0
        self.ids: set[str] = set()
        self.metadata: dict[str, str] = {}
        self.relations: dict[str, str] = {}
        self.reader_parts: list[str] = []
        self.duplicate_ids: set[str] = set()
        self.elements: list[tuple[str, bool]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            if values["id"] in self.ids:
                self.duplicate_ids.add(values["id"])
            self.ids.add(values["id"])
        if tag == "a" and values.get("name"):
            self.ids.add(values["name"])
        if tag == "meta" and values.get("content"):
            self.metadata[str(values.get("name") or values.get("property"))] = values["content"]
        if tag == "link" and values.get("rel") in {"prev", "next"}:
            self.relations[values["rel"]] = str(values.get("href", ""))
        if tag not in {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}:
            excluded = (self.elements[-1][1] if self.elements else False) or tag in {"pre", "code", "script", "style"} or "arithmatex" in str(values.get("class", "")).split()
            self.elements.append((tag, excluded))
        if tag == "details":
            self.details_count += 1
        attribute = "href" if tag in {"a", "link"} else "src" if tag in {"img", "script"} else None
        if not attribute:
            return
        values = dict(attrs)
        value = values.get(attribute)
        if value:
            self.urls.append(value)

    def handle_endtag(self, tag: str) -> None:
        for index in range(len(self.elements) - 1, -1, -1):
            if self.elements[index][0] == tag:
                del self.elements[index:]
                break

    def handle_data(self, data: str) -> None:
        if not self.elements or not self.elements[-1][1]:
            self.reader_parts.append(data)


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
    if parsed.scheme or parsed.netloc:
        return None
    if not parsed.path:
        return page if parsed.fragment else None
    path = unquote(parsed.path)
    if LANGUAGE == "ko" and path.startswith("/ai-math-guide/en/"):
        return None  # Cross-language targets are checked after artifact assembly.
    if LANGUAGE == "en" and path.startswith("/ai-math-guide/en/"):
        target = SITE_DIR / path.removeprefix("/ai-math-guide/en/")
    elif LANGUAGE == "en" and path.startswith("/ai-math-guide/"):
        return None
    elif path.startswith("/ai-math-guide/"):
        target = SITE_DIR / path.removeprefix("/ai-math-guide/")
    elif path.startswith("/"):
        target = SITE_DIR / path.lstrip("/")
    else:
        target = page.parent / path
    target = target.resolve()
    if path.endswith("/") or target.is_dir():
        target = target / "index.html"
    return target


def generated_fragment_exists(target: Path, url: str, cache: dict[Path, set[str]]) -> bool:
    fragment = unquote(urlsplit(url).fragment)
    if not fragment or fragment == "__consent" or target.suffix != ".html":
        return True
    if target not in cache:
        collector = LinkCollector()
        collector.feed(read_text(target))
        cache[target] = collector.ids
    return fragment in cache[target]


def sitemap_issues(public_pages: list[str]) -> list[str]:
    path = SITE_DIR / "sitemap.xml"
    if not path.exists():
        return ["missing sitemap"]
    prefix = PUBLIC_ROOT + ("en/" if LANGUAGE == "en" else "")
    expected = {prefix + page_url(relative) for relative in public_pages}
    locations = [str(element.text) for element in ET.parse(path).findall("{*}url/{*}loc")]
    if len(locations) != len(expected) or set(locations) != expected:
        return [f"sitemap coverage mismatch: missing={sorted(expected - set(locations))}, extra={sorted(set(locations) - expected)}"]
    return []


def search_page_hits(documents: list[dict], term: str, relative: str) -> list[str]:
    expected = page_url(relative)
    return [
        str(document.get("location", ""))
        for document in documents
        if unquote(urlsplit(str(document.get("location", ""))).path) == expected
        and term.casefold()
        in f"{document.get('title', '')} {document.get('text', '')}".casefold()
    ]


def validate() -> None:
    foundation_lessons = discover_lessons()
    n05_lessons = discover_n05_lessons()
    post_n05_lessons = [
        lesson
        for stage in POST_N05_STAGE_SPECS
        for lesson in discover_post_n05_stage(stage)
    ]
    n05_registry = load_n05_example_registry()
    stage_registries = {
        stage: load_stage_example_registry(stage)
        for stage in POST_N05_STAGE_SPECS
    }
    _, gpu_experiments = load_gpu_registries()
    lessons = foundation_lessons + n05_lessons + post_n05_lessons
    descriptions = load_page_metadata(lessons, require_complete=not ALLOW_PARTIAL)
    issues: list[str] = []
    _, reading_table_count, reading_cell_count = lint_english_readings()

    if not CONFIG_PATH.exists() or not SITE_DIR.exists():
        raise SiteError("prepare와 MkDocs build를 먼저 실행해야 한다")
    assert_current_sources(lessons)

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
    if len(staged_foundations) != len(foundation_lessons):
        issues.append(f"staged foundation lesson count={len(staged_foundations)}, expected={len(foundation_lessons)}")
    if len(staged_n05) != len(n05_lessons):
        issues.append(f"staged N05 lesson count={len(staged_n05)}, expected={len(n05_lessons)}")
    if len(staged_post_n05) != len(post_n05_lessons):
        issues.append(
            f"staged post-N05 lesson count={len(staged_post_n05)}, expected={len(post_n05_lessons)}"
        )

    original_checklists = sum(
        len(re.findall(rf"^##\s+{re.escape(checklist_title())}\s*$", read_text(Path(str(lesson["path"]))), flags=re.MULTILINE))
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
    if "집필자 점검표" in staged_text or "Author checklist" in staged_text:
        issues.append("staging에 집필자 점검표가 남았다")
    if "<details>" in staged_text:
        issues.append("staging에 Markdown 처리가 꺼진 details가 남았다")

    for internal in INTERNAL_DOCS:
        if (DOCS_DIR / internal).exists():
            issues.append(f"internal doc staged: {internal}")

    config = yaml.safe_load(read_text(CONFIG_PATH))
    if config["extra"].get("scope") != PUBLIC_PATH:
        issues.append("analytics consent storage scope is not shared")
    nav_paths = flatten_nav_paths(config.get("nav", []))
    lesson_nav_paths = [path for path in nav_paths if re.match(r"part-1-foundations/M0[0-4]/M0[0-4]-", path)]
    if len(lesson_nav_paths) != len(foundation_lessons) or len(set(lesson_nav_paths)) != len(foundation_lessons):
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
        path
        for path in nav_paths
        if any(
            path.startswith(f"{spec['directory']}/{stage}-")
            for stage, spec in POST_N05_STAGE_SPECS.items()
        )
    ]
    if len(post_nav_paths) != len(post_n05_lessons) or len(set(post_nav_paths)) != len(post_n05_lessons):
        issues.append(
            f"post-N05 nav count/unique={len(post_nav_paths)}/{len(set(post_nav_paths))}, "
            f"expected={len(post_n05_lessons)}"
        )
    expected_lesson_paths = [str(lesson["relative_path"]) for lesson in lessons]
    if [path for path in nav_paths if path in set(expected_lesson_paths)] != expected_lesson_paths:
        issues.append("formal lesson navigation differs from the educational order")

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
        stage = str(lesson["stage"])
        stage_registry = stage_registries[stage]
        staged_source = read_text(DOCS_DIR / str(lesson["relative_path"]))
        example_spec = stage_registry.get(lesson_id)
        if example_spec is not None:
            example_id = str(example_spec["example_id"])
            source_path = Path(str(example_spec["source_path"]))
            source = read_text(source_path).rstrip()
            if f"```python\n{source}\n```" not in staged_source:
                issues.append(f"staged {stage} code differs from source: {lesson_id}")
            result_path = BUILD_ROOT / stage.lower() / "results" / f"{example_id}.json"
            if not result_path.exists():
                issues.append(f"{stage} generated result missing: {example_id}")
        for experiment_id, experiment in gpu_experiments.items():
            if experiment.get("lesson_id") != lesson_id:
                continue
            source_hash = hashlib.sha256(GPU_RUNNER_PATH.read_bytes()).hexdigest()
            if f"GPU_SOURCE_SHA256: {experiment_id} {source_hash}" not in staged_source:
                issues.append(f"GPU source hash marker missing from staging: {lesson_id}/{experiment_id}")
            placeholder = "Local GPU results are not included" if LANGUAGE == "en" else "로컬 GPU 결과가 삽입되지 않음"
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
        if not path.exists() and not (LANGUAGE == "en" and ALLOW_PARTIAL):
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
        if not ALLOW_PARTIAL and f"<code>{spoken_reading}</code>" not in combined_html:
            issues.append(f"spoken reading missing from HTML: {spoken_reading}")
    if "집필자 점검표" in combined_html or "Author checklist" in combined_html:
        issues.append("generated HTML에 집필자 점검표가 남았다")
    public_pages = [str(lesson["relative_path"]) for lesson in lessons] + list(PUBLIC_DOCUMENTS.values())
    if not ALLOW_PARTIAL:
        issues.extend(sitemap_issues(public_pages))
    if LANGUAGE == "en" and not ALLOW_PARTIAL:
        missing_alternates = {page_url(relative) for relative in public_pages} - set(config["extra"]["bilingual"]["en_pages"])
        if missing_alternates:
            issues.append(f"missing English language-switch coverage: {sorted(missing_alternates)}")
    for relative in public_pages:
        page = output_html_for(relative)
        if not page.exists():
            continue
        html = read_text(page)
        collector = LinkCollector()
        collector.feed(html)
        if collector.duplicate_ids:
            issues.append(f"duplicate HTML anchors: {relative}/{sorted(collector.duplicate_ids)}")
        if re.search(r"(?<![A-Za-z0-9_/-])(?:A09-[A-Z]{3}(?:-\d{2})?|[MNI]\d{2}(?:-\d{2})?|A09)(?![A-Za-z0-9_/-])", " ".join(collector.reader_parts)):
            issues.append(f"management ID exposed in reader-facing text: {relative}")
        original_relative = next((source for source, target in PUBLIC_DOCUMENTS.items() if target == relative), relative)
        if original_relative in descriptions:
            description = descriptions[original_relative][LANGUAGE]
            for key in ("description", "og:description", "twitter:description"):
                if collector.metadata.get(key) != description:
                    issues.append(f"wrong page description: {relative}/{key}")
        suffix = page_url(relative)
        expected_url = PUBLIC_ROOT + ("en/" if LANGUAGE == "en" else "") + suffix
        if not suffix and collector.metadata.get("og:title") != config["site_name"]:
            issues.append(f"homepage sharing title differs from the site name: {relative}")
        if collector.metadata.get("og:url") != expected_url:
            issues.append(f"wrong sharing URL: {relative}")
        expected_locale = "en_US" if LANGUAGE == "en" else "ko_KR"
        alternate_locale = "ko_KR" if LANGUAGE == "en" else "en_US"
        if (collector.metadata.get("og:locale"), collector.metadata.get("og:locale:alternate")) != (expected_locale, alternate_locale):
            issues.append(f"wrong sharing locales: {relative}")
        if not collector.metadata.get("og:title") or collector.metadata.get("og:title") != collector.metadata.get("twitter:title"):
            issues.append(f"missing or inconsistent sharing titles: {relative}")
        if "noindex" in collector.metadata.get("robots", "").lower():
            issues.append(f"public page blocked by noindex: {relative}")
        verification = config["extra"].get("google_site_verification")
        if verification and collector.metadata.get("google-site-verification") != verification:
            issues.append(f"missing Search Console verification tag: {relative}")
        if relative in expected_lesson_paths:
            index = expected_lesson_paths.index(relative)
            if collector.metadata.get("og:title") != lessons[index]["title"]:
                issues.append(f"sharing lesson title differs from display name: {relative}")
            for relation, offset in (("prev", -1), ("next", 1)):
                target = resolve_generated_url(page, collector.relations[relation]) if relation in collector.relations else None
                expected_target = output_html_for(expected_lesson_paths[index + offset]).resolve() if 0 <= index + offset < len(lessons) else None
                if target != expected_target:
                    issues.append(f"wrong learning {relation}: {relative}")
        if f'<html lang="{LANGUAGE}"' not in html or f'<link rel="canonical" href="{expected_url}">' not in html:
            issues.append(f"wrong HTML language/self canonical: {relative}")
        if suffix in config["extra"]["bilingual"]["en_pages"]:
            for language, prefix in (("ko", ""), ("en", "en/")):
                if f'hreflang="{language}" href="{PUBLIC_ROOT}{prefix}{suffix}"' not in html:
                    issues.append(f"missing page-specific hreflang: {relative}/{language}")
                if f'href="{PUBLIC_PATH}{prefix}{suffix}" target="_self" hreflang="{language}"' not in html:
                    issues.append(f"wrong same-page language switch: {relative}/{language}")
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
        stage = str(lesson["stage"])
        stage_registry = stage_registries[stage]
        page = output_html_for(str(lesson["relative_path"]))
        page_text = read_text(page) if page.exists() else ""
        example_spec = stage_registry.get(lesson_id)
        if example_spec is not None:
            example_id = str(example_spec["example_id"])
            source_path = Path(str(example_spec["source_path"]))
            source_hash = hashlib.sha256(source_path.read_bytes()).hexdigest()
            if f"{stage}_SOURCE_SHA256: {example_id} {source_hash}" not in page_text:
                issues.append(f"{stage} source hash marker missing from HTML: {lesson_id}")
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
    fragment_cache: dict[Path, set[str]] = {}
    for page in html_paths:
        collector = LinkCollector()
        collector.feed(read_text(page))
        html_details += collector.details_count
        for url in collector.urls:
            target = resolve_generated_url(page, url)
            if target is not None and not target.exists():
                broken_urls.append(f"{page.relative_to(SITE_DIR)} -> {url}")
            elif target is not None and not generated_fragment_exists(target, url, fragment_cache):
                broken_urls.append(f"{page.relative_to(SITE_DIR)} -> {url} (missing fragment)")
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
        search_pages = {unquote(urlsplit(str(document.get("location", ""))).path) for document in documents}
        if search_pages != {page_url(relative) for relative in public_pages}:
            issues.append("search index differs from the public page inventory")
        for document in documents:
            location = str(document.get("location", ""))
            target = resolve_generated_url(SITE_DIR / "index.html", location)
            if target is not None and target.exists() and not generated_fragment_exists(target, location, fragment_cache):
                issues.append(f"search result points to missing fragment: {location}")
            if re.search(r"(?:A09-[A-Z]{3}|[MNI]\d{2})(?:-\d{2})?", str(document.get("title", ""))):
                issues.append(f"management ID exposed in search title: {location}")
        search_terms = SEARCH_TERMS if LANGUAGE == "ko" else {
            "Jacobian": "M03-11", "singular value decomposition": "M02-13",
            "mutual information": "M04-14", "chain rule": "M01-06", "calibration": "M04-15",
        }
        available_pages = {str(lesson["id"]): str(lesson["relative_path"]) for lesson in lessons} | PUBLIC_DOCUMENTS
        for term, expected_id in search_terms.items():
            if ALLOW_PARTIAL and expected_id not in available_pages:
                continue
            hits = search_page_hits(documents, term, available_pages[expected_id])
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
        "checklist_exposure": combined_html.count(checklist_title()),
        "n05_generated_results": sum(
            (
                BUILD_ROOT
                / "n05"
                / "results"
                / f"{str(example_spec['example_id'])}.json"
            ).exists()
            for example_spec in n05_registry.values()
        ),
        "i06_generated_results": sum(
            (BUILD_ROOT / "i06" / "results" / f"{str(example_spec['example_id'])}.json").exists()
            for example_spec in stage_registries["I06"].values()
        ),
        "i07_generated_results": sum(
            (BUILD_ROOT / "i07" / "results" / f"{str(example_spec['example_id'])}.json").exists()
            for example_spec in stage_registries["I07"].values()
        ),
        "i08_generated_results": sum(
            (BUILD_ROOT / "i08" / "results" / f"{str(example_spec['example_id'])}.json").exists()
            for example_spec in stage_registries["I08"].values()
        ),
        "gpu_result_mode": include_gpu_results,
        "gpu_registered_experiments": len(gpu_experiments),
        "search_hits": {term: len(hits) for term, hits in search_hits.items()},
    }
    summary["language"] = LANGUAGE
    summary["partial_preview"] = ALLOW_PARTIAL
    if LANGUAGE == "en":
        prose_sources = [Path(lesson["path"]) for lesson in lessons]
        prose_sources.extend(CONTENT_ROOT / source for source in PUBLIC_DOCUMENTS if (CONTENT_ROOT / source).is_file())
        summary["korean_prose_diagnostics"] = [diagnostic for path in prose_sources for diagnostic in find_korean_prose(path, read_text(path))]
    write_text(CONFIG_PATH.parent / "validation.json", json.dumps(summary, ensure_ascii=False, indent=2) + "\n")

    if issues:
        raise SiteError("generated-site validation 실패:\n- " + "\n- ".join(issues))
    print(json.dumps(summary, ensure_ascii=False, indent=2))


def merge_sites(*, allow_partial: bool = False) -> None:
    """Assemble locally verified locale outputs without touching the existing preview."""
    gate = [sys.executable, str(ROOT / "scripts" / "concepts.py"), "check-translations"]
    if not allow_partial:
        gate.append("--require-verified")
    result = subprocess.run(gate, cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    if result.returncode:
        raise SiteError(result.stderr.strip() or result.stdout.strip())
    for language in ("ko", "en"):
        select_language(language, allow_partial=allow_partial and language == "en", isolated=True)
        validate()
    destination = BUILD_ROOT / "bilingual" / "site"
    if destination.resolve().parent != (BUILD_ROOT / "bilingual").resolve() or not destination.resolve().is_relative_to(BUILD_ROOT.resolve()):
        raise SiteError("unsafe bilingual output path")
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(BUILD_ROOT / "ko" / "site", destination)
    shutil.copytree(BUILD_ROOT / "en" / "site", destination / "en")
    broken: list[str] = []
    fragment_cache: dict[Path, set[str]] = {}
    for page in destination.rglob("*.html"):
        collector = LinkCollector()
        collector.feed(read_text(page))
        for href in collector.urls:
            parsed = urlsplit(href)
            if parsed.scheme or parsed.netloc:
                continue
            path = unquote(parsed.path)
            target = (destination / path.removeprefix(PUBLIC_PATH) if path.startswith(PUBLIC_PATH) else page.parent / path) if path else page
            target = target.resolve()
            if not target.is_relative_to(destination.resolve()):
                broken.append(f"{page.relative_to(destination)} -> {href} (outside artifact)")
                continue
            if path.endswith("/") or target.is_dir():
                target = target / "index.html"
            if not target.exists():
                broken.append(f"{page.relative_to(destination)} -> {href}")
            elif not generated_fragment_exists(target, href, fragment_cache):
                broken.append(f"{page.relative_to(destination)} -> {href} (missing fragment)")
    for prefix in ("", "en"):
        output = destination / prefix
        if not (output / "search" / "search_index.json").exists() or not (output / "sitemap.xml").exists():
            broken.append(f"missing locale search index/sitemap: {prefix or 'ko'}")
            continue
        search = json.loads(read_text(output / "search" / "search_index.json"))
        for item in search.get("docs", []):
            parsed = urlsplit(str(item["location"]))
            path = unquote(parsed.path)
            target = (output / path).resolve()
            if (
                parsed.scheme or parsed.netloc or path.startswith("/")
                or ".." in Path(path).parts
                or not target.is_relative_to(output.resolve())
                or (not prefix and target.is_relative_to((destination / "en").resolve()))
            ):
                broken.append(f"outside locale search target: {prefix or 'ko'}/{item['location']}")
                continue
            if path.endswith("/") or target.is_dir():
                target /= "index.html"
            if not target.exists():
                broken.append(f"missing locale search target: {prefix}/{path}")
            elif not generated_fragment_exists(target, str(item["location"]), fragment_cache):
                broken.append(f"missing locale search fragment: {prefix}/{item['location']}")
    summary = {"partial_preview": allow_partial, "output": destination.relative_to(ROOT).as_posix(),
               "broken_links_or_assets": len(broken), "translation_audit": json.loads(result.stdout)}
    write_text(destination.parent / "validation.json", json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    if broken:
        raise SiteError("bilingual artifact validation failed:\n- " + "\n- ".join(broken[:30]))
    print(json.dumps(summary, ensure_ascii=False, indent=2))


class BilingualPreviewHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path: str) -> str:
        if path.startswith(PUBLIC_PATH):
            path = "/" + path.removeprefix(PUBLIC_PATH)
        elif urlsplit(path).path == PUBLIC_PATH.rstrip("/"):
            path = "/"
        return super().translate_path(path)


def serve_bilingual(port: int) -> None:
    output = BUILD_ROOT / "bilingual" / "site"
    if not all((output / prefix / "index.html").is_file() for prefix in ("", "en")):
        raise SiteError("build and merge both locales before previewing")
    from functools import partial

    handler = partial(BilingualPreviewHandler, directory=str(output))
    with ThreadingHTTPServer(("127.0.0.1", port), handler) as server:
        print(f"Korean: http://127.0.0.1:{port}{PUBLIC_PATH}", flush=True)
        print(f"English: http://127.0.0.1:{port}{PUBLIC_PATH}en/", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("audit", "prepare", "validate", "merge", "serve"))
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--lang", choices=("ko", "en"), default="ko")
    parser.add_argument("--allow-partial", action="store_true", help="Local English preview only; final checks require every translation")
    parser.add_argument("--isolated", action="store_true", help="Keep the legacy Korean preview; write under .build/ko instead")
    args = parser.parse_args()
    try:
        if args.command == "serve":
            serve_bilingual(args.port)
            return 0
        if args.command == "merge":
            merge_sites(allow_partial=args.allow_partial)
            return 0
        else:
            select_language(args.lang, allow_partial=args.allow_partial, isolated=args.isolated)
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
