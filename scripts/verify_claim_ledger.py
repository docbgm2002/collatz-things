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
# Compared after stripping leading emphasis markers, so bolded forms such as
# '**Refuted**' and '**Proved here, unconditional**' are accepted.
STATUS_PREFIXES = (
    "Proved",
    "Finite",
    "Conditional",
    "Known",
    "Refuted",
)


HEADER_RE = re.compile(
    r"\|\s*ID\s*\|\s*Claim\s*\|\s*Status\s*\|\s*Source\s*\|"
    r"\s*Verification(?:\s*/\s*dependency)?\s*\|\Z"
)
SEPARATOR_RE = re.compile(r":?-{3,}:?\Z")


def claim_rows(lines: list[str]) -> list[tuple[int, list[str]]]:
    """Return parsed rows from every five-column claim table in the ledger.

    Every pipe table in this claim ledger must have a recognized five-column
    header and separator. Validate those before collecting rows, so a damaged
    header cannot hide an entire table and a missing separator cannot hide its
    first claim. Both supported verification-column headings remain accepted.
    """
    rows: list[tuple[int, list[str]]] = []
    index = 0
    table_count = 0
    while index < len(lines):
        line = lines[index].strip()
        if not line.startswith("|"):
            first_cell = line.partition("|")[0].strip()
            if "|" in line and (CLAIM_ID_RE.fullmatch(first_cell) or line.count("|") >= 4):
                raise ValueError(f"line {index + 1}: claim table line is missing its opening pipe")
            index += 1
            continue
        if not HEADER_RE.fullmatch(line):
            raise ValueError(f"line {index + 1}: unrecognized claim table header")
        header_line = index + 1
        table_count += 1
        index += 1
        separator = lines[index].strip() if index < len(lines) else ""
        cells = [cell.strip() for cell in separator[1:-1].split("|")]
        if (not separator.startswith("|") or not separator.endswith("|")
                or len(cells) != 5
                or not all(SEPARATOR_RE.fullmatch(cell) for cell in cells)):
            raise ValueError(f"line {index + 1}: missing or malformed claim table separator")
        index += 1
        row_start = len(rows)
        while index < len(lines) and lines[index].strip().startswith("|"):
            line = lines[index].strip()
            if not line.endswith("|"):
                raise ValueError(f"line {index + 1}: claim row is missing its closing pipe")
            cells = [cell.strip() for cell in line[1:-1].split("|")]
            rows.append((index + 1, cells))
            index += 1
        if len(rows) == row_start:
            raise ValueError(f"line {header_line}: claim table contains no rows")
    if not table_count:
        raise ValueError("no five-column claim table header found")
    return rows


def validate() -> tuple[list[str], int]:
    lines = LEDGER_PATH.read_text(encoding="utf-8").splitlines()
    errors: list[str] = []

    try:
        rows = claim_rows(lines)
    except ValueError as error:
        return [str(error)], 0

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
        # Status classes may be emphasised, e.g. '**Proved here, unconditional**'.
        if not status.lstrip("*_").startswith(STATUS_PREFIXES):
            errors.append(
                f"line {line_number}: unrecognized status class {status!r}"
            )

        source_paths = REPOSITORY_PATH_RE.findall(source)
        # A row may be sourced to the manuscript rather than to a note in the
        # repository; QLG1 is the standing example.
        if not source_paths and "manuscript" not in source.lower():
            errors.append(
                f"line {line_number}: source cell has no docs/*.md reference "
                f"and does not cite the manuscript"
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
