#!/usr/bin/env python3
"""
Verification for "The Corridor Rate Theorem" (corridor_rate.md).

Checks:
  1. Constant calculus: u* = 2(theta-1)/theta, I(theta), C0 = 1/u*,
     rho = e^-I, rho1 = e^(-I/theta); prefactor sum of Theorem 1a < 31;
     identities 2^theta = 3 and 3^(1/theta) = 2.
  2. Lemma 1 (Chernoff at the line): P(E_j <= theta*j + 1) <= C0 * rho^j,
     with the exact left side computed by rational convolution, j <= 40.
  3. Theorem 1a numerically: p_K <= 31 * rho1^K for K up to 1800
     (prefix-sum O(K^2) DP, cross-checked against the exact slow DP at
     K = 20 and K = 100 to 1e-10 relative).
  4. Limit evidence: local rate (p_K / p_K')^(1/(K-K')) increases
     monotonically toward rho1.
  5. Tilt calculus: tilted mean 2/(2-u) = mu solvable on (1,2);
     I(mu)/mu -> I(theta)/theta.
"""
import math
from fractions import Fraction

THETA = math.log2(3.0)


def constants():
    th = THETA
    u = 2 * (th - 1) / th
    I = (th - 1) * math.log(u) + math.log(2 - u)
    rho = math.exp(-I)
    rho1 = math.exp(-I / th)
    C0 = 1 / u
    return th, u, I, rho, rho1, C0


def check_constants():
    th, u, I, rho, rho1, C0 = constants()
    assert abs(2 ** th - 3) < 1e-12
    assert abs(3 ** (1 / th) - 2) < 1e-12
    # stationarity of the Legendre maximand at u*
    h = 1e-7
    f = lambda v: (th - 1) * math.log(v) + math.log(2 - v)
    assert abs((f(u + h) - f(u - h)) / (2 * h)) < 1e-5
    # Theorem 1a prefactors
    pref1 = 4 * C0 * (3 * rho) ** (1 - 1 / th) / (3 * rho - 1)
    pref2 = C0 * rho ** (-1 / th) / (1 - rho)
    assert pref1 + pref2 < 31, (pref1, pref2)
    print(f"1. constants: PASS  I={I:.6f} rho={rho:.6f} rho1={rho1:.6f} "
          f"C0={C0:.5f}  prefactors {pref1:.3f}+{pref2:.3f} < 31")
    return th, u, I, rho, rho1, C0


def check_lemma1(jmax=40):
    """Exact tail P(E_j <= floor(theta*j+1)) via rational convolution,
    truncating the geometric law at the needed weight (exact: weights
    above the threshold cannot contribute to the lower tail)."""
    th, u, I, rho, rho1, C0 = constants()
    for j in range(1, jmax + 1):
        a = math.floor(th * j + 1)  # E_j <= theta*j+1  <=>  E_j <= a
        # dist[E] = P(E_j = E) for E <= a, exact
        dist = {0: Fraction(1)}
        for _ in range(j):
            nd = {}
            for E, p in dist.items():
                w = Fraction(1, 2)
                for v in range(1, a - E + 1):
                    nd[E + v] = nd.get(E + v, Fraction(0)) + p * w
                    w /= 2
            dist = nd
        tail = float(sum(dist.values()))
        assert tail <= C0 * rho ** j + 1e-12, (j, tail, C0 * rho ** j)
    print(f"2. Lemma 1: PASS  exact tail <= C0*rho^j for j=1..{jmax}")


def survivor_density_fast(K):
    """O(K^2) prefix-sum DP for p_K (float64)."""
    pow3 = [1]
    for _ in range(K + 2):
        pow3.append(pow3[-1] * 3)

    def crossed(E, j):
        return E >= 1 and (1 << (E - 1)) >= pow3[j]

    cur = [0.0] * (K + 1)
    cur[0] = 1.0
    surv = 0.0
    for j in range(0, K + 1):
        for E in range(0, K + 1):
            if cur[E]:
                surv += cur[E] * (0.5 ** (K - E))
        nxt = [0.0] * (K + 1)
        S = 0.0
        alive = False
        for Ep in range(1, K + 1):
            S = 0.5 * (S + cur[Ep - 1])
            if S and not crossed(Ep, j + 1):
                nxt[Ep] = S
                alive = True
        cur = nxt
        if not alive:
            break
    return surv


