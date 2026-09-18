# Lingwei's homepage

Homepage made from a [quarto template](https://github.com/drganghe/quarto-academic-website-template).

For original examples and tips, please check:
<https://drganghe.github.io/quarto-academic-site-examples.html>

## Project structure

- `_quarto.yml`: Quarto website configuration.
- `index.qmd`: homepage profile, education, awards, and recent news.
- `publications.qmd`, `presentation.qmd`, `teaching.qmd`, `contact.qmd`: main site pages.
- `files/`: profile images, CV, favicon, and reusable includes.
- `posts/`: news and post pages.
- `docs/`: rendered site output used by GitHub Pages.

## Local workflow

Preview the site:

```bash
quarto preview
```

Render the site into `docs/`:

```bash
quarto render
```

Validate publication data before rendering:

```bash
python scripts/validate_publications.py
```

Before pushing content changes, inspect both the source `.qmd` files and the rendered `docs/` changes.

## Local CV workspace

`cv/` is the local workspace for bilingual CV preparation and updates. Start with
`cv/README.md`; the initial audit is `cv/audit/review-2026-09-18.md`.
The directory is excluded from Git and Quarto rendering/resource copying because
it contains private application materials. It lives under the existing OneDrive
folder; Git clones do not include it.

Published article metadata remains in `files/data/publications.yml`. The website
downloads `files/Lingwei_s_Resume.pdf`; `docs/files/Lingwei_s_Resume.pdf` is its
rendered copy. The website now uses the current English Quarto/Typst CV.
Run `cv/build.ps1` to build both languages, or
`cv/build.ps1 -Language en -SyncWebsite` to rebuild the English CV and update the
website source and rendered output together. To sync an already reviewed English
PDF, run `cv/sync-website.ps1`. These commands render locally; deployment still
requires committing and pushing the reviewed website changes.
Published articles and manuscripts are shared between languages; other profile
sections still live in the two QMD files. See `cv/README.md` for editing details.
