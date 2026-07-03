#!/usr/bin/env python3
"""
Verification and exploration for latent_fuel_notes.md.

Exact (verified): Lemmas L1, L2 for k <= 60.
Exploratory: mod-3 filtering of x'_M; search for the depth-3 family and
its period (conjecture: period 2*3^(d-1), i.e. 18 at d=3).
"""


def v2(n):
    return (n & -n).bit_length() - 1


def tau(x):
    return v2(x + 1)


def f(x):
    t = 3 * x + 1
    return t >> v2(t)


def check_L1(kmax=60):
    for k in range(1, kmax + 1):
        M = 2 * k + 3
        xp = (2 ** (M + 2) - 5) // 3
        assert (2 ** (M + 2) - 5) % 3 == 0
        word = int("10" * k + "1001", 2)
        assert word == xp, (k, "word mismatch")
        assert f(xp) == 2 ** M - 1, k
        assert tau(xp) == 1, k
        assert v2(3 * xp + 1) == 2, k
    print(f"L1: PASS  x'_M = (10)^k 1001 and f(x') = 2^M - 1, k=1..{kmax}")


def check_L2(kmax=60):
    for k in range(1, kmax + 1):
        M = 6 * k + 1
        y = (2 ** (6 * k + 5) - 23) // 9
        assert (2 ** (6 * k + 5) - 23) % 9 == 0
        word = int("111000" * k + "01", 2)
        assert word == y, (k, "word mismatch")
        xp = (2 ** (M + 2) - 5) // 3
        assert f(y) == xp, k
        assert f(f(y)) == 2 ** M - 1, k
        assert tau(y) == 1, k
        # per-step ratio -> 3/4 from below/above: check < 1 (value drops)
        assert xp < y and 4 * xp > 3 * y - 3, k
    print(f"L2: PASS  y_k = (111000)^k 01, f^2(y) = 2^(6k+1) - 1, k=1..{kmax}")


def mod3_filter(count=20):
    print("\nexploratory: x'_M mod 3 (M odd) — preimage existence filter")
    vals = []
    for i in range(count):
        M = 5 + 2 * i
        xp = (2 ** (M + 2) - 5) // 3
        vals.append(xp % 3)
    print("   pattern:", vals, " (0 = no f-preimage exists)")


def search_depth3(kmax=8):
    print("\nexploratory: depth-3 family — preimages z of y_k, f(z) = y_k")
    print("   conjectured period 2*3^2 = 18")
    for k in range(1, kmax + 1):
        y = (2 ** (6 * k + 5) - 23) // 9
        if y % 3 == 0:
            print(f"   k={k}: y_k = 0 mod 3, no preimage")
            continue
        found = None
        for e in range(1, 12):
            num = y * 2 ** e - 1
            if num % 3 == 0:
                z = num // 3
                if z % 2 == 1:
                    found = (e, z)
                    break
        if found:
            e, z = found
            b = bin(z)[2:]
            # report the suffix in 18-bit chunks for period inspection
            chunks = []
            s = b
            while len(s) > 18:
                chunks.append(s[-18:])
                s = s[:-18]
            chunks.append(s)
            print(f"   k={k}: e={e}  z has {len(b)} bits; "
                  f"18-bit chunks (low to high): {chunks}")
        else:
            print(f"   k={k}: no small preimage found")


def main():
    check_L1()
    check_L2()
    mod3_filter()
    search_depth3()
    print("\nExact checks (L1, L2) passed; remaining output is exploratory.")


if __name__ == "__main__":
    main()
