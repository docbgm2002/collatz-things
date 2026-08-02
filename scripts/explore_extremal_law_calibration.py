#!/usr/bin/env python3
"""Calibration of the extremal laws (W13).

NAVIGATION ONLY.  Nothing here eliminates a cylinder or proves a bound;
barrier 2 applies in full.  The purpose is to stop exact lemmas being
attempted with the wrong target exponent.

Two extremal statistics are calibrated.

A. Record deficit.  D_K = K log_2 3 - E_K is the log-height of the orbit's
   excursion above its start (x_K >= x_0 2^{D_K}).  Under the standard
   valuation model P(e = k) = 2^{-k} the increment is X = log_2 3 - e with
   E[X] = log_2(3/4) < 0, so max_K D_K is a NEGATIVE-DRIFT EXCURSION HEIGHT
   and the governing law is Cramer-Lundberg, not Bramson: P(max D > u) ~
   C 2^{-u}, because the Lundberg exponent solves E[e^{gamma X}] = 1 with
   the exact root gamma = log 2.  Hence over N sampled orbits the record is
   log_2 N + O(1) -- logarithmic in the SAMPLE SIZE, not in K.

B. Plateau records.  A plateau run of l blocks demands that sum(delta_j)
   prescribed bits match, at cost bar-delta = 5 + beta = 5.419... bits per
   block (W11).  So the first PCD-length-l plateau is expected near
   m_l = 2^{bar-delta (l-1)} and the running maximum is
   1 + log_2(m) / bar-delta -- Theta(log m) with an explicit constant.

Run:
    python3 scripts/explore_extremal_law_calibration.py
    python3 scripts/explore_extremal_law_calibration.py --nmax 5001
"""

from __future__ import annotations

import argparse
import math
from fractions import Fraction

THETA3 = math.log2(3)
BETA = 2 / math.log2(3 / 2) - 3          # Sturmian slope (W11)
BAR_DELTA = 5 + BETA                     # mean valuation per balanced block

NOTES: list[str] = []


def note(label: str, ok: bool) -> None:
    if not ok:
        NOTES.append(label)
    print(f"  [{'ok  ' if ok else 'MISS'}] {label}")


def v2(x: int) -> int:
    return (x & -x).bit_length() - 1


def f_odd(x: int) -> int:
    y = 3 * x + 1
    return y >> v2(y)


# ---------------------------------------------------------------------------
# A. the Lundberg exponent
# ---------------------------------------------------------------------------

def part_a_theory() -> None:
    print("\n== A1. the governing law for record deficits ==")
    print("  D_K = K log_2 3 - E_K,  increment X = log_2 3 - e,")
    print("  P(e = k) = 2^{-k} (k >= 1), so E[e] = 2 and")
    print(f"  E[X] = log_2 3 - 2 = {THETA3 - 2:.6f} < 0 : negative drift.")
    print("  Cramer-Lundberg: P(max_K D_K > u) ~ C exp(-gamma u) where")
    print("  E[e^{gamma X}] = 1.  With u = e^{-gamma} this is")
    print("      u^{1 - log_2 3} = 2 - u ,")
    print("  whose nontrivial root is u = 1/2 EXACTLY, i.e. gamma = log 2.")

    def lhs(u: float) -> float:
        return u ** (1 - THETA3)

    ok = abs(lhs(0.5) - (2 - 0.5)) < 1e-12
    note("u = 1/2 solves u^{1-log_2 3} = 2 - u exactly "
         f"(lhs {lhs(0.5):.12f}, rhs {1.5})", ok)
    # and it is the only root in (0,1)
    roots = [u / 1000 for u in range(1, 1000)
             if abs(lhs(u / 1000) - (2 - u / 1000)) < 2e-3]
    print(f"  numerical roots of the Lundberg equation in (0,1): "
          f"{sorted(set(round(r, 3) for r in roots))}")
    print("\n  => P(max_K D_K > u) is proportional to 2^{-u}.")
    print("     Over N sampled orbits the record deficit is log_2 N + O(1).")
    print("     This is a LOG-OF-SAMPLE-SIZE law.  It is NOT Bramson's")
    print("     -(3/2 theta) log K correction: that governs the leftmost")
    print("     particle of a branching random walk at depth K, whereas the")
    print("     record deficit is an excursion height over independent")
    print("     starting values.  W13's suggested law family is the wrong one.")
    print("\n  Self-consistency: the set of valuation words with D_K >= u has")
    print("  density 2^{-u} by the budget identity D_K + Q_K = K log_2(3/2),")
    print("  which is exactly the Lundberg tail.  The exponent gamma = log 2")
    print("  is therefore forced by the ledger, not fitted.")


