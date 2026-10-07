# Bilingual navigation and release specification

Approved user instruction. Both design and publication transitions are authorized in advance. This file is an operations document, not a public page.

In C:\Users\klim\Documents\ChatGPT\수학공부, preserve the verified Korean and English editions while improving the website’s reader-facing information architecture, navigation, and search metadata. Validate representative screens, apply the verified design across both editions, complete integration checks, then push the finished bilingual release to the main branch of leeklim/ai-math-guide and publish it through the existing GitHub Pages workflow.

ADVANCE AUTHORIZATION

The user has authorized both transitions:
1. After representative screen validation passes, proceed to full rollout without waiting for user approval.
2. After final validation passes, push the completed bilingual release to main and deploy it publicly without requesting another release confirmation.

Keep both validation checkpoints. Fix detected defects before proceeding. This authorization covers the website changes and publication described below. Separate approval remains necessary for substantive source corrections, unrelated repositories, or changes beyond this scope. Missing credentials or account access may still require user input.

1. Baseline and scope

- Inspect the completed bilingual editions and existing verification records, then record the baseline. Do not regenerate the English edition or repeat the completed translation project.
- Preserve 199 lessons and 1,154 exercise–solution pairs in each language, the existing public supporting documents, and 1,355 shared SVG assets.
- Preserve the manuscripts’ educational scope, mathematical meaning, writing style, equations, exercises, solutions, figures, lab code, and execution results.
- Keep Korean pages at the existing root and English pages under /en/. Preserve filenames, internal lesson IDs, and existing URLs.
- Preserve the existing body-reading design. Do not redesign the reading width, typography, line spacing, or equation, table, and figure presentation across the site.
- Use the existing MkDocs Material theme and build structure. Do not replace the framework, introduce unnecessary plugins, create a separate translation or content-management platform, or refactor unrelated code.
- Preserve unrelated files, directories, and existing changes.
- Store the execution rules and progress in existing documentation where practical, or add a minimal revision specification.

2. Reader-facing information architecture

Organize the homepage and navigation so a first-time reader can choose a learning route:

- Start from the beginning
- Full learning path
- Part 1: Mathematical foundations
- Part 2: Neural networks and Transformers
- Part 3: Model interpretability
- Part 4: Optional advanced topics
- Reference materials: glossary, execution environment, architecture guide, and GPU/Pythia guide

Requirements:

- Place modules and lessons under their parts in educational order.
- Use descriptive Korean and English names in reader-facing navigation.
- Make the current part and module easy to identify. Avoid expanding all other parts and reference sections by default.
- Let readers return home through the top logo or site title. Remove redundant displays of the long site name from the sidebar.
- Show the current location through name-based breadcrumbs. Keep the right-hand table of contents focused on the current lesson.
- Move environment instructions into reference materials, while linking to them from the first relevant lab or real-model lesson.
- Reuse the existing full learning path page. Make each lesson title link to its lesson.
- Do not add overview pages or duplicate navigation without a demonstrated need.
- Keep language switching mapped to the corresponding page of the same lesson.
- Use a coherent, restrained design with clear hierarchy, balanced spacing, and readable labels in both languages.

Distinguish the formal learning sequence from navigation shortcuts:

- Moving reference materials must not disrupt previous/next lesson navigation or the sequence described in lesson prose.
- Treat “Start from the beginning” as a shortcut rather than a second occurrence in the formal lesson sequence.
- Do not weaken lesson coverage or unique-placement checks by allowing arbitrary duplicates.

3. Remove management IDs from reader-facing labels

Keep IDs such as M03-11 and N05-15 for internal management. Replace them with descriptive names where readers need to understand the content.

Inspect:

- Sidebar and menus
- Page H1 headings and breadcrumbs
- Prerequisites and cross-lesson references in prose
- The full learning path
- Previous/next lesson labels
- Search result titles and summaries

Implementation requirements:

- Prefer the existing public-site preparation or presentation layer so the verified source manuscripts and translation-review hashes remain intact.
- Do not delete IDs without preserving their meaning. Replace them with the correct lesson name and link where needed.
- Review exceptions in context, including Korean particles and English sentence connections.
- Preserve filenames, URLs, internal identifiers, and IDs required by code.
- Preserve educational part and section numbering, exercise numbers, and equation numbers.
- Do not reimplement existing ID-free browser titles or other working transformations.
- Do not rely on CSS hiding or post-render JavaScript replacement while leaving search and accessibility information unchanged.
- Protect lab code, equations, and output blocks from display-name transformations.

