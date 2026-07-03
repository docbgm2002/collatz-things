#!/usr/bin/env python3
"""
Exploration: the Mersenne spine epoch.  Looking for structure that could turn
Conjecture G (epoch(2^n-1) = O(n)) into a proof. Research tool, not a proof.
"""

def v2(n):
    return (n & -n).bit_length() - 1 if n else 10 ** 9

def tau(x):
    return v2(x + 1)

def f(x):
    t = 3 * x + 1
    return t >> v2(t)


def repunit_hunch():
    print("== Mersenne -> base-3 repunit a_n=(3^n-1)/2 in exactly n odd-steps? ==")
    for n in range(3, 16):
        x = 2 ** n - 1
        for _ in range(n):
            x = f(x)
        a_n = (3 ** n - 1) // 2
        parity = "odd " if n % 2 else "even"
        print(f"  n={n:2d} ({parity}): f^{n}(2^n-1)={x}  a_n={a_n}  match={x == a_n}")


def epoch_decomposition():
    print("\n== Full epoch (odd-steps until value < x_0 = 2^n-1), decomposed ==")
    print(f"  {'n':>3} {'epoch':>6} {'eps/n':>6} {'->a_n':>6} {'post':>5} "
          f"{'maxtau_post':>11} {'spikes':>6} {'pk/x0=(3/2)^(n-1)?':>18}")
    for n in range(5, 81, 2):
        x0 = 2 ** n - 1
        a_n = (3 ** n - 1) // 2
        x = x0
        steps = 0
        reached = None
        maxtau_post = 0
        spikes = 0
        peak = x0
        prev_t = tau(x)
        while x >= x0:
            x = f(x)
            steps += 1
            peak = max(peak, x)
            if reached is None and x == a_n:
                reached = steps
            if reached is not None:
                t = tau(x)
                maxtau_post = max(maxtau_post, t)
                if t >= 4 and t > prev_t + 2:
                    spikes += 1
            prev_t = tau(x)
            if steps > 60 * n:
                steps = -1
                break
        post = steps - (reached or 0) if steps > 0 else -1
        # peak should be x_{n-1} = 2*3^(n-1)-1
        pk_ok = (peak == 2 * 3 ** (n - 1) - 1)
        print(f"  {n:3d} {steps:6d} {steps/n:6.2f} {str(reached):>6} {post:5d} "
              f"{maxtau_post:11d} {spikes:6d} {str(pk_ok):>18}")


def post_repunit_profile(n):
    """Look at the descent AFTER reaching a_n: residues mod 8, v2(3x+1), tau."""
    print(f"\n== Post-repunit descent profile for n={n} (from a_n down past x_0) ==")
    x0 = 2 ** n - 1
    a_n = (3 ** n - 1) // 2
    x = a_n
    rail_counts = {1: 0, 3: 0, 5: 0, 7: 0}
    vcounts = {}
    steps = 0
    while x >= x0:
        r = x % 8
        rail_counts[r] = rail_counts.get(r, 0) + 1
        vv = v2(3 * x + 1)
        vcounts[vv] = vcounts.get(vv, 0) + 1
        x = f(x)
        steps += 1
        if steps > 60 * n:
            break
    tot = sum(rail_counts.values())
    print(f"  steps a_n -> below x_0: {steps}")
    print(f"  rail histogram (mod 8): "
          + ", ".join(f"{r}:{rail_counts[r]}({100*rail_counts[r]/tot:.0f}%)"
                      for r in (1, 3, 5, 7)))
    print(f"  v2(3x+1) histogram: "
          + ", ".join(f"{k}:{vcounts[k]}" for k in sorted(vcounts)))
    exp_v = sum(k * c for k, c in vcounts.items()) / tot
    print(f"  mean v2(3x+1) = {exp_v:.3f} (random-model expectation = 2.000)")


if __name__ == "__main__":
    repunit_hunch()
    epoch_decomposition()
    for n in (51, 75):
        post_repunit_profile(n)
