"""Regression tests for conclusive, inconclusive, and missing SMT results."""

import contextlib
import importlib.util
import io
from pathlib import Path
import sys
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "verify_machine_synthesis.py"
SPEC = importlib.util.spec_from_file_location("machine_synthesis_results", SCRIPT)
machine = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = machine
SPEC.loader.exec_module(machine)


@contextlib.contextmanager
def resource_limited_solver():
    """Use real Z3 with a tiny budget, rather than faking an unknown result."""
    original_solver = machine.z3.Solver

    def limited_solver():
        solver = original_solver()
        solver.set(rlimit=1)
        return solver

    with patch.object(machine.z3, "Solver", side_effect=limited_solver):
        yield


class SolverResultTests(unittest.TestCase):
    def setUp(self):
        machine.FAILURES.clear()
        machine.INCOMPLETE.clear()

    @unittest.skipUnless(machine.HAVE_Z3, "z3-solver is not installed")
    def test_satisfiable_and_infeasible_constraints(self):
        # h > 0, h <= 3h is feasible; h > 0, 3h <= h is not.
        self.assertEqual(machine.smt_feasible([("a", "a", 3, 1)]).status, "sat")
        self.assertEqual(machine.smt_feasible([("a", "a", 1, 3)]).status, "unsat")

    @unittest.skipUnless(machine.HAVE_Z3, "z3-solver is not installed")
    def test_real_unknown_preserves_reason(self):
        with resource_limited_solver():
            result = machine.smt_feasible([("a", "a", 3, 1)])
        self.assertEqual(result.status, "unknown")
        self.assertTrue(result.reason)

    def test_missing_solver_is_explicit(self):
        with patch.object(machine, "HAVE_Z3", False):
            result = machine.smt_feasible([("a", "a", 3, 1)])
        self.assertEqual(result.status, "unavailable")
        self.assertIn("not installed", result.reason)

    @unittest.skipUnless(machine.HAVE_Z3, "z3-solver is not installed")
    def test_unknown_cannot_pass_premise_cross_check(self):
        output = io.StringIO()
        with resource_limited_solver(), contextlib.redirect_stdout(output):
            machine.part_a()
        self.assertIn("[INCOMPLETE] z3 cross-check: unknown", output.getvalue())
        self.assertNotIn("[PASS] z3 cross-check", output.getvalue())
        self.assertNotIn("UNSAT", output.getvalue())
        self.assertTrue(machine.INCOMPLETE)
        self.assertFalse(machine.FAILURES)

    @unittest.skipUnless(machine.HAVE_Z3, "z3-solver is not installed")
    def test_unknown_search_does_not_invent_sat_or_agreement(self):
        output = io.StringIO()
        with resource_limited_solver(), contextlib.redirect_stdout(output):
            machine.part_c(101)
        text = output.getvalue()
        self.assertIn("z3 unknown:", text)
        self.assertIn("no-go (exact certificate)", text)
        self.assertIn("[PASS] the certificate's gain is a strict integer inequality", text)
        self.assertIn("[INCOMPLETE] certificate/SMT agreement", text)
        self.assertNotIn("[PASS] the certificate search and the SMT decision agree", text)
        self.assertNotIn("VACUOUS sat", text)
        self.assertNotIn("genuine sat", text)
        self.assertNotIn("UNSAT", text)
        self.assertTrue(machine.INCOMPLETE)

    def test_missing_solver_does_not_pass_search_agreement(self):
        output = io.StringIO()
        with (patch.object(machine, "HAVE_Z3", False),
              patch.object(machine, "repunit_orbit", return_value=[5, 1]),
              contextlib.redirect_stdout(output)):
            machine.part_c(3)
        text = output.getvalue()
        self.assertIn("z3 unavailable: z3-solver is not installed", text)
        self.assertNotIn("[PASS] the certificate search and the SMT decision agree", text)
        self.assertNotIn("VACUOUS sat", text)
        self.assertNotIn("genuine sat", text)
        self.assertNotIn("UNSAT", text)
        self.assertTrue(machine.INCOMPLETE)

    def test_incomplete_run_has_distinct_nonzero_exit(self):
        output = io.StringIO()
        with (patch.object(sys, "argv", [str(SCRIPT)]),
              patch.object(machine, "part_a", side_effect=lambda: machine.incomplete("unknown")),
              patch.object(machine, "part_b"), patch.object(machine, "part_c"),
              contextlib.redirect_stdout(output),
              self.assertRaises(SystemExit) as caught):
            machine.main()
        self.assertEqual(caught.exception.code, 2)
        self.assertIn("MACHINE-SYNTHESIS: INCOMPLETE", output.getvalue())
        self.assertNotIn("MACHINE-SYNTHESIS: PASS", output.getvalue())


if __name__ == "__main__":
    unittest.main()
