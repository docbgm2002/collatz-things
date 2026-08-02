#!/usr/bin/env python3
"""Diagnostics for docs/no-go/avenue_a_mean_valuation_route.md.

Exploratory. Reproduces the four measurements in that note:

  A. the mean-valuation reformulation of the Avenue A score
     (rest >= 0  <=>  t / rho_t >= 20/11), on both windows, and the
     complete list of odd n below threshold on each;
  B. dyadic-window minima of E_K / K_down, showing the margin grows;
  C. minimum mean cycle of Delta = 11(e-1) - 9h on the block automaton
     mod 2^m: negative and m-independent, so no modulus closes the
     case bash (the method no-go of the note, §3);
  D. the disjunctive cut DISJ (§4): the finite misses of the t = 5n-2
     and t = 6n windows are disjoint;
  F1. cylinder-plateau lengths on the ACTUAL a_n towers, which refute
     the retracted PCD9/PCD10 route of §5.

Exact integer / Fraction arithmetic throughout; reported ratios are
measurements, not claims.

Usage:
    python3 scripts/explore_mean_valuation_gap.py [--limit 601] [--mmc] [--f1]
"""

import argparse
from collections import defaultdict
from fractions import Fraction

THRESHOLD = Fraction(20, 11)


def v2(x: int) -> int:
    return (x & -x).bit_length() - 1


# ----------------------------------------------------------------- A, B, D

def rho_window(n: int, t: int) -> int:
    """Odd-step count of the Terras shortcut map over t steps from a_n."""
    x = (3 ** n - 1) // 2
    r = 0
    for _ in range(t):
        if x & 1:
            x = (3 * x + 1) >> 1
            r += 1
        else:
            x >>= 1
    return r


def first_descent(n: int):
    """(K_down, E_K) for the odd-indexed repunit tail a_n."""
    x = (3 ** n - 1) // 2
    target = 2 ** n - 1
    K = E = 0
    while x >= target:
        e = v2(3 * x + 1)
        x = (3 * x + 1) >> e
        E += e
        K += 1
    return K, E


def report_reformulation(limit: int):
    print("A. mean-valuation reformulation")
    print("   rest >= 0  <=>  rho_t <= (11/20) t  <=>  t/rho_t >= 20/11 = %.6f"
          % float(THRESHOLD))
    print()
    bad6 = [n for n in range(3, min(limit, 401) + 1, 2)
            if Fraction(6 * n, rho_window(n, 6 * n)) < THRESHOLD]
    print("   window t = 6n     : odd n below threshold =", bad6)
    print("     (expected {5, 11}: n=11 is the unique 911-6-strong miss,")
    print("      n=5 handled direct, n=17 is the equality case)")

    badK = [n for n in range(3, limit + 1, 2)
            if Fraction(*reversed(first_descent(n))) < THRESHOLD]
    print("   first-descent E_K/K: odd n below threshold =", badK)
    print("     (expected {5, 17, 23}: exactly the 5n-2 even-budget")
    print("      saturations; n=23 is the unique 911 miss)")
    print()


def report_windows(limit: int):
    vals = {}
    for n in range(3, limit + 1, 2):
        K, E = first_descent(n)
        vals[n] = Fraction(E, K)
    print("B. dyadic-window minima of E_K / K_down")
    print("   %-16s %7s  %-10s %7s  %s" % ("window", "count", "min", "argmin", "margin"))
    lo, top = 8, max(vals)
    while lo <= top:
        hi = min(2 * lo, top + 1)
        sub = [(r, n) for n, r in vals.items() if lo <= n < hi]
        if sub:
            r, n = min(sub)
            print("   [%5d,%5d)   %6d  %.6f  %6d   %+.6f"
                  % (lo, hi, len(sub), float(r), n, float(r - THRESHOLD)))
        lo = hi
    print("   (the minimum rises and settles near 1.93; the gap is marginal")
    print("    only at n <= 23, where the finite certificates saturate)")
    print()


