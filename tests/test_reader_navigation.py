from __future__ import annotations

import unittest
import tempfile
import json
from pathlib import Path
from unittest.mock import patch

import markdown

from scripts import site


class ReaderNavigationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.language = site.LANGUAGE
        site.LANGUAGE = "en"
        self.lessons = [
            {"id": "M00-01", "stage": "M00", "title": "Numbers", "relative_path": "part-1-foundations/M00/M00-01-numbers.md"},
            {"id": "M03-11", "stage": "M03", "title": "Jacobian", "relative_path": "part-1-foundations/M03/M03-11-jacobian.md"},
        ]

    def tearDown(self) -> None:
        site.LANGUAGE = self.language

    def test_nav_uses_parts_and_names_without_duplicate_shortcut(self) -> None:
        nav = site.build_nav(self.lessons)
        paths = site.flatten_nav_paths(nav)
        self.assertEqual(paths.count(self.lessons[0]["relative_path"]), 1)
        self.assertIn("Part 1: Mathematical foundations", str(nav))
        self.assertIn("Reference materials", str(nav))
        self.assertNotIn("M03-11 Jacobian", str(nav))
        self.assertLess(paths.index(self.lessons[1]["relative_path"]), paths.index("glossary.md"))

    def test_display_labels_preserve_original_heading_anchor_and_code(self) -> None:
        text = (
            "# M03-11. Jacobian\n\nSee M00-01 and [M00-01 Numbers](../M00/M00-01-numbers.md).\n\n"
            "```python\nprint('M00-01')\n```\n\n$x_{M00-01}$\n"
        )
        result = site.prepare_reader_markdown(text, str(self.lessons[1]["relative_path"]), self.lessons, {})
        html = markdown.markdown(result, extensions=["meta", "attr_list", "toc", "fenced_code"])
        self.assertIn('<h1 id="m03-11-jacobian">Jacobian</h1>', html)
        self.assertIn("See [Numbers](../M00/M00-01-numbers.md)", result)
        self.assertIn("[Numbers](../M00/M00-01-numbers.md)", result)
        self.assertIn("print('M00-01')", result)
        self.assertIn("$x_{M00-01}$", result)

    def test_curriculum_removes_id_column_and_links_lesson_titles(self) -> None:
        text = "# Curriculum\n\n| ID | Lesson | Result |\n|---|---|---|\n| M00-01 | Numbers | Read numbers. |\n"
        result = site.prepare_reader_markdown(text, "01-CURRICULUM.md", self.lessons, {})
        self.assertIn("| Lesson | Result |", result)
        self.assertNotIn("| ID |", result)
        self.assertIn("[Numbers](part-1-foundations/M00/M00-01-numbers.md)", result)

    def test_learning_neighbors_do_not_link_into_reference_materials(self) -> None:
        result = site.prepare_reader_markdown("# M03-11. Jacobian\n", str(self.lessons[1]["relative_path"]), self.lessons, {})
        metadata = site.FRONTMATTER_RE.match(result)
        self.assertIsNotNone(metadata)
        import yaml
        values = yaml.safe_load(metadata.group(1))
        self.assertEqual(values["learning_previous"]["title"], "Numbers")
        self.assertIsNone(values["learning_next"])

    def test_lesson_ranges_preserve_both_endpoints_and_existing_link(self) -> None:
        for language in ("ko", "en"):
            site.LANGUAGE = language
            lessons = [
                {"id": "N05-01", "title": "Tensors", "relative_path": "N05/N05-01.md"},
                {"id": "N05-10", "title": "Autograd", "relative_path": "N05/N05-10.md"},
                {"id": "A09-GEO-01", "title": "Manifolds", "relative_path": "GEO/A09-GEO-01.md"},
                {"id": "A09-GEO-07", "title": "Pitfalls", "relative_path": "GEO/A09-GEO-07.md"},
            ]
            text = "# Review\n\n## N05-01~10 review\n\nN05-01–N05-10 and `N05-01–10`.\n\n[A09-GEO-01–07](GEO/A09-GEO-07.md)\n"
            result = site.prepare_reader_markdown(text, "review.md", lessons, {})
            connector = " through " if language == "en" else "부터 "
            suffix = "" if language == "en" else "까지"
            self.assertIn(f"Tensors{connector}Autograd{suffix} review", result)
            self.assertIn(f"[Tensors](N05/N05-01.md){connector}[Autograd](N05/N05-10.md){suffix}", result)
            self.assertIn(f"[Manifolds{connector}Pitfalls{suffix}](GEO/A09-GEO-07.md)", result)
            self.assertNotIn("~10", result)
            self.assertNotIn("–07]", result)

    def test_fragment_only_and_encoded_fragments_are_checked(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "index.html"
            target.write_text('<h1 id="m03-11-jacobian">Jacobian</h1><a name="old">Old</a>', encoding="utf-8")
            self.assertEqual(site.resolve_generated_url(target, "#m03-11-jacobian"), target)
            self.assertTrue(site.generated_fragment_exists(target, "#m03%2D11-jacobian", {}))
            self.assertTrue(site.generated_fragment_exists(target, "index.html#old", {}))
            self.assertFalse(site.generated_fragment_exists(target, "#missing", {}))
            self.assertTrue(site.generated_fragment_exists(target, "#__consent", {}))

    def test_metadata_changes_invalidate_source_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config, script = root / "site/mkdocs.base.yml", root / "scripts/site.py"
            site.write_text(config, "fixture")
            site.write_text(script, "fixture")
            metadata = root / "site/page-metadata/M00.json"
            site.write_text(metadata, '{}')
            with patch.object(site, "ROOT", root), patch.object(site, "CONTENT_ROOT", root), patch.object(site, "BASE_CONFIG", config), patch.object(site, "__file__", str(script)), patch.object(site, "load_gpu_registries", return_value=({}, {})):
                before = site.source_snapshot([])
                self.assertIn("site/page-metadata/M00.json", before["sources"])
                site.write_text(metadata, '{"changed": true}')
                self.assertNotEqual(before, site.source_snapshot([]))

    def test_reader_text_excludes_only_protected_code_math_and_script(self) -> None:
        collector = site.LinkCollector()
        collector.feed('<h1 id="old">Jacobian</h1><p>M03-11</p><pre><code>N05-15</code></pre><span class="arithmatex">M01-01</span><script>M00</script><link rel="next" href="next/"><h2 id="old">Repeat</h2>')
        reader_text = " ".join(collector.reader_parts)
        self.assertIn("M03-11", reader_text)
        self.assertNotIn("N05-15", reader_text)
        self.assertNotIn("M01-01", reader_text)
        self.assertNotIn("M00", reader_text)
        self.assertEqual(collector.duplicate_ids, {"old"})
        self.assertEqual(collector.relations, {"next": "next/"})

    def test_sitemap_checks_exact_locale_coverage_and_duplicates(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            sitemap = root / "sitemap.xml"
            url = site.PUBLIC_ROOT + "en/"
            with patch.object(site, "SITE_DIR", root):
                sitemap.write_text(f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{url}</loc></url></urlset>', encoding="utf-8")
                self.assertEqual(site.sitemap_issues(["index.md"]), [])
                sitemap.write_text(f'<urlset><url><loc>{url}</loc></url><url><loc>{url}</loc></url></urlset>', encoding="utf-8")
                self.assertTrue(site.sitemap_issues(["index.md"]))

    def test_description_loader_rejects_missing_pages(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch.object(site, "ROOT", root):
                self.assertEqual(site.load_page_metadata(self.lessons), {})
                with self.assertRaisesRegex(site.SiteError, "incomplete"):
                    site.load_page_metadata(self.lessons, require_complete=True)


if __name__ == "__main__":
    unittest.main()
