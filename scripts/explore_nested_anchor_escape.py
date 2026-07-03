#!/usr/bin/env python3
"""
Explore the nested-anchor/residue-certificate idea.

For an odd start x, let f(x) be the accelerated Collatz map.  If x first
descends after j odd-steps and the cumulative 2-adic valuation is E, then its
exact accelerated valuation prefix is fixed modulo 2^(E+1), giving an affine
image for every integer in that residue class.

The script measures:

1. the exact accelerated-prefix depth E+1 for concrete and Mersenne starts;
2. whether the Mersenne depth appears bounded linearly by its exponent;
3. whether a simpler fuse-map induction on value/cofactor can replace the
   full residue history (it cannot, and the script prints small witnesses);
4. the fact that the nested all-ones residue branch has no positive integer
   in its intersection.

This is exploratory.  Finite bounds printed here are not universal proofs.
"""

from dataclasses import dataclass


def v2(n):
    return (n & -n).bit_length() - 1 if n else 10**9


def odd_step(x):
    t = 3 * x + 1
    e = v2(t)
    return t >> e, e


def tau(x):
    return v2(x + 1)


@dataclass(frozen=True)
class DescentCertificate:
    start: int
    landing: int
    odd_steps: int
    division_count: int
    bit_depth: int
    odd_multiplier_power: int
    valuations: tuple


def first_descent_certificate(x, step_limit=100000):
    """Return the concrete first-descent parity certificate for odd x."""
    if x <= 1 or x % 2 == 0:
        raise ValueError("x must be an odd integer greater than 1")

    cur = x
    valuations = []
    while cur >= x and len(valuations) < step_limit:
        cur, e = odd_step(cur)
        valuations.append(e)

    if cur >= x:
        return None

    E = sum(valuations)
    j = len(valuations)
    assert pow(3, j) < (1 << E)

    return DescentCertificate(
        start=x,
        landing=cur,
        odd_steps=j,
        division_count=E,
        bit_depth=E + 1,
        odd_multiplier_power=j,
        valuations=tuple(valuations),
    )


def affine_image_for_prefix(x, certificate, q):
    """
    Exact image of x + 2^(E+1) q under the fixed accelerated prefix.

    If q is any nonnegative integer, the E+1 low bits are unchanged, so

        f^j(x + 2^(E+1) q) = landing + 2*3^j q.
    """
    K = certificate.bit_depth
    j = certificate.odd_steps
    lifted = x + (1 << K) * q
    cur = lifted
    observed = []
    for _ in range(j):
        cur, e = odd_step(cur)
        observed.append(e)
    assert tuple(observed) == certificate.valuations
    assert cur == certificate.landing + 2 * pow(3, j) * q
    return cur


def fuse_transition(x):
    """Compress one full trailing-one burn and its payout."""
    L = tau(x)
    m = (x + 1) >> L
    raw = pow(3, L) * m - 1
    s = v2(raw)
    y = raw >> s
    L2 = tau(y)
    m2 = (y + 1) >> L2
    return y, L, m, s, L2, m2


def scan_simple_orders(limit=1_000_000):
    """
    Test two tempting one-episode inductions:

      - the fuse image is smaller;
      - if not, at least its odd cofactor is smaller.

    Neither is universal.
    """
    non_value = 0
    non_value_or_cofactor = 0
    first_value_failure = None
    first_joint_failure = None

    for x in range(3, limit + 1, 2):
        y, L, m, s, L2, m2 = fuse_transition(x)
        if y >= x:
            non_value += 1
            if first_value_failure is None:
                first_value_failure = (x, L, m, y, s, L2, m2)
            if m2 >= m:
                non_value_or_cofactor += 1
                if first_joint_failure is None:
                    first_joint_failure = (x, L, m, y, s, L2, m2)

    return {
        "limit": limit,
        "non_value": non_value,
        "non_value_or_cofactor": non_value_or_cofactor,
        "first_value_failure": first_value_failure,
        "first_joint_failure": first_joint_failure,
    }


def mersenne_depth_records(min_exponent=7, max_exponent=2001):
    """Return record ratios (E+1)/n and j/n for odd Mersenne exponents."""
    depth_records = []
    step_records = []
    best_depth = -1.0
    best_steps = -1.0

    for n in range(min_exponent, max_exponent + 1, 2):
        x = (1 << n) - 1
        cert = first_descent_certificate(x)
        depth_ratio = cert.bit_depth / n
        step_ratio = cert.odd_steps / n
        if depth_ratio > best_depth:
            best_depth = depth_ratio
            depth_records.append(
                (
                    n,
                    cert.bit_depth,
                    cert.division_count,
                    cert.odd_steps,
                    depth_ratio,
                    cert.landing,
                )
            )
        if step_ratio > best_steps:
            best_steps = step_ratio
            step_records.append(
                (
                    n,
                    cert.bit_depth,
                    cert.division_count,
                    cert.odd_steps,
                    step_ratio,
                    cert.landing,
                )
            )

    return depth_records, step_records


def check_all_ones_intersection(max_depth=256):
    """
    The residues r_K=2^K-1 are nested, but no positive integer lies in all.

    For a fixed positive x, x == -1 mod 2^K can hold only while K <= tau(x).
    """
    samples = (3, 7, 15, 27, 31, 127, 255, 1023, 12345)
    for x in samples:
        holding = [K for K in range(1, max_depth + 1) if x % (1 << K) == (1 << K) - 1]
        assert holding == list(range(1, tau(x) + 1))
    return samples


def main():
    cert = first_descent_certificate(27)
    for q in range(8):
        affine_image_for_prefix(27, cert, q)

    samples = check_all_ones_intersection()
    simple = scan_simple_orders()
    depth_records, step_records = mersenne_depth_records()

    print("Nested-anchor identity: PASS for the first-descent prefix of 27")
    print(
        "  f^j(27 + 2^(E+1) q) = landing + 2*3^j q with",
        f"j={cert.odd_steps}, E={cert.division_count}, "
        f"K=E+1={cert.bit_depth}, landing={cert.landing}",
    )
    print()
    print("All-ones branch:")
    print("  residues 2^K-1 mod 2^K are nested and converge 2-adically to -1")
    print("  no positive integer survives all depths; checked samples:", samples)
    print()
    print("One-fuse simple induction scan:")
    print(
        f"  odd x <= {simple['limit']}: value non-descent in "
        f"{simple['non_value']} cases"
    )
    print(
        "  value and cofactor both non-descending in",
        simple["non_value_or_cofactor"],
        "cases",
    )
    print("  first joint failure (x,L,m,y,payout,L2,m2):", simple["first_joint_failure"])
    print()
    print("Mersenne first-descent certificate depth records (odd n <= 2001):")
    for row in depth_records:
        n, K, E, j, ratio, landing = row
        print(
            f"  n={n:4d}  K={K:5d}  E={E:5d}  j={j:5d}  "
            f"K/n={ratio:8.5f}  landing_bits={landing.bit_length()}"
        )
    print("  final maximum K/n:", f"{depth_records[-1][4]:.8f}")
    print()
    print("Mersenne odd-step record ratios:")
    for row in step_records:
        n, K, E, j, ratio, landing = row
        print(f"  n={n:4d}  j={j:5d}  j/n={ratio:8.5f}  E={E}  K={K}")


if __name__ == "__main__":
    main()