def report_window_sweep(limit: int, cs=(5, 6, 7, 8, 9, 10, 12, 15)):
    """Section 5: the window t = c*n is a free parameter for c > 4.5605."""
    print("E. window sweep (note §5): t = c*n is a valid cut for every c > 4.5605")
    print("   the note uses c = 5, 6 -- the tightest end, where margins vanish")
    print()
    print("   %-4s %-13s %-8s %-15s %s" % ("c", "min margin", "argmin", "min over n>=25", "exceptions"))
    for c in cs:
        rows = [(Fraction(c * n, rho_window(n, c * n)) - THRESHOLD, n)
                for n in range(5, limit + 1, 2)]
        m, am = min(rows)
        tail = [r for r in rows if r[1] >= 25]
        m2, am2 = min(tail) if tail else (m, am)
        exc = [n for r, n in rows if r <= 0]
        print("   %-4d %+.6f    %-8d %+.6f       %s"
              % (c, float(m), am, float(m2), exc if exc else "NONE"))
    print()
    print("   CAUTION (note §5.3): the cap at window cn ASSERTS a descent depth")
    print("     log2 x_t <= n(log2 3 - 0.12827 c)")
    print("   so c is bounded ABOVE as well as below:")
    print("     c > 4.5605  : else weaker than 'below M_n' and the cut is invalid")
    print("     c < 12.3565 : else the cap asserts descent to O(1) = Collatz for a_n")
    print("   and empirically sigma_1(n) ~ 7.64 n, so for c >~ 7.6 the measured")
    print("   margin is borrowed from the trivial 1->2->1 tail, not from descent.")
    print("   The margin is NOT monotone in c: fill in c=7,8,9 below and see.")
    print()


def report_envelope(limit: int = 301, cs=(5, 6, 8, 10, 15, 20)):
    """Section 5.2: the exact envelope of Lemma SD-K-density-c.

    U^t(a_n)/T <= (a_n/T) (3^rho / 2^t) (1 + 1/(3T))^rho  at the score cap
    rho = floor(11cn/20), with the correction bounded exactly by
    (1+x)^rho <= 1/(1 - rho x).  All Fraction arithmetic.
    """
    def envelope(n, c):
        t, rho, T = c * n, (11 * c * n) // 20, 2 ** n - 1
        x = Fraction(1, 3 * T)
        assert rho * x < 1
        return (Fraction(3 ** n - 1, 2) / T * Fraction(3 ** rho, 2 ** t)
                / (1 - rho * x))

    print("G. exact envelope (note §5.2): is U^t(a_n)/T < 1 at the score cap?")
    print("   %-5s %-12s %-9s %s" % ("c", "holds n<=%d" % limit, "worst n", "worst value"))
    for c in cs:
        rows = [(envelope(n, c), n) for n in range(7, limit + 1, 2)]
        v, n = max(rows)
        print("   %-5d %-12s %-9d %.4e"
              % (c, "YES" if all(r < 1 for r, _ in rows) else "NO", n, float(v)))
    print()
    print("   uniform certificate at c=15, odd n>=7:")
    print("     U^t(a_n)/T < (16/27) lambda^n,  lambda = 3^(37/4)/2^16")
    print("     since (64/127)(381/324) = 16/27 exactly  [381 = 3*127]")
    print("     3^37 = %d" % 3 ** 37)
    print("     2^64 = %d" % 2 ** 64)
    print("     3^37 < 2^64 : %s  (factor %.2f)" % (3 ** 37 < 2 ** 64, 2 ** 64 / 3 ** 37))
    print("     => lambda = %.6f < 0.396, bound at n=7 is %.3e < 1"
          % ((3 ** 37 / 2 ** 64) ** 0.25, 16 / 27 * (3 ** 37 / 2 ** 64) ** 1.75))
    print()


def report_bakex2(cs=(6, 10, 15, 20, 30, 50)):
    """Section 5.1: W9-B's crossover N0(c) under the hypothesis K_down <= c*n.

    Rerun of W9 §3.2 with c in place of 6.  q = i + B <= (c+2)n, so Rhin (R)
    gives (log2)||q.theta|| >= (2.085(c+2)n)^-13.3, against
    (log2)Delta <= A(c) n / 2^n.  N0(c) is the least n with
        2^n > A(c) n (2.085 (c+2) n)^13.3.
    The c=6 row must reproduce W9's published A=3, k=16.68, N0=161.
    """
    import math

    def A(c):
        return math.ceil((c / 3) * 1.004 + 0.0753)

    print("F. BAKEX2 crossover N0(c) under K_down <= c*n  (rerun of W9-B)")
    print("   %-5s %-6s %-12s %-8s %s" % ("c", "A(c)", "2.085(c+2)", "N0(c)", "inside W9-A (n<=501)?"))
    for c in cs:
        a, k = A(c), 2.085 * (c + 2)
        n = 9
        while n - math.log2(a * n) - 13.3 * math.log2(k * n) <= 0:
            n += 1
        note = "  <-- reproduces W9" if c == 6 else ""
        print("   %-5d %-6d %-12.3f %-8d %s%s"
              % (c, a, k, n, "YES" if n <= 501 else "no", note))
    print("   N0(c) ~ 161 + 14.3*log2(c/6): the crossover grows only")
    print("   logarithmically, so the choice of 6n was never forced by Baker.")
    print("   At c=15: crossover 178; the 17 values 161<=n<=177 are already")
    print("   covered by W9-A's finite certificate. Nothing left over.")
    print()


