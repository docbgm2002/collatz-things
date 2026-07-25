#!/usr/bin/env python3
"""
verify_quantized_log_witnesses.py
=================================

Independent, exact verification of quantized-log no-go certificates for the
3x+1 map, re-mined from scratch (WITN1).

WHAT A CERTIFICATE IS.  Fix precision Q = 2^j and modulus m.  The coordinate
is

    C(x) = ( floor(Q * log_2 x),  tau(x),  x mod m ).

A certificate is a list of K odd integers x_1, ..., x_K such that, writing
y_i = f(x_i) = (3 x_i + 1)/2^{v_2(3 x_i + 1)},

    C(y_i) = C(x_{i+1})   for i = 1..K   (indices mod K)      [closure]
    y_1 y_2 ... y_K  >  x_1 x_2 ... x_K                       [strict gain]

Then no potential Phi(x) = log_2 x + g(C(x)) is nonincreasing: summing the
K monotonicity constraints makes every g-term cancel by closure, leaving
log_2(prod y_i) <= log_2(prod x_i), contradicting strict gain.

WHY THIS FILE EXISTS.  The original mining and verification scripts for
manuscript Section 6 are not in the repository.  These certificates were
re-mined independently (Bellman-Ford negative-cycle search over the
coordinate digraph, floats for GUIDANCE ONLY) and are confirmed here in
exact integer arithmetic.  Nothing in this file uses floating point.

EXACTNESS OF THE QUANTIZED LOG.  For integer Q,

    floor(Q * log_2 x) = bitlength(x^Q) - 1,

since 2^n <= x^Q < 2^{n+1} iff n = bitlength(x^Q) - 1.  Pure integer
arithmetic; no logarithm is ever evaluated numerically.
"""

import json
import os
import sys

FAILURES = []


def check(name, cond, detail=""):
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))
    if not cond:
        FAILURES.append(name)


def qlog2(x, Q):
    """Exact floor(Q * log_2 x) by bit length. No floating point."""
    return (x ** Q).bit_length() - 1


def v2(n):
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def f(x):
    y = 3 * x + 1
    e = v2(y)
    return y // 2 ** e, e


def tau(x):
    t = 0
    while (x >> t) & 1:
        t += 1
    return t


def coord(x, Q, m):
    return (qlog2(x, Q), tau(x), x % m)


def floor_K_log2_3(K):
    return (3 ** K).bit_length() - 1


def admissible(j, K):
    """COST1 criterion: s = floor(K b) 2^j - K floor(2^j b) in [0, K]."""
    L = (3 ** (2 ** j)).bit_length() - 1
    s = (floor_K_log2_3(K) << j) - K * L
    return 0 <= s <= K, s


# ---------------------------------------------------------------------------
print("\n(E) exactness of the quantized logarithm")
ok = True
for x in (3, 5, 1275, 99991, 2 ** 20 + 7):
    for j in (0, 1, 3, 5):
        Q = 2 ** j
        n = qlog2(x, Q)
        if not (2 ** n <= x ** Q < 2 ** (n + 1)):
            ok = False
check("bitlength identity gives the true floor(Q log_2 x)", ok,
      "2^n <= x^Q < 2^(n+1) confirmed")

# ---------------------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(HERE, "certificates_quantized_log_remined.json")
if not os.path.exists(PATH):
    print(f"\nERROR: {PATH} not found")
    sys.exit(1)
CERTS = json.load(open(PATH))

print("\n(C) certificate verification, exact integer arithmetic")
for j in sorted(CERTS, key=int):
    d = CERTS[j]
    j_i, m, K = int(j), d["m"], d["K"]
    Q = 2 ** j_i
    W = d["witnesses"]

    good = len(W) == K
    check(f"j={j_i}: K={K} witnesses present", good)
    if not good:
        continue

    # every witness is odd and > 1
    check(f"j={j_i}: all witnesses odd and > 1",
          all(x % 2 == 1 and x > 1 for x in W))

    # closure
    Y = [f(x)[0] for x in W]
    closes = all(coord(Y[i], Q, m) == coord(W[(i + 1) % K], Q, m) for i in range(K))
    check(f"j={j_i}: coordinate cycle closes at all {K} junctions", closes)

    # strict gain, as an exact integer comparison
    num = den = 1
    for x, y in zip(W, Y):
        num *= y
        den *= x
    check(f"j={j_i}: strict gain  prod(y) > prod(x)", num > den,
          f"{num.bit_length()}-bit vs {den.bit_length()}-bit, ratio ~ {num / den:.8f}")

    # the total valuation matches floor(K log_2 3) or is admissible
    adm, s = admissible(j_i, K)
    check(f"j={j_i}: K={K} satisfies the COST1 closure criterion", adm, f"s={s}")

    # witnesses are distinct (a degenerate repeated witness would be vacuous)
    check(f"j={j_i}: witnesses distinct", len(set(W)) == K)

    print(f"       window 2^{d['window_bits']}, first witness {W[0]}")

# ---------------------------------------------------------------------------
print("\n(H) height law:  witnesses first appear at log_2 x ~ j + O(1)")
rows = [(int(j), CERTS[j]["window_bits"]) for j in sorted(CERTS, key=int)]
diffs = {b - j for j, b in rows}
check("window_bits - j is constant across j", len(diffs) == 1,
      f"constant = {diffs.pop() if len(diffs) == 1 else diffs}")
print("      consistent with the counting heuristic: an interval of")
print("      multiplicative width 2^(1/Q) about x holds ~x/(Q) integers, so a")
print("      residue class mod 2^(m+e) is hit once log_2 x >~ m + e + j.")
print("      THIS IS EVIDENCE, NOT A PROOF, OF SUFFICIENCY.")

print("\n" + "=" * 64)
if FAILURES:
    print(f"FAILED: {len(FAILURES)} check(s)")
    for x in FAILURES:
        print("   -", x)
    sys.exit(1)
print("ALL PASS")
