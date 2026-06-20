#!/usr/bin/env python3
"""Census Baker-applicable enemy constants on active primitive tails.

For every primitive repunit tail and every prefix before its first descent,
form

    R_K = A_K + 2^(E_K+1) = 3^r d,  3 not dividing d.

The induced enemy equation is

    v2(3^(n+K-r) + d) >= E_K + 2.

A fixed or unusually low-height d is a plausible Baker/Yu family. Generic
rows with bitlength(|d|) comparable to E_K are not.

All output is a finite diagnostic, not a theorem.
"""

import argparse
import csv
from collections import Counter, defaultdict

from explore_repunit_tail_merges import scan as scan_merges


def v2(value):
    return (value & -value).bit_length() - 1


def compact_pattern(values, width=12):
    if len(values) <= 2 * width:
        return ",".join(map(str, values))
    head = ",".join(map(str, values[:width]))
    tail = ",".join(map(str, values[-width:]))
    return f"{head},...,{tail}"


def compact_stored_pattern(row):
    head = row["pattern_head"]
    tail = row["pattern_tail"]
    length = row.get("K", row.get("end_K"))
    if length <= len(head):
        return ",".join(map(str, head[:length]))
    if length <= len(head) + len(tail):
        overlap = len(head) + len(tail) - length
        values = head + tail[overlap:]
        return ",".join(map(str, values))
    return (
        ",".join(map(str, head))
        + ",...,"
        + ",".join(map(str, tail))
    )


def compact_integer(value, decimal_digits=18):
    magnitude = abs(value)
    bits = magnitude.bit_length()
    if bits > 256:
        high = magnitude >> (bits - 32)
        low = magnitude & ((1 << 32) - 1)
        sign = "-" if value < 0 else ""
        return f"{sign}0x{high:08x}...{low:08x}({bits}b)"
    text = str(value)
    if len(text) <= decimal_digits:
        return text
    sign = "-" if value < 0 else ""
    digits = text.lstrip("-")
    return f"{sign}{digits[:8]}...{digits[-8:]}({bits}b)"


def primitive_rows(limit, factor):
    result = scan_merges(limit=limit, factor=factor)
    return sorted(result["primitives"], key=lambda row: row["n"])


def trace_active_enemy_rows(n, sigma):
    """Yield Baker-normalized rows for 1 <= K < sigma."""
    x = (3**n - 1) // 2
    E = 0
    A = -1
    pattern = []

    for K in range(1, sigma):
        value = 3 * x + 1
        e = v2(value)
        x = value >> e
        pattern.append(e)

        A = 3 * A + (1 << (E + 1))
        E += e

        R = A + (1 << (E + 1))
        modulus = 1 << (E + 2)
        assert (pow(3, n + K, modulus) + R) % modulus == 0
        assert R != 0

        r = 0
        d = R
        while d % 3 == 0:
            d //= 3
            r += 1

        height = abs(d).bit_length()
        yield {
            "n": n,
            "sigma": sigma,
            "K": K,
            "E": E,
            "r": r,
            "m": n + K - r,
            "d": d,
            "height": height,
            "height_ratio": height / E,
            "saving": E - height,
            "last_e": e,
            "pattern_head": tuple(pattern[:12]),
            "pattern_tail": tuple(pattern[-12:]),
        }


def census(limit, factor):
    primitives = primitive_rows(limit, factor)
    rows = []
    for primitive in primitives:
        rows.extend(trace_active_enemy_rows(primitive["n"], primitive["sigma"]))
    return primitives, rows


def fixed_constant_families(rows, min_k):
    grouped = defaultdict(list)
    for row in rows:
        if row["K"] >= min_k:
            grouped[row["d"]].append(row)

    families = []
    for d, members in grouped.items():
        exponents = {row["n"] for row in members}
        if len(members) < 2:
            continue
        families.append(
            {
                "d": d,
                "height": abs(d).bit_length(),
                "states": len(members),
                "exponents": len(exponents),
                "max_K": max(row["K"] for row in members),
                "max_E": max(row["E"] for row in members),
                "m_values": len({row["m"] for row in members}),
                "members": members,
            }
        )
    return sorted(
        families,
        key=lambda family: (
            family["exponents"],
            family["states"],
            family["max_K"],
            -family["height"],
        ),
        reverse=True,
    )


def persistent_runs(rows, min_k):
    by_n = defaultdict(list)
    for row in rows:
        by_n[row["n"]].append(row)

    runs = []
    for n, members in by_n.items():
        members.sort(key=lambda row: row["K"])
        start = 0
        while start < len(members):
            end = start + 1
            while (
                end < len(members)
                and members[end]["d"] == members[start]["d"]
                and members[end]["K"] == members[end - 1]["K"] + 1
            ):
                end += 1
            run = members[start:end]
            if run[-1]["K"] >= min_k and len(run) >= 2:
                runs.append(
                    {
                        "n": n,
                        "d": run[0]["d"],
                        "height": run[0]["height"],
                        "start_K": run[0]["K"],
                        "end_K": run[-1]["K"],
                        "length": len(run),
                        "end_E": run[-1]["E"],
                        "pattern_head": run[-1]["pattern_head"],
                        "pattern_tail": run[-1]["pattern_tail"],
                        "all_extension_vals_one": all(
                            row["last_e"] == 1 for row in run[1:]
                        ),
                    }
                )
            start = end

    return sorted(
        runs,
        key=lambda run: (run["length"], run["end_K"], -run["height"]),
        reverse=True,
    )