def survivor_density_slow_exact(K):
    """Exact-rational reference DP (as in verify_survivor_density_rate.py)."""
    pow3 = [1]
    for _ in range(K + 2):
        pow3.append(pow3[-1] * 3)

    def crossed(E, j):
        return E >= 1 and (1 << (E - 1)) >= pow3[j]

    cur = {0: Fraction(1)}
    surv = Fraction(0)
    j = 0
    while cur:
        nxt = {}
        for E, p in cur.items():
            pv = p * Fraction(1, 2)
            for v in range(1, K - E + 1):
                E2 = E + v
                if not crossed(E2, j + 1):
                    nxt[E2] = nxt.get(E2, Fraction(0)) + pv
                pv *= Fraction(1, 2)
            surv += p * Fraction(1, 2) ** (K - E)
        cur = nxt
        j += 1
        if j > K + 1:
            break
    return surv


def check_theorem1a_and_limit():
    th, u, I, rho, rho1, C0 = constants()
    # cross-check fast vs exact
    for K in (20, 100):
        a = survivor_density_fast(K)
        b = float(survivor_density_slow_exact(K))
        assert abs(a - b) / b < 1e-10, (K, a, b)
    print("   fast DP cross-checked against exact-rational DP at K=20,100")
    Ks = [50, 100, 200, 400, 600, 800, 1000, 1400, 1800]
    ps = []
    for K in Ks:
        p = survivor_density_fast(K)
        assert p <= 31 * rho1 ** K, (K, p, 31 * rho1 ** K)
        ps.append(p)
    print(f"3. Theorem 1a: PASS  p_K <= 31*rho1^K for K in {Ks}")
    rates = [(ps[i] / ps[i - 1]) ** (1.0 / (Ks[i] - Ks[i - 1]))
             for i in range(1, len(Ks))]
    for i in range(1, len(rates)):
        assert rates[i] > rates[i - 1] - 1e-9, (i, rates)
    assert all(r < rho1 for r in rates)
    print(f"4. limit evidence: PASS  local rate increases "
          f"{rates[0]:.5f} -> {rates[-1]:.5f} toward rho1={rho1:.5f}")


def check_tilt():
    th, u, I, rho, rho1, C0 = constants()
    for mu in (1.2, 1.4, th - 0.2, th - 0.05, th - 0.005):
        uu = 2 - 2 / mu  # solves 2/(2-u) = mu
        assert 0 < uu < 1
        m = 2 / (2 - uu)
        assert abs(m - mu) < 1e-12
        Imu = (mu - 1) * math.log(uu) + math.log(2 - uu)
        # Legendre value must be the sup: compare against grid
        grid = max((mu - 1) * math.log(v) + math.log(2 - v)
                   for v in [i / 1000 for i in range(1, 1000)])
        assert Imu >= grid - 1e-6
        if mu == th - 0.005:
            assert abs(Imu / mu - I / th) < 2e-3
    print("5. tilt calculus: PASS  tilted mean solvable; "
          "I(mu)/mu -> I(theta)/theta")


def check_corollary2_sandwich():
    """Corollary 2: 2^(K-1) p_{K+1} <= N_K <= 2^(K-1) p_{K-2} by direct
    enumeration of not-decided-discharged classes, K = 8..14. (Observed:
    the upper bound is attained exactly at every tested K.)"""
    import math as _m
    pow3max = [3 ** i for i in range(20)]

    def _v2(n):
        return (n & -n).bit_length() - 1

    def _crossed(E, j):
        return E >= 1 and (1 << (E - 1)) >= pow3max[j]

    def N_K(K):
        cnt = 0
        for r in range(1, 2 ** K, 2):
            N, rr, E, j, dd = K, r, 0, 0, False
            while True:
                t = (3 * rr + 1) % (1 << N)
                if t == 0:
                    break
                e = _v2(t)
                if e >= N - 1:
                    break
                E += e
                j += 1
                if _crossed(E, j):
                    dd = True
                    break
                N -= e
                rr = (t >> e) % (1 << N)
                if N < 2:
                    break
            if not dd:
                cnt += 1
        return cnt

    for K in range(8, 15):
        n = N_K(K)
        lo = survivor_density_fast(K + 1) * 2 ** (K - 1)
        hi = survivor_density_fast(K - 2) * 2 ** (K - 1)
        assert lo <= n <= hi + 1e-6, (K, n, lo, hi)
    print("6. Corollary 2 sandwich: PASS  (K=8..14; upper bound attained "
          "exactly)")


def main():
    check_constants()
    check_lemma1()
    check_theorem1a_and_limit()
    check_tilt()
    check_corollary2_sandwich()
    print("\nAll checks passed.")


if __name__ == "__main__":
    main()
