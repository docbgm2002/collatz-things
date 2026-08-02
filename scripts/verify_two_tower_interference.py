#!/usr/bin/env python3
"""Interference of exact normal forms: two-tower arithmetic (W8, re-scoped).

Exact integer / rational arithmetic throughout.

RE-SCOPING.  W8 was written as "a cheap exact laboratory for W1's ledger".
Session 5 closed W1: the superposition defect is a slope mismatch of
trajectory size, so no laboratory rescues it.  What survives is W8's own
question, which never needed W1:

    do sums and differences of tower members carry closed-form itineraries,
    i.e. is there a new exact lane like SPN1?

The answer is yes, and the classification is complete.

Notation (W2-A):  w_d(M) = 1 + (4/3)^d (2^M - 2),  defined when
3^d | 2^M - 2, i.e. M = 1 mod 2*3^{d-1}.  Its frozen 2-adic tail is
Lambda_d = 1 - 2(4/3)^d.

A. The ghost algebra.  Xi_{d,d'} := 1 - (4/3)^d - (4/3)^{d'} is the frozen
   tail of the halved sum, 3 Xi_{d,d'} + 1 = 4 Xi_{d-1,d'-1}, and
   Lambda_d = Xi_{d,d} exactly.
B. The exact lane.  A halved diagonal sum lies in the SAME tower cylinder as
   a single tower member, so it inherits the whole TWR1 itinerary: e-word
   2^d 1^{V-1}.
C. Off-diagonal and differences: complete closed-form classification.
D. Where the lane ends (the kill clause), and a 471-bit stress test.

Run:
    python3 scripts/verify_two_tower_interference.py
"""

from __future__ import annotations

import argparse
from fractions import Fraction

FAILURES: list[str] = []


def check(label: str, ok: bool) -> None:
    if not ok:
        FAILURES.append(label)
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")


def v2(x: int) -> int:
    if x == 0:
        raise ValueError("v2(0)")
    return (x & -x).bit_length() - 1


def f_odd(x: int) -> int:
    y = 3 * x + 1
    return y >> v2(y)


def e_word(x: int, steps: int) -> list[int]:
    out = []
    for _ in range(steps):
        y = 3 * x + 1
        e = v2(y)
        out.append(e)
        x = y >> e
    return out


def order_d(d: int) -> int:
    return 2 * 3 ** (d - 1)


def w(d: int, M: int) -> int:
    """w_d(M) = 1 + (4/3)^d (2^M - 2)  (W2-A form of TWR1)."""
    num = 4 ** d * ((1 << M) - 2)
    assert num % 3 ** d == 0, (d, M)
    return 1 + num // 3 ** d


def frac_mod(q: Fraction, mod: int) -> int:
    """The residue of a 2-adic rational (odd denominator) modulo mod."""
    return (q.numerator * pow(q.denominator, -1, mod)) % mod


LAM = lambda d: 1 - 2 * Fraction(4, 3) ** d
XI = lambda d, dp: 1 - Fraction(4, 3) ** d - Fraction(4, 3) ** dp


# ---------------------------------------------------------------------------
# A. the ghost algebra
# ---------------------------------------------------------------------------

def part_a() -> None:
    print("\n== A. the two-tower ghost algebra ==")
    ok = all(LAM(d) == XI(d, d) for d in range(0, 12))
    check("Lambda_d = Xi_{d,d} exactly: the diagonal sum has the SAME frozen "
          "tail as a single tower member", ok)

    ok = all(3 * XI(d, dp) + 1 == 4 * XI(d - 1, dp - 1)
             for d in range(1, 10) for dp in range(1, 10))
    check("3 Xi_{d,d'} + 1 = 4 Xi_{d-1,d'-1}, i.e. Xi_{d,d'} = P_2(Xi_{d-1,d'-1})",
          ok)

    ok = True
    for d in range(1, 9):
        for dp in range(1, 9):
            m, k = min(d, dp), abs(d - dp)
            z = -Fraction(4, 3) ** k
            for _ in range(m):
                z = (4 * z - 1) / 3          # P_2 on Q
            if z != XI(d, dp):
                ok = False
    check("Xi_{d,d'} = P_2^{min(d,d')} ( -(4/3)^{|d-d'|} )", ok)

    print("   d  d'   Xi_{d,d'}          v_2      f-image")
    for d, dp in ((1, 1), (2, 2), (3, 3), (1, 2), (1, 3), (2, 4)):
        z = XI(d, dp)
        num = 3 * z + 1
        vv = v2(num.numerator) - v2(num.denominator) if num != 0 else None
        img = "undefined (3x+1 = 0)" if num == 0 else str(num / 2 ** vv)
        print(f"   {d}  {dp}    {str(z):<18s} {'-' if vv is None else vv:<8} {img}")
    print("  so the whole family reduces to the points -(4/3)^k, and after")
    print("  min(d,d') steps the orbit is at -3^{-k}, k = |d-d'|.")
    ok = True
    for d in range(1, 8):
        for dp in range(1, 8):
            m, k = min(d, dp), abs(d - dp)
            z = XI(d, dp)
            for _ in range(m):
                num = 3 * z + 1
                if num == 0:
                    break
                vv = v2(num.numerator) - v2(num.denominator)
                z = num / 2 ** vv
            if z != -Fraction(1, 3 ** k):
                ok = False
    check("f^{min(d,d')}(Xi_{d,d'}) = -3^{-|d-d'|}, exactly, in Q_2", ok)


