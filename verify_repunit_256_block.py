#!/usr/bin/env python3
"""Verify the bounded active 256-block certificate."""

from explore_repunit_tail_merges import fingerprint, state_at, v2


LIMIT = 10001
BLOCK = 256
FLOOR = 425


def exact_candidate_match(x, candidates):
    for source_n, source_step in candidates:
        if x == state_at(source_n, source_step):
            return source_n, source_step
    return None


def main():
    seen = {}
    power3 = 3**7
    windows = 0
    below = 0
    minimum = None
    minimum_locations = []

    for n in range(7, LIMIT + 1, 2):
        target = (1 << n) - 1
        x = (power3 - 1) // 2
        power3 *= 9
        pending = []
        valuations = []

        for step in range(3 * n + 1):
            key = fingerprint(x)
            candidates = seen.get(key)
            if candidates and exact_candidate_match(x, candidates):
                break

            pending.append((key, step))
            if step > 0 and x < target:
                break

            value = 3 * x + 1
            e = v2(value)
            valuations.append(e)
            x = value >> e

        for key, step in pending:
            seen.setdefault(key, []).append((n, step))

        if len(valuations) < BLOCK:
            continue

        total = sum(valuations[:BLOCK])
        for start in range(len(valuations) - BLOCK + 1):
            if start:
                total += valuations[start + BLOCK - 1] - valuations[start - 1]
            windows += 1
            if minimum is None or total < minimum:
                minimum = total
                minimum_locations = [(n, start)]
            elif total == minimum:
                minimum_locations.append((n, start))
            if total < FLOOR:
                below += 1

    assert windows == 1_712_672
    assert minimum == FLOOR
    assert minimum_locations == [(2449, 306)]
    assert below == 0

    print(
        "BLOCK256 finite certificate: PASS "
        "(odd 7 <= n <= 10001; 1,712,672 active blocks; "
        "minimum=425 at n=2449, step=306)"
    )


if __name__ == "__main__":
    main()

