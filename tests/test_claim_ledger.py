"""Regression checks for silently omitted ledger claims."""

import contextlib
import io
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import verify_claim_ledger as ledger


HEADER = "| ID | Claim | Status | Source | Verification |"
SEPARATOR = "|---|---|---|---|---|"


def table(claim_id, header=HEADER):
    return [header, SEPARATOR,
            f"| {claim_id} | Example claim | Proved here | manuscript | Algebra |"]


class ClaimLedgerTests(unittest.TestCase):
    def validate_lines(self, lines):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "ledger.md"
            path.write_text("\n".join(lines) + "\n", encoding="utf-8")
            with patch.object(ledger, "LEDGER_PATH", path):
                return ledger.validate()

    def test_current_ledger_checks_every_claim_table(self):
        errors, count = ledger.validate()
        self.assertEqual(errors, [])
        # Independent count of the ID-bearing rows, not of recognized headers.
        lines = ledger.LEDGER_PATH.read_text(encoding="utf-8").splitlines()
        expected = sum(
            line.startswith("|") and len(line.split("|")) > 2
            and bool(ledger.CLAIM_ID_RE.fullmatch(line.split("|")[1].strip()))
            and line.split("|")[1].strip() != "ID"
            for line in lines
        )
        self.assertEqual(count, expected)

    def test_both_header_forms_and_aligned_separators(self):
        lines = table("AAA1") + [""] + table(
            "BBB1", HEADER.replace("Verification", "Verification / dependency"))
        lines[1] = "|:---|---:|:---:|---|---|"
        errors, count = self.validate_lines(["  " + line for line in lines])
        self.assertEqual((errors, count), ([], 2))

    def test_missing_separator_cannot_skip_first_claim(self):
        lines = table("AAA1")
        del lines[1]
        errors, count = self.validate_lines(lines)
        self.assertIn("separator", errors[0])
        self.assertEqual(count, 0)

    def test_malformed_separator_is_rejected(self):
        for separator in ("|---|---|---|---|", "|---|---|oops|---|---|"):
            with self.subTest(separator=separator):
                lines = table("AAA1")
                lines[1] = separator
                errors, _ = self.validate_lines(lines)
                self.assertIn("separator", errors[0])

    def test_damaged_header_cannot_hide_a_later_table(self):
        for damaged in (HEADER.replace("ID", "Id"), HEADER.replace("Source", "Sorce"),
                        HEADER.replace("Verification", "Verificatiom")):
            with self.subTest(header=damaged):
                errors, count = self.validate_lines(table("AAA1") + [""] + table("BBB1", damaged))
                self.assertIn("unrecognized claim table header", errors[0])
                self.assertEqual(count, 0)

    def test_missing_all_headers_returns_validation_error(self):
        errors, count = self.validate_lines(["# Empty ledger"])
        self.assertEqual(count, 0)
        self.assertIn("no five-column claim table header", errors[0])

    def test_main_reports_structural_error_without_traceback(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "ledger.md"
            path.write_text("# No tables\n", encoding="utf-8")
            output = io.StringIO()
            with patch.object(ledger, "LEDGER_PATH", path), contextlib.redirect_stdout(output):
                with self.assertRaises(SystemExit) as stopped:
                    ledger.main()
            self.assertEqual(stopped.exception.code, 1)
            self.assertIn("Claim ledger validation: FAIL", output.getvalue())

    def test_empty_later_table_is_not_accepted(self):
        errors, _ = self.validate_lines(table("AAA1") + ["", HEADER, SEPARATOR])
        self.assertIn("contains no rows", errors[0])

    def test_row_without_closing_pipe_is_rejected(self):
        lines = table("AAA1")
        lines[-1] = lines[-1][:-1]
        errors, _ = self.validate_lines(lines)
        self.assertIn("closing pipe", errors[0])

    def test_final_row_without_opening_pipe_cannot_be_silently_dropped(self):
        for claim_id in ("BBB1", "bad-id"):
            with self.subTest(claim_id=claim_id):
                lines = table("AAA1") + [table(claim_id)[-1][1:]]
                errors, count = self.validate_lines(lines)
                self.assertIn("opening pipe", errors[0])
                self.assertEqual(count, 0)

    def test_duplicate_ids_across_tables_still_fail(self):
        errors, count = self.validate_lines(table("AAA1") + [""] + table("AAA1"))
        self.assertEqual(count, 2)
        self.assertTrue(any("duplicate claim ID" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
