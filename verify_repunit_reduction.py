#!/usr/bin/env python3
"""
Verification for "The Mersenne-Repunit Reduction for the 3x+1 Map".

Exact integer arithmetic for R0-R3; R4 is an EMPIRICAL profile, reported (and
loosely sanity-gated) but not claimed as a theorem.

  R0  3 a_m + 1 = a_{m+1}                        (a_m = (3^m - 1)/2)
  R1  f^j(2^n-1) = 3^j 2^(n-j) - 1, monotone >= x0
  R2  f^n(2^n-1) = (3^n-1)/2 = a_n            (odd n)
                 = (3^n-1)/2^(2+v2(n))         (even n)
  R3  epoch(2^n-1) = n + sigma(a_n), no earlier passage below x0
  R4  the descent of a_n is statistically generic (empirical table)

No external dependencies.
"""
import statistics


def v2(n):
    return (n & -n).bit_length() - 1 if n else 10 ** 9


def tau(x):
    return v2(x + 1)


def f(x):
    t = 3 * x + 1
    return t >> v2(t)


def a(m):
    return (3 ** m - 1) // 2


# ---------------------------------------------------------------- R0
def check_R0(M=500):
    for m in range(M + 1):
        assert 3 * a(m) + 1 == a(m + 1), m
    print(f"R0: PASS  3 a_m + 1 = a_(m+1)  (m=0..{M})")


# ---------------------------------------------------------------- R1
def check_R1(N=200):
    for n in range(2, N + 1):
        x = 2 ** n - 1
        x0 = x
        for j in range(n):
            assert x == 3 ** j * 2 ** (n - j) - 1, (n, j)
            assert x >= x0, (n, j)               # never below the start
            if j < n - 1:
                assert v2(3 * x + 1) == 1, (n, j)
                x = f(x)
    print(f"R1: PASS  f^j(2^n-1)=3^j 2^(n-j)-1, monotone >= x0  (n=2..{N})")


# ---------------------------------------------------------------- R2
def check_R2(N=200):
    for n in range(2, N + 1):
        x = 2 ** n - 1
        for _ in range(n):
            x = f(x)
        if n % 2 == 1:
            assert x == (3 ** n - 1) // 2 == a(n), n
        else:
            assert x == (3 ** n - 1) // (2 ** (2 + v2(n))), n
            assert x == a(n) // (2 ** (1 + v2(n))), n
    print(f"R2: PASS  f^n(2^n-1)=a_n (odd n) / a_n/2^(1+v2(n)) (even n)  (n=2..{N})")


# ---------------------------------------------------------------- R3
def check_R3(N=120):
    for n in range(3, N + 1, 2):                 # odd n
        x0 = 2 ** n - 1
        an = a(n)
        # no passage below x0 in the first n steps; step n lands exactly on a_n
        x = x0
        for t in range(1, n + 1):
            x = f(x)
            assert x >= x0, (n, t)               # stays at/above start
        assert x == an, n
        # sigma(a_n): first passage of a_n below x0
        y = an
        sigma = 0
        while y >= x0:
            y = f(y)
            sigma += 1
            assert sigma <= 100 * n, (n, sigma)
        # full epoch from 2^n-1 measured independently must equal n + sigma
        z = x0
        epoch = 0
        while True:
            z = f(z)
            epoch += 1
            if z < x0:
                break
        assert epoch == n + sigma, (n, epoch, n + sigma)
    print(f"R3: PASS  epoch(2^n-1) = n + sigma(a_n), no earlier passage  "
          f"(odd n=3..{N})")


# ---------------------------------------------------------------- R4 (empirical)
def report_R4(lo=11, hi=159):
    vcount = {}
    ratios = []
    exceed = 0
    total = 0
    for n in range(lo, hi + 1, 2):               # odd n
        x0 = 2 ** n - 1
        an = a(n)
        peak = 2 * 3 ** (n - 1) - 1
        x = an
        steps = 0
        mx = an
        while x >= x0:
            vv = v2(3 * x + 1)
            vcount[vv] = vcount.get(vv, 0) + 1
            x = f(x)
            steps += 1
            mx = max(mx, x)
            if steps > 100 * n:
                break
        total += 1
        ratios.append(steps / n)
        if mx > peak:
            exceed += 1
    tot = sum(vcount.values())
    meanv = sum(k * c for k, c in vcount.items()) / tot
    print("R4 (EMPIRICAL, not a theorem): descent of a_n is generic")
    print("    v2(3x+1) law: "
          + ", ".join(f"{k}:{vcount[k]/tot:.3f}" for k in sorted(vcount) if k <= 5)
          + "   | geometric 2^-k: 1:.500 2:.250 3:.125 4:.062 5:.031")
    print(f"    mean v2(3x+1) = {meanv:.3f} (generic 2.000)")
    print(f"    sigma(a_n)/n: mean={statistics.mean(ratios):.2f} "
          f"sd={statistics.pstdev(ratios):.2f} "
          f"range=[{min(ratios):.2f},{max(ratios):.2f}]")
    print(f"    orbits exceeding the burn peak after a_n: {exceed}/{total}")
    # loose sanity gates only (these are observations, not proofs)
    assert 1.7 < meanv < 2.3, meanv
    assert 0.40 < vcount[1] / tot < 0.60, vcount[1] / tot


if __name__ == "__main__":
    check_R0()
    check_R1()
    check_R2()
    check_R3()
    print()
    report_R4()
    print("\nR0-R3 verified exactly; R4 reported as empirical evidence.")
