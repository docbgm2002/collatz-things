#!/usr/bin/env python3
"""Verify the bounded multi-gap synchronization union certificate."""

from explore_repunit_sync_union import scan


def main():
    trees = scan(
        gaps=(2, 4, 6),
        through_step=7,
        max_total=20,
        common_depth=20,
    )

    expected = {
        2: {
            "levels": (16384, 14592, 11008, 8676, 6859, 5521),
            "union": 63040,
        },
        4: {
            "levels": (256, 689, 892, 1076, 1088, 852),
            "union": 4853,
        },
        6: {
            "levels": (16, 25, 61, 65, 51, 12),
            "union": 230,
        },
    }

    for gap, target in expected.items():
        levels = tuple(
            len(trees[gap]["levels"][step]["hits"])
            for step in range(2, 8)
        )
        assert levels == target["levels"]
        assert len(trees[gap]["union"]) == target["union"]

    gap2 = trees[2]["union"]
    gap4 = trees[4]["union"]
    gap6 = trees[6]["union"]
    assert len(gap2 & gap4) == 1609
    assert len(gap2 & gap6) == 53
    assert len(gap4 & gap6) == 35
    assert len(gap2 & gap4 & gap6) == 15
    assert len(gap2 | gap4 | gap6) == 66441

    print(
        "SYNCUNION: PASS "
        "(depth 20, steps 2..7, gaps 2/4/6, "
        "combined union 66441/524288)"
    )


if __name__ == "__main__":
    main()
