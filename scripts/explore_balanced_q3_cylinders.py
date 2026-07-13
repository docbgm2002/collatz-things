#!/usr/bin/env python3
"""Intersect the PCD8 balanced q=3 language with repunit exponent cylinders.

The word begins with a q=3 payout.  Subsequent blocked payouts use the
mechanical gaps from floor(2m/log2(3/2)); gaps are three or four and all
intervening valuations are one.  For every post-payout prefix this
script computes the exact exponent class n modulo 2^E without constructing a
discrete-log table.  The power-of-three residue and its exponent generator
are streamed inside a checkpointed precision window.  It reports whether the
class contains odd repunit exponents and the least positive representative
when it does.

This is an exact cylinder diagnostic.  It does not assert that a surviving
representative is primitive or that its full tail avoids descent.
"""

import argparse
from functools import lru_cache
from math import floor, log2


def correction_c(word):
    """Return c with f^K(x)=(3^K x+c)/2^E for the supplied word."""
    c = 0
    E = 0
    for payout in word:
        c = 3 * c + (1 << E)
        E += payout
    return c, E


def discrete_log_base3_power2(target, exponent_bits):
    """Solve 3^n=target mod 2^(exponent_bits+2), returning n mod 2^bits."""
    modulus = 1 << (exponent_bits + 2)
    target %= modulus
    residue8 = target & 7
    if residue8 == 1:
        n = 0
    elif residue8 == 3:
        n = 1
    else:
        return None

    # n is known modulo 2.  At bit k, distinguish n from n+2^k at the
    # first modulus where those powers differ.
    for k in range(1, exponent_bits):
        test_modulus = 1 << (k + 3)
        if pow(3, n, test_modulus) != target % test_modulus:
            n += 1 << k
            assert pow(3, n, test_modulus) == target % test_modulus
    assert pow(3, n, modulus) == target
    return n


def lift_discrete_log_base3_power2(target, exponent_bits, n, known_bits):
    """Extend a known nested exponent residue from known_bits to exponent_bits."""
    assert 1 <= known_bits <= exponent_bits
    assert 0 <= n < (1 << known_bits)
    modulus = 1 << (exponent_bits + 2)
    target %= modulus
    value = pow(3, n, modulus)
    generator = pow(3, 1 << known_bits, modulus)
    for lift in range(1 << (exponent_bits - known_bits)):
        if value == target:
            result = n + (lift << known_bits)
            assert pow(3, result, modulus) == target
            return result
        value = value * generator % modulus
    raise AssertionError("nested discrete-log lift has no solution")


@lru_cache(maxsize=None)
def normalized_power_coefficient(k, bits):
    """Return h_k mod 2^bits where 3^(2^k)=1+2^(k+2)h_k."""
    if bits <= 0:
        return 0
    modulus = 1 << bits
    h = 1  # h_1=(3^2-1)/2^3
    current = 1
    while current < k and current + 1 < bits:
        h = (h + (1 << (current + 1)) * h * h) % modulus
        current += 1
    return h


def power_two_generator(k, modulus_bits):
    """Return 3^(2^k) modulo 2^modulus_bits without large exponentiation."""
    coefficient_bits = modulus_bits - (k + 2)
    if coefficient_bits <= 0:
        return 1
    h = normalized_power_coefficient(k, coefficient_bits)
    return (1 + (h << (k + 2))) % (1 << modulus_bits)


def repunit_target(c, E, length):
    starting_modulus = 1 << (E + 1)
    starting_residue = (
        ((1 << E) - c)
        * pow(pow(3, length, starting_modulus), -1, starting_modulus)
    ) % starting_modulus
    return 2 * starting_residue + 1


def repunit_exponent_class(word):
    """Return the exact n mod 2^E class realising word, or None."""
    c, E = correction_c(word)
    target = repunit_target(c, E, len(word))
    n = discrete_log_base3_power2(target, E)
    if n is None:
        return None
    return n, 1 << E


def balanced_prefixes(count):
    c = log2(3 / 2)
    yield 1, 1, (3,)
    if count == 1:
        return
    previous_time = 0
    elapsed = 1
    for payout_index in range(2, count + 1):
        current_time = floor(2 * (payout_index - 1) / c)
        gap = current_time - previous_time
        assert gap in (3, 4)
        suffix = (1,) * (gap - 1) + (3,)
        previous_time = current_time
        elapsed += gap
        yield payout_index, elapsed, suffix


