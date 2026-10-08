from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from mkdocs.commands.build import build
from mkdocs.config import load_config

from scripts import site


class BilingualSiteTests(unittest.TestCase):
    def setUp(self) -> None:
        self.original = {
            name: getattr(site, name)
            for name in ("LANGUAGE", "ALLOW_PARTIAL", "CONTENT_ROOT", "DOCS_DIR", "SITE_DIR", "CONFIG_PATH")
        }

    def tearDown(self) -> None:
        for name, value in self.original.items():
            setattr(site, name, value)

    def test_locale_output_is_separate_but_code_results_and_assets_are_shared(self) -> None:
        site.select_language("en", allow_partial=True)
        self.assertEqual(site.CONTENT_ROOT, site.ROOT / "translations" / "en")
        self.assertEqual(site.DOCS_DIR, site.BUILD_ROOT / "en" / "docs")
        self.assertEqual(site.SITE_DIR, site.BUILD_ROOT / "en" / "site")
        self.assertEqual(site.CONFIG_PATH, site.BUILD_ROOT / "en" / "mkdocs.yml")
        self.assertEqual(site.N05_REGISTRY_PATH, site.ROOT / "labs" / "N05" / "examples.json")
        self.assertEqual(site.GPU_RUNNER_PATH, site.ROOT / "labs" / "real_models" / "run_pythia.py")
        site.select_language("ko")
        self.assertEqual(site.DOCS_DIR, site.BUILD_ROOT / "docs")
        self.assertEqual(site.SITE_DIR, site.BUILD_ROOT / "site")
        self.assertEqual(site.CONFIG_PATH, site.BUILD_ROOT / "mkdocs.yml")
        site.select_language("ko", isolated=True)
        self.assertEqual(site.SITE_DIR, site.BUILD_ROOT / "ko" / "site")
        self.assertEqual(site.CONFIG_PATH, site.BUILD_ROOT / "ko" / "mkdocs.yml")
        with self.assertRaises(site.SiteError):
            site.select_language("ko", allow_partial=True)

    def test_english_config_preserves_settings_scope_without_analytics_or_consent(self) -> None:
        site.select_language("en", allow_partial=True)
        config = site.localized_config()
        self.assertEqual(config["theme"]["language"], "en")
        self.assertEqual(config["site_url"], site.PUBLIC_ROOT + "en/")
        self.assertEqual(config["extra"]["scope"], site.PUBLIC_PATH)
        self.assertNotIn("analytics", config["extra"])
        self.assertNotIn("consent", config["extra"])
        self.assertNotIn("#__consent", config.get("copyright", ""))
        self.assertTrue(config["extra"]["bilingual"]["partial_preview"])
        self.assertEqual((site.CONFIG_PATH.parent / config["theme"]["custom_dir"]).resolve(), site.ROOT / "site" / "overrides")

    def test_generated_prose_does_not_translate_actual_code_or_stdout(self) -> None:
        site.select_language("en")
        original = (
            "#### 실제 실행 코드\n\n```python\n# 실제 실행 코드\nprint('환경')\n```\n"
            "#### 실제 실행 결과\n\n```text\n실제 실행 결과: 환경\n```\n"
            "| 환경 | Python `3.12` |\n| 계산시간 | `0.01`초 |\n"
        )
        result = site.localize_execution_prose(original)
        self.assertIn("#### Executed source code", result)
        self.assertIn("#### Actual execution output", result)
        self.assertIn("```python\n# 실제 실행 코드\nprint('환경')\n```", result)
        self.assertIn("```text\n실제 실행 결과: 환경\n```", result)
        self.assertIn("| Environment |", result)
        self.assertIn("`0.01` seconds", result)

    def test_english_checklist_is_removed_without_weakening_korean_rules(self) -> None:
        site.select_language("en")
        result = site.strip_editor_checklist("# Lesson\n\n## Author checklist\n\n- [x] Check\n", "M00-01")
        self.assertEqual(result, "# Lesson\n")
        with self.assertRaises(site.SiteError):
            site.strip_editor_checklist("# Lesson\n", "M00-01")
        site.select_language("ko")
        with self.assertRaises(site.SiteError):
            site.strip_editor_checklist("# Lesson\n\n## Author checklist\n", "M00-01")

    def test_partial_source_audit_uses_only_real_translations_and_final_rejects_gaps(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            relative = "part-1-foundations/M00/M00-01-fixture.md"
            ko = self.fixture_lesson(english=False)
            en = self.fixture_lesson(english=True)
            site.write_text(root / relative, ko)
            site.write_text(root / "part-1-foundations/M00/M00-02-fixture.md", ko.replace("M00-01", "M00-02"))
            site.write_text(root / "translations/en" / relative, en)
            with patch.object(site, "ROOT", root):
                site.select_language("en", allow_partial=True)
                lessons = site.discover_english_stage("M00", "part-1-foundations/M00")
                self.assertEqual([lesson["id"] for lesson in lessons], ["M00-01"])
                self.assertFalse((site.CONTENT_ROOT / "part-1-foundations/M00/M00-02-fixture.md").exists())
                site.select_language("en")
                with self.assertRaisesRegex(site.SiteError, "missing English lesson"):
                    site.discover_english_stage("M00", "part-1-foundations/M00")

    @staticmethod
    def fixture_lesson(*, english: bool) -> str:
        first = "Symbol or term" if english else "기호·용어"
        checklist = "Author checklist" if english else "집필자 점검표"
        check = site.EN_SPOKEN_READING_CHECKLIST if english else site.SPOKEN_READING_CHECKLIST
        summary = "Show solution" if english else "해설 보기"
        status = "complete" if english else "완료"
        return (
            f'---\nid: M00-01\ntitle: Fixture\npart: 1\nstage: M00\nstatus: {status}\nprerequisites: []\n---\n'
            f"# M00-01. Fixture\n\n## Terms\n\n| {first} | Common spoken reading | Meaning | Shape and conditions |\n"
            "|---|---|---|---|\n| $x$ | `x` | A variable | Scalar |\n\n## Exercises\n\n"
            f"<details>\n<summary>{summary}</summary>\n\n$x=1$.\n\n</details>\n\n"
            f"## {checklist}\n\n- [x] {check}\n"
        )

    def test_english_notation_table_requires_english_headers(self) -> None:
        source = self.fixture_lesson(english=True).replace("Shape and conditions", "주의점")
        issues, _, _ = site.lint_english_readings([(Path("M00-01.md"), source)], language="en")
        self.assertTrue(any("English notation-table headers" in issue for issue in issues))

    def test_english_notation_table_preserves_source_width_and_context_header(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            relative = "part-1-foundations/M00/M00-01-fixture.md"
            ko_four = self.fixture_lesson(english=False)
            en_four = self.fixture_lesson(english=True).replace("Shape and conditions", "Cautions")
            def three_columns(value: str) -> str:
                return value.replace(" | Shape and conditions |", " |").replace(" | Cautions |", " |").replace("|---|---|---|---|", "|---|---|---|").replace(" | Scalar |", " |")
            site.write_text(root / relative, ko_four)
            path = root / "translations/en" / relative
            with patch.object(site, "ROOT", root):
                site.select_language("en")
                issues, _, _ = site.lint_english_readings([(path, en_four)], language="en")
                self.assertEqual(issues, [])
                en_three = three_columns(en_four).replace("| Meaning |", "| Meaning in this lesson |")
                issues, _, _ = site.lint_english_readings([(path, en_three)], language="en")
                self.assertTrue(any("column count differs" in issue for issue in issues))
                site.write_text(root / relative, three_columns(ko_four))
                issues, _, _ = site.lint_english_readings([(path, en_three)], language="en")
                self.assertEqual(issues, [])
                issues, _, _ = site.lint_english_readings([(path, en_four)], language="en")
                self.assertTrue(any("column count differs" in issue for issue in issues))
                relative_path = Path(os.path.relpath(path, Path.cwd()))
                relative_issues, _, _ = site.lint_english_readings([(relative_path, en_four)], language="en")
                self.assertTrue(any("column count differs" in issue for issue in relative_issues))
                issues, _, _ = site.lint_english_readings([(path, en_three.replace("| $x$ | `x` | A variable |", "| $x$ | `x` | A variable | Scalar |"))], language="en")
                self.assertTrue(any("row width differs" in issue for issue in issues))

    def test_korean_term_translation_preserves_math_and_spoken_reading(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            relative = "part-1-foundations/M00/M00-01-fixture.md"
            ko = self.fixture_lesson(english=False).replace("| $x$ | `x`", "| $x$와 수 | `x`")
            en = self.fixture_lesson(english=True).replace("| $x$ | `x`", "| $x$ and a number | `x`")
            site.write_text(root / relative, ko)
            site.write_text(root / "translations/en" / relative, en)
            with patch.object(site, "ROOT", root):
                site.select_language("en")
                self.assertEqual(len(site.discover_english_stage("M00", "part-1-foundations/M00")), 1)
                site.write_text(site.CONTENT_ROOT / relative, en.replace("$x$ and", "$y$ and"))
                with self.assertRaisesRegex(site.SiteError, "symbols/spoken readings differ"):
                    site.discover_english_stage("M00", "part-1-foundations/M00")
                site.write_text(site.CONTENT_ROOT / relative, en.replace("`x`", "`y`"))
                with self.assertRaisesRegex(site.SiteError, "symbols/spoken readings differ"):
                    site.discover_english_stage("M00", "part-1-foundations/M00")

    def test_residual_korean_prose_is_reported_but_code_stdout_are_preserved(self) -> None:
        text = (
            "# English lesson\n\n이 문장은 검토가 필요하다.\n\n"
            "```python\n# 한글 주석 보존\nprint('고양이')\n```\n"
            "```text\n고양이\n```\n\nA Korean token: `고양이`.\n\n"
            "## Author checklist\n\n- [x] 내부 메모\n"
        )
        diagnostics = site.find_korean_prose(Path("fixture.md"), text)
        self.assertEqual(len(diagnostics), 2)
        self.assertIn("검토가 필요", diagnostics[0])
        self.assertIn("Korean token", diagnostics[1])

    def test_optional_gpu_wrapper_localizes_only_labels_in_english(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            runner = root / "labs/real_models/run_pythia.py"
            site.write_text(runner, "# shared source fixture\n")
            source_hash = hashlib.sha256(runner.read_bytes()).hexdigest()
            model = {"repository": "fixture/model", "revision": "fixture-revision", "peak_vram_limit_bytes": 1024**3, "timeout_seconds": 2}
            experiment = {"lesson_id": "I07-07", "model_key": "fixture", "mode": "patch", "layer": 0, "token": "last", "sequence_length": 2}
            manifest = {
                "schema_version": 1, "experiment_id": "fixture_patch", "lesson_id": "I07-07", "status": "passed",
                "source": {"sha256": source_hash}, "model": {"repository": model["repository"], "requested_revision": model["revision"], "resolved_sha": "fixture-sha"},
                "inputs": {}, "hook": {}, "resources": {"peak_allocated_bytes": 128, "artifact_bytes": 0}, "artifacts": [], "assertions": {},
                "summary": {"output": "보존된 실제 출력", "value": 1.25}, "failure": None, "timestamps": {"seconds": 0.5},
            }
            site.write_text(root / ".build/gpu/results/fixture_patch/manifest.json", json.dumps(manifest))
            with patch.object(site, "ROOT", root), patch.object(site, "BUILD_ROOT", root / ".build"), patch.object(site, "GPU_RUNNER_PATH", runner), patch.object(site, "load_gpu_registries", return_value=({"fixture": model}, {"fixture_patch": experiment})), patch.dict(os.environ, {"AI_MATH_GPU_RESULTS": "1"}):
                site.select_language("en")
                expanded = site.expand_gpu_experiments("<!-- GPU_EXPERIMENT: fixture_patch -->", "I07-07")
                self.assertIn("#### Verified local GPU results", expanded)
                self.assertIn("| Artifact size |", expanded)
                self.assertIn("보존된 실제 출력", expanded)
                self.assertIn('"value": 1.25', expanded)
                self.assertIn(source_hash, expanded)
                self.assertNotIn("Local GPU results are not included", expanded)
                config = root / "site/mkdocs.base.yml"
                lesson = site.CONTENT_ROOT / "part-3-interpretability/I07/I07-07-fixture.md"
                artifact = root / ".build/gpu/results/fixture_patch/output.txt"
                for path in (config, lesson, artifact):
                    site.write_text(path, "fixture\n")
                manifest["artifacts"] = [{"path": artifact.relative_to(root).as_posix(), "sha256": hashlib.sha256(artifact.read_bytes()).hexdigest()}]
                manifest_path = artifact.parent / "manifest.json"
                site.write_text(manifest_path, json.dumps(manifest))
                lessons = [{"id": "I07-07", "stage": "I07", "path": lesson}]
                with patch.object(site, "BASE_CONFIG", config), patch.object(site, "__file__", str(runner)), patch.object(site, "load_stage_example_registry", return_value={}):
                    site.write_text(site.CONFIG_PATH.parent / "source-snapshot.json", json.dumps(site.source_snapshot(lessons)))
                    site.assert_current_sources(lessons)
                    site.write_text(artifact, "changed artifact\n")
                    with self.assertRaisesRegex(site.SiteError, "staging is stale"):
                        site.assert_current_sources(lessons)
                    site.write_text(artifact, "fixture\n")
                    manifest["summary"]["value"] = 2.5
                    site.write_text(manifest_path, json.dumps(manifest))
                    with self.assertRaisesRegex(site.SiteError, "staging is stale"):
                        site.assert_current_sources(lessons)

    def test_partial_links_are_marked_and_shared_images_are_not_rewritten(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            site.write_text(root / "part-1-foundations/M00/M00-01-a.md", "# A\n")
            site.write_text(root / "part-1-foundations/M00/M00-02-b.md", "# B\n")
            with patch.object(site, "ROOT", root):
                site.select_language("en", allow_partial=True)
                text = "[Next](M00-02-b.md)\n![A figure](../../figures/assets/M00/a.svg)\n"
                rewritten = site.rewrite_partial_links(text, "part-1-foundations/M00/M00-01-a.md")
                self.assertIn("[Next (Korean; not yet translated)](/ai-math-guide/part-1-foundations/M00/M00-02-b/)", rewritten)
                self.assertIn("![A figure](../../figures/assets/M00/a.svg)", rewritten)
                site.select_language("en")
                with self.assertRaisesRegex(site.SiteError, "missing English link target"):
                    site.rewrite_partial_links(text, "part-1-foundations/M00/M00-01-a.md")

    def test_minimal_english_strict_build_has_same_lesson_links_and_self_canonical(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            temporary = Path(directory)
            site.select_language("en", allow_partial=True)
            with patch.object(site, "CONFIG_PATH", temporary / "mkdocs.yml"):
                config = site.localized_config()
            relative = "part-1-foundations/M00/M00-03-functions-input-output.md"
            suffix = site.page_url(relative)
            config["extra"]["bilingual"]["en_pages"] = ["", suffix]
            config["docs_dir"], config["site_dir"] = "docs", "site"
            config["nav"] = [{"Home": "index.md"}, {"Functions": relative}]
            site.write_text(temporary / "docs/index.md", "# English preview\n")
            site.write_text(temporary / "docs" / relative, "# Functions\n\nA function maps inputs to outputs.\n")
            for asset in ("stylesheets/extra.css", "javascripts/mathjax.js"):
                site.write_text(temporary / "docs/assets" / asset, site.read_text(site.ROOT / "site/assets" / asset))
            import yaml
            site.write_text(temporary / "mkdocs.yml", yaml.safe_dump(config, allow_unicode=True))
            with contextlib.redirect_stdout(io.StringIO()):
                build(load_config(config_file=str(temporary / "mkdocs.yml")), dirty=False)
            html = site.read_text(temporary / "site" / Path(relative).with_suffix("") / "index.html")
            self.assertIn('<html lang="en"', html)
            self.assertIn(f'<link rel="canonical" href="{site.PUBLIC_ROOT}en/{suffix}">', html)
            self.assertIn(f'hreflang="ko" href="{site.PUBLIC_ROOT}{suffix}"', html)
            self.assertIn(f'hreflang="en" href="{site.PUBLIC_ROOT}en/{suffix}"', html)
            self.assertIn(f'href="{site.PUBLIC_PATH}{suffix}" target="_self" hreflang="ko"', html)
            self.assertIn(f'href="{site.PUBLIC_PATH}en/{suffix}" target="_self" hreflang="en"', html)
            self.assertIn('new URL("/ai-math-guide/",location)', html)
            self.assertIn("Partial English preview", html)
            self.assertTrue((temporary / "site/search/search_index.json").exists())
            self.assertTrue((temporary / "site/sitemap.xml").exists())

    def test_source_snapshot_tracks_content_and_site_assets(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            script = root / "scripts/site.py"
            config = root / "site/mkdocs.base.yml"
            lesson = root / "translations/en/part-1-foundations/M00/M00-01-fixture.md"
            asset = root / "site/assets/stylesheets/extra.css"
            for path in (script, config, lesson, asset):
                site.write_text(path, "fixture\n")
            with patch.object(site, "ROOT", root), patch.object(site, "BASE_CONFIG", config), patch.object(site, "__file__", str(script)):
                site.select_language("en", allow_partial=True)
                first = site.source_snapshot([{"path": lesson}])
                site.write_text(lesson, "updated fixture\n")
                second = site.source_snapshot([{"path": lesson}])
                self.assertNotEqual(first, second)
                site.write_text(asset, "updated style\n")
                self.assertNotEqual(second, site.source_snapshot([{"path": lesson}]))

    def test_shared_svg_consumed_results_and_gpu_option_make_staging_stale(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            build_root = root / ".build"
            script, config = root / "scripts/site.py", root / "site/mkdocs.base.yml"
            lesson = root / "translations/en/part-2-neural-computation/N05/N05-01-fixture.md"
            code = root / "labs/N05/n05_01_fixture.py"
            result = build_root / "n05/results/n05_01_fixture.json"
            unrelated = build_root / "n05/results/n05_02_other.json"
            svg = root / "figures/assets/N05/N05-01-fixture.svg"
            for path in (script, config, lesson, code, result, svg, unrelated):
                site.write_text(path, "fixture\n")
            registry = {"N05-01": {"example_id": "n05_01_fixture", "source_path": code}, "N05-02": {"example_id": "n05_02_other", "source_path": code}}
            lessons = [{"id": "N05-01", "stage": "N05", "path": lesson}]
            with patch.object(site, "ROOT", root), patch.object(site, "BUILD_ROOT", build_root), patch.object(site, "BASE_CONFIG", config), patch.object(site, "__file__", str(script)), patch.object(site, "load_n05_example_registry", return_value=registry), patch.object(site, "load_gpu_registries", return_value=({}, {})), patch.dict(os.environ, {"AI_MATH_GPU_RESULTS": "0"}):
                site.select_language("en", allow_partial=True)
                snapshot = site.CONFIG_PATH.parent / "source-snapshot.json"
                site.write_text(snapshot, json.dumps(site.source_snapshot(lessons)))
                site.assert_current_sources(lessons)
                for path in (svg, result):
                    site.write_text(path, "changed fixture\n")
                    with self.assertRaisesRegex(site.SiteError, "staging is stale"):
                        site.assert_current_sources(lessons)
                    site.write_text(path, "fixture\n")
                site.write_text(unrelated, "unconsumed output changed\n")
                site.assert_current_sources(lessons)
                with patch.dict(os.environ, {"AI_MATH_GPU_RESULTS": "1"}):
                    with self.assertRaisesRegex(site.SiteError, "staging is stale"):
                        site.assert_current_sources(lessons)

    def test_prepare_rejects_source_changed_after_staging_and_records_start_snapshot(self) -> None:
        base_config = site.read_text(site.BASE_CONFIG)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            relative = "part-1-foundations/M00/M00-01-fixture.md"
            source = root / "translations/en" / relative
            config, script = root / "site/mkdocs.base.yml", root / "scripts/site.py"
            site.write_text(root / relative, self.fixture_lesson(english=False))
            site.write_text(source, self.fixture_lesson(english=True))
            site.write_text(config, base_config)
            site.write_text(script, "# script fixture\n")
            site.write_text(root / "site/assets/stylesheets/extra.css", ".fixture {}\n")
            original_write = site.write_text

            def write_then_change_source(path: Path, text: str) -> None:
                original_write(path, text)
                if path == site.DOCS_DIR / relative:
                    original_write(source, site.read_text(source).replace("A variable", "Changed original"))

            with patch.object(site, "ROOT", root), patch.object(site, "BUILD_ROOT", root / ".build"), patch.object(site, "BASE_CONFIG", config), patch.object(site, "__file__", str(script)), patch.object(site, "load_n05_example_registry", return_value={}), patch.object(site, "load_stage_example_registry", return_value={}), patch.object(site, "load_gpu_registries", return_value=({}, {})):
                site.select_language("en", allow_partial=True)
                with patch.object(site, "write_text", side_effect=write_then_change_source):
                    with self.assertRaisesRegex(site.SiteError, "sources changed during prepare"):
                        site.prepare()
                self.assertIn("A variable", site.read_text(site.DOCS_DIR / relative))
                self.assertIn("Changed original", site.read_text(source))
                self.assertFalse(site.CONFIG_PATH.exists())
                self.assertFalse((site.CONFIG_PATH.parent / "source-snapshot.json").exists())
                with contextlib.redirect_stdout(io.StringIO()):
                    site.prepare()
                site.assert_current_sources(site.discover_all_lessons())

    def test_locale_validation_defers_cross_language_links_until_merge(self) -> None:
        site.select_language("en", allow_partial=True)
        self.assertIsNone(site.resolve_generated_url(site.SITE_DIR / "index.html", "/ai-math-guide/curriculum/"))
        self.assertEqual(site.resolve_generated_url(site.SITE_DIR / "index.html", "/ai-math-guide/en/"), site.SITE_DIR / "index.html")
        site.select_language("ko", isolated=True)
        self.assertIsNone(site.resolve_generated_url(site.SITE_DIR / "index.html", "/ai-math-guide/en/"))

    def test_final_merge_requires_verified_translations_before_mutation(self) -> None:
        failed = subprocess.CompletedProcess([], 1, "", "translation audit is incomplete")
        with patch.object(site.subprocess, "run", return_value=failed) as run, patch.object(site, "validate") as validate, patch.object(site.shutil, "rmtree") as remove:
            with self.assertRaisesRegex(site.SiteError, "translation audit is incomplete"):
                site.merge_sites()
            self.assertIn("--require-verified", run.call_args.args[0])
            validate.assert_not_called()
            remove.assert_not_called()

    def test_search_terms_must_occur_on_the_expected_lesson_page(self) -> None:
        relative = "part-1-foundations/M03/M03-11-jacobian.md"
        location = site.page_url(relative)
        for term in ("Jacobian", "자코비안"):
            with self.subTest(term=term):
                glossary = {"location": "glossary/#jacobian", "text": term}
                self.assertEqual(site.search_page_hits([glossary], term, relative), [])
                expected = {"location": location + "#definition", "title": term}
                self.assertEqual(site.search_page_hits([glossary, expected], term, relative), [expected["location"]])
                self.assertEqual(site.search_page_hits([{"location": location, "text": "unrelated"}], term, relative), [])
        self.assertEqual(site.SEARCH_TERMS["mutual information"], "M04-14")
        self.assertEqual(site.SEARCH_TERMS["상호정보량"], "04-GLOSSARY.md")
        glossary = {"location": "glossary/#mutual-information", "text": "상호정보량"}
        self.assertEqual(site.search_page_hits([glossary], "상호정보량", site.PUBLIC_DOCUMENTS["04-GLOSSARY.md"]), [glossary["location"]])

    def test_partial_merge_checks_both_search_indexes_and_language_targets(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            build_root = root / ".build"
            for locale in ("ko", "en"):
                output = build_root / locale / "site"
                site.write_text(output / "index.html", '<a href="/ai-math-guide/en/">English</a><a href="/ai-math-guide/">Korean</a>')
                site.write_text(output / "sitemap.xml", "<urlset/>\n")
                site.write_text(output / "search/search_index.json", json.dumps({"docs": [{"location": ""}]}))
            legacy = build_root / "site/index.html"
            site.write_text(legacy, "existing Korean preview")
            gate = subprocess.CompletedProcess([], 0, '{"verified": 0}', "")
            with patch.object(site, "ROOT", root), patch.object(site, "BUILD_ROOT", build_root), patch.object(site, "validate") as validate, patch.object(site.subprocess, "run", return_value=gate) as run, contextlib.redirect_stdout(io.StringIO()):
                site.merge_sites(allow_partial=True)
                self.assertEqual(validate.call_count, 2)
                self.assertNotIn("--require-verified", run.call_args.args[0])
                self.assertEqual(site.read_text(legacy), "existing Korean preview")
                summary = json.loads(site.read_text(build_root / "bilingual/validation.json"))
                self.assertEqual(summary["broken_links_or_assets"], 0)
                self.assertTrue(summary["partial_preview"])
                for locale, location in (
                    ("en", "../index.html#definition"),
                    ("en", "%2e%2e/index.html"),
                    ("en", "https://example.com/"),
                    ("en", "/ai-math-guide/"),
                    ("ko", "en/"),
                    ("ko", "./en/"),
                ):
                    with self.subTest(locale=locale, location=location):
                        search = build_root / locale / "site/search/search_index.json"
                        site.write_text(search, json.dumps({"docs": [{"location": location}]}))
                        with self.assertRaisesRegex(site.SiteError, "outside locale search target"):
                            site.merge_sites(allow_partial=True)
                        site.write_text(search, json.dumps({"docs": [{"location": ""}]}))
                site.write_text(build_root / "en/site/index.html", '<a href="/ai-math-guide/en/missing/">Missing translation</a>')
                with self.assertRaisesRegex(site.SiteError, "missing/"):
                    site.merge_sites(allow_partial=True)

    def test_merge_cli_does_not_validate_again_after_assembly(self) -> None:
        with patch.object(site.sys, "argv", ["site.py", "merge", "--allow-partial"]), patch.object(site, "merge_sites") as merge, patch.object(site, "validate") as validate:
            self.assertEqual(site.main(), 0)
            merge.assert_called_once_with(allow_partial=True)
            validate.assert_not_called()

    def test_preview_handler_maps_public_prefix_to_merged_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            handler = site.BilingualPreviewHandler.__new__(site.BilingualPreviewHandler)
            handler.directory = directory
            for url, expected in (
                ("/ai-math-guide/", ""),
                ("/ai-math-guide", ""),
                ("/ai-math-guide/en/?q=example", "en"),
                ("/ai-math-guide/en/assets/stylesheets/extra.css", "en/assets/stylesheets/extra.css"),
            ):
                with self.subTest(url=url):
                    self.assertEqual(Path(handler.translate_path(url)), Path(directory) / expected)
            target = Path(handler.translate_path("/ai-math-guide/%2e%2e/secret.txt"))
            self.assertTrue(target.is_relative_to(Path(directory)))

    def test_preview_requires_both_locales_and_binds_only_localhost(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            build_root = Path(directory) / ".build"
            with patch.object(site, "BUILD_ROOT", build_root), patch.object(site, "ThreadingHTTPServer") as server:
                with self.assertRaisesRegex(site.SiteError, "both locales"):
                    site.serve_bilingual(8009)
                server.assert_not_called()
                for prefix in ("", "en"):
                    site.write_text(build_root / "bilingual/site" / prefix / "index.html", "preview")
                with contextlib.redirect_stdout(io.StringIO()):
                    site.serve_bilingual(8009)
                self.assertEqual(server.call_args.args[0], ("127.0.0.1", 8009))
                self.assertEqual(server.call_args.args[1].keywords["directory"], str(build_root / "bilingual/site"))
                server.return_value.__enter__.return_value.serve_forever.assert_called_once()

    def test_build_and_deploy_use_verified_bilingual_artifact(self) -> None:
        import yaml

        wrapper = site.read_text(site.ROOT / "scripts/build_site.ps1")
        gate = wrapper.index("check-translations --require-verified")
        self.assertLess(gate, wrapper.index("unittest discover"))
        self.assertLess(gate, wrapper.index("if ($RunExamples)"))
        self.assertIn('param([switch]$RunExamples)', wrapper)
        self.assertIn('".build/$Language/mkdocs.yml"', wrapper)
        self.assertIn('"scripts/site.py" merge', wrapper)
        preview = site.read_text(site.ROOT / "scripts/preview_site.ps1")
        self.assertIn('"scripts/site.py" serve --port $Port', preview)
        self.assertNotIn("mkdocs serve", preview)
        workflow = yaml.safe_load(site.read_text(site.ROOT / ".github/workflows/site-check.yml"))
        steps = workflow["jobs"]["build"]["steps"]
        names = [step["name"] for step in steps]
        self.assertLess(names.index("Require reviewed and verified full English edition"), names.index("Run required N05 examples"))
        upload = next(step for step in steps if step["name"] == "Upload GitHub Pages artifact")
        self.assertEqual(upload["with"]["path"], ".build/bilingual/site")
        self.assertIn("github.ref == 'refs/heads/main'", upload["if"])
        self.assertIn("github.event_name == 'push'", upload["if"])
        self.assertNotIn("pull_request", upload["if"])


if __name__ == "__main__":
    unittest.main()
