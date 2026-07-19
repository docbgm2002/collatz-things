#!/usr/bin/env python3
"""L4 peak--crash / replenishment probe inside the 3/4-block language.

Builds hand-made {3,4}-block words aimed at the P-L4 falsifier shape:
  deep negative drift with large IEF15 partition Z, yet bounded IEF18/IEF21
  directional margins on natural periodic-prefix approximants.

Local to L_{3/4} after atlas demote-1. Evidence only.
"""

from __future__ import annotations

import argparse
from math import log2

from explore_balanced_q3_residual_axes import (
    analyse,
    block_directional_budget,
    cumulative_drift,
    drift_partition,
)
from explore_balanced_q3_sturmian_intercepts import mechanical_word


C = log2(3 / 2)
B_X = 64 * 1_000_000 / 65
INC4 = C * 4 - 2  # ≈ +0.339
INC3 = C * 3 - 2  # ≈ -0.245


def path_SZ(word: list[int]):
    cumulative = 0.0
    partition = 0.0
    rows = []
    for index, block in enumerate(word, start=1):
        increment = C * block - 2
        cumulative += increment
        partition = 1.0 + (2.0**increment) * partition
        rows.append((index, cumulative, partition, cumulative / index))
    return rows


def deepest_negative(rows, min_depth: float = 1.0):
    return [row for row in rows if row[1] <= -min_depth]


def make_peak_crash(peak_fours: int, crash_threes: int, flat_mixed: int) -> list[int]:
    """Climb on 4s, crash on 3s, then alternate 3/4 near critically."""
    word = [4] * peak_fours + [3] * crash_threes
    # near-critical filler: mechanical-like 3,4,3,4... but biased to hold low
    for i in range(flat_mixed):
        word.append(3 if i % 2 == 0 else 4)
    return word


def make_long_negative_sojourn(depth_threes: int, sojourn: int, fours_ratio: float) -> list[int]:
    """Drop with 3s, then a long mixed sojourn with prescribed 4-density."""
    word = [3] * depth_threes
    # fours_ratio ~ critical density of 4s for zero mean:
    # p*INC4 + (1-p)*INC3 = 0 => p = -INC3/(INC4-INC3) ≈ 0.420
    period = 100
    fours_per = max(1, min(period - 1, round(fours_ratio * period)))
    pattern = [4] * fours_per + [3] * (period - fours_per)
    while len(word) < depth_threes + sojourn:
        word.extend(pattern)
    return word[: depth_threes + sojourn]


def make_irregular_neg_sojourn(depth_threes: int, sojourn: int, seed: int = 1) -> list[int]:
    """Drop, then an aperiodic near-critical sojourn (xorshift 3/4)."""
    word = [3] * depth_threes
    state = seed & 0xFFFFFFFF
    # target density of 4s near critical
    threshold = int((-INC3 / (INC4 - INC3)) * (1 << 32))
    for _ in range(sojourn):
        state ^= (state << 13) & 0xFFFFFFFF
        state ^= (state >> 17) & 0xFFFFFFFF
        state ^= (state << 5) & 0xFFFFFFFF
        state &= 0xFFFFFFFF
        word.append(4 if state < threshold else 3)
    return word


def make_spike_train(spikes: int, spike_fours: int, valley_threes: int) -> list[int]:
    """Repeated peak/valley to inflate Z via many near-equal visits."""
    word = []
    for _ in range(spikes):
        word.extend([4] * spike_fours)
        word.extend([3] * valley_threes)
    return word


