from __future__ import annotations

import struct
import unittest
from html.parser import HTMLParser
from pathlib import Path
from types import SimpleNamespace

from jinja2 import ChoiceLoader, DictLoader, Environment, FileSystemLoader


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_ROOT = "https://leeklim.github.io/ai-math-guide/"


class MetadataCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.metadata: dict[str, str] = {}
        self.links: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "meta":
            key = values.get("property") or values.get("name")
            if key:
                self.metadata[key] = values.get("content", "")
        elif tag == "link":
            self.links.append(values)


class SharingPreviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.templates = Environment(loader=ChoiceLoader([
            DictLoader({"base.html": "{% block site_meta %}{% endblock %}"}),
            FileSystemLoader(ROOT / "site/overrides"),
        ]))
        cls.templates.filters["url"] = lambda value: value

    def render(self, language: str, *, homepage: bool, preview: bool = False) -> MetadataCollector:
        suffix = "" if homepage else "part-2-neural-computation/N05/N05-15-causal-scaled-dot-product-attention/"
        locale_root = PUBLIC_ROOT + ("en/" if language == "en" else "")
        config = {
            "site_name": "AI Math Guide",
            "site_description": "A free bilingual mathematics textbook.",
            "site_url": "http://127.0.0.1:8001/ai-math-guide/" if preview else locale_root,
            "theme": {"language": language, "favicon": "assets/images/favicon.png"},
            "extra": {"bilingual": {"root": "/ai-math-guide/", "en_pages": [suffix]}},
        }
        page = SimpleNamespace(
            meta={"description": "Causal attention <with> conditions & examples."},
            title="Causal attention", is_homepage=homepage, canonical_url=locale_root + suffix,
            url=suffix, previous_page=None, next_page=None,
        )
        result = MetadataCollector()
        result.feed(self.templates.get_template("main.html").render(config=config, page=page, mkdocs_version="1.6"))
        return result

    def test_both_locales_use_large_production_image_on_home_and_lessons(self) -> None:
        for language in ("ko", "en"):
            for homepage in (True, False):
                with self.subTest(language=language, homepage=homepage):
                    rendered = self.render(language, homepage=homepage)
                    image = PUBLIC_ROOT + f"assets/images/social/ai-math-guide-{language}.png"
                    self.assertEqual(rendered.metadata["og:image"], image)
                    self.assertEqual(rendered.metadata["twitter:image"], image)
                    self.assertEqual(rendered.metadata["twitter:card"], "summary_large_image")
                    self.assertEqual(rendered.metadata["og:image:type"], "image/png")
                    self.assertEqual(rendered.metadata["og:image:width"], "1200")
                    self.assertEqual(rendered.metadata["og:image:height"], "630")
                    self.assertEqual(rendered.metadata["og:image:alt"], rendered.metadata["twitter:image:alt"])
                    self.assertIn("English" if language == "en" else "한영", rendered.metadata["og:image:alt"])

    def test_preview_does_not_rewrite_public_image_address(self) -> None:
        for language in ("ko", "en"):
            self.assertEqual(
                self.render(language, homepage=True).metadata["og:image"],
                self.render(language, homepage=True, preview=True).metadata["og:image"],
            )

    def test_page_titles_descriptions_canonical_and_language_links_are_preserved(self) -> None:
        for language in ("ko", "en"):
            for homepage in (True, False):
                with self.subTest(language=language, homepage=homepage):
                    rendered = self.render(language, homepage=homepage)
                    expected_title = "AI Math Guide" if homepage else "Causal attention"
                    self.assertEqual(rendered.metadata["og:title"], expected_title)
                    self.assertEqual(rendered.metadata["twitter:title"], expected_title)
                    self.assertEqual(rendered.metadata["og:description"], "Causal attention <with> conditions & examples.")
                    self.assertEqual(rendered.metadata["og:url"], next(link["href"] for link in rendered.links if link["rel"] == "canonical"))
                    self.assertEqual({link["hreflang"] for link in rendered.links if link["rel"] == "alternate"}, {"ko", "en"})

    def test_checked_in_images_have_declared_png_dimensions(self) -> None:
        for language in ("ko", "en"):
            with self.subTest(language=language):
                path = ROOT / f"site/assets/images/social/ai-math-guide-{language}.png"
                header = path.read_bytes()[:24]
                self.assertEqual(header[:8], b"\x89PNG\r\n\x1a\n")
                self.assertEqual(header[12:16], b"IHDR")
                self.assertEqual(struct.unpack(">II", header[16:24]), (1200, 630))


if __name__ == "__main__":
    unittest.main()
