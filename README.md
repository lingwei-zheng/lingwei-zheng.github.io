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

Before pushing content changes, inspect both the source `.qmd` files and the rendered `docs/` changes.
