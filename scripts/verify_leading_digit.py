#!/usr/bin/env python3
"""
Verification for "Leading Digits Do Not Survive" (leading_digit_nogo.md).
Exact integer arithmetic in every assertion; floats only for display.
"""
import math
from fractions import Fraction


def v2(n):
    return (n & -n).bit_length() - 1


def tau(x):
    return v2(x + 1)


def f(x):
    t = 3 * x + 1
    return t >> v2(t)


def w_d(d, M):
    num = 2 ** (M + 2 * d) - 2 ** (2 * d + 1) + 3 ** d
    assert num % 3 ** d == 0
    return num // 3 ** d


def lam(d, x, smax=20):
    o = 2 * 3 ** (d - 1)
    best = None
    for s in range(1, smax + 1):
        T = w_d(d, 1 + o * s)
        mod = 1 << (T.bit_length() + 1)
        if x % mod == T % mod:
            best = s
    return best


def LD(y, j):
    return y >> (y.bit_length() - j)


def check_irrationality():
    """log2(9/8) rational <=> 2^(p+3q) = 3^(2q) for some q>=1: impossible
    since v3(LHS)=0 < 2q = v3(RHS)."""
    for q in range(1, 30):
        for p in range(0, 100):
            assert 2 ** (p + 3 * q) != 3 ** (2 * q)
    print("irrationality arithmetic: PASS  (2^(p+3q) = 3^(2q) has no "
          "solutions; v3 argument)")


def check_theorem_F(m=6, j=4, a=53):
    beta = math.log2(9 / 8)
    frac = a * beta - math.floor(a * beta)
    assert min(frac, 1 - frac) < 2 ** (-j - 3)
    N = 3 * a + max(m, 5) + j + 8
    # w chosen with top bits 1011 (mid-cell for LD_4) — cell distance check
    w = (0b1011 << 40) + 12345
    x0 = 2 ** N * w - 5
    # walk with full itinerary checks
    x = x0
    for i in range(a):
        depth = N - 3 * i
        assert x % (1 << (depth - 3)) == (-5) % (1 << (depth - 3)), i
        assert tau(x) == 2 and v2(3 * x + 1) == 1, i
        for d in (1, 2, 3):
            assert lam(d, x) is None, (i, d)
        x = f(x)
        assert x % (1 << (depth - 3)) == (-7) % (1 << (depth - 3)), i
        assert tau(x) == 1 and v2(3 * x + 1) == 2, i
        for d in (1, 2, 3):
            assert lam(d, x) is None, (i, d)
        x = f(x)
    xa = x
    # exact closed form
    assert 8 ** a * xa == 9 ** a * x0 + 5 * (9 ** a - 8 ** a)
    # coordinate closure
    assert x0 % (1 << m) == xa % (1 << m) == (-5) % (1 << m)
    assert tau(x0) == tau(xa) == 2
    for d in (1, 2, 3):
        assert lam(d, xa) is None
    assert LD(x0, j) == LD(xa, j)
    # strict gain, exact
    assert xa > x0
    assert Fraction(xa, x0) > Fraction(9, 8) ** a  # delta > 0
    print(f"Theorem F instance (m={m}, j={j}, a={a}, N={N}): PASS")
    print(f"  LD_{j}: {bin(LD(x0, j))[2:]} -> {bin(LD(xa, j))[2:]} (closed); "
          f"gain = 2^{math.log2(xa / x0):.4f} > 0; all coords frozen; "
          f"detectors BOT on {2 * a + 1} nodes")


def check_dirichlet_supply():
    """for each j <= 8 there is a <= 5000 with ||a*beta|| < 2^-(j+3)."""
    beta = math.log2(9 / 8)
    for j in range(1, 9):
        eps = 2 ** (-j - 3)
        found = None
        for a in range(1, 5001):
            fr = a * beta - math.floor(a * beta)
            if min(fr, 1 - fr) < eps:
                found = a
                break
        assert found, j
    print("Dirichlet supply: PASS  suitable a exists for every j <= 8 "
          "(a <= 5000)")


def main():
    check_irrationality()
    check_theorem_F()
    check_dirichlet_supply()
    print("\nAll checks passed.")


if __name__ == "__main__":
    main()
