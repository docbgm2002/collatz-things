#!/usr/bin/env python3
"""
verify_cost_law_proof.py
========================

Step-by-step machine verification of the PROOF of the cost law (COST1),
upgrading it from a finite certificate over ten maps to a theorem.

THEOREM (COST1).  Let beta = log_c(a) be irrational and Q >= 1.  Let
K_min(Q) be the least K admissible at precision Q, i.e. the least K with
s(Q,K) = floor(K beta)*Q - K*floor(Q beta) in [0, K].  Then floor(K_min
beta)/K_min is a best approximation to beta FROM BELOW, and hence K_min(Q)
is the denominator of a semiconvergent of beta lying below beta.

PROOF, and what each step below checks:

  S0  s = K*phi_Q - Q*{K beta}                         [Lemma L1, algebra]
  S1  the upper half of the window is VACUOUS: s <= K always, because
      s <= K  <=>  K(phi_Q - 1) <= Q{K beta}, and phi_Q < 1 (irrationality)
      makes the left side negative and the right side nonnegative.
      So admissibility reduces to s >= 0.
  S2  s >= 0  <=>  floor(K beta)/K >= floor(Q beta)/Q.
  S3  Q is admissible at Q, so K_min(Q) exists and K_min(Q) <= Q.
  S4  minimality forces a STRICT RECORD of K |-> floor(K beta)/K.
  S5  beta irrational gives floor(K beta)/K < beta < (floor(K beta)+1)/K,
      so floor(K beta)/K is the largest fraction of denominator exactly K
      below beta; a record therefore says it is the largest of denominator
      AT MOST K below beta -- a best approximation from below.
  S6  CLASSICAL INPUT (not proved here): the best approximations from below
      to an irrational are exactly its semiconvergents lying below it.
      (Khinchin, Continued Fractions, theory of intermediate fractions.)
      Checked here as an inclusion over ten maps.

PRECISION.  floor(K beta) is computed in 200-digit decimal and every
evaluation ASSERTS a separation of at least 1e-50 from an integer, so no
floor is ever decided within the error of the representation.  The values
are additionally cross-checked against exact integer comparison
(c^m <= a^K) on a subrange.  All comparisons of fractions are exact
Fractions.
"""

import sys
from fractions import Fraction as F
from decimal import Decimal, getcontext

getcontext().prec = 200
MARGIN = Decimal(10) ** -50
FAILURES = []


def check(name, cond, detail=""):
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))
    if not cond:
        FAILURES.append(name)


def beta(a, c):
    return Decimal(a).ln() / Decimal(c).ln()


