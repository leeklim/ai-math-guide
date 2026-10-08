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
        cls.templates.filters["url"] = lambda value: value

    def render(self, template: str, config: dict | None = None) -> str:
        return self.templates.get_template(template).render(
            config=self.config if config is None else config,
            lang=SimpleNamespace(t=lambda key: key),
        )

    def test_public_site_has_no_google_analytics_or_consent_configuration(self) -> None:
        self.assertEqual(self.config["site_url"], "https://leeklim.github.io/ai-math-guide/")
        self.assertNotIn("analytics", self.config["extra"])
        self.assertNotIn("consent", self.config["extra"])
        self.assertEqual(self.overrides, ROOT / "site" / "overrides")
        self.assertFalse((self.overrides / "partials/integrations/analytics/google.html").exists())
        self.assertFalse((self.overrides / "partials/integrations/analytics.html").exists())

    def test_cloudflare_uses_fixed_public_address_and_public_beacon_token(self) -> None:
        settings = self.config["extra"]["cloudflare_web_analytics"]
        self.assertEqual(settings["public_url"], "https://leeklim.github.io/ai-math-guide/")
        self.assertRegex(settings["token"], r"^[0-9a-f]{32}$")
        script = self.render("partials/cloudflare-web-analytics.html")
        self.assertIn('id="__cloudflare_web_analytics"', script)
        self.assertIn('https://static.cloudflareinsights.com/beacon.min.js', script)
        self.assertIn('script.type = "module"', script)

    def test_missing_cloudflare_token_disables_loader(self) -> None:
        config = dict(self.config, extra={"cloudflare_web_analytics": {"token": ""}})
        self.assertEqual(self.render("partials/cloudflare-web-analytics.html", config).strip(), "")

    def test_preview_url_rewrite_does_not_change_cloudflare_guard(self) -> None:
        preview = dict(self.config, site_url="http://127.0.0.1:8005/ai-math-guide/")
        self.assertEqual(
            self.render("partials/cloudflare-web-analytics.html", preview),
            self.render("partials/cloudflare-web-analytics.html"),
        )

    def test_bilingual_footer_links_to_privacy_without_consent_controls(self) -> None:
        for language, label in (("ko", "개인정보·통계 안내"), ("en", "Privacy & Analytics")):
            with self.subTest(language=language):
                config = dict(self.config, theme=dict(self.config["theme"], language=language))
                html = self.templates.get_template("partials/footer.html").render(
                    config=config, features=[], lang=SimpleNamespace(t=lambda key: key),
                    page=SimpleNamespace(meta={}, previous_page=None, next_page=None),
                )
                self.assertIn('href="privacy/"', html)
                self.assertIn(label, html)
                self.assertNotIn("__consent", html)

    def test_footer_has_no_obsolete_consent_settings_link(self) -> None:
        footer = TagCollector()
        footer.feed(self.render("partials/copyright.html"))
        self.assertFalse(any(
            tag == "a" and attrs.get("href") == "#__consent"
            for tag, attrs in footer.tags
        ))

    def test_google_analytics_partial_renders_nothing_on_public_and_local_urls(self) -> None:
        for url in (self.config["site_url"], "http://127.0.0.1:8001/ai-math-guide/"):
            with self.subTest(url=url):
                config = dict(self.config, site_url=url)
                self.assertEqual(self.render("partials/integrations/analytics.html", config).strip(), "")


if __name__ == "__main__":
    unittest.main()