def report_family(name: str, word: list[int], caps: list[int]) -> None:
    rows = path_SZ(word)
    _, final_Z, _, _ = drift_partition(word)
    S = rows[-1][1]
    neg = deepest_negative(rows, min_depth=5.0)
    # Z at points that are both deep and late (true replenishment test)
    late = max(1, len(word) // 2)
    deep_late = [row for row in neg if row[0] >= late]
    max_Z_deep_late = max((z for _, s, z, _ in deep_late), default=0.0)
    max_Z_on_deep = max((z for _, s, z, _ in neg), default=0.0)
    min_S = min(s for _, s, _, _ in rows)
    print(f"\n== {name} ==")
    print(
        f"blocks={len(word)} final_S={S:.6f} final_S/L={S/len(word):.8f} "
        f"final_Z={final_Z:.6f} min_S={min_S:.6f} "
        f"max_Z_on_S<=-5={max_Z_on_deep:.6f} "
        f"max_Z_deep_late={max_Z_deep_late:.6f} B_X={B_X:.3f}"
    )
    deep_sorted = sorted(neg, key=lambda row: row[1])[:3]
    if deep_sorted:
        print("deepest points (L, S, Z, S/L):")
        for L, s, z, rate in deep_sorted:
            print(f"  L={L:5d} S={s:10.4f} Z={z:12.4f} S/L={rate:.8f}")
    if deep_late:
        top_late = sorted(deep_late, key=lambda row: row[2], reverse=True)[:3]
        print("largest-Z deep late points:")
        for L, s, z, rate in top_late:
            print(f"  L={L:5d} S={s:10.4f} Z={z:12.4f} S/L={rate:.8f}")

    _, margin_rows = analyse(word, caps)
    print("approximant margins:")
    margins = []
    for (
        cap,
        ratio,
        agreement,
        preperiod,
        period,
        _env,
        _cr,
        _bcost,
        _dr,
        _loss,
        loss_ratio,
        _k,
        coarse,
        directional,
        exact,
    ) in margin_rows:
        margins.append(directional)
        print(
            f"  cap={cap:4d} agr={agreement:4d} U={preperiod:3d} V={period:3d} "
            f"ratio={ratio:.3f} dir_margin={directional:10.2f} "
            f"exact_margin={exact:8.1f} Hloss_ratio={loss_ratio:.5f} "
            f"coarse={coarse:10.2f}"
        )

    large_Z = max_Z_deep_late > B_X
    # In R, coordinate D forbids divergent margins. Treat "all caps >> 0 and
    # increasing" as discharged-by-IEF18, not a falsifier of L4.
    min_margin = min(margins) if margins else 0.0
    growing = len(margins) >= 2 and margins[-1] > margins[0] + 50
    discharged_like = min_margin > 20
    print(
        f"L4_read: large_Z_deep_late={large_Z} min_dir_margin={min_margin:.2f} "
        f"margins_grow={growing} discharged_like={discharged_like} "
        f"verdict="
        f"{'candidate_falsifier' if large_Z and not discharged_like else 'no_falsifier'}"
    )


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--caps", default="32,64,128,256")
    parser.add_argument("--sojourn", type=int, default=20000)
    return parser.parse_args()


def main():
    args = parse_args()
    caps = [int(x) for x in args.caps.split(",")]
    print("== Atlas L4 peak-crash probe (local to L_{3/4}) ==")
    crit = -INC3 / (INC4 - INC3)
    print(f"INC4={INC4:.6f} INC3={INC3:.6f} critical_four_density~={crit:.6f}")
    print(f"B_X={B_X:.6f}")

    families = {
        "peak_crash_short_flat": make_peak_crash(80, 200, 400),
        "peak_crash_long_flat": make_peak_crash(200, 500, 5000),
        "long_neg_sojourn_critical": make_long_negative_sojourn(
            200, args.sojourn, -INC3 / (INC4 - INC3)
        ),
        "long_neg_sojourn_slight_neg": make_long_negative_sojourn(
            200, args.sojourn, 0.35
        ),
        "irregular_neg_sojourn": make_irregular_neg_sojourn(50, args.sojourn),
        "spike_train": make_spike_train(40, 30, 50),
        "mechanical_control": mechanical_word(min(args.sojourn, 5000), 0.0, 80),
    }
    for name, word in families.items():
        report_family(name, word, caps)


if __name__ == "__main__":
    main()
