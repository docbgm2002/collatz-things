#!/usr/bin/env python3
"""Validate the structure and repository references of CLAIM_LEDGER.md."""

from __future__ import annotations

import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LEDGER_PATH = REPO_ROOT / "CLAIM_LEDGER.md"

CLAIM_ID_RE = re.compile(r"[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*\Z")
REPOSITORY_PATH_RE = re.compile(
    r"(?<![A-Za-z0-9_.-])"
    r"((?:docs|scripts)/[A-Za-z0-9_./-]+\.(?:md|py))"
)
STATUS_PREFIXES = (
    "Proved",
    "Finite",
    "Conditional",
    "Known",
    "**Refuted**",
)


def claim_rows(lines: list[str]) -> list[tuple[int, list[str]]]:
    """Return parsed rows from the ledger's five-column claim table."""
    header_index = next(
        index
        for index, line in enumerate(lines)
        if line == "| ID | Claim | Status | Source | Verification / dependency |"
    )

    rows: list[tuple[int, list[str]]] = []
    for index in range(header_index + 2, len(lines)):
        line = lines[index]
        if not line.startswith("|"):
            break
        cells = [cell.strip() for cell in line[1:-1].split("|")]
        rows.append((index + 1, cells))
    return rows


def validate() -> tuple[list[str], int]:
    lines = LEDGER_PATH.read_text(encoding="utf-8").splitlines()
    errors: list[str] = []

    try:
        rows = claim_rows(lines)
    except StopIteration:
        return ["claim table header is missing"], 0

    seen_ids: dict[str, int] = {}
    for line_number, cells in rows:
        if len(cells) != 5:
            errors.append(
                f"line {line_number}: expected 5 cells, found {len(cells)}; "
                "use \\lvert and \\rvert instead of raw | inside mathematics"
            )
            continue

        claim_id, claim, status, source, verification = cells
        if not CLAIM_ID_RE.fullmatch(claim_id):
            errors.append(f"line {line_number}: invalid claim ID {claim_id!r}")
        elif claim_id in seen_ids:
            errors.append(
                f"line {line_number}: duplicate claim ID {claim_id!r}; "
                f"first used on line {seen_ids[claim_id]}"
            )
        else:
            seen_ids[claim_id] = line_number

        if not claim:
            errors.append(f"line {line_number}: claim text is empty")
        if not status.startswith(STATUS_PREFIXES):
            errors.append(
                f"line {line_number}: unrecognized status class {status!r}"
            )

        source_paths = REPOSITORY_PATH_RE.findall(source)
        if not source_paths:
            errors.append(
                f"line {line_number}: source cell has no docs/*.md reference"
            )

        for path in REPOSITORY_PATH_RE.findall(f"{source} {verification}"):
            if not (REPO_ROOT / path).is_file():
                errors.append(
                    f"line {line_number}: referenced path does not exist: {path}"
                )

    if not rows:
        errors.append("claim table contains no rows")

    return errors, len(rows)


def main() -> None:
    errors, row_count = validate()
    if errors:
        print("Claim ledger validation: FAIL")
        for error in errors:
            print(f"  - {error}")
        raise SystemExit(1)

    print(
        "Claim ledger validation: PASS "
        f"({row_count} rows; unique IDs, status classes, and paths checked)"
    )


if __name__ == "__main__":
    main()
