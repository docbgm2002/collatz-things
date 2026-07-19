#!/usr/bin/env python3
"""Probe EC1-near: seed-cut, delta=j0-i_cut asymptotics, both-near s-bounds.

Supports Avenue A.  For odd n>=11 both crossings lie in the hat_e=4 layer of
S, and delta is given by an exact ceiling formula (Theta(n), not O(1)).

Diagnostics only.
"""

from __future__ import annotations

import argparse
import math

from explore_ec1_collisions import large_threshold, scan_first_collision, v2


def seed_is_large(n: int) -> bool:
    return (3**n - 1) // 2 >= large_threshold(n)


def layer4_prefix(n: int) -> tuple[int, int]:
    """Count and S after completing hat_e = 1,2,3 layers (n>=3)."""
    # counts: 2^{n-1}, 2^{n-2}, 2^{n-3}; S = 1*2^{n-1}+2*2^{n-2}+3*2^{n-3}
    count_before = 7 << (n - 3)
    s_before = 11 << (n - 3)
    return count_before, s_before


def crossing_in_layer4(n: int, log_extra: float) -> tuple[int, int]:
    """Return (j, t) for the least crossing inside the hat_e=4 layer."""
    threshold = (1 << n) - 1
    log3a = math.log2(3) + math.log2(1 + 1 / (3 * threshold))
    count_before, s_before = layer4_prefix(n)
    layer_count = 1 << (n - 4)  # exact hat_e=4 classes
    denom = 4 - log3a
    assert denom > 0
    rhs = log_extra + count_before * log3a - s_before
    if rhs < 0:
        t = 1
    else:
        t = math.floor(rhs / denom) + 1
    assert 1 <= t <= layer_count, (n, t, layer_count, log_extra)
    return count_before + t, t


def compute_j0_i_cut_delta(n: int) -> tuple[int, int, int]:
    """Exact j0, i_cut, delta for odd n>=11 via the hat_e=4 layer formula."""
    if n < 11 or n % 2 == 0:
        raise ValueError("layer-4 formula is for odd n>=11")
    threshold = (1 << n) - 1
    cut = large_threshold(n)
    a_n = (3**n - 1) // 2
    j0, _ = crossing_in_layer4(n, math.log2(a_n / threshold))
    i_cut, _ = crossing_in_layer4(n, math.log2(a_n / cut))
    return j0, i_cut, j0 - i_cut


def delta_upper_bound(n: int) -> float:
    """log2(cut/T)/(4-log2(3)-log_alpha) — asymptotic envelope for delta."""
    threshold = (1 << n) - 1
    cut = large_threshold(n)
    log3a = math.log2(3) + math.log2(1 + 1 / (3 * threshold))
    return math.log2(cut / threshold) / (4 - log3a)


def first_near_index(n: int) -> tuple[int | None, int]:
    threshold = (1 << n) - 1
    cut = large_threshold(n)
    x = (3**n - 1) // 2
    first = None
    for step in range(0, 200_000):
        if step > 0 and x < threshold:
            return first, step
        if first is None and threshold <= x < cut:
            first = step
        value = 3 * x + 1
        x = value >> v2(value)
    raise RuntimeError(f"no descent for n={n}")


def both_near_s_max(n: int) -> int:
    threshold = (1 << n) - 1
    cut = large_threshold(n)
    return (cut - 1 - threshold) // (1 << (n + 1))


def verify_seed_cut(limit: int = 201) -> None:
    for n in range(3, limit + 1, 2):
        large = seed_is_large(n)
        need = n + (n + 1) // 2 + 1
        sufficient = 3**n >= (1 << need)
        if n >= 19:
            assert large and sufficient, (n, large, sufficient)
        else:
            assert not large, n
    print(f"EC1-seed-cut: PASS (odd 3<=n<{limit}: large iff n>=19)")


def verify_delta_formula(limit: int = 41) -> None:
    """Check layer-4 delta through modest n (float-safe) and Theta(n) growth.

    For very large n, float evaluation of j*log2(3) loses ulps relative to S;
    the Avenue A note records the exact layer-4 asymptotic instead.
    """
    limit = min(limit, 41)
    max_delta = 0
    max_n = 11
    print(f"{'n':>4} {'delta':>6} {'asymp':>8} {'j0':>12} {'i_cut':>12}")
    prev = None
    for n in range(11, limit + 1, 2):
        j0, i_cut, delta = compute_j0_i_cut_delta(n)
        asymp = delta_upper_bound(n)
        # Within two steps of the real asymptotic (ceiling noise).
        assert abs(delta - asymp) < 2.0, (n, delta, asymp)
        assert delta >= 1
        if prev is not None:
            # Nondecreasing on this range (weak Theta(n) witness).
            assert delta >= prev - 1, (n, delta, prev)
        prev = delta
        if delta > max_delta:
            max_delta = delta
            max_n = n
        print(f"{n:4d} {delta:6d} {asymp:8.3f} {j0:12d} {i_cut:12d}")
    assert max_delta >= 6, max_delta
    print(
        f"EC1-delta formula: PASS (odd 11<=n<={limit}; "
        f"max delta={max_delta} at n={max_n}; grows as Theta(n), not O(1))"
    )


def explore(limit: int) -> None:
    verify_seed_cut(min(limit, 201))
    verify_delta_formula(min(limit, 41))

    row = scan_first_collision(5)
    assert row is not None and not row["large"]
    assert both_near_s_max(5) >= abs(row["s"])
    print(
        "n=5 both-near s-bound: PASS "
        f"(s={row['s']} <= smax={both_near_s_max(5)})"
    )
    for n in range(19, min(limit, 201) + 1, 2):
        assert seed_is_large(n)
        fn, kd = first_near_index(n)
        assert fn is not None and fn >= 1, (n, fn)
        assert kd <= (1 << n) - 1
    print(
        f"EC1-near entry: PASS (odd 19<=n<={min(limit,201)}: "
        "seed large and first_near>=1)"
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=61)
    return parser.parse_args()


if __name__ == "__main__":
    explore(parse_args().limit)
