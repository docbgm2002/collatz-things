#!/usr/bin/env python3
"""
Verification for "Mod-8 Rail Descent for the 3x+1 Map".
All checks use exact integer arithmetic. No external dependencies.

Covers:
  Lemma 1   f(8y+1) = 6y+1 exactly; strict descent for y>=1
  Lemma 2   f(8y+5) <= 3y+2 < 8y+5
  Lemma 3   exact bridge 8y+3 -> 12y+5 -> 9y+4 (incl. negative y)
  Lemma 4   stay-in-7: f2(8y+7) == 7 (mod 8)  <=>  v2(y+1) >= 2
  Lemma 5   consecutive stays in rail 7 == floor(v2(y+1)/2);
            all-ones class 2^k-1 has unbounded v2(y+1)
  Section 5 finite-window: every odd x in [3,1e6] descends; report worst case
"""


def v2(n):
    return (n & -n).bit_length() - 1 if n else 10 ** 9


def f(x):
    """Odd-step map on odd x: (3x+1)/2^v2(3x+1)."""
    t = 3 * x + 1
    return t >> v2(t)


def f2(x):
    return f(f(x))


def check_lemma1(Y=300_000):
    img_bad = desc_bad = 0
    for y in range(Y):
        x = 8 * y + 1
        if f(x) != 6 * y + 1:
            img_bad += 1
        if x > 1 and not (f(x) < x):
            desc_bad += 1
    assert img_bad == 0 and desc_bad == 0
    print(f"Lemma 1: PASS  f(8y+1)=6y+1 exact; strict descent y>=1  (y<{Y})")


def check_lemma2(Y=300_000):
    bad = 0
    for y in range(Y):
        x = 8 * y + 5
        if not (f(x) <= 3 * y + 2 and f(x) < x):
            bad += 1
    assert bad == 0
    print(f"Lemma 2: PASS  f(8y+5)<=3y+2<8y+5  (y<{Y})")


def check_lemma3(lo=-100_000, hi=300_000):
    bad = 0
    for y in range(lo, hi):
        x = 8 * y + 3
        a = 3 * x + 1                      # 24y+10
        if a != 24 * y + 10 or a % 2:
            bad += 1
        s1 = a // 2                        # 12y+5
        if s1 != 12 * y + 5:
            bad += 1
        b = 3 * s1 + 1                     # 36y+16
        if b != 36 * y + 16 or b % 4:
            bad += 1
        if b // 4 != 9 * y + 4:            # 9y+4
            bad += 1
    assert bad == 0
    print(f"Lemma 3: PASS  bridge 8y+3->12y+5->9y+4 exact  (y in [{lo},{hi}))")


def check_lemma4_5(Y=500_000):
    stay_bad = cap_bad = 0
    for y in range(Y):
        x = 8 * y + 7
        # Lemma 4
        if (f2(x) % 8 == 7) != (v2(y + 1) >= 2):
            stay_bad += 1
        # Lemma 5 (skip exact all-ones, treated separately)
        if x != (1 << x.bit_length()) - 1:
            cnt, cur = 0, x
            while cur % 8 == 7:
                nxt = f2(cur)
                if nxt % 8 == 7:
                    cnt += 1
                    cur = nxt
                else:
                    break
                if cnt > 500:
                    break
            if cnt != v2(y + 1) // 2:
                cap_bad += 1
    assert stay_bad == 0 and cap_bad == 0
    print(f"Lemma 4-5: PASS  stay<=>v2(y+1)>=2; cap=floor(v2(y+1)/2)  (y<{Y})")
    # all-ones unboundedness
    vals = []
    for k in range(3, 24):
        x = 2 ** k - 1
        y = (x - 7) // 8
        vals.append(v2(y + 1))
    assert vals == sorted(vals) and vals[-1] >= vals[0] + 10
    print(f"           all-ones 2^k-1: v2(y+1)=k-3 grows without bound "
          f"(k=3..23 -> {vals[0]}..{vals[-1]})")


def check_section5(LIM=10 ** 6):
    worst_steps = worst_x = fails = 0
    for x in range(3, LIM + 1, 2):
        cur, steps = f(x), 1
        while cur >= x:
            cur = f(cur)
            steps += 1
            if steps > 5000:
                fails += 1
                break
        if steps > worst_steps:
            worst_steps, worst_x = steps, x
    assert fails == 0
    print(f"Section 5: PASS  all odd x in [3,{LIM}] descend; "
          f"max {worst_steps} odd-steps at x={worst_x}; 0 failures")


if __name__ == "__main__":
    check_lemma1()
    check_lemma2()
    check_lemma3()
    check_lemma4_5()
    check_section5()
    print("\nAll checks passed.")
