#!/usr/bin/env python3
"""
Exploration: intersect low-valuation Terras patterns with the repunit curve.

A K-step valuation pattern e=(e_0,...,e_{K-1}) with total E determines one
odd residue class modulo 2^E.  The repunit a_n=(3^n-1)/2 lies in that class iff

    3^n == 2r + 1  (mod 2^(E+1)).

This script enumerates low-total-valuation patterns for small windows and asks
how often they are compatible with the repunit curve. Research tool, not proof.
"""
import math
from collections import defaultdict


THETA = math.log2(3)


def v2(n):
    return (n & -n).bit_length() - 1 if n else 10 ** 9


def f_with_e(x):
    t = 3 * x + 1
    e = v2(t)
    return t >> e, e


def a(n):
    return (3 ** n - 1) // 2


def log2_int(n):
    bits = n.bit_length()
    if bits <= 1024:
        return math.log2(n)
    shift = bits - 1024
    return shift + math.log2(n >> shift)


def pattern_residue(pattern):
    """Return (r, E) where pattern is the unique odd class r mod 2^E."""
    E = sum(pattern)
    mod = 1 << E
    c = 0
    prefix = 0
    K = len(pattern)
    for i, e in enumerate(pattern):
        c += (3 ** (K - 1 - i)) * (1 << prefix)
        prefix += e
    inv = pow(3 ** K, -1, mod)
    return (-c * inv) % mod, E


def gen_patterns(K, max_E, prefix=(), total=0):
    """Generate positive integer patterns of length K with sum <= max_E."""
    if len(prefix) == K:
        yield prefix
        return
    remaining = K - len(prefix) - 1
    # Leave at least 1 for every remaining valuation.
    for e in range(1, max_E - total - remaining + 1):
        yield from gen_patterns(K, max_E, prefix + (e,), total + e)


def actual_tail_pattern(n, K):
    x = a(n)
    out = []
    for _ in range(K):
        x, e = f_with_e(x)
        out.append(e)
    return tuple(out)


def gap_bits(n):
    return log2_int(a(n)) - log2_int((1 << n) - 1)


_curve_cache = {}


def curve_targets(E):
    """All values 3^n mod 2^(E+1) for odd n in one period."""
    if E in _curve_cache:
        return _curve_cache[E]
    mod = 1 << (E + 1)
    period = 1 if E + 1 <= 2 else 1 << (E - 1)
    vals = set()
    cur = 1
    for n in range(period):
        if n > 0:
            cur = (cur * 3) % mod
        if n % 2 == 1:
            vals.add(cur)
    _curve_cache[E] = vals
    return vals


def scan_small_windows(max_K=12):
    print("== Bad-pattern intersection with repunit curve ==")
    print("bad means E <= floor(K log2(3)); no n-specific height gap included")
    print(f"{'K':>3} {'bad pats':>9} {'classes':>8} {'curve hits':>10} {'hit pats':>8}")
    for K in range(2, max_K + 1):
        max_E = math.floor(K * THETA)
        class_by_E = defaultdict(set)
        hit_patterns = 0
        hit_residues = set()
        total = 0
        curve_by_E = {}
        for pat in gen_patterns(K, max_E):
            total += 1
            r, E = pattern_residue(pat)
            class_by_E[E].add(r)
            if E not in curve_by_E:
                curve_by_E[E] = curve_targets(E)
            if (2 * r + 1) % (1 << (E + 1)) in curve_by_E[E]:
                hit_patterns += 1
                hit_residues.add((E, r))
        classes = sum(len(s) for s in class_by_E.values())
        print(f"{K:3d} {total:9d} {classes:8d} {len(hit_residues):10d} {hit_patterns:8d}")


def scan_actual_repunit_prefix(limit=301, c=3):
    print(f"\n== Actual repunit tail: lower-tail membership through K=floor({c}n) ==")
    print("For each n, report the minimum prefix surplus before descent.")
    print(f"{'n':>4} {'sigma':>6} {'min raw':>9} {'at K':>6} {'actual E@min':>12}")
    worst = (10 ** 9, 0, 0, 0)
    for n in range(7, limit + 1, 2):
        target = (1 << n) - 1
        x = a(n)
        E = 0
        min_raw = 10 ** 9
        min_K = 0
        min_E = 0
        sigma = None
        gap = gap_bits(n)
        for K in range(1, int(c * n) + 1):
            x, e = f_with_e(x)
            E += e
            raw = E - THETA * K - gap
            if raw < min_raw:
                min_raw = raw
                min_K = K
                min_E = E
            if sigma is None and x < target:
                sigma = K
                break
        if min_raw < worst[0]:
            worst = (min_raw, n, min_K, min_E)
        if n <= 51 or min_raw < -20:
            print(f"{n:4d} {sigma or -1:6d} {min_raw:9.3f} {min_K:6d} {min_E:12d}")
    print(
        f"  worst minimum surplus up to {limit}: {worst[0]:.3f} "
        f"at n={worst[1]}, K={worst[2]}, E={worst[3]}"
    )


def first_step_residue_classes(limit=64):
    print("\n== First-step forced payout by n modulo powers of two ==")
    print("v2(3a_n+1)=1+v2(n+1), so high first payout occurs at n == -1 mod 2^q.")
    for q in range(1, 8):
        hits = [n for n in range(1, limit + 1, 2) if v2(n + 1) >= q]
        print(f"  q={q}: n == {((1 << q) - 1)} mod {1<<q}; hits <= {limit}: {hits[:8]}")


def scan_forced_first_step(max_K=12):
    print("\n== Bad patterns with forced first repunit payout ==")
    print("For compatible n, require e0 = 1 + v2(n+1), checked over the curve period.")
    print(f"{'K':>3} {'bad pats':>9} {'curve hits':>10} {'forced hits':>12}")
    for K in range(2, max_K + 1):
        max_E = math.floor(K * THETA)
        bad = curve_hit = forced_hit = 0
        n_cache = {}
        for pat in gen_patterns(K, max_E):
            bad += 1
            r, E = pattern_residue(pat)
            mod = 1 << (E + 1)
            target = (2 * r + 1) % mod
            period = 1 if E + 1 <= 2 else 1 << (E - 1)
            if E not in n_cache:
                cur = 1
                by_target = defaultdict(list)
                for n in range(period):
                    if n > 0:
                        cur = (cur * 3) % mod
                    if n % 2 == 1:
                        by_target[cur].append(n)
                n_cache[E] = by_target
            hits = n_cache[E].get(target, [])
            if hits:
                curve_hit += 1
                if any(pat[0] == 1 + v2(n + 1) for n in hits):
                    forced_hit += 1
        print(f"{K:3d} {bad:9d} {curve_hit:10d} {forced_hit:12d}")


if __name__ == "__main__":
    scan_small_windows()
    scan_actual_repunit_prefix()
    first_step_residue_classes()
    scan_forced_first_step()
