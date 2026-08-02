#!/usr/bin/env python3
"""Diagnostics for docs/no-go/avenue_a_mean_valuation_route.md.

Exploratory. Generates the three measurements in that note:

  A. the mean-valuation reformulation of Gap SD-K-block-8-17
     (rest >= 0  <=>  E_K / K_down >= 20/11), and the complete list of
     odd n below the threshold;
  B. dyadic-window minima of E_K / K_down, showing the margin grows;
  C. the minimum mean cycle of Delta = 11(e-1) - 9h on the block
     automaton mod 2^m, which is negative and m-independent -- the
     mechanical no-go for closing the gap by modulus refinement.

All arithmetic is exact integer arithmetic; the only floats are the
reported ratios, which are measurements, not claims.

Usage:
    python3 scripts/explore_mean_valuation_gap.py [--limit 6001] [--mmc]
"""

import argparse
from collections import defaultdict
from fractions import Fraction

THRESHOLD = Fraction(20, 11)


def v2(x: int) -> int:
    return (x & -x).bit_length() - 1


# ---------------------------------------------------------------- A / B

def first_descent(n: int):
    """Return (K_down, E_K) for the odd-indexed repunit tail a_n."""
    x = (3 ** n - 1) // 2
    target = 2 ** n - 1
    K = 0
    E = 0
    while x >= target:
        e = v2(3 * x + 1)
        x = (3 * x + 1) >> e
        E += e
        K += 1
    return K, E


def scan(limit: int):
    out = {}
    for n in range(3, limit + 1, 2):
        K, E = first_descent(n)
        out[n] = (K, E, Fraction(E, K))
    return out


def report_threshold(vals):
    below = sorted(n for n, (_, _, r) in vals.items() if r < THRESHOLD)
    print("A. mean-valuation reformulation")
    print("   rest >= 0  <=>  E_K / K_down >= 20/11 = %.6f" % float(THRESHOLD))
    print("   odd n with E_K/K < 20/11 :", below)
    print("   (expected: [5, 17, 23] -- exactly the known exceptional set;")
    print("    n=17 is the Gap SD-K-block-8-17 equality case, n=23 the 5n-2")
    print("    even-budget saturation and unique 911 miss, n=5 handled direct)")
    n11 = vals.get(11)
    if n11:
        print("   n=11 (the unique 911-6-strong miss): %.6f" % float(n11[2]))
    print()


def report_windows(vals):
    print("B. dyadic-window minima of E_K / K_down")
    print("   %-16s %7s  %-10s %7s  %s" % ("window", "count", "min", "argmin", "margin"))
    lo = 8
    top = max(vals)
    while lo <= top:
        hi = min(2 * lo, top + 1)
        sub = [(r, n) for n, (_, _, r) in vals.items() if lo <= n < hi]
        if sub:
            r, n = min(sub)
            print("   [%5d,%5d)   %6d  %.6f  %6d   %+.6f"
                  % (lo, hi, len(sub), float(r), n, float(r - THRESHOLD)))
        lo = hi
    print("   (the minimum rises and settles near 1.93: the gap is marginal")
    print("    only at n <= 23, which is where the finite certificates saturate)")
    print()


# -------------------------------------------------------------------- C

def block(x: int):
    """One Avenue A block from an odd x with h(x)=1.

    Payout e = v2(3x+1) >= 2, landing y of height h = v2(y+1), then h-1
    rails back to an h=1 state via Lemma SD-K-rail-closed.
    Returns (e, h, x_next).
    """
    e = v2(3 * x + 1)
    y = (3 * x + 1) >> e
    h = v2(y + 1)
    if h == 1:
        return e, h, y
    return e, h, 3 ** (h - 1) * ((y + 1) >> (h - 1)) - 1


def raw_transitions(m: int, pad: int):
    """Transitions on states x mod 2^m, enumerated from explicit lifts.

    Only outcomes determined by the enumerated bits are kept, so every
    edge produced is realizable: this under-approximates the edge set,
    which is the conservative direction for exhibiting a bad cycle.
    """
    mask = (1 << m) - 1
    out = []
    for x in range(1, 1 << (m + pad), 4):      # x = 1 mod 4  <=>  h(x) = 1
        e, h, xn = block(x)
        if e + h - 1 > pad:
            continue
        out.append((x & mask, xn & mask, e, h))
    return out


def edges(raw, hcap):
    E = defaultdict(dict)
    for u, v, e, h in raw:
        if h > hcap:
            continue
        w = 11 * (e - 1) - 9 * h
        if v not in E[u] or w < E[u][v]:
            E[u][v] = w
    return E


def karp_min_mean(E):
    """Karp's minimum mean cycle. Returns (mean, n_nodes, n_edges)."""
    nodes = sorted(set(E) | {v for d in E.values() for v in d})
    idx = {u: i for i, u in enumerate(nodes)}
    N = len(nodes)
    INF = float("inf")
    d = [[INF] * N for _ in range(N + 1)]
    for i in range(N):
        d[0][i] = 0
    for k in range(1, N + 1):
        dk, dp = d[k], d[k - 1]
        for u, outs in E.items():
            du = dp[idx[u]]
            if du == INF:
                continue
            for v, w in outs.items():
                iv = idx[v]
                if du + w < dk[iv]:
                    dk[iv] = du + w
    best = INF
    for v in range(N):
        if d[N][v] == INF:
            continue
        worst = float("-inf")
        for k in range(N):
            if d[k][v] == INF:
                continue
            worst = max(worst, (d[N][v] - d[k][v]) / (N - k))
        if worst > float("-inf"):
            best = min(best, worst)
    return best, N, sum(len(x) for x in E.values())


def report_mmc(ms=(6, 8, 10), pad=12):
    print("C. minimum mean cycle of Delta = 11(e-1) - 9h on the block automaton")
    print("   a POSITIVE value would close the gap uniformly in n; it is negative")
    print("   and independent of m, so no modulus closes the case bash.")
    print()
    print("   %-4s %-8s %-9s %s" % ("m", "states", "edges", "min mean cycle"))
    for m in ms:
        R = raw_transitions(m, pad)
        mm, N, ne = karp_min_mean(edges(R, hcap=pad - 1))
        print("   %-4d %-8d %-9d %+.4f" % (m, N, ne, mm))
    print()
    print("   restricted landings (m = %d):" % ms[-1])
    R = raw_transitions(ms[-1], pad)
    for hcap in (2, 3, 4, 5, 6, 8):
        mm, N, ne = karp_min_mean(edges(R, hcap))
        print("     h <= %d : %+8.4f" % (hcap, mm))
    print("   (h<=2 gives -7 = 11 - 18, on the cycle whose 2-adic fixed point")
    print("    is x = -7 -- REPLOW3's ghost. Excising that ball does not help.)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=6001)
    ap.add_argument("--mmc", action="store_true",
                    help="also run the minimum-mean-cycle diagnostic (slow)")
    a = ap.parse_args()

    vals = scan(a.limit)
    report_threshold(vals)
    report_windows(vals)
    if a.mmc:
        report_mmc()
    else:
        print("C. skipped (pass --mmc to run the block-automaton diagnostic)")


if __name__ == "__main__":
    main()
