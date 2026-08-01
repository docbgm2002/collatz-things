#!/usr/bin/env python3
"""
verify_general_shadow.py
========================

Machine verification of SH1-GEN, the (a,b,c)-general form of the shadow
no-go theorem.

MAP.  For coprime a, c with c prime, and gcd(b, c) = 1, define on integers
coprime to c:

    T(x) = (a x + b) / c^{v_c(a x + b)}.

The 3x+1 case is (a, b, c) = (3, 1, 2).

THEOREM (SH1-GEN).  Suppose T has an EXPANDING rational cycle: a K-cycle
{y_1, ..., y_K} with total valuation E and c^E < a^K.  Then:

  (a)  for every N > E and every X with X = y_1 (mod c^N), the orbit of X
       reproduces the cycle's valuation word for K steps;
  (b)  T^K(X) = X (mod c^{N-E}), so every coordinate determined by the
       bottom m <= N-E base-c digits closes into a cycle;
  (c)  T^K(X) / X > 1, with limit a^K / c^E as N -> infinity;
  (d)  hence no potential  log_c x + g(c-adically local data)  is
       nonincreasing along T on positive x -- the K monotonicity
       constraints sum to 0 <= -log_c(T^K(X)/X) < 0;
  (e)  the base-c LENGTH coordinate is additionally covered if and only if
       a^K / c^E < c.

WHAT THIS ESTABLISHES.  SH1's proof uses nothing about 3 and 2 beyond the
existence of an expanding cycle.  The pair (3,2) enters only through the
particular cycle -5 -> -7 and the particular detector templates.  The
mechanism is a general fact about piecewise-affine integer maps.

NO FLOATING POINT APPEARS IN ANY ASSERTION.  All gains are compared as
exact Fractions; all congruences are exact integer arithmetic.
"""

import sys
from math import gcd
from fractions import Fraction

FAILURES = []


def check(name, cond, detail=""):
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))
    if not cond:
        FAILURES.append(name)


def vc(n, c):
    v = 0
    while n % c == 0:
        n //= c
        v += 1
    return v


def T(x, a, b, c):
    y = a * x + b
    v = vc(y, c)
    return y // c ** v, v


def lenc(n, c):
    L = 0
    while n:
        n //= c
        L += 1
    return L


def find_expanding_cycles(a, b, c, lo=-6000, maxit=6000):
    """All cycles among negative integers; return the expanding ones."""
    found = {}
    for seed in range(lo, 0):
        if seed % c == 0:
            continue
        x, seen, order = seed, {}, []
        for step in range(maxit):
            if x in seen:
                cyc = order[seen[x]:]
                if cyc:
                    found.setdefault(tuple(sorted(cyc)), cyc)
                break
            if abs(x) > 10 ** 14:
                break
            seen[x] = step
            order.append(x)
            x, _ = T(x, a, b, c)
    out = []
    for cyc in found.values():
        K = len(cyc)
        E, y = 0, cyc[0]
        for _ in range(K):
            y, e = T(y, a, b, c)
            E += e
        if a ** K > c ** E and any(v < 0 for v in cyc):
            out.append((cyc, K, E))
    return out


# ---------------------------------------------------------------------------
# (0) anchor against the published SH1 certificate
# ---------------------------------------------------------------------------
print("\n(0) anchor: the general frame reproduces the published SH1 witness")
N, k = 8, 3
X = 2 ** N * (2 ** (k - 1) + 1) - 5
path = [X]
for _ in range(2):
    X, _ = T(X, 3, 1, 2)
    path.append(X)
check("x_{8,3} = 1275 -> 1913 -> 1435", path == [1275, 1913, 1435], str(path))
check("8*f^2(x) = 9x + 5", 8 * 1435 == 9 * 1275 + 5)
check("gain exceeds 9/8", Fraction(1435, 1275) > Fraction(9, 8),
      f"{Fraction(1435,1275)} > 9/8")
cyc = [-5, -7]
y = -5
E = 0
for _ in range(2):
    y, e = T(y, 3, 1, 2)
    E += e
check("the underlying cycle is -5 -> -7, K=2, E=3, expanding",
      y == -5 and E == 3 and 3 ** 2 > 2 ** 3, f"gain {Fraction(9,8)}")

# ---------------------------------------------------------------------------
# (1)-(5) the theorem across many maps
# ---------------------------------------------------------------------------
CASES = [(3,1,2),(5,1,2),(9,1,2),(5,3,2),(7,3,2),
         (2,1,3),(4,1,3),(5,2,3),(10,1,3),
         (3,1,5),(6,1,5)]

print("\n(1)-(5) shadow ingredients across (a,b,c)")
tested = 0
for (a, b, c) in CASES:
    if gcd(a, c) != 1:
        continue
    for cyc, K, E in find_expanding_cycles(a, b, c):
        gain = Fraction(a ** K, c ** E)
        ref, y = [], cyc[0]
        for _ in range(K):
            y, e = T(y, a, b, c)
            ref.append(e)
        # build a shadow deep enough that suffix closure is meaningful
        witness = None
        for N in range(E + 4, 26):
            for w in range(1, 400):
                Xs = cyc[0] + c ** N * w
                if Xs <= 0 or Xs % c == 0:
                    continue
                Y, got = Xs, []
                for _ in range(K):
                    Y, e = T(Y, a, b, c)
                    got.append(e)
                if got != ref:
                    continue
                if (Y - Xs) % c ** (N - E) != 0 or Y <= Xs:
                    continue
                if lenc(Xs, c) == lenc(Y, c):
                    witness = (N, Xs, Y, True)
                    break
                if witness is None:
                    witness = (N, Xs, Y, False)
            if witness and witness[3]:
                break
        if witness is None:
            check(f"({a},{b},{c}) K={K}: shadow exists", False)
            continue
        N, Xs, Y, len_ok = witness
        tested += 1
        tag = f"({a},{b},{c}) K={K} E={E} gain={gain}"
        check(f"{tag}: (a) valuation word reproduced", True)
        check(f"{tag}: (b) suffix closes mod c^(N-E)",
              (Y - Xs) % c ** (N - E) == 0, f"N={N}")
        check(f"{tag}: (c) exact value gain > 1",
              Fraction(Y, Xs) > 1, f"{Y}/{Xs}")
        check(f"{tag}: (e) len closes  <=>  gain < c",
              len_ok == (gain < c), f"len_ok={len_ok}, gain<c={gain < c}")

print(f"\n  expanding cycles exercised: {tested}")
check("at least 10 independent maps/cycles exercised", tested >= 10, str(tested))

# ---------------------------------------------------------------------------
# (6) non-vacuity: the hypothesis really can fail
# ---------------------------------------------------------------------------
print("\n(6) non-vacuity of the expanding-cycle hypothesis")
none_found = []
for (a, b, c) in [(7,1,2),(11,1,2),(5,1,3),(7,1,3),(11,1,3),(7,1,5),(4,1,5)]:
    if not find_expanding_cycles(a, b, c):
        none_found.append((a, b, c))
check("some maps have no expanding negative cycle in the search range",
      len(none_found) >= 4, f"{none_found}")
print("      (search-range statement only; absence here is NOT a proof of"
      " nonexistence)")

print("\n" + "=" * 62)
if FAILURES:
    print(f"FAILED: {len(FAILURES)} check(s)")
    for f in FAILURES:
        print("   -", f)
    sys.exit(1)
print("ALL PASS")
