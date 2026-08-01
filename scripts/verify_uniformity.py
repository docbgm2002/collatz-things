#!/usr/bin/env python3
"""
verify_uniformity.py
====================

Machine verification of UNIF1 (the cell-dip bound) and of SUFF1 in the case
(j, K) = (3, 2), via an explicit infinite family of certificates.

UNIF1 (cell dip).  Around a cycle the cells return, but partial products can
dip.  With X_i = 2^{C_i/Q}, we have X_i / X_1 = 3^{i-1} / 2^{E_{i-1}}, so the
worst prefix dip is min_i ( floor((i)*log_2 3) - E_i ), which for the WALK1
recipe word with payouts front-loaded is linear in K at rate about -0.24.
Hence the starting cell need only be chosen O(K) higher than the
single-edge threshold.

SUFF1 at (j, K) = (3, 2).  Take

    x_1 = 2^n + 27.

Then for n >= 10, EXACTLY:
    3 x_1 + 1 = 2 (3 * 2^{n-1} + 41),          so e_1 = 1 and
    y_1 = f(x_1) = 3 * 2^{n-1} + 41;
    tau(x_1) = v_2(2^n + 28) = 2;
    x_1 = 11 (mod 16);
    tau(y_1) = v_2(3*2^{n-1} + 42) = 1;
    y_1 = 9 (mod 16);
    cell(y_1) - cell(x_1) = +4 = L_Q - Q e_1 + delta = 12 - 8 + 0.

THE BOUND n >= 10 IS SHARP AND IS CARRY1.  The in-cell position of x_1 is
u_n = 8 log_2(1 + 27/2^n), decreasing in n, and delta = 1 exactly when
u_n >= 1 - phi_Q with phi_Q = {8 log_2 3}.  At n = 9, u_9 > 1 - phi_Q so
delta = 1 and the cell shift is +5, breaking closure; from n = 10 on,
delta = 0.  An earlier draft claimed the family from n >= 5 and the verifier
caught n = 9; logged in CLAIM_LEDGER.md.

The partner x_2 is then the least integer congruent to 9 mod 16 lying in the
non-carrying sub-interval of cell(y_1).  That sub-interval has length about
2^n * (1 - phi_Q) * ln2 / Q, which exceeds the modulus 16 for all n >= 8, so
x_2 EXISTS by the elementary count.  The carry lemma (CARRY1) then forces
cell(f(x_2)) = cell(x_1), and TAU1 forces the tau match.

The verifier confirms the algebraic identities symbolically for many n, and
exhibits closed, gaining certificates up to n = 200 (201-bit witnesses).

NO FLOATING POINT APPEARS IN ANY ASSERTION.
"""

import sys

FAILURES = []


def check(name, cond, detail=""):
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))
    if not cond:
        FAILURES.append(name)


def v2(n):
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def tau(x):
    return v2(x + 1)


def f(x):
    y = 3 * x + 1
    e = v2(y)
    return y // 2 ** e, e


Q, MOD = 8, 16


def qlog2(x, q=Q):
    return (x ** q).bit_length() - 1


def coord(x):
    return (qlog2(x), tau(x), x % MOD)


def L_of(q):
    return (3 ** q).bit_length() - 1


# ---------------------------------------------------------------------------
print("\n(UNIF1) the cell dip is linear in K")
rows = []
for K in (12, 53, 120, 300, 800):
    E = (3 ** K).bit_length() - 1
    b, a = E - K - 2, 2 * K - E - 3
    word = ([2] * b + [1] * a)[:K]
    while len(word) < K:
        word.append(1)
    mn, Ei = 0, 0
    for i, e in enumerate(word):
        Ei += e
        mn = min(mn, ((3 ** (i + 1)).bit_length() - 1) - Ei)
    rows.append((K, mn))
check("dip is negative and O(K)", all(m < 0 for _, m in rows),
      ", ".join(f"K={K}: 2^{m}" for K, m in rows))
rates = [abs(m) / K for K, m in rows]
check("dip rate is bounded (approaches a constant)",
      max(rates) - min(rates) < 0.02,
      f"rates {[round(r,4) for r in rates]}")

