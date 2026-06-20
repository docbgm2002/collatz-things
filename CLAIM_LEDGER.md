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
| REPAFF1 | The relative affine correction satisfies \(1+q_K=\prod_{i<K}(1+1/(3x_i))\) | Proved here | `repunit_affine_tail_bound.md` | Exact recurrence; `verify_repunit_affine_tail.py` |
| REPAFF2 | Before descent below \(T=2^n-1\), \(\log_2(1+q_K)\le K\log_2(1+1/(3T))<K/(3T\ln2)\) | Proved here | `repunit_affine_tail_bound.md` | Makes the affine allowance exponentially small in linear windows |
| REPAFF3 | Raw surplus above the REPAFF2 bound implies descent below the Mersenne target by time \(K\) | Proved here | `repunit_affine_tail_bound.md` | Exact affine-safe surplus criterion |
| REPMRG1 | Equality of repunit diagonal states \((n+i,E_i,A_i)\) forces exact trajectory merging | Proved here | `repunit_tail_merge_reduction.md` | Direct from the exact normal form |
| REPMRG1B | Two states on one diagonal coalesce on the next step iff \(3A+2^{E+1}=3B+2^{F+1}\) | Proved here | `repunit_tail_merge_reduction.md` | Exact successor-state criterion |
| REPMRG2 | A tail merging into a smaller exponent's pre-descent tail inherits finite descent | Proved here | `repunit_tail_merge_reduction.md` | Strong-induction reduction |
| REPMRG3 | For odd \(7\le n\le10001\), 4783 tails merge into smaller tails before descent, 215 are primitive, and all observed merges are same-diagonal | Finite certificate | `repunit_tail_merge_reduction.md` | `verify_repunit_tail_merges.py` |
| GAPMRG1 | Every first same-diagonal merger lies on an even collision shell: if predecessor cumulative valuations differ by \(2h\), their corrections differ by \(2^{u+1}(2^{2h}-1)/3\), and their outgoing valuations differ by \(2h\) | Proved here | `repunit_gap_merger_analysis.md` | Algebraic consequence of \(3A+2^{E+1}=3B+2^{F+1}\) |
| GAPMRG2 | If \(n\equiv31\bmod64\), then \(x_2(n)=x_4(n-2)\) | Proved here | `repunit_gap_merger_analysis.md` | Exact prefixes \((6)\) and \((2,1,1)\); `verify_repunit_gap_mergers.py` |
| GAPMRG2B | If \(n\equiv79\bmod128\), \(199\bmod256\), \(323\bmod512\), or \(1289\bmod4096\), then \(x_3(n)=x_5(n-2)\) | Proved here | `repunit_gap_merger_analysis.md` | Four exact smallest-shell prefix pairs; the fourth is hidden by source-selection order in the first-merger table |
| GAPMRG3 | If \(n\equiv2047\bmod4096\), then \(x_2(n)=x_6(n-4)\) | Proved here | `repunit_gap_merger_analysis.md` | Exact prefixes \((12)\) and \((3,1,2,3,1)\); `verify_repunit_gap_mergers.py` |
| GAPMRG4 | Through odd \(n\le10001\), the shell \(|E-F|=2\) accounts for 4527 of 4783 mergers and 2735 of 2858 mergers with exponent gap \(2,4,\) or \(6\) | Finite certificate | `repunit_gap_merger_analysis.md` | `verify_repunit_gap_mergers.py`; proportions \(94.65\%\) and \(95.70\%\) |
| GAPMRG5 | The 17 level-\(4\) gap-\(2\) cylinders listed in `repunit_gap2_sync_tree.md` each force \(x_4(n)=x_6(n-2)\) as a first synchronization | Proved here + depth-bounded classification | `repunit_gap2_sync_tree.md` | Symbolic valuation-word enumeration through cumulative depth 24; all 17 lie on \(|E-F|=2\) |
| GAPMRG6 | At modulus \(2^{24}\), the resolved gap-\(2\) first-hit cylinders through levels \(2,\ldots,7\) cover 1,012,093 of 8,388,608 odd classes | Finite symbolic certificate | `repunit_gap2_sync_tree.md` | `explore_repunit_sync_tree.py`; \(12.0651\%\), with deeper unresolved cylinders omitted |
| GAPMRG7 | At modulus \(2^{20}\), with levels \(2,\ldots,7\) and cumulative valuations at most \(20\), the gap-\(2,4,6\) synchronization-tree union covers 66,441 of 524,288 odd classes | Finite symbolic certificate | `repunit_multigap_sync_union.md` | `verify_repunit_sync_union.py`; \(12.672615\%\), versus \(12.023926\%\) for gap \(2\) alone |
| COLDEF1 | For aligned states, the normalized correction difference obeys \(\delta'=\delta+e-f\) and \(z'=(3z+2^\alpha-2^\beta)/2^{\min(\alpha+e,\beta+f)}\) | Proved here | `repunit_collision_defect_dynamics.md` | Exact normal-form recurrence; next-step merger iff the numerator is zero |
| COLDEF2 | The compressed state \((d,E,F,\delta,z)\) does not determine the outgoing valuation pair, even on repunit tails | Proved by counterexample | `repunit_collision_defect_dynamics.md` | At diagonal 3320 two states with \(E=F=128,\delta=0,z=-6\) have outgoing pairs \((1,2)\) and \((3,1)\); `verify_repunit_collision_defect.py` |
| REP256-1 | If every active 256-valuation block has weight at least \(425\), then every odd-indexed repunit tail descends, with primitive activity bounded by \(256\lceil n/32\rceil\) | Conditional result | `repunit_256_block_target.md` | Uses REPAFF1-3 and REPMRG1-2 |
| REP256-2 | For odd \(7\le n\le10001\), all \(1{,}712{,}672\) active 256-blocks have weight at least \(425\) | Finite certificate | `repunit_256_block_target.md` | `verify_repunit_256_block.py`; unique minimum at \(n=2449\), step \(306\) |
| REPLOW1 | For every \(K\), an explicit odd exponent class modulo \(2^{K+1}\) has initial valuation word \((2,1^{K-1})\) | Proved here | `repunit_low_prefix_obstruction.md` | Exact valuation class plus discrete logarithm; `verify_repunit_low_prefix.py` |
| REPLOW2 | Such a low-prefix tail does not descend during its first \(K\) steps and cannot share an equal full diagonal state \((d,E,A)\) with a smaller odd exponent | Proved here | `repunit_low_prefix_obstruction.md` | Growth bound and cumulative-valuation contradiction |
| BAKER1 | If the repunit tail of \(a_n\) begins with \((2,1^{K-1})\), then \(v_2(3^{n+1}+7)\ge K+3\) | Proved here | `repunit_baker_nonshadowing.md` | Equivalent reformulation of REPLOW1 at the enemy branch |
| BAKER2 | Under the same hypothesis, \(K\le C_7\log(n+1)\) for an effective constant \(C_7\) | Known theorem applied | `repunit_baker_nonshadowing.md` | Fixed-\(d=7\) consequence of Yu's \(p\)-adic logarithmic-form bounds; no numerical global constant is derived here |
| BAKER3 | More generally, a prefix \((2,1^{g(n)-1})\) is eventually impossible when \(g(n)/\log(n+1)\to\infty\); in particular for \(g(n)=3n\) | Known theorem applied | `repunit_baker_nonshadowing.md` | Corollary of BAKER2 |
| BAKERC1 | The enemy coordinate \((m_K,d_K)\) is invariant across every valuation-one extension | Proved here | `repunit_baker_applicability_census.md` | If \(e_K=1\), then \(R_{K+1}=3R_K\), \(r_{K+1}=r_K+1\), and \(m_{K+1}=m_K\) |
| BAKERC2 | Through odd \(n\le5001\), the 165 primitive tails contain 342,694 active prefix states; among the 341,551 with \(K\ge8\), only 46 have reduced-height ratio at most \(0.75\) | Finite certificate | `repunit_baker_applicability_census.md` | `explore_baker_applicability.py --limit 5001`; 9 ratios in \((0.25,0.50]\), 37 in \((0.50,0.75]\) |
| REPEP1 | A valuation-one run of length \(L\), together with its terminal valuation \(q>1\), has raw surplus \(L+q-(L+1)\log_2 3\) | Proved here | `repunit_enemy_episode_analysis.md` | Exact sum of the episode valuations |
| REPEP2 | Through odd \(n\le10001\), only 92,195 of 219,847 Case B episodes with \(L\ge1\) either repair their deficit at the terminal payout or exit to a prior primitive enemy coordinate | Finite certificate / candidate refuted | `repunit_enemy_episode_analysis.md` | `explore_repunit_enemy_episodes.py --limit 10001 --min-run 1`; coverage \(41.94\%\) |
| REPEP3 | In the same finite domain, the longest Case B local recovery is 129 steps; no recovery bound depending only linearly on the one-run length is supported | Finite certificate | `repunit_enemy_episode_analysis.md` | Maximum recovery/(episode length) is \(64.5\); eventual recovery by first descent is logically automatic |
| REPLOW3 | The low-prefix classes are nested truncations of the unique odd \(\alpha\in\mathbb Z_2\) satisfying \(3^{\alpha+1}=-7\), and can extend beyond any prescribed finite recovery horizon | Proved here | `repunit_low_prefix_obstruction.md` | Closed form \(v_2(3^{n+1}+7)\ge K+3\); `verify_repunit_low_prefix.py` |
| REPLOW4 | A positive exponent realising \((2,1^{K-1})\) satisfies \(K<\log_2(3)(n+1)-2\), so this 2-adic branch cannot shadow for \(3n\) steps | Proved here | `repunit_low_prefix_obstruction.md` | Divisibility plus ordinary size bound |
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

- `RESEARCH_ROADMAP.md`
- `fuse_map_theory.md`
- `fuse_burn_attack.md`
- `repunit_tail_attack.md`
- `repunit_diagonal_survivor_notes.md`
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
