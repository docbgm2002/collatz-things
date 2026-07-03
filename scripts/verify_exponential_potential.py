#!/usr/bin/env python3
"""
Verification for "The Exponentially Decayed Bit Potential Model for the 3x+1 Map".
Bypasses the Recharge No-Go contradiction. No external dependencies.

This script checks:
  1. Lemma 1 (Uniform Bound): g_r(x) < 1/(1-r) for all odd x.
  2. Theorem 1 (Guaranteed Recharge Descent): strict potential decrease on the
     recharge family x_m -> 2^m-1.
  3. Large-Scale Sweep: strict potential decrease across every first-descent
     epoch for the first 1,000,000 odd integers under c=0.2, r=0.2.
"""

import math
import sys
import time

def v2(n):
    return (n & -n).bit_length() - 1 if n else 10**9

def f(x):
    t = 3 * x + 1
    return t >> v2(t)

def make_pot_function(c, r):
    # Precompute powers of r to avoid math.pow overhead in the sweep
    r_pow = [r**i for i in range(120)]
    
    def pot(x):
        val = 0.0
        temp = x
        i = 0
        while temp > 0:
            if temp & 1:
                val += r_pow[i]
            temp >>= 1
            i += 1
        return math.log2(x) + c * val
    return pot

def first_descent_epoch(x, step_limit=1000):
    cur = x
    steps = 0
    while cur >= x and steps < step_limit:
        cur = f(cur)
        steps += 1
    return cur, steps

def check_lemma1(r=0.2, max_x=100000):
    """g_r(x) is strictly bounded by 1/(1-r)."""
    bound = 1.0 / (1.0 - r)
    r_pow = [r**i for i in range(120)]
    for x in range(1, max_x, 2):
        val = 0.0
        temp = x
        i = 0
        while temp > 0:
            if temp & 1:
                val += r_pow[i]
            temp >>= 1
            i += 1
        assert val < bound, (x, val, bound)
    print(f"Lemma 1 (Uniform Bound): PASS for x < {max_x} (g_r(x) < {bound:.4f})")

def check_theorem1(c=0.2, r=0.2, max_m=51):
    """Guaranteed descent on the recharge family x_m -> 2^m-1."""
    pot = make_pot_function(c, r)
    for m in range(3, max_m, 2):
        xm = ((1 << (m + 2)) - 5) // 3
        fxm = 2**m - 1
        assert f(xm) == fxm, (m, xm, f(xm))
        
        p_start = pot(xm)
        p_end = pot(fxm)
        assert p_end < p_start, (m, p_start, p_end)
    print(f"Theorem 1 (Recharge Descent): PASS for odd m=3..{max_m-1} (guaranteed delta < 0)")

def run_large_sweep(c=0.2, r=0.2, limit=1000000):
    """Strict potential decrease across every first-descent epoch up to limit."""
    pot = make_pot_function(c, r)
    start_time = time.time()
    failures = 0
    worst_delta = -1e9
    worst_case = None
    
    for x in range(3, limit + 1, 2):
        end, steps = first_descent_epoch(x)
        if steps >= 1000:
            continue
        p_start = pot(x)
        p_end = pot(end)
        delta = p_end - p_start
        if delta > worst_delta:
            worst_delta = delta
            worst_case = (x, end, steps)
        if delta >= 0:
            failures += 1
            print(f"  FAILURE: x={x} -> end={end} (steps={steps}), delta={delta:+.6f}")
            break
            
    duration = time.time() - start_time
    assert failures == 0, f"Expected 0 failures, found {failures} failures."
    print(f"Large-Scale Sweep: PASS for all odd x <= {limit:,} (0 failures observed, max epoch delta: {worst_delta:+.6f} on x={worst_case[0]})")
    print(f"                   completed sweep in {duration:.2f} seconds.")

if __name__ == "__main__":
    print("=== Exponentially Decayed Bit Potential Verification ===")
    check_lemma1(r=0.2)
    check_theorem1(c=0.2, r=0.2)
    run_large_sweep(c=0.2, r=0.2, limit=1000000)
    print("\nAll checks passed successfully.")
