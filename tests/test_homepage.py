from __future__ import annotations

import unittest
from unittest.mock import patch

from scripts import site
from scripts.site import prepare_homepage, remove_h2_sections


class HomepageTests(unittest.TestCase):
    def test_code_comments_do_not_end_a_removed_section(self) -> None:
        source = (
            "# Book\n\n## Operator notes\n\n```python\n"
            "# Comment\n## Another comment\nprint('internal')\n```\n"
            "Private instructions\n\n## Reading\n\nPublic instructions\n"
        )
        result = remove_h2_sections(source, {"Operator notes"}, required=True)
        self.assertEqual(result, "# Book\n\n## Reading\n\nPublic instructions\n")

    def test_operator_sections_are_not_published(self) -> None:
        homepage = prepare_homepage()
        for heading in ("기준 문서", "제작 원칙", "현재 상태", "로컬 HTML 검수"):
            self.assertNotIn(f"## {heading}", homepage)
        for operator_text in ("revision/concept-audit.csv", "scripts/build_site.ps1", "site/README.md"):
            self.assertNotIn(operator_text, homepage)

    def test_reader_navigation_is_preserved(self) -> None:
        homepage = prepare_homepage()
        self.assertIn("# 모델 해석을 위한 수학과 방법론", homepage)
        self.assertIn("## 네 부분 { #_2 }", homepage)
        self.assertIn("## 읽기 시작 { #_4 }", homepage)
        self.assertIn("[전체 학습경로](curriculum.md)", homepage)
        self.assertIn("part-1-foundations/M00/M00-01-numbers-variables.md", homepage)

    def test_both_homepages_show_paths_figures_and_feedback_before_operator_notes(self) -> None:
        for language, root in (("ko", site.ROOT), ("en", site.ROOT / "translations/en")):
            with self.subTest(language=language), patch.object(site, "LANGUAGE", language), patch.object(site, "CONTENT_ROOT", root):
                homepage = prepare_homepage()
                self.assertEqual(homepage.count('class="home-path"'), 3)
                self.assertEqual(homepage.count('<figure class="lesson-figure'), 3)
                self.assertLess(homepage.index('class="home-paths"'), homepage.index('<figure'))
                self.assertIn("M02-13-svd-three-stage.svg", homepage)
                self.assertIn("N05-15-causal-mask-matrices.svg", homepage)
                self.assertIn("I07-07-three-runs.svg", homepage)
                self.assertNotIn("](../../figures/assets/", homepage)
                self.assertIn("https://github.com/leeklim/ai-math-guide/issues", homepage)
                self.assertIn("https://leeklim.github.io/ai-math-guide/en/", homepage)
                self.assertNotIn("Production principles", homepage)
                self.assertNotIn("## 제작 원칙", homepage)


if __name__ == "__main__":
    unittest.main()
