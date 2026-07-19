#!/usr/bin/env python3
"""Probe residual odd-density vs Gap SD-K-block-8-17 threshold."""

from __future__ import annotations

import argparse
from collections import Counter


def v2(v: int) -> int:
    return (v & -v).bit_length() - 1


def h_of(x: int) -> int:
    return v2(x + 1)


def residual_stats(n: int) -> dict:
    t = 6 * n
    x = (3**n - 1) // 2
    steps = 0
    raw = 3 * x + 1
    e0 = v2(raw)
    steps += e0
    x = raw >> e0
    while h_of(x) >= 2 and steps < t:
        steps += 1
        x = (3 * x + 1) >> 1
    raw = 3 * x + 1
    e = v2(raw)
    steps += e
    x = raw >> e
    h1 = h_of(x)
    while h_of(x) >= 2 and steps < t:
        steps += 1
        x = (3 * x + 1) >> 1

    O = E = 0
    score = 0
    min_score = 0
    blocks = 0
    max_h = 0
    sum_e = sum_h = 0
    e_hist: Counter[int] = Counter()
    h_hist: Counter[int] = Counter()
    while steps < t:
        raw = 3 * x + 1
        ee = v2(raw)
        rem = t - steps
        if ee > rem:
            O += 1
            E += max(0, rem - 1)
            score += 11 * max(0, rem - 1) - 9
            break
        steps += ee
        O += 1
        E += ee - 1
        x = raw >> ee
        hl = h_of(x)
        rails = 0
        while h_of(x) >= 2 and steps < t:
            steps += 1
            x = (3 * x + 1) >> 1
            rails += 1
            O += 1
        heff = 1 + rails if rails < hl - 1 else hl
        d = 11 * (ee - 1) - 9 * heff
        score += d
        min_score = min(min_score, score)
        blocks += 1
        max_h = max(max_h, heff)
        sum_e += ee
        sum_h += heff
        e_hist[ee] += 1
        h_hist[heff] += 1

    L = O + E
    rest = 11 * E - 9 * O
    need = 9 * h1 - 11
    return {
        "n": n,
        "h1": h1,
        "L": L,
        "O": O,
        "E": E,
        "rest": rest,
        "need": need,
        "dens": O / L if L else None,
        "thresh": (11 * L - need) / (20 * L) if L else None,
        "margin": rest - need,
        "min_partial": min_score,
        "blocks": blocks,
        "avg_e": sum_e / blocks if blocks else None,
        "avg_h": sum_h / blocks if blocks else None,
        "max_h": max_h,
        "e_hist": e_hist,
        "h_hist": h_hist,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=4001)
    args = parser.parse_args()

    for label, pred in [
        ("odd k", lambda k: k % 2 == 1),
        ("k=2 mod 4", lambda k: k % 4 == 2),
        ("all k>=1", lambda k: k >= 1),
    ]:
        worst = None
        dens_list = []
        print(f"=== {label} ===")
        for n in range(17, args.limit + 1, 64):
            k = (n - 17) // 64
            if not pred(k) or k == 0:
                continue
            r = residual_stats(n)
            slack = r["thresh"] - r["dens"]
            dens_list.append(r["dens"])
            if worst is None or slack < worst[0]:
                worst = (slack, r)
        assert worst is not None
        wr = worst[1]
        print(
            f"count={len(dens_list)} dens in "
            f"[{min(dens_list):.4f},{max(dens_list):.4f}] "
            f"mean={sum(dens_list)/len(dens_list):.4f}"
        )
        print(
            f"worst dens-slack={worst[0]:.4f} at n={wr['n']} "
            f"dens={wr['dens']:.4f} thresh={wr['thresh']:.4f} "
            f"avg_e={wr['avg_e']:.3f} avg_h={wr['avg_h']:.3f} "
            f"max_h={wr['max_h']} rest/n={wr['rest']/wr['n']:.3f} "
            f"min_partial={wr['min_partial']}"
        )
        print(f"  e_hist={dict(sorted(wr['e_hist'].items()))}")
        print(f"  h_hist={dict(sorted(wr['h_hist'].items()))}")
        print()

    # Compare total even surplus to a crude 2-adic lower bound:
    # if every residual payout had e>=2, then E >= blocks, O = sum h,
    # and steps L = sum(e+h-1) >= sum(1+h) = blocks + O.
    # rest = 11E-9O >= 11(L-O)-9O = 11L-20O.
    # With E[e]=2, E[h]~?, ...
    print("=== crude: rest vs 2*blocks - 9*(avg excess height) ===")
    for n in [81, 209, 465, 1489, 2001]:
        r = residual_stats(n)
        # If e>=2 always: E >= blocks, but actually E = sum(e-1)
        print(
            f"n={n} blocks={r['blocks']} E={r['E']} O={r['O']} "
            f"E-blocks={r['E']-r['blocks']} rest={r['rest']} need={r['need']}"
        )


if __name__ == "__main__":
    main()
