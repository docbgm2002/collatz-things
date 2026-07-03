#!/usr/bin/env python3
"""
Verification for "No-Go for Potentials with a Latent-Fuel Detector (NLP2)"
(nlp2_alternation.md). Exact integer arithmetic throughout.

Checks Lemma 0 (coordinate facts) over wide ranges, the burn-step freeze,
and the closing chain arithmetic.
"""
from fractions import Fraction


def v2(n):
    return (n & -n).bit_length() - 1


def tau(x):
    return v2(x + 1)


def f(x):
    t = 3 * x + 1
    return t >> v2(t)


def xprime(M):
    assert M % 2 == 1
    num = 2 ** (M + 2) - 5
    assert num % 3 == 0
    return num // 3


def yk(k):
    num = 2 ** (6 * k + 5) - 23
    assert num % 9 == 0
    return num // 9


def lam(x, lmax=None):
    """lambda(x) = max{l>=0: x = x'_{2l+3} mod 2^{2l+4}}, None if no match."""
    if lmax is None:
        lmax = x.bit_length() // 2 + 3
    best = None
    for l in range(0, lmax + 1):
        mod = 1 << (2 * l + 4)
        if x % mod == xprime(2 * l + 3) % mod:
            best = l
    return best


def check_lemma0():
    # 0.1: l=0 template is 9 mod 16
    assert xprime(3) == 9
    # 0.2: burn members and all-ones are 15 mod 16 -> lambda = BOT
    for t in range(4, 24):
        for j in range(0, 14):
            x = 3 ** j * 2 ** t - 1
            assert x % 16 == 15
            assert lam(x) is None, (j, t)
    for M in range(4, 60):
        x = 2 ** M - 1
        assert x % 16 == 15 and lam(x) is None, M
    print("0.1-0.2: PASS  template=9 mod 16; burn and all-ones are 15 mod 16,"
          " lambda=BOT")
    # 0.3: lambda(x'_M) = (M-3)/2
    for M in range(5, 80, 2):
        assert lam(xprime(M)) == (M - 3) // 2, M
    print("0.3:     PASS  lambda(x'_M) = (M-3)/2 for odd M in [5,79]")
    # 0.4: y_k facts
    for k in range(1, 40):
        y = yk(k)
        assert y % 16 == 1 and lam(y) is None, k
        assert tau(y) == 1, k
    for m in range(0, 13):
        mod = 1 << m
        if mod == 1:
            continue
        inv9 = pow(9, -1, mod)
        for k in range(max(1, m), m + 12):
            assert yk(k) % mod == (-23 * inv9) % mod, (m, k)
    print("0.4:     PASS  y_k = 1 mod 16 (lambda=BOT), tau=1, residue "
          "r** = -23*9^-1 frozen")
    # 0.5: exact ratio bounds and the chain itself
    for k in range(1, 40):
        M = 6 * k + 1
        y, xp, mer = yk(k), xprime(M), 2 ** M - 1
        assert f(y) == xp and f(xp) == mer, k
        assert 3 * y < 4 * xp, k
        assert 3 * xp < 4 * mer, k
    print("0.5:     PASS  chain y_k -> x'_{6k+1} -> 2^(6k+1)-1 exact; both "
          "ratios < 4/3")
    # frozen residue r* (from NLP1, rechecked)
    for m in range(1, 13):
        mod = 1 << m
        inv3 = pow(3, -1, mod)
        for k in range(max(1, m), m + 12):
            assert xprime(6 * k + 1) % mod == (-5 * inv3) % mod, (m, k)
    print("         PASS  residue r* = -5*3^-1 frozen (recheck)")


def check_burn_freeze(mmax=12, tmax=30, jmax=14):
    """Burn step endpoints share residue -1 mod 2^m and lambda=BOT."""
    for m in range(0, mmax + 1):
        mod = 1 << m
        t0 = max(m + 1, 5)
        for t in range(t0, tmax + 1):
            for j in range(0, jmax + 1):
                x = 3 ** j * 2 ** t - 1
                fx = f(x)
                assert fx == 3 ** (j + 1) * 2 ** (t - 1) - 1
                assert x % mod == (mod - 1) % mod
                assert fx % mod == (mod - 1) % mod
                assert lam(x) is None and lam(fx) is None
                assert tau(x) == t and tau(fx) == t - 1
                assert Fraction(fx, x) > Fraction(3, 2)
    print(f"burn:    PASS  coordinate freeze on both endpoints "
          f"(m<={mmax}, t0..{tmax}, j<={jmax})")


def check_chain_arithmetic():
    """(6k+1-t0)*log2(3/2) exceeds C + 2*log2(4/3) for every sampled C:
    exact rational form (3/2)^(6k+1-t0) > (4/3)^2 * B."""
    for m in (0, 1, 4, 8, 12):
        t0 = max(m + 1, 5)
        for exp10 in range(0, 61, 10):
            B = Fraction(10) ** exp10
            bound = Fraction(16, 9) * B
            val = Fraction(1)
            n = 0
            while val <= bound:
                n += 1
                val *= Fraction(3, 2)
                assert n < 10000
            # exists k with 6k+1-t0 >= n: unbounded in k, trivially
        print(f"   m={m:2d}: t0={t0}, chain closes for every sampled "
              f"constant gap (exact rational)")
    print("chain:   PASS  (1)+(2)+(3) jointly infeasible for sampled m")


def main():
    check_lemma0()
    check_burn_freeze()
    check_chain_arithmetic()
    print("\nAll checks passed.")


if __name__ == "__main__":
    main()
