#!/usr/bin/env python3
"""
verify_nogo_certificate.py
==========================

Independent certificate miner for one-step potentials
    Phi(x) = log_2 x + g(coords(x)).

The constraint "Phi nonincreasing along f" restricted to the observed steps
x -> f(x), odd x <= LIMIT, is the difference-constraint system

    g(coords(f(x))) - g(coords(x)) <= -log_2( f(x) / x ).

It is infeasible iff the coordinate digraph (one node per coordinate
vector, one edge per observed step with weight log x - log f(x)) contains a
directed cycle of negative total weight, i.e. a closed chain of witnesses
x_1, ..., x_K with coords(f(x_i)) = coords(x_{i+1}) and
prod f(x_i) > prod x_i.  Summing the K constraints along such a cycle
cancels every g-term and leaves prod f(x_i) <= prod x_i, a contradiction.

This script uses NO lemma from the manuscript.  It only looks at raw orbit
steps.  Floats guide the Bellman-Ford search; every reported cycle is
re-confirmed in exact integer arithmetic (closure at each junction, and the
product comparison), and the script fails if the exact check does not hold.

Windows (coordinate vectors) mined by default:

    A4   (x mod 16, tau)                              Theorem A class, m = 4
    A4L  (x mod 16, tau, lambda_1)                    + level-1 detector
    A6   (x mod 64, tau, len)                         Theorem A class with len
    B    (x mod 16, tau, LD_3)                        Theorem B class, j = 3
    F3   (floor(8 log_2 x), tau, x mod 16)            Theorem F class, j = 3
    F5   (floor(32 log_2 x), tau, x mod 16)           Theorem F class, j = 5

Usage:  python3 scripts/verify_nogo_certificate.py [--limit 1000000] [--windows A4,A4L,...]
"""

import argparse
import math
import sys
from fractions import Fraction


def v2(n):
    return (n & -n).bit_length() - 1


def f(x):
    y = 3 * x + 1
    return y >> v2(y)


def tau(x):
    return v2(x + 1)


def LD(j, x):
    return x >> max(0, x.bit_length() - j)


def cell(Q, x):
    return (x ** Q).bit_length() - 1


def w_d(d, M):
    num = 2 ** (M + 2 * d) - 2 ** (2 * d + 1) + 3 ** d
    return num // 3 ** d


_TEMPLATES = {}


def lam(d, x, smax=12):
    """Level-d suffix detector of the manuscript (Definition of the detectors)."""
    if d not in _TEMPLATES:
        o = 2 * 3 ** (d - 1)
        _TEMPLATES[d] = [(w_d(d, 1 + o * s), 1 << (w_d(d, 1 + o * s).bit_length() + 1))
                         for s in range(1, smax + 1)]
    best = 0
    for s, (T, mod) in enumerate(_TEMPLATES[d], start=1):
        if x % mod == T % mod:
            best = s
    return best  # 0 encodes bottom


WINDOWS = {
    "A4": lambda x: (x % 16, tau(x)),
    "A4L": lambda x: (x % 16, tau(x), lam(1, x)),
    "A6": lambda x: (x % 64, tau(x), x.bit_length()),
    "B": lambda x: (x % 16, tau(x), LD(3, x)),
    "F3": lambda x: (cell(8, x), tau(x), x % 16),
    "F5": lambda x: (cell(32, x), tau(x), x % 16),
}


def mine(coords, limit):
    """Return a list of witnesses forming an exact gaining closed cycle, or None."""
    # edges: (u, v) -> best (smallest) weight and the witness x achieving it
    edges = {}
    nodes = {}

    def nid(c):
        if c not in nodes:
            nodes[c] = len(nodes)
        return nodes[c]

    for x in range(3, limit + 1, 2):
        y = f(x)
        u, v = nid(coords(x)), nid(coords(y))
        w = math.log(x) - math.log(y)  # negative when the step gains value
        key = (u, v)
        if key not in edges or w < edges[key][0]:
            edges[key] = (w, x)
    n = len(nodes)
    adj = [[] for _ in range(n)]
    for (u, v), (w, x) in edges.items():
        adj[u].append((v, w, x))
    # Bellman-Ford from a virtual source (dist 0 everywhere), with
    # predecessor tracking; a relaxation in round n signals a negative cycle.
    dist = [0.0] * n
    pred = [None] * n
    predx = [None] * n
    cyc_node = None
    for rnd in range(n + 1):
        changed = False
        for u in range(n):
            du = dist[u]
            for (v, w, x) in adj[u]:
                if du + w < dist[v] - 1e-15:
                    dist[v] = du + w
                    pred[v] = u
                    predx[v] = x
                    changed = True
                    cyc_node = v
        if not changed:
            return None
    # walk predecessors back n times to land inside the cycle
    v = cyc_node
    for _ in range(n):
        v = pred[v]
    cycle_nodes = [v]
    u = pred[v]
    while u != v:
        cycle_nodes.append(u)
        u = pred[u]
    cycle_nodes.reverse()
    witnesses = [predx[cycle_nodes[(i + 1) % len(cycle_nodes)]] for i in range(len(cycle_nodes))]
    return witnesses


def confirm(coords, witnesses):
    """Exact check: closure at every junction and strict product gain."""
    K = len(witnesses)
    num, den = 1, 1
    for i, x in enumerate(witnesses):
        y = f(x)
        if coords(y) != coords(witnesses[(i + 1) % K]):
            return False, None
        num *= y
        den *= x
    return num > den, Fraction(num, den)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=1_000_000)
    ap.add_argument("--windows", default=",".join(WINDOWS))
    args = ap.parse_args()
    failures = 0
    for name in args.windows.split(","):
        coords = WINDOWS[name]
        wit = mine(coords, args.limit)
        if wit is None:
            print(f"[{name:4}] no gaining cycle found among odd x <= {args.limit} (FEASIBLE on this window)")
            failures += 1
            continue
        ok, ratio = confirm(coords, wit)
        chain = ", ".join(f"{x}->{f(x)}" for x in wit)
        print(f"[{name:4}] {'INFEASIBLE' if ok else 'BAD CYCLE'}: length {len(wit)} cycle {chain}; "
              f"ratio product {ratio.numerator}/{ratio.denominator}")
        if not ok:
            failures += 1
    if failures:
        print("FAIL")
        sys.exit(1)
    print("ALL PASS: every window carries an exactly confirmed gaining cycle")


if __name__ == "__main__":
    main()
