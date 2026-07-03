#!/usr/bin/env python3
"""
Exploration: bad valuation strings as congruence classes of the index n.

For a valuation pattern e with total E, the associated class x=r mod 2^E
intersects the repunit curve a_n=(3^n-1)/2 iff

    3^n == 2r+1 mod 2^(E+1).

When it intersects, it gives residue classes of n modulo the order of 3.
This script counts those surviving n-classes for low-valuation patterns.

Research tool, not a proof.
"""
import math
from collections import defaultdict


THETA = math.log2(3)


def pattern_residue(pattern):
    E = sum(pattern)
    mod = 1 << E
    c = 0
    prefix = 0
    K = len(pattern)
    for i, e in enumerate(pattern):
        c += (3 ** (K - 1 - i)) * (1 << prefix)
        prefix += e
    return (-c * pow(3 ** K, -1, mod)) % mod, E


def gen_patterns(K, max_E, prefix=(), total=0):
    if len(prefix) == K:
        yield prefix
        return
    remaining = K - len(prefix) - 1
    for e in range(1, max_E - total - remaining + 1):
        yield from gen_patterns(K, max_E, prefix + (e,), total + e)


_dlog_cache = {}


def odd_power_log_table(E):
    """
    Return map 3^n mod 2^(E+1) -> n modulo period, for odd n.

    The order of 3 mod 2^(E+1) is 2^(E-1) for E+1>=3.
    We only keep odd n because the Mersenne-repunit reduction uses odd n.
    """
    if E in _dlog_cache:
        return _dlog_cache[E]
    mod = 1 << (E + 1)
    period = 1 if E + 1 <= 2 else 1 << (E - 1)
    table = {}
    cur = 1
    for n in range(period):
        if n > 0:
            cur = (cur * 3) % mod
        if n & 1:
            table[cur] = n
    _dlog_cache[E] = (table, period)
    return table, period


def scan_index_survivors(max_K=12):
    print("== Low-valuation patterns as surviving n-classes ==")
    print("bad means total E <= floor(K log2 3); n is odd.")
    print(
        f"{'K':>3} {'bad pats':>9} {'hit pats':>9} {'max E':>5} "
        f"{'n classes':>10} {'odd modulus':>11} {'density':>9}"
    )
    for K in range(2, max_K + 1):
        max_E = math.floor(K * THETA)
        max_period = 1 << (max_E - 1)
        lifted_classes = set()
        bad = hit = 0
        by_E = defaultdict(int)
        for pat in gen_patterns(K, max_E):
            bad += 1
            r, E = pattern_residue(pat)
            target = (2 * r + 1) % (1 << (E + 1))
            table, period = odd_power_log_table(E)
            n0 = table.get(target)
            if n0 is None:
                continue
            hit += 1
            by_E[E] += 1
            # Lift n0 modulo period to the common max_period.
            for n in range(n0, max_period, period):
                lifted_classes.add(n)
        odd_classes = max_period // 2
        density = len(lifted_classes) / odd_classes if odd_classes else 0
        print(
            f"{K:3d} {bad:9d} {hit:9d} {max_E:5d} "
            f"{len(lifted_classes):10d} {odd_classes:11d} {density:9.5f}"
        )
        tail = ", ".join(f"E{E}:{by_E[E]}" for E in sorted(by_E)[-4:])
        print(f"      hit distribution by total E: {tail}")


def scan_prefix_nested(max_K=14):
    """
    Track n-classes that survive every prefix lower-tail bound:
    E_j <= floor(j log2 3) for all j<=K.

    This is stronger than final-total badness and closer to a shadowing
    automaton. It still ignores the n-dependent initial height gap.
    """
    print("\n== Prefix-bad surviving n-classes ==")
    print("Require every prefix E_j <= floor(j log2 3).")
    print(f"{'K':>3} {'patterns':>9} {'hit pats':>9} {'max E':>5} {'n-density':>10}")
    for K in range(2, max_K + 1):
        bounds = [math.floor(j * THETA) for j in range(K + 1)]
        max_E = bounds[K]
        max_period = 1 << (max_E - 1)
        lifted_classes = set()
        patterns = hit = 0

        def rec(prefix, total):
            nonlocal patterns, hit
            j = len(prefix)
            if j == K:
                patterns += 1
                r, E = pattern_residue(prefix)
                target = (2 * r + 1) % (1 << (E + 1))
                table, period = odd_power_log_table(E)
                n0 = table.get(target)
                if n0 is None:
                    return
                hit += 1
                for n in range(n0, max_period, period):
                    lifted_classes.add(n)
                return
            remaining = K - j - 1
            max_next = bounds[j + 1] - total
            for e in range(1, max_next + 1):
                # Ensure the remaining slots can carry at least 1 each and
                # still meet the final bound.
                if total + e + remaining <= max_E:
                    rec(prefix + (e,), total + e)

        rec((), 0)
        odd_classes = max_period // 2
        density = len(lifted_classes) / odd_classes if odd_classes else 0
        print(f"{K:3d} {patterns:9d} {hit:9d} {max_E:5d} {density:10.6f}")


if __name__ == "__main__":
    scan_prefix_nested()
    scan_index_survivors()
