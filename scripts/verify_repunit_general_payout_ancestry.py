#!/usr/bin/env python3
"""Verify automatic shell-partner realisation for general payouts q >= 2.

For a realised high valuation word ending in a payout q, let h=floor(q/2),
let u be the lower cumulative valuation selected by the canonical collision
shell, and let C be the shell-partner correction.  If C equals A_i(w) for an
admissible source word w of total u, the theorem in
``general_payout_ancestry.md`` says that the aligned smaller repunit exponent
automatically realises w and merges with the high tail on the next odd step.
"""

from functools import lru_cache
from itertools import product
from math import floor, log2

from verify_repunit_ancestry_realization import (
    A_of,
    c_of,
    compositions,
    follow_word,
    odd_step,
    repunit,
    repunit_exponent_class,
    starting_residue,
)
from explore_balanced_q3_cylinders import (
    repunit_exponent_class as lifted_repunit_exponent_class,
)


def shell_displacement(u, h):
    return (1 << (u + 1)) * ((1 << (2 * h)) - 1) // 3


@lru_cache(maxsize=None)
def source_layer(total, parts):
    layer = {}
    for word in compositions(total, parts):
        layer.setdefault(A_of(word), []).append(word)
    return layer


def verify_mod3_obstruction(max_pre_total=12, max_q=30):
    checked_targets = 0
    checked_sources = 0
    for total in range(1, max_pre_total + 2):
        for parts in range(1, total + 1):
            for word in compositions(total, parts):
                assert A_of(word) % 3 != 0
                checked_sources += 1

    for pre_total in range(1, max_pre_total + 1):
        for j in range(1, min(4, pre_total) + 1):
            for high_prefix in compositions(pre_total, j):
                for q in range(2, max_q + 1):
                    h = q // 2
                    u = pre_total + q - 2 * h
                    C = A_of(high_prefix + (q,)) + shell_displacement(u, h)
                    assert (C % 3 == 0) == (q % 6 in (3, 4))
                    checked_targets += 1
    print(
        "General-payout mod-3 obstruction: PASS  "
        f"({checked_sources} source corrections, {checked_targets} targets)"
    )


def verify_consecutive_q3_fusion(max_pre_total=100):
    for pre_total in range(max_pre_total + 1):
        earlier = shell_displacement(pre_total + 1, 1)
        later = shell_displacement(pre_total + 4, 1)
        fused = shell_displacement(pre_total + 1, 2)
        assert later - 3 * earlier == fused
    print(
        "Consecutive-q=3 shell fusion: PASS  "
        f"({max_pre_total + 1} pre-payout totals)"
    )


def verify_mixed_shell_fusions(max_pre_total=100):
    for E in range(max_pre_total + 1):
        # Adjacent payout blocks (2,3), (3,2), and (4,2).
        assert (
            shell_displacement(E + 3, 1)
            - 3 * shell_displacement(E, 1)
            == shell_displacement(E, 2)
        )
        assert (
            shell_displacement(E + 3, 1)
            - 3 * shell_displacement(E + 1, 1)
            == shell_displacement(E + 1, 1)
        )
        assert (
            shell_displacement(E + 4, 1)
            - 3 * shell_displacement(E, 2)
            == shell_displacement(E, 1)
        )

        # Gap-two block (3,1,2).
        assert (
            9 * shell_displacement(E + 1, 1)
            - shell_displacement(E + 4, 1)
            == shell_displacement(E + 1, 1)
        )

        # Gap-three blocks (2,1,1,3) and (3,a,b,2), a+b=3.
        assert (
            shell_displacement(E + 5, 1)
            - 27 * shell_displacement(E, 1)
            == shell_displacement(E, 2)
        )
        assert (
            shell_displacement(E + 6, 1)
            - 27 * shell_displacement(E + 1, 1)
            == shell_displacement(E + 1, 2)
        )
    print(
        "Mixed blocked/eligible shell fusions: PASS  "
        f"(6 identities, {max_pre_total + 1} pre-payout totals)"
    )


def canonical_correction(A, E, payout):
    post_A = 3 * A + (1 << (E + 1))
    post_E = E + payout
    h = payout // 2
    u = post_E - 2 * h
    return post_A, post_E, post_A + shell_displacement(u, h), u


def correction_lift_defect(word, initial_E, initial_A):
    A = initial_A
    E = initial_E
    first_C = None
    first_u = None
    for index, payout in enumerate(word):
        A, E, C, u = canonical_correction(A, E, payout)
        if index == 0:
            first_C = C
            first_u = u
    return C - 3 ** (len(word) - 1) * first_C, first_u, u


