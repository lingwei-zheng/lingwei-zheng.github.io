# Experiment Log

## Site Checks

- date: 2026-05-20
- goal: Establish sync context for the Quarto website repository.
- command / script: `quarto --version`; `quarto render`
- config / parameters: Quarto website configured by `_quarto.yml`, output directory `docs/`.

## Result

- key result: Quarto is available locally, version `1.7.27`; full render succeeds.
- output files: rendered website under `docs/`.
- notable behavior: Initial render included root-level sync Markdown files, so `_quarto.yml` was updated with an explicit render scope for `.qmd` site sources only.

## Decision

- keep / discard / rerun: Keep the explicit render scope in `_quarto.yml`.
- next experiment: Browser-preview the rendered site after the next content or layout change.
- checkpoint owner: sync.
- related workflow state files: `.codex/project.yaml`, `TODO.md`, `HANDOFF.md`.
