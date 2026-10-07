from __future__ import annotations

import unittest

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
        for heading in ("기준 문서", "현재 상태", "로컬 HTML 검수"):
            self.assertNotIn(f"## {heading}", homepage)
        for operator_text in ("revision/concept-audit.csv", "scripts/build_site.ps1", "site/README.md"):
            self.assertNotIn(operator_text, homepage)

    def test_reader_navigation_is_preserved(self) -> None:
        homepage = prepare_homepage()
        self.assertIn("# 모델 해석을 위한 수학과 방법론", homepage)
        self.assertIn("## 네 부분", homepage)
        self.assertIn("## 읽기 시작", homepage)
        self.assertIn("[전체 학습경로](curriculum.md)", homepage)
        self.assertIn("part-1-foundations/M00/M00-01-numbers-variables.md", homepage)


if __name__ == "__main__":
    unittest.main()
