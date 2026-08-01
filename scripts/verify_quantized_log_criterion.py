#!/usr/bin/env python3
"""
verify_quantized_log_criterion.py
=================================

Exact-integer verification of the arithmetic half of QLG1 (manuscript
Theorem E / Section 6): the closure criterion for multi-witness cycles in
the quantized-logarithm potential class

    Phi(x) = log_2 x + g( floor(2^j log_2 x), tau(x), x mod 2^m ).

SCOPE.  This script verifies the *criterion* and the *admissible-K
proposition*.  It does NOT re-mine or re-check the integer witness
certificates; those live in `verify_quantized_log.py` /
`certificates_quantized_log.json`, which are not present in this
checkout (see REPO_EDITS_3.md).  Status of what is checked here:

    (C1) exact evaluation of E_K = floor(K log_2 3) and
         L_j = floor(2^j log_2 3) with no floating point;
    (C2) the closure criterion s = E_K * 2^j - K * L_j in [0, K];
    (C3) reproduction of the published admissible (j, K) table;
    (C4) the regression case (j, K) = (12, 53), which an earlier
         float-based criterion wrongly admitted;
    (C5) the Proposition: an admissible K exists for every j tested.

NO FLOATING POINT APPEARS IN ANY ASSERTION.

Method.  With beta = log_2 3, floor(K*beta) is the largest E with
2^E <= 3^K, i.e. bitlength(3^K) - 1.  Likewise L_j = bitlength(3^(2^j)) - 1.
Both are exact integer computations.
"""

import sys

FAILURES = []


def check(name, condition, detail=""):
    status = "PASS" if condition else "FAIL"
    print(f"  [{status}] {name}" + (f"  ({detail})" if detail else ""))
    if not condition:
        FAILURES.append(name)


def floor_K_log2_3(K):
    """Exact floor(K * log_2 3), integer arithmetic only."""
    return (3 ** K).bit_length() - 1


def L(j):
    """Exact L_j = floor(2^j * log_2 3), integer arithmetic only."""
    return (3 ** (2 ** j)).bit_length() - 1


def slack(j, K):
    """Exact closure slack s = E_K * 2^j - K * L_j."""
    return (floor_K_log2_3(K) << j) - K * L(j)


def admissible(j, K):
    """Closure criterion: 0 <= s <= K."""
    return 0 <= slack(j, K) <= K


# ---------------------------------------------------------------------------
# (C1) exactness of the floor evaluations
# ---------------------------------------------------------------------------
print("\n(C1) exact floor evaluations")
ok = True
for K in range(1, 400):
    E = floor_K_log2_3(K)
    # defining property: 2^E <= 3^K < 2^(E+1)
    if not (2 ** E <= 3 ** K < 2 ** (E + 1)):
        ok = False
        break
check("2^E_K <= 3^K < 2^(E_K+1) for 1 <= K <= 399", ok)

ok = True
for j in range(0, 16):
    Lj = L(j)
    if not (2 ** Lj <= 3 ** (2 ** j) < 2 ** (Lj + 1)):
        ok = False
        break
check("2^L_j <= 3^(2^j) < 2^(L_j+1) for 0 <= j <= 15", ok)

# ---------------------------------------------------------------------------
# (C2)/(C3) the published admissible table
# ---------------------------------------------------------------------------
print("\n(C3) published admissible (j, K) pairs")
PUBLISHED = {3: 2, 5: 7, 8: 12, 9: 53, 12: 665, 14: 665}
for j, K in sorted(PUBLISHED.items()):
    s = slack(j, K)
    check(
        f"j={j:2d}, K={K:4d} admissible",
        admissible(j, K),
        f"E={floor_K_log2_3(K)}, L_j={L(j)}, s={s}, bound K={K}",
    )

# ---------------------------------------------------------------------------
# (C3b) minimality of the published K at each j
# ---------------------------------------------------------------------------
print("\n(C3b) minimality of the published K")
for j, K in sorted(PUBLISHED.items()):
    smaller = [k for k in range(1, K) if admissible(j, k)]
    check(f"no admissible K' < {K} at j={j}", not smaller,
          f"found {smaller[:5]}" if smaller else "minimal")

# ---------------------------------------------------------------------------
# (C4) regression: the float criterion wrongly admitted (j, K) = (12, 53)
# ---------------------------------------------------------------------------
print("\n(C4) regression case (j, K) = (12, 53)")
s = slack(12, 53)
check("(12, 53) is REJECTED by the exact criterion", not admissible(12, 53),
      f"s = {s} < 0")

# ---------------------------------------------------------------------------
# (C5) an admissible K exists for every j in range
# ---------------------------------------------------------------------------
print("\n(C5) existence of an admissible K for each j")
for j in range(0, 15):
    found = None
    for K in range(1, 20000):
        if admissible(j, K):
            found = K
            break
    check(f"admissible K exists at j={j:2d}", found is not None,
          f"minimal K = {found}")

# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
if FAILURES:
    print(f"FAILED: {len(FAILURES)} check(s): {FAILURES}")
    sys.exit(1)
print("ALL PASS")