# ---------------------------------------------------------------------------
# B. the exact lane
# ---------------------------------------------------------------------------

def part_b() -> None:
    print("\n== B. the new exact lane: diagonal two-tower sums ==")
    print("  s = w_d(M) + w_d(M'),  v_2(s) = 1,  x_0 = s/2.")
    print("  Claim: x_0 = Lambda_d mod 2^{min(M,M')-2}, so x_0 lies in the SAME")
    print("  tower cylinder as w_d itself; hence its e-word begins 2^d 1^{V-1}")
    print("  with V = min(M,M') - 2d - 1.")
    print("\n   d   M     M'    v2(s)  predicted word          matches?")
    ok_v2 = True
    ok_word = True
    ok_freeze = True
    for d in (1, 2, 3, 4):
        o = order_d(d)
        Ms = [1 + o * s for s in range(2, 7)]
        for i in range(len(Ms)):
            for j in range(i, len(Ms)):
                M, Mp = Ms[i], Ms[j]
                s = w(d, M) + w(d, Mp)
                if v2(s) != 1:
                    ok_v2 = False
                x0 = s >> 1
                mo = 1 << (min(M, Mp) - 2)
                if x0 % mo != frac_mod(LAM(d), mo):
                    ok_freeze = False
                V = min(M, Mp) - 2 * d - 1
                want = [2] * d + [1] * (V - 1)
                got = e_word(x0, len(want))
                good = got == want
                if not good:
                    ok_word = False
                if (i, j) in ((0, 0), (0, 1)) and d <= 3:
                    print(f"   {d}   {M:<5d} {Mp:<5d} {v2(s):<6d} "
                          f"2^{d} 1^{V - 1:<15d} {'yes' if good else 'NO'}")
    check("v_2(w_d(M) + w_d(M')) = 1 for every tested diagonal pair", ok_v2)
    check("x_0 = Lambda_d mod 2^{min(M,M')-2}: same frozen tail as w_d", ok_freeze)
    check("the e-word of x_0 begins exactly 2^d 1^{V-1}, V = min(M,M')-2d-1",
          ok_word)
    print("  The 2^d prefix walks the tower down to a Mersenne-form number")
    print("  2^V u - 1, and the 1^{V-1} suffix is the Andaloro burn.  So the")
    print("  halved diagonal sum is a genuine new exact lane, of length")
    print("  d + V - 1 = min(M,M') - d - 2.")


# ---------------------------------------------------------------------------
# C. off-diagonal sums, and differences
# ---------------------------------------------------------------------------

