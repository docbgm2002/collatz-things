#!/usr/bin/env python3
"""Finite check of first-descent storage-dominance (Avenue A).

For every odd repunit exponent n in the stated range, through and including
the first accelerated step with x_i < 2^n - 1, verify

    0 < R_i < 3^{n+i},

where R_0 = 1 and R_{i+1} = 3 R_i + 2^{E_i+1}(2^{e_i}-2).

This is a finite certificate, not a proof of the universal lemma.
"""

from __future__ import annotations

import argparse
import math
from fractions import Fraction


def v2(value: int) -> int:
    return (value & -value).bit_length() - 1


def h_of(x: int) -> int:
    return v2(x + 1)


def scan_tail(n: int, step_limit: int = 200_000) -> dict[str, int]:
    threshold = (1 << n) - 1
    x = (3**n - 1) // 2
    E = 0
    R = 1
    min_slack = None
    min_slack_step = 0
    # Maximize theta = R/bound by comparing cross-products.
    max_R = 1
    max_bound = 3**n
    max_theta_step = 0

    for step in range(0, step_limit + 1):
        bound = 3 ** (n + step)
        assert R > 0, (n, step, R)
        assert R < bound, (n, step, R, bound)
        # Optional stronger finite probe used in the Avenue A note.
        assert 27 * R <= 5 * bound, (n, step, R, bound)
        slack = bound - R
        if min_slack is None or slack < min_slack:
            min_slack = slack
            min_slack_step = step
        if R * max_bound > max_R * bound:
            max_R = R
            max_bound = bound
            max_theta_step = step

        if step > 0 and x < threshold:
            return {
                "n": n,
                "descent_step": step,
                "min_slack": min_slack,
                "min_slack_step": min_slack_step,
                "max_R": max_R,
                "max_bound": max_bound,
                "max_theta_step": max_theta_step,
            }

        value = 3 * x + 1
        e = v2(value)
        R = 3 * R + (1 << (E + 1)) * ((1 << e) - 2)
        E += e
        x = value >> e

    raise RuntimeError(f"no descent within step limit for n={n}")


def verify(limit: int) -> None:
    worst_slack = None
    worst_slack_n = 3
    max_R = 1
    max_bound = 3**3
    max_theta_n = 3
    max_descent = 0
    max_descent_n = 3
    worst_k_over_t_n = 3
    worst_k_over_t_num = 0
    worst_k_over_t_den = 1

    worst_k_over_n = 0.0
    worst_k_over_n_n = 3
    for n in range(3, limit + 1, 2):
        row = scan_tail(n)
        threshold = (1 << n) - 1
        k_down = row["descent_step"]
        assert k_down <= threshold, (n, k_down, threshold)
        assert k_down <= 6 * n, (n, k_down)
        ratio_n = k_down / n
        if ratio_n > worst_k_over_n:
            worst_k_over_n = ratio_n
            worst_k_over_n_n = n
        if k_down * worst_k_over_t_den > worst_k_over_t_num * threshold:
            worst_k_over_t_num = k_down
            worst_k_over_t_den = threshold
            worst_k_over_t_n = n
        if worst_slack is None or row["min_slack"] < worst_slack:
            worst_slack = row["min_slack"]
            worst_slack_n = n
        if row["max_R"] * max_bound > max_R * row["max_bound"]:
            max_R = row["max_R"]
            max_bound = row["max_bound"]
            max_theta_n = n
        if k_down > max_descent:
            max_descent = k_down
            max_descent_n = n

    # max_R/max_bound is the global max theta; compare to 5/27 from n=3.
    assert 27 * max_R <= 5 * max_bound
    print("Storage-dominance through first descent: PASS")
    print(f"domain: odd 3 <= n <= {limit}")
    print(f"worst absolute slack={worst_slack} at n={worst_slack_n}")
    print(
        "max theta = R/3^(n+i) realised at n="
        f"{max_theta_n}; integer check 27R <= 5*bound holds "
        "(matches the n=3 prototype theta=5/27)"
    )
    print(f"longest first descent={max_descent} steps at n={max_descent_n}")
    print(
        "K_down <= T gate: PASS "
        f"(worst K/T at n={worst_k_over_t_n}: "
        f"{worst_k_over_t_num}/{worst_k_over_t_den})"
    )
    print(
        "K_down <= 6n gate: PASS "
        f"(worst K/n={worst_k_over_n:.4f} at n={worst_k_over_n_n})"
    )


def gamma(n: int) -> int:
    t = (1 << n) - 1
    return (3**n - 1) * t - (1 << (n - 1)) * (3**n + 1)


def check_stay_reduction(limit: int) -> None:
    """Check SD1S, SD½, strong slack, and SD½P on stay-above payouts."""
    stay_checked = 0
    strong_checked = 0
    half_checked = 0
    mass_checked = 0
    max_half_num = 0
    max_half_den = 1
    max_half_n = 3
    for n in range(3, limit + 1, 2):
        assert gamma(n) > 0
        threshold = (1 << n) - 1
        x = (3**n - 1) // 2
        E = 0
        R = 1
        for step in range(0, 200_000):
            bound = 3 ** (n + step)
            sigma = bound - (x + 1) * (1 << E)
            assert sigma > 0
            assert sigma * (1 << n) > bound  # SD1+
            strong_checked += 1
            # SD½: sigma > 3^step
            assert sigma > 3**step
            half_u = (3**step) * (3**n - 1)
            half_lhs = (x + 1) << E
            assert half_lhs < half_u
            half_checked += 1
            if half_lhs * max_half_den > max_half_num * half_u:
                max_half_num = half_lhs
                max_half_den = half_u
                max_half_n = n
            if step > 0 and x < threshold:
                assert x != 1
                break
            value = 3 * x + 1
            e = v2(value)
            nxt = value >> e
            if e >= 2 and nxt >= threshold:
                assert 3 ** (n + step + 1) < (1 << n) * (
                    3 * sigma + (1 << (E + 1))
                )
                stay_checked += 1
                payout_mass = R - 3**step
                assert payout_mass >= 0
                # SD½P and the stronger SD½P⁻ (drop 2^{E+n+1})
                assert (3 ** (step + 1)) * gamma(n) + (
                    1 << (E + n + 1)
                ) > 3 * (1 << (n - 1)) * payout_mass
                assert (payout_mass << (n - 1)) < (3**step) * gamma(n)
                mass_checked += 1
                assert x != threshold  # observed barrier used in IH attempts
            R = 3 * R + (1 << (E + 1)) * ((1 << e) - 2)
            E += e
            x = nxt
        else:
            raise RuntimeError(f"no descent within step limit for n={n}")

    print(
        "SD1S/SD½/SD½P stay reductions: PASS "
        f"(stay={stay_checked}, mass={mass_checked}, "
        f"half-states={half_checked}, strong={strong_checked}; "
        f"odd 3 <= n <= {limit})"
    )
    print(
        f"worst SD½ ratio at n={max_half_n} "
        f"(prototype n=3 has phi=16/13)"
    )


def _window_has_power_of_two_for(n: int, i: int, a_n: int, target: int) -> bool:
    """Return True if [L, L*(1+1/(3T))^i] contains a power of 2."""
    if i <= 0:
        return False
    threshold = (1 << n) - 1
    log_l = i * math.log2(3) + math.log2(a_n) - math.log2(target)
    log_alpha = math.log2(1 + 1 / (3 * threshold))
    if abs(log_l - round(log_l)) < 1e-12:
        return True
    frac_up = math.ceil(log_l) - log_l
    return frac_up <= i * log_alpha + 1e-14