def report_disjunction(limit: int):
    print("D. disjunctive cut DISJ: do the two windows' misses overlap?")
    rows, both = [], []
    for n in range(7, limit + 1, 2):
        mA = Fraction(6 * n, rho_window(n, 6 * n)) - THRESHOLD
        mB = Fraction(5 * n - 2, rho_window(n, 5 * n - 2)) - THRESHOLD
        if max(mA, mB) <= 0:
            both.append(n)
        rows.append((max(mA, mB), n, mA, mB))
    rows.sort()
    print("   odd 7 <= n <= %d failing BOTH windows: %s" % (limit, both or "none"))
    print("   five tightest:   n    margin(6n)   margin(5n-2)       max")
    for m, n, a, b in rows[:5]:
        print("                 %5d   %+.6f    %+.6f   %+.6f"
              % (n, float(a), float(b), float(m)))
    print("   (n=17 and n=11 are each rescued by the other cut)")
    print()


# --------------------------------------------------------------------- F1

def report_f1(ns=(131, 471, 1197, 2349, 4401)):
    print("F1. cylinder-plateau lengths on the ACTUAL a_n towers")
    print("    n_m = least odd representative of the class realising the first m")
    print("    valuations = n mod 2^{E_m}  (PCD9). Plateau = run of constant n_m.")
    print()
    print("    %-7s %-8s %-8s %-12s %s" % ("n", "K_down", "E_K", "m*(n_m=n)", "longest plateau"))
    for n in ns:
        x = (3 ** n - 1) // 2
        target = 2 ** n - 1
        E = 0
        tower = []
        while x >= target:
            e = v2(3 * x + 1)
            x = (3 * x + 1) >> e
            E += e
            tower.append(n % (1 << E) if E < n.bit_length() + 2 else n)
        runs, cur = [], 1
        for i in range(1, len(tower)):
            if tower[i] == tower[i - 1]:
                cur += 1
            else:
                runs.append(cur)
                cur = 1
        runs.append(cur)
        mstar = next(i + 1 for i, v in enumerate(tower) if v == n)
        print("    %-7d %-8d %-8d %-12d %d" % (n, len(tower), E, mstar, max(runs)))
    print()
    print("    Plateaus are Theta(n), not Theta(log n): once 2^{E_m} > n, the")
    print("    exponent is trivially its own least representative forever.")
    print("    PCD10 constrains which n realise a PRESCRIBED word; it says")
    print("    nothing about the word an n actually produces. Route retracted.")
    print()


# ---------------------------------------------------------------------- C

def block(x: int):
    """One Avenue A block from odd x with h(x)=1. Returns (e, h, x_next)."""
    e = v2(3 * x + 1)
    y = (3 * x + 1) >> e
    h = v2(y + 1)
    if h == 1:
        return e, h, y
    return e, h, 3 ** (h - 1) * ((y + 1) >> (h - 1)) - 1


def raw_transitions(m: int, pad: int):
    """Transitions on states x mod 2^m from explicit lifts.

    Only outcomes determined by the enumerated bits are kept, so every
    edge is realizable: this UNDER-approximates the edge set, the
    conservative direction for exhibiting a bad cycle.
    """
    mask = (1 << m) - 1
    out = []
    for x in range(1, 1 << (m + pad), 4):      # x = 1 mod 4 <=> h(x) = 1
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
    print("   a POSITIVE value would close the gap uniformly in n. It is")
    print("   negative and independent of m: no modulus closes the case bash.")
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
    print("   (h<=2 gives -7 = 11-18, on the cycle whose 2-adic fixed point is")
    print("    x = -7, REPLOW3's ghost. Excising that ball does not help.)")
    print()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=601)
    ap.add_argument("--mmc", action="store_true", help="run the block-automaton no-go (slow)")
    ap.add_argument("--f1", action="store_true", help="run the plateau falsifier F1 (slow)")
    a = ap.parse_args()

    report_reformulation(a.limit)
    report_windows(a.limit)
    report_disjunction(a.limit)
    report_window_sweep(min(a.limit, 401))
    report_envelope(min(a.limit, 301))
    report_bakex2()
    if a.f1:
        report_f1()
    if a.mmc:
        report_mmc()
    if not (a.f1 or a.mmc):
        print("(pass --mmc for the modulus no-go, --f1 for the plateau falsifier)")


if __name__ == "__main__":
    main()
