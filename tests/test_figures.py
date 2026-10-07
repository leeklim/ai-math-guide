from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("mmi_figures", ROOT / "scripts" / "figures.py")
assert SPEC is not None and SPEC.loader is not None
FIGURES = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(FIGURES)


class FigureAuditTests(unittest.TestCase):
    def test_manifest_assets_and_lesson_references_match(self) -> None:
        summary = FIGURES.validate_manifest(reproduce=False)
        self.assertGreaterEqual(summary["figures"], 21)
        self.assertEqual(summary["lesson_references"], summary["figures"])
        self.assertGreaterEqual(summary["generated_plots"], 3)

    def collect_fixture(self, caption: str, *, duplicate: bool = False, asset_path: str = "../../figures/assets/M00/M00-03-function.svg") -> tuple[dict, list[str]]:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            ko = root / "part-1-foundations/M00/M00-03-functions.md"
            en = root / "translations/en/part-1-foundations/M00/M00-03-functions.md"
            ko.parent.mkdir(parents=True)
            en.parent.mkdir(parents=True)
            body = f'<figure class="lesson-figure" markdown="1">\n![A function maps each input to one output.]({asset_path})\n<figcaption>{caption}</figcaption>\n</figure>\n'
            en.write_text('---\nid: "M00-03"\n---\n' + body * (2 if duplicate else 1), encoding="utf-8")
            ko.write_text('---\nid: "M00-03"\n---\n' + body.replace(caption, "입력과 출력의 대응"), encoding="utf-8")
            with patch.object(FIGURES, "ROOT", root), patch.object(FIGURES, "LESSON_ROOTS", (root / "part-1-foundations",)):
                ko_references, ko_issues = FIGURES.collect_lesson_references()
                self.assertFalse(ko_issues)
                references, issues = FIGURES.collect_lesson_references("en")
                if not issues:
                    self.assertEqual(set(ko_references), set(references))
                return references, issues

    def test_english_uses_shared_asset_without_cross_language_duplicate(self) -> None:
        references, issues = self.collect_fixture("Each input has exactly one output.")
        self.assertFalse(issues)
        self.assertEqual(list(references), ["figures/assets/M00/M00-03-function.svg"])

    def test_english_caption_must_exist_and_not_contain_hangul(self) -> None:
        for caption in ("", "한국어 caption"):
            with self.subTest(caption=caption):
                _, issues = self.collect_fixture(caption)
                self.assertTrue(any("English figcaption" in issue for issue in issues))

    def test_duplicate_within_one_language_remains_invalid(self) -> None:
        _, issues = self.collect_fixture("One output for each input.", duplicate=True)
        self.assertTrue(any("여러 번" in issue for issue in issues))


if __name__ == "__main__":
    unittest.main()
