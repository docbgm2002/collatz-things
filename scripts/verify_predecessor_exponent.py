#!/usr/bin/env python3
"""
verify_predecessor_exponent.py
==============================

Rigorous certificate for a lower bound on the number of 3x+1 predecessors:

    for every a >= 3 not lying on a cycle of T and every X >= a,
        #{n <= X : the T-orbit of n passes through a}  >=  c_k v_{a mod 3^k} (X/a)^gamma - 1,

with gamma = GAMMA, c_k = 2^{-gamma} / max v, and v the certified vector.
In particular #{n <= X : n reaches 1} >= c (X/4)^gamma - 1.

The mathematics (docs/density-cycles/predecessor_exponent.md): the predecessor
tree above a non-cyclic a, restricted to [1, X], is a finite forest in which
each node p has children 2p (if <= X) and b(p) = (2p-1)/3 (if p = 2 mod 3).
The function u(p) = max(0, c v_{m(p)} (X/p)^gamma - 1) is a subsolution of
the exact recursion  g(p) = 1 + g(2p) + g(b(p))  provided the vector
inequalities

    (S)  v_m <= 2^{-gamma} v_{2m} + (3/2)^gamma * min_{j<3} v_{c_j(m)}   (m = 2 mod 3, child class a unit)
         v_m <= 2^{-gamma} v_{2m}                                        (otherwise)

hold for every unit class m modulo 3^k, where c_j(m) = (2m-1)/3 + j 3^{k-1}.
A subsolution of a nilpotent monotone recursion is dominated by its solution.

This script checks (S) EXACTLY.  The vector is scaled to integers V_m (the
subsolution principle is homogeneous, so scaling is free), and the two
irrational coefficients are replaced by rational lower bounds A <= 2^{-gamma},
B <= (3/2)^gamma with denominator 2^SHIFT; the checked inequality
     V_m * 2^SHIFT <= A_num V_{2m} + B_num min_j V_{c_j}
implies (S) because it is stronger.  All arithmetic is in Python integers
(or int64 where the products provably fit).

Usage:
    python3 scripts/verify_predecessor_exponent.py --k 11 --gamma 0.8300 [--iters 2000]
    python3 scripts/verify_predecessor_exponent.py --k 13 --gamma 0.8420 --npz vector.npz

Without --npz the vector is recomputed by power iteration at the given gamma
(floats, guidance only); the exact check is what counts.  Exit 0 and ALL PASS
iff the certificate is valid; the printed exponent is then a theorem.
"""

import argparse
import sys
import time
from decimal import Decimal, getcontext

import numpy as np

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from explore_predecessor_exponent import build, apply  # noqa: E402

getcontext().prec = 60


def rational_lower(x: Decimal, shift: int) -> int:
    """floor(x * 2^shift) as an integer (a lower bound numerator)."""
    scaled = x * (Decimal(2) ** shift)
    return int(scaled.to_integral_value(rounding="ROUND_FLOOR"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, required=True)
    ap.add_argument("--gamma", type=str, required=True, help="decimal string, e.g. 0.8300")
    ap.add_argument("--iters", type=int, default=2000)
    ap.add_argument("--npz", default=None)
    ap.add_argument("--shift", type=int, default=28, help="bits of precision for coefficients and vector")
    ap.add_argument("--count-check", action="store_true", help="also count predecessors of 4 up to 2^22 by BFS")
    args = ap.parse_args()

    k = args.k
    gamma_dec = Decimal(args.gamma)
    gamma = float(gamma_dec)
    t0 = time.time()
    units, two, is2, child_unit, cidx = build(k)
    n = len(units)
    print(f"k={k}: {n} unit classes modulo 3^{k}; gamma = {args.gamma}")

    # --- float vector (guidance) ---
    if args.npz:
        d = np.load(args.npz)
        v = d["v"]
        assert len(v) == n
    else:
        v = np.ones(n)
    for it in range(args.iters):
        w = apply(v, gamma, two, child_unit, cidx)
        v = w / w.max()
    w = apply(v, gamma, two, child_unit, cidx)
    ratios = w / v
    print(f"  power iteration: min A(v)/v = {ratios.min():.10f}, max = {ratios.max():.10f}  ({time.time()-t0:.1f}s)")
    if ratios.min() < 1.0:
        # one more smoothing: use w itself (A is monotone; if A v >= (1-e) v, then A w >= ...)
        pass

    # --- exact check ---
    S = args.shift
    scale = 1 << S
    # integer vector; keep it positive on every unit class
    V = np.floor(v * scale).astype(np.int64)
    if V.min() <= 0:
        print("  [FAIL] vector has a non-positive entry after scaling; increase --shift")
        sys.exit(1)
    A_num = rational_lower(Decimal(2) ** (-gamma_dec), S)      # <= 2^{-gamma} * 2^S
    B_num = rational_lower((Decimal(3) / 2) ** gamma_dec, S)   # <= (3/2)^gamma * 2^S
    # sanity on the Decimal power evaluation: compare against float
    assert abs(float(A_num) / scale - 2.0 ** (-gamma)) < 2.0 ** (1 - S)
    assert abs(float(B_num) / scale - 1.5 ** gamma) < 2.0 ** (1 - S)
    # products: V < 2^S * ... ; V <= 2^S, A_num, B_num < 2^(S+1): products < 2^(2S+1) <= 2^57 for S = 28 -> fits int64
    assert 2 * S + 2 <= 62
    lhs = V * scale
    rhs = A_num * V[two]
    m3 = np.minimum(np.minimum(V[cidx[:, 0]], V[cidx[:, 1]]), V[cidx[:, 2]])
    rhs = rhs + np.where(child_unit, B_num * m3, 0)
    bad = np.flatnonzero(lhs > rhs)
    slack = (rhs - lhs).min() / scale / V.max()
    if len(bad):
        print(f"  [FAIL] {len(bad)} of {n} vector inequalities fail; worst relative slack {slack:.3e}")
        print("         first failures at classes", units[bad[:5]].tolist())
        sys.exit(1)
    print(f"  [PASS] all {n} inequalities (S) hold exactly with coefficients rounded down; min slack {slack:.3e}")
    vmax = V.max()
    v4 = V[np.flatnonzero(units == 4 % 3 ** k)[0]]
    # c = 2^{-gamma} / vmax  (in the scaled normalization, v_m -> V_m / vmax)
    print(f"  Theorem: for all non-cyclic a >= 3, a not = 0 mod 3, and X >= a:")
    print(f"     #{{n <= X reaching a}} >= 2^(-gamma) * (V_a/V_max) * (X/a)^gamma - 1,   V_a/V_max >= {V.min()/vmax:.3e}")
    print(f"  For a = 4: #{{n <= X reaching 1}} >= {2.0**(-gamma) * v4 / vmax:.4e} * (X/4)^{args.gamma} - 1")

    if args.count_check:
        # empirical cross-check of the inequality for a = 4 (not part of the proof)
        X = 1 << 22
        from collections import deque
        seen = 0
        dq = deque([4])
        while dq:
            p = dq.popleft()
            seen += 1
            if 2 * p <= X:
                dq.append(2 * p)
            if p % 3 == 2:
                b = (2 * p - 1) // 3
                if b >= 1:
                    dq.append(b)
        bound = 2.0 ** (-gamma) * v4 / vmax * (X / 4) ** gamma - 1
        print(f"  count check: predecessors of 4 up to 2^22 = {seen}; certified bound {bound:.1f}; ratio {seen/bound:.1f}")
        assert seen >= bound
    print("ALL PASS")


if __name__ == "__main__":
    main()
