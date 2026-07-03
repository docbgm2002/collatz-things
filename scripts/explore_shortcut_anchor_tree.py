#!/usr/bin/env python3
"""
Exact nested-anchor tree for the shortcut Collatz map

    U(n) = n/2          if n is even,
           (3n+1)/2    if n is odd.

For a fixed residue r modulo 2^K, the first K shortcut parities are fixed.
Writing n=2^K*q+r, every prefix has the exact affine form

    U^t(n) = A_t*q+b_t,

where A_t=2^(K-t)*3^(number of odd steps).  A class is discharged as soon as
this affine value is strictly below the starting affine value for every q>=0.

This is the map for which the original nested-anchor identity

    U^k(a+2^k*m) = U^k(a)+3^rho*m

is exact, provided the first k parities of a are used and rho is their number
of odd steps.

Finite coverage is a certificate only at the displayed depth.  Unresolved
classes are not counterexamples.
"""

from collections import Counter


def shortcut(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def stopping_time(n, limit):
    """First t<=limit with U^t(n)<n, or None."""
    cur = n
    for step in range(1, limit + 1):
        cur = shortcut(cur)
        if cur < n:
            return step
    return None


def prefix_affine(r, K):
    """Yield exact affine states for n=2^K*q+r through the fixed K-bit prefix."""
    A = 1 << K
    b = r
    odd_count = 0
    for step in range(1, K + 1):
        if b % 2:
            A = 3 * A // 2
            b = (3 * b + 1) // 2
            odd_count += 1
        else:
            A //= 2
            b //= 2
        yield step, A, b, odd_count


def residue_certificate(r, K):
    """Try to prove U^t(2^K*q+r) < 2^K*q+r uniformly for q>=0."""
    start_A = 1 << K
    for step, A, b, odd_count in prefix_affine(r, K):
        if A < start_A and b < r:
            return {
                "status": "proved",
                "step": step,
                "A": A,
                "b": b,
                "odd_count": odd_count,
            }
        if A < start_A and b == r and r == 1:
            return {
                "status": "proved",
                "step": step,
                "A": A,
                "b": b,
                "odd_count": odd_count,
            }
    return {
        "status": "unresolved",
        "step": K,
        "A": A,
        "b": b,
        "odd_count": odd_count,
    }


def verify_anchor_identity(limit=1000):
    for a in range(1, limit + 1):
        x = a
        for k in range(1, 16):
            odd_count = 0
            y = a
            for _ in range(k):
                odd_count += y % 2
                y = shortcut(y)
            for m in range(8):
                lifted = a + (1 << k) * m
                z = lifted
                for _ in range(k):
                    z = shortcut(z)
                assert z == y + pow(3, odd_count) * m
            x = shortcut(x)
    return True


def verify_tree_equivalence(max_K=16):
    """For r>1, discharge by K is equivalent to concrete descent by K."""
    for K in range(1, max_K + 1):
        for r in range(1, 1 << K, 2):
            result = residue_certificate(r, K)
            if r == 1:
                # The induction base is accepted although 1 lies on its cycle.
                continue
            concrete = stopping_time(r, K)
            assert (result["status"] == "proved") == (concrete is not None)
            if concrete is not None:
                assert result["step"] == concrete
    return True


def all_ones_prefix(K):
    r = (1 << K) - 1
    rows = list(prefix_affine(r, K))
    # The first K parities are odd for the all-ones residue.
    assert all(odd_count == step for step, _A, _b, odd_count in rows)
    return rows[-1]


def summarize(depths=range(8, 23, 2)):
    verify_anchor_identity()
    verify_tree_equivalence()
    print("Shortcut nested-anchor identity: PASS")
    print("Tree/stopping-time equivalence: PASS")
    print()
    for K in depths:
        proved = 0
        unresolved = []
        lengths = Counter()
        for r in range(1, 1 << K, 2):
            result = residue_certificate(r, K)
            if result["status"] == "proved":
                proved += 1
                lengths[result["step"]] += 1
            else:
                unresolved.append((r, result))

        total = 1 << (K - 1)
        mersenne = (1 << K) - 1
        assert any(r == mersenne for r, _ in unresolved)
        _step, A, b, odd_count = all_ones_prefix(K)
        print(
            f"K={K}: proved {proved}/{total} ({100*proved/total:.2f}%), "
            f"unresolved {len(unresolved)}"
        )
        print(
            f"  all-ones endpoint: A={A}, b={b}, odd_count={odd_count}; "
            "nested limit is -1"
        )
        print(f"  common discharge lengths: {lengths.most_common(8)}")
        primitive = [
            (step, count // (1 << (K - step)))
            for step, count in sorted(lengths.items())
        ]
        print(f"  primitive prefix leaves by depth: {primitive}")
        print(
            "  first unresolved:",
            ", ".join(str(r) for r, _ in unresolved[:16]),
        )


if __name__ == "__main__":
    summarize()
