#!/usr/bin/env python3
"""
Explore the Entropy and Kolmogorov Complexity properties of the Collatz map.

This script tracks the "information balance" (resolved bits vs. value growth)
and computes the exact 2-adic residue classes of the exponent n modulo 2^(E_K-1)
along the trajectory of a_n = (3^n - 1) / 2.
"""

import argparse
import math
import sys


def v2(n):
    return (n & -n).bit_length() - 1 if n else 10**9


def log2_int(n):
    bits = n.bit_length()
    if bits <= 1022:
        return math.log2(n)
    shift = bits - 1022
    return shift + math.log2(n >> shift)


def discrete_log_base3(B, M):
    """Solve 3^A = B mod 2^M for M >= 3.
    B must be odd and congruent to 1 or 3 mod 8.
    Returns A mod 2^(M-2).
    """
    B = B % (2**M)
    if B % 8 not in (1, 3):
        return None
    
    A = 0
    if B % 4 == 3:
        A = 1
        # B = B * 3^-1 mod 2^M
        inv3 = pow(3, -1, 2**M)
        B = (B * inv3) % (2**M)
        
    y = 0
    cur_val = 1
    powers = []
    p = 9
    for j in range(M - 3):
        powers.append(p)
        p = (p * p) % (2**M)
        
    for j in range(M - 3):
        mod = 1 << (j + 4)
        if (cur_val % mod) != (B % mod):
            y |= (1 << j)
            cur_val = (cur_val * powers[j]) % (2**M)
            
    return 2 * y + A


def trace_entropy(n, max_steps=2000):
    start = (3**n - 1) // 2
    x = start
    E = 0
    A = -1
    
    print(f"\nTracing exponent n = {n} (a_n = {start})")
    print(f"{'Step i':>8} {'Val e_i':>8} {'Cum E_i':>8} {'x_i':>12} {'Log Ratio':>12} {'Entropy Bal':>12} {'Residue Class of n':>24}")
    print("-" * 90)
    
    for i in range(max_steps):
        val = 3 * x + 1
        e = v2(val)
        
        # Calculate before update
        log_ratio = log2_int(x) - log2_int(start)
        entropy_bal = E - log_ratio
        
        # Determine the residue class of n modulo 2^(E-1) if E >= 3
        res_str = "N/A"
        if E >= 3:
            modulus = 1 << (E - 1)
            target_B = -A % (1 << (E + 1))
            dl = discrete_log_base3(target_B, E + 1)
            if dl is not None:
                n_res = (dl - i) % modulus
                res_str = f"n = {n_res} mod {modulus}"
            else:
                res_str = "Error: B not in cyclic subgroup"
        
        # Output step details (truncating x_i representation for readability if large)
        x_str = str(x)
        if len(x_str) > 12:
            x_str = x_str[:5] + "..." + x_str[-4:]
            
        print(f"{i:8d} {e:8d} {E:8d} {x_str:>12} {log_ratio:12.6f} {entropy_bal:12.6f} {res_str:>24}")
        
        # Update state
        x = val >> e
        E += e
        A = (3 * A + (1 << (E - e + 1)))
        
        if x < (1 << n) - 1:
            # Reached descent
            log_ratio = log2_int(x) - log2_int(start)
            entropy_bal = E - log_ratio
            print("-" * 90)
            print(f"Descent reached at step {i+1}! Final x = {x} < 2^{n}-1")
            print(f"Final Entropy Balance: {entropy_bal:.6f}")
            return True
            
    print(f"Did not reach descent in {max_steps} steps.")
    return False


def main():
    parser = argparse.ArgumentParser(description="Explore Entropy Balance Track")
    parser.add_argument("--exponent", type=int, default=23, help="Odd exponent to trace")
    parser.add_argument("--steps", type=int, default=100, help="Max steps to trace")
    args = parser.parse_args()
    
    if args.exponent % 2 == 0:
        print("Exponent must be odd.")
        sys.exit(1)
        
    trace_entropy(args.exponent, args.steps)


if __name__ == "__main__":
    main()
