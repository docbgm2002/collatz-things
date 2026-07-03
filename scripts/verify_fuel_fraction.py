#!/usr/bin/env python3
"""
Verification for "No-Go for Fuel-Fraction Potentials" (fuel_fraction_nogo.md).
Self-contained; exact integer/rational arithmetic in every assertion.
"""
from fractions import Fraction

W11 = [524543, 524415, 524351, 524319, 524303, 524295, 524291,
       707241, 526335, 525311, 524799]
W2 = [524315, 699065]


def v2(n):
    return (n & -n).bit_length() - 1


def tau(x):
    return v2(x + 1)


def f(x):
    t = 3 * x + 1
    return t >> v2(t)


def check_cycle(witnesses, coord, name):
    pairs = []
    prod = Fraction(1)
    for x in witnesses:
        fx = f(x)
        pairs.append((coord(x), coord(fx)))
        prod *= Fraction(fx, x)
    m = len(witnesses)
    for i in range(m):
        assert pairs[i][1] == pairs[(i + 1) % m][0], (name, i, "not closed")
    assert prod > 1, (name, float(prod))
    # summing the monotonicity constraints around the cycle yields
    # 0 <= -log2(prod) < 0: contradiction for every g. Report exactly.
    print(f"{name}: PASS  closed {m}-cycle, exact ratio product "
          f"{prod.numerator}/{prod.denominator} > 1")
    return prod


def check_theorem_D():
    coord = lambda x: (tau(x), x.bit_length())
    p = check_cycle(W11, coord, "Theorem D  (tau, len)")
    # structural claims: burn witnesses are 2^19 + 2^t - 1, steps stay in window
    for i, t in enumerate(range(8, 1, -1)):
        x = W11[i]
        assert x == 2 ** 19 + 2 ** t - 1, (i, t)
        fx = f(x)
        assert 2 ** 19 <= x < 2 ** 20 and 2 ** 19 <= fx < 2 ** 20
        assert 2 * fx > 3 * x                      # ratio > 3/2 exactly
    # recharge witness: e = 2, tau 1 -> 11, in window
    x = W11[7]
    assert tau(x) == 1 and v2(3 * x + 1) == 2
    assert tau(f(x)) == 11 and f(x).bit_length() == 20
    print("           structural claims PASS (burn form 2^19+2^t-1, "
          "in-window, recharge e=2)")


def check_corollary():
    coord = lambda x: (tau(x), x.bit_length(), x % 16)
    check_cycle(W2, coord, "Corollary  (tau, len, mod 16)")


def check_fixed_length_freeze(mmax=10, nmax=40):
    """2^n + 2^t - 1 = -1 mod 2^m for t >= m; image likewise for t-1 >= m;
    image stays at len n+1 for t <= n-2; ratio > 3/2."""
    for m in range(1, mmax + 1):
        mod = 1 << m
        for n in range(m + 3, nmax + 1):
            for t in range(m + 1, n - 1):
                x = 2 ** n + 2 ** t - 1
                assert x % mod == mod - 1, (m, n, t)
                assert tau(x) == t
                fx = f(x)
                assert fx == 3 * 2 ** (n - 1) + 3 * 2 ** (t - 1) - 1, (n, t)
                assert fx % mod == mod - 1, (m, n, t)
                assert tau(fx) == t - 1
                assert fx.bit_length() == n + 1 == x.bit_length()
                assert 2 * fx > 3 * x
    print(f"Fixed-length burn family: PASS  residue frozen at -1, len frozen, "
          f"tau descending (m<={mmax}, n<={nmax})")


def main():
    check_theorem_D()
    check_corollary()
    check_fixed_length_freeze()
    print("\nAll checks passed.")


if __name__ == "__main__":
    main()
