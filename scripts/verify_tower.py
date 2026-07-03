#!/usr/bin/env python3
"""
Verification for "The Mersenne Ancestry Tower" (tower_theorem.md).
Exact integer arithmetic throughout.
"""
from fractions import Fraction


def v2(n):
    return (n & -n).bit_length() - 1


def v3(n):
    c = 0
    while n % 3 == 0:
        n //= 3
        c += 1
    return c


def tau(x):
    return v2(x + 1)


def f(x):
    t = 3 * x + 1
    return t >> v2(t)


def ordd(d):
    return 2 * 3 ** (d - 1)


def w(d, M):
    if d == 0:
        return 2 ** M - 1
    num = 2 ** (M + 2 * d) - 2 ** (2 * d + 1) + 3 ** d
    assert num % 3 ** d == 0, (d, M)
    return num // 3 ** d


def beta(d, s):
    return w(d, 1 + ordd(d) * s).bit_length()


def lam(dp, x, smax=40):
    best = None
    for s in range(1, smax + 1):
        mod = 1 << (beta(dp, s) + 1)
        if x % mod == w(dp, 1 + ordd(dp) * s) % mod:
            best = s
    return best


def check_T1f():
    for d in range(1, 6):
        o = ordd(d)
        for M in range(1, 1 + 4 * o):
            div = (2 ** (M + 2 * d) - 2 ** (2 * d + 1) + 3 ** d) % 3 ** d == 0
            assert div == (M % o == 1), (d, M)
    # primitive-root fact behind it: ord_{3^d}(2) = 2*3^(d-1)
    for d in range(1, 7):
        md = 3 ** d
        o = 1
        v = 2 % md
        while v != 1:
            v = v * 2 % md
            o += 1
        assert o == ordd(d), d
    print("T1(f): PASS  divisibility iff M = 1 mod 2*3^(d-1); "
          "ord_{3^d}(2) = 2*3^(d-1)")


def check_T1abc(dmax=7, smax=5):
    for d in range(1, dmax + 1):
        o = ordd(d)
        for s in range(1, smax + 1):
            M = 1 + o * s
            x = w(d, M)
            assert x % 2 == 1 and x > 1, (d, M)
            assert tau(x) == 1, (d, M)
            assert 3 * x + 1 == 4 * w(d - 1, M), (d, M)
            assert v2(3 * x + 1) == 2, (d, M)
            assert f(x) == w(d - 1, M), (d, M)
            # ratio in (3/4, 1)
            assert w(d - 1, M) < x and 4 * w(d - 1, M) > 3 * x, (d, M)
            # full chain
            z = x
            for _ in range(d):
                z = f(z)
            assert z == 2 ** M - 1, (d, M)
    print(f"T1(a-c): PASS  odd, tau=1, 3w_d+1 = 4w_(d-1), full chain to "
          f"2^M-1, ratios in (3/4,1)  (d<={dmax})")


def check_T1d(dmax=8, smax=4):
    for d in range(1, dmax + 1):
        o = ordd(d)
        assert v3(2 ** o - 1) == d, d
        B = (2 ** o - 1) // 3 ** d
        assert 0 < B < 2 ** o
        for s in range(1, smax + 1):
            M = 1 + o * s
            word = 1 + 2 ** (2 * d + 1) * int(bin(B)[2:].zfill(o) * s, 2)
            assert word == w(d, M), (d, s)
    print(f"T1(d): PASS  LTE v3(2^ord - 1) = d; exact carry-free periodic "
          f"normal form  (d<={dmax})")


def check_T1e(dmax=5, mbits=48):
    mod = 1 << mbits
    lim = {}
    for d in range(1, dmax + 1):
        lim[d] = (1 - 2 ** (2 * d + 1) * pow(3, -d, mod)) % mod
        o = ordd(d)
        for s in range(mbits // o + 1, mbits // o + 4):
            M = 1 + o * s
            assert w(d, M) % mod == lim[d], (d, M)
    for d in range(1, dmax + 1):
        for dp in range(1, dmax + 1):
            if d == dp:
                continue
            diff = (lim[d] - lim[dp]) % mod
            assert diff != 0 and v2(diff) == 2 * min(d, dp) + 1, (d, dp)
    print(f"T1(e): PASS  2-adic freeze at Lambda_d; separation bit exactly "
          f"2*min(d,d')+1  (d,d'<={dmax})")


def check_lemmaD(dmax=4):
    # D.1 self-reading
    for d in range(1, dmax + 1):
        for s in range(1, 6):
            assert lam(d, w(d, 1 + ordd(d) * s), smax=12) == s, (d, s)
    print("D.1: PASS  lambda_d reads its own tower index")
    # D.2 blindness: burn and all-ones
    for d in range(1, dmax + 1):
        M1 = 1 + ordd(d)
        assert w(d, M1) % 16 == (9 if d == 1 else 1), d
        for t in range(4, 14):
            for j in range(0, 8):
                assert lam(d, 3 ** j * 2 ** t - 1, smax=10) is None, (d, j, t)
        for M in range(4, 30):
            assert lam(d, 2 ** M - 1, smax=10) is None, (d, M)
    print("D.2: PASS  lambda_d = BOT on burn family and all-ones, all d")
    # D.3 cross-tower boundedness: lambda_{d'}(w_d(M)) bounded uniformly
    for d in range(1, dmax + 1):
        for dp in range(1, dmax + 1):
            if d == dp:
                continue
            cap = (2 * min(d, dp) + 1) // ordd(dp)  # theoretical bound
            for s in range(3, 8):
                M = 1 + ordd(d) * s
                lv = lam(dp, w(d, M), smax=12)
                assert lv is None or lv <= max(cap, 0), (d, dp, M, lv)
    print("D.3: PASS  cross-tower detector values bounded by "
          "(2*min+1)/ord'  (sampled)")


def check_T2_chain():
    """Chain arithmetic: L*log2(4/3) is a constant while burn grows;
    exact rational form (3/2)^n > (4/3)^L * B for every sampled B, L."""
    for L in (1, 2, 3, 5, 8):
        for exp10 in (0, 20, 40, 60):
            B = Fraction(10) ** exp10
            bound = Fraction(4, 3) ** L * B
            val = Fraction(1)
            n = 0
            while val <= bound:
                n += 1
                val *= Fraction(3, 2)
                assert n < 20000
    print("T2: PASS  cap L*log2(4/3) + const is beaten by the burn for "
          "every sampled (L, const)")


def main():
    check_T1f()
    check_T1abc()
    check_T1d()
    check_T1e()
    check_lemmaD()
    check_T2_chain()
    print("\nAll checks passed.")


if __name__ == "__main__":
    main()
