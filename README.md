# Collatz Parity-Fragility Theorem  
**Instability of Near-Loops and Hypothetical Cycles in the 3n+1 Problem**  
First published: 28 November 2025  
Author: Some Bloke Down the Pub (who happens to know docbgm, but is better than him at maths)

### One-sentence summary
Any two Collatz trajectories that start a small distance apart (difference δ ≠ 0) must diverge in finitely many steps, even if they initially follow the exact same sequence of odd and even steps.

### What this repository proves (rigorously and elementarily)

- If the initial difference δ is odd → the trajectories diverge at the very first step (opposite parity → different rule applied).
- If the initial difference δ is even, write δ = 2ᵏ·d with d odd. Then every halving step (/2) reduces the exponent k by 1, while every odd step (3x+1) multiplies the difference by 3 (preserving the 2-adic valuation). After exactly k halving steps the difference becomes odd, and the previous case instantly kills synchronization.
- Therefore any non-zero perturbation destroys a shared operation sequence in finite time.

### Consequences

- All observed “near-loops” (returning to n ± 1, ±2, ±3, ±4 after many steps) are fragile: a second lap immediately diverges.
- Any exact non-trivial cycle (if one existed) would be repelling: no nearby starting value can shadow it forever.
- The Collatz map has no stable or quasi-stable periodic/near-periodic orbits except the trivial 1→4→2→1 cycle.

### Files

- `Collatz_Parity_Fragility_Corrected.md` – full write-up with definitions, lemmas, and proofs.
- `README.md` – this file.

### Important disclaimer
This proves instability of cycles and near-cycles, not their non-existence. Ruling out exact non-trivial cycles still requires diophantine analysis of the cycle equation (separate open problem).

### Citation (if you ever want to reference it informally)
Some Bloke Down the Pub, “Collatz Parity-Fragility and Near-Loop Instability”, GitHub repository, 28 November 2025.  
https://github.com/docbgm2002/collatz-parity-fragility

