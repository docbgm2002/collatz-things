# Claim ledger

This ledger is the authoritative index of mathematical claims in the
repository. If a note conflicts with this file, the note must be repaired
before its claim is used downstream.

| ID | Claim | Status | Source | Verification / dependency |
|---|---|---|---|---|
| BF1 | \(3(2^L-1)=\texttt{10}1^{L-2}\texttt{01}\) for \(L\ge2\) | Proved here | `Block_Fracture_Lemma.md` | `verify_block_fracture.py` |
| BF2 | In an isolated-block decomposition, positions \(k+2,\ldots,k+L-1\) of \(3n\) and \(3n+1\) are \(1\) | Proved here | `Block_Fracture_Lemma.md` | The guaranteed window may merge with neighbouring \(1\)-bits |
| BF3 | One odd-step sends \(M_L\) to \(\texttt{10}1^{L-1}\) | Proved here | `Block_Fracture_Lemma.md` | `verify_block_fracture.py` |
| RAIL1 | \(f(8y+1)=6y+1\), with strict descent for \(y\ge1\) | Proved here | `Mod8_Rail_Descent.md` | `verify_mod8_rails.py` |
| RAIL5 | \(f(8y+5)\le3y+2<8y+5\) | Proved here | `Mod8_Rail_Descent.md` | `verify_mod8_rails.py` |
| RAIL3 | The prescribed bridge \(8y+3\to12y+5\to9y+4\) is exact | Proved here | `Mod8_Rail_Descent.md` | It is a fixed-division bridge, not always two applications of \(f\) |
| RAIL7 | \(f^2(8y+7)=18y+17\), with stay depth \(\lfloor v_2(y+1)/2\rfloor\) | Proved here | `Mod8_Rail_Descent.md`, `collatz_rail7_new_results.md` | `verify_mod8_rails.py` |
| FIN1 | Every odd \(x\le10^6\) descends below itself within at most 111 odd-steps | Finite certificate | `Mod8_Rail_Descent.md` | `verify_mod8_rails.py` |
| RNG1 | No potential \(\log_2x+g(\tau(x))\) is globally nonincreasing for every odd \(x>1\) | Proved here | `recharge_nogo.md` | `verify_recharge_nogo.py` checks identities and the explicit contradiction |
| MER1 | The Mersenne burn is \(f^{(j)}(M_n)=3^j2^{n-j}-1\) through its closed-form phase | Proved here | `recharge_nogo.md` | `verify_recharge_nogo.py` |
| MER2 | \(f^{(n)}(M_n)=(3^n-1)/2^{v_2(3^n-1)}\) | Proved here | `mersenne_repunit_reduction.md` | `verify_repunit_reduction.py` |
| REP5-1 | For odd \(n\), \(a_n\equiv1\bmod8\) when \(n\equiv1\bmod4\), and \(a_n\equiv5\bmod8\) when \(n\equiv3\bmod4\) | Proved here | `repunit_rail5_exact.md` | `verify_repunit_rail5.py` |
| REP5-2 | For odd \(n\), \(f(a_n)=a_{n+1}/2^{2+v_2((n+1)/2)}\); for \(n\equiv1\bmod4\) this is the base-\(9\) repunit \(b_{(n+1)/2}\) | Proved here | `repunit_rail5_exact.md` | LTE; `verify_repunit_rail5.py` |
| REP5-3 | For odd \(m\), the stated \(v_2(3b_m+1)\) classification by \(m\bmod16\) holds, including \(v_2=3\) on \(m\equiv13\bmod16\) and \(v_2\ge4\) on \(m\equiv5\bmod16\) | Proved here | `repunit_rail5_exact.md` | Complete modulo-\(128\) calculation; `verify_repunit_rail5.py` |
| REP5-4 | Among odd indices \(n\), the natural density reaching rail \(5\) at step \(0\) or \(1\) is exactly \(5/8\) | Proved here | `repunit_rail5_exact.md` | Union of five odd residue classes modulo \(16\); not a lower bound for every finite prefix |
| REP5-5 | Every odd-indexed repunit with \(3\le n\le199\) reaches rail \(5\) within at most \(12\) odd-steps | Finite certificate | `repunit_rail5_exact.md` | `verify_repunit_rail5.py`; worst cases \(n=17,61\) |
| REP5-6 | For odd \(m,\ell\), \(v_2(b_m-b_\ell)=v_2(m-\ell)\), so the base-\(9\) repunit map permutes odd classes modulo every \(2^q\) | Proved here | `repunit_rail5_density.md` | LTE; `verify_repunit_rail5_density.py` |
| REP5-7 | The density of odd indices whose repunit avoids rail \(5\) through step \(K\) is exactly \(\frac12(3/4)^K\) | Proved here | `repunit_rail5_density.md` | REP5-6 plus exact valuation-pattern density; `verify_repunit_rail5_density.py` |
| REP5-8 | Almost every odd-indexed repunit eventually reaches rail \(5\); the first-hit density is \(1/2\) at step \(0\) and \(\frac18(3/4)^{k-1}\) at step \(k\ge1\) | Proved here | `repunit_rail5_density.md` | Corollary of REP5-7; does not imply every index hits |
| DEN1 | Almost every odd integer has finite stopping time, with the explicit bound stated in the note | Known theorem rederived | `stopping_time_density.md` | Terras/Everett; verifier checks finite instances of the ingredients |
| POT1 | The decayed-bit potential decreases on the explicit recharge family under the stated parameter bound | Proved here | `Exponential_Decay_Potential.md` | Proof uses a uniform ratio and fuel bound |
| POT2 | Epoch-potential descent for odd \(x\le10^6\) under \(c=r=0.2\) | Finite certificate | `Exponential_Decay_Potential.md` | `verify_exponential_potential.py` |
| CYC1 | A \(K\)-odd-step cycle satisfies \(x(2^{E_K}-3^K)=c_K\) | Proved here | `cycle_reduction.md` | `verify_cycle_reduction.py` checks the identity |
| CYC2 | The bounded valuation-pattern search implemented for \(K\le8\) finds only \(x=1\) | Finite certificate | `cycle_reduction.md` | Not exhaustive over unbounded \(E_K\) |
| CYC3 | Minima of nontrivial cycles have natural density zero | Conditional corollary | `cycle_reduction.md` | Depends on DEN1; does not imply the same for every cycle element |
| CYC4 | No nontrivial positive cycle has an element \(\le10^6\) | Finite certificate | `cycle_reduction.md` | Any such cycle would have a minimum \(\le10^6\), contradicting FIN1 |
| TREE1 | The all-ones residue anchors every tested descent-tree depth and has minimal initial valuations | Proved burn + finite tree certificate | `descent_tree_survivors.md` | `verify_tree_survivors.py` |
| TREE2 | Tree-survivor density is universally bounded by \(\rho^K\) | Conjecture / proof gap | `descent_tree_survivors.md` | Current argument conflates bit depth with odd-step count |
| PAR1 | Two trajectories with nonzero offset cannot follow the same parity-rule sequence indefinitely | Proved here | `Collatz_Parity_Fragility_Corrected.md` | Does not imply non-merging, repulsion, or absence of basins |

## Exploratory documents

These notes are not dependencies of the proved-results track:

- `fuse_map_theory.md`
- `fuse_burn_attack.md`
- `repunit_tail_attack.md`
- `repunit_bad_automaton_notes.md`
- `repunit_normal_form_notes.md`
- all `explore_*.py` programs

## Archived documents

Superseded heuristics, legacy summaries, and their bounded artifacts are
listed in `archive/README.md`. They are retained for provenance and are not
dependencies of maintained claims.

## Admission rule

A claim may be promoted to **Proved here** only when its quantifiers and domain
are explicit, the human proof covers all cases, its dependencies are already
proved, and any verifier tests the same statement without silently replacing a
universal quantifier by a finite range.
