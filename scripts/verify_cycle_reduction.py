#!/usr/bin/env python3
"""
Verification for "A Cycle Reduction for the 3x+1 Map".

Uses the exact affine accumulation (stopping_time_density.md) to derive the
cycle equation, then establishes what is provable elementarily:

  C1  cycle equation: a K-odd-step cycle through x satisfies
        x (2^{E_K} - 3^K) = c_K,   c_K = sum_{i<K} 3^{K-1-i} 2^{E_i} > 0,
      hence 2^{E_K} > 3^K (E_K >= ceil(K log2 3)) and x = c_K/(2^{E_K}-3^K).
  C2  bounded equation search (K<=8 and a stated finite E_K window):
      only the fixed point x=1.
  C3  cycle minima have natural density 0 (corollary of the stopping-time
      density theorem: a cycle minimum has sigma = infinity).
  C4  machine-verified finite exclusion: no nontrivial cycle has an element
      <= 10^6 (every odd m descends).

C3's density-0 conclusion is logical (from stopping_time_density.md); here we
verify the implication's hypothesis on a finite range (C4) and the equation
identities (C1, C2). Exact integer arithmetic.
"""
import math
from itertools import combinations

THETA = math.log2(3)


def v2(n):
    return (n & -n).bit_length() - 1 if n else 10 ** 9


def f(x):
    t = 3 * x + 1
    return t >> v2(t)


def accumulate(x, K):
    E = 0
    cur = x
    Es = []
    for _ in range(K):
        Es.append(E)
        t = 3 * cur + 1
        e = v2(t)
        cur = t >> e
        E += e
    cK = cur * (2 ** E) - (3 ** K) * x
    return E, cur, cK, Es


# ---------------------------------------------------------------- C1
def check_cycle_equation(xmax=50000):
    """For every odd x and K, x_K = x  <=>  x(2^{E_K}-3^K) = c_K, and the
       fixed point realises it with K=1, E=2, c=1."""
    # fixed point
    E, xK, cK, _ = accumulate(1, 1)
    assert xK == 1 and E == 2 and cK == 1 and 1 == cK // (2 ** E - 3 ** 1)
    # identity c_K = x_K 2^{E_K} - 3^K x, so x_K=x iff cycle equation holds
    for x in range(1, xmax, 2):
        for K in (1, 2, 3, 5, 8):
            E, xK, cK, Es = accumulate(x, K)
            assert cK == sum(3 ** (K - 1 - i) * 2 ** Es[i] for i in range(K))
            assert (xK == x) == (x * (2 ** E - 3 ** K) == cK)
    print("C1: PASS  cycle equation x(2^E-3^K)=c_K  (fixed point + identity)")


# ---------------------------------------------------------------- C2
def check_small_search(Kmax=8):
    def cK(Es, K):
        return sum(3 ** (K - 1 - i) * 2 ** Es[i] for i in range(K))
    mins = set()
    for K in range(1, Kmax + 1):
        Emin = math.ceil(K * THETA)
        for EK in range(Emin, Emin + K + 4):
            gap = 2 ** EK - 3 ** K
            if gap <= 0:
                continue
            for inner in combinations(range(1, EK), K - 1):
                Es = [0] + list(inner)
                c = cK(Es, K)
                if c % gap:
                    continue
                x = c // gap
                if x >= 1 and x % 2 == 1:
                    cur = x
                    for _ in range(K):
                        cur = f(cur)
                    if cur == x:
                        mins.add(x)
    assert mins == {1}, mins
    print("C2: PASS  bounded equation search K<=8 in the documented E_K window "
          "yields only the fixed point x=1")


# ---------------------------------------------------------------- C4 (=> C3 hypothesis)
def check_finite_exclusion(N=10 ** 6):
    """A nontrivial cycle's minimum m never descends below itself (sigma=inf).
       If any cycle element were <=N, its minimum would also be <=N.
       Every odd m in [3,N] descends, so no cycle element is <=N."""
    worst = fails = 0
    for m in range(3, N, 2):
        cur = m
        steps = 0
        while cur >= m:
            cur = f(cur)
            steps += 1
            if steps > 2000:
                fails += 1
                break
        worst = max(worst, steps)
    assert fails == 0
    print(f"C4: PASS  every odd m in [3,{N}] descends (max {worst} odd-steps); "
          f"no nontrivial cycle element <= {N}")
    print("C3: (corollary) cycle minima subset of {sigma=infinity} subset of non-K-good for all K, "
          "density <= rho^K -> 0  [see stopping_time_density.md]")


if __name__ == "__main__":
    check_cycle_equation()
    check_small_search()
    check_finite_exclusion()
    print("\nAll checks passed.")
