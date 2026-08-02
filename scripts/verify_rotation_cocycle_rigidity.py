#!/usr/bin/env python3
"""Rotation-cocycle rigidity for the balanced plateau problem (W11).

Exact integer arithmetic; floats appear only in printing and in the
continued fraction of the (irrational) Sturmian slope.

W11 proposed to realise the PCD13 plateau condition t_m = kappa_m as a
cocycle over the Sturmian rotation with values in the compact group Z_2, so
that Furstenberg's unique-ergodicity criterion would give an EVERY-ORBIT
equidistribution statement and thereby evade barrier 2.  This script tests
the three sub-deliverables and finds the dictionary does not exist.

A. The fibre map is 2-adically EXPANDING.  PCD15's displacement identity
   F(y+2^M,t) - F(y,t) = 3^{|v|} 2^{M-delta} says the endpoint recursion
   multiplies 2-adic distance by exactly 2^{delta_m}.  Compact-group
   extensions are fibrewise isometric, so no skew product -- and no finite
   tower of them -- can be conjugate to this system.  The 2-adic Lyapunov
   exponent is computed and shown to converge to 5 + beta.

B. The plateau carry is the 2-adic digit shift of 3^n.  PCD14's
   C' = (C-t)/2^delta with t = C mod 2^delta is exactly C' = floor(C/2^delta),
   and C = floor(3^n / 2^{E+2}).  So a plateau run is an agreement between
   the affine lift word and a window of the BINARY DIGITS OF 3^n.

C. The Furstenberg character test cannot be posed: the IEF starting-cylinder
   lift digit is not a
   function of any finite window of the Sturmian word, so there is no
   phi on the circle to test.

D. Denjoy-Koksma at the Ostrowski scales Q_k of beta.  Positive control:
   the gap word IS bounded-variation over the rotation and its cocycle sums
   are bounded by the variation, as DK predicts.  Negative test: the lift
   and plateau streams are not.

Run:
    python3 scripts/verify_rotation_cocycle_rigidity.py
    python3 scripts/verify_rotation_cocycle_rigidity.py --blocks 8000
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import log2

from explore_balanced_q3_zero_cylinders import (
    BLOCK_DATA,
    analyse,
    mechanical_blocks,
)

FAILURES: list[str] = []


def check(label: str, ok: bool) -> None:
    if not ok:
        FAILURES.append(label)
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")


BETA = 2 / log2(3 / 2) - 3          # Sturmian slope of the 4-block indicator
MEAN_DELTA = 5 + BETA               # mean total valuation per block


# ---------------------------------------------------------------------------
# A. the fibre map is 2-adically expanding
# ---------------------------------------------------------------------------

def endpoint_step(y: int, t: int, block_steps: int) -> Fraction:
    """F_v(y,t) = (3^{|v|}(y + 2 t 3^K) + c(v)) / 2^delta, PCD15.

    K is the odd-step count already consumed; the displacement identity below
    does not depend on it, so we take K = 0 for the comparison.
    """
    delta, correction, _req = BLOCK_DATA[block_steps]
    return Fraction(3 ** block_steps * (y + 2 * t) + correction, 1 << delta)


def part_a(blocks: int) -> None:
    print("\n== A. the fibre map is 2-adically expanding ==")

    # PCD15 displacement identity, exactly
    ok = True
    for block_steps in (3, 4):
        delta = BLOCK_DATA[block_steps][0]
        for M in range(delta + 1, delta + 12):
            for y in (0, 7, 1234567, 2 ** 40 + 3):
                for t in (0, 1, 5):
                    d = endpoint_step(y + (1 << M), t, block_steps) \
                        - endpoint_step(y, t, block_steps)
                    if d != Fraction(3 ** block_steps * (1 << (M - delta))):
                        ok = False
    check("PCD15: F(y+2^M,t) - F(y,t) = 3^{|v|} 2^{M-delta}, exactly", ok)
    print("  so |F(y1)-F(y2)|_2 = 2^delta |y1-y2|_2 : the fibre map multiplies")
    print("  2-adic distance by exactly 2^delta.  A compact-group skew product")
    print("  (x,y) -> (x+alpha, y+phi(x)) is fibrewise an ISOMETRY (factor 1).")

    plan = mechanical_blocks(blocks)
    deltas = [BLOCK_DATA[b][0] for b in plan]
    print("\n  2-adic Lyapunov exponent (per block), in units of log 2:")
    print("   m        (1/m) sum delta_j     5 + beta        difference")
    running = 0
    rows = []
    for m, d in enumerate(deltas, 1):
        running += d
        if m in (10, 100, 1000, 2000, 4000, len(deltas)):
            rows.append((m, running / m))
            print(f"   {m:<8d} {running / m:<20.8f} {MEAN_DELTA:<15.8f}"
                  f" {running / m - MEAN_DELTA:+.2e}")
    check("the mean valuation per block converges to 5 + beta = "
          f"{MEAN_DELTA:.6f}", abs(rows[-1][1] - MEAN_DELTA) < 1e-3)
    check("the 2-adic Lyapunov exponent is strictly positive, so the system"
          " is not fibrewise isometric", rows[-1][1] > 5)
    print("  A finite tower of compact-group extensions over a rotation is")
    print("  fibrewise isometric at every level, hence has Lyapunov exponent 0.")
    print("  => no finite tower is conjugate to this system.  W11(i) KILL.")


# ---------------------------------------------------------------------------
# B. the plateau carry is the digit shift of 3^n
# ---------------------------------------------------------------------------

def part_b() -> None:
    print("\n== B. the plateau carry is the 2-adic digit shift of 3^n ==")
    print("  PCD13/PCD14 set C = (3^n - (2r+1)) / 2^{E+2} with")
    print("  3^n = 2r+1 mod 2^{E+2} and 0 <= 2r+1 < 2^{E+2}.  Hence")
    print("      C = floor( 3^n / 2^{E+2} ) :  C is the HIGH PART of 3^n.")

    ok = True
    examples = []
    for E in (6, 10, 14, 20, 26):
        mod = 1 << (E + 2)
        # pick an exponent n and read off the cylinder it lands in
        for n in (5, 17, 43, 111, 471):
            val = pow(3, n)
            low = val % mod
            r = (low - 1) // 2
            if (2 * r + 1) != low:
                ok = False
            C = (val - low) // mod
            if C != val >> (E + 2):
                ok = False
            if E == 14 and n in (43, 471):
                examples.append((E, n, C.bit_length(), bin(C % 256)[2:].zfill(8)))
    check("C = floor(3^n / 2^{E+2}) for every tested (E, n)", ok)
    for E, n, bits, low8 in examples:
        print(f"   E={E:<3d} n={n:<4d} C has {bits} bits, low 8 bits of C = {low8}")

    # PCD14 on a plateau: t = C mod 2^delta and C' = (C-t)/2^delta
    ok = True
    for delta in (5, 6):
        for C in (0, 1, 12345678901234567890, pow(3, 471) >> 16):
            t = C % (1 << delta)
            if (C - t) // (1 << delta) != C >> delta:
                ok = False
    check("PCD14 on a plateau: C' = (C-t)/2^delta = floor(C/2^delta), "
          "i.e. the 2-adic digit shift", ok)
    print("  So a plateau run of blocks delta_1..delta_l is EXACTLY the event")
    print("      (low delta_1+..+delta_l bits of 3^n)  =  t_1|t_2|..|t_l ,")
    print("  an agreement between the affine lift word and a window of the")
    print("  binary digits of 3^n.  That is W10's object with height c = 1.")
    print("  It is also the portfolio's set-aside item 'normality / Fourier")
    print("  results on digits of 3^n', which W11 was supposed to avoid.")


# ---------------------------------------------------------------------------
# C. the Furstenberg character test cannot be posed
# ---------------------------------------------------------------------------

def part_c(rows: list[dict]) -> None:
    print("\n== C. there is no phi: the lift is not a window function ==")
    print("  Furstenberg's criterion applies to (x,y) -> (x+alpha, y+phi(x))")
    print("  with phi a measurable function ON THE CIRCLE.  For the test to be")
    print("  posable, t_m would have to be a function of the rotation phase,")
    print("  i.e. determined by the Sturmian word around position m.  The stream\n  tested is analyse()'s starting-cylinder lift digit, which is PCD13's t.")
    word = [r["block_steps"] for r in rows]
    lifts = [r["lift_digit"] for r in rows]
    print("\n   window radius W   distinct windows   Sturmian p(2W+1)   ambiguous")
    ok = True
    sturmian = True
    for W in (1, 2, 4, 8, 16, 32, 64, 128):
        buckets: dict[tuple, set] = {}
        for m in range(W, len(word) - W):
            key = tuple(word[m - W:m + W + 1])
            buckets.setdefault(key, set()).add(lifts[m])
        ambiguous = sum(1 for v in buckets.values() if len(v) > 1)
        expected = 2 * W + 2                     # p(L) = L+1 for a Sturmian word
        print(f"   {W:<17d} {len(buckets):<18d} {expected:<18d} "
              f"{ambiguous} of {len(buckets)}")
        if ambiguous != len(buckets):
            ok = False
        if len(buckets) != expected:
            sturmian = False
    check("the block word has Sturmian factor complexity p(L) = L+1 "
          "(built-in consistency check on the driver)", sturmian)
    check("EVERY factor, at every tested length, carries more than one lift "
          "value: t_m is not a function of the Sturmian phase at any "
          "finite resolution", ok)
    print("  This is the computational face of PCD15 (no fixed-width endpoint")
    print("  state is closed).  With no phi there is no fibre character to")
    print("  test, so the Furstenberg criterion is not merely hard here --")
    print("  it is inapplicable.  W11(ii) is vacuous.")


# ---------------------------------------------------------------------------
# D. Denjoy-Koksma at the Ostrowski scales
# ---------------------------------------------------------------------------

def cf_denominators(x: float, limit: int) -> list[int]:
    """Convergent denominators of x up to limit (numerical; beta is irrational)."""
    p_prev, p = 0, 1
    q_prev, q = 1, 0
    out = []
    for _ in range(64):
        a = int(x // 1)
        p_prev, p = p, a * p + p_prev
        q_prev, q = q, a * q + q_prev
        if q > limit:
            break
        if q > 0:
            out.append(q)
        rem = x - a
        if rem <= 0:
            break
        x = 1 / rem
    return sorted(set(out))


def part_d(rows: list[dict]) -> None:
    print("\n== D. Denjoy-Koksma at the Ostrowski scales of beta ==")
    n = len(rows)
    qs = [q for q in cf_denominators(BETA, n) if q >= 2]
    print(f"  beta = {BETA:.12f};  convergent denominators <= {n}: {qs}")

    # --- positive control: the gap word is BV over the rotation ---
    word = [r["block_steps"] for r in rows]
    deltas = [BLOCK_DATA[b][0] for b in word]
    print("\n  positive control -- gap word.  delta_m = 5 + 1[4-block] is the")
    print("  indicator of an interval, so Var = 2 and DK predicts")
    print("      | sum_{m<Q} (delta_m - (5+beta)) |  <=  2   at every Q = Q_k.")
    print("   Q_k       cocycle sum      |sum| <= 2 ?")
    ok = True
    for q in qs:
        s = sum(deltas[:q]) - q * MEAN_DELTA
        good = abs(s) <= 2 + 1e-9
        print(f"   {q:<9d} {s:+.6f}        {'yes' if good else 'NO'}")
        if not good:
            ok = False
    check("Denjoy-Koksma holds for the gap word at every Ostrowski scale",
          ok)

    # --- negative test: the lift stream is not BV over the rotation ---
    lifts = [r["lift_digit"] for r in rows]
    norm = [lifts[m] / (1 << deltas[m]) for m in range(n)]
    mean_norm = sum(norm) / n
    print(f"\n  negative test -- normalised lift t_m / 2^delta_m,"
          f" empirical mean {mean_norm:.6f}")
    print("   Q_k       cocycle sum      growth vs sqrt(Q)")
    sums = []
    for q in qs:
        s = sum(norm[:q]) - q * mean_norm
        sums.append(abs(s))
        print(f"   {q:<9d} {s:+.6f}        {abs(s) / max(q, 1) ** 0.5:.4f}")
    check("the lift cocycle sums exceed the gap-word variation bound, so the "
          "lift is not BV-over-the-rotation with the driver's variation",
          max(sums) > 2)
    print("  (Decisively: part C shows the lift is not a function of the phase")
    print("   at all, so there is no variation to bound these sums with.  The")
    print("   DK experiment localises the obstruction rather than testing it:")
    print("   the gap word is the BV part, the carry is not.)")

    # --- the IEF stabilisation indicator (NOT the PCD plateau indicator) ---
    #
    # CAUTION.  analyse() returns the IEF *starting-cylinder* lift digit z_H
    # of u_H (IEF7's stream: "an ordinary positive integer can realize the
    # infinite word only if these lift digits are eventually zero").  PCD's
    # cylinder plateau is a zero *exponent* lift, i.e. n_{m+1} = n_m, which
    # by PCD13 is the condition t = kappa and needs the exponent-side carry
    # kappa (the digits of 3^n).  The two streams are different -- they are
    # the digit streams of two different 2-adic ghosts, related by the 2-adic
    # discrete logarithm.  We therefore report this one under its own name
    # and do NOT compare its histogram with PCD12's.
    zero_lift = [1 if x == 0 else 0 for x in lifts]
    rate = sum(zero_lift) / n
    print(f"\n  IEF starting-cylinder stabilisation indicator 1[z_H = 0],")
    print(f"  empirical rate {rate:.6f}  (uniform heuristic "
          f"{((1 - BETA) / 32 + BETA / 64):.6f})")
    print("   Q_k       zero lifts   expected      deviation")
    for q in qs:
        obs = sum(zero_lift[:q])
        exp = q * rate
        print(f"   {q:<9d} {obs:<12d} {exp:<13.3f} {obs - exp:+.3f}")
    runs = []
    cur = 0
    for p in zero_lift:
        if p:
            cur += 1
        else:
            if cur:
                runs.append(cur)
            cur = 0
    if cur:
        runs.append(cur)
    hist: dict[int, int] = {}
    for r in runs:
        hist[r] = hist.get(r, 0) + 1
    print(f"  zero-lift run histogram: {dict(sorted(hist.items()))}")
    print("  (This is IEF7's stream.  It is NOT PCD's cylinder-plateau")
    print("   stream, whose histogram PCD12 reports as {1:1423, 2:37, 3:1}")
    print("   through m=1500; that one needs the exponent-side carry kappa.)")
    check("the IEF stabilisation runs stay short on the tested range -- "
          "finite evidence only, NOT a theorem: this is exactly barrier 2",
          max(runs, default=0) <= 4)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--blocks", type=int, default=8000)
    args = ap.parse_args()
    print("== W11: rotation-cocycle rigidity for the plateau problem ==")
    rows = analyse(args.blocks)
    part_a(args.blocks)
    part_b()
    part_c(rows)
    part_d(rows)
    print()
    if FAILURES:
        print(f"FAILURES ({len(FAILURES)}):")
        for f in FAILURES:
            print(f"  - {f}")
        raise SystemExit(1)
    print("ROTATION-COCYCLE: PASS")


if __name__ == "__main__":
    main()