def check_L1_gates(limit: int) -> None:
    """Certify max h < n+2 and max v2(x-1) < n+3 through first descent.

    Also certifies the first-landing bounds h(x1) < n+2 and v(x1) < n+3,
    the elementary e0=2 identity v(x1) = v2(n-1) - 1, absence of the
    unit e=2 L=1 point z_n = 1+2^{n+3}, and (for n>=9) emptiness of the
    affine E-window for z_n on the pre-descent path.
    """
    max_h_gap = None  # (n+2 - max_h, n, max_h)
    max_v_gap = None
    max_h1 = 0
    max_h1_n = 3
    max_v1 = 0
    max_v1_n = 3
    max_v_e3 = 0
    max_v_e3_n = 3
    unit_gap_checks = 0
    for n in range(3, limit + 1, 2):
        threshold = (1 << n) - 1
        a_n = (3**n - 1) // 2
        z_n = 1 + (1 << (n + 3))
        e0 = 1 + v2(n + 1)
        x1 = (3 ** (n + 1) - 1) // (1 << (e0 + 1))
        h1 = v2(x1 + 1)
        v1 = v2(x1 - 1)
        assert h1 < n + 2, (n, h1)
        assert v1 < n + 3, (n, v1)
        if e0 == 2:
            assert v1 == v2(n - 1) - 1, (n, v1, v2(n - 1) - 1)
        if h1 > max_h1:
            max_h1 = h1
            max_h1_n = n
        if v1 > max_v1:
            max_v1 = v1
            max_v1_n = n

        x = a_n
        max_h = v2(x + 1)
        max_v = v2(x - 1)
        for step in range(0, 200_000):
            if step > 0 and x < threshold:
                break
            assert x != z_n, (n, step, x)
            if n >= 9 and step >= 1:
                assert not _window_has_power_of_two_for(n, step, a_n, z_n), (
                    n,
                    step,
                )
                unit_gap_checks += 1
            max_h = max(max_h, v2(x + 1))
            max_v = max(max_v, v2(x - 1))
            value = 3 * x + 1
            e = v2(value)
            y = value >> e
            if e >= 3:
                vy = v2(y - 1)
                if vy > max_v_e3:
                    max_v_e3 = vy
                    max_v_e3_n = n
            x = y
        else:
            raise RuntimeError(f"no descent within step limit for n={n}")
        assert max_h < n + 2, (n, max_h)
        assert max_v < n + 3, (n, max_v)
        h_gap = n + 2 - max_h
        v_gap = n + 3 - max_v
        if max_h_gap is None or h_gap < max_h_gap[0]:
            max_h_gap = (h_gap, n, max_h)
        if max_v_gap is None or v_gap < max_v_gap[0]:
            max_v_gap = (v_gap, n, max_v)
    assert max_h_gap is not None and max_v_gap is not None
    print(
        "L=1 height/v gates: PASS "
        f"(odd 3 <= n <= {limit}; "
        f"tightest h gap {max_h_gap[0]} at n={max_h_gap[1]} "
        f"(max_h={max_h_gap[2]}); "
        f"tightest v gap {max_v_gap[0]} at n={max_v_gap[1]} "
        f"(max_v={max_v_gap[2]}); "
        f"max h(x1)={max_h1} at n={max_h1_n}; "
        f"max v(x1)={max_v1} at n={max_v1_n}; "
        f"max v after e>=3={max_v_e3} at n={max_v_e3_n}; "
        f"z_n window-gap checks={unit_gap_checks})"
    )


def check_seed_L1_gap(limit: int) -> None:
    """Certify no L=1 residue collision at the seed for odd n <= limit.

    For e0 = 1 + v2(n+1) = 2 the obstruction is unconditional (see the
    Avenue A note). For e0 >= 3 this checks v2(Delta) < e0 + n + 2 with
    Delta = 2^{e0}(3^n - 1) - (3^{n+1} - 1).
    """
    max_uw = 0
    max_uw_n = 3
    checked = 0
    for n in range(3, limit + 1, 2):
        e0 = 1 + v2(n + 1)
        delta = ((1 << e0) - 3) * (3**n) - ((1 << e0) - 1)
        # Equivalent form: Delta = 2^{e0}(3^n - 1) - (3^{n+1} - 1).
        assert delta == (1 << e0) * (3**n - 1) - (3 ** (n + 1) - 1)
        vd = v2(delta)
        assert vd < e0 + n + 2, (n, e0, vd)
        uw = vd - (e0 + 1)
        if uw > max_uw:
            max_uw = uw
            max_uw_n = n
        checked += 1
    print(
        "Seed L=1 gap: PASS "
        f"(odd 3 <= n <= {limit}, checked={checked}; "
        f"max v2(a_n - f(a_n)) = {max_uw} at n={max_uw_n})"
    )


def check_e2_preimage(limit: int) -> None:
    """Certify x* = (2^{n+4}-5)/3 is absent from the a_n-orbit.

    For n ≡ 1 (mod 6) the obstruction is unconditional (3 | x*, and the
    orbit never meets multiples of 3). For n ≡ 3,5 (mod 6) this also
    checks that the affine E-window is empty for every pre-descent index
    (i_* > K_down), and records E_K >= K + pi + 1.
    """
    checked_struct = 0
    checked_scan = 0
    checked_gap = 0
    max_scan_n = 3
    worst_k_over_n = 0.0
    worst_k_over_n_n = 3
    for n in range(3, limit + 1, 2):
        a_n = (3**n - 1) // 2
        target = ((1 << (n + 4)) - 5) // 3
        if n % 6 == 1:
            assert target % 3 == 0, (n, target)
            assert pow(2, n + 4, 9) == 5, n
            checked_struct += 1
        threshold = (1 << n) - 1
        x = a_n
        E = 0
        pi_stay = 0
        for step in range(0, 200_000 + 1):
            if step > 0 and x < threshold:
                k_down = step
                assert E >= k_down + pi_stay + 1, (n, E, k_down, pi_stay)
                assert k_down <= 6 * n, (n, k_down)
                ratio = k_down / n
                if ratio > worst_k_over_n:
                    worst_k_over_n = ratio
                    worst_k_over_n_n = n
                break
            assert x % 3 != 0, (n, step, x)
            assert x != target, (n, step, x)
            # n=3,5 are hand-settled (orbit); window may be nonempty at n=5.
            if n >= 9 and n % 6 in (3, 5) and step >= 1:
                assert not _window_has_power_of_two_for(n, step, a_n, target), (
                    n,
                    step,
                )
                checked_gap += 1
            value = 3 * x + 1
            e = v2(value)
            y = value >> e
            if e >= 2 and y >= threshold:
                pi_stay += 1
            E += e
            x = y
        else:
            raise RuntimeError(f"no descent within step limit for n={n}")
        checked_scan += 1
        max_scan_n = n
    print(
        "E2 Mersenne preimage: PASS "
        f"(struct n=1 mod 6: {checked_struct}; "
        f"orbit scan odd 3 <= n <= {max_scan_n}, checked={checked_scan}; "
        f"window-gap checks: {checked_gap}; "
        f"worst K/n={worst_k_over_n:.3f} at n={worst_k_over_n_n})"
    )


