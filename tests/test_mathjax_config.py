from __future__ import annotations

import unittest

from scripts.site import ROOT, read_text


class MathJaxConfigTests(unittest.TestCase):
    def test_mathtools_extension_is_loaded_and_enabled(self) -> None:
        config = read_text(ROOT / "site" / "assets" / "javascripts" / "mathjax.js")
        self.assertIn('"[tex]/mathtools"', config)
        self.assertRegex(config, r'packages:\s*\{[^}]*"mathtools"[^}]*\}')

    def test_navigation_labels_are_typeset(self) -> None:
        config = read_text(ROOT / "site" / "assets" / "javascripts" / "mathjax.js")
        self.assertIn('processHtmlClass: "arithmatex|md-ellipsis"', config)

    def test_initial_typesetting_uses_the_document_subscription_only(self) -> None:
        config = read_text(ROOT / "site" / "assets" / "javascripts" / "mathjax.js")
        self.assertRegex(config, r"startup:\s*\{\s*typeset:\s*false\s*\}")
        self.assertIn("document$.subscribe", config)
        self.assertEqual(config.count("MathJax.typesetPromise()"), 1)

    def test_inline_body_and_solution_math_can_scroll_inside_its_wrapper(self) -> None:
        styles = read_text(ROOT / "site" / "assets" / "stylesheets" / "extra.css")
        self.assertRegex(
            styles,
            r"\.md-typeset span\.arithmatex\s*\{[^}]*display:\s*inline-block;",
        )
        self.assertRegex(
            styles,
            r"\.md-typeset \.arithmatex\s*\{[^}]*max-width:\s*100%;[^}]*overflow-x:\s*auto;",
        )
        self.assertRegex(
            styles,
            r"\.md-typeset span\.arithmatex mjx-assistive-mml\s*\{[^}]*width:\s*1px\s*!important;",
        )


if __name__ == "__main__":
    unittest.main()
