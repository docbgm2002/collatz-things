#!/usr/bin/env python3
"""
Verification for "Shadow Certificates: the Master No-Go Theorem"
(shadow_certificate.md). Exact integer arithmetic throughout.
"""
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


def lam(d, x, smax=25):
    o = 2 * 3 ** (d - 1)
    best = None
    for s in range(1, smax + 1):
        T = w_d(d, 1 + o * s)
        mod = 1 << (T.bit_length() + 1)
        if x % mod == T % mod:
            best = s
    return best


def check_lemma_S(Nmax=19, kmax=6, dmax=4):
    for N in range(8, Nmax + 1):
        for k in range(3, kmax + 1):
            w = 2 ** (k - 1) + 1
            x = 2 ** N * w - 5
            # orbit identities
            assert v2(3 * x + 1) == 1
            fx = f(x)
            assert fx == 3 * 2 ** (N - 1) * w - 7
            assert v2(3 * fx + 1) == 2
            ffx = f(fx)
            assert ffx == 9 * 2 ** (N - 3) * w - 5
            assert 8 * ffx == 9 * x + 5
            assert Fraction(ffx, x) == Fraction(9 * x + 5, 8 * x) > Fraction(9, 8)
            # fuel
            assert tau(x) == 2 and tau(fx) == 1 and tau(ffx) == 2
            # residues to full stated depth
            for m in range(1, N - 2):
                mod = 1 << m
                assert x % mod == ffx % mod == (-5) % mod, (N, k, m)
                assert fx % mod == (-7) % mod, (N, k, m)
            # length closure
            assert x.bit_length() == ffx.bit_length() == N + k
            # detectors BOT on all three points
            for d in range(1, dmax + 1):
                assert lam(d, x) is None and lam(d, fx) is None \
                    and lam(d, ffx) is None, (N, k, d)
    print(f"Lemma S: PASS  N=8..{Nmax}, k=3..{kmax}, detectors d<={dmax}")


def check_smallest():
    x = 1275
    assert f(x) == 1913 and f(1913) == 1435
    assert 8 * 1435 == 9 * 1275 + 5
    assert Fraction(1913, 1275) * Fraction(1435, 1913) == Fraction(287, 255) > 1
    print("Smallest certificate: PASS  1275 -> 1913 -> 1435, product 287/255")


def check_minus17_shadow():
    """General principle spot-check: the K=7 expanding cycle at -17
    (-17,-25,-37,-55,-82/..): shadow x = -17 mod 2^N traverses a closed
    residue itinerary with product 3^7/2^11 > 1."""
    N = 30
    x0 = 2 ** N * 5 - 17
    # follow 7 odd steps; record valuations and check total
    x = x0
    E = 0
    for _ in range(7):
        e = v2(3 * x + 1)
        E += e
        x = f(x)
    assert E == 11, E
    assert Fraction(x, x0) > Fraction(3 ** 7, 2 ** 11) > 1
    # residue returns: x = x0 = -17 mod 2^(N - 11)
    mod = 1 << (N - 11)
    assert x % mod == x0 % mod == (-17) % mod
    print("General principle: PASS  -17 shadow closes with product > "
          "3^7/2^11 = 2187/2048 > 1")


def main():
    check_lemma_S()
    check_smallest()
    check_minus17_shadow()
    print("\nAll checks passed.")


if __name__ == "__main__":
    main()