def flo(K, b):
    v = K * b
    f = int(v // 1)
    assert min(v - f, f + 1 - v) > MARGIN, "insufficient precision"
    return f


def flo_exact(K, a, c):
    lo, hi = 0, K * a.bit_length() + 2
    while lo < hi:
        m = (lo + hi + 1) // 2
        if c ** m <= a ** K:
            lo = m
        else:
            hi = m - 1
    return lo


def cf_log(x, y, n=11):
    out = []
    x, y = F(x), F(y)
    for _ in range(n):
        k = 0
        while x ** (k + 1) <= y:
            k += 1
        out.append(k)
        r = y / x ** k
        if r == 1:
            break
        x, y = r, x
    return out


def semiconvergents(cfl):
    p0, q0, p1, q1 = 1, 0, cfl[0], 1
    S = [(p1, q1)]
    for aa in cfl[1:]:
        for t in range(1, aa + 1):
            S.append((p0 + t * p1, q0 + t * q1))
        p0, q0, p1, q1 = p1, q1, aa * p1 + p0, aa * q1 + q0
    return S


MAPS = [(3,2),(5,2),(5,3),(7,2),(7,3),(4,3),(10,3),(3,5),(11,2),(13,3)]

# ---------------------------------------------------------------------------
print("\n(P) precision control")
ok = True
for (a, c) in [(3,2),(5,3),(13,3)]:
    b = beta(a, c)
    if any(flo(K, b) != flo_exact(K, a, c) for K in range(1, 120)):
        ok = False
check("decimal floor agrees with exact integer floor (K<120, 3 maps)", ok)

# ---------------------------------------------------------------------------
print("\n(S1) the upper half of the window is vacuous:  s <= K always")
viol = []
for (a, c) in MAPS[:6]:
    b = beta(a, c)
    for j in range(1, 11):
        Q = 2 ** j
        LQ = flo(Q, b)
        for K in range(1, 500):
            if flo(K, b) * Q - K * LQ > K:
                viol.append((a, c, Q, K))
check("no (map,Q,K) with s > K", not viol, f"{len(viol)} violations")
print("      => the manuscript's window s in [0,K] is equivalent to s >= 0")

# ---------------------------------------------------------------------------
print("\n(S2) admissibility  <=>  floor(K b)/K >= floor(Q b)/Q")
mis = 0
for (a, c) in MAPS[:6]:
    b = beta(a, c)
    for j in range(1, 11):
        Q = 2 ** j
        LQ = flo(Q, b)
        for K in range(1, 500):
            E = flo(K, b)
            if (0 <= E * Q - K * LQ <= K) != (F(E, K) >= F(LQ, Q)):
                mis += 1
check("criterion equivalence holds", mis == 0, f"{mis} mismatches")

# ---------------------------------------------------------------------------
print("\n(S3)/(S4) K_min exists, K_min <= Q, and is a STRICT record")
tested = nonrec = toobig = 0
for (a, c) in MAPS:
    b = beta(a, c)
    for j in range(1, 12):
        Q = 2 ** j
        LQ = flo(Q, b)
        km = None
        for K in range(1, 8000):
            if F(flo(K, b), K) >= F(LQ, Q):
                km = K
                break
        if km is None:
            continue
        tested += 1
        if km > Q:
            toobig += 1
        v = F(flo(km, b), km)
        if any(F(flo(K, b), K) >= v for K in range(1, km)):
            nonrec += 1
check("K_min(Q) <= Q always", toobig == 0, f"{tested} (map,Q) pairs")
check("K_min(Q) is a strict record of floor(Kb)/K", nonrec == 0,
      f"{tested} (map,Q) pairs")

# ---------------------------------------------------------------------------
print("\n(S5) records are best approximations FROM BELOW")
bad = 0
for (a, c) in MAPS[:5]:
    b = beta(a, c)
    best, recs = None, []
    for K in range(1, 1200):
        v = F(flo(K, b), K)
        if best is None or v > best:
            best = v
            recs.append(K)
    for K in recs:
        p = flo(K, b)
        if not (Decimal(p) / Decimal(K) < b < Decimal(p + 1) / Decimal(K)):
            bad += 1
        if any(F(flo(Kp, b), Kp) >= F(p, K) for Kp in range(1, K)):
            bad += 1
check("every record is a best under-approximation", bad == 0, f"{bad} violations")

# ---------------------------------------------------------------------------
print("\n(S6) classical input: records lie among semiconvergents below beta")
allok = True
for (a, c) in MAPS:
    b = beta(a, c)
    S = semiconvergents(cf_log(c, a, 11))
    below = {q for (p, q) in S if Decimal(p) / Decimal(q) < b}
    lim = max(below)
    best, recs = None, []
    for K in range(1, min(lim, 20000) + 1):
        v = F(flo(K, b), K)
        if best is None or v > best:
            best = v
            recs.append(K)
    missing = [k for k in recs if k not in below]
    if missing:
        allok = False
    check(f"log_{c}({a}): all records are semiconvergent-below denominators",
          not missing, f"{len(recs)} records" if not missing else str(missing[:4]))

# ---------------------------------------------------------------------------
print("\n(A) anchor: the (3,2) instance reproduces QLG1's published pairs")
b32 = beta(3, 2)
for (j, K) in [(3,2),(5,7),(8,12),(9,53),(12,665),(14,665)]:
    Q = 2 ** j
    s = flo(K, b32) * Q - K * flo(Q, b32)
    check(f"j={j:2d}, K={K:4d} admissible", 0 <= s <= K, f"s={s}")
s = flo(53, b32) * 4096 - 53 * flo(4096, b32)
check("regression (j,K)=(12,53) rejected", not (0 <= s <= 53), f"s={s}")

print("\n" + "=" * 64)
if FAILURES:
    print(f"FAILED: {len(FAILURES)} check(s)")
    for f in FAILURES:
        print("   -", f)
    sys.exit(1)
print("ALL PASS")
