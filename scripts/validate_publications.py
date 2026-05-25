#!/usr/bin/env python3
"""Validate files/data/publications.yml schema and basic field quality."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REQUIRED_FIELDS = [
    "authors",
    "year",
    "title",
    "journal",
    "volume",
    "pages_or_article",
    "doi",
    "badges",
    "is_corresponding",
]

DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")


def main() -> int:
    path = Path("files/data/publications.yml")
    if not path.exists():
        print(f"ERROR: missing file: {path}")
        return 1

    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if not isinstance(data, list):
        print("ERROR: publications.yml must be a top-level list")
        return 1

    errors: list[str] = []
    for idx, item in enumerate(data, start=1):
        if not isinstance(item, dict):
            errors.append(f"item {idx}: must be a mapping")
            continue

        for field in REQUIRED_FIELDS:
            if field not in item:
                errors.append(f"item {idx}: missing required field '{field}'")

        year = item.get("year")
        if not isinstance(year, int):
            errors.append(f"item {idx}: year must be an integer")

        for text_field in ["authors", "title", "journal", "volume", "pages_or_article", "doi"]:
            value = item.get(text_field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"item {idx}: '{text_field}' must be a non-empty string")

        doi = item.get("doi")
        if isinstance(doi, str) and not DOI_RE.match(doi):
            errors.append(f"item {idx}: invalid DOI format '{doi}'")

        badges = item.get("badges")
        if not isinstance(badges, list):
            errors.append(f"item {idx}: 'badges' must be a list")

        is_corresponding = item.get("is_corresponding")
        if not isinstance(is_corresponding, bool):
            errors.append(f"item {idx}: 'is_corresponding' must be true/false")

    if errors:
        print("Validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print(f"OK: validated {len(data)} publication entries in {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())