def low_height_rows(rows, min_k, max_height, max_ratio, min_saving):
    selected = [
        row
        for row in rows
        if row["K"] >= min_k
        and row["saving"] >= min_saving
        and (row["height"] <= max_height or row["height_ratio"] <= max_ratio)
    ]
    return sorted(
        selected,
        key=lambda row: (
            row["saving"],
            -row["height_ratio"],
            row["K"],
        ),
        reverse=True,
    )


def print_report(
    primitives,
    rows,
    limit,
    min_k,
    max_height,
    max_ratio,
    min_saving,
    top,
):
    print("== Baker applicability census ==")
    print(f"finite domain: odd 7 <= n <= {limit}")
    print(
        f"primitive tails={len(primitives)} "
        f"active prefix states={len(rows)} min_K={min_k}"
    )

    height_bands = Counter()
    for row in rows:
        if row["K"] < min_k:
            continue
        ratio = row["height_ratio"]
        if ratio <= 0.25:
            height_bands["<=0.25"] += 1
        elif ratio <= 0.50:
            height_bands["0.25..0.50"] += 1
        elif ratio <= 0.75:
            height_bands["0.50..0.75"] += 1
        elif ratio <= 1.00:
            height_bands["0.75..1.00"] += 1
        else:
            height_bands[">1.00"] += 1
    print(f"height-ratio bands: {dict(height_bands)}")

    families = fixed_constant_families(rows, min_k)
    print("\nRepeated exact reduced constants:")
    if not families:
        print("  none")
    for family in families[:top]:
        sample = max(family["members"], key=lambda row: row["K"])
        print(
            f"  d={compact_integer(family['d'])} h={family['height']} "
            f"states={family['states']} exponents={family['exponents']} "
            f"distinct_m={family['m_values']} "
            f"maxK={family['max_K']} maxE={family['max_E']} "
            f"sample_n={sample['n']}"
        )

    runs = persistent_runs(rows, min_k)
    print("\nLongest same-d runs on one active tail:")
    if not runs:
        print("  none")
    for run in runs[:top]:
        assert run["all_extension_vals_one"]
        print(
            f"  n={run['n']} d={compact_integer(run['d'])} "
            f"h={run['height']} "
            f"K={run['start_K']}..{run['end_K']} length={run['length']} "
            f"endE={run['end_E']} "
            f"prefix={compact_stored_pattern(run)}"
        )
    print(
        "  identity: every displayed persistence step has e_K=1, so "
        "R_(K+1)=3R_K and the reduced d is unchanged"
    )

    exceptional = low_height_rows(
        rows,
        min_k,
        max_height=max_height,
        max_ratio=max_ratio,
        min_saving=min_saving,
    )
    print(
        "\nLow-height rows "
        f"(saving>={min_saving} and "
        f"(h<={max_height} or h/E<={max_ratio:g})): {len(exceptional)}"
    )
    for row in exceptional[:top]:
        print(
            f"  n={row['n']} K={row['K']} E={row['E']} "
            f"d={compact_integer(row['d'])} "
            f"h={row['height']} h/E={row['height_ratio']:.4f} "
            f"saving={row['saving']} r={row['r']} m={row['m']} "
            f"prefix={compact_stored_pattern(row)}"
        )

    if exceptional:
        distinct_d = len({row["d"] for row in exceptional})
        distinct_n = len({row["n"] for row in exceptional})
        print(
            f"\nlow-height support: distinct d={distinct_d}, "
            f"distinct exponents={distinct_n}"
        )

    return families, runs, exceptional


def write_csv(path, rows):
    fields = [
        "n",
        "sigma",
        "K",
        "E",
        "r",
        "m",
        "d",
        "height",
        "height_ratio",
        "saving",
        "last_e",
        "pattern_head",
        "pattern_tail",
    ]
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            output = dict(row)
            output["pattern_head"] = ",".join(map(str, row["pattern_head"]))
            output["pattern_tail"] = ",".join(map(str, row["pattern_tail"]))
            writer.writerow({field: output[field] for field in fields})


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=2001)
    parser.add_argument("--factor", type=int, default=3)
    parser.add_argument("--min-k", type=int, default=8)
    parser.add_argument("--max-height", type=int, default=64)
    parser.add_argument("--max-ratio", type=float, default=0.5)
    parser.add_argument("--min-saving", type=int, default=4)
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument("--csv")
    return parser.parse_args()


def main():
    args = parse_args()
    primitives, rows = census(args.limit, args.factor)
    print_report(
        primitives,
        rows,
        args.limit,
        args.min_k,
        args.max_height,
        args.max_ratio,
        args.min_saving,
        args.top,
    )
    if args.csv:
        write_csv(args.csv, rows)
        print(f"\nwrote {args.csv}")


if __name__ == "__main__":
    main()
