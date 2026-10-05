"""Reporting must handle empty levels without changing their computed mass."""

import contextlib
import io
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from explore_repunit_sync_tree import print_report


class SyncTreeReportingTests(unittest.TestCase):
    def test_empty_levels_have_undefined_ratios_and_zero_mass(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            hits = print_report(gap=2, through_step=4, max_total=4, common_depth=4)
        self.assertEqual(hits, set())
        self.assertEqual(output.getvalue().count("level-mass ratio=n/a"), 3)
        self.assertEqual(output.getvalue().count("cumulative=0/8"), 3)
        self.assertIn("depth-truncated lower bounds", output.getvalue())

    def test_nonempty_ratio_and_union_mass_are_preserved(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            hits = print_report(gap=2, through_step=3, max_total=12, common_depth=12)
        self.assertEqual(len(hits), 121)
        self.assertIn("level-mass ratio=0.890625", output.getvalue())
        self.assertIn("cumulative=121/2048", output.getvalue())


if __name__ == "__main__":
    unittest.main()
