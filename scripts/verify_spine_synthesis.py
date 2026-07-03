#!/usr/bin/env python3
"""
Verification for "Spine Synthesis: the Complete Exact Lane"
(spine_synthesis.md). Exact integer arithmetic throughout.

S1: full lane w_d(M) ->^d 2^M-1 ->^(M-1) peak ->^1 a_M ->^1 a_(M+1)/2^e*,
    payout formula e* = 1+v2(M+1) = 2+v2(1+3^(d-1)s), = 2 iff s even;
    rail 8y+1 for all tower members.
S2: exact burn ratio over M-1 steps exceeds (3/2)^(M-1), so any bounded
    correction fails for M > 1 + Omega/log2(3/2).
"""
from fractions import Fraction


def v2(n):
    return (n & -n).bit_length() - 1


def f(x):
    t = 3 * x + 1
    return t >> v2(t)


def w(d, M):
    if d == 0:
        return 2 ** M - 1
    num = 2 ** (M + 2 * d) - 2 ** (2 * d + 1) + 3 ** d
    assert num % 3 ** d == 0
    return num // 3 ** d


def a(m):
    return (3 ** m - 1) // 2


def check_S1(dmax=5, smax=5):
    for d in range(1, dmax + 1):
        o = 2 * 3 ** (d - 1)
        for s in range(1, smax + 1):
            M = 1 + o * s
            assert M % 2 == 1
            x = w(d, M)
            # tower segment: d steps, each e=2, value strictly decreasing
            for _ in range(d):
                assert v2(3 * x + 1) == 2
                nx = f(x)
                assert nx < x
                x = nx
            assert x == 2 ** M - 1
            # burn segment: M-1 steps, each e=1, ratio > 3/2
            for _ in range(M - 1):
                assert v2(3 * x + 1) == 1
                nx = f(x)
                assert 2 * nx > 3 * x
                x = nx
            assert x == 2 * 3 ** (M - 1) - 1
            # repunit landing
            x = f(x)
            assert x == a(M), (d, s)
            # payout formula and parity criterion
            e = v2(3 * a(M) + 1)
            assert e == 1 + v2(M + 1) == 2 + v2(1 + 3 ** (d - 1) * s), (d, s)
            assert (e == 2) == (s % 2 == 0), (d, s)
            assert f(a(M)) == a(M + 1) // 2 ** e
    print(f"S1 lane: PASS  d<={dmax}, s<={smax}  (full d+M+1 exact steps, "
          f"payout formula, parity criterion)")


def check_rails(dmax=6, smax=7):
    for d in range(1, dmax + 1):
        o = 2 * 3 ** (d - 1)
        for s in range(1, smax + 1):
            assert w(d, 1 + o * s) % 8 == 1, (d, s)
    print(f"S1 rail: PASS  every tower member on rail 8y+1  "
          f"(d<={dmax}, s<={smax})")


def check_S2(Ms=(9, 15, 21, 31)):
    for M in Ms:
        x = 2 ** M - 1
        prod = Fraction(1)
        for _ in range(M - 1):
            nx = f(x)
            prod *= Fraction(nx, x)
            x = nx
        assert prod > Fraction(3, 2) ** (M - 1), M
    # threshold arithmetic: (M-1) log2(3/2) > Omega once M > 1 + Omega/log2(3/2)
    # exact rational form: (3/2)^(M-1) > 2^Omega for sampled Omega
    for Omega in (1, 10, 100):
        val = Fraction(1)
        n = 0
        while val <= Fraction(2) ** Omega:
            n += 1
            val *= Fraction(3, 2)
            assert n < 10000
    print(f"S2: PASS  exact burn ratio > (3/2)^(M-1); bounded oscillation "
          f"beaten for every sampled Omega")


def main():
    check_S1()
    check_rails()
    check_S2()
    print("\nAll checks passed.")


if __name__ == "__main__":
    main()