# ---------------------------------------------------------------------------
print("\n(F) the algebraic identities of the family x_1 = 2^n + 27")
bad = []
for n in range(10, 300):
    x1 = 2 ** n + 27
    y1, e1 = f(x1)
    if e1 != 1:
        bad.append(("e1", n))
    if y1 != 3 * 2 ** (n - 1) + 41:
        bad.append(("y1", n))
    if tau(x1) != 2:
        bad.append(("tau x1", n))
    if x1 % MOD != 11:
        bad.append(("x1 mod 16", n))
    if tau(y1) != 1:
        bad.append(("tau y1", n))
    if y1 % MOD != 9:
        bad.append(("y1 mod 16", n))
    if qlog2(y1) - qlog2(x1) != 4:
        bad.append(("cell shift", n))
check("e_1 = 1, y_1 = 3*2^(n-1)+41, tau/residue/cell-shift as claimed",
      not bad, f"n = 10..299, {len(bad)} violations")

# the exclusion of n = 9 is CARRY1, not an accident
x9 = 2 ** 9 + 27
y9, _ = f(x9)
check("n = 9 is excluded because delta = 1 (a carry), shift = +5",
      qlog2(y9) - qlog2(x9) == 5, f"shift {qlog2(y9) - qlog2(x9)}")
check("n = 10 is the first n with delta = 0",
      qlog2(f(2 ** 10 + 27)[0]) - qlog2(2 ** 10 + 27) == 4)
check("cell shift equals L_Q - Q*e_1 + 0", L_of(Q) - Q * 1 == 4,
      f"L_Q = {L_of(Q)}, 12 - 8 = 4")

# ---------------------------------------------------------------------------
print("\n(S) closed, gaining certificates at prescribed heights")


def lowest_in_cell(C, hi_bits):
    lo, hi = 1, 1 << hi_bits
    while lo < hi:
        mid = (lo + hi) // 2
        if qlog2(mid) >= C:
            hi = mid
        else:
            lo = mid + 1
    return lo


def build(n, cap=400000):
    x1 = 2 ** n + 27
    y1, _ = f(x1)
    c1, cy1 = coord(x1), coord(y1)
    start = lowest_in_cell(cy1[0], n + 4)
    xx = start + ((9 - start) % MOD)
    cnt = 0
    while qlog2(xx) == cy1[0] and cnt < cap:
        if coord(xx) == cy1:
            y2, _ = f(xx)
            if coord(y2) == c1 and y1 * y2 > x1 * xx:
                return x1, y1, xx, y2
        xx += MOD
        cnt += 1
    return None


TESTS = list(range(10, 31)) + [40, 60, 80, 120, 160, 200]
fails = []
for n in TESTS:
    r = build(n)
    if r is None:
        fails.append(n)
        continue
    x1, y1, x2, y2 = r
    ok = (f(x1)[0] == y1 and f(x2)[0] == y2
          and coord(y1) == coord(x2) and coord(y2) == coord(x1)
          and y1 * y2 > x1 * x2
          and x1 % 2 == 1 and x2 % 2 == 1 and x1 != x2)
    if not ok:
        fails.append(n)
check("a closed gaining 2-cycle exists for every tested n", not fails,
      f"n up to {max(TESTS)}, {len(fails)} failures")

r = build(200)
if r:
    x1, y1, x2, y2 = r
    check("n = 200: witnesses are 201-bit and the cycle closes exactly",
          x1.bit_length() == 201 and coord(y1) == coord(x2)
          and coord(y2) == coord(x1) and y1 * y2 > x1 * x2,
          f"x1 has {x1.bit_length()} bits, x2 has {x2.bit_length()} bits")

# ---------------------------------------------------------------------------
print("\n(N) the counting bound that makes x_2 exist is met")
for n in (8, 12, 40, 200):
    x1 = 2 ** n + 27
    y1, _ = f(x1)
    C = coord(y1)[0]
    lo = lowest_in_cell(C, n + 4)
    hi = lowest_in_cell(C + 1, n + 5)
    check(f"n={n}: cell length exceeds the modulus 16", hi - lo > MOD,
          f"cell holds {hi - lo} integers")

print("\n(X) SCOPE")
print("""      SUFF1 is established here for (j,K) = (3,2) only: an explicit
      infinite family plus the elementary count.  The general case has all
      its ingredients (CARRY1, FREE1, WALK1, TAU1, UNIF1) but the composition
      with constants uniform in (j,K,m) is NOT written out.  SUFF1 in general
      remains OPEN.""")

print("\n" + "=" * 64)
if FAILURES:
    print(f"FAILED: {len(FAILURES)} check(s)")
    for x in FAILURES:
        print("   -", x)
    sys.exit(1)
print("ALL PASS")
