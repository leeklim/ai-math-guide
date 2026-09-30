#!/usr/bin/env python3
"""Prepare and validate the private-review MkDocs site."""

from __future__ import annotations

import argparse
import json
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
}

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


class SiteError(RuntimeError):
    """Raised when a source or generated-site invariant fails."""


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def parse_frontmatter(path: Path, text: str) -> dict[str, object]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise SiteError(f"frontmatter가 없다: {path.relative_to(ROOT)}")
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise SiteError(f"frontmatter 형식이 잘못됐다: {path.relative_to(ROOT)}")
    return data


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

    if len(lessons) != 70:
        issues.append(f"total lesson count={len(lessons)}, expected=70")
    if issues:
        raise SiteError("source audit 실패:\n- " + "\n- ".join(issues))
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


def build_nav(lessons: list[dict[str, object]]) -> list[dict[str, object]]:
    nav: list[dict[str, object]] = [
        {"홈": "index.md"},
        {"전체 학습경로": "curriculum.md"},
    ]
    for stage in STAGE_COUNTS:
        stage_items: list[dict[str, str]] = []
        for lesson in lessons:
            if lesson["stage"] != stage:
                continue
            label = f"{lesson['id']} {lesson['title']}"
            stage_items.append({label: str(lesson["relative_path"])})
        nav.append({STAGE_TITLES[stage]: stage_items})
    nav.append({"용어집": "glossary.md"})
    return nav


def assert_safe_build_root() -> None:
    root = ROOT.resolve()
    build = BUILD_ROOT.resolve()
    if build.parent != root or build.name != ".build":
        raise SiteError(f"안전하지 않은 build path: {build}")


def prepare() -> None:
    lessons = discover_lessons()
    assert_safe_build_root()
    if BUILD_ROOT.exists():
        shutil.rmtree(BUILD_ROOT)
    DOCS_DIR.mkdir(parents=True)

    write_text(DOCS_DIR / "index.md", prepare_homepage())
    write_text(DOCS_DIR / "curriculum.md", read_text(ROOT / "01-CURRICULUM.md"))
    write_text(DOCS_DIR / "glossary.md", read_text(ROOT / "04-GLOSSARY.md"))

    for lesson in lessons:
        source_path = lesson["path"]
        if not isinstance(source_path, Path):
            raise SiteError("lesson path type 오류")
        text = strip_editor_checklist(read_text(source_path), str(lesson["id"]))
        text = enable_markdown_in_details(text, str(lesson["id"]))
        text = add_search_alias(text, str(lesson["id"]))
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
    lessons = discover_lessons()
    issues: list[str] = []

    if not CONFIG_PATH.exists() or not SITE_DIR.exists():
        raise SiteError("prepare와 MkDocs build를 먼저 실행해야 한다")

    staged_lessons = sorted((DOCS_DIR / "part-1-foundations").glob("M0[0-4]/M0[0-4]-*.md"))
    if len(staged_lessons) != 70:
        issues.append(f"staged lesson count={len(staged_lessons)}, expected=70")

    original_checklists = sum(
        len(re.findall(r"^##\s+집필자 점검표\s*$", read_text(Path(str(lesson["path"]))), flags=re.MULTILINE))
        for lesson in lessons
    )
    if original_checklists != 70:
        issues.append(f"original checklist count={original_checklists}, expected=70")

    staged_text = "\n".join(read_text(path) for path in DOCS_DIR.rglob("*.md"))
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

    missing_pages: list[str] = []
    lesson_html_paths: list[Path] = []
    for lesson in lessons:
        page = output_html_for(str(lesson["relative_path"]))
        lesson_html_paths.append(page)
        if not page.exists():
            missing_pages.append(str(lesson["id"]))
    if missing_pages:
        issues.append("missing lesson HTML: " + ", ".join(missing_pages))

    for path in (SITE_DIR / "index.html", SITE_DIR / "curriculum" / "index.html", SITE_DIR / "glossary" / "index.html"):
        if not path.exists():
            issues.append(f"missing public page: {path.relative_to(SITE_DIR)}")

    html_paths = sorted(SITE_DIR.rglob("*.html"))
    combined_html = "\n".join(read_text(path) for path in html_paths)
    if "집필자 점검표" in combined_html:
        issues.append("generated HTML에 집필자 점검표가 남았다")
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
        "staged_lessons": len(staged_lessons),
        "generated_lesson_pages": sum(path.exists() for path in lesson_html_paths),
        "broken_links_or_assets": len(broken_urls),
        "source_details": source_details,
        "generated_details": html_details,
        "arithmatex_wrappers": arithmatex_count,
        "checklist_exposure": combined_html.count("집필자 점검표"),
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
            lessons = discover_lessons()
            print(f"source audit passed: lessons={len(lessons)}")
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
