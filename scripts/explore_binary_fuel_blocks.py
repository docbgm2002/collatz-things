#!/usr/bin/env python3
"""
Explore binary-fuel block gates for the accelerated odd Collatz map.

This is an exploratory diagnostic, not a proof. It collapses a trailing-one
burn plus the terminal payout into a block (t, a, r):

    x = 2^t u - 1
    a = v2(3^t u - 1)
    x_next = (3^t u - 1) / 2^a = 2^r u_next - 1

A block is "bad" when a - t*log2(3/2) < 0.
"""

from __future__ import annotations

import argparse
import math
from fractions import Fraction


ALPHA = math.log2(3 / 2)


def v2(n: int) -> int:
    return (n & -n).bit_length() - 1 if n else 10**9


def block_from_integer(x: int) -> tuple[int, int, int, int, float]:
    """Return (t, a, r, y, surplus) for a positive odd representative."""
    t = v2(x + 1)
    u = (x + 1) >> t
    value = pow(3, t) * u - 1
    a = v2(value)
    y = value >> a
    r = v2(y + 1)
    return t, a, r, y, a - ALPHA * t


def resolved_edge(x: int, modulus_bits: int):
    """
    Classify the low-bit state x modulo 2^M.

    Returns:
      ("bad", y, t, a, r, surplus)
      ("good", y, t, a, r, surplus)
      ("amb", ...)

    Ambiguous means the available low bits do not determine the block safely.
    """
    modulus = 1 << modulus_bits
    xp1 = (x + 1) % modulus
    if xp1 == 0:
        return ("amb",)

    t = v2(xp1)
    if t + 4 >= modulus_bits:
        return ("amb", t)

    # Use the least nonnegative representative. If enough low bits are
    # available, the valuations and next residue are independent of the
    # unknown higher bits.
    u = (x + 1) >> t
    value = pow(3, t) * u - 1
    a = v2(value)
    y = value >> a

    yp1 = (y + 1) % modulus
    if yp1 == 0:
        return ("amb", t, a)

    r = v2(yp1)
    if t + a + r + 3 >= modulus_bits:
        return ("amb", t, a, r)

    surplus = a - ALPHA * t
    kind = "bad" if surplus < 0 else "good"
    return (kind, y % modulus, t, a, r, surplus)


def find_bad_cycles(bad_next: dict[int, int]) -> list[list[int]]:
    color: dict[int, int] = {}
    cycles: list[list[int]] = []

    def visit(x: int, stack: dict[int, int]) -> None:
        color[x] = 1
        stack[x] = len(stack)
        y = bad_next.get(x)
        if y in bad_next:
            if color.get(y) == 1:
                keys = list(stack.keys())
                cycles.append(keys[stack[y] :])
            elif color.get(y) != 2:
                visit(y, stack)
        color[x] = 2
        stack.pop(x, None)

    for x in list(bad_next):
        if color.get(x, 0) == 0:
            visit(x, {})
    return cycles


def longest_bad_path(bad_next: dict[int, int], labels: dict[int, tuple[int, int, int]]):
    cycles = find_bad_cycles(bad_next)
    if cycles:
        return cycles, 0, None, []

    memo: dict[int, int] = {}

    def depth(x: int) -> int:
        if x not in bad_next:
            return 0
        if x in memo:
            return memo[x]
        memo[x] = 1 + depth(bad_next[x])
        return memo[x]

    best_depth, best_state = max(((depth(x), x) for x in bad_next), default=(0, None))
    chain = []
    cur = best_state
    while cur is not None and cur in bad_next and len(chain) < best_depth:
        chain.append(labels[cur])
        cur = bad_next[cur]
    return cycles, best_depth, best_state, chain


def scan_moduli(start: int, stop: int) -> None:
    print("== Resolved bad-block suffix graph ==")
    print("bad means a - t*log2(3/2) < 0; ambiguous states need more bits.")
    for modulus_bits in range(start, stop + 1, 2):
        counts = {"bad": 0, "good": 0, "amb": 0}
        bad_next: dict[int, int] = {}
        labels: dict[int, tuple[int, int, int]] = {}

        for x in range(1, 1 << modulus_bits, 2):
            edge = resolved_edge(x, modulus_bits)
            counts[edge[0]] += 1
            if edge[0] == "bad":
                _, y, t, a, r, _ = edge
                bad_next[x] = y
                labels[x] = (t, a, r)

        cycles, depth, state, chain = longest_bad_path(bad_next, labels)
        bad_fraction = counts["bad"] / (1 << (modulus_bits - 1))
        print(
            f"M={modulus_bits:2d} "
            f"bad={counts['bad']:7d} good={counts['good']:7d} "
            f"amb={counts['amb']:5d} bad_frac={bad_fraction:.6f} "
            f"cycles={len(cycles):2d} max_depth={depth:2d}"
        )
        if chain:
            print(f"  longest prefix: {chain[:12]}")
        if cycles:
            first = cycles[0]
            print(f"  first projected cycle length={len(first)} state={first[0]}")
            print(f"  labels: {[labels[x] for x in first[:12]]}")


