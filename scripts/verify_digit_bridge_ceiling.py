#!/usr/bin/env python3
"""Digit arithmetic of powers of three: the reset-count bridge (W10).

Exact integer arithmetic; floats only in printing and in the Stewart
size comparison, where the quantities differ by astronomical factors.

A. W10(a) -- the elementary ceiling, consolidated and made exact.
   For a fixed odd target A, matching 3^n against A to 2-adic depth W is
   governed by a single ghost alpha_A in Z_2 with 3^{alpha_A} = A:

       v_2(3^n - A) = 1                    if n and alpha_A differ in parity
                    = 2 + v_2(n - alpha_A) otherwise,

   and the least n reaching depth W is exactly alpha_A mod 2^{W-2}.
   This generalises the BAKER1-3 identity of the W9 audit (A = -7) and is
   the exact form of "matching to depth v forces R into a progression
   mod 2^{v-2}".

B. W10(b) -- the bridge on the plateau branch.  PCD13/PCD14 give
   C = floor(3^{n_m} / 2^{E_m+2}), so the plateau stream IS a window of the
   binary digits of a power of three with height c = 1.  The bridge exists.

C. W10(c) -- Stewart, and why it is vacuous here.  Stewart (1980) bounds the
   TOTAL number of nonzero binary digits of 3^R from below.  PCD10 forces
   bitlen(n_m) >= E_m - 6*plateau + 1, so the expansion of 3^{n_m} is
   2^{Theta(E_m)} digits long while the plateau window has width O(E_m).
   The guaranteed nonzero digits are too few, and too undistributed, to say
   anything about that window.  Worse, the bound degrades exactly when the
   plateau is long -- the input is anti-correlated with the event.

Run:
    python3 scripts/verify_digit_bridge_ceiling.py
"""

from __future__ import annotations

import argparse
import math

FAILURES: list[str] = []


def check(label: str, ok: bool) -> None:
    if not ok:
        FAILURES.append(label)
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")


def v2(x: int) -> int:
    if x == 0:
        raise ValueError("v2(0)")
    return (x & -x).bit_length() - 1


# ---------------------------------------------------------------------------
# A. the ghost of an odd target, and the elementary ceiling
# ---------------------------------------------------------------------------

def ghost(A: int, depth: int) -> int | None:
    """The unique alpha in Z_2 with 3^alpha = A, returned mod 2^depth.

    Exists iff A = 1 or 3 (mod 8): the closure of <3> in Z_2^* is exactly
    {x : x = 1, 3 mod 8}, of index 2.
    """
    if A % 8 not in (1, 3):
        return None
    a = 0
    for j in range(depth):
        modulus = 1 << (j + 3)
        if pow(3, a, modulus) != A % modulus:
            a += 1 << j
        if pow(3, a, modulus) != A % modulus:
            return None
    return a % (1 << depth)


def part_a(depth: int) -> None:
    print("\n== A. W10(a): the elementary ceiling, exactly ==")
    print("  <3> is closed of index 2 in Z_2^*, with image {x = 1,3 mod 8}.")
    print("  For such a target A there is a unique ghost alpha_A in Z_2 with")
    print("  3^{alpha_A} = A, and matching depth is read off from it.")

    targets = [1, 3, 9, 11, 17, 19, 25, 27, 41, 43, 57, 59, -7 % (1 << 40),
               2 * 121 + 1, 2 * 1093 + 1]
    ok_id = True
    ok_least = True
    rows = []
    for A in targets:
        A %= 1 << depth
        if A % 8 not in (1, 3):
            continue
        al = ghost(A, depth)
        assert al is not None
        par = al & 1
        for n in range(0, 600):
            lhs = v2(3 ** n - A) if 3 ** n != A else depth
            d = (n - al) % (1 << depth)
            rhs = 1 if (n & 1) != par else 2 + (v2(d) if d else depth)
            if min(lhs, depth) != min(rhs, depth):
                ok_id = False
                print(f"    identity fails at A={A}, n={n}: {lhs} vs {rhs}")
                break
        # least representative at depth W is alpha mod 2^{W-2}
        for W in range(4, 22):
            m0 = al % (1 << (W - 2))
            if pow(3, m0, 1 << W) != A % (1 << W):
                ok_least = False
            if any(pow(3, m, 1 << W) == A % (1 << W) for m in range(m0)):
                ok_least = False
        rows.append((A % 256, al % (1 << 20), al & 1))
    check("v_2(3^n - A) = 1 on a parity mismatch, else 2 + v_2(n - alpha_A)",
          ok_id)
    check("the least n matching A to depth W is exactly alpha_A mod 2^{W-2}",
          ok_least)
    print("   A mod 256   alpha_A mod 2^20   parity of alpha_A")
    for a8, a20, par in rows[:8]:
        print(f"   {a8:<11d} {a20:<18d} {par}")

    print("\n  Consequence (the ceiling).  If 3^n matches a fixed target to")
    print("  depth W then n >= alpha_A mod 2^{W-2}, so W <= 2 + log_2 n unless")
    print("  the ghost has an anomalously long run of zero digits.  This is")
    print("  the W9 BAKER1-3 statement with A = -7, verbatim, for general A.")
    a7 = ghost((-7) % (1 << depth), depth)
    check("specialising to A = -7 reproduces the W9 ghost "
          "(alpha = 1198 mod 2^16)", a7 is not None and a7 % (1 << 16) == 1198)


