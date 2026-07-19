#!/usr/bin/env python3
"""Probe rigorous pre-descent rho cap from U^H < T => 3^{rho} a_n < T 2^H."""

from __future__ import annotations

import argparse
import math


def v2(v: int) -> int:
    return (v & -v).bit_length() - 1


def descent_data(n: int) -> dict:
    t = 5 * n - 2
    threshold = (1 << n) - 1
    a_n = (3**n - 1) // 2
    x = a_n
    steps = 0
    odd = 0
    while True:
        raw = 3 * x + 1
        e = v2(raw)
        for division in range(1, e + 1):
            steps += 1
            if division == 1:
                odd += 1
            cand = raw >> division
            if cand < threshold:
                # exact: 3^odd * a_n + P = cand * 2^steps for some P>=0
                # so 3^odd * a_n < threshold * 2^steps
                return {
                    "n": n,
                    "H": steps,
                    "t": t,
                    "rho_pre": odd,
                    "cap": (11 * n) // 4,
                    "a_n": a_n,
                    "T": threshold,
                    "endpoint": cand,
                }
            x = cand
        # completed payout without crossing — continue with x = raw>>e already set
        # (loop structure: x updated inside; if no cross, x is final candidate)


def descent_data_fixed(n: int) -> dict:
    t = 5 * n - 2
    threshold = (1 << n) - 1
    a_n = (3**n - 1) // 2
    x = a_n
    steps = 0
    odd = 0
    while x >= threshold:
        raw = 3 * x + 1
        e = v2(raw)
        for division in range(1, e + 1):
            steps += 1
            if division == 1:
                odd += 1
            cand = raw >> division
            if cand < threshold:
                log_bound = math.log(threshold * (1 << steps) / a_n) / math.log(3)
                return {
                    "n": n,
                    "H": steps,
                    "t": t,
                    "rho_pre": odd,
                    "log_bound": log_bound,
                    "floor_bound": math.floor(log_bound),
                    "cap": (11 * n) // 4,
                    "room_post_for_911": (11 * t + 9) // 20 - odd,
                    "post_len": t - steps,
                }
            x = cand
    raise AssertionError("no descent")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=2001)
    args = parser.parse_args()

    print("n | H | rho_pre | floor_log_bound | slack_bound | post_len | room_911 | post_dens_max_for_911")
    tight = []
    for n in range(7, args.limit + 1, 2):
        if n == 23:
            continue  # H=t saturator
        r = descent_data_fixed(n)
        slack_b = r["floor_bound"] - r["rho_pre"]
        room = r["room_post_for_911"]
        post = r["post_len"]
        dens_max = room / post if post else None
        if dens_max is not None and dens_max < 0.55:
            tight.append((dens_max, n, r["rho_pre"], room, post, r["H"]))
        if n in (7, 17, 25, 31, 43, 131, 193, 501, 1001, 2001) or n < 40:
            print(
                f"{n:4d} | {r['H']:5d} | {r['rho_pre']:5d} | {r['floor_bound']:5d} | "
                f"{slack_b:4d} | {post:5d} | {room:5d} | {dens_max}"
            )

    tight.sort()
    print("20 tightest required post dens_max for 911:", tight[:20])
    if tight:
        print("min dens_max", tight[0])
        print("count dens_max < 0.5", sum(1 for z in tight if z[0] < 0.5))
        print("count dens_max < 0.52", sum(1 for z in tight if z[0] < 0.52))


if __name__ == "__main__":
    main()
