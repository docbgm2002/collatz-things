#!/usr/bin/env python3
"""
Verification for "The Descent-Tree Survivors Are the Spine".

Ties together verify_descent_tree.py (the branching certificate), the
stopping-time density theorem (stopping_time_density.md), and the spine notes:
finite survivor fractions through the tested depth, and the exact initial
Mersenne burn showing that the all-ones residue 2^K-1 survives each tested
depth. The script does not prove a universal rho^K bound.

Exact integer arithmetic; rho is the Cramer rate from stopping_time_density.md.
"""
import math

THETA = math.log2(3)
RHO = 0.9465                      # e^{-I(log2 3)}, see stopping_time_density.md


def v2(n):
    return (n & -n).bit_length() - 1 if n else 10 ** 9


def tau(x):
    return v2(x + 1)


def f(x):
    t = 3 * x + 1
    return t >> v2(t)


def discharge_level(r, jmax=5000):
    """Cumulative valuation E_j at the first step where descent is forced
       (E_j >= theta*j + 1). This many low bits suffice to discharge the
       whole class r mod 2^(that level)."""
    E = 0
    cur = r
    for j in range(1, jmax):
        t = 3 * cur + 1
        e = v2(t)
        cur = t >> e
        E += e
        if E >= THETA * j + 1:
            return E
    return None


def survivors(K):
    """Odd residues mod 2^K not discharged by their first K bits."""
    out = []
    for r in range(1, 2 ** K, 2):
        L = discharge_level(r)
        if L is None or L > K:
            out.append(r)
    return out


def check_density_bound(Klo=6, Khi=20):
    print("== finite survivor-fraction certificate ==")
    print(f"   {'K':>3} {'survivors':>9} {'frac':>8} {'rho^K':>8} "
          f"{'mean_tau':>8} {'max_tau':>7}")
    prev = 1.0
    for K in range(Klo, Khi + 1):
        S = survivors(K)
        frac = len(S) / 2 ** (K - 1)
        taus = [tau(r) for r in S]
        mt = sum(taus) / len(taus)
        assert frac <= RHO ** K, (K, frac, RHO ** K)        # density bound
        assert frac <= prev + 1e-12                          # non-increasing
        prev = frac
        print(f"   {K:3d} {len(S):9d} {frac:8.4f} {RHO**K:8.4f} {mt:8.2f} {max(taus):7d}")
    print(f"   PASS  frac(S_K) <= rho^K and non-increasing for K={Klo}..{Khi}")


def check_spine_anchor(Khi=22):
    """The all-ones residue 2^K-1 survives every depth (it is the unique
       minimal-valuation orbit: it burns with e_i=1, so E_j=j < theta*j+1)."""
    for K in range(3, Khi + 1):
        r = 2 ** K - 1
        L = discharge_level(r)
        assert L is None or L > K, (K, L)         # never discharged by K bits
        # the burn gives E_j = j for the first K-1 steps
        E = 0
        cur = r
        for j in range(1, K):
            t = 3 * cur + 1
            e = v2(t)
            cur = t >> e
            E += e
            assert E == j, (K, j, E)              # all valuations are 1
    print(f"   PASS  2^K-1 survives every depth K<=22; burn has E_j=j (all e_i=1)")


def check_high_fuel(K=12):
    """Survivors are valuation-deficient = high trailing-one fuel. Show the
       mean tau of survivors exceeds the mean tau over all odd residues."""
    S = survivors(K)
    mean_surv = sum(tau(r) for r in S) / len(S)
    mean_all = sum(tau(r) for r in range(1, 2 ** K, 2)) / 2 ** (K - 1)
    assert mean_surv > mean_all + 0.3, (mean_surv, mean_all)
    # the extreme survivors cluster at the top of the fuel scale
    top = sorted(S, key=tau, reverse=True)[:5]
    print(f"   PASS  K={K}: mean tau survivors={mean_surv:.2f} vs all={mean_all:.2f}; "
          f"top-fuel survivors tau={[tau(r) for r in top]}")


if __name__ == "__main__":
    check_density_bound()
    print()
    check_spine_anchor()
    check_high_fuel()
    print("\nAll checks passed.")
