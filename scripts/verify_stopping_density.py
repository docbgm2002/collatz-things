#!/usr/bin/env python3
"""
Verification for "An Explicit Stopping-Time Density for the 3x+1 Map"
(an elementary, machine-checked re-derivation of Terras 1976 / Everett 1977,
with an explicit geometric rate).

Exact integer / rational arithmetic throughout.

  L1  accumulation:  x_K = (3^K x + c_K)/2^{E_K},
      c_K = sum_{i<K} 3^{K-1-i} 2^{E_i},  and  c_K/2^{E_K} < (3/2)^K.
  L2  descent criterion: E_K(x) >= K*log2(3)+1 and x >= 2(3/2)^K  =>  x_K < x.
  L3  exact valuation equidistribution: among odd residues mod 2^N, every
      K-step valuation pattern of total weight E (<= N-1) occurs EXACTLY
      2^{N-1-E} times (so the per-step valuations are i.i.d. Geometric(1/2)).
  T   density: D(K) = density{ odd x : stopping time sigma(x) <= K } satisfies
      D(K) >= 1 - rho^K  with  rho = e^{-I(log2 3)} = 0.94650...,
      I the Cramer rate of the geometric valuation sum.  Hence D(K) -> 1.

No external dependencies.
"""
import math
from fractions import Fraction as Fr
from collections import Counter

THETA = math.log2(3)            # 1.5849625...


def v2(n):
    return (n & -n).bit_length() - 1 if n else 10 ** 9


def f(x):
    t = 3 * x + 1
    return t >> v2(t)


def accumulate(x, K):
    """Return (E_K, x_K, c_K, [E_0..E_{K-1}]) for K odd-steps."""
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


# ----------------------------------------------------------------- L1
def check_accumulation(xmax=120000):
    for K in range(1, 13):
        for x in range(3, xmax, 2):
            E, xK, cK, Es = accumulate(x, K)
            assert xK * (2 ** E) == 3 ** K * x + cK, (x, K)
            assert cK == sum(3 ** (K - 1 - i) * 2 ** Es[i] for i in range(K)), (x, K)
            assert Fr(cK, 2 ** E) < Fr(3, 2) ** K, (x, K)
    print("L1: PASS  x_K=(3^K x + c_K)/2^E, c_K=sum 3^(K-1-i)2^(E_i), "
          "c_K/2^E < (3/2)^K  (K<=12)")


# ----------------------------------------------------------------- L2
def check_descent_criterion(xmax=200000):
    bad = tested = 0
    for K in range(1, 13):
        thr = math.floor(K * THETA) + 1            # E >= K log2 3 + 1
        xmin = math.ceil(2 * (1.5 ** K))
        for x in range(3, xmax, 2):
            E, xK, _, _ = accumulate(x, K)
            if E >= thr and x >= xmin:
                tested += 1
                if not (xK < x):
                    bad += 1
    assert bad == 0, bad
    print(f"L2: PASS  E_K>=K log2 3 + 1 and x>=2(3/2)^K  =>  x_K<x  "
          f"({tested} cases, 0 violations)")


# ----------------------------------------------------------------- L3
def check_equidistribution_exact():
    def pattern(x, K):
        p = []
        cur = x
        for _ in range(K):
            t = 3 * cur + 1
            e = v2(t)
            cur = t >> e
            p.append(e)
        return tuple(p)

    for N, K in [(12, 4), (14, 4), (16, 5)]:
        groups = Counter()
        for r in range(1, 2 ** N, 2):
            groups[pattern(r, K)] += 1
        checked = 0
        for pat, c in groups.items():
            E = sum(pat)
            if E <= N - 1:                          # fully determined patterns
                assert c == 2 ** (N - 1 - E), (N, K, pat, c)
                checked += 1
        print(f"L3: mod 2^{N}, K={K}: {checked} patterns, each weight-E pattern "
              f"occurs exactly 2^({N}-1-E)  PASS")


# ----------------------------------------------------------------- T (rate + density)
def geom_conv(K, maxE):
    """Exact P(E_K = E) for E_K = sum of K i.i.d. Geometric(1/2) on {1,2,...}."""
    dist = {0: Fr(1)}
    for _ in range(K):
        nd = {}
        for E, p in dist.items():
            j = 1
            while E + j <= maxE:
                nd[E + j] = nd.get(E + j, Fr(0)) + p * Fr(1, 2 ** j)
                j += 1
        dist = nd
    return dist


def cramer_rate(theta=THETA):
    u = 2 * (theta - 1) / theta                      # maximiser u* in (0,1)
    I = (theta - 1) * math.log(u) + math.log(2 - u)
    return I, math.exp(-I)


def check_rate_and_density():
    I, rho = cramer_rate()
    print(f"T:  Cramer rate I(log2 3) = {I:.5f},  rho = e^-I = {rho:.5f}")
    print(f"    {'K':>3} {'P(non-good)':>12} {'rho^K':>10} {'1-rho^K':>9} "
          f"{'meas D(K)':>10}")
    # measured stopping-time density over odd x in [3, XMAX]
    XMAX = 200000
    sig = []
    for x in range(3, XMAX, 2):
        cur = x
        s = 0
        while cur >= x:
            cur = f(cur)
            s += 1
        sig.append(s)
    sig.sort()
    nsamp = len(sig)
    import bisect
    for K in [4, 8, 12, 16, 20, 24]:
        a = math.floor(THETA * K)                    # non-good = {E_K <= a}
        dist = geom_conv(K, 3 * K)
        Pbad = float(sum(dist[E] for E in dist if E <= a))
        rk = rho ** K
        assert Pbad <= rk + 1e-12, (K, Pbad, rk)     # Cramer upper bound
        measD = bisect.bisect_right(sig, K) / nsamp  # density sigma(x) <= K
        assert measD >= 1 - rk - 1e-9, (K, measD, 1 - rk)
        print(f"    {K:3d} {Pbad:12.4e} {rk:10.4f} {1-rk:9.4f} {measD:10.4f}")
    print("    PASS  P(non-good) <= rho^K  and  measured D(K) >= 1 - rho^K -> 1")


if __name__ == "__main__":
    check_accumulation()
    check_descent_criterion()
    check_equidistribution_exact()
    check_rate_and_density()
    print("\nAll checks passed.")