# ---------------------------------------------------------------------------
# A2. the census
# ---------------------------------------------------------------------------

def peak_deficit(n: int) -> tuple[float, int, int]:
    """max_K D_K over the pre-descent a_n orbit, plus (K, E_K) attaining it.

    Comparisons are exact: D_K > D_J  iff  3^K 2^{E_J} > 3^J 2^{E_K}.
    """
    T = (1 << n) - 1
    x = (3 ** n - 1) // 2
    E = 0
    K = 0
    bestK, bestE = 0, 0
    while x >= T:
        e = v2(3 * x + 1)
        x = (3 * x + 1) >> e
        E += e
        K += 1
        # exact comparison of D_K against the running best
        if 3 ** K * (1 << bestE) > 3 ** bestK * (1 << E):
            bestK, bestE = K, E
    return bestK * THETA3 - bestE, bestK, bestE


def part_a_census(nmax: int) -> None:
    print("\n== A2. the tail of max_K D_K, measured ==")
    print("  The record-versus-log_2 N comparison is a single order statistic")
    print("  and far too noisy to test an exponent.  The tail itself is not:")
    print("  the prediction P(max D > u) ~ C 2^{-u} says the survival counts")
    print("  should HALVE for each extra unit of u.")
    vals = []
    best_n, best = 0, -1.0
    for n in range(3, nmax + 1, 2):
        d, _K, _E = peak_deficit(n)
        vals.append(d)
        if d > best:
            best, best_n = d, n
    N = len(vals)
    print(f"\n  samples {N};  max {best:.4f} at n = {best_n};  "
          f"median {sorted(vals)[N // 2]:.4f}")
    print("\n   u    #(max D > u)   log_2(fraction)   step slope   populated?")
    pts = []
    prev = None
    for u in range(0, 14):
        c = sum(1 for v in vals if v > u)
        if c < 3:
            break
        lg = math.log2(c / N)
        s = None if prev is None else lg - prev
        pop = c >= 20                     # only these carry a usable slope
        if pop:
            pts.append((u, lg))
        print(f"   {u:<4d} {c:<14d} {lg:<17.3f} "
              f"{'' if s is None else f'{s:+.3f}':<12s} "
              f"{'yes' if pop else 'thin'}")
        prev = lg
    # endpoint slope over the well-populated bins (counts >= 20)
    (u0, l0), (u1, l1) = pts[0], pts[-1]
    slope = (l1 - l0) / (u1 - u0)
    print(f"\n  slope over the populated range u = {u0}..{u1} "
          f"(counts >= 20): {slope:+.4f}")
    note(f"the measured tail slope is -1 to within 0.05 ({slope:+.4f}): the "
         "Lundberg exponent gamma = log 2 is confirmed, so "
         "P(max D > u) ~ 2^{-u}", abs(slope + 1) < 0.05)
    note(f"the record ({best:.3f}) sits within 2 bits of log_2 N "
         f"({math.log2(N):.3f}), as a 2^{{-u}} tail predicts",
         abs(best - math.log2(N)) < 2.0)
    print("\n  Implication for Avenue F / any rank function: the deficit a")
    print("  rank must tolerate grows like log_2 of the number of exponents")
    print("  considered, i.e. ~11 bits at n <= 5001 and ~21 bits at n <= 10^6.")
    print("  A rank designed for a CONSTANT deficit bound is under-specified;")
    print("  one designed for a linear-in-K bound is over-engineered.")


# ---------------------------------------------------------------------------
# B. plateau records
# ---------------------------------------------------------------------------

