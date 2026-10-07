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


if __name__ == "__main__":
    unittest.main()
