#!/usr/bin/env python3
"""Probe SD-L1 later-landing gates: max h/v growth and s>1 height points.

Avenue A Remaining attack: exclude h>=n+2 (e=1 L=1) and v>=n+3 (e=2 L=1)
on later landings. Diagnostics only.
"""

from __future__ import annotations

import argparse


def v2(value: int) -> int:
    return (value & -value).bit_length() - 1


def scan_gates(n: int) -> dict[str, int]:
    threshold = (1 << n) - 1
    x = (3**n - 1) // 2
    max_h = v2(x + 1)
    max_v = v2(x - 1)
    max_e = 0
    max_h_step = 0
    max_v_step = 0
    for step in range(0, 200_000):
        if step > 0 and x < threshold:
            return {
                "n": n,
                "K": step,
                "max_h": max_h,
                "max_v": max_v,
                "max_e": max_e,
                "h_slack": n + 2 - max_h,
                "v_slack": n + 3 - max_v,
                "max_h_step": max_h_step,
                "max_v_step": max_v_step,
            }
        h = v2(x + 1)
        vv = v2(x - 1)
        if h > max_h:
            max_h = h
            max_h_step = step
        if vv > max_v:
            max_v = vv
            max_v_step = step
        value = 3 * x + 1
        e = v2(value)
        max_e = max(max_e, e)
        x = value >> e
    raise RuntimeError(f"no descent for n={n}")


def scan_s_height_hits(n: int, s_max: int = 16) -> list[tuple[int, int, int]]:
    """Return list of (step, s, x) where x = s*2^{n+2}-1 appears pre-descent."""
    threshold = (1 << n) - 1
    targets = {s * (1 << (n + 2)) - 1: s for s in range(2, s_max + 1)}
    x = (3**n - 1) // 2
    hits: list[tuple[int, int, int]] = []
    for step in range(0, 200_000):
        if step > 0 and x < threshold:
            break
        s = targets.get(x)
        if s is not None:
            hits.append((step, s, x))
        value = 3 * x + 1
        x = value >> v2(value)
    return hits


def explore(limit: int) -> None:
    worst_h = None
    worst_v = None
    print(f"{'n':>5} {'K':>6} {'max_h':>6} {'h_sl':>5} {'max_v':>6} {'v_sl':>5} {'max_e':>5}")
    sample = [n for n in range(3, min(limit, 101) + 1, 2)]
    for n in (201, 471, 1001):
        if n <= limit:
            sample.append(n)
    for n in sample:
        row = scan_gates(n)
        if worst_h is None or row["h_slack"] < worst_h["h_slack"]:
            worst_h = row
        if worst_v is None or row["v_slack"] < worst_v["v_slack"]:
            worst_v = row
        if n <= 61 or n in (101, 201, 471, 1001):
            print(
                f"{n:5d} {row['K']:6d} {row['max_h']:6d} {row['h_slack']:5d} "
                f"{row['max_v']:6d} {row['v_slack']:5d} {row['max_e']:5d}"
            )
    assert worst_h is not None and worst_v is not None
    assert worst_h["h_slack"] >= 1
    assert worst_v["v_slack"] >= 1
    print(
        f"gate slacks: PASS through sampled n<= {limit}; "
        f"worst h_slack={worst_h['h_slack']} at n={worst_h['n']} "
        f"(max_h={worst_h['max_h']}); "
        f"worst v_slack={worst_v['v_slack']} at n={worst_v['n']} "
        f"(max_v={worst_v['max_v']})"
    )

    # Empirical: max_h and max_v grow slowly vs n (suggest O(log n) or bounded).
    # Record max_h / log2(K) style ratios on the sample.
    best_h_over_log = 0.0
    best_n = 3
    import math

    for n in sample:
        row = scan_gates(n)
        if row["K"] <= 1:
            continue
        ratio = row["max_h"] / math.log2(row["K"] + 1)
        if ratio > best_h_over_log:
            best_h_over_log = ratio
            best_n = n
    print(f"max max_h/log2(K+1) ~ {best_h_over_log:.3f} at n={best_n}")

    hits_total = 0
    first_hits: list[tuple[int, int, int]] = []
    for n in range(3, min(limit, 501) + 1, 2):
        hits = scan_s_height_hits(n, s_max=16)
        hits_total += len(hits)
        for step, s, _x in hits[:1]:
            first_hits.append((n, step, s))
    print(
        f"s=2..16 height points x=s*2^(n+2)-1 on pre-descent orbits: "
        f"hits={hits_total} through odd n<={min(limit,501)}"
    )
    if first_hits:
        print("first few:", first_hits[:10])
    else:
        print("no s>=2 height L=1 candidates hit (supports height-gate residual)")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=201)
    return parser.parse_args()


if __name__ == "__main__":
    explore(parse_args().limit)
