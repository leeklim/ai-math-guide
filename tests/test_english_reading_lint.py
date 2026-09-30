from __future__ import annotations

import unittest
from pathlib import Path

from scripts.site import lint_english_readings


CHECKLIST = (
    "## 집필자 점검표\n\n"
    "- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 "
    "기계적 직역을 포함하지 않는다.\n"
)


def lesson(rows: list[tuple[str, str]], header: str = "Common spoken reading") -> str:
    body = "\n".join(f"| {symbol} | {reading} | 뜻 |" for symbol, reading in rows)
    return (
        "## 기호와 용어\n\n"
        f"| 기호·용어 | {header} | 의미 |\n"
        "|---|---|---|\n"
        f"{body}\n\n"
        f"{CHECKLIST}"
    )


class EnglishReadingLintTests(unittest.TestCase):
    def lint(self, text: str) -> list[str]:
        issues, _, _ = lint_english_readings([(Path("part-9/M99/M99-01-test.md"), text)])
        return issues

    def test_required_spoken_readings_pass(self) -> None:
        rows = [
            ("$w_i$", "`w sub i`"),
            ("$x^2$", "`x squared`"),
            ("$\\arg\\max_x f(x)$", "`arg max over x of f of x`"),
            ("$\\exp(x)$", "`the exponential of x`"),
            ("$\\frac{\\partial f}{\\partial x}$", "`partial f over partial x`"),
            ("upper triangular matrix", "`upper triangular matrix`"),
        ]
        self.assertEqual(self.lint(lesson(rows)), [])

    def test_invalid_cells_fail(self) -> None:
        cases = {
            "Hangul transliteration": "`더블유 아래 아이`",
            "incorrect exp expansion": "`익스프레스 엑스`",
            "empty cell": "",
            "missing backticks": "w sub i",
            "below": "`x below i`",
            "upper": "`x upper two`",
        }
        for name, reading in cases.items():
            with self.subTest(name=name):
                self.assertTrue(self.lint(lesson([("$w_i$", reading)])))

    def test_old_header_fails(self) -> None:
        self.assertTrue(self.lint(lesson([("$w_i$", "`w sub i`")], header="읽는 법")))

    def test_unexplained_inconsistency_fails(self) -> None:
        sources = [
            (Path("part-9/M99/M99-01-a.md"), lesson([("$w_i$", "`w sub i`")])),
            (Path("part-9/M99/M99-02-b.md"), lesson([("$w_i$", "`w index i`")])),
        ]
        issues, _, _ = lint_english_readings(sources)
        self.assertTrue(any("inconsistent" in issue for issue in issues))


if __name__ == "__main__":
    unittest.main()
