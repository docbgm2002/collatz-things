#!/usr/bin/env python3
"""Probe Gap SD-K-911-6-strong on the hard case e0=2 (n ≡ 1 mod 4).

Tracks block contributions Delta = 11*(e-1) - 9*h_eff after a correct
seed + rail prefix, and compares final score to the target >= 11.
"""

from __future__ import annotations

import argparse
import statistics as st


def v2(v: int) -> int:
    return (v & -v).bit_length() - 1


def h_of(x: int) -> int:
    return v2(x + 1)


def score_and_blocks(n: int) -> dict:
    t = 6 * n
    e0 = 1 + v2(n + 1)
    x = (3**n - 1) // 2
    # seed payout
    raw = 3 * x + 1
    assert v2(raw) == e0
    x = raw >> e0
    steps = e0
    # rails after seed to next h=1
    while h_of(x) >= 2 and steps < t:
        raw = 3 * x + 1
        assert v2(raw) == 1
        steps += 1
        x = raw >> 1
    seed_rails = steps - e0

    deltas: list[int] = []
    es: list[int] = []
    hs: list[int] = []
    while steps < t:
        assert h_of(x) == 1 or steps >= t
        raw = 3 * x + 1
        e = v2(raw)
        rem = t - steps
        if e > rem:
            heff = 1
            em1 = max(0, rem - 1)
            deltas.append(11 * em1 - 9 * heff)
            es.append(e)
            hs.append(heff)
            steps = t
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
        deltas.append(11 * (e - 1) - 9 * heff)
        es.append(e)
        hs.append(heff)

    # Full-window score from direct odd/even count
    xx = (3**n - 1) // 2
    odd = even = stps = 0
    while stps < t:
        raw = 3 * xx + 1
        e = v2(raw)
        for d in range(1, e + 1):
            stps += 1
            if d == 1:
                odd += 1
            else:
                even += 1
            xx = raw >> d
            if stps >= t:
                break
        else:
            continue
        break
    score = 11 * even - 9 * (odd - 1)
    block_sum = sum(deltas)
    # Lemma SD-K-score-split: score = 11*(e0-1) + block_sum - 9*seed_rails
    reconstructed = 11 * (e0 - 1) + block_sum - 9 * seed_rails
    return {
        "n": n,
        "e0": e0,
        "seed_rails": seed_rails,
        "score": score,
        "block_sum": block_sum,
        "reconstructed": reconstructed,
        "blocks": len(deltas),
        "deltas": deltas,
        "es": es,
        "hs": hs,
        "neg_blocks": sum(1 for d in deltas if d < 0),
        "min_delta": min(deltas) if deltas else 0,
        "running_min": _running_min(11 * (e0 - 1), deltas),
        "frac_e2": sum(1 for e in es if e == 2) / max(1, len(es)),
        "frac_h1": sum(1 for h in hs if h == 1) / max(1, len(hs)),
        "mean_delta": st.mean(deltas) if deltas else 0.0,
    }


def _running_min(start: int, deltas: list[int]) -> int:
    s = start
    mn = s
    for d in deltas:
        s += d
        if s < mn:
            mn = s
    return mn


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=2001)
    args = parser.parse_args()

    hard = []
    easy = []
    mismatch = []
    for n in range(7, args.limit + 1, 2):
        if n == 11:
            continue
        r = score_and_blocks(n)
        if r["reconstructed"] != r["score"]:
            # seed-rail odds affect height accounting; track mismatch
            mismatch.append((n, r["score"], r["reconstructed"], r["seed_rails"]))
        if r["e0"] == 2:
            hard.append(r)
        else:
            easy.append(r)

    print(f"e0=2 count={len(hard)}; e0>=3 count={len(easy)}")
    print(f"score vs reconstructed mismatches: {len(mismatch)} sample={mismatch[:5]}")

    hard_by_score = sorted(hard, key=lambda r: r["score"])
    print("tightest e0=2 scores:")
    for r in hard_by_score[:10]:
        print(
            f"  n={r['n']} score={r['score']} block_sum={r['block_sum']} "
            f"recon={r['reconstructed']} seed_rails={r['seed_rails']} "
            f"minD={r['min_delta']} runmin={r['running_min']} "
            f"meanD={r['mean_delta']:.3f} frac_e2={r['frac_e2']:.3f} "
            f"frac_h1={r['frac_h1']:.3f}"
        )

    # For e0=2: need block_sum >= 0 for reconstructed seed+blocks = 11 + block_sum >= 11
    # But mismatch may exist due to seed rails in height-count
    print(
        "e0=2 block_sum>=0 count",
        sum(1 for r in hard if r["block_sum"] >= 0),
        "/",
        len(hard),
    )
    print(
        "e0=2 mean mean_delta",
        st.mean(r["mean_delta"] for r in hard),
        "min mean_delta",
        min(r["mean_delta"] for r in hard),
    )

    # Pair (e,h) frequency on e0=2 orbits
    from collections import Counter

    joint: Counter[tuple[int, int]] = Counter()
    for r in hard:
        for e, h in zip(r["es"], r["hs"]):
            joint[(min(e, 8), min(h, 8))] += 1
    print("top (e,h) for e0=2:")
    for k, v in joint.most_common(12):
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