def part_b() -> None:
    print("\n== B. plateau records ==")
    print(f"  A PCD-length-l plateau needs (l-1) consecutive zero exponent")
    print(f"  lifts, i.e. sum(delta) = {BAR_DELTA:.4f}(l-1) prescribed bits.")
    print("  Under a uniform heuristic the first occurrence is near")
    print("      m_l = 2^{bar-delta (l-1)},")
    print("  and the running maximum through m is")
    print("      l_max(m) = 1 + log_2(m) / bar-delta .")
    print(f"  bar-delta = 5 + beta = {BAR_DELTA:.6f}  (beta = {BETA:.6f})")

    print("\n   PCD-length l   predicted first m   status")
    for l in range(2, 7):
        m = 2 ** (BAR_DELTA * (l - 1))
        if l == 2:
            st = "present early (PCD10: max 2 through m=300)"
        elif l == 3:
            st = "OBSERVED first at m = 1198 (PCD10)"
        elif l == 4:
            st = "prediction: not yet reached by any census"
        else:
            st = "prediction"
        print(f"   {l:<14d} {m:<19.4g} {st}")

    print("\n   census point            observed   predicted l_max")
    checks = [("PCD10, m <= 300", 300, 2),
              ("PCD10, m <= 1500", 1500, 3),
              ("W11 run, m <= 8000", 8000, 3)]
    ok = True
    for label, m, obs in checks:
        pred = 1 + math.log2(m) / BAR_DELTA
        agree = abs(pred - obs) < 1.0
        ok = ok and agree
        print(f"   {label:<23s} {obs:<10d} {pred:.3f}  "
              f"{'agrees' if agree else 'MISMATCH'}")
    note("the plateau law reproduces every certified census point to within "
         "one unit", ok)

    m3 = 2 ** (BAR_DELTA * 2)
    note(f"predicted first length-3 plateau {m3:.0f} is within a factor 2 of "
         "the observed 1198", 0.5 < m3 / 1198 < 2.0)

    print("\n  ANSWER to W13's stated question.  The honest target for plateau")
    print("  growth is Theta(log m) with the explicit constant 1/bar-delta =")
    print(f"  {1 / BAR_DELTA:.4f}, i.e.  l_max(m) ~ 1 + {1 / BAR_DELTA:.4f} log_2 m.")
    print("  It is NOT O(log m log log m), and it is far below the o(m) that")
    print("  PCD10 asks for: proving o(m) leaves a huge margin, while proving")
    print("  O(log m) would be essentially optimal.")
    print("\n  FALSIFIABLE FORWARD PREDICTIONS (for whoever extends the census):")
    print(f"   * first PCD-length-4 plateau near m = {2 ** (BAR_DELTA * 3):.3g}")
    print(f"   * first PCD-length-5 plateau near m = {2 ** (BAR_DELTA * 4):.3g}")
    print("   * no length-4 plateau below m ~ 2 x 10^4 (a factor-4 margin)")


def part_c(nmax: int) -> None:
    print("\n== C. the n = 471 anchor ==")
    d, K, E = peak_deficit(471)
    print(f"  n=471: peak deficit D_K = {d:.4f} at K = {K}, E_K = {E}")
    print(f"  predicted record over {(nmax - 1) // 2} samples: "
          f"{math.log2((nmax - 1) // 2):.3f}")
    note("n=471's peak deficit is within the predicted record band, so it is "
         "extremal-but-not-anomalous: the hard primitive is where the law "
         "says the record should sit, not an outlier needing its own theory",
         d <= math.log2((nmax - 1) // 2) + 3)
    print("  PCD2 places all six blocked-diffuse records on n=471 at")
    print("  K = 31,33,34,35,37,38 -- consistent with a single deep excursion")
    print("  rather than a distinct mechanism.")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--nmax", type=int, default=2001)
    args = ap.parse_args()
    print("== W13: calibration of the extremal laws (navigation only) ==")
    part_a_theory()
    part_a_census(args.nmax)
    part_b()
    part_c(args.nmax)
    print()
    if NOTES:
        print(f"CALIBRATION MISMATCHES ({len(NOTES)}):")
        for f in NOTES:
            print(f"  - {f}")
        raise SystemExit(1)
    print("EXTREMAL-CALIBRATION: consistent")


if __name__ == "__main__":
    main()
