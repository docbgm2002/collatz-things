#!/usr/bin/env python3
"""
Verification script for the Entropy and Kolmogorov Complexity alternative track.
Checks:
- Theorem 1 (Conservation Identity): exact log-space relation.
- Discrete log congruence solver for exponent n.
- Theorem 2: strict monotonicity of Entropy Balance.
"""

import math
import random


THETA = math.log2(3)


def v2(n):
    return (n & -n).bit_length() - 1 if n else 10**9


def log2_int(n):
    bits = n.bit_length()
    if bits <= 1022:
        return math.log2(n)
    shift = bits - 1022
    return shift + math.log2(n >> shift)


def discrete_log_base3(B, M):
    B = B % (1 << M)
    if B % 8 not in (1, 3):
        return None
    
    A = 0
    if B % 4 == 3:
        A = 1
        inv3 = pow(3, -1, 1 << M)
        B = (B * inv3) % (1 << M)
        
    y = 0
    cur_val = 1
    powers = []
    p = 9
    for j in range(M - 3):
        powers.append(p)
        p = (p * p) % (1 << M)
        
    for j in range(M - 3):
        mod = 1 << (j + 4)
        if (cur_val % mod) != (B % mod):
            y |= (1 << j)
            cur_val = (cur_val * powers[j]) % (1 << M)
            
    return 2 * y + A


def verify_conservation_identity(num_samples=1000, max_K=15):
    """Verify that Theorem 1 holds for random odd integers."""
    print("Running verification of Theorem 1 (Conservation Identity)...")
    for _ in range(num_samples):
        x0 = random.randint(3, 100000) | 1
        x = x0
        E = 0
        q = 0.0
        
        # We trace K steps
        for K in range(1, max_K + 1):
            val = 3 * x + 1
            e = v2(val)
            
            # Update affine correction: 1+q_next = (1+q)*(1+1/3x)
            q = (1 + q) * (1 + 1 / (3 * x)) - 1
            
            x = val >> e
            E += e
            
            # Theorem 1: E_K + log2(x_K/x0) = K*log2(3) + log2(1+q_K)
            log_ratio = log2_int(x) - log2_int(x0)
            lhs = E + log_ratio
            rhs = K * THETA + math.log2(1 + q)
            
            error = abs(lhs - rhs)
            assert error < 1e-9, f"Conservation Identity failed for x0={x0}, K={K}. Error={error}"
            
    print("   PASS: Theorem 1 (Conservation Identity) holds to high precision.")


def verify_discrete_log_congruence(num_samples=100):
    """Verify that the discrete log computes the correct congruence for n."""
    print("Running verification of Discrete Log Exponent Solver...")
    for _ in range(num_samples):
        # Pick a random odd exponent n
        n = random.randint(7, 299) | 1
        start = (3**n - 1) // 2
        x = start
        E = 0
        A = -1
        
        for i in range(10):  # Test first 10 steps
            val = 3 * x + 1
            e = v2(val)
            
            # Check residue class mod 2^(E-1) if E >= 3
            if E >= 3:
                modulus = 1 << (E - 1)
                target_B = -A % (1 << (E + 1))
                dl = discrete_log_base3(target_B, E + 1)
                assert dl is not None, f"Discrete log returned None for n={n}, step {i}"
                n_res = (dl - i) % modulus
                assert n % modulus == n_res, f"Congruence mismatch: n={n}, expected {n_res} mod {modulus} (step {i})"
                
            x = val >> e
            E += e
            A = 3 * A + (1 << (E - e + 1))
            
    print("   PASS: Discrete Log correctly solves for residue class of n modulo 2^(E-1).")


def verify_entropy_monotonicity(num_samples=1000, max_K=30):
    """Verify the exact positive increment formula for Entropy Balance."""
    print("Running verification of Theorem 2 (Entropy Monotonicity)...")
    for _ in range(num_samples):
        x0 = random.randint(3, 100000) | 1
        x = x0
        E = 0
        q = 0.0
        
        last_bal = 0.0
        for K in range(1, max_K + 1):
            val = 3 * x + 1
            e = v2(val)
            
            # Calculate current balance before step
            log_ratio = log2_int(x) - log2_int(x0)
            bal = E - log_ratio
            
            if K > 1:
                assert bal > last_bal, f"Entropy balance decreased for x0={x0} at step {K}"
                
            last_bal = bal
            
            x = val >> e
            E += e
            
    print("   PASS: Theorem 2 (Entropy Balance Monotonicity) verified successfully.")


if __name__ == "__main__":
    print("== Entropy Track Verification Script ==\n")
    verify_conservation_identity()
    print()
    verify_discrete_log_congruence()
    print()
    verify_entropy_monotonicity()
    print("\nAll verifications completed successfully.")
