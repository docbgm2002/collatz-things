#!/usr/bin/env python3
"""
Inspect repunit shortcut prefixes closest to the conjectural 5n-2 budget.

For odd n, start at a_n=(3^n-1)/2 and follow the shortcut map U until the
first value below T_n=2^n-1.  Every t-step prefix has the exact form

    U^t(a_n) = (3^rho a_n + c_t) / 2^t
             = (3^(n+rho) + D_t) / 2^(t+1),

where rho is the number of odd shortcut positions and D_t=2c_t-3^rho.
Factoring D_t=3^r d gives the exact enemy equation

    v2(3^(n+rho-r) + d) >= t+1.

The report ranks finite examples by closeness to the proposed tail budget
H(n)<=5n-2 and measures the reduced enemy height.  It is diagnostic only.
"""

import argparse
from collections import Counter, defaultdict


def v2(value):
    return (value & -value).bit_length() - 1 if value else 10**9


def compact_integer(value):
    bits = abs(value).bit_length()
    if bits <= 96:
        return str(value)
    magnitude = abs(value)
    high = magnitude >> (bits - 24)
    low = magnitude & ((1 << 24) - 1)
    sign = "-" if value < 0 else ""
    return f"{sign}0x{high:06x}...{low:06x}({bits}b)"


def shortcut(value):
    return value // 2 if value % 2 == 0 else (3 * value + 1) // 2


def enemy_coordinate(n, t, rho, c):
    D = 2 * c - pow(3, rho)
    assert D != 0
    r = 0
    d = D
    while d % 3 == 0:
        d //= 3
        r += 1
    m = n + rho - r
    modulus = 1 << (t + 1)
    assert (pow(3, m, modulus) + d) % modulus == 0
    return {
        "D": D,
        "r": r,
        "m": m,
        "d": d,
        "height": abs(d).bit_length(),
        "height_ratio": abs(d).bit_length() / (t + 1),
        "saving": (t + 1) - abs(d).bit_length(),
    }


def trace(n, repunit):
    target = (1 << n) - 1
    x = repunit
    t = 0
    rho = 0
    c = 0
    parity_head = []
    parity_tail = []
    last_survivor = None

    while x >= target:
        parity = x & 1
        if len(parity_head) < 24:
            parity_head.append(parity)
        parity_tail.append(parity)
        if len(parity_tail) > 24:
            parity_tail.pop(0)

        if parity:
            c = 3 * c + (1 << t)
            rho += 1
            x = (3 * x + 1) // 2
        else:
            x //= 2
        t += 1

        # Verify the affine and repunit normal forms at every step.
        assert (pow(3, rho) * repunit + c) == (x << t)
        D = 2 * c - pow(3, rho)
        assert pow(3, n + rho) + D == (x << (t + 1))

        if x >= target:
            last_survivor = (t, rho, c, x)

    H = t
    full_allowance = 5 * n - 2
    crossing = enemy_coordinate(n, t, rho, c)

    if last_survivor is None:
        survivor_enemy = None
        survivor_t = survivor_rho = survivor_x = 0
    else:
        survivor_t, survivor_rho, survivor_c, survivor_x = last_survivor
        survivor_enemy = enemy_coordinate(
            n, survivor_t, survivor_rho, survivor_c
        )

    return {
        "n": n,
        "H": H,
        "budget_slack": full_allowance - H,
        "crossing_rho": rho,
        "crossing_density": rho / H,
        "crossing_enemy": crossing,
        "survivor_t": survivor_t,
        "survivor_rho": survivor_rho,
        "survivor_density": (
            survivor_rho / survivor_t if survivor_t else 0.0
        ),
        "survivor_x": survivor_x,
        "survivor_enemy": survivor_enemy,
        "required_full_rho": 11 * n // 4 + 1,
        "parity_head": tuple(parity_head),
        "parity_tail": tuple(parity_tail),
    }


def scan(limit):
    rows = []
    repunit = (3**7 - 1) // 2
    for n in range(7, limit + 1, 2):
        if n > 7:
            repunit = 9 * repunit + 4
        rows.append(trace(n, repunit))
    return rows


def parity_text(row):
    head = "".join(map(str, row["parity_head"]))
    tail = "".join(map(str, row["parity_tail"]))
    if row["H"] <= 24:
        return head[: row["H"]]
    if row["H"] <= 48:
        overlap = 48 - row["H"]
        return head + tail[overlap:]
    return head + "..." + tail


def print_row(row):
    enemy = row["survivor_enemy"]
    print(
        f"  n={row['n']:5d} H={row['H']:6d} "
        f"slack={row['budget_slack']:6d} "
        f"last={row['survivor_t']:6d} "
        f"rho={row['survivor_rho']:6d} "
        f"odd={row['survivor_density']:.5f}"
    )
    if enemy is not None:
        print(
            f"    enemy: m={enemy['m']} d={compact_integer(enemy['d'])} "
            f"height={enemy['height']} h/(t+1)={enemy['height_ratio']:.5f} "
            f"saving={enemy['saving']}"
        )
    print(f"    parity={parity_text(row)}")


