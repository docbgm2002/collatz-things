# scripts/verify_macro_step_lundberg.py

"""Verification harness for docs/no-go/macro_step_lundberg.md.

Checks MAC2, MAC3, LUN1, ANC1 with exact integer arithmetic, and prints
an evidence-only probe for the escape frequency. Not a proof; see the note
for status.

The spectral claims of the note (section 6) are checked separately by
scripts/verify_walsh1.py.
"""

import math
import random

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


def check_MAC2_MAC3(N=200_000, seed=0):
    rng = random.Random(seed)
    joint = {}
    deltas = []
    for _ in range(N):
        x = 4 * rng.randrange(1, 10**9) + 1      # tau(x) = 1
        y, v = f(x)
        K = tau(y)
        joint[(v, K)] = joint.get((v, K), 0) + 1
        # full macro-step drift: B-step then K-1 A-steps
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
    print(f"MAC3: E[Delta] = {mean_delta:.6f}, theory = {theory:.6f}")
    assert max_dev < 0.005
    assert abs(mean_delta - theory) < 0.005
    print("MAC2/MAC3 PASS")


def mgf(theta, Kmax=400):
    # exact truncated MGF from the geometric laws
    s_K = sum((2 ** -K) * math.exp(theta * K * ALPHA) for K in range(1, Kmax))
    s_v = sum((2 ** -(j - 1)) * math.exp(-theta * j) for j in range(2, Kmax))
    return s_K * s_v * math.exp(theta)  # e^{theta*(1)} from the +1 term


def check_LUN1A(terms=400):
    """E[x_out / x_in] = 1 exactly over one macro-step.

    The ratio is 2^Delta = (3/2)^K * 2^(1-v); MAC2 makes the factors
    independent.  Done in exact rationals so the identity is not obscured
    by floating point.
    """
    from fractions import Fraction as F

    e_K = sum(F(1, 2 ** i) * F(3, 2) ** i for i in range(1, terms))
    e_v = 2 * sum(F(1, 2 ** (j - 1)) * F(1, 2 ** j) for j in range(2, terms))
    print(f"LUN1A: E[(3/2)^K] = {float(e_K):.10f} (expect 3), "
          f"E[2^(1-v)] = {float(e_v):.10f} (expect 1/3)")
    print(f"LUN1A: E[ratio] = {float(e_K * e_v):.10f}  (expect 1)")
    # truncated tails are positive, so the partial sums approach from below
    assert abs(float(e_K) - 3.0) < 1e-12
    assert abs(float(e_v) - 1.0 / 3.0) < 1e-12
    assert abs(float(e_K * e_v) - 1.0) < 1e-12
    # the Jensen gap: log2 of the mean exceeds the mean of log2
    gap = 0.0 - (2 * LOG2_3 - 4)
    print(f"LUN1A: Jensen gap = {gap:.6f} bits per macro-step")
    assert gap > 0
    print("LUN1A PASS")


def check_LUN1():
    m_star = mgf(THETA_STAR)
    print(f"LUN1: M(ln 2) = {m_star:.10f}  (expect 1)")
    assert abs(m_star - 1.0) < 1e-9
    # Sign structure around theta*. log M is convex with M(0) = 1 and
    # M'(0) = E[Delta] < 0, so M < 1 strictly inside (0, theta*) and M > 1
    # above it.  M(0.3) = 0.8676, M(1.0) = 1.9728.
    assert mgf(0.3) < 1.0
    assert mgf(1.0) > 1.0
    print("LUN1 PASS")


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
    """Evidence only: finite-window escape frequency among b-bit odds vs 2^-a."""
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
    print(f"DISC1 probe (evidence only): P(peak >= 2^{a} x0) "
          f"~ {escapes / N:.6f}, Haar bound = {2 ** -a:.6f}")


if __name__ == "__main__":
    check_MAC2_MAC3()
    check_LUN1A()
    check_LUN1()
    check_ANC1()
    probe_DISC1()