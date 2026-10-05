# scripts/verify_macro_step_lundberg.py

"""Verification harness for docs/no-go/macro_step_lundberg.md.

Checks the MAC3 affine endpoint formula and ANC1 with exact arithmetic.
MAC2/MAC3 distribution checks are numerical diagnostics, LUN1A uses exact
rational partial sums, and LUN1 uses floating-point approximations. These
multiplier checks do not establish a bound for actual orbit growth. An
evidence-only finite orbit probe is printed separately. Not a proof; see
the note for status.

The spectral claims of the note (section 6) are checked separately by
scripts/verify_walsh1.py.
"""

import math
import random
from fractions import Fraction

LOG2_3 = math.log2(3)
ALPHA = LOG2_3 - 1.0
THETA_STAR = math.log(2)


def v2(n):
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def tau(x):
    return v2(x + 1)


def f(x):
    y = 3 * x + 1
    v = v2(y)
    return y >> v, v


def check_MAC3_endpoints(xmax=20_001):
    """Compare the affine formula with directly iterated integer endpoints."""
    checked = 0
    for x in range(5, xmax + 1, 4):
        y, v = f(x)
        K = tau(y)
        for _ in range(K - 1):
            y, burn_v = f(y)
            assert burn_v == 1
        assert tau(y) == 1

        denominator = 2 ** (v + K - 1)
        correction = 3 ** (K - 1) * (1 + 2 ** v) - denominator
        numerator = 3 ** K * x + correction
        assert y * denominator == numerator, (x, v, K, y)
        multiplier = Fraction(3 ** K, denominator)
        assert correction > 0
        assert Fraction(y, x) == multiplier + Fraction(correction, denominator * x)
        assert Fraction(y, x) > multiplier
        checked += 1

    # The fixed Class B state 1 has multiplier 3/4 and affine term 1/4.
    fixed_y, fixed_v = f(1)
    fixed_K = tau(fixed_y)
    assert (fixed_y, fixed_v, fixed_K) == (1, 2, 1)
    fixed_denominator = 2 ** (fixed_v + fixed_K - 1)
    assert Fraction(3 ** fixed_K, fixed_denominator) == Fraction(3, 4)
    fixed_correction = 3 ** (fixed_K - 1) * (1 + 2 ** fixed_v) - fixed_denominator
    assert Fraction(fixed_correction, fixed_denominator) == Fraction(1, 4)

    # The actual escape event and the homogeneous multiplier event differ,
    # even when their maxima are taken over the complete orbit down to 1.
    x = 9
    orbit = [x]
    multiplier = Fraction(1)
    multipliers = [multiplier]
    while x != 1:
        x, v = f(x)
        orbit.append(x)
        multiplier *= Fraction(3, 2 ** v)
        multipliers.append(multiplier)
    assert orbit == [9, 7, 11, 17, 13, 5, 1]
    assert tau(orbit[1]) == 3
    actual_macro_ratio = Fraction(orbit[3], orbit[0])
    assert actual_macro_ratio == Fraction(17, 9)
    assert multipliers[3] == Fraction(27, 16)
    threshold = Fraction(7, 4)
    assert Fraction(max(orbit), orbit[0]) == actual_macro_ratio > threshold
    assert max(multipliers) == Fraction(27, 16) < threshold
    print(f"MAC3 endpoint PASS (exact arithmetic, {checked} Class B starts "
          f"5..{xmax})")
    print("Orbit/multiplier separation PASS (start 9, actual peak ratio 17/9 "
          "> 7/4 > multiplier peak 27/16)")


def check_MAC2_MAC3(N=200_000, seed=0):
    rng = random.Random(seed)
    joint = {}
    deltas = []
    for _ in range(N):
        x = 4 * rng.randrange(1, 10**9) + 1      # tau(x) = 1
        y, v = f(x)
        K = tau(y)
        joint[(v, K)] = joint.get((v, K), 0) + 1
        # Homogeneous log-multiplier, excluding the affine correction.
        deltas.append(K * ALPHA + 1 - v)

    # independence check on a coarse grid
    v_marg, K_marg = {}, {}
    for (v, K), c in joint.items():
        v_marg[v] = v_marg.get(v, 0) + c
        K_marg[K] = K_marg.get(K, 0) + c

    max_dev = 0.0
    for (v, K), c in joint.items():
        p_hat = c / N
        p_v = v_marg[v] / N
        p_K = K_marg[K] / N
        max_dev = max(max_dev, abs(p_hat - p_v * p_K))

    mean_delta = sum(deltas) / N
    theory = 2 * LOG2_3 - 4
    print(f"MAC2: max |P(v,K) - P(v)P(K)| = {max_dev:.6f}  (expect ~0)")
    print(f"MAC3: mean log2(multiplier) = {mean_delta:.6f}, "
          f"theory = {theory:.6f}")
    assert max_dev < 0.005
    assert abs(mean_delta - theory) < 0.005
    print("MAC2/MAC3 numerical distribution checks PASS")


