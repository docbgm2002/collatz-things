#!/usr/bin/env python3
"""
explore_predecessor_exponent.py
===============================

Krasikov-type difference inequalities for the predecessor tree of the 3x+1
map, with variables attached to the unit residue classes modulo 3^k, and the
exponent they imply.  This is the exploratory solver; the rigorous
certificate check is in verify_predecessor_exponent.py.

Setting (T-map).  For a >= 3 not in a cycle let P(a) be the set of integers
whose T-orbit passes through a, and pi_a(X) = #{n <= X : n in P(a)}.  The
immediate predecessors of a are 2a (always) and b(a) = (2a-1)/3 (when
a = 2 mod 3; b(a) is then odd), with disjoint predecessor trees, so

    pi_a(X) = 1 + pi_{2a}(X) + [a = 2 mod 3] pi_{b(a)}(X)       (a <= X).

If a = m (mod 3^k) then 2a = 2m (mod 3^k) and b(a) = (2m-1)/3 (mod 3^{k-1}),
so b(a) lies in one of three classes modulo 3^k.  For a = 0 mod 3 the tree
above a is {2^j a}: linear growth only.

Subsolution principle.  Fix gamma in (0,1) and a vector v >= 0 on the unit
classes mod 3^k (v = 0 on classes divisible by 3) with

    v_m <= 2^{-gamma} v_{2m} + (3/2)^gamma * min_j v_{c_j(m)}   (m = 2 mod 3)
    v_m <= 2^{-gamma} v_{2m}                                     (m = 1 mod 3)

where c_j(m) = (2m-1)/3 + j*3^{k-1}.  Then u(a) = max(0, c v_m (X/a)^gamma - C)
is a subsolution of the recursion on [1, X] for small c, C, and since the
predecessor relation restricted to [1, X] is a finite forest (nilpotent),
pi_a(X) >= u(a).  Hence pi_a(X) >= c v_m (X/a)^gamma - C for every a <= X in
a unit class: at least c' X^gamma integers below X reach a.

The best exponent gamma_k is the largest gamma admitting such a v > 0; it is
found by bisection on gamma with nonlinear power iteration of the monotone,
concave, degree-1 homogeneous map  A_gamma(v)_m = RHS above.

Usage:  python3 scripts/explore_predecessor_exponent.py --kmax 12 [--iters 400]
Prints gamma_k for k = 2..kmax and writes the normalized vector for the
largest k to scratch (optional --save).
"""

import argparse
import math
import sys
import time

import numpy as np


def build(k):
    """Index arrays for the unit classes modulo 3^k."""
    M = 3 ** k
    units = np.arange(M, dtype=np.int64)
    units = units[units % 3 != 0]  # 2*3^(k-1) of them
    pos = -np.ones(M, dtype=np.int64)
    pos[units] = np.arange(len(units))
    two = pos[(2 * units) % M]
    is2 = (units % 3 == 2)
    # odd child class (2m-1)/3 mod 3^(k-1), lifted to three classes mod 3^k
    c = np.zeros(len(units), dtype=np.int64)
    c[is2] = ((2 * units[is2] - 1) // 3) % (3 ** (k - 1))
    cj = np.stack([(c + j * 3 ** (k - 1)) % M for j in range(3)], axis=1)
    child_unit = (c % 3 != 0) & is2
    cidx = np.where(child_unit[:, None], pos[cj], 0)  # index 0 is a dummy when unused
    return units, two, is2, child_unit, cidx


def apply(v, gamma, two, child_unit, cidx):
    a = 2.0 ** (-gamma)
    b = 1.5 ** gamma
    w = a * v[two]
    m = np.minimum(np.minimum(v[cidx[:, 0]], v[cidx[:, 1]]), v[cidx[:, 2]])
    w = w + np.where(child_unit, b * m, 0.0)
    return w


def growth(gamma, two, child_unit, cidx, iters=300, v0=None):
    """Cone spectral radius of A_gamma by power iteration; returns (rho, v)."""
    n = len(two)
    v = np.ones(n) if v0 is None else v0.copy()
    rho = 1.0
    for it in range(iters):
        w = apply(v, gamma, two, child_unit, cidx)
        s = w.max()
        if s <= 0:
            return 0.0, v
        v = w / s
        rho = s
    # Collatz-Wielandt style bounds: min and max of A(v)/v over support
    w = apply(v, gamma, two, child_unit, cidx)
    mask = v > 1e-300
    ratios = w[mask] / v[mask]
    return rho, v, ratios.min(), ratios.max()


def best_gamma(k, iters=300, tol=1e-6, verbose=False, lo=0.3, hi=1.0):
    units, two, is2, child_unit, cidx = build(k)
    v = None
    while hi - lo > tol:
        mid = 0.5 * (lo + hi)
        rho, vv, rmin, rmax = growth(mid, two, child_unit, cidx, iters=iters, v0=v)
        # feasible (v <= A v possible) iff rho >= 1; use rmin as the safe test
        if rmin >= 1.0:
            lo = mid
            v = vv
        elif rmax < 1.0:
            hi = mid
        else:
            # undecided at this iteration count: use rho
            if rho >= 1.0:
                lo = mid
                v = vv
            else:
                hi = mid
        if verbose:
            print(f"    k={k} gamma={mid:.6f} rho={rho:.6f} ratios=[{rmin:.6f},{rmax:.6f}]")
    return lo, v, units


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kmin", type=int, default=2)
    ap.add_argument("--kmax", type=int, default=12)
    ap.add_argument("--iters", type=int, default=300)
    ap.add_argument("--save", default=None, help="npz file for the vector at kmax")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--lo", type=float, default=0.3)
    ap.add_argument("--hi", type=float, default=1.0)
    ap.add_argument("--tol", type=float, default=1e-6)
    args = ap.parse_args()
    for k in range(args.kmin, args.kmax + 1):
        t0 = time.time()
        g, v, units = best_gamma(k, iters=args.iters, verbose=args.verbose, lo=args.lo, hi=args.hi, tol=args.tol)
        print(f"k={k:2d}  classes={len(units):9d}  gamma_k >= {g:.5f}   ({time.time()-t0:.1f}s)")
        sys.stdout.flush()
        if args.save and k == args.kmax:
            np.savez(args.save, k=k, gamma=g, v=v, units=units)


if __name__ == "__main__":
    main()