def follow_suffix_state(x, suffix):
    for expected in suffix:
        value = 3 * x + 1
        observed = (value & -value).bit_length() - 1
        if observed != expected:
            return None
        x = value >> observed
    return x


def starting_residue_for_word(word):
    c, E = correction_c(word)
    modulus = 1 << (E + 1)
    residue = (
        ((1 << E) - c)
        * pow(pow(3, len(word), modulus), -1, modulus)
    ) % modulus
    return residue, E


def analyse(count, precision_chunk_bits=2048):
    if count < 1:
        raise ValueError("count must be positive")
    if precision_chunk_bits < 1:
        raise ValueError("precision_chunk_bits must be positive")

    prefix_plan = list(balanced_prefixes(count))
    final_E = sum(sum(suffix) for _, _, suffix in prefix_plan)
    final_power_bits = final_E + 2

    rows = []
    c = 0
    E = 0
    length = 0
    power3 = 1
    starting_residue = None
    endpoint_state = None
    previous_n = None
    previous_E = 0
    power_value = None
    exponent_generator = None
    power_modulus_bits = 0
    power_modulus = None
    for payout_index, time, suffix in prefix_plan:
        old_E = E
        old_starting_residue = starting_residue
        exponent_lift = None
        extension_bits = None
        starting_lift = None
        exponent_carry = None
        if starting_residue is not None:
            suffix_residue, delta_E = starting_residue_for_word(suffix)
            lift_modulus = 1 << delta_E
            difference = suffix_residue - endpoint_state
            assert difference % 2 == 0
            starting_lift = (
                (difference // 2)
                * pow(power3, -1, lift_modulus)
            ) % lift_modulus
            endpoint_state = follow_suffix_state(
                endpoint_state + 2 * starting_lift * power3, suffix
            )
            assert endpoint_state is not None
            starting_residue += starting_lift << (E + 1)

        for payout in suffix:
            c = 3 * c + (1 << E)
            E += payout
            length += 1
            power3 *= 3

        if starting_residue is None:
            modulus = 1 << (E + 1)
            starting_residue = (
                ((1 << E) - c) * pow(power3, -1, modulus)
            ) % modulus
            endpoint_state = (power3 * starting_residue + c) >> E

        target = 2 * starting_residue + 1
        if previous_n is None:
            n0 = discrete_log_base3_power2(target, E)
            power_modulus_bits = min(
                final_power_bits, E + 2 + precision_chunk_bits
            )
            power_modulus = 1 << power_modulus_bits
            power_value = pow(3, n0, power_modulus)
            exponent_generator = power_two_generator(E, power_modulus_bits)
        else:
            required_bits = E + 2
            extension_bits = E - old_E
            if required_bits > power_modulus_bits:
                power_modulus_bits = min(
                    final_power_bits,
                    required_bits + precision_chunk_bits,
                )
                power_modulus = 1 << power_modulus_bits
                power_value = pow(3, previous_n, power_modulus)
                exponent_generator = power_two_generator(
                    old_E, power_modulus_bits
                )
            modulus = 1 << required_bits
            value = power_value % modulus
            old_power_value = value

            local_modulus = 1 << extension_bits
            old_target = 2 * old_starting_residue + 1
            carry_difference = old_power_value - old_target
            assert carry_difference % (1 << (old_E + 2)) == 0
            exponent_carry = (
                carry_difference >> (old_E + 2)
            ) % local_modulus
            h = normalized_power_coefficient(old_E, extension_bits)
            coefficient = h * (old_target % local_modulus) % local_modulus
            predicted_lift = (
                (starting_lift - exponent_carry)
                * pow(coefficient, -1, local_modulus)
            ) % local_modulus
            exponent_lift = predicted_lift
            assert (exponent_lift == 0) == (starting_lift == exponent_carry)
            n0 = previous_n + (exponent_lift << old_E)

            power_value = (
                power_value
                * pow(exponent_generator, exponent_lift, power_modulus)
            ) % power_modulus
            assert power_value % modulus == target

            for _ in range(extension_bits):
                exponent_generator = (
                    exponent_generator * exponent_generator
                ) % power_modulus
        if n0 is None:
            rows.append(
                {
                    "m": payout_index,
                    "K": time,
                    "E": E,
                    "status": "no-class",
                    "n0": None,
                }
            )
            continue
        period = 1 << E
        previous_n = n0
        previous_E = E
        rows.append(
            {
                "m": payout_index,
                "K": time,
                "E": E,
                "status": "odd" if n0 & 1 else "even-only",
                "n0": n0,
                "period": period,
                "bits": n0.bit_length(),
                "extension_bits": extension_bits,
                "exponent_lift": exponent_lift,
                "starting_lift": starting_lift,
                "exponent_carry": exponent_carry,
            }
        )
    return rows


def print_report(rows, show):
    odd = [row for row in rows if row["status"] == "odd"]
    even = [row for row in rows if row["status"] == "even-only"]
    absent = [row for row in rows if row["status"] == "no-class"]
    print("== Balanced q=3 repunit-cylinder diagnostic ==")
    print(
        f"prefixes={len(rows)}; odd classes={len(odd)}; "
        f"even-only={len(even)}; absent={len(absent)}"
    )
    if odd:
        ratios = [(row["bits"] / row["E"], row) for row in odd]
        minimum_ratio, minimum_row = min(ratios, key=lambda item: item[0])
        asymptotic = [item for item in ratios if item[1]["m"] >= 10]
        asymptotic_ratio, asymptotic_row = min(
            asymptotic or ratios, key=lambda item: item[0]
        )
        longest_plateau = 1
        current_plateau = 1
        plateau_end = odd[0]
        has_changed = False
        completed_plateaus = []
        plateau_start = odd[0]["m"]
        for previous, current in zip(odd, odd[1:]):
            if current["n0"] == previous["n0"]:
                current_plateau += 1
            else:
                completed_plateaus.append(
                    (plateau_start, previous["m"], current_plateau)
                )
                current_plateau = 1
                plateau_start = current["m"]
                has_changed = True
            if has_changed:
                assert current["bits"] >= current["E"] - 6 * current_plateau + 1
            if current_plateau > longest_plateau:
                longest_plateau = current_plateau
                plateau_end = current
        completed_plateaus.append(
            (plateau_start, odd[-1]["m"], current_plateau)
        )
        nontrivial = [item for item in completed_plateaus if item[2] > 1]
        histogram = {}
        for _, _, length in completed_plateaus:
            histogram[length] = histogram.get(length, 0) + 1
        print(
            "least-representative growth: "
            f"min bits/E={minimum_ratio:.6f} at m={minimum_row['m']}; "
            f"min for m>=10={asymptotic_ratio:.6f} "
            f"at m={asymptotic_row['m']}; "
            f"longest plateau={longest_plateau} prefixes "
            f"at m={plateau_end['m'] - longest_plateau + 1}..{plateau_end['m']} "
            f"(K={plateau_end['K']}, E={plateau_end['E']}, "
            f"bits={plateau_end['bits']})"
        )
        print(
            f"plateau histogram={dict(sorted(histogram.items()))}; "
            f"nontrivial starts={[start for start, _, _ in nontrivial]}"
        )
        lift_histograms = {}
        for row in odd[1:]:
            bits = row["extension_bits"]
            lift = row["exponent_lift"]
            histogram_for_bits = lift_histograms.setdefault(bits, {})
            histogram_for_bits[lift] = histogram_for_bits.get(lift, 0) + 1
        for bits, lift_histogram in sorted(lift_histograms.items()):
            total = sum(lift_histogram.values())
            occupied = len(lift_histogram)
            zero_count = lift_histogram.get(0, 0)
            minimum = min(lift_histogram.values())
            maximum = max(lift_histogram.values())
            print(
                f"{bits}-bit exponent lifts: total={total}; "
                f"occupied={occupied}/{1 << bits}; zero={zero_count}; "
                f"count range={minimum}..{maximum}"
            )
    selected = rows if show <= 0 else rows[:show]
    for row in selected:
        if row["n0"] is None:
            print(
                f"  m={row['m']:4d} K={row['K']:5d} E={row['E']:5d} "
                f"status={row['status']}"
            )
        else:
            print(
                f"  m={row['m']:4d} K={row['K']:5d} E={row['E']:5d} "
                f"status={row['status']:9s} n0_bits={row['bits']:5d} "
                f"n0={row['n0']}"
            )


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--payouts", type=int, default=40)
    parser.add_argument(
        "--show",
        type=int,
        default=20,
        help="number of prefix rows to print; use 0 for all",
    )
    parser.add_argument(
        "--precision-chunk",
        type=int,
        default=2048,
        help="high power-of-three bits retained between exact checkpoints",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    print_report(
        analyse(args.payouts, args.precision_chunk),
        args.show,
    )


if __name__ == "__main__":
    main()
