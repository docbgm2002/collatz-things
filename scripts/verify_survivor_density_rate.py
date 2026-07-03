#!/usr/bin/env python3
"""
Exact first-passage computation of the descent-tree survivor density.

RESULT: Conjecture 1 of descent_tree_survivors.md (dens(S_K) <= rho^K) is
FALSE. In the exact natural-density (walk) formulation the bound holds for
K <= 194 and first fails at K = 195 (confirmed in exact rational
arithmetic); the ratio dens/rho^K then grows without bound (1.24 by K=210,
4.6 by K=300), so the residue-count formulation fails by K ~ 200 at the
latest regardless of the <=0.5% formulation discrepancy observed at small K.
The corrected conjectured rate is rho^(1/theta) = e^(-I(theta)/theta)
= 0.965907..., the Mogulskii first-passage rate.

Walk model (exact by Lemma 3 of stopping_time_density.md):
e_i i.i.d. with P(e=v)=2^-v (v>=1), E_j = e_0+...+e_{j-1}.
Crossing at step j >= 1 iff E_j >= theta*j + 1 (theta = log2 3).
Survivor at budget K iff the walk exceeds E=K before or at the first crossing,
i.e. it stays strictly below the line while E <= K.

dens(S_K) (natural density over odd integers) equals this probability exactly.
Conjecture 1 of descent_tree_survivors.md claims dens(S_K) <= rho^K with
rho = e^{-I(log2 3)} = 0.946507...  The Mogulskii-type heuristic instead
predicts asymptotic rate rho^(1/theta) ~= 0.9659 > rho, so the conjecture
should FAIL at some finite K. This script finds out.

Cross-check: for K = 6..20 compare against direct enumeration of odd
residues mod 2^K using the same discharge rule as verify_tree_survivors.py.
"""
import math
from fractions import Fraction

THETA = math.log2(3.0)


def crossing(E, j):
    """E_j >= theta*j + 1, matching verify_tree_survivors.py's comparison.
    Exact since theta*j+1 is never an integer (theta irrational): use the
    integer test E-1 >= theta*j  <=>  2^(E-1) >= 3^j."""
    return 2 ** (E - 1) >= 3 ** j


def survivor_density_dp(K, exact=False):
    """P(survivor at budget K) by forward DP over states (j, E),
    E <= K, uncrossed. Returns float (or Fraction if exact=True)."""
    half = Fraction(1, 2) if exact else 0.5
    one = Fraction(1) if exact else 1.0
    # cur[E] = prob of being at (j, E) uncrossed with E <= K
    cur = {0: one}
    surv = one - one  # zero of the right type
    j = 0
    while cur:
        nxt = {}
        for E, p in cur.items():
            # jump v = 1 .. K-E lands within budget
            pv = p * half
            for v in range(1, K - E + 1):
                E2 = E + v
                if not crossing(E2, j + 1):
                    nxt[E2] = nxt.get(E2, one - one) + pv
                # else discharged: drop
                pv *= half
            # jump v >= K-E+1 exceeds budget -> survivor
            # P(e >= K-E+1) = 2^-(K-E)
            surv += p * (half ** (K - E))
        cur = nxt
        j += 1
        if j > K + 1:
            break
    return surv


def v2(n):
    return (n & -n).bit_length() - 1


def enumerate_density(K, jmax=5000):
    """Direct enumeration matching verify_tree_survivors.py."""
    count = 0
    for r in range(1, 2 ** K, 2):
        E = 0
        cur = r
        surv = True
        for j in range(1, jmax):
            t = 3 * cur + 1
            e = v2(t)
            cur = t >> e
            E += e
            if crossing(E, j):
                surv = E > K
                break
        if surv:
            count += 1
    return count / 2 ** (K - 1)


def cramer_rho():
    th = THETA
    u = 2 * (th - 1) / th
    I = (th - 1) * math.log(u) + math.log(2 - u)
    return math.exp(-I), I


def main():
    rho, I = cramer_rho()
    rho1 = math.exp(-I / THETA)
    print(f"rho        = {rho:.6f}   (conjectured rate in TREE2)")
    print(f"rho^(1/th) = {rho1:.6f}   (Mogulskii first-passage heuristic)")
    print()
    print("== cross-check DP vs enumeration, K=6..16 ==")
    print(f"{'K':>3} {'enum':>10} {'DP':>10} {'ratio':>8}")
    for K in range(6, 17):
        de = enumerate_density(K)
        dd = survivor_density_dp(K)
        print(f"{K:3d} {de:10.6f} {dd:10.6f} {de/dd:8.4f}")
    print()
    print("== conjecture test: dens(S_K) vs rho^K ==")
    print(f"{'K':>4} {'dens_DP':>12} {'rho^K':>12} {'dens/rho^K':>11} "
          f"{'emp_rate':>9}")
    prev = None
    first_violation = None
    for K in list(range(10, 200, 5)):
        d = survivor_density_dp(K)
        r = rho ** K
        rate = (d / prev) ** (1 / 5) if prev is not None else float('nan')
        flag = "  <-- VIOLATION" if d > r else ""
        if d > r and first_violation is None:
            first_violation = K
        print(f"{K:4d} {d:12.6e} {r:12.6e} {d/r:11.4f} {rate:9.5f}{flag}")
        prev = d
    if first_violation is not None:
        # narrow down
        lo = first_violation - 5
        for K in range(lo, first_violation + 1):
            d = survivor_density_dp(K)
            if d > rho ** K:
                print(f"\nFirst violation at K = {K}: "
                      f"dens = {d:.6e} > rho^K = {rho**K:.6e}")
                # exact-arithmetic confirmation
                de = survivor_density_dp(K, exact=True)
                print(f"Exact Fraction check: dens = {float(de):.6e} "
                      f"({'VIOLATION CONFIRMED' if float(de) > rho**K else 'no violation'})")
                break
    else:
        print("\nNo violation found up to K=195.")


if __name__ == "__main__":
    main()