def verify_mixed_correction_lift_nogo(max_pre_total=40):
    patterns = {
        (2, 3): 9,
        (3, 2): 10,
        (4, 2): 17,
        (3, 1, 2): 38,
        (2, 1, 1, 3): 81,
        (3, 1, 2, 2): 194,
        (3, 2, 1, 2): 242,
    }
    checked = 0
    for E in range(max_pre_total + 1):
        for word, coefficient in patterns.items():
            for A in (-17, 0, 23):
                defect, first_u, later_u = correction_lift_defect(word, E, A)
                assert defect == coefficient * 2 ** (E + 1)
                gap = later_u - first_u
                if gap % 2 == 0:
                    required = shell_displacement(first_u, gap // 2)
                    assert defect != required
                checked += 1
    print(
        "Mixed-fusion complete-correction no-go: PASS  "
        f"({checked} exact lifts)"
    )


def verify_canonical_shell_annihilation(max_pre_total=40, max_h=12):
    """Check the affine-aware one-step collapse of every canonical shell."""
    checked = 0
    for u in range(max_pre_total + 1):
        for h in range(1, max_h + 1):
            F = u + 2 * h
            displacement = shell_displacement(u, h)
            for A in (-17, 0, 23):
                partner_correction = A + displacement
                transported_partner = 3 * partner_correction + (1 << (u + 1))
                transported_high = 3 * A + (1 << (F + 1))
                assert transported_partner == transported_high
                checked += 1
    print(
        "Canonical-shell affine annihilation: PASS  "
        f"({checked} exact correction transports)"
    )


def verify_blocked_effective_count_budget(max_length=7, max_payout=6):
    """Check the exact integer form of the blocked valuation-charge bound."""
    checked = 0
    for length in range(1, max_length + 1):
        for word in product(range(1, max_payout + 1), repeat=length):
            E = 0
            blocked_weights = []
            blocked_excess = 0
            for j, payout in enumerate(word):
                if payout % 6 in (3, 4):
                    weight = (
                        3 ** (length - 1 - j)
                        * (1 << (E + 1))
                        * ((1 << payout) - 2)
                    )
                    blocked_weights.append(weight)
                    blocked_excess += payout - 1
                E += payout
            if blocked_weights:
                mass = sum(blocked_weights)
                square_mass = sum(weight * weight for weight in blocked_weights)
                assert 2 * mass * mass <= blocked_excess * square_mass
                checked += 1
    print(
        "Blocked effective-count valuation budget: PASS  "
        f"({checked} exact payout ledgers)"
    )


def verify_balanced_blocked_spacing_nogo(max_payouts=10000):
    """Check the finite prefixes of the PCD8 balanced q=3 construction."""
    c = log2(3 / 2)
    post_deficits = []
    gaps = []
    previous_time = 0
    for m in range(1, max_payouts + 1):
        current_time = floor(2 * m / c)
        gap = current_time - previous_time
        assert gap in (3, 4)
        gaps.append(gap)
        post_deficits.append(c * current_time - 2 * m)
        previous_time = current_time

    width = max(post_deficits) - min(post_deficits)
    assert width < c
    weights = [(3 / 4) * 2 ** (-D) for D in post_deficits]
    effective_count = sum(weights) ** 2 / sum(weight * weight for weight in weights)
    assert effective_count >= 4 * max_payouts / 9

    # The balanced phase has a uniformly bounded maximum, while a terminal
    # valuation-one run increases D by c at every step and eventually makes
    # every subsequent step a strict record.
    D = 0.0
    historical_max = D
    for gap in gaps:
        for _ in range(gap - 1):
            D += c
            historical_max = max(historical_max, D)
        D += c - 2
        historical_max = max(historical_max, D)
    terminal_steps = floor((historical_max - D) / c) + 3
    records = 0
    for _ in range(terminal_steps):
        D += c
        if D > historical_max:
            historical_max = D
            records += 1
    assert records >= 2
    print(
        "Balanced blocked-spacing no-go: PASS  "
        f"({max_payouts} q=3 payouts, gaps {sorted(set(gaps))}, "
        f"deficit-band width {width:.6f})"
    )


def verify_repunit_cylinder_saturation(max_total=12):
    checked = 0
    for total in range(1, max_total + 1):
        for parts in range(1, total + 1):
            for word in compositions(total, parts):
                table_class = repunit_exponent_class(word)
                lifted_class = lifted_repunit_exponent_class(word)
                assert lifted_class == table_class
                has_odd_class = table_class is not None and table_class[0] & 1
                assert bool(has_odd_class) == (word[0] >= 2)
                checked += 1
    print(
        "Odd-repunit cylinder saturation: PASS  "
        f"({checked} valuation words, total <= {max_total})"
    )


def verify_full_carry_shift(max_E=8, max_delta=6):
    checked = 0
    for E in range(1, max_E + 1):
        for delta in range(1, max_delta + 1):
            old_modulus = 1 << (E + 1)
            new_modulus = 1 << (E + delta + 1)
            generator = 3 ** (1 << E)
            for n in range(1, 1 << E, 2):
                power = 3**n
                r = ((power - 1) // 2) % old_modulus
                C = (power - (2 * r + 1)) >> (E + 2)
                for z in range(min(1 << delta, 4)):
                    new_n = n + (z << E)
                    new_power = 3**new_n
                    new_r = ((new_power - 1) // 2) % new_modulus
                    assert (new_r - r) % (1 << (E + 1)) == 0
                    t = (new_r - r) >> (E + 1)
                    new_C = (new_power - (2 * new_r + 1)) >> (E + delta + 2)
                    G = (generator**z - 1) >> (E + 2)
                    numerator = C - t + power * G
                    assert numerator % (1 << delta) == 0
                    assert new_C == numerator >> delta
                    if z == 0:
                        assert C % (1 << delta) == t
                        assert new_C == (C - t) >> delta
                    checked += 1
    print(
        "Full-carry cylinder shift: PASS  "
        f"({checked} exact extensions)"
    )


def verify_fixed_width_endpoint_nogo():
    blocks = {
        (1, 1, 3): 55,
        (1, 1, 1, 3): 79,
    }
    checked = 0
    for word, suffix_residue in blocks.items():
        delta = sum(word)
        length = len(word)
        assert starting_residue(word) == suffix_residue
        for K in range(1, 11):
            inverse = pow(3**K, -1, 1 << delta)
            for M in range(delta + 1, delta + 9):
                for y in (1, 3, 17):
                    t = ((suffix_residue - y) // 2) * inverse % (1 << delta)
                    lifted = y + 2 * t * 3**K
                    final = follow_word(lifted, word)

                    y2 = y + (1 << M)
                    t2 = ((suffix_residue - y2) // 2) * inverse % (1 << delta)
                    assert t2 == t
                    final2 = follow_word(lifted + (1 << M), word)
                    assert final2 - final == 3**length * (1 << (M - delta))
                    assert (final2 - final) % (1 << M) != 0
                    checked += 1
    print(
        "Fixed-width endpoint-state no-go: PASS  "
        f"({checked} exact paired transitions)"
    )


def verify_balanced_block_distortion(max_start=100, max_length=100):
    blocks = {
        (1, 1, 3): (3, 5, 19),
        (1, 1, 1, 3): (4, 6, 65),
    }
    for word, (length, total, correction) in blocks.items():
        assert len(word) == length
        assert sum(word) == total
        assert c_of(word) == correction

    c = log2(3 / 2)
    checked = 0
    for start in range(max_start + 1):
        T_start = floor(2 * start / c)
        for block_length in range(1, max_length + 1):
            T_end = floor(2 * (start + block_length) / c)
            steps = T_end - T_start
            denominator_power = steps + 2 * block_length
            numerator = 3**steps
            denominator = 1 << denominator_power
            assert 3 * numerator > 2 * denominator
            assert 2 * numerator < 3 * denominator
            checked += 1
    print(
        "Balanced-block bounded distortion: PASS  "
        f"({checked} exact mechanical intervals)"
    )


def verify_general_payouts(max_pre_total=12, max_q=6):
    tested_high_words = 0
    abstract_matches = 0
    realised_matches = 0
    matches_by_q = {q: 0 for q in range(2, max_q + 1)}
    realised_by_q = {q: 0 for q in range(2, max_q + 1)}

    for pre_total in range(2, max_pre_total + 1):
        for j in range(1, min(4, pre_total) + 1):
            for high_prefix in compositions(pre_total, j):
                for q in range(2, max_q + 1):
                    h = q // 2
                    u = pre_total + q - 2 * h
                    full_high = high_prefix + (q,)
                    high_A = A_of(full_high)
                    C = high_A + shell_displacement(u, h)
                    exponent_class = repunit_exponent_class(full_high)
                    if exponent_class is not None and exponent_class[0] & 1:
                        tested_high_words += 1

                    d_offset = j + 1
                    for i in range(j + 2, u + 1):
                        if i % 2 != (j + 1) % 2:
                            continue
                        matches = source_layer(u, i).get(C, ())
                        abstract_matches += len(matches)
                        matches_by_q[q] += len(matches)
                        if not matches or exponent_class is None:
                            continue

                        n0, period = exponent_class
                        if not n0 & 1:
                            continue
                        n = n0
                        if n < 3:
                            n += period
                        while n + d_offset - i < 1:
                            n += period
                        m = n + d_offset - i
                        assert 0 < m < n and (m & 1) and (n & 1)

                        X = follow_word(repunit(n), full_high)
                        expected_Y = 4**h * X + (4**h - 1) // 3
                        for source in matches:
                            Y = follow_word(repunit(m), source)
                            assert Y == expected_Y
                            assert odd_step(Y)[0] == odd_step(X)[0]
                            realised_matches += 1
                            realised_by_q[q] += 1

    assert realised_matches > 0
    print(
        "General-payout automatic realisation: PASS  "
        f"({tested_high_words} realised high words, "
        f"{abstract_matches} abstract matches, "
        f"{realised_matches} realised aligned matches)"
    )
    print(f"Abstract matches by q: {matches_by_q}")
    print(f"Realised aligned matches by q: {realised_by_q}")


if __name__ == "__main__":
    verify_mod3_obstruction()
    verify_consecutive_q3_fusion()
    verify_mixed_shell_fusions()
    verify_mixed_correction_lift_nogo()
    verify_canonical_shell_annihilation()
    verify_blocked_effective_count_budget()
    verify_balanced_blocked_spacing_nogo()
    verify_repunit_cylinder_saturation()
    verify_full_carry_shift()
    verify_fixed_width_endpoint_nogo()
    verify_balanced_block_distortion()
    verify_general_payouts()
