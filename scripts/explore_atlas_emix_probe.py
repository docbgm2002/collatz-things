#!/usr/bin/env python3
"""Probe whether n=471 (E_mix seed) admits a simple itinerary normal form.

Looks for:
  - eventual entry into mechanical 3/4 language
  - eventual restriction of payout alphabet
  - periodic or ultimately periodic payout-q / gap structure
  - blocked-diffuse recurrence along the actual descent

Evidence only; used by docs/residual-atlas/.
"""

from __future__ import annotations

import argparse
import math
from collections import Counter


THETA = math.log2(3)


def v2(value: int) -> int:
    return (value & -value).bit_length() - 1


def full_tail_word(n: int, max_steps: int) -> tuple[list[int], int, bool]:
    x = (3**n - 1) // 2
    target = 2**n - 1
    word = []
    descended = False
    for _ in range(max_steps):
        value = 3 * x + 1
        e = v2(value)
        x = value >> e
        word.append(e)
        if x < target:
            descended = True
            break
    return word, len(word), descended


def mechanical_suffix_from(word: list[int], start: int) -> bool:
    tail = word[start:]
    events = [(i, e) for i, e in enumerate(tail) if e > 1]
    if len(events) < 3:
        return False
    if any(q != 3 for _, q in events):
        return False
    for (i, _), (j, _) in zip(events, events[1:]):
        if j - i not in (3, 4):
            return False
        if any(e != 1 for e in tail[i + 1 : j]):
            return False
    return True


def earliest_mechanical(word: list[int]) -> int | None:
    for start in range(len(word)):
        if mechanical_suffix_from(word, start):
            return start
    return None


def window_alphabets(word: list[int], window: int) -> list[tuple[int, frozenset[int]]]:
    out = []
    for start in range(0, max(1, len(word) - window + 1), max(1, window // 4)):
        chunk = word[start : start + window]
        payouts = frozenset(e for e in chunk if e > 1)
        out.append((start, payouts))
    return out


def payout_q_string(word: list[int]) -> list[int]:
    return [e for e in word if e > 1]


def longest_repeated_prefix(seq: list[int], max_period: int) -> tuple[int, int]:
    """Return (period, repetitions) for best ultimately-periodic fit at end."""
    best = (0, 0)
    n = len(seq)
    for p in range(1, min(max_period, n // 2) + 1):
        block = seq[-p:]
        reps = 1
        pos = n - p
        while pos - p >= 0 and seq[pos - p : pos] == block:
            reps += 1
            pos -= p
        if reps > best[1]:
            best = (p, reps)
    return best


def report(n: int, max_steps: int) -> None:
    word, steps, descended = full_tail_word(n, max_steps)
    print(f"== E_mix normal-form probe: n={n} ==")
    print(f"steps_used={steps} descended={descended}")
    print(f"full_alphabet={sorted(set(word))}")
    print(f"payout_alphabet={sorted({e for e in word if e > 1})}")
    print(f"payout_counts={dict(Counter(e for e in word if e > 1))}")

    mech = earliest_mechanical(word)
    print(f"earliest_mechanical_3/4_suffix_start={mech}")

    print("sliding payout alphabets (start, alphabet):")
    for start, alphabet in window_alphabets(word, window=40):
        print(f"  {start:4d} {sorted(alphabet)}")

    qs = payout_q_string(word)
    period, reps = longest_repeated_prefix(qs, max_period=24)
    print(f"best_terminal_payout_period={period} repetitions={reps} tail={qs[-period:] if period else []}")

    # gaps between successive payouts
    events = [i for i, e in enumerate(word) if e > 1]
    gaps = [b - a for a, b in zip(events, events[1:])]
    g_period, g_reps = longest_repeated_prefix(gaps, max_period=24)
    print(
        f"best_terminal_gap_period={g_period} repetitions={g_reps} "
        f"tail={gaps[-g_period:] if g_period else []}"
    )
    print(f"gap_alphabet={sorted(set(gaps))}")


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=471)
    parser.add_argument("--max-steps", type=int, default=5000)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    report(args.n, args.max_steps)
