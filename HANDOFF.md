# Handoff

## Current task

Organize the personal website repository so it can be understood and resumed cleanly across Codex sessions or devices.

## What was done

- Identified the project as a Quarto static website for Lingwei Zheng's academic homepage.
- Confirmed `docs/` is the Quarto output directory used for GitHub Pages.
- Confirmed `origin` points to `https://github.com/lingwei-zheng/lingwei-zheng.github.io.git`.
- Added the sync path contract in `.codex/project.yaml`.
- Added root-level `TODO.md` and `HANDOFF.md`.
- Added notes files for site-maintenance and publication-writing context.
- Updated `_quarto.yml` so Quarto renders only site `.qmd` files, preventing sync Markdown files from being published.
- Ran `quarto render` successfully after the render scope was corrected.
- Removed stale rendered include artifacts under `files/includes/`.
- Removed tracked local `.Rhistory` and added it to `.gitignore`.
- Cleaned template comments and normalized external links to HTTPS.

## Current status

- working: Local checkout is on `main` and tracks `origin/main`.
- working: Quarto is installed locally; detected version is `1.7.27`.
- working: `quarto render` completes successfully with 16 rendered `.qmd` pages.
- working: Browser smoke audit passed for Home, Publications, Presentations, Teaching, and Contact.
- blocked: Nothing is currently blocked.
- not yet checked: Visual browser review of the rendered site.

## Project map

- `_quarto.yml`: website configuration, navigation, theme, analytics, output directory, and includes.
- `index.qmd`: homepage biography, education, awards, and recent news.
- `publications.qmd`: peer-reviewed publications.
- `presentation.qmd`: conference presentations.
- `teaching.qmd`: teaching and professional service.
- `contact.qmd`: contact page.
- `posts/`: news/event/paper post pages and templates.
- `files/`: profile images, CV, images, favicon, and Quarto include snippets.
- `_extensions/`: vendored Quarto extensions.
- `docs/`: rendered website output served by GitHub Pages.

## Next steps

1. Inspect generated `docs/listings.json`, `docs/search.json`, and `docs/sitemap.xml` before committing; the current render changed ordering.
2. Run a browser preview if making visual/content changes.
3. Push `main` when the rendered site and source files are consistent.

## Constraints

- Treat `.codex/project.yaml` as the canonical project path map.
- Keep sync-owned files limited to `.codex/project.yaml`, `TODO.md`, `HANDOFF.md`, `notes/`, and optional `sync/`.
- Do not overwrite generated `docs/` blindly; inspect render output first.
- Do not allow root-level sync Markdown files to enter the public site render.
- Do not delete template-derived `_extensions/` without testing the site.
- Keep GitHub Pages deployment compatible with Quarto's `output-dir: docs`.