# ---------------------------------------------------------------------------
# C. Stewart, and the size gap
# ---------------------------------------------------------------------------
#
# Stewart, "On the representation of an integer in two different bases",
# J. reine angew. Math. 319 (1980), 63-72: for n > 25 and multiplicatively
# independent bases a, b,
#
#     s_a(n) + s_b(n) > log log n / (log log log n + C(a,b)) - 1,
#
# effectively.  With n = 3^R, s_3 = 1, log log n = log(R log 3), so
#
#     s_2(3^R) > log R / (log log R + C) - 2 .
#
# We take C = 0, i.e. we OVERSTATE Stewart's guarantee, so the vacuity
# conclusion below is conservative.

def stewart_from_log2R(log2R: float) -> float:
    """Stewart's guaranteed count for 3^R, given log_2 R (avoids huge ints).

    s_2(3^R) > log R / (log log R + C) - 2; we take C = 0, i.e. we OVERSTATE
    the guarantee, so the vacuity conclusion below is conservative.
    """
    logR = log2R * math.log(2)
    if logR < 3:
        return 0.0
    return logR / math.log(logR) - 2


def part_c() -> None:
    print("\n== C. W10(c): Stewart applies, and is vacuous by 2^Theta(E) ==")
    print("  Bridge (W11-C / PCD13-14): the plateau stream is a window of the")
    print("  binary digits of 3^{n_m}, height c = 1 -- the best possible case,")
    print("  so W10's stated kill ('unbounded height c') does NOT fire.")
    print("  The kill comes from the EXPONENT instead.")
    print()
    print("  PCD10: bitlen(n_m) >= E_m - 6*plateau + 1.  So the expansion of")
    print("  3^{n_m} has ~1.585 * 2^{bitlen} binary digits, while the plateau")
    print("  window has width only sum(delta) = O(E_m).")
    print()
    print("   E_m    plateau   bitlen(n_m)>=   digits of 3^{n_m}   Stewart >=   "
          "expected in window")
    ok = True
    for E in (100, 500, 1000, 5000):
        for plateau in (3, 10):
            bl = E - 6 * plateau + 1
            if bl < 40:
                continue
            # n_m >= 2^{bl-1}; 3^{n_m} has ~ n_m * log2 3 binary digits
            log2_digits = (bl - 1) + math.log2(math.log2(3))
            st = stewart_from_log2R(bl - 1)
            window = 6 * plateau
            # expected Stewart digits inside a window of that width, if the
            # guaranteed nonzero digits were spread uniformly
            log10_expected = (math.log10(window) + math.log10(max(st, 1e-300))
                              - log2_digits * math.log10(2))
            print(f"   {E:<6d} {plateau:<9d} {bl:<15d} 2^{log2_digits:<17.1f}"
                  f" {st:<12.1f} 1e{log10_expected:.0f}")
            if log10_expected > -6:
                ok = False
    check("the Stewart-guaranteed nonzero digits expected inside the plateau "
          "window is astronomically below 1 in every live regime", ok)

    print("\n  Worse: the bound is ANTI-correlated with the event it must")
    print("  exclude.  A longer plateau makes bitlen(n_m) SMALLER (PCD10), so")
    print("  Stewart's guarantee gets WEAKER exactly when it is needed.")
    print("   plateau l   bitlen(n_m) >= E-6l+1 at E=1000   Stewart >=")
    prev = None
    mono = True
    for l in (1, 3, 10, 30, 100, 160):
        bl = 1000 - 6 * l + 1
        st = stewart_from_log2R(max(bl - 1, 1))
        print(f"   {l:<11d} {bl:<32d} {st:.1f}")
        if prev is not None and st > prev:
            mono = False
        prev = st
    check("Stewart's guarantee is non-increasing in the plateau length",
          mono)
    print("\n  Stewart becomes non-vacuous only when 6l ~ E_m, i.e. only when")
    print("  the plateau is already linear in m -- precisely the case the")
    print("  target 'plateau = o(m)' assumes away.  W10(c) KILL.")


def part_b() -> None:
    print("\n== B. W10(b): the bridge exists, at height c = 1 ==")
    print("  PCD13: C = (3^n - (2r+1))/2^{E+2} with 0 <= 2r+1 < 2^{E+2},")
    print("  hence C = floor(3^n / 2^{E+2}).")
    ok = True
    for E in (8, 16, 32, 64):
        for n in (11, 43, 111, 471, 1197):
            val = pow(3, n)
            if (val - val % (1 << (E + 2))) // (1 << (E + 2)) != val >> (E + 2):
                ok = False
    check("C = floor(3^n / 2^{E+2}) exactly (the bridge, height c = 1)", ok)
    print("  So W10's own kill criterion -- 'kill if the bridge provably")
    print("  requires unbounded-height c on every branch class' -- does not")
    print("  fire.  The height is 1.  The obstruction is elsewhere; see C.")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--depth", type=int, default=64)
    args = ap.parse_args()
    print("== W10: digit arithmetic of powers of three ==")
    part_a(args.depth)
    part_b()
    part_c()
    print()
    if FAILURES:
        print(f"FAILURES ({len(FAILURES)}):")
        for f in FAILURES:
            print(f"  - {f}")
        raise SystemExit(1)
    print("DIGIT-BRIDGE: PASS")


if __name__ == "__main__":
    main()