Preserve existing URL fragments and heading anchors:

- Retain compatibility anchors if changing a displayed heading would remove an existing anchor.
- Check that internal links reach the target fragment, not only an existing target file.
- Maintain Korean–English page correspondence through internal IDs and the existing mapping.

4. Representative implementation and validation

Implement the shared design on representative screens before full rollout.

Include:

- Homepage and full learning path
- A foundational lesson
- A lesson with many prerequisites and cross-lesson references
- A lesson with long English prose and lab code
- An advanced lesson
- Search results and a lesson entered through search

Inspect actual HTML in both languages under these conditions:

- Desktop: 1440 × 900
- Mobile: 390 × 844
- Light and dark themes

Check appearance and reader tasks:

- Start learning from the beginning.
- Find a chosen part, module, and lesson.
- Follow a prerequisite link and return to the original lesson.
- Identify the current location after entering through search.
- Switch languages without leaving the corresponding lesson.
- Follow previous/next links in the correct learning order.
- Use menus, search, and language switching through keyboard navigation and mobile touch.
- Confirm that long titles and English text do not clip or distort the navigation.

Use existing Material features first. Make minimal template or CSS changes where testing establishes a limitation.

Record representative screenshots, test results, and local preview addresses. Correct detected defects, then proceed to full rollout without requesting user approval.

5. Full rollout and parallel work

Keep the existing 17 work units:

- M00, M01, M02, M03, and M04 as separate units
- N05-01–14 and N05-15–28 as separate units
- I06, I07, and I08 as separate units
- A09 GEO, DYN, SYM, LRN, KER, RMT, and CAU as seven separate units

The main agent owns shared presentation rules. Parallelize lesson-specific exceptions, page descriptions, and comparison review across non-overlapping ranges.

Default roles:

- Main agent: shared code, terminology, site structure, and integration validation
- Two workers: separate ranges of display-name exceptions and page descriptions
- One reviewer: source fidelity, Korean–English correspondence, and rendered results

Adjust roles according to lesson length and review backlog. Do not accumulate a large draft backlog and postpone review until the end.

Do not let multiple workers edit shared code or shared ledgers at the same time. Integrate results with clear ownership and review status.

6. Search and sharing metadata

Preserve and validate existing canonical URLs, hreflang, document language, corresponding-language links, and search functionality.

Improve:

- Page-specific Korean and English descriptions
- Consistency across navigation labels, H1 headings, and search titles
- Open Graph and Twitter sharing titles, descriptions, URLs, and locale information
- Exact public-page coverage in sitemaps
- Search Console verification and sitemap-submission preparation

Page-description requirements:

- Ground each description in the page’s actual content and learning objectives.
- Describe what distinguishes the page from others.
- Avoid repeated module-level boilerplate and keyword stuffing.
- Do not claim outcomes or benefits absent from the manuscript.
- Do not distort meaning to meet a fixed character count.
- Do not create new sharing images as mandatory deliverables.

Use minimal site metadata outside the manuscripts if that preserves reviewed sources. Include new metadata in change detection and build-freshness checks so the build cannot reuse stale prepared content.

Check each language’s sitemap against the existing 205 public documents and compare its URLs, canonical values, and language coverage.

- Validate both Korean and English sitemaps.
- Exclude private documents, production records, local results, and preview URLs.
- Keep the existing two sitemaps if they suffice. Do not add a sitemap index without a need.

Inspect robots and noindex behavior at the actual public addresses. Do not assume a robots.txt file under the project path controls the host. Obtain separate approval if a host-root change or work in another repository becomes necessary.

Prepare Search Console for the URL-prefix property:
https://leeklim.github.io/ai-math-guide/

- Request required verification values and unavailable account permissions before the final deployment where possible.
- Use an HTML verification meta tag, verification file, or another method suited to the current site.
- Do not assume consent-gated, delayed GA4 loading can establish site ownership.
- If verification values or access are missing, report the required input and pending tasks while continuing unaffected work.

Do not promise search rankings, traffic growth, or indexing dates. Do not use them as completion criteria.

7. Separate treatment of source errata

Keep previously recorded source uncertainties separate from website design work.

