#!/usr/bin/env python3
"""Atlas side-project diagnostic: blocked-diffuse vs 3/4-block language.

Extracts the valuation word of a named repunit tail through a record depth,
reports payout gaps, and checks whether the word is a PCD8-style mechanical
3/4-block word (after an optional finite preperiod).

Evidence only; not a proof. Used by docs/residual-atlas/.
"""

from __future__ import annotations

import argparse
import math
from collections import Counter


THETA = math.log2(3)
C = math.log2(3 / 2)


def v2(value: int) -> int:
    return (value & -value).bit_length() - 1


def valuation_word(n: int, steps: int) -> list[int]:
    x = (3**n - 1) // 2
    word = []
    for _ in range(steps):
        value = 3 * x + 1
        e = v2(value)
        x = value >> e
        word.append(e)
    return word


def payout_events(word: list[int]) -> list[tuple[int, int]]:
    """Return (step_index, q) for every e > 1."""
    return [(i, e) for i, e in enumerate(word) if e > 1]


def gaps_between_payouts(events: list[tuple[int, int]]) -> list[int]:
    """Step gaps between consecutive payouts (including intervening ones)."""
    return [b[0] - a[0] for a, b in zip(events, events[1:])]


def gaps_between_q3(events: list[tuple[int, int]]) -> list[tuple[int, list[int]]]:
    """Between successive q=3 payouts, list intervening payout qs and step gap."""
    q3 = [(i, q) for i, q in events if q == 3]
    out = []
    for (i, _), (j, _) in zip(q3, q3[1:]):
        intervening = [q for (t, q) in events if i < t < j]
        out.append((j - i, intervening))
    return out


def is_mechanical_34_suffix(word: list[int], max_preperiod: int) -> tuple[bool, int, str]:
    """Check whether some finite preperiod leaves a PCD8-style 3/4 word.

    Mechanical pattern after optional preperiod:
      - every payout is q=3
      - intervening valuations are all 1
      - gaps between consecutive q=3 payouts are in {3,4}
    """
    for pre in range(max_preperiod + 1):
        tail = word[pre:]
        if not tail:
            continue
        events = payout_events(tail)
        if not events:
            return False, pre, "no payouts in suffix"
        bad_q = [q for _, q in events if q != 3]
        if bad_q:
            continue
        # rebuild: between payouts only ones; gaps in {3,4}
        ok = True
        reason = "ok"
        # optional leading ones before first payout
        first = events[0][0]
        if any(e != 1 for e in tail[:first]):
            ok = False
            reason = "non-one before first q=3"
        for (i, _), (j, _) in zip(events, events[1:]):
            gap = j - i
            if gap not in (3, 4):
                ok = False
                reason = f"gap {gap} not in {{3,4}}"
                break
            if any(e != 1 for e in tail[i + 1 : j]):
                ok = False
                reason = "non-one between q=3 payouts"
                break
        # after last payout, only ones
        last = events[-1][0]
        if ok and any(e != 1 for e in tail[last + 1 :]):
            # trailing ones are fine; non-ones are extra payouts already caught
            pass
        if ok and len(events) >= 2:
            return True, pre, reason
    return False, -1, "no preperiod yields mechanical 3/4 suffix"


def mechanical_gap_word(events: list[tuple[int, int]]) -> list[int] | None:
    """If events are pure q=3 with one-fills, return gap word; else None."""
    if not events or any(q != 3 for _, q in events):
        return None
    gaps = []
    for (i, _), (j, _) in zip(events, events[1:]):
        gap = j - i
        if gap not in (3, 4):
            return None
        gaps.append(gap)
    return gaps


def report(n: int, steps: int, max_preperiod: int) -> None:
    word = valuation_word(n, steps)
    events = payout_events(word)
    qs = [q for _, q in events]
    print(f"== Atlas L5 diagnostic: n={n}, steps={steps} ==")
    print(f"valuation word: {word}")
    print(f"payout events (step,q): {events}")
    print(f"q multiset: {dict(Counter(qs))}")
    print(f"gaps between successive payouts: {gaps_between_payouts(events)}")
    print(f"q=3-to-q=3 gaps and intervening qs: {gaps_between_q3(events)}")

    mech = mechanical_gap_word(events)
    print(f"pure mechanical gap word from t=0: {mech}")

    ok, pre, reason = is_mechanical_34_suffix(word, max_preperiod)
    print(
        f"mechanical 3/4 suffix within preperiod<={max_preperiod}: "
        f"{ok} (pre={pre}, {reason})"
    )

    # crude drift on payout-gap alphabet if we project only q=3 spacings
    # ignoring intervening non-q3 (diagnostic for exotic seed)
    q3_gaps = [g for g, inter in gaps_between_q3(events)]
    if q3_gaps:
        S = sum(C * g - 2 for g in q3_gaps)
        print(
            f"projected q=3 gap count={len(q3_gaps)} "
            f"alphabet={sorted(set(q3_gaps))} "
            f"sum(c*g-2)={S:.6f}"
        )


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=471)
    parser.add_argument("--steps", type=int, default=80)
    parser.add_argument("--max-preperiod", type=int, default=40)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    report(args.n, args.steps, args.max_preperiod)
