#!/usr/bin/env python3
"""
Explore finite residue-class descent certificates for the shortcut Collatz map.

For a fixed K and odd residue r modulo 2^K, the script follows shortcut
odd-steps while the required 2-adic valuations are determined by those K low
bits. A residue is discharged when the resulting affine map is uniformly below
the starting value for every integer in that residue class.

This is exploratory. Unresolved classes are not counterexamples; they are the
places where the fixed K-bit certificate runs out of valuation information
before proving descent.
"""

from collections import Counter


def v2(n):
    return (n & -n).bit_length() - 1 if n else 10**9


def try_residue_certificate(r, K, max_steps=200):
    """Try to prove descent for all n = 2^K*q + r, q >= 0."""
    start_a = 1 << K
    start_b = r
    a = start_a
    b = start_b
    valuation_budget = 0
    valuations = []

    for step in range(1, max_steps + 1):
        valuation = v2(3 * b + 1)
        # Equality is not enough to determine the exact valuation uniformly:
        # the parameter term and constant term can cancel after division by
        # 2^K.  One additional known bit is required to continue the affine
        # accelerated trajectory without branching.
        if valuation_budget + valuation >= K:
            return {
                "status": "unresolved",
                "reason": "need_more_bits",
                "steps": step - 1,
                "budget": valuation_budget,
                "next_v2": valuation,
                "a": a,
                "b": b,
                "valuations": valuations,
            }

        a = (3 * a) >> valuation
        b = (3 * b + 1) >> valuation
        valuation_budget += valuation
        valuations.append(valuation)

        if a < start_a and (b < start_b or b == start_b == 1):
            return {
                "status": "proved",
                "steps": step,
                "budget": valuation_budget,
                "a": a,
                "b": b,
                "valuations": valuations,
            }

    return {
        "status": "unresolved",
        "reason": "max_steps",
        "steps": max_steps,
        "budget": valuation_budget,
        "a": a,
        "b": b,
        "valuations": valuations,
    }


def rail7_escape_profile(r):
    """Return the rail-7 escape profile for an odd residue r == 7 mod 8."""
    y = (r - 7) // 8
    depth = v2(y + 1) // 2
    y_exit = (pow(9, depth) * (y + 1) // (4**depth)) - 1
    x_exit = 18 * y_exit + 17
    return depth, x_exit % 8, v2(y + 1)


def summarize(K_values):
    for K in K_values:
        total = 1 << (K - 1)
        proved = 0
        unresolved = []
        step_counts = Counter()
        reason_counts = Counter()
        rail7_profiles = Counter()

        for r in range(1, 1 << K, 2):
            result = try_residue_certificate(r, K)
            if result["status"] == "proved":
                proved += 1
                step_counts[result["steps"]] += 1
            else:
                unresolved.append((r, result))
                reason_counts[result["reason"]] += 1
                if r % 8 == 7:
                    rail7_profiles[rail7_escape_profile(r)] += 1

        pct = 100 * proved / total
        print(f"K={K}: proved {proved}/{total} ({pct:.2f}%), unresolved {len(unresolved)}")
        print(f"  unresolved reasons: {dict(reason_counts)}")
        print(f"  most common proof lengths: {step_counts.most_common(8)}")
        if rail7_profiles:
            print(f"  unresolved rail-7 escape profiles: {rail7_profiles.most_common(8)}")
        if unresolved:
            sample = ", ".join(str(r) for r, _ in unresolved[:16])
            print(f"  first unresolved residues: {sample}")


if __name__ == "__main__":
    summarize(range(8, 21, 2))