def check_s4(limit: int) -> None:
    """Certify M_{n+4}=2^{n+4}-1 is absent from the pre-descent a_n-orbit.

    This is the e=1 L=1 height point with s=4 (Lemma SD-L1-s4). For n>=11
    also checks that the affine E-window is empty on every pre-descent index
    (i_* > K_down). Small odd n in {3,5,7,9} are orbit-settled in Avenue A;
    n=5 may have a nonempty window without hitting the target.
    """
    checked_scan = 0
    checked_gap = 0
    max_scan_n = 3
    nonempty_small = 0
    for n in range(3, limit + 1, 2):
        a_n = (3**n - 1) // 2
        target = (1 << (n + 4)) - 1
        assert a_n != target, (n, a_n)
        threshold = (1 << n) - 1
        e0 = 1 + v2(n + 1)
        x1 = (3 ** (n + 1) - 1) // (1 << (e0 + 1))
        assert x1 != target, (n, x1)
        if n >= 11:
            assert x1 > target, (n, x1, target)
        x = a_n
        for step in range(0, 200_000 + 1):
            if step > 0 and x < threshold:
                k_down = step
                assert k_down <= 6 * n, (n, k_down)
                break
            assert x != target, (n, step, x)
            if n >= 11 and step >= 1:
                assert not _window_has_power_of_two_for(n, step, a_n, target), (
                    n,
                    step,
                )
                checked_gap += 1
            elif n == 5 and step >= 1:
                if _window_has_power_of_two_for(n, step, a_n, target):
                    nonempty_small += 1
            value = 3 * x + 1
            x = value >> v2(value)
        else:
            raise RuntimeError(f"no descent within step limit for n={n}")
        checked_scan += 1
        max_scan_n = n
    print(
        "S4 Mersenne height point: PASS "
        f"(orbit scan odd 3 <= n <= {max_scan_n}, checked={checked_scan}; "
        f"window-gap checks: {checked_gap}; "
        f"n=5 nonempty-window indices observed={nonempty_small})"
    )


def check_k_linear(limit: int) -> None:
    """Certify K_down(n) <= 6n for every odd n in the domain.

    Supports Lemma SD-K-linear (finite half). Worst ratio is 6 at n=5.
    """
    worst_ratio = 0.0
    worst_n = 3
    worst_k = 1
    checked = 0
    for n in range(3, limit + 1, 2):
        threshold = (1 << n) - 1
        x = (3**n - 1) // 2
        for step in range(0, 200_000 + 1):
            if step > 0 and x < threshold:
                k_down = step
                assert k_down <= 6 * n, (n, k_down)
                ratio = k_down / n
                if ratio > worst_ratio:
                    worst_ratio = ratio
                    worst_n = n
                    worst_k = k_down
                break
            value = 3 * x + 1
            x = value >> v2(value)
        else:
            raise RuntimeError(f"no descent within step limit for n={n}")
        checked += 1
    print(
        "K_down linear bound: PASS "
        f"(odd 3 <= n <= {limit}, checked={checked}; "
        f"worst K/n={worst_ratio:.4f} at n={worst_n}, K={worst_k}; "
        f"target K <= 6n)"
    )


def check_h_linear(limit: int) -> None:
    """Certify H(n) <= 5n-2 (Gap SD-K-survivor, finite half).

    H is the shortcut-step count from a_n to the first value < 2^n-1.
    Saturation H = 5n-2 occurs at n=23 on the tested domain.
    """
    if limit < 7:
        print("H linear bound: SKIP (need limit >= 7)")
        return
    worst_slack = None
    worst_n = 7
    worst_h = 0
    checked = 0
    for n in range(7, limit + 1, 2):
        threshold = (1 << n) - 1
        budget = 5 * n - 2
        x = (3**n - 1) // 2
        shortcut = 0
        while x >= threshold:
            raw = 3 * x + 1
            e = v2(raw)
            crossed = False
            for division in range(1, e + 1):
                shortcut += 1
                candidate = raw >> division
                if candidate < threshold:
                    x = candidate
                    crossed = True
                    break
            if crossed:
                break
            x = raw >> e
        assert shortcut <= budget, (n, shortcut, budget)
        slack = budget - shortcut
        if worst_slack is None or slack < worst_slack:
            worst_slack = slack
            worst_n = n
            worst_h = shortcut
        checked += 1
    assert worst_slack is not None
    print(
        "H linear bound: PASS "
        f"(odd 7 <= n <= {limit}, checked={checked}; "
        f"tightest slack={worst_slack} at n={worst_n}, H={worst_h}, "
        f"budget={5 * worst_n - 2}; target H <= 5n-2)"
    )


def check_rho_cap(limit: int) -> None:
    """Certify rho_t(n) <= floor(11n/4) for t=5n-2 (Gap SD-K-nonconcentration).

    Counts odd U-steps in the first t shortcut steps from a_n, continuing
    after descent below T. By Lemma SD-K-nc-strong this implies H <= t.
    """
    if limit < 7:
        print("rho_t cap: SKIP (need limit >= 7)")
        return
    worst_slack = None
    worst_n = 7
    worst_rho = 0
    checked = 0
    for n in range(7, limit + 1, 2):
        t = 5 * n - 2
        cap = (11 * n) // 4
        a_n = (3**n - 1) // 2
        assert a_n < (1 << t), (n, a_n.bit_length(), t)
        x = a_n
        odd = 0
        steps = 0
        while steps < t:
            raw = 3 * x + 1
            e = v2(raw)
            for division in range(1, e + 1):
                steps += 1
                if division == 1:
                    odd += 1
                x = raw >> division
                if steps >= t:
                    break
            else:
                continue
            break
        assert odd <= cap, (n, odd, cap)
        slack = cap - odd
        if worst_slack is None or slack < worst_slack:
            worst_slack = slack
            worst_n = n
            worst_rho = odd
        checked += 1
    assert worst_slack is not None
    print(
        "rho_t cap: PASS "
        f"(odd 7 <= n <= {limit}, checked={checked}; "
        f"tightest cap-rho={worst_slack} at n={worst_n}, "
        f"rho_t={worst_rho}, cap={(11 * worst_n) // 4}; "
        f"target rho_t <= floor(11n/4))"
    )


def check_even_budget(limit: int) -> None:
    """Certify even-U count >= t - floor(11n/4) (Gap SD-K-even-budget).

    Equivalent to check_rho_cap by Lemma SD-K-even-id: every even U-step is
    a trailing division of a payout (seed or suffix). Asserts the identity
    rho + even == t and the even lower bound.
    """
    if limit < 7:
        print("even budget: SKIP (need limit >= 7)")
        return
    worst_slack = None
    worst_n = 7
    worst_even = 0
    worst_need = 0
    checked = 0
    for n in range(7, limit + 1, 2):
        t = 5 * n - 2
        cap = (11 * n) // 4
        need = t - cap
        a_n = (3**n - 1) // 2
        x = a_n
        odd = 0
        even = 0
        steps = 0
        while steps < t:
            raw = 3 * x + 1
            e = v2(raw)
            for division in range(1, e + 1):
                steps += 1
                if division == 1:
                    odd += 1
                else:
                    even += 1
                x = raw >> division
                if steps >= t:
                    break
            else:
                continue
            break
        assert odd + even == t, (n, odd, even, t)
        assert even >= need, (n, even, need, odd, cap)
        slack = even - need
        if worst_slack is None or slack < worst_slack:
            worst_slack = slack
            worst_n = n
            worst_even = even
            worst_need = need
        checked += 1
    assert worst_slack is not None
    print(
        "even budget: PASS "
        f"(odd 7 <= n <= {limit}, checked={checked}; "
        f"tightest even-need slack={worst_slack} at n={worst_n}, "
        f"even={worst_even}, need={worst_need}; "
        f"target even >= 5n-2-floor(11n/4))"
    )


