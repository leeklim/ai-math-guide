#!/usr/bin/env python3
"""Validate and reproduce the textbook's tracked SVG figures."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "figures" / "manifest.json"
FIGURE_BLOCK_RE = re.compile(
    r'<figure class="lesson-figure" markdown="1">(?P<body>.*?)</figure>',
    re.DOTALL,
)
IMAGE_RE = re.compile(r"!\[(?P<alt>[^\]]+)\]\((?P<path>[^)]+\.svg)\)")
CAPTION_RE = re.compile(r"<figcaption>(?P<caption>.*?)</figcaption>", re.DOTALL)
FRONTMATTER_ID_RE = re.compile(r'^id:\s*"(?P<id>[A-Z0-9-]+)"\s*$', re.MULTILINE)
HANGUL_RE = re.compile(r"[가-힣]")
BANNED_SVG_TAGS = {"script", "foreignObject", "image"}
LESSON_ROOTS = (
    ROOT / "part-1-foundations",
    ROOT / "part-2-neural-computation",
    ROOT / "part-3-interpretability",
    ROOT / "part-4-advanced",
)


class FigureError(RuntimeError):
    """Raised when a figure invariant fails."""


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_manifest() -> list[dict[str, object]]:
    if not MANIFEST_PATH.exists():
        raise FigureError("figures/manifest.json이 없다")
    data = json.loads(read_text(MANIFEST_PATH))
    if data.get("schema_version") != 1 or not isinstance(data.get("figures"), list):
        raise FigureError("figure manifest schema가 잘못됐다")
    return data["figures"]


def lesson_paths() -> list[Path]:
    paths: list[Path] = []
    for root in LESSON_ROOTS:
        paths.extend(root.rglob("*.md"))
    return sorted(paths)


def safe_repo_path(value: object, *, suffix: str | None = None) -> Path:
    relative = Path(str(value))
    path = (ROOT / relative).resolve()
    if not path.is_relative_to(ROOT) or ".." in relative.parts:
        raise FigureError(f"안전하지 않은 경로다: {value}")
    if suffix is not None and path.suffix != suffix:
        raise FigureError(f"확장자가 {suffix}가 아니다: {value}")
    return path


def validate_svg(path: Path) -> list[str]:
    issues: list[str] = []
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as error:
        return [f"SVG XML을 읽을 수 없다: {path.relative_to(ROOT)}: {error}"]
    if root.tag.rsplit("}", 1)[-1] != "svg":
        issues.append(f"root element가 svg가 아니다: {path.relative_to(ROOT)}")
    if not root.get("viewBox"):
        issues.append(f"viewBox가 없다: {path.relative_to(ROOT)}")
    for element in root.iter():
        tag = element.tag.rsplit("}", 1)[-1]
        if tag in BANNED_SVG_TAGS:
            issues.append(f"금지 SVG element {tag}: {path.relative_to(ROOT)}")
        for key, value in element.attrib.items():
            if key.rsplit("}", 1)[-1] == "href" and (
                value.startswith(("http:", "https:", "data:", "//"))
            ):
                issues.append(f"외부 SVG 참조가 있다: {path.relative_to(ROOT)}")
    return issues


def collect_lesson_references() -> tuple[dict[str, tuple[str, Path]], list[str]]:
    references: dict[str, tuple[str, Path]] = {}
    issues: list[str] = []
    for lesson_path in lesson_paths():
        text = read_text(lesson_path)
        lesson_match = FRONTMATTER_ID_RE.search(text)
        if lesson_match is None:
            continue
        lesson_id = lesson_match.group("id")
        for block in FIGURE_BLOCK_RE.finditer(text):
            body = block.group("body")
            image_matches = list(IMAGE_RE.finditer(body))
            caption_match = CAPTION_RE.search(body)
            if len(image_matches) != 1:
                issues.append(f"figure block의 SVG가 하나가 아니다: {lesson_path.relative_to(ROOT)}")
                continue
            image_match = image_matches[0]
            alt = image_match.group("alt").strip()
            raw_path = image_match.group("path").strip()
            if HANGUL_RE.search(alt):
                issues.append(f"대체 텍스트에 한글이 있다: {lesson_path.relative_to(ROOT)} -> {alt}")
            if len(alt.split()) < 5:
                issues.append(f"대체 텍스트가 지나치게 짧다: {lesson_path.relative_to(ROOT)} -> {alt}")
            if caption_match is None or not HANGUL_RE.search(caption_match.group("caption")):
                issues.append(f"한국어 figcaption이 없다: {lesson_path.relative_to(ROOT)}")
            resolved = (lesson_path.parent / raw_path).resolve()
            if not resolved.is_relative_to(ROOT / "figures" / "assets"):
                issues.append(f"figure 경로가 figures/assets 밖이다: {lesson_path.relative_to(ROOT)}")
                continue
            relative = resolved.relative_to(ROOT).as_posix()
            if relative in references:
                issues.append(f"같은 figure가 여러 번 참조됐다: {relative}")
            if not resolved.stem.startswith(lesson_id):
                issues.append(f"figure 파일명이 단원 ID로 시작하지 않는다: {relative}")
            references[relative] = (lesson_id, lesson_path)
    return references, issues


def validate_manifest(*, reproduce: bool) -> dict[str, int]:
    entries = load_manifest()
    references, issues = collect_lesson_references()
    manifest_paths: set[str] = set()
    figure_ids: set[str] = set()
    lesson_ids = {
        match.group("id")
        for path in lesson_paths()
        if (match := FRONTMATTER_ID_RE.search(read_text(path))) is not None
    }

    for entry in entries:
        if not isinstance(entry, dict):
            issues.append("manifest entry가 object가 아니다")
            continue
        figure_id = str(entry.get("id", ""))
        lesson_id = str(entry.get("lesson_id", ""))
        kind = str(entry.get("kind", ""))
        asset_value = str(entry.get("asset", ""))
        if figure_id in figure_ids or not figure_id.startswith(f"{lesson_id}-"):
            issues.append(f"figure ID가 중복됐거나 단원 ID와 맞지 않는다: {figure_id}")
        figure_ids.add(figure_id)
        if lesson_id not in lesson_ids:
            issues.append(f"존재하지 않는 단원을 가리킨다: {figure_id}/{lesson_id}")
        if kind not in {"concept-svg", "generated-plot"}:
            issues.append(f"알 수 없는 figure kind다: {figure_id}/{kind}")
        try:
            asset = safe_repo_path(asset_value, suffix=".svg")
        except FigureError as error:
            issues.append(str(error))
            continue
        if not asset.is_relative_to(ROOT / "figures" / "assets"):
            issues.append(f"asset이 figures/assets 밖이다: {asset_value}")
        if asset.stem != figure_id:
            issues.append(f"figure ID와 asset stem이 다르다: {figure_id}/{asset_value}")
        if asset_value in manifest_paths:
            issues.append(f"manifest asset이 중복됐다: {asset_value}")
        manifest_paths.add(asset_value)
        if not asset.exists():
            issues.append(f"figure asset이 없다: {asset_value}")
        else:
            issues.extend(validate_svg(asset))

        generator_value = entry.get("generator")
        if kind == "generated-plot":
            if not generator_value:
                issues.append(f"generated plot의 generator가 없다: {figure_id}")
                continue
            try:
                generator = safe_repo_path(generator_value, suffix=".py")
            except FigureError as error:
                issues.append(str(error))
                continue
            if not generator.is_relative_to(ROOT / "figures" / "generators") or not generator.exists():
                issues.append(f"generator가 없거나 잘못된 위치다: {generator_value}")
            elif reproduce and asset.exists():
                with tempfile.TemporaryDirectory(prefix="mmi-figure-") as temp_dir:
                    reproduced = Path(temp_dir) / asset.name
                    result = subprocess.run(
                        [sys.executable, str(generator), "--output", str(reproduced)],
                        cwd=ROOT,
                        capture_output=True,
                        text=True,
                        check=False,
                    )
                    if result.returncode != 0:
                        issues.append(
                            f"figure 재생성 실패: {figure_id}: {result.stderr.strip() or result.stdout.strip()}"
                        )
                    elif reproduced.read_bytes() != asset.read_bytes():
                        issues.append(f"재생성 결과가 저장된 SVG와 다르다: {figure_id}")
        elif generator_value is not None:
            issues.append(f"concept SVG에는 generator를 두지 않는다: {figure_id}")

    missing_from_manifest = set(references) - manifest_paths
    unused_manifest_assets = manifest_paths - set(references)
    if missing_from_manifest:
        issues.append("manifest에 없는 본문 그림: " + ", ".join(sorted(missing_from_manifest)))
    if unused_manifest_assets:
        issues.append("본문에서 참조하지 않는 manifest 그림: " + ", ".join(sorted(unused_manifest_assets)))

    tracked_assets = {
        path.relative_to(ROOT).as_posix()
        for path in (ROOT / "figures" / "assets").rglob("*.svg")
    }
    unregistered_assets = tracked_assets - manifest_paths
    if unregistered_assets:
        issues.append("등록되지 않은 SVG: " + ", ".join(sorted(unregistered_assets)))

    if issues:
        raise FigureError("figure audit 실패:\n- " + "\n- ".join(issues))
    return {
        "figures": len(entries),
        "lesson_references": len(references),
        "generated_plots": sum(entry.get("kind") == "generated-plot" for entry in entries),
    }


def generate() -> None:
    for entry in load_manifest():
        if entry.get("kind") != "generated-plot":
            continue
        asset = safe_repo_path(entry["asset"], suffix=".svg")
        generator = safe_repo_path(entry["generator"], suffix=".py")
        asset.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            [sys.executable, str(generator), "--output", str(asset)],
            cwd=ROOT,
            check=True,
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("check", "generate"))
    parser.add_argument("--reproduce", action="store_true")
    args = parser.parse_args()
    try:
        if args.command == "generate":
            generate()
        summary = validate_manifest(reproduce=args.reproduce)
        print(json.dumps(summary, ensure_ascii=False))
    except (FigureError, subprocess.CalledProcessError) as error:
        print(str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