def show_fixed_bad_block(t: int, a: int) -> None:
    """Show the real sign of the repeated block with r=t."""
    numerator = 1 - (1 << a)
    denominator = pow(3, t) - (1 << (a + t))
    print("== Repeated block fixed point ==")
    print(f"block: (t,a,r)=({t},{a},{t})")
    print(f"u = ({numerator}) / ({denominator})")
    if denominator == 0:
        print("degenerate denominator")
        return
    sign = "positive" if numerator * denominator > 0 else "negative"
    print(f"real sign of u: {sign}")
    print(f"surplus: {a - ALPHA * t:.12f}")


def scan_repeated_bad_blocks(max_t: int) -> None:
    """List repeated single-block ghosts with negative surplus."""
    print(f"== Repeated single-block bad ghosts through t={max_t} ==")
    print("A repeated block has r=t. Bad surplus forces a negative real fixed point.")
    for t in range(2, max_t + 1):
        entries = []
        for a in range(1, math.floor(ALPHA * t) + 1):
            numerator = 1 - (1 << a)
            denominator = pow(3, t) - (1 << (a + t))
            if denominator <= 0:
                continue
            # x = 2^t*u - 1 with u = numerator / denominator.
            entries.append((a, a - ALPHA * t, numerator, denominator))
        if entries:
            compact = ", ".join(
                f"a={a} surplus={surplus:.3f} u={num}/{den}"
                for a, surplus, num, den in entries
            )
            print(f"t={t:2d}: {compact}")


def least_positive_start_for_chain(chain: list[tuple[int, int, int]]) -> tuple[int, int, int]:
    """
    Return (x0, u0, uN) for the least positive odd terminal uN realizing chain.

    Backward block equation:
        u_i = (2^(a+r) u_{i+1} - 2^a + 1) / 3^t.

    After composition:
        u_0 = (A*u_N + B) / 3^T.
    """
    a_coeff = 1
    b_coeff = 0
    denom = 1
    for t, a, r in reversed(chain):
        shift = 1 << (a + r)
        c = 1 - (1 << a)
        a_coeff = shift * a_coeff
        b_coeff = shift * b_coeff + c * denom
        denom *= 3**t

    residue = (-b_coeff * pow(a_coeff, -1, denom)) % denom
    candidates = []
    for k in range(4):
        u_terminal = residue + k * denom
        if u_terminal > 0 and u_terminal % 2 == 1:
            candidates.append(u_terminal)
    u_terminal = min(candidates)
    u0 = (a_coeff * u_terminal + b_coeff) // denom
    t0 = chain[0][0]
    x0 = (1 << t0) * u0 - 1
    return x0, u0, u_terminal


def trace_records(limit: int) -> None:
    """Find records for initial consecutive bad-block chains."""
    records = []
    best = 0
    for x0 in range(1, limit + 1, 2):
        x = x0
        bad_len = 0
        for _ in range(1000):
            t, a, r, y, surplus = block_from_integer(x)
            if surplus >= 0:
                break
            bad_len += 1
            x = y
        if bad_len > best:
            best = bad_len
            records.append((x0, bad_len))

    print(f"== Initial consecutive bad-block records up to {limit} ==")
    for x0, bad_len in records:
        x = x0
        chain = []
        for _ in range(bad_len):
            t, a, r, y, _ = block_from_integer(x)
            chain.append((t, a, r))
            x = y
        recovered, u0, u_terminal = least_positive_start_for_chain(chain)
        marker = "ok" if recovered == x0 else f"recovered={recovered}"
        print(
            f"{x0:9d} bad_len={bad_len:2d} bits={x0.bit_length():2d} "
            f"{marker} u0={u0} uN={u_terminal} chain={chain}"
        )


def scan_mersenne_spikes(max_r: int) -> None:
    """
    Scan the exact spike family (2,1,R) with R == 5 mod 6.

    For these R, the least positive start maps directly to 2^R-1.
    We measure when cumulative block surplus first becomes nonnegative and
    when the block orbit first descends below the spike start.
    """
    print(f"== Mersenne-spike recovery scan through R={max_r} ==")
    print("family: x0 = 4*(2^(R+1)-1)/9 - 1, R == 5 mod 6")
    worst = (0, None)
    exceptions = []
    for fuel in range(5, max_r + 1, 6):
        x0 = 4 * ((1 << (fuel + 1)) - 1) // 9 - 1
        x = x0
        cumulative = 0.0
        recover = None
        descend = None
        for block_index in range(1, 20000):
            t, a, r, y, surplus = block_from_integer(x)
            cumulative += surplus
            x = y
            if recover is None and cumulative >= 0:
                recover = block_index
            if descend is None and x < x0:
                descend = block_index
            if recover is not None or descend is not None:
                break
        if recover != descend:
            exceptions.append((fuel, recover, descend, cumulative))
        if recover is not None and recover > worst[0]:
            worst = (recover, fuel)
        if fuel <= 35 or fuel % 30 == 5:
            print(
                f"R={fuel:3d} bits={x0.bit_length():3d} "
                f"recover={recover} descend={descend} final_surplus={cumulative:.3f}"
            )
    print(f"exceptions={len(exceptions)} worst_recover={worst[0]} at R={worst[1]}")