def check_nine_eleven(limit: int) -> None:
    """Certify 11*(t-rho) >= 9*(rho-1) except the known saturator n=23.

    Sufficient for Gap SD-K-nonconcentration by Lemma SD-K-911-implies:
    the inequality forces rho <= floor((11t+9)/20) <= floor(11n/4).
    At n=23 it fails (rho=63, bound 62) while rho=cap still holds.
    """
    if limit < 7:
        print("nine-eleven: SKIP (need limit >= 7)")
        return
    exceptions = []
    worst_score = None
    worst_n = 7
    checked = 0
    for n in range(7, limit + 1, 2):
        t = 5 * n - 2
        cap = (11 * n) // 4
        a_n = (3**n - 1) // 2
        x = a_n
        odd = 0
        steps = 0
        while steps < t:
            raw = 3 * x + 1
            e = v2(raw)
            for division in range(1, e + 1):
                steps += 1
                if division == 1:
                    odd += 1
                x = raw >> division
                if steps >= t:
                    break
            else:
                continue
            break
        even = t - odd
        score = 11 * even - 9 * (odd - 1)
        bound = (11 * t + 9) // 20
        if score < 0:
            exceptions.append(n)
            assert n == 23, (n, odd, even, score, cap)
            assert odd <= cap, (n, odd, cap)
        else:
            assert odd <= bound <= cap, (n, odd, bound, cap)
        if worst_score is None or score < worst_score:
            worst_score = score
            worst_n = n
        checked += 1
    assert worst_score is not None
    print(
        "nine-eleven: PASS "
        f"(odd 7 <= n <= {limit}, checked={checked}; "
        f"exceptions={exceptions} (allowed: [23]); "
        f"tightest 11*even-9*(rho-1)={worst_score} at n={worst_n}; "
        f"target 11*(t-rho)>=9*(rho-1) except n=23)"
    )


def ceiling_forces_descent_6(n: int) -> bool:
    """Exact rational envelope for Lemma SD-K-density-6."""
    target = (1 << n) - 1
    repunit = (3**n - 1) // 2
    t = 6 * n
    rho = (33 * n) // 10
    upper = (
        Fraction(repunit, target)
        * Fraction(3**rho, 1 << t)
        * Fraction(3 * target + 1, 3 * target) ** rho
    )
    return upper < 1


def check_density6_envelope(limit: int) -> None:
    """Certify the SD-K-density-6 rational envelope for every odd n in range."""
    if limit < 7:
        print("density-6 envelope: SKIP (need limit >= 7)")
        return
    checked = 0
    worst_upper = None
    worst_n = 7
    for n in range(7, limit + 1, 2):
        target = (1 << n) - 1
        repunit = (3**n - 1) // 2
        t = 6 * n
        rho = (33 * n) // 10
        upper = (
            Fraction(repunit, target)
            * Fraction(3**rho, 1 << t)
            * Fraction(3 * target + 1, 3 * target) ** rho
        )
        assert upper < 1, (n, float(upper))
        if worst_upper is None or upper > worst_upper:
            worst_upper = upper
            worst_n = n
        checked += 1
    assert worst_upper is not None
    print(
        "density-6 envelope: PASS "
        f"(odd 7 <= n <= {limit}, checked={checked}; "
        f"largest upper={float(worst_upper):.6f} at n={worst_n}; "
        f"target U^t/T < 1 under rho <= floor(33n/10), t=6n)"
    )


def check_h_linear_6(limit: int) -> None:
    """Certify H(n) <= 6n (Gap SD-K-survivor-6, finite half)."""
    if limit < 7:
        print("H linear-6: SKIP (need limit >= 7)")
        return
    worst_slack = None
    worst_n = 7
    worst_h = 0
    checked = 0
    for n in range(7, limit + 1, 2):
        budget = 6 * n
        threshold = (1 << n) - 1
        x = (3**n - 1) // 2
        steps = 0
        while True:
            raw = 3 * x + 1
            e = v2(raw)
            for division in range(1, e + 1):
                steps += 1
                cand = raw >> division
                if cand < threshold:
                    assert steps <= budget, (n, steps, budget)
                    slack = budget - steps
                    if worst_slack is None or slack < worst_slack:
                        worst_slack = slack
                        worst_n = n
                        worst_h = steps
                    checked += 1
                    break
                x = cand
            else:
                continue
            break
    assert worst_slack is not None
    print(
        "H linear-6: PASS "
        f"(odd 7 <= n <= {limit}, checked={checked}; "
        f"tightest slack={worst_slack} at n={worst_n}, H={worst_h}, "
        f"budget={6 * worst_n}; target H <= 6n)"
    )


def check_rho_cap_6(limit: int) -> None:
    """Certify rho_{6n} <= floor(33n/10) except the known miss n=11.

    Gap SD-K-nc-6. At n=11 one has rho=38 > 36 while H(11)=46 <= 66,
    so Gap SD-K-survivor-6 still holds.
    """
    if limit < 7:
        print("rho_t cap-6: SKIP (need limit >= 7)")
        return
    exceptions = []
    worst_slack = None
    worst_n = 7
    worst_rho = 0
    checked = 0
    for n in range(7, limit + 1, 2):
        t = 6 * n
        cap = (33 * n) // 10
        x = (3**n - 1) // 2
        odd = 0
        steps = 0
        while steps < t:
            raw = 3 * x + 1
            e = v2(raw)
            for division in range(1, e + 1):
                steps += 1
                if division == 1:
                    odd += 1
                x = raw >> division
                if steps >= t:
                    break
            else:
                continue
            break
        if odd > cap:
            exceptions.append(n)
            assert n == 11, (n, odd, cap)
        else:
            slack = cap - odd
            if worst_slack is None or slack < worst_slack:
                worst_slack = slack
                worst_n = n
                worst_rho = odd
        checked += 1
    print(
        "rho_t cap-6: PASS "
        f"(odd 7 <= n <= {limit}, checked={checked}; "
        f"exceptions={exceptions} (allowed: [11]); "
        f"tightest non-exception cap-rho={worst_slack} at n={worst_n}, "
        f"rho={worst_rho}, cap={(33 * worst_n) // 10}; "
        f"target rho_{{6n}} <= floor(33n/10) except n=11)"
    )


def check_nine_eleven_6(limit: int) -> None:
    """Certify score = 11*even - 9*(rho-1) >= 11 except n=11.

    Gap SD-K-911-6-strong. By Lemma SD-K-911-6-strong-implies this forces
    rho <= floor((66n-2)/20) <= floor(33n/10). Equality score=11 at n=17.
    """
    if limit < 7:
        print("nine-eleven-6: SKIP (need limit >= 7)")
        return
    exceptions = []
    worst_score = None
    worst_n = 7
    checked = 0
    for n in range(7, limit + 1, 2):
        t = 6 * n
        cap = (33 * n) // 10
        x = (3**n - 1) // 2
        odd = 0
        steps = 0
        while steps < t:
            raw = 3 * x + 1
            e = v2(raw)
            for division in range(1, e + 1):
                steps += 1
                if division == 1:
                    odd += 1
                x = raw >> division
                if steps >= t:
                    break
            else:
                continue
            break
        even = t - odd
        score = 11 * even - 9 * (odd - 1)
        bound = (66 * n - 2) // 20
        if n == 11:
            exceptions.append(n)
            assert score < 11, (n, score)
        else:
            assert score >= 11, (n, score, odd, even)
            assert odd <= bound <= cap, (n, odd, bound, cap, score)
        if worst_score is None or score < worst_score:
            worst_score = score
            worst_n = n
        checked += 1
    assert worst_score is not None
    print(
        "nine-eleven-6: PASS "
        f"(odd 7 <= n <= {limit}, checked={checked}; "
        f"exceptions={exceptions} (allowed: [11]); "
        f"tightest score={worst_score} at n={worst_n}; "
        f"target score >= 11 except n=11)"
    )


