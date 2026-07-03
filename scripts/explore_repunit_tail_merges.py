#!/usr/bin/env python3
"""
Explore exact mergers between repunit tails.

Process odd exponents in increasing order. For each n, follow the tail from
a_n=(3^n-1)/2 until it either:

1. descends below 2^n-1 without meeting an earlier tail; or
2. reaches a state already visited by a smaller exponent m.

The second case yields an inductive certificate in the finite computation:
after the merge, the n-tail follows the already processed m-tail.

State fingerprints are used only as an index. Every reported merge is verified
by recomputing and comparing the exact integer states.
"""

import argparse
import hashlib
import time
from collections import Counter


def v2(n):
    return (n & -n).bit_length() - 1


def fingerprint(n):
    data = n.to_bytes((n.bit_length() + 7) // 8, "little")
    return hashlib.blake2b(data, digest_size=16).digest()


def state_at(n, step):
    x = (3**n - 1) // 2
    for _ in range(step):
        value = 3 * x + 1
        x = value >> v2(value)
    return x


def exact_candidate_match(x, candidates):
    for source_n, source_step in candidates:
        if x == state_at(source_n, source_step):
            return source_n, source_step
    return None


def scan(limit, factor=3, progress_every=0):
    # fingerprint -> list[(n, step)], permitting exact collision resolution.
    seen = {}
    merges = []
    primitives = []
    unresolved = []
    power3 = 3**7
    started = time.perf_counter()

    for n in range(7, limit + 1, 2):
        target = (1 << n) - 1
        x = (power3 - 1) // 2
        power3 *= 9
        pending = []
        outcome = None

        for step in range(0, factor * n + 1):
            key = fingerprint(x)
            candidates = seen.get(key)
            if candidates:
                source = exact_candidate_match(x, candidates)
                if source is not None:
                    source_n, source_step = source
                    outcome = {
                        "n": n,
                        "step": step,
                        "source_n": source_n,
                        "source_step": source_step,
                        "gap": n - source_n,
                        "diagonal": n + step,
                        "source_diagonal": source_n + source_step,
                    }
                    merges.append(outcome)
                    break

            pending.append((key, step))
            if step > 0 and x < target:
                outcome = {
                    "n": n,
                    "sigma": step,
                    "ratio": step / n,
                }
                primitives.append(outcome)
                break

            value = 3 * x + 1
            x = value >> v2(value)

        if outcome is None:
            unresolved.append({"n": n})

        # Insert only the pre-outcome path. Later tails may merge into it.
        for key, step in pending:
            seen.setdefault(key, []).append((n, step))

        if progress_every and n % progress_every in (0, 1):
            elapsed = time.perf_counter() - started
            print(
                f"progress n={n}/{limit} merges={len(merges)} "
                f"primitive={len(primitives)} states={len(seen)} "
                f"elapsed={elapsed:.1f}s"
            )

    return {
        "merges": merges,
        "primitives": primitives,
        "unresolved": unresolved,
        "states": len(seen),
        "elapsed": time.perf_counter() - started,
    }


def print_report(result, limit):
    merges = result["merges"]
    primitives = result["primitives"]
    total = merges + primitives
    count = len(merges) + len(primitives) + len(result["unresolved"])

    print("== Repunit-tail merge explorer ==")
    print(f"finite domain: odd 7 <= n <= {limit}")
    print(
        f"processed={count} merged={len(merges)} "
        f"primitive={len(primitives)} unresolved={len(result['unresolved'])}"
    )
    if count:
        print(f"merge fraction={len(merges)/count:.2%}")

    off_diagonal = [
        row
        for row in merges
        if row["diagonal"] != row["source_diagonal"]
    ]
    print(f"off-diagonal exact merges={len(off_diagonal)}")

    gap_counts = Counter(row["gap"] for row in merges)
    print(f"merge-gap counts: {gap_counts.most_common(20)}")

    if primitives:
        worst = max(primitives, key=lambda row: row["ratio"])
        largest = max(primitives, key=lambda row: row["n"])
        print(
            f"worst primitive ratio: n={worst['n']} "
            f"sigma={worst['sigma']} ratio={worst['ratio']:.9f}"
        )
        print(
            f"largest primitive exponent: n={largest['n']} "
            f"sigma={largest['sigma']}"
        )
        print(
            "primitive exponents: "
            + ",".join(str(row["n"]) for row in primitives[:80])
            + ("..." if len(primitives) > 80 else "")
        )

    print("\nFirst exact merges:")
    for row in merges[:30]:
        print(
            f"  n={row['n']} step={row['step']} -> "
            f"n={row['source_n']} step={row['source_step']} "
            f"gap={row['gap']} diagonal={row['diagonal']}"
        )

    print(
        f"\nindexed fingerprints={result['states']} "
        f"elapsed={result['elapsed']:.2f}s"
    )


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=1001)
    parser.add_argument("--factor", type=int, default=3)
    parser.add_argument("--progress-every", type=int, default=0)
    return parser.parse_args()


def main():
    args = parse_args()
    result = scan(args.limit, args.factor, args.progress_every)
    print_report(result, args.limit)


if __name__ == "__main__":
    main()