def report(rows, top):
    print("== High-odd-density repunit-prefix diagnostic ==")
    print(
        f"finite domain: odd {rows[0]['n']} <= n <= {rows[-1]['n']}; "
        "prefixes stop at first descent"
    )

    closest = sorted(
        rows,
        key=lambda row: (
            row["budget_slack"],
            -row["survivor_density"],
            row["n"],
        ),
    )
    print("\nClosest to the proposed H(n)<=5n-2 budget:")
    for row in closest[:top]:
        print_row(row)

    densest = sorted(
        rows,
        key=lambda row: (
            row["survivor_density"],
            row["survivor_t"],
        ),
        reverse=True,
    )
    print("\nHighest odd density at the last surviving prefix:")
    for row in densest[:top]:
        print_row(row)

    low_height = sorted(
        (row for row in rows if row["survivor_enemy"] is not None),
        key=lambda row: (
            row["survivor_enemy"]["height_ratio"],
            -row["survivor_enemy"]["saving"],
        ),
    )
    print("\nLowest reduced enemy-height ratios:")
    for row in low_height[:top]:
        print_row(row)

    repeated = defaultdict(list)
    repeated_full = defaultdict(list)
    for row in rows:
        enemy = row["survivor_enemy"]
        if enemy is not None:
            repeated[enemy["d"]].append(row)
            repeated_full[(enemy["m"], enemy["d"])].append(row)
    families = sorted(
        (
            (d, members)
            for d, members in repeated.items()
            if len(members) >= 2
        ),
        key=lambda item: (
            len(item[1]),
            max(row["survivor_t"] for row in item[1]),
        ),
        reverse=True,
    )
    print("\nRepeated reduced constants at last-survivor states:")
    if not families:
        print("  none")
    for d, members in families[:top]:
        print(
            f"  d={compact_integer(d)} states={len(members)} "
            f"exponents={[row['n'] for row in members[:12]]}"
        )

    full_families = sorted(
        (
            (coordinate, members)
            for coordinate, members in repeated_full.items()
            if len(members) >= 2
        ),
        key=lambda item: (
            len(item[1]),
            max(row["survivor_t"] for row in item[1]),
        ),
        reverse=True,
    )
    print("\nRepeated full enemy coordinates (m,d):")
    if not full_families:
        print("  none")
    for (m, d), members in full_families[:top]:
        states = [
            (
                row["n"],
                row["survivor_t"],
                row["survivor_rho"],
                row["survivor_enemy"]["r"],
            )
            for row in members[:12]
        ]
        print(
            f"  m={m} d={compact_integer(d)} states={len(members)} "
            f"(n,t,rho,r)={states}"
        )

    scaling_mergers = []
    for (m, d), members in full_families:
        by_r = defaultdict(list)
        for row in members:
            by_r[row["survivor_enemy"]["r"]].append(row)
        for r, same_r in by_r.items():
            if len(same_r) < 2:
                continue
            same_r.sort(key=lambda row: row["survivor_t"], reverse=True)
            base = same_r[0]
            for row in same_r[1:]:
                gap = base["survivor_t"] - row["survivor_t"]
                assert gap > 0
                assert row["survivor_x"] == (base["survivor_x"] << gap)
                cur = row["survivor_x"]
                for _ in range(gap):
                    assert cur % 2 == 0
                    cur = shortcut(cur)
                assert cur == base["survivor_x"]
                scaling_mergers.append((m, d, r, base, row, gap))

    print("\nExact power-of-two mergers from repeated (m,d,r):")
    if not scaling_mergers:
        print("  none")
    for m, d, r, base, row, gap in scaling_mergers[:top]:
        print(
            f"  n={row['n']} state --{gap} forced even steps--> "
            f"n={base['n']} state; m={m} r={r} "
            f"d={compact_integer(d)}"
        )
    print(f"  total verified scaling mergers: {len(scaling_mergers)}")

    slack_bands = Counter()
    for row in rows:
        slack = row["budget_slack"]
        if slack == 0:
            slack_bands["0"] += 1
        elif slack <= row["n"] // 4:
            slack_bands["<=n/4"] += 1
        elif slack <= row["n"] // 2:
            slack_bands["<=n/2"] += 1
        elif slack <= row["n"]:
            slack_bands["<=n"] += 1
        else:
            slack_bands[">n"] += 1
    print(f"\nBudget-slack bands: {dict(slack_bands)}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=2001)
    parser.add_argument("--top", type=int, default=12)
    args = parser.parse_args()
    rows = scan(args.limit)
    report(rows, args.top)


if __name__ == "__main__":
    main()