def check_block8_first(limit: int) -> None:
    """Certify first-block dictionary for Gap SD-K-block-8 (n ≡ 1 mod 8).

    Checks Lemmas SD-K-v2-35 / first-e / first-h-good on odd n=17..limit
    with n ≡ 1 mod 8: e = v2(3^{n+2}+5)-3, and the stable (e,h,Delta)
    values on n mod 64 in {1,33,49,57}.
    """
    if limit < 17:
        print("block8-first: SKIP (need limit >= 17)")
        return

    def h_of(x: int) -> int:
        return v2(x + 1)

    checked = 0
    for n in range(17, limit + 1, 8):
        assert n % 8 == 1
        x1 = (3 ** (n + 1) - 1) // 8
        assert h_of(x1) == 1, (n, x1 % 4)
        e = v2(3 * x1 + 1)
        assert e == v2(3 ** (n + 2) + 5) - 3, (n, e)
        y = (3 * x1 + 1) >> e
        hl = h_of(y)
        delta = 11 * (e - 1) - 9 * hl
        r = n % 64
        if n >= 33 and n % 32 == 1:
            assert e == 2, (n, e)
        if r in (1, 33):
            assert n < 33 or (e == 2 and hl == 1 and delta == 2), (n, e, hl, delta)
        elif r == 49:
            assert e == 2 and hl == 2 and delta == -7, (n, e, hl, delta)
        elif r == 57:
            assert e == 3 and hl == 1 and delta == 13, (n, e, hl, delta)
        elif r == 17:
            assert e == 2 and hl >= 3, (n, e, hl)
        elif r == 25:
            assert e == 3 and hl >= 2, (n, e, hl)
        elif r == 41:
            assert e == 4, (n, e)
        checked += 1
    # pure v2 lemma census
    for k in range(0, max(1, (limit // 32) + 2)):
        m = 3 + 32 * k
        assert v2(3**m + 5) == 5, (m, v2(3**m + 5))
    print(
        "block8-first: PASS "
        f"(n=17..{limit} step 8, checked={checked}; "
        f"stable first Delta on mod64 in {{1,33,49,57}}; "
        f"v2(3^{{3+32k}}+5)=5 through k<={limit // 32 + 1})"
    )


def check_block8_mod17(limit: int) -> None:
    """Certify h1 formula / parity and rest >= 9*h1-11 for n=64k+17.

    Supports Lemmas SD-K-h1-17 / h1-parity and Gap SD-K-block-8-17 (finite).
    """
    if limit < 17:
        print("block8-mod17: SKIP (need limit >= 17)")
        return

    def h_of(x: int) -> int:
        return v2(x + 1)

    checked = 0
    worst_margin = None
    worst_n = 17
    for n in range(17, limit + 1, 64):
        k = (n - 17) // 64
        x1 = (3 ** (n + 1) - 1) // 8
        e = v2(3 * x1 + 1)
        assert e == 2, (n, e)
        h1 = v2(3 ** (n + 2) + 37) - 5
        y = (3 * x1 + 1) >> 2
        assert h_of(y) == h1, (n, h_of(y), h1)
        if k >= 1 and k % 2 == 1:
            assert h1 == 3, (n, k, h1)
        if k >= 1 and k % 4 == 2:
            assert h1 == 4, (n, k, h1)
        if k == 0:
            assert h1 == 5, (n, h1)

        # e2 formula / odd-3mod4 lemma
        m = (3 ** (n + 2) + 37) // (2 ** (h1 + 5))
        assert m % 2 == 1, (n, m)
        y = (3 ** (n + 2) + 5) // 32
        x2 = (3 ** (h1 - 1) * (y + 1)) // (2 ** (h1 - 1)) - 1
        e2 = v2(3 * x2 + 1)
        assert e2 == 1 + v2((3**h1) * m - 1), (n, e2, h1, m)
        if k % 4 == 3:
            assert e2 == 2, (n, k, e2)
        if k % 8 == 3:
            # Lemma SD-K-h2-3mod8: second block e=2, h=1
            y2 = (3 * x2 + 1) >> e2
            assert e2 == 2 and h_of(y2) == 1, (n, k, e2, h_of(y2))
            # rail to x3, then check e3-stable classes
            x3 = y2
            while h_of(x3) >= 2:
                x3 = (3 * x3 + 1) >> 1
            e3 = v2(3 * x3 + 1)
            y3 = (3 * x3 + 1) >> e3
            h3 = h_of(y3)
            r64 = k % 64
            if r64 == 3:
                assert e3 == 3 and h3 == 1, (n, k, e3, h3)
            elif r64 in (11, 43):
                assert e3 == 2 and h3 == 1, (n, k, e3, h3)
            elif r64 == 59:
                assert e3 == 2 and h3 == 2, (n, k, e3, h3)
            # fourth-block clearance theorems
            x4 = y3
            while h_of(x4) >= 2:
                x4 = (3 * x4 + 1) >> 1
            e4 = v2(3 * x4 + 1)
            h4 = h_of((3 * x4 + 1) >> e4)
            if k % 256 == 3:
                assert e4 == 2 and h4 == 1, (n, k, e4, h4)
                assert 2 + 13 + 2 >= 16
            if k % 256 == 171:
                assert e4 == 3 and h4 == 1, (n, k, e4, h4)
                assert 2 + 2 + 13 >= 16
            if k % 512 == 323:
                assert e4 == 3 and h4 == 1, (n, k, e4, h4)
                assert 2 + 13 + 13 >= 16
            if k % 1024 == 579:
                assert e4 == 3 and h4 == 2, (n, k, e4, h4)
                assert 2 + 13 + 4 >= 16
        if k >= 1 and k % 2 == 1:
            # Lemma SD-K-x2-mod8
            if k % 4 == 1:
                assert x2 % 8 == 5, (n, k, x2 % 8)
            else:
                assert x2 % 8 == 1, (n, k, x2 % 8)
        if n == 81:
            # Lemma SD-K-81-clear
            y2 = (3 * x2 + 1) >> e2
            assert e2 == 5 and h_of(y2) == 3, (n, e2, h_of(y2))
            assert 11 * (e2 - 1) - 9 * h_of(y2) == 17

        # residual sum after first block
        t = 6 * n
        steps = 2 + e  # seed + first payout (e=2)
        x = y
        # rails of first landing
        while h_of(x) >= 2 and steps < t:
            steps += 1
            x = (3 * x + 1) >> 1
        rest = 0
        blocks = 0
        extra = 0
        odd_h = 0
        while steps < t:
            raw = 3 * x + 1
            ee = v2(raw)
            rem = t - steps
            if ee > rem:
                rest += 11 * max(0, rem - 1) - 9
                break
            steps += ee
            x = raw >> ee
            hl = h_of(x)
            rails = 0
            while h_of(x) >= 2 and steps < t:
                steps += 1
                x = (3 * x + 1) >> 1
                rails += 1
            heff = 1 + rails if rails < hl - 1 else hl
            rest += 11 * (ee - 1) - 9 * heff
            blocks += 1
            extra += ee - 2
            odd_h += heff
        need = 9 * h1 - 11
        assert rest >= need, (n, rest, need, h1)
        if n >= 145 and blocks > 0:
            # Gap SD-K-EB-17 finite certificate
            assert extra * 10 >= 9 * blocks, (n, extra, blocks)
            assert odd_h * 10 <= 21 * blocks, (n, odd_h, blocks)
        margin = rest - need
        if worst_margin is None or margin < worst_margin:
            worst_margin = margin
            worst_n = n
        checked += 1
    assert worst_margin is not None
    print(
        "block8-mod17: PASS "
        f"(n=17..{limit} step 64, checked={checked}; "
        f"h1/x2-mod8/EB ok; tightest rest-(9h1-11)={worst_margin} "
        f"at n={worst_n}; target rest >= 9h1-11)"
    )


def _block_deltas_after_first(n: int, max_blocks: int = 6) -> tuple[int, list[int]]:
    """Return (h1, list of Delta_j for j=2..max_blocks) on the residual tail."""
    h1 = v2(3 ** (n + 2) + 37) - 5
    x1 = (3 ** (n + 1) - 1) // 8
    assert v2(3 * x1 + 1) == 2
    x = (3 * x1 + 1) >> 2
    while h_of(x) >= 2:
        x = (3 * x + 1) >> 1
    deltas: list[int] = []
    for _ in range(2, max_blocks + 1):
        raw = 3 * x + 1
        e = v2(raw)
        x = raw >> e
        hl = h_of(x)
        rails = 0
        while h_of(x) >= 2:
            x = (3 * x + 1) >> 1
            rails += 1
        heff = 1 + rails if rails < hl - 1 else hl
        deltas.append(11 * (e - 1) - 9 * heff)
        while h_of(x) >= 2:
            x = (3 * x + 1) >> 1
    return h1, deltas


def _iter_k11_mod64(limit_k: int):
    """Yield (n, k) for k ≡ 11 (mod 64) with 11 <= k <= limit_k."""
    for k in range(11, limit_k + 1, 64):
        yield 64 * k + 17, k


def check_block8_k11_mod256(limit_k: int) -> None:
    """Certify Lemma SD-K-b4start-mod256 / Cor SD-K-blocks24-k11mod64.

    For k ≡ 11 (mod 64), checks block-4 start x mod 32 and (Δ2,Δ3,Δ4) on
    each k mod 256 slice inside that class.  ``limit_k`` is the maximum k
    scanned (not the maximum n).
    """
    if limit_k < 11:
        print("block8-k11-mod256: SKIP (need limit_k >= 11)")
        return

    expected_delta = {
        11: (2, 2, 2),
        75: (2, 2, -7),
        139: (2, 2, 2),
        203: (2, 2, -16),
    }
    expected_x32 = {
        11: {1, 17},
        75: {25},
        139: {1, 17},
        203: {9},
    }

    checked = 0
    for n, k in _iter_k11_mod64(limit_k):
        r = k % 256
        assert r in expected_delta, (n, k, r)
        if r == 203 and k % 512 != 203:
            continue
        _, deltas = _block_deltas_after_first(n, max_blocks=4)
        assert tuple(deltas[:3]) == expected_delta[r], (n, k, r, deltas[:3])

        # block-4 start residue (after blocks 2 and 3)
        x1 = (3 ** (n + 1) - 1) // 8
        x = (3 * x1 + 1) >> 2
        while h_of(x) >= 2:
            x = (3 * x + 1) >> 1
        for _ in range(2):
            raw = 3 * x + 1
            e = v2(raw)
            x = raw >> e
            while h_of(x) >= 2:
                x = (3 * x + 1) >> 1
            while h_of(x) >= 2:
                x = (3 * x + 1) >> 1
        assert x % 32 in expected_x32[r], (n, k, r, x % 32)
        checked += 1

    print(
        "block8-k11-mod256: PASS "
        f"(k≡11 mod 64, k<= {limit_k}, checked={checked}; "
        f"Δ2..4 and block-4 start x mod 32 on slices 11/75/139/203 mod 256; "
        f"203 slice only at k≡203 mod 512)"
    )


def check_block8_k11_mod512(limit_k: int) -> None:
    """Certify mod-512 refinements on k≡11 (mod 64) (Lemma SD-K-b4start-mod512,
    Cor SD-K-block5-mod512-k11slice).  ``limit_k`` is the maximum k scanned."""
    if limit_k < 11:
        print("block8-k11-mod512: SKIP (need limit_k >= 11)")
        return

    b4_203 = 0
    for n, k in _iter_k11_mod64(limit_k):
        if k % 512 != 203:
            continue
        _, deltas = _block_deltas_after_first(n, max_blocks=4)
        assert tuple(deltas[:3]) == (2, 2, -16), (n, k, deltas[:3])
        b4_203 += 1

    b5_267 = 0
    b5_523 = 0
    b5_779 = 0
    b5_11 = 0
    for n, k in _iter_k11_mod64(limit_k):
        _, deltas = _block_deltas_after_first(n, max_blocks=5)
        if k % 512 == 267:
            assert tuple(deltas[:4]) == (2, 2, 2, 2), (n, k, deltas[:4])
            b5_267 += 1
        if k % 1024 == 523:
            assert deltas[3] == -7 and tuple(deltas[:3]) == (2, 2, 2), (n, k, deltas)
            b5_523 += 1
        if k % 1024 == 779:
            assert deltas[3] == 2 and tuple(deltas[:3]) == (2, 2, 2), (n, k, deltas)
            b5_779 += 1
        if k % 2048 == 11:
            assert deltas[3] == -16 and tuple(deltas[:3]) == (2, 2, 2), (n, k, deltas)
            b5_11 += 1

    print(
        "block8-k11-mod512: PASS "
        f"(k<= {limit_k}; b4 k≡203 mod512={b4_203}; "
        f"b5 k≡267 mod512={b5_267}, k≡523 mod1024={b5_523}, "
        f"k≡779 mod1024={b5_779}, k≡11 mod2048={b5_11})"
    )


def check_block8_k11_mod8192(limit_k: int) -> None:
    """Certify mod-8192 block-4/5/6 refinements on k≡11 (mod 64).

    Supports Lemma SD-K-b4start-mod8192, Cor SD-K-block5-mod8192-1035,
    Cor SD-K-block6-mod8192-k267slice and the 267-family gap theorems.
    """
    if limit_k < 11:
        print("block8-k11-mod8192: SKIP (need limit_k >= 11)")
        return

    b4_mod8192 = {
        3531: (2, 2, -52),
        7627: (2, 2, -88),
    }
    b4_count = 0
    for n, k in _iter_k11_mod64(limit_k):
        if k % 8192 not in b4_mod8192:
            continue
        _, deltas = _block_deltas_after_first(n, max_blocks=4)
        assert tuple(deltas[:3]) == b4_mod8192[k % 8192], (n, k, deltas[:3])
        b4_count += 1

    b5_mod8192 = {
        1035: -43,
        3083: -25,
        5131: -34,
        7179: -25,
    }
    b5_count = 0
    for n, k in _iter_k11_mod64(limit_k):
        if k % 8192 not in b5_mod8192:
            continue
        _, deltas = _block_deltas_after_first(n, max_blocks=5)
        assert tuple(deltas[:3]) == (2, 2, 2), (n, k, deltas[:3])
        assert deltas[3] == b5_mod8192[k % 8192], (n, k, deltas)
        b5_count += 1

    # Block 6 on k≡267 (mod 512): stable (Δ2..Δ6) at mod 8192.
    b6_mod8192 = {
        267: (2, 2, 2, 2, 35),
        779: (2, 2, 2, 2, 2),
        1291: (2, 2, 2, 2, 13),
        1803: (2, 2, 2, 2, -16),
        2315: (2, 2, 2, 2, -12),
        2827: (2, 2, 2, 2, 2),
        3339: (2, 2, 2, 2, 4),
        3851: (2, 2, 2, 2, -7),
        4363: (2, 2, 2, 2, 46),
        4875: (2, 2, 2, 2, 2),
        5387: (2, 2, 2, 2, 13),
        5899: (2, 2, 2, 2, -34),
        6411: (2, 2, 2, 2, 24),
        6923: (2, 2, 2, 2, 2),
        7435: (2, 2, 2, 2, -5),
        7947: (2, 2, 2, 2, -7),
    }
    b6_count = 0
    gap6_count = 0
    for n, k in _iter_k11_mod64(limit_k):
        if k % 512 != 267:
            continue
        _, deltas = _block_deltas_after_first(n, max_blocks=6)
        r = k % 8192
        assert r in b6_mod8192, (n, k, r, tuple(deltas[:5]))
        assert tuple(deltas[:5]) == b6_mod8192[r], (n, k, r, deltas[:5])
        b6_count += 1
        if sum(deltas[:5]) >= 16:
            gap6_count += 1

    b7_mod8192 = {
        267: 13,
        779: 13,
        1291: -7,
        1803: 13,
        2315: 4,
        2827: 2,
        3339: 15,
        3851: 2,
        4363: -7,
        4875: 46,
        5387: 13,
        5899: 2,
        6411: -25,
        6923: -34,
        7435: 24,
        7947: 13,
    }
    b7_count = 0
    gap7_count = 0
    for n, k in _iter_k11_mod64(limit_k):
        if k % 512 != 267:
            continue
        _, deltas = _block_deltas_after_first(n, max_blocks=7)
        r = k % 8192
        assert r in b7_mod8192, (n, k, r, deltas[5:])
        assert deltas[5] == b7_mod8192[r], (n, k, r, deltas[5])
        b7_count += 1
        if sum(deltas[:6]) >= 16:
            gap7_count += 1

    print(
        "block8-k11-mod8192: PASS "
        f"(k<= {limit_k}; b4 mod8192={b4_count}; b5 mod8192={b5_count}; "
        f"b6 k≡267 mod512={b6_count}, cum6>=16={gap6_count}; "
        f"b7={b7_count}, cum7>=16={gap7_count})"
    )


def check_height_s(limit: int, s_max: int = 32) -> None:
    """Certify y_n(s)=s*2^{n+2}-1 absent for 3<=s<=s_max on pre-descent orbits.

    Supports Lemma SD-L1-s-fixed / SD-L1-s6. For every odd n>=13 the affine
    E-window is required empty for each such s (i_* > K_down). Smaller n may
    have nonempty windows; absence is by direct orbit scan only.
    """
    if s_max < 3:
        raise ValueError("s_max must be >= 3")
    checked_pairs = 0
    checked_gap = 0
    max_scan_n = 3
    for n in range(3, limit + 1, 2):
        a_n = (3**n - 1) // 2
        threshold = (1 << n) - 1
        shift = 1 << (n + 2)
        targets = {s * shift - 1: s for s in range(3, s_max + 1)}
        for s, target in ((s, s * shift - 1) for s in range(3, s_max + 1)):
            assert a_n != target, (n, s, a_n)
        x = a_n
        for step in range(0, 200_000 + 1):
            if step > 0 and x < threshold:
                break
            hit_s = targets.get(x)
            assert hit_s is None, (n, step, hit_s, x)
            if n >= 13 and step >= 1:
                for s in range(3, s_max + 1):
                    target = s * shift - 1
                    assert not _window_has_power_of_two_for(n, step, a_n, target), (
                        n,
                        step,
                        s,
                    )
                    checked_gap += 1
            value = 3 * x + 1
            x = value >> v2(value)
        else:
            raise RuntimeError(f"no descent within step limit for n={n}")
        checked_pairs += s_max - 2
        max_scan_n = n
    print(
        "Height-s points: PASS "
        f"(s=3..{s_max}, odd 3 <= n <= {max_scan_n}, "
        f"pair-scans={checked_pairs}; window-gap checks: {checked_gap})"
    )


def hat_e_counts(m: int) -> list[int]:
    """Return count[k] = number of odd residues mod 2^m with hat_e == k.

    Uses Lemma SD-residue-sum: #{hat_e >= k} = 2^{m-k} for 1 <= k <= m,
    plus one class with hat_e >= m+1 when m is odd.
    """
    # index by exact valuation; allocate enough room for the optional >m class
    ge = [0] * (m + 3)
    for k in range(1, m + 1):
        ge[k] = 1 << (m - k)
    if m % 2 == 1:
        ge[m + 1] = 1
    counts = [0] * (m + 3)
    for k in range(1, m + 2):
        counts[k] = ge[k] - ge[k + 1]
    return counts


def s_of_j(n: int, j: int) -> int:
    """Sum of the j smallest hat_e values among odd residues mod 2^{n+1}."""
    if j <= 0:
        return 0
    counts = hat_e_counts(n + 1)
    remaining = j
    total = 0
    for k, count in enumerate(counts):
        if k == 0 or count == 0:
            continue
        take = min(remaining, count)
        total += take * k
        remaining -= take
        if remaining == 0:
            return total
    raise ValueError(f"j={j} exceeds the {1 << n} odd residues mod 2^{n+1}")


def compute_j0(n: int) -> int:
    """Least j0 <= T with S(j0) > j0*log2(3) + log2(a_n/T) + j0*log2(1+1/(3T))."""
    threshold = (1 << n) - 1
    a_n = (3**n - 1) // 2
    log_base = math.log2(a_n / threshold)
    log3 = math.log2(3)
    log_alpha = math.log2(1 + 1 / (3 * threshold))
    # Walk j upward; S(j) grows ~2j while the RHS grows ~j log2(3) < 2j.
    max_j = threshold
    for j in range(1, max_j + 1):
        if s_of_j(n, j) > j * log3 + log_base + j * log_alpha:
            return j
    raise RuntimeError(f"j0 not found for n={n} within T={threshold}")


def check_early_collisions(limit: int, j0_check_limit: int = 21) -> None:
    """Probe residue collisions mod 2^{n+1} on the stay-above path.

    For each odd n, walk through first descent and record the first index
    pair with x_i ≡ x_j (mod 2^{n+1}) while still x >= T.  Such a collision
    before j0(n) is exactly the early-collision case left open by Theorem
    SD-length-distinct.  Also verify the small-n values j0(5)=30, j0(7)=115.
    """
    if j0_check_limit >= 5:
        assert compute_j0(5) == 30, compute_j0(5)
    if j0_check_limit >= 7:
        assert compute_j0(7) == 115, compute_j0(7)

    collisions: list[tuple[int, int, int, int]] = []
    no_collision = 0
    shortest_first = None  # (L, n, i, j)
    for n in range(3, limit + 1, 2):
        threshold = (1 << n) - 1
        modulus = 1 << (n + 1)
        x = (3**n - 1) // 2
        seen: dict[int, int] = {}
        first = None
        for step in range(0, 200_000 + 1):
            if step > 0 and x < threshold:
                break
            residue = x % modulus
            prev = seen.get(residue)
            if prev is not None:
                first = (prev, step, x)
                break
            seen[residue] = step
            value = 3 * x + 1
            x = value >> v2(value)
        else:
            raise RuntimeError(f"no descent within step limit for n={n}")

        if first is None:
            no_collision += 1
            continue
        i, j, _ = first
        L = j - i
        collisions.append((n, i, j, L))
        if shortest_first is None or L < shortest_first[0]:
            shortest_first = (L, n, i, j)

    # Under the contradiction K_down >= T+1 the gate needs no early collision
    # with stay-above through j0.  On the actual finite domain every seed has
    # K_down <= T (checked in verify), so these collisions are pre-descent
    # facts on orbits that already descend early — not falsifiers of SD1.
    print(
        "Early residue collisions mod 2^{n+1} through first descent: "
        f"PASS scan (odd 3 <= n <= {limit}; "
        f"no-collision seeds={no_collision}; "
        f"with-collision seeds={len(collisions)})"
    )
    if collisions:
        assert shortest_first is not None
        # n=5 is the known short-return prototype in the Avenue A note.
        n5 = [c for c in collisions if c[0] == 5]
        assert n5, "expected a pre-descent residue collision for n=5"
        print(
            f"shortest collision length L={shortest_first[0]} "
            f"at n={shortest_first[1]} (i={shortest_first[2]}, "
            f"j={shortest_first[3]}); "
            f"n=5 first collision i={n5[0][1]}, j={n5[0][2]}, L={n5[0][3]}"
        )
        # Sample: report up to five smallest-n collisions for the writeup.
        sample = ", ".join(
            f"n={n}:L={L}@{i}->{j}" for n, i, j, L in collisions[:5]
        )
        print(f"first five collision seeds: {sample}")
    else:
        print("no pre-descent residue collisions in the domain")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=5001)
    parser.add_argument(
        "--check-stay",
        action="store_true",
        help="also verify SD1S and the strong slack bound",
    )
    parser.add_argument(
        "--check-seed-l1",
        action="store_true",
        help="also verify the seed L=1 2-adic gap",
    )
    parser.add_argument(
        "--check-l1-gates",
        action="store_true",
        help="also verify max h < n+2 and max v2(x-1) < n+3",
    )
    parser.add_argument(
        "--check-e2-preimage",
        action="store_true",
        help="also verify absence of (2^{n+4}-5)/3 on the a_n-orbit",
    )
    parser.add_argument(
        "--check-early-collisions",
        action="store_true",
        help="probe residue collisions mod 2^{n+1} before first descent",
    )
    parser.add_argument(
        "--check-s4",
        action="store_true",
        help="also verify absence of M_{n+4}=2^{n+4}-1 on the a_n-orbit",
    )
    parser.add_argument(
        "--check-height-s",
        action="store_true",
        help="also verify absence of s*2^{n+2}-1 for s=3..s-max",
    )
    parser.add_argument(
        "--s-max",
        type=int,
        default=32,
        help="with --check-height-s, largest s to scan (default 32)",
    )
    parser.add_argument(
        "--check-k-linear",
        action="store_true",
        help="also verify K_down(n) <= 6n",
    )
    parser.add_argument(
        "--check-h-linear",
        action="store_true",
        help="also verify shortcut H(n) <= 5n-2 (Gap SD-K-survivor finite)",
    )
    parser.add_argument(
        "--check-rho-cap",
        action="store_true",
        help="also verify rho_t <= floor(11n/4) for t=5n-2",
    )
    parser.add_argument(
        "--check-even-budget",
        action="store_true",
        help="also verify even-U count >= t-floor(11n/4) (Gap SD-K-even-budget)",
    )
    parser.add_argument(
        "--check-nine-eleven",
        action="store_true",
        help="also verify 11*(t-rho)>=9*(rho-1) except n=23",
    )
    parser.add_argument(
        "--check-density6-envelope",
        action="store_true",
        help="also verify SD-K-density-6 rational envelope (t=6n)",
    )
    parser.add_argument(
        "--check-h-linear-6",
        action="store_true",
        help="also verify H(n) <= 6n (Gap SD-K-survivor-6 finite)",
    )
    parser.add_argument(
        "--check-rho-cap-6",
        action="store_true",
        help="also verify rho_{6n} <= floor(33n/10) except n=11",
    )
    parser.add_argument(
        "--check-nine-eleven-6",
        action="store_true",
        help="also verify 6n strong score >= 11 except n=11",
    )
    parser.add_argument(
        "--check-block8-first",
        action="store_true",
        help="also verify first-block dictionary for n=1 mod 8",
    )
    parser.add_argument(
        "--check-block8-mod17",
        action="store_true",
        help="also verify h1/rest bound for n=17 mod 64",
    )
    parser.add_argument(
        "--check-block8-k11-mod256",
        action="store_true",
        help="also verify block-4 dictionary on k≡11 mod 64 slices mod 256 (limit = max k)",
    )
    parser.add_argument(
        "--check-block8-k11-mod512",
        action="store_true",
        help="also verify mod-512 block-4/5 refinements on k≡11 mod 64 (limit = max k)",
    )
    parser.add_argument(
        "--check-block8-k11-mod8192",
        action="store_true",
        help="also verify mod-8192 block-4/5/6 refinements on k≡11 mod 64 (limit = max k)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    verify(args.limit)
    if args.check_stay:
        check_stay_reduction(args.limit)
    if args.check_seed_l1:
        check_seed_L1_gap(args.limit)
    if args.check_l1_gates:
        check_L1_gates(args.limit)
    if args.check_e2_preimage:
        check_e2_preimage(args.limit)
    if args.check_early_collisions:
        check_early_collisions(args.limit)
    if args.check_s4:
        check_s4(args.limit)
    if args.check_height_s:
        check_height_s(args.limit, s_max=args.s_max)
    if args.check_k_linear:
        check_k_linear(args.limit)
    if args.check_h_linear:
        check_h_linear(args.limit)
    if args.check_rho_cap:
        check_rho_cap(args.limit)
    if args.check_even_budget:
        check_even_budget(args.limit)
    if args.check_nine_eleven:
        check_nine_eleven(args.limit)
    if args.check_density6_envelope:
        check_density6_envelope(args.limit)
    if args.check_h_linear_6:
        check_h_linear_6(args.limit)
    if args.check_rho_cap_6:
        check_rho_cap_6(args.limit)
    if args.check_nine_eleven_6:
        check_nine_eleven_6(args.limit)
    if args.check_block8_first:
        check_block8_first(args.limit)
    if args.check_block8_mod17:
        check_block8_mod17(args.limit)
    if args.check_block8_k11_mod256:
        check_block8_k11_mod256(args.limit)
    if args.check_block8_k11_mod512:
        check_block8_k11_mod512(args.limit)
    if args.check_block8_k11_mod8192:
        check_block8_k11_mod8192(args.limit)
