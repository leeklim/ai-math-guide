from __future__ import annotations

import unittest
from html.parser import HTMLParser
from pathlib import Path
from types import SimpleNamespace

import material
import yaml
from jinja2 import Environment, FileSystemLoader

from scripts.site import BASE_CONFIG, CONFIG_PATH, ROOT, read_text


class TagCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tags: list[tuple[str, dict[str, str | None]]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.tags.append((tag, dict(attrs)))


class AnalyticsConfigTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.config = yaml.safe_load(read_text(BASE_CONFIG))
        cls.overrides = (CONFIG_PATH.parent / cls.config["theme"]["custom_dir"]).resolve()
        material_templates = Path(material.__file__).resolve().parent / "templates"
        cls.templates = Environment(
            loader=FileSystemLoader([cls.overrides, material_templates]),
        )

    def render(self, template: str, config: dict | None = None) -> str:
        return self.templates.get_template(template).render(
            config=self.config if config is None else config,
            lang=SimpleNamespace(t=lambda key: key),
        )

    def test_public_measurement_and_override_are_configured(self) -> None:
        self.assertEqual(self.config["site_url"], "https://leeklim.github.io/ai-math-guide/")
        self.assertEqual(
            self.config["extra"]["analytics"],
            {
                "provider": "google",
                "property": "G-VXDGRXQFT3",
                "public_url": "https://leeklim.github.io/ai-math-guide/",
            },
        )
        self.assertEqual(self.overrides, ROOT / "site" / "overrides")
        self.assertTrue((self.overrides / "partials/integrations/analytics/google.html").is_file())
        self.assertFalse((self.overrides / "partials/integrations/analytics.html").exists())

    def test_consent_is_opt_in_and_can_be_reopened_or_rejected(self) -> None:
        consent = TagCollector()
        consent.feed(self.render("partials/consent.html"))
        analytics_inputs = [
            attrs for tag, attrs in consent.tags
            if tag == "input" and attrs.get("name") == "analytics"
        ]
        self.assertEqual(len(analytics_inputs), 1)
        self.assertNotIn("checked", analytics_inputs[0])
        buttons = [attrs for tag, attrs in consent.tags if tag == "button"]
        self.assertEqual(len(buttons), 2)
        self.assertEqual(sum(attrs.get("type") == "reset" for attrs in buttons), 1)
        self.assertEqual(sum(attrs.get("type", "submit") == "submit" for attrs in buttons), 1)

        footer = TagCollector()
        footer.feed(self.render("partials/copyright.html"))
        self.assertTrue(any(
            tag == "a" and attrs.get("href") == "#__consent"
            for tag, attrs in footer.tags
        ))

    def test_rendered_analytics_uses_public_id_without_search_or_manual_page_views(self) -> None:
        rendered = self.render("partials/integrations/analytics.html")
        self.assertIn('const canonical = new URL("https://leeklim.github.io/ai-math-guide/")', rendered)
        self.assertIn('const measurementId = "G-VXDGRXQFT3"', rendered)
        self.assertIn("https://www.googletagmanager.com/gtag/js?id=", rendered)
        self.assertEqual(rendered.count('window.gtag("config",'), 1)
        self.assertNotIn("search_term", rendered)
        self.assertNotIn('"blur"', rendered)
        self.assertNotIn("page_view", rendered)
        self.assertNotIn("location$.subscribe", rendered)
        self.assertNotIn("{{", rendered)

    def test_preview_site_url_cannot_change_the_public_analytics_guard(self) -> None:
        preview_config = dict(self.config, site_url="http://127.0.0.1:8001/ai-math-guide/")
        rendered = self.render("partials/integrations/analytics.html", preview_config)
        self.assertIn('const canonical = new URL("https://leeklim.github.io/ai-math-guide/")', rendered)
        self.assertNotIn("127.0.0.1", rendered)

    def test_native_outer_partial_keeps_initialization_consent_gated(self) -> None:
        rendered = self.render("partials/integrations/analytics.html")
        self.assertIn('var consent=__md_get("__consent")', rendered)
        self.assertIn("consent&&consent.analytics&&__md_analytics()", rendered)
        self.assertNotIn('<script>"undefined"!=typeof __md_analytics&&__md_analytics()', rendered)


if __name__ == "__main__":
    unittest.main()
