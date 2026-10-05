#!/usr/bin/env python3
"""Verifier for the manuscript section on residue-class certificates.

Checks, in exact integer / 2-adic arithmetic:

1. Ball lemma: for odd k, x1 = (3^(64k+18)-1)/8 lies in 9 + 64 Z_2, and
   k -> x1 mod 2^(j+5) is a bijection from odd k mod 2^j onto 9 + 64 Z
   mod 2^(j+5) (checked for j <= 12).
2. The shadow point: x1* = -47/9 is in 9 + 64 Z_2, its block scores are
   Delta_1 = -16 and Delta_j = -7 for j >= 2 (-5 -> -7 cycle), and the
   2-adic k* with 3^(64k*+20) = -367 maps to x1*.
3. Theorem (shadow classes): the class k = k* (mod 2^J) determines exactly
   B(J) = floor((J+2)/3) blocks, and all of Delta_2..Delta_B(J) equal -7
   (checked for 1 <= J <= --max-j).
4. The four early closure theorems are single class evaluations.
5. Optional (--measure): exact dyadic closure measures within 10 blocks
   at J = 14, 18 (and 22 with --measure-22).
"""

from __future__ import annotations

import argparse
import sys
from fractions import Fraction

sys.path.insert(0, "scripts")
from prove_block8_17_classes import NeedMoreBits, class_blocks  # noqa: E402


def v2(x: int) -> int:
    return (x & -x).bit_length() - 1


def x1_mod(k: int, p: int) -> int:
    return ((pow(3, 64 * k + 18, 1 << (p + 3)) - 1) % (1 << (p + 3))) >> 3


def check_ball() -> None:
    for j in range(1, 13):
        images = {x1_mod(k, j + 5) for k in range(1, 1 << j, 2)}
        target = {x for x in range(9, 1 << (j + 5), 64)}
        assert images == target, j
    print("ball lemma: PASS (odd k mod 2^j <-> 9 + 64Z mod 2^(j+5), j <= 12)")


def shadow_point(prec: int) -> tuple[int, int]:
    mod = 1 << prec
    xs = (-47 * pow(9, -1, mod)) % mod
    assert xs % 64 == 9
    # 3^(n*+3) = -367 with n* = 64k*+17: lift k* bit by bit.
    k = 0
    for j in range(prec - 9):
        for c in (k, k + (1 << j)):
            if (pow(3, 64 * c + 20, 1 << (j + 9)) + 367) % (1 << (j + 9)) == 0:
                k = c
                break
        else:
            raise AssertionError(f"lift failed at bit {j}")
    assert k & 1, "k* must be odd"
    assert x1_mod(k, prec - 9) == xs % (1 << (prec - 9))
    return xs, k


def check_shadow_blocks(xs: int, prec: int) -> None:
    x, p = xs, prec
    raw = (3 * x + 1) % (1 << p)
    assert v2(raw) == 2
    y = raw >> 2
    assert (y - (-11 * pow(3, -1, 1 << p))) % (1 << (p - 2)) == 0  # y1 = -11/3
    h1 = v2(y + 1)
    assert h1 == 3
    for _ in range(h1 - 1):
        y = (3 * y + 1) >> 1
    assert (y + 7) % (1 << (p - 10)) == 0  # x2 = -7
    print("shadow point: PASS (x1* = -47/9, y1 = -11/3, h1 = 3, x2 = -7; "
          "3^(64k*+20) = -367, k* odd)")


def check_shadow_classes(k_star: int, max_j: int) -> None:
    for J in range(1, max_j + 1):
        r = k_star % (1 << J)
        B = 1
        while True:
            try:
                h1, d = class_blocks(r, J, B + 1)
            except NeedMoreBits:
                break
            B += 1
            assert d[-1] == -7, (J, d)
        assert B == (J + 2) // 3, (J, B)
        if B >= 2:
            h1, d = class_blocks(r, J, B)
            assert h1 == 3 and all(x == -7 for x in d), (J, h1, d)
    print(f"shadow classes: PASS (B(J) = floor((J+2)/3), Delta_2..Delta_B = -7, "
          f"1 <= J <= {max_j})")


def check_early() -> None:
    rows = [(3, 8, (2, 13, 2)), (171, 8, (2, 2, 13)),
            (323, 9, (2, 13, 13)), (579, 10, (2, 13, 4))]
    for r, j, sig in rows:
        h1, d = class_blocks(r, j, 4)
        assert h1 == 3 and tuple(d) == sig and sum(d) >= 16, (r, d)
    print("early theorems: PASS (k = 3,171 mod 2^8; 323 mod 2^9; 579 mod 2^10; "
          "one class evaluation each)")


def closure_measure(blocks: int, J: int) -> tuple[Fraction, Fraction, Fraction]:
    closed = opened = undet = Fraction(0)
    stack = [(1, 1)]
    while stack:
        r, j = stack.pop()
        try:
            _, d = class_blocks(r, j, blocks, stop_at=16)
        except NeedMoreBits:
            if j >= J:
                undet += Fraction(1, 2 ** (j - 1))
            else:
                stack += [(r, j + 1), (r + (1 << j), j + 1)]
            continue
        w = Fraction(1, 2 ** (j - 1))
        if sum(d) >= 16:
            closed += w
        else:
            opened += w
    return closed, opened, undet


EXPECTED = {14: Fraction(1013, 2048), 18: Fraction(77177, 131072),
            22: Fraction(10687, 16384)}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--max-j", type=int, default=120)
    ap.add_argument("--measure", action="store_true")
    ap.add_argument("--measure-22", action="store_true")
    args = ap.parse_args()

    check_ball()
    prec = args.max_j + 64
    xs, k_star = shadow_point(prec)
    check_shadow_blocks(xs, prec)
    check_shadow_classes(k_star, args.max_j)
    check_early()
    if args.measure or args.measure_22:
        for J in ((14, 18, 22) if args.measure_22 else (14, 18)):
            c, o, u = closure_measure(10, J)
            assert c == EXPECTED[J] and c + o + u == 1, (J, c, o, u)
            print(f"closure measure J={J}: PASS (closed {c} = {float(c):.5f}, "
                  f"open {float(o):.6f}, undetermined {float(u):.5f})")
    print("ALL PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
