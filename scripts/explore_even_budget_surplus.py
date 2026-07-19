#!/usr/bin/env python3
"""Probe seed-adjusted payout surplus vs landing height (Gap SD-K-even-budget).

Tracks S = (e0-1) + sum((e-1) - (9/11) h_eff) along the length-(5n-2)
itinerary of a_n, and the integer form 11*even - 9*sum_h.
"""

from __future__ import annotations

import argparse


def v2(v: int) -> int:
    return (v & -v).bit_length() - 1


def h_of(x: int) -> int:
    return v2(x + 1)


def surplus_path(n: int, c: float = 9 / 11) -> dict:
    t = 5 * n - 2
    e0 = 1 + v2(n + 1)
    x = (3**n - 1) // 2
    x = (3 * x + 1) >> e0
    steps = e0
    score = float(e0 - 1)
    min_s = score
    min_at = 0
    k = 0
    while steps < t:
        raw = 3 * x + 1
        e = v2(raw)
        rem = t - steps
        if e > rem:
            score += max(0, rem - 1) - c * 1
            k += 1
            if score < min_s:
                min_s = score
                min_at = k
            break
        steps += e
        x = raw >> e
        hl = h_of(x)
        rails = 0
        while h_of(x) >= 2 and steps < t:
            steps += 1
            x = (3 * x + 1) >> 1
            rails += 1
        heff = 1 + rails if rails < hl - 1 else hl
        score += (e - 1) - c * heff
        k += 1
        if score < min_s:
            min_s = score
            min_at = k
    return {
        "n": n,
        "e0": e0,
        "final": score,
        "min_s": min_s,
        "min_at": min_at,
        "blocks": k,
    }


def int_path(n: int) -> dict:
    t = 5 * n - 2
    e0 = 1 + v2(n + 1)
    x = (3**n - 1) // 2
    x = (3 * x + 1) >> e0
    steps = e0
    even = e0 - 1
    sum_h = 0
    score = 11 * even
    min_sc = score
    while steps < t:
        raw = 3 * x + 1
        e = v2(raw)
        rem = t - steps
        if e > rem:
            even += max(0, rem - 1)
            sum_h += 1
            score = 11 * even - 9 * sum_h
            if score < min_sc:
                min_sc = score
            break
        steps += e
        even += e - 1
        x = raw >> e
        hl = h_of(x)
        rails = 0
        while h_of(x) >= 2 and steps < t:
            steps += 1
            x = (3 * x + 1) >> 1
            rails += 1
        heff = 1 + rails if rails < hl - 1 else hl
        sum_h += heff
        score = 11 * even - 9 * sum_h
        if score < min_sc:
            min_sc = score
    return {
        "n": n,
        "even": even,
        "sum_h": sum_h,
        "score": score,
        "min_sc": min_sc,
        "ok": 11 * even >= 9 * sum_h,
        "rho": 1 + sum_h,
        "cap": (11 * n) // 4,
    }


def nine_eleven_ok(n: int) -> bool:
    """11*(t-rho) >= 9*(rho-1), equivalent to rho <= (11t+9)/20."""
    t = 5 * n - 2
    ip = int_path(n)
    rho = ip["rho"]
    even = t - rho
    return 11 * even >= 9 * (rho - 1)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=2001)
    args = parser.parse_args()
    limit = args.limit

    print("selected paths (float surplus):")
    for n in (7, 11, 17, 23, 25, 31, 43, 131, 193):
        if n > limit:
            break
        r = surplus_path(n)
        print(
            f"  n={n} e0={r['e0']} final={r['final']:.4f} "
            f"minS={r['min_s']:.4f} at={r['min_at']}/{r['blocks']}"
        )

    neg_min = []
    bad_int = []
    bad_911 = []
    worst_min = None
    worst_final_ratio = None
    for n in range(7, limit + 1, 2):
        r = surplus_path(n)
        if r["min_s"] < -1e-9:
            neg_min.append((n, r["min_s"], r["min_at"], r["final"]))
        ip = int_path(n)
        if not ip["ok"]:
            bad_int.append(n)
        if not nine_eleven_ok(n):
            bad_911.append(n)
        if worst_min is None or ip["min_sc"] < worst_min[0]:
            worst_min = (ip["min_sc"], n, ip["score"], ip["even"], ip["sum_h"])
        ratio = ip["even"] / ip["sum_h"] if ip["sum_h"] else 99.0
        if worst_final_ratio is None or ratio < worst_final_ratio[0]:
            worst_final_ratio = (ratio, n, ip["even"], ip["sum_h"], ip["rho"], ip["cap"])

    print(f"paths with minS<0 through {limit}: {len(neg_min)}")
    if neg_min:
        print("  sample:", neg_min[:12])
    print(f"integer 11*even >= 9*sum_h fails: {bad_int}")
    print(f"11*(t-rho) >= 9*(rho-1) fails: {bad_911}")
    print(f"worst running 11e-9h min: {worst_min}")
    print(f"worst final even/sum_h: {worst_final_ratio}")

    # Implication check: criterion => rho <= floor((11t+9)/20)
    imply_fail = []
    for n in range(7, limit + 1, 2):
        ip = int_path(n)
        t = 5 * n - 2
        if nine_eleven_ok(n):
            bound = (11 * t + 9) // 20
            if ip["rho"] > bound:
                imply_fail.append((n, ip["rho"], bound, ip["cap"]))
            if ip["rho"] > ip["cap"]:
                imply_fail.append(("cap", n, ip["rho"], ip["cap"]))
    print(f"implication rho<=floor((11t+9)/20) fails: {imply_fail[:10]} count={len(imply_fail)}")


if __name__ == "__main__":
    main()
