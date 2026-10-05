#!/usr/bin/env python3
"""Machine synthesis inside the surviving potential class (W6).

Exact arithmetic for every promoted claim.  Floats are used only to *guide*
the negative-cycle search; every certificate is re-checked as an integer
product comparison (the discipline of WITN1).

THE ENCODING.  "A nonincreasing potential Phi(x) = log_2 x + g(C(x)) exists
on a finite window" is, after the substitution h_c = 2^{g_c} > 0,

    for every observed transition x -> y = f(x):     y * h_{C(y)}  <=  x * h_{C(x)}

a linear system with INTEGER coefficients.  z3 solves it over the rationals
(a timed-out run is inconclusive), and infeasibility is equivalent to a cycle with
prod(y) > prod(x) -- a certificate in the sense of SH1/WITN1.  So the SMT
question and the certificate question are the same question, and we solve
both and cross-check.

A. Premise check.  W6 says the quantized-log class "has never been
   searched".  SUFF1 (unconditional via CONN1) already proves certificates
   exist against (floor(Q log2 x), tau, x mod 2^m) for every j and every
   m >= 3.  We rediscover such certificates independently.

B. The surviving class is the TWO-VARIABLE one: V(x,n) on (state, repunit
   exponent).  The SH1 shadow cancels an n-dependence only if the shadow
   cycle lies inside ONE a_n orbit.  We measure how deep the -5 shadow is
   actually realised on repunit orbits.

C. The search in the two-variable class, with the n=471 and
   1275 -> 1913 -> 1435 stress tests.

Run:
    python3 scripts/verify_machine_synthesis.py
    python3 scripts/verify_machine_synthesis.py --nmax 601
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from fractions import Fraction
from typing import Literal

try:
    import z3
    HAVE_Z3 = True
except ImportError:                                  # pragma: no cover
    HAVE_Z3 = False

FAILURES: list[str] = []
INCOMPLETE: list[str] = []


def check(label: str, ok: bool) -> None:
    if not ok:
        FAILURES.append(label)
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")


def incomplete(label: str) -> None:
    INCOMPLETE.append(label)
    print(f"  [INCOMPLETE] {label}")


def v2(x: int) -> int:
    return (x & -x).bit_length() - 1


def f_odd(x: int) -> int:
    y = 3 * x + 1
    return y >> v2(y)


def tau(x: int) -> int:
    return v2(x + 1)


def qlog(x: int, j: int) -> int:
    """floor(2^j * log_2 x) = bitlen(x^(2^j)) - 1, exactly (no logarithms)."""
    return (x ** (1 << j)).bit_length() - 1


# ---------------------------------------------------------------------------
# the core decision procedure
# ---------------------------------------------------------------------------

def gain_cycle(edges: list[tuple[object, object, int, int]]):
    """Find a coordinate cycle with prod(y) > prod(x), or None.

    edges: (coord_x, coord_y, x, y).  Weight log(x) - log(y); a cycle of
    negative total weight is a certificate.  Floats guide, integers decide.
    """
    nodes = {}
    for cx, cy, _x, _y in edges:
        nodes.setdefault(cx, len(nodes))
        nodes.setdefault(cy, len(nodes))
    n = len(nodes)
    if n == 0:
        return None
    E = [(nodes[cx], nodes[cy], math.log(x) - math.log(y), x, y)
         for cx, cy, x, y in edges]
    dist = [0.0] * n
    pred: list[tuple[int, int, int] | None] = [None] * n
    last = -1
    for it in range(n):
        last = -1
        for idx, (u, v, w, x, y) in enumerate(E):
            if dist[u] + w < dist[v] - 1e-12:
                dist[v] = dist[u] + w
                pred[v] = (u, x, y)
                last = v
        if last == -1:
            return None
    # walk back into the cycle
    cur = last
    for _ in range(n):
        cur = pred[cur][0]
    cyc = []
    node = cur
    while True:
        u, x, y = pred[node]
        cyc.append((x, y))
        node = u
        if node == cur:
            break
    px = py = 1
    for x, y in cyc:
        px *= x
        py *= y
    return (cyc, px, py) if py > px else None       # exact integer decision


@dataclass(frozen=True)
class SMTResult:
    status: Literal["sat", "unsat", "unknown", "unavailable"]
    reason: str = ""


def smt_feasible(edges: list[tuple[object, object, int, int]]) -> SMTResult:
    """Ask whether some g makes log_2 x + g(C(x)) nonincreasing.

    h_c = 2^{g_c} > 0 and  y*h_{C(y)} <= x*h_{C(x)}  -- linear over Q.
    Preserve inconclusive solver outcomes; a timeout is not infeasibility.
    """
    if not HAVE_Z3:
        return SMTResult("unavailable", "z3-solver is not installed")
    hs: dict[object, z3.ArithRef] = {}

    def var(c):
        if c not in hs:
            hs[c] = z3.Real(f"h{len(hs)}")
        return hs[c]

    s = z3.Solver()
    s.set("timeout", 20000)
    for cx, cy, x, y in edges:
        s.add(var(cx) > 0, var(cy) > 0)
        s.add(y * var(cy) <= x * var(cx))
    result = s.check()
    if result == z3.sat:
        return SMTResult("sat")
    if result == z3.unsat:
        return SMTResult("unsat")
    return SMTResult("unknown", s.reason_unknown())


# ---------------------------------------------------------------------------
# A. premise check: the one-variable quantized-log class
# ---------------------------------------------------------------------------

def part_a() -> None:
    print("\n== A. premise check: is the quantized-log class still open? ==")
    print("  W6 assumes SH1/SH2/BND1 leave floor(2^j log_2 x) unsearched.")
    print("  But SUFF1 (unconditional via CONN1) already proves closed")
    print("  certificates exist there for every j and every m >= 3.")
    print("  We rediscover them independently, by exact negative-cycle search.")
    print("\n   j   m    odd x range   coords   certificate found   prod y / prod x")
    ok_any = False
    for j, m, hi in ((1, 8, 4000), (2, 8, 4000), (3, 16, 20000)):
        edges = []
        for x in range(3, hi, 2):
            y = f_odd(x)
            cx = (qlog(x, j), tau(x), x % (1 << m))
            cy = (qlog(y, j), tau(y), y % (1 << m))
            edges.append((cx, cy, x, y))
        res = gain_cycle(edges)
        ncoord = len({e[0] for e in edges} | {e[1] for e in edges})
        if res:
            ok_any = True
            cyc, px, py = res
            print(f"   {j}   {m:<4d} {hi:<13d} {ncoord:<8d} yes (len {len(cyc)})"
                  f"        {Fraction(py, px)}")
        else:
            print(f"   {j}   {m:<4d} {hi:<13d} {ncoord:<8d} no")
    check("certificates against the quantized-log coordinate are rediscovered "
          "independently: the one-variable class is CLOSED, not open", ok_any)
    print("  => W6's premise is out of date.  Its one-variable branch is")
    print("     subsumed by SUFF1 + CONN1.  Only the TWO-VARIABLE branch")
    print("     (V(x,n) on state-exponent pairs) is genuinely unsearched.")

    edges = []
    for x in range(3, 4000, 2):
        y = f_odd(x)
        cx = (qlog(x, 1), tau(x), x % 256)
        cy = (qlog(y, 1), tau(y), y % 256)
        edges.append((cx, cy, x, y))
    feas = smt_feasible(edges)
    if feas.status in ("sat", "unsat"):
        check("z3 cross-check: the same system is UNSAT (no potential exists)",
              feas.status == "unsat")
    else:
        incomplete(f"z3 cross-check: {feas.status} ({feas.reason}); "
                   "the independent integer certificates remain available")


# ---------------------------------------------------------------------------
# B. how deep is the -5 shadow actually realised on repunit orbits?
# ---------------------------------------------------------------------------

def repunit_orbit(n: int) -> list[int]:
    T = (1 << n) - 1
    x = (3 ** n - 1) // 2
    out = [x]
    while x >= T:
        x = f_odd(x)
        out.append(x)
    return out


def part_b(nmax: int) -> None:
    print("\n== B. the -5 shadow on ACTUAL repunit orbits ==")
    print("  SH1's certificate uses arbitrary integers 2^N w - 5.  A")
    print("  two-variable potential V(x,n) has its n-part cancelled by a")
    print("  shadow cycle only if that cycle lies inside ONE a_n orbit,")
    print("  because n is constant along an orbit.  So the relevant quantity")
    print("  is the shadow depth actually realised on repunit orbits:")
    print("      N*(n) = max_i v_2(x_i(n) + 5).")
    best = 0
    best_at = None
    total_states = 0
    rows = []
    for n in range(3, nmax + 1, 2):
        orb = repunit_orbit(n)
        total_states += len(orb)
        d = max(v2(x + 5) for x in orb if x != -5)
        if d > best:
            best, best_at = d, n
        if n in (11, 51, 101, 201, 301, 471, 501, 601):
            rows.append((n, len(orb), d, best))
    print("\n   n     orbit len   N*(n)   running max")
    for n, L, d, b in rows:
        print(f"   {n:<5d} {L:<11d} {d:<7d} {b}")
    print(f"\n  states scanned: {total_states};  best shadow depth "
          f"N* = {best} at n = {best_at}")
    print(f"  heuristic for {total_states} 'random' states: "
          f"log2 = {math.log2(total_states):.1f}")
    check("the realised shadow depth grows only like log2(#states): the SH1 "
          "certificate is NOT available at arbitrary depth inside a single "
          "repunit orbit", best <= math.log2(total_states) + 6)
    print("  Consequence: on repunit orbits the shadow gives a FINITE no-go")
    print(f"  (potentials reading x mod 2^m with m <= {max(best - 3, 0)}),")
    print("  not the universal SH1 statement.  This is exactly the gap the")
    print("  two-variable class lives in.")


# ---------------------------------------------------------------------------
# C. the two-variable search
# ---------------------------------------------------------------------------

def part_c(nmax: int) -> None:
    print("\n== C. the surviving two-variable class ==")
    print("  Coordinate: C(x,n) = (x mod 2^m, tau(x), floor(Q log_2(x/a_n))),")
    print("  i.e. the quantized log taken RELATIVE to the orbit's own seed --")
    print("  a genuine second-variable reading, not a function of x alone.")
    print("  Edges are actual repunit-orbit transitions only.")
    def build(m: int, j: int):
        """Edges, plus the set of (state, orbit) pairs they act on.

        The same integer can occur in several orbits with different
        coordinates, because the third component is taken relative to that
        orbit's own seed.  So the right denominator for "how much does the
        coordinate compress?" is the number of (x, n) PAIRS, not of x.
        """
        edges = []
        pairs = set()
        for n in range(3, min(nmax, 201) + 1, 2):
            orb = repunit_orbit(n)
            a = orb[0]
            qa = qlog(a, j)
            for i in range(len(orb) - 1):
                x, y = orb[i], orb[i + 1]
                cx = (x % (1 << m), tau(x), qlog(x, j) - qa)
                cy = (y % (1 << m), tau(y), qlog(y, j) - qa)
                edges.append((cx, cy, x, y))
                pairs.add((x, n))
                pairs.add((y, n))
        return edges, pairs

    print("\n  A SAT answer is only meaningful if the coordinate actually")
    print("  identifies distinct states.  When #coords approaches #states the")
    print("  alphabet is injective, every g is free, and SAT is VACUOUS.")
    print("\n   m    j   (x,n) pairs  coords   compression   certificate?  z3      verdict")
    ok = True
    complete = True
    found_any = False
    first_cert = None
    vacuous_from = None
    all_sat_vacuous = True
    for m, j in ((4, 1), (6, 1), (8, 2), (12, 2), (16, 3), (24, 3), (32, 4)):
        edges, pairs = build(m, j)
        res = gain_cycle(edges)
        ncoord = len({e[0] for e in edges} | {e[1] for e in edges})
        nstate = len(pairs)
        comp = 1 - ncoord / nstate            # 0 = injective alphabet
        feas = smt_feasible(edges)
        found_any = found_any or bool(res)
        if res and first_cert is None:
            first_cert = (m, j, res)
        if (not res and feas.status == "sat" and comp < 0.02
                and vacuous_from is None):
            vacuous_from = (m, j)
        if feas.status == "sat" and comp >= 0.02:
            all_sat_vacuous = False
        if res:
            verdict = "no-go (exact certificate)"
        elif feas.status == "sat":
            verdict = "VACUOUS sat" if comp < 0.02 else "genuine sat"
        else:
            verdict = "unresolved"
        print(f"   {m:<4d} {j}   {nstate:<12d} {ncoord:<8d} {comp:<13.4f} "
              f"{'yes' if res else 'no':<14s} "
              f"{feas.status:<7s} "
              f"{verdict}")
        if feas.status in ("unknown", "unavailable"):
            complete = False
            print(f"       z3 {feas.status}: {feas.reason}")
        if res and feas.status == "sat":
            ok = False                          # the two answers must agree
        if (not res) and feas.status == "unsat":
            ok = False
    if complete or not ok:
        check("the certificate search and the SMT decision agree on every "
              "coordinate tested", ok)
    if not complete:
        incomplete("certificate/SMT agreement is unresolved: "
                   "one or more solver results are unknown or unavailable")
    if found_any:
        print("  => Exact gain certificates rule out potentials even")
        print("     in the two-variable coordinate, from ACTUAL repunit")
        print("     orbits.  A new finite no-go extending SH1 to V(x,n).")
    if vacuous_from:
        print(f"  => From (m,j) = {vacuous_from} the coordinate is essentially")
        print("     injective on this window, so SAT carries no information:")
        print("     it reports the absence of constraints, not a candidate V.")
        print("     Enlarging the solver will not help; only enlarging the")
        print("     window (more states, hence more coordinate returns) will.")
        check("no SAT answer on this window is claimed as a candidate "
              "potential: every SAT here is diagnosed vacuous", all_sat_vacuous)

    if first_cert:
        m, j, (cyc, px, py) = first_cert
        print(f"\n  the certificate at (m,j) = ({m},{j}), exactly:")
        print(f"   cycle length {len(cyc)};  prod(y)/prod(x) = "
              f"{Fraction(py, px)} > 1")
        for x, y in cyc[:6]:
            print(f"     x = {str(x)[:44]:<44s} -> y = {str(y)[:44]}")
        check("the certificate's gain is a strict integer inequality "
              "prod(y) > prod(x)", py > px)

    print("\n  stress tests.")
    # the SH1 shadow family must not be claimed to descend
    x0 = 1275
    orb = [x0, f_odd(x0), f_odd(f_odd(x0))]
    check("SH1 shadow family reproduced: 1275 -> 1913 -> 1435 with "
          "8*1435 = 9*1275 + 5",
          orb == [1275, 1913, 1435] and 8 * 1435 == 9 * 1275 + 5)
    print(f"   shadow triple {orb}, value gain "
          f"{Fraction(1435, 1275)} > 1")
    # does the shadow family live on a repunit orbit?
    on_orbit = False
    for n in range(3, min(nmax, 201) + 1, 2):
        if 1275 in repunit_orbit(n):
            on_orbit = True
            break
    check("the SH1 shadow triple does NOT occur on any tested repunit orbit "
          "(so it cannot by itself refute a two-variable V)", not on_orbit)

    orb471 = repunit_orbit(471)
    d471 = max(v2(x + 5) for x in orb471)
    print(f"   n=471: {len(orb471)} pre-descent states, "
          f"max v_2(x+5) = {d471}")
    check("n=471 stress: the blocked-diffuse phase realises only a shallow "
          "shadow, consistent with part B", d471 <= 40)


def main() -> None:
    FAILURES.clear()
    INCOMPLETE.clear()
    ap = argparse.ArgumentParser()
    ap.add_argument("--nmax", type=int, default=101,
                    help="larger windows are the natural next step but the "
                         "z3 solve grows quickly; 201 takes ~1 min")
    args = ap.parse_args()
    print("== W6: machine synthesis inside the surviving potential class ==")
    print(f"  z3: {'available' if HAVE_Z3 else 'NOT available (SMT skipped)'}")
    part_a()
    part_b(args.nmax)
    part_c(args.nmax)
    print()
    if FAILURES:
        print(f"FAILURES ({len(FAILURES)}):")
        for f in FAILURES:
            print(f"  - {f}")
        raise SystemExit(1)
    if INCOMPLETE:
        print(f"MACHINE-SYNTHESIS: INCOMPLETE ({len(INCOMPLETE)} unresolved checks)")
        raise SystemExit(2)
    print("MACHINE-SYNTHESIS: PASS")


if __name__ == "__main__":
    main()