def bad_payouts(t: int) -> list[int]:
    return [a for a in range(1, math.floor(ALPHA * t) + 1)]


def beam_search_bad_chains(length: int, width: int, max_fuel: int) -> None:
    """
    Search bad-block chain space using the exact backward constructor.

    This is heuristic because the beam keeps only the `width` smallest starts
    at each length and caps fuel values by `max_fuel`.
    """
    beam: list[tuple[int, list[tuple[int, int, int]]]] = []
    for t in range(2, max_fuel + 1):
        for a in bad_payouts(t):
            for r in range(1, max_fuel + 1):
                chain = [(t, a, r)]
                x0, _, _ = least_positive_start_for_chain(chain)
                beam.append((x0, chain))
    beam = sorted(beam, key=lambda item: item[0])[:width]

    print(
        f"== Beam search for bad-block chains "
        f"(length={length}, width={width}, max_fuel={max_fuel}) =="
    )
    for current_len in range(1, length + 1):
        print(f"L={current_len:2d}")
        for x0, chain in beam[:5]:
            print(f"  {x0:12d} bits={x0.bit_length():2d} chain={chain}")
        if current_len == length:
            break

        next_beam: list[tuple[int, list[tuple[int, int, int]]]] = []
        for _, chain in beam:
            t = chain[-1][2]
            for a in bad_payouts(t):
                for r in range(1, max_fuel + 1):
                    extended = chain + [(t, a, r)]
                    x0, _, _ = least_positive_start_for_chain(extended)
                    next_beam.append((x0, extended))
        beam = sorted(next_beam, key=lambda item: item[0])[:width]


def inspect_chain(chain_text: str) -> None:
    """Inspect a semicolon-separated chain such as '2,1,3;3,1,2'."""
    chain = []
    for part in chain_text.split(";"):
        if not part.strip():
            continue
        t, a, r = (int(piece.strip()) for piece in part.split(","))
        chain.append((t, a, r))
    if not chain:
        return

    affine_a = Fraction(1)
    affine_b = Fraction(0)
    total_steps = 0
    total_valuation = 0
    for t, a, r in chain:
        step_a = Fraction(3**t, 2 ** (a + r))
        step_b = Fraction((1 << a) - 1, 2 ** (a + r))
        affine_a = step_a * affine_a
        affine_b = step_a * affine_b + step_b
        total_steps += t
        total_valuation += t + a

    print("== Chain affine inspection ==")
    print(f"chain={chain}")
    print(f"u_N = ({affine_a}) * u_0 + ({affine_b})")
    if affine_a != 1:
        fixed_u = affine_b / (1 - affine_a)
        print(f"fixed u_0 = {fixed_u} ({'positive' if fixed_u > 0 else 'negative'})")
    surplus = total_valuation - total_steps * math.log2(3)
    print(f"odd_steps={total_steps} valuation={total_valuation} surplus={surplus:.12f}")

    x0, u0, u_terminal = least_positive_start_for_chain(chain)
    print(f"least positive start x0={x0} u0={u0} terminal_u={u_terminal}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=8, help="first modulus bit depth")
    parser.add_argument("--stop", type=int, default=20, help="last modulus bit depth")
    parser.add_argument("--records", type=int, default=2_000_000, help="record scan limit")
    parser.add_argument("--skip-records", action="store_true")
    parser.add_argument("--ghosts", type=int, default=16, help="max t for repeated bad ghosts")
    parser.add_argument("--beam-length", type=int, default=0, help="run bad-chain beam search")
    parser.add_argument("--beam-width", type=int, default=500)
    parser.add_argument("--beam-max-fuel", type=int, default=9)
    parser.add_argument("--spike-max-r", type=int, default=0)
    parser.add_argument(
        "--inspect-chain",
        default="",
        help="semicolon-separated triples, e.g. '2,1,3;3,1,2'",
    )
    args = parser.parse_args()

    scan_moduli(args.start, args.stop)
    print()
    show_fixed_bad_block(4, 1)
    print()
    scan_repeated_bad_blocks(args.ghosts)
    if not args.skip_records:
        print()
        trace_records(args.records)
    if args.beam_length:
        print()
        beam_search_bad_chains(args.beam_length, args.beam_width, args.beam_max_fuel)
    if args.inspect_chain:
        print()
        inspect_chain(args.inspect_chain)
    if args.spike_max_r:
        print()
        scan_mersenne_spikes(args.spike_max_r)


if __name__ == "__main__":
    main()