- Distinguish confirmed errors, statements missing conditions, and editorial issues.
- Do not revive concerns that earlier review withdrew.
- Present a specific correction proposal and obtain separate approval before changing mathematical meaning, exercises, solutions, or figures.
- Apply approved corrections to both languages and update the affected comparison and verification records.
- Do not alter mathematical content or claim strength through display-name transformations.
- Do not expand errata review into another full-book explanation revision, figure revision, or retranslation project.

8. Validation cadence and progress records

For individual files and small batches, inspect the affected diff, display names, links, metadata, and preservation of meaning.

- Do not repeat whole-book hash comparisons, complete test suites, or full HTML builds for each small batch.
- At work-unit completion, update the ledger and perform the necessary HTML reflection checks.
- For changes to shared templates, link processing, search, metadata, or build code, run the relevant site-wide checks.
- Do not rerun tests because progress wording alone changed.
- Do not create a separate validation system to reduce testing. Extend existing checks only where needed.

Final integration validation must cover:

- Lesson counts and exercise–solution preservation in both languages
- Preservation of manuscripts, figures, code, and execution results
- Source audit, English-reading lint, and existing relevant tests
- Valid translation-review records
- Internal links and fragments
- Complete lesson access, unique placement, and learning order
- Unwanted management-ID exposure on reader-facing screens
- Search, language switching, canonical URLs, hreflang, page descriptions, and sharing metadata
- Exact sitemap coverage
- Broken asset paths and accidental exposure of production documents
- Strict bilingual HTML builds and the final merged artifact
- Existing GA4 consent, rejection, and local-host blocking behavior

Do not regenerate unchanged SVGs, run large models or GPU experiments, or recompute unchanged lab results. Reuse existing verified results with freshness checks.

Focus visual review on representative page types and pages with exceptions or detected defects. Validate shared layout changes in both languages, desktop and mobile layouts, and light and dark themes.

Record completed ranges, substantive changes, checks performed, detected issues, and next steps. Do not report a test or screen inspection as passed unless it was performed.

9. Final release validation and authorized publication

At local readiness, record and report:

- Korean and English preview addresses
- The revised information architecture and representative screens
- Preservation results and actual validation evidence
- Known limitations and pending external configuration
- The exact release scope

This report is informational. Do not wait for another design or release confirmation.

The user has authorized publication of the completed bilingual site:

- Once final validation passes, integrate the verified release into main and push it to leeklim/ai-math-guide.
- Deploy through the existing GitHub Pages workflow.
- Publish the completed Korean and English editions together. Do not publish intermediate modules or unfinished English pages.
- Do not publish changes that fail required checks.
- Group local commits by implementation scope and verification state. Preserve unrelated changes and existing history.
- Do not force-push or rewrite history.
- Keep remote changes within this repository and the defined release scope. Avoid unnecessary PRs or external preview uploads.

Missing credentials, unavailable account access, or a required scope expansion may require user input. These are not renewed design or publication approval gates. Continue work that remains possible and report the affected task.

10. Post-deployment verification and completion

After deployment, inspect the actual public site:

- Korean and English homepages and representative lessons
- Navigation, search, learning order, and language switching
- Equations, tables, figures, and mobile presentation
- Canonical URLs, hreflang, page descriptions, and sharing metadata
- Both sitemaps and indexing-blocking settings
- Existing GA4 measurement ID G-VXDGRXQFT3 and consent flow
- Actual GA4 receipt of a consented visit to the public site
- Search Console ownership verification and sitemap submission within authorized account access

Report any missing input required for account access or external-service verification. Do not substitute local tests for actual GA4 receipt or Search Console verification.

Completion requires:

- The validated navigation structure applies across both language editions.
- Manuscripts, learning order, URLs, anchors, exercises, solutions, figures, and code remain preserved.
- Reader-facing labels and search/sharing metadata are consistent and accurate.
- Integration checks and actual screen inspections have passed.
- The completed bilingual release has been pushed and publicly deployed under the user’s advance authorization.
- Post-deployment checks and the authorized external configuration are complete.
- The final report distinguishes public URLs, verified results, and remaining limitations.

Distinguish “ready for deployment locally” from “publicly deployed and verified.” Do not mark the whole Goal complete while required deployment or external verification remains pending.

If progress requires missing credentials, new authority, or a scope change, report the blocker, attempted in-scope alternatives, remaining work, and the input needed. Do not silently waive requirements or redefine completion.
