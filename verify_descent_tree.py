#!/usr/bin/env python3
"""
verify_descent_tree.py
Exploratory residue-class descent search for the shortcut Collatz map.
Uses a hybrid branching residue-class tree algorithm with conservative checks.

A residue marked PROVEN is discharged by this script's sufficient affine
inequalities. A FAILED residue means unresolved branches remain at the selected
depth; it is not a counterexample.
"""
import sys

def v2(n):
    return (n & -n).bit_length() - 1 if n else 10 ** 9

def collatz_concrete_descends(n):
    """Verify if a concrete integer n eventually descends below itself."""
    if n <= 1:
        return True
    cur = n
    # Apply standard shortcut Collatz map
    steps = 0
    while cur >= n:
        t = 3 * cur + 1
        cur = t >> v2(t)
        steps += 1
        if steps > 1000:
            return False
    return True

class ResidueBranch:
    def __init__(self, a, b, a_start, b_start, history=""):
        self.a = a
        self.b = b
        self.a_start = a_start
        self.b_start = b_start
        self.history = history

    def is_descended(self):
        # Strict descent for all z >= 0
        if self.a < self.a_start and self.b < self.b_start:
            return True
        # Descent for all z >= 1, and manual check for z = 0
        if self.a < self.a_start and self.b == self.b_start:
            return collatz_concrete_descends(self.b_start)
        return False

def prove_residue_descent(r, K, max_depth=25, verbose=False):
    """
    Try to discharge all integers of the form 2^K * y + r (for y >= 0)
    by branching on residue refinements until a sufficient descent inequality
    applies.
    """
    # Start with the initial state
    root = ResidueBranch(a=2**K, b=r, a_start=2**K, b_start=r, history=f"x = 2^{K}y + {r}")
    queue = [root]
    
    depth = 0
    while queue and depth < max_depth:
        next_queue = []
        for node in queue:
            if node.is_descended():
                continue
            
            p = v2(node.a)
            
            # If the coefficient a is odd, the parameter z MUST be even
            # for the value x_t = a z + b to be odd.
            # So we deterministically substitute z = 2w.
            if p == 0:
                odd_node = ResidueBranch(
                    a=2 * node.a, b=node.b,
                    a_start=2 * node.a_start, b_start=node.b_start,
                    history=node.history + " [z=2w (forced odd)]"
                )
                next_queue.append(odd_node)
                continue
            
            q = v2(3 * node.b + 1)
            v = min(p, q)
            
            # Try instant conservative step check
            new_a = (3 * node.a) >> v
            new_b = (3 * node.b + 1) >> v
            cons_node = ResidueBranch(
                a=new_a, b=new_b,
                a_start=node.a_start, b_start=node.b_start,
                history=node.history + f" -> (3x+1)/2^{v} (cons)"
            )
            
            if cons_node.is_descended():
                # Conservative step is enough to prove descent!
                continue
                
            # If conservative step is not enough to prove descent,
            # we check if we have an exact valuation (p > q) or need branching (p <= q)
            if p > q:
                # Exact valuation, no branching possible
                next_queue.append(cons_node)
            else:
                # Branching could unlock a larger division
                # Case 2.1: z = 2w
                branch1 = ResidueBranch(
                    a=2 * node.a, b=node.b,
                    a_start=2 * node.a_start, b_start=node.b_start,
                    history=node.history + " [z=2w]"
                )
                # Case 2.2: z = 2w + 1
                branch2 = ResidueBranch(
                    a=2 * node.a, b=node.a + node.b,
                    a_start=2 * node.a_start, b_start=node.a_start + node.b_start,
                    history=node.history + " [z=2w+1]"
                )
                
                for b in [branch1, branch2]:
                    if not b.is_descended():
                        next_queue.append(b)
        
        queue = next_queue
        depth += 1
        
    if not queue:
        return True, depth
    else:
        if verbose:
            print(f"    Failed branches at depth {depth}:")
            for i, node in enumerate(queue[:5]):
                print(f"      Branch {i+1}: current={node.a}z + {node.b}, start={node.a_start}z + {node.b_start}")
                print(f"        History: {node.history}")
            if len(queue) > 5:
                print(f"      ... and {len(queue) - 5} more branches.")
        return False, len(queue)

def main():
    print("=== Collatz Automated Descent Prover ===")
    
    # Let's test residues mod 8
    print("\nProving residues mod 8:")
    for r in [1, 3, 5, 7]:
        success, info = prove_residue_descent(r, 3, max_depth=25, verbose=True)
        if success:
            print(f"  Residue 8y + {r}: PROVEN (max depth: {info})")
        else:
            print(f"  Residue 8y + {r}: FAILED (remaining active branches: {info})")

    # Let's see if we can prove all odd residues mod 16
    print("\nProving residues mod 16:")
    for r in range(1, 16, 2):
        success, info = prove_residue_descent(r, 4, max_depth=25)
        if success:
            print(f"  Residue 16y + {r}: PROVEN (max depth: {info})")
        else:
            print(f"  Residue 16y + {r}: FAILED")
            
    # Let's see if we can prove all odd residues mod 32
    print("\nProving residues mod 32:")
    for r in range(1, 32, 2):
        success, info = prove_residue_descent(r, 5, max_depth=25)
        if success:
            print(f"  Residue 32y + {r}: PROVEN (max depth: {info})")
        else:
            print(f"  Residue 32y + {r}: FAILED")

if __name__ == "__main__":
    main()