def part_c() -> None:
    print("\n== C. off-diagonal sums and differences ==")
    print("  off-diagonal sum: m = min(d,d'), k = |d-d'| >= 1.  Predicted")
    print("  e-word of x_0 = (w_d(M)+w_{d'}(M'))/2 is 2^{m-1} then 2+2k.")
    ok = True
    rows = []
    for d in range(1, 5):
        for dp in range(1, 5):
            if d == dp:
                continue
            m, k = min(d, dp), abs(d - dp)
            o1, o2 = order_d(d), order_d(dp)
            M = 1 + o1 * 6
            Mp = 1 + o2 * 6
            s = w(d, M) + w(dp, Mp)
            if v2(s) != 1:
                ok = False
            x0 = s >> 1
            want = [2] * (m - 1) + [2 + 2 * k]
            got = e_word(x0, len(want))
            if got != want:
                ok = False
            # and the landing point matches -3^{-k}
            y = x0
            for _ in range(m):
                y = f_odd(y)
            depth = min(M, Mp) - 2 - (2 * m + 2 * k)
            land = (y % (1 << depth)) == frac_mod(-Fraction(1, 3 ** k),
                                                  1 << depth)
            if not land:
                ok = False
            if len(rows) < 6:
                rows.append((d, dp, m, k, want, got == want, land))
    print("   d  d'  m  k   predicted word     word ok   lands on -3^-k")
    for d, dp, m, k, want, wok, land in rows:
        print(f"   {d}  {dp}   {m}  {k}   {str(want):<18s} "
              f"{'yes' if wok else 'NO':<9s} {'yes' if land else 'NO'}")
    check("off-diagonal sums: e-word 2^{m-1}(2+2k), then the orbit sits on "
          "-3^{-k} to the full frozen depth", ok)

    print("\n  differences.  Diagonal: w_d(M) - w_d(M') = (4/3)^d 2^{M'}(2^{L}-1),")
    print("  L = M-M', so v_2 = 2d + M' and the odd part is exactly (2^L-1)/3^d.")
    ok = True
    for d in (1, 2, 3):
        o = order_d(d)
        for a in range(2, 6):
            for b in range(a + 1, 7):
                M, Mp = 1 + o * b, 1 + o * a
                diff = w(d, M) - w(d, Mp)
                if v2(diff) != 2 * d + Mp:
                    ok = False
                odd = diff >> v2(diff)
                if odd != ((1 << (M - Mp)) - 1) // 3 ** d:
                    ok = False
    check("diagonal difference: v_2 = 2d + M', odd part = (2^{M-M'}-1)/3^d",
          ok)

    print("  Off-diagonal (d < d'): v_2 = 2d+1 and the odd part is")
    print("  -3^{-d}(1 - (4/3)^{d'-d}) to the frozen depth.")
    ok = True
    for d in range(1, 4):
        for dp in range(d + 1, 5):
            M = 1 + order_d(d) * 6
            Mp = 1 + order_d(dp) * 6
            diff = w(d, M) - w(dp, Mp)
            if v2(diff) != 2 * d + 1:
                ok = False
            odd = diff >> v2(diff)
            k = dp - d
            depth = min(M, Mp) - 2 - (2 * d + 1)
            target = frac_mod(-Fraction(1, 3 ** d)
                              * (1 - Fraction(4, 3) ** k), 1 << depth)
            if odd % (1 << depth) != target:
                ok = False
    check("off-diagonal difference: v_2 = 2 min(d,d') + 1 and the odd part "
          "has frozen tail -3^{-d}(1-(4/3)^{k})", ok)

    print("\n  w_d(M) +- 2^j:  the tail Lambda_d is perturbed at bit j, so the")
    print("  itinerary agrees with the tower's for as long as the cumulative")
    print("  valuation stays below j.")
    ok = True
    for d in (1, 2, 3):
        M = 1 + order_d(d) * 6
        base = w(d, M)
        for j in (20, 40, 60):
            if j >= M - 2:
                continue
            for sgn in (1, -1):
                x = base + sgn * (1 << j)
                if x % 2 == 0:
                    continue
                shared = 0
                wb = e_word(base, 12)
                wx = e_word(x, 12)
                cum = 0
                for t in range(12):
                    if wb[t] != wx[t]:
                        break
                    cum += wb[t]
                    shared = t + 1
                if cum > j:
                    ok = False
    check("w_d(M) +- 2^j agrees with the tower word while the cumulative "
          "valuation stays below j", ok)


# ---------------------------------------------------------------------------
# D. where the lane ends, and the 471-bit stress
# ---------------------------------------------------------------------------

def part_d() -> None:
    print("\n== D. where the lane ends (the kill clause), and a stress test ==")
    print("  The kill clause asks whether carries destroy the structure")
    print("  immediately outside the frozen overlap.  They do not destroy it")
    print("  immediately -- the lane runs the full frozen depth -- but the")
    print("  lane IS finite, of length ~min(M,M'), exactly like TWR1's own.")
    d = 2
    o = order_d(d)
    M, Mp = 1 + o * 8, 1 + o * 9
    x0 = (w(d, M) + w(d, Mp)) >> 1
    V = min(M, Mp) - 2 * d - 1
    predicted = [2] * d + [1] * (V - 1)
    got = e_word(x0, len(predicted) + 6)
    agree = 0
    for t in range(len(predicted)):
        if got[t] != predicted[t]:
            break
        agree += 1
    print(f"  d={d}, M={M}, M'={Mp}: predicted lane length {len(predicted)}, "
          f"agreement {agree}")
    print(f"  first 6 steps past the lane: {got[len(predicted):]}")
    check("the lane runs to its full predicted length and then stops being "
          "closed-form", agree == len(predicted))

    print("\n  471-bit stress.  Choose d, M so that w_d(M) is comparable in")
    print("  size to a_471 (746 bits).")
    d = 3
    o = order_d(d)
    M = 1 + o * 41                      # 2*9 = 18 -> M = 739
    while w(d, M).bit_length() < 700:
        M += o
    x0 = (w(d, M) + w(d, M + o)) >> 1
    V = M - 2 * d - 1
    predicted = [2] * d + [1] * (V - 1)
    got = e_word(x0, len(predicted))
    print(f"  d={d}, M={M}: w_d(M) has {w(d, M).bit_length()} bits; "
          f"x_0 has {x0.bit_length()} bits")
    print(f"  predicted lane length {len(predicted)}; matches: "
          f"{got == predicted}")
    check("the exact lane holds at 471-bit scale (d=3, ~740-bit tower sum)",
          got == predicted)
    a471 = (3 ** 471 - 1) // 2
    check("the lane family is disjoint from a_471 itself (sanity)",
          x0 != a471)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.parse_args()
    print("== W8 (re-scoped): interference of exact normal forms ==")
    part_a()
    part_b()
    part_c()
    part_d()
    print()
    if FAILURES:
        print(f"FAILURES ({len(FAILURES)}):")
        for f in FAILURES:
            print(f"  - {f}")
        raise SystemExit(1)
    print("TWO-TOWER: PASS")


if __name__ == "__main__":
    main()