def mgf(theta, Kmax=400):
    # Floating-point truncated MGF of the homogeneous log-multiplier.
    s_K = sum((2 ** -K) * math.exp(theta * K * ALPHA) for K in range(1, Kmax))
    s_v = sum((2 ** -(j - 1)) * math.exp(-theta * j) for j in range(2, Kmax))
    return s_K * s_v * math.exp(theta)  # constant 1 in K*ALPHA + 1 - v


def check_LUN1A(terms=400):
    """Check partial sums for the mean-one homogeneous multiplier law.

    The multiplier is (3/2)^K * 2^(1-v); it is not x_out / x_in.
    MAC2 makes its factors independent. Exact rational tails recover the
    infinite geometric sums; the displayed decimal values are rounded.
    """
    F = Fraction

    e_K = sum(F(1, 2 ** i) * F(3, 2) ** i for i in range(1, terms))
    e_v = 2 * sum(F(1, 2 ** (j - 1)) * F(1, 2 ** j) for j in range(2, terms))
    print(f"LUN1A: E[(3/2)^K] = {float(e_K):.10f} (expect 3), "
          f"E[2^(1-v)] = {float(e_v):.10f} (expect 1/3)")
    print(f"LUN1A: E[multiplier] partial sum = {float(e_K * e_v):.10f} "
          "(limit 1)")
    assert e_K + 3 * F(3, 4) ** (terms - 1) == 3
    assert e_v + F(1, 3) * F(1, 4) ** (terms - 2) == F(1, 3)
    # truncated tails are positive, so the partial sums approach from below
    assert 0 < 3 - e_K < F(1, 10 ** 12)
    assert 0 < F(1, 3) - e_v < F(1, 10 ** 12)
    assert 0 < 1 - e_K * e_v < F(1, 10 ** 12)
    # the Jensen gap: log2 of the mean exceeds the mean of log2
    gap = 0.0 - (2 * LOG2_3 - 4)
    print(f"LUN1A: multiplier Jensen gap = {gap:.6f} bits per macro-step")
    assert gap > 0
    print("LUN1A multiplier partial sums and tails PASS")


def check_LUN1():
    # Compare the geometric sums and closed form at interior points of the
    # finite domain -ln(2) < theta < ln(2)/ALPHA, including negative theta.
    for theta in (-0.3, 0.0, 0.3, THETA_STAR, 1.0):
        closed_form = math.exp(theta * (ALPHA - 1)) / (
            (2 - math.exp(theta * ALPHA)) * (2 - math.exp(-theta))
        )
        assert math.isclose(mgf(theta), closed_form, rel_tol=1e-12, abs_tol=1e-12)
    m_star = mgf(THETA_STAR)
    print(f"LUN1: multiplier M(ln 2) = {m_star:.10f}  (expect 1)")
    assert abs(m_star - 1.0) < 1e-9
    # Sign structure around theta*. log M is convex with M(0) = 1 and
    # M'(0) = E[Delta] < 0, so M < 1 strictly inside (0, theta*) and M > 1
    # above it.  M(0.3) = 0.8676, M(1.0) = 1.9728.
    assert mgf(0.3) < 1.0
    assert mgf(1.0) > 1.0
    print("LUN1 numerical multiplier MGF checks PASS")


def check_ANC1(zmax=20_000, vmax=60):
    for z in range(1, zmax + 1, 2):
        if z % 3 == 0:
            continue
        bitlens = []
        for v in range(1, vmax + 1):
            num = (2 ** v) * z - 1
            if num % 3 != 0:
                continue
            x = num // 3
            if x > 0 and x % 2 == 1:
                bitlens.append(x.bit_length())
        if len(bitlens) != len(set(bitlens)):
            raise AssertionError(f"ANC1 violation at z={z}: {bitlens}")
        for a, b in zip(bitlens, bitlens[1:]):
            if b - a < 2:
                raise AssertionError(f"ANC1 spacing violation at z={z}")
    print(f"ANC1 PASS (all z <= {zmax}, v <= {vmax})")


def probe_DISC1(a=10, b=24, N=20_000, seed=1):
    """Finite positive-integer orbit diagnostic; no Haar bound is asserted."""
    rng = random.Random(seed)
    escapes = 0
    for _ in range(N):
        x0 = (1 << (b - 1)) | rng.getrandbits(b - 1) | 1
        x = x0
        peak = x0
        for _ in range(3 * b):            # finite window
            x, _ = f(x)
            peak = max(peak, x)
            if x == 1:
                break
        if peak >= (1 << a) * x0:
            escapes += 1
    print(f"DISC1 finite orbit probe (evidence only): P(peak >= 2^{a} x0) "
          f"~ {escapes / N:.6f}, multiplier-model reference 2^-a = {2 ** -a:.6f} "
          "(not a proved bound for this experiment)")


if __name__ == "__main__":
    check_MAC3_endpoints()
    check_MAC2_MAC3()
    check_LUN1A()
    check_LUN1()
    check_ANC1()
    probe_DISC1()
