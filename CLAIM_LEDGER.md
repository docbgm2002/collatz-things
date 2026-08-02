# Claim ledger

This ledger is the authoritative index of mathematical claims in the
repository. If a note conflicts with this file, the note must be repaired
before its claim is used downstream.

“Proved here” records the repository's internal proof status. It does not by
itself assert novelty. `BIBLIOGRAPHY_PASS.md` records the completed literature
review for the no-go programme; later, topic-specific attribution checks are
recorded in their source notes. Neither convention asserts that a comprehensive
literature review has been completed unless the cited record says so.

## Status and verification conventions

The status cell records the mathematical claim class; qualifiers after a
semicolon record provenance, subsumption, or review state. The principal
classes are **Proved here**, **Finite certificate**, **Conditional result**,
**Known theorem applied/rederived/translated**, **Proved by counterexample**,
and **Refuted**. Mixed rows must say which part has which class.

Verification artifacts have two roles:

- `verify_*.py` programs are maintained checks of identities or stated finite
  domains. They support, but do not replace, human proofs of universal claims.
- `explore_*.py` programs are bounded generators or diagnostics. They may
  generate an explicitly finite or mixed ledger row, or be cited as a
  cross-check on a universal row; they are never by themselves a proof of a
  universal claim.

Run `python scripts/verify_claim_ledger.py` to check table structure, unique
IDs, status classes, and referenced repository paths.

## Topic index

- **Core map and rails:** BF, RAIL, FIN, PAR.
- **Potential no-go and ancestry:** RNG, NLP, TWR, FFN, SH, SPN, BND, MER.
- **Repunit rails and geometry:** REP5, REP5G.
- **Repunit affine, merger, and collision machinery:** REPAFF, REPMRG,
  GAPMRG, COLDEF, REP256, REPLOW, RUNLEN, REPEXT.
- **Repunit ancestry and payout programme:** REPANC, GPA, NSF, PCD.
- **Integral escape frontier:** IEF.
- **Density, cycles, and survivor corridors:** DEN, CYC, TREE, COR.
- **Other bounded potentials and external-theorem applications:** POT, BAKER,
  BAKERC, REPEP.

| ID | Claim | Status | Source | Verification / dependency |
|---|---|---|---|---|
| BF1 | \(3(2^L-1)=\texttt{10}1^{L-2}\texttt{01}\) for \(L\ge2\) | Proved here | `docs/core/Block_Fracture_Lemma.md` | `scripts/verify_block_fracture.py` |
| BF2 | In an isolated-block decomposition, positions \(k+2,\ldots,k+L-1\) of \(3n\) and \(3n+1\) are \(1\) | Proved here | `docs/core/Block_Fracture_Lemma.md` | The guaranteed window may merge with neighbouring \(1\)-bits |
| BF3 | One odd-step sends \(M_L\) to \(\texttt{10}1^{L-1}\) | Proved here | `docs/core/Block_Fracture_Lemma.md` | `scripts/verify_block_fracture.py` |
| RAIL1 | \(f(8y+1)=6y+1\), with strict descent for \(y\ge1\) | Proved here | `docs/core/Mod8_Rail_Descent.md` | `scripts/verify_mod8_rails.py` |
| RAIL5 | \(f(8y+5)\le3y+2<8y+5\) | Proved here | `docs/core/Mod8_Rail_Descent.md` | `scripts/verify_mod8_rails.py` |
| RAIL3 | The prescribed bridge \(8y+3\to12y+5\to9y+4\) is exact | Proved here | `docs/core/Mod8_Rail_Descent.md` | It is a fixed-division bridge, not always two applications of \(f\) |
| RAIL7 | \(f^2(8y+7)=18y+17\), with stay depth \(\lfloor v_2(y+1)/2\rfloor\) | Proved here | `docs/core/Mod8_Rail_Descent.md`, `docs/core/collatz_rail7_new_results.md` | `scripts/verify_mod8_rails.py` |
| FIN1 | Every odd \(x\le10^6\) descends below itself within at most 111 odd-steps | Finite certificate | `docs/core/Mod8_Rail_Descent.md` | `scripts/verify_mod8_rails.py`; see also: W7 identifies \(B_X=64X/65\) as the binding IEF17 coordinate, so raising \(X\) tightens it linearly (`docs/repunit/ief17_genericity.md` §4) |
| RNG1 | No potential \(\log_2x+g(\tau(x))\) is globally nonincreasing for every odd \(x>1\) | Proved here | `docs/no-go/recharge_nogo.md` | `scripts/verify_recharge_nogo.py` checks identities and the explicit contradiction |
| NLP1 | No potential \(\log_2 x + g(x \bmod 2^m, \tau(x))\) is nonincreasing along \(f\), for any \(m\ge0\) and any \(g\) | Proved here; novelty review incomplete | `docs/no-go/no_local_potential.md` | `scripts/verify_no_local_potential.py`; generalizes RNG1 (the \(m=0\) case); depends on `docs/no-go/recharge_nogo.md` Lemmas 1–2 |
| NLP2 | No potential \(\log_2x+g(x\bmod2^m,\tau(x),\lambda_1(x))\) is nonincreasing, for any \(m\) and any \(g\) | Proved here; subsumed by SH1 | `docs/no-go/nlp2_alternation.md` | `scripts/verify_nlp2.py`; retained for its explicit level-2 price mechanism |
| TWR1 | For \(M\equiv1\pmod{2\cdot3^{d-1}}\), the exact ancestry tower \(w_d(M)\) satisfies \(f^d(w_d(M))=2^M-1\), with the stated periodic normal form and 2-adic separation | Proved here | `docs/no-go/tower_theorem.md` | `scripts/verify_tower.py`; see also: W2 shows \(w_d(M)=P_2^{\,d}(2^M-1)\) with \(P_2(z)=(4z-1)/3\), recovering the domain condition as \(3^d\mid z-1\) (`docs/no-go/certificate_semigroup.md` §3) |
| NLPD | No potential \(\log_2x+g(x\bmod2^m,\tau,(\lambda_i)_{i\in S})\) is nonincreasing for any finite detector set \(S\) | Proved here; subsumed by SH1 | `docs/no-go/tower_theorem.md` | `scripts/verify_tower.py`; supersedes the conditional formulation in `docs/no-go/nlp2_alternation.md` |
| FFN1 | No potential \(\log_2x+g(\tau(x),\mathrm{len}(x))\) is nonincreasing; likewise after adding \(x\bmod16\) | Proved here; subsumed by SH1 | `docs/no-go/fuel_fraction_nogo.md` | Explicit finite coordinate-cycle certificate; `scripts/verify_fuel_fraction.py` |
| SH1 | No potential \(\log_2x+g(x\bmod2^m,\tau,\mathrm{len},\lambda_1,\ldots,\lambda_d)\) is nonincreasing, for any \(m,d\) | Proved here; master local-coordinate no-go theorem | `docs/no-go/shadow_certificate.md` | Expanding \(-5\leftrightarrow-7\) shadow; `scripts/verify_shadow.py`; subsumes NLP1/NLP2/NLPD/FFN1 as impossibility statements; see also: the row is universal, but on **actual repunit orbits** the realised shadow depth is only \(\approx\log_2(\#\text{states})\) — 12 over 3464 states, 10 on \(n=471\) (`docs/no-go/machine_synthesis_surviving_class.md` §3) |
| SH2 | Adding any fixed number of leading binary digits does not permit such a nonincreasing potential | Proved here | `docs/no-go/leading_digit_nogo.md` | Iterated shadow plus Dirichlet approximation; `scripts/verify_leading_digit.py` |
| SPN1 | The tower-to-Mersenne-to-burn-to-repunit lane has the stated length, exact payout, and rail-1 location | Proved here | `docs/no-go/spine_synthesis.md` | Composition of TWR1, MER1, and MER2 plus exact additions; `scripts/verify_spine_synthesis.py` |
| BND1 | No potential \(\log_2x+G(x)\) with bounded \(G\) is nonincreasing | Proved here | `docs/no-go/spine_synthesis.md` | One-paragraph consequence of the Mersenne burn; arithmetic checked by `scripts/verify_spine_synthesis.py` |
| MER1 | The Mersenne burn is \(f^{(j)}(M_n)=3^j2^{n-j}-1\) through its closed-form phase | Proved here | `docs/no-go/recharge_nogo.md` | `scripts/verify_recharge_nogo.py` |
| MER2 | \(f^{(n)}(M_n)=(3^n-1)/2^{v_2(3^n-1)}\) | Proved here | `docs/repunit/mersenne_repunit_reduction.md` | `scripts/verify_repunit_reduction.py` |
| REP5-1 | For odd \(n\), \(a_n\equiv1\bmod8\) when \(n\equiv1\bmod4\), and \(a_n\equiv5\bmod8\) when \(n\equiv3\bmod4\) | Proved here | `docs/repunit/repunit_rail5_exact.md` | `scripts/verify_repunit_rail5.py` |
| REP5-2 | For odd \(n\), \(f(a_n)=a_{n+1}/2^{2+v_2((n+1)/2)}\); for \(n\equiv1\bmod4\) this is the base-\(9\) repunit \(b_{(n+1)/2}\) | Proved here | `docs/repunit/repunit_rail5_exact.md` | LTE; `scripts/verify_repunit_rail5.py` |
| REP5-3 | For odd \(m\), the stated \(v_2(3b_m+1)\) classification by \(m\bmod16\) holds, including \(v_2=3\) on \(m\equiv13\bmod16\) and \(v_2\ge4\) on \(m\equiv5\bmod16\) | Proved here | `docs/repunit/repunit_rail5_exact.md` | Complete modulo-\(128\) calculation; `scripts/verify_repunit_rail5.py` |
| REP5-4 | Among odd indices \(n\), the natural density reaching rail \(5\) at step \(0\) or \(1\) is exactly \(5/8\) | Proved here | `docs/repunit/repunit_rail5_exact.md` | Union of five odd residue classes modulo \(16\); not a lower bound for every finite prefix |
| REP5-5 | Every odd-indexed repunit with \(3\le n\le199\) reaches rail \(5\) within at most \(12\) odd-steps | Finite certificate | `docs/repunit/repunit_rail5_exact.md` | `scripts/verify_repunit_rail5.py`; worst cases \(n=17,61\) |
| REP5-6 | For odd \(m,\ell\), \(v_2(b_m-b_\ell)=v_2(m-\ell)\), so the base-\(9\) repunit map permutes odd classes modulo every \(2^q\) | Proved here | `docs/repunit/repunit_rail5_density.md` | LTE; `scripts/verify_repunit_rail5_density.py` |
| REP5-7 | The density of odd indices whose repunit avoids rail \(5\) through step \(K\) is exactly \(\frac12(3/4)^K\) | Proved here | `docs/repunit/repunit_rail5_density.md` | REP5-6 plus exact valuation-pattern density; `scripts/verify_repunit_rail5_density.py` |
| REP5-8 | Almost every odd-indexed repunit eventually reaches rail \(5\); the first-hit density is \(1/2\) at step \(0\) and \(\frac18(3/4)^{k-1}\) at step \(k\ge1\) | Proved here | `docs/repunit/repunit_rail5_density.md` | Corollary of REP5-7; does not imply every index hits |
| REP5G-1 | The infinite odd \(2\)-adic rail-\(5\) survivor set satisfies \(\mathcal S=\phi_1(\mathcal S)\dot\cup\phi_2(\mathcal S)\), where \(\phi_e(y)=(2^e y-1)/3\), and is conjugate to the full shift on \(\{1,2\}^{\mathbb N}\) | Proved here | `docs/repunit/repunit_rail5_survivor_geometry.md` | Exact inverse branches with contraction ratios \(1/2,1/4\); `scripts/verify_repunit_rail5_survivor_geometry.py` |
| REP5G-2 | The infinite rail-\(5\) survivor set has Haar measure zero | Proved here | `docs/repunit/repunit_rail5_survivor_geometry.md` | Level-\(K\) measure is exactly \((3/4)^K\) |
| REP5G-3 | The infinite rail-\(5\) survivor set has \(2\)-adic Hausdorff dimension \(\log_2((1+\sqrt5)/2)\) | Proved here | `docs/repunit/repunit_rail5_survivor_geometry.md` | Self-similar dimension equation \(2^{-s}+2^{-2s}=1\) |
| REP5G-4 | The corresponding \(2\)-adic repunit-index survivor set has Haar measure zero and the same Hausdorff dimension | Proved here | `docs/repunit/repunit_rail5_survivor_geometry.md` | Transfer by the base-\(9\) repunit isometry and \(n=2m-1\); positive integer membership beyond \(n=1\) remains open |
| REPAFF1 | The relative affine correction satisfies \(1+q_K=\prod_{i<K}(1+1/(3x_i))\) | Proved here | `docs/repunit/repunit_affine_tail_bound.md` | Exact recurrence; `scripts/verify_repunit_affine_tail.py` |
| REPAFF2 | Before descent below \(T=2^n-1\), \(\log_2(1+q_K)\le K\log_2(1+1/(3T))<K/(3T\ln2)\) | Proved here | `docs/repunit/repunit_affine_tail_bound.md` | Makes the affine allowance exponentially small in linear windows |
| REPAFF3 | Raw surplus above the REPAFF2 bound implies descent below the Mersenne target by time \(K\) | Proved here | `docs/repunit/repunit_affine_tail_bound.md` | Exact affine-safe surplus criterion |
| REPMRG1 | Equality of repunit diagonal states \((n+i,E_i,A_i)\) forces exact trajectory merging | Proved here | `docs/repunit/repunit_tail_merge_reduction.md` | Direct from the exact normal form |
| REPMRG1B | Two states on one diagonal coalesce on the next step iff \(3A+2^{E+1}=3B+2^{F+1}\) | Proved here | `docs/repunit/repunit_tail_merge_reduction.md` | Exact successor-state criterion |
| REPMRG2 | A tail merging into a smaller exponent's pre-descent tail inherits finite descent | Proved here | `docs/repunit/repunit_tail_merge_reduction.md` | Strong-induction reduction |
| REPMRG3 | For odd \(7\le n\le10001\), 4783 tails merge into smaller tails before descent, 215 are primitive, and all observed merges are same-diagonal | Finite certificate | `docs/repunit/repunit_tail_merge_reduction.md` | `scripts/verify_repunit_tail_merges.py` |
| GAPMRG1 | Every first same-diagonal merger lies on an even collision shell: if predecessor cumulative valuations differ by \(2h\), their corrections differ by \(2^{u+1}(2^{2h}-1)/3\), and their outgoing valuations differ by \(2h\) | Proved here | `docs/repunit/repunit_gap_merger_analysis.md` | Algebraic consequence of \(3A+2^{E+1}=3B+2^{F+1}\) |
| GAPMRG2 | If \(n\equiv31\bmod64\), then \(x_2(n)=x_4(n-2)\) | Proved here | `docs/repunit/repunit_gap_merger_analysis.md` | Exact prefixes \((6)\) and \((2,1,1)\); `scripts/verify_repunit_gap_mergers.py` |
| GAPMRG2B | If \(n\equiv79\bmod128\), \(199\bmod256\), \(323\bmod512\), or \(1289\bmod4096\), then \(x_3(n)=x_5(n-2)\) | Proved here | `docs/repunit/repunit_gap_merger_analysis.md` | Four exact smallest-shell prefix pairs; the fourth is hidden by source-selection order in the first-merger table |
| GAPMRG3 | If \(n\equiv2047\bmod4096\), then \(x_2(n)=x_6(n-4)\) | Proved here | `docs/repunit/repunit_gap_merger_analysis.md` | Exact prefixes \((12)\) and \((3,1,2,3,1)\); `scripts/verify_repunit_gap_mergers.py` |
| GAPMRG4 | Through odd \(n\le10001\), the shell \(\lvert E-F\rvert=2\) accounts for 4527 of 4783 mergers and 2735 of 2858 mergers with exponent gap \(2,4,\) or \(6\) | Finite certificate | `docs/repunit/repunit_gap_merger_analysis.md` | `scripts/verify_repunit_gap_mergers.py`; proportions \(94.65\%\) and \(95.70\%\) |
| GAPMRG5 | The 17 level-\(4\) gap-\(2\) cylinders listed in `docs/repunit/repunit_gap2_sync_tree.md` each force \(x_4(n)=x_6(n-2)\) as a first synchronization | Proved here + depth-bounded classification | `docs/repunit/repunit_gap2_sync_tree.md` | Symbolic valuation-word enumeration through cumulative depth 24; all 17 lie on \(\lvert E-F\rvert=2\) |
| GAPMRG6 | At modulus \(2^{24}\), the resolved gap-\(2\) first-hit cylinders through levels \(2,\ldots,7\) cover 1,012,093 of 8,388,608 odd classes | Finite symbolic certificate | `docs/repunit/repunit_gap2_sync_tree.md` | `scripts/explore_repunit_sync_tree.py`; \(12.0651\%\), with deeper unresolved cylinders omitted |
| GAPMRG7 | At modulus \(2^{20}\), with levels \(2,\ldots,7\) and cumulative valuations at most \(20\), the gap-\(2,4,6\) synchronization-tree union covers 66,441 of 524,288 odd classes | Finite symbolic certificate | `docs/repunit/repunit_multigap_sync_union.md` | `scripts/verify_repunit_sync_union.py`; \(12.672615\%\), versus \(12.023926\%\) for gap \(2\) alone |
| COLDEF1 | For aligned states, the normalized correction difference obeys \(\delta'=\delta+e-f\) and \(z'=(3z+2^\alpha-2^\beta)/2^{\min(\alpha+e,\beta+f)}\) | Proved here | `docs/repunit/repunit_collision_defect_dynamics.md` | Exact normal-form recurrence; next-step merger iff the numerator is zero |
| COLDEF2 | The compressed state \((d,E,F,\delta,z)\) does not determine the outgoing valuation pair, even on repunit tails | Proved by counterexample | `docs/repunit/repunit_collision_defect_dynamics.md` | At diagonal 3320 two states with \(E=F=128,\delta=0,z=-6\) have outgoing pairs \((1,2)\) and \((3,1)\); `scripts/verify_repunit_collision_defect.py` |
| REP256-1 | If every active 256-valuation block has weight at least \(425\), then every odd-indexed repunit tail descends, with primitive activity bounded by \(256\lceil n/32\rceil\) | Conditional result | `docs/repunit/repunit_256_block_target.md` | Uses REPAFF1-3 and REPMRG1-2 |
| REP256-2 | For odd \(7\le n\le10001\), all \(1{,}712{,}672\) active 256-blocks have weight at least \(425\) | Finite certificate | `docs/repunit/repunit_256_block_target.md` | `scripts/verify_repunit_256_block.py`; unique minimum at \(n=2449\), step \(306\) |
| REPLOW1 | For every \(K\), an explicit odd exponent class modulo \(2^{K+1}\) has initial valuation word \((2,1^{K-1})\) | Proved here | `docs/repunit/repunit_low_prefix_obstruction.md` | Exact valuation class plus discrete logarithm; `scripts/verify_repunit_low_prefix.py` |
| REPLOW2 | Such a low-prefix tail does not descend during its first \(K\) steps and cannot share an equal full diagonal state \((d,E,A)\) with a smaller odd exponent | Proved here | `docs/repunit/repunit_low_prefix_obstruction.md` | Growth bound and cumulative-valuation contradiction |
| BAKER1 | If the repunit tail of \(a_n\) begins with \((2,1^{K-1})\), then \(v_2(3^{n+1}+7)\ge K+3\) | Proved here | `docs/repunit/repunit_baker_nonshadowing.md` | Equivalent reformulation of REPLOW1 at the enemy branch |
| BAKER2 | Under the same hypothesis, \(K\le C_7\log(n+1)\) for an effective constant \(C_7\) | Known theorem applied | `docs/repunit/repunit_baker_nonshadowing.md` | Fixed-\(d=7\) consequence of Yu's \(p\)-adic logarithmic-form bounds; no numerical global constant is derived here; see also: W9 removes the transcendence input in finite range: \(v_2(3^m+7)=2+v_2(m-\alpha)\) with \(3^\alpha=-7\) in \(\mathbb Z_2\) (`docs/no-go/baker_explicit_constants_audit.md` §4) |
| BAKER3 | More generally, a prefix \((2,1^{g(n)-1})\) is eventually impossible when \(g(n)/\log(n+1)\to\infty\); in particular for \(g(n)=3n\) | Known theorem applied | `docs/repunit/repunit_baker_nonshadowing.md` | Corollary of BAKER2; see also: W9 §4.2 gives the exact envelope: max \(K=17\), attained only at \(n=1197\), through odd \(n\le50001\) |
| RUNLEN1 | On a repunit tail, \(\tau(x_K)=v_2(x_K+1)=v_2(3^{m_K}+d_K)-E_K-1\) at every step | Proved here | `docs/repunit/repunit_run_length_identity.md` | Fuel-enemy bridge; `scripts/verify_repunit_run_length.py` |
| RUNLEN2 | A maximal valuation-one run from step \(K_0\) has length exactly \(\tau(x_{K_0})-1=v_2(3^{m_{K_0}}+d_{K_0})-E_{K_0}-2\), with \((m,d)\) invariant in the run | Proved here | `docs/repunit/repunit_run_length_identity.md` | Trailing-one burn; `scripts/verify_repunit_run_length.py` |
| RUNLEN3 | The largest primitive record-deficit enemy constants \(d_K\) are high-height rough primes, so multi-term Baker via factorization cannot control them | Finite certificate | `docs/repunit/repunit_run_length_identity.md` | `scripts/explore_repunit_enemy_factorization.py`; smooth cases coincide with low height |
| BAKERC1 | The enemy coordinate \((m_K,d_K)\) is invariant across every valuation-one extension | Proved here | `docs/repunit/repunit_baker_applicability_census.md` | If \(e_K=1\), then \(R_{K+1}=3R_K\), \(r_{K+1}=r_K+1\), and \(m_{K+1}=m_K\) |
| BAKERC2 | Through odd \(n\le5001\), the 165 primitive tails contain 342,694 active prefix states; among the 341,551 with \(K\ge8\), only 46 have reduced-height ratio at most \(0.75\) | Finite certificate | `docs/repunit/repunit_baker_applicability_census.md` | `scripts/explore_baker_applicability.py --limit 5001`; 9 ratios in \((0.25,0.50]\), 37 in \((0.50,0.75]\) |
| REPEP1 | A valuation-one run of length \(L\), together with its terminal valuation \(q>1\), has raw surplus \(L+q-(L+1)\log_2 3\) | Proved here | `docs/repunit/repunit_enemy_episode_analysis.md` | Exact sum of the episode valuations |
| REPEP2 | Through odd \(n\le10001\), only 92,195 of 219,847 Case B episodes with \(L\ge1\) either repair their deficit at the terminal payout or exit to a prior primitive enemy coordinate | Finite certificate / candidate refuted | `docs/repunit/repunit_enemy_episode_analysis.md` | `scripts/explore_repunit_enemy_episodes.py --limit 10001 --min-run 1`; coverage \(41.94\%\) |
| REPEP3 | In the same finite domain, the longest Case B local recovery is 129 steps; no recovery bound depending only linearly on the one-run length is supported | Finite certificate | `docs/repunit/repunit_enemy_episode_analysis.md` | Maximum recovery/(episode length) is \(64.5\); eventual recovery by first descent is logically automatic |
| REPEXT1 | With \(R_K=A_K+2^{E_K+1}\) and \(Z_K=R_K/2^{E_K+1}\), one has \(Z_{K+1}=1+(3Z_K-2)/2^{e_K}\) | Proved here | `docs/repunit/repunit_extremal_principle.md` | Exact normal-form algebra; `scripts/verify_repunit_extremal_principle.py` |
| REPEXT2 | If \(D_{K+1}= (K+1)\log_2 3-E_{K+1}\) is a strict new record relative to \(D_0,\ldots,D_K\), then \(e_K=1\); moreover \(D_K-\log_2 Z_K\) is constant through each valuation-one run | Proved here | `docs/repunit/repunit_extremal_principle.md` | Since \(e_K\in\mathbb Z_{\ge1}\); `scripts/verify_repunit_extremal_principle.py` |
| REPEXT3 | The exact payout ledger is \(Z_K/2^{D_K}=\frac12+\sum_{j<K,e_j>1}(1-2^{1-e_j})2^{-D_{j+1}}\) | Proved here | `docs/repunit/repunit_extremal_principle.md` | Equivalent integer expansion for \(R_K\); `scripts/verify_repunit_extremal_principle.py` |
| REPEXT4 | Every payout correction is an exact combination of collision-shell displacements: \(P(E,q)=3S(E+1,q-1)\) for odd \(q\), and \(P(E,q)=3S(E,q)-S(E,2)\) for even \(q\) | Proved here | `docs/repunit/repunit_extremal_principle.md` | \(S(u,2h)=2^{u+1}(2^{2h}-1)/3\); `scripts/verify_repunit_extremal_principle.py` |
| REPEXT5 | A payout \(q\ge2\) selecting \(h=\lfloor q/2\rfloor\) gives the canonical odd partner \(Y=4^hX+(4^h-1)/3\) of its successor state \(X\), with \(f(Y)=f(X)\) and the exact shell-coordinate displacement | Proved here | `docs/repunit/repunit_extremal_principle.md` | Reachability of \(Y\) from a smaller repunit exponent is not implied; `scripts/verify_repunit_extremal_principle.py` |
| REPANC1 | For a realised \(q=2\) payout, a correction match \(C=A_i(\mathbf f)\) at an admissible aligned source length automatically realises \(\mathbf f\) on the smaller repunit exponent and forces a next-step merge | Proved here | `docs/repunit/primitive_ancestry_lemma.md` Section 9A | Exact-itinerary induction; `scripts/verify_repunit_ancestry_realization.py` |
| REPANC2 | Every REPANC1 correction match satisfies \(3^i-2^{i+1}\le3\cdot2^{u-j+1}(3^j-2^j)-3^{j+1}+2^{u+2}\), hence \(i<1+(u+\log_2(6(3/2)^j+4))/\log_2 3\) | Proved here | `docs/repunit/primitive_ancestry_lemma.md` Section 13 | Exact correction-layer bounds; checked on all matches in `scripts/verify_repunit_ancestry_realization.py` |
| REPANC3 | For a fixed realised high word, each admissible REPANC1 match produces the aligned merge for every sufficiently large exponent in its cylinder; nonmembership produces none and does not refine the exponent class | Proved here | `docs/repunit/primitive_ancestry_lemma.md` Section 9B | Consequence of REPANC1 and parity-itinerary uniqueness; cylinder lifts checked by `scripts/verify_repunit_ancestry_realization.py` |
| GPA1 | For every realised payout \(q\ge2\), equality of its canonical shell-partner correction with a source correction at an admissible aligned length automatically realises the complete smaller repunit valuation word and forces a next-step merge | Proved here | `docs/repunit/general_payout_ancestry.md` Section 2 | Exact-itinerary argument; `scripts/verify_repunit_general_payout_ancestry.py` |
| NSF1 | For every post-payout state \(X\) and shell height \(h\ge1\) with \(u_h=E+q-2h\ge0\), the odd partner \(Y_h=4^hX+(4^h-1)/3\) has correction \(C_h=A_{j+1}+2^{u_h+1}(4^h-1)/3\) and satisfies \(f(Y_h)=f(X)\) | Proved here | `docs/repunit/noncanonical_shell_fan.md` Sections 1--2 | Exact collision-shell algebra; `scripts/verify_noncanonical_shell_fan.py` |
| NSF2 | A noncanonical shell-fan correction match at any admissible aligned source length automatically realises the complete smaller repunit word and forces a next-step merge; the match is uniform across sufficiently large representatives of the high cylinder | Proved here | `docs/repunit/noncanonical_shell_fan.md` Section 3 | GPA1 exact-itinerary argument with arbitrary shell height; exhaustive small matches checked by `scripts/verify_noncanonical_shell_fan.py` |
| NSF3 | A shell-fan target satisfies \(C_h\equiv0\pmod3\) exactly when \(h\equiv1\pmod3\) for odd \(q\), or \(h\equiv2\pmod3\) for even \(q\); the other two height classes are not excluded modulo \(3\) | Proved here | `docs/repunit/noncanonical_shell_fan.md` Section 4 | Exact residue calculation; this does not establish a correction match; `scripts/verify_noncanonical_shell_fan.py` |
| NSF4 | On the highest dangerous exceptional PCD2 record for each tail through odd \(n\le5001\), 19 modulo-three-eligible fan targets occur; their survivor counts modulo \(3,\ldots,3^{10}\) are \(17,14,12,9,8,6,3,1,1,1\); only \((n,j,q,h,u,i)=(471,27,3,2,40,30)\) survives modulo \(3^{10}\), and its exact obstruction depth is \(13\) | Finite certificate | `docs/repunit/noncanonical_shell_fan.md` Section 7 | Exact reverse suffix recursion, checked on all small layers; `scripts/explore_noncanonical_shell_fan_records.py --limit 5001 --max-power 10 --exact-survivors` |
| GPA2 | If \(q\equiv3,4\pmod6\), the canonical shell-partner correction is divisible by \(3\), whereas every positive-length source correction is nonzero modulo \(3\); hence canonical shell reachability is impossible | Proved here | `docs/repunit/general_payout_ancestry.md` Section 3 | Exact residue argument; `scripts/verify_repunit_general_payout_ancestry.py` |
| PCD1 | Every payout ledger has the exact initial/eligible/blocked mass trichotomy; in the blocked branch, for every \(0<\eta<1\), either one blocked ancestor carries at least \(\eta\) of the blocked mass or the blocked effective count exceeds \(1/\eta\) | Proved here | `docs/repunit/payout_concentration_diffusion.md` Section 2 | Positivity, exact normalization, and the square-sum inequality |
| PCD2 | Through odd \(n\le5001\), the \(110\) primitive record prefixes with \(D_K\ge2\) split \(88/0/16/6\) across the ordered eligible, initial, blocked-concentrated, and blocked-diffuse branches; all six diffuse records lie on \(n=471\) | Finite certificate | `docs/repunit/payout_concentration_diffusion.md` Section 3 | Exact integer branch comparisons; `scripts/explore_payout_concentration.py --limit 5001 --top 0` |
| PCD3 | Two consecutive \(q=3\) canonical shells satisfy \(S(E+4,2)-3S(E+1,2)=S(E+1,4)\) | Proved here | `docs/repunit/payout_concentration_diffusion.md` Section 5 | Direct shell algebra; `scripts/verify_repunit_general_payout_ancestry.py` |
| PCD4 | The six short valuation blocks listed in the payout-concentration note give exact mixed blocked/eligible shell-fusion identities; they account for all \(43\) exact shell differences among \(671\) distinct mixed pairs in the dangerous primitive census through \(n=5001\) | Proved identities plus finite classification | `docs/repunit/payout_concentration_diffusion.md` Section 6 | Direct algebra; `scripts/verify_repunit_general_payout_ancestry.py`; `scripts/explore_mixed_shell_pairs.py --limit 5001 --top 100` |
| PCD5 | None of the seven short mixed-fusion valuation blocks lifts to a collision under the naive complete-correction transport \(C_r-3^rC_0\) | Proved here | `docs/repunit/payout_concentration_diffusion.md` Section 7 | Exact affine recurrence and collision-shell comparison; `scripts/verify_repunit_general_payout_ancestry.py` |
| PCD6 | Every canonical shell correction is annihilated into the original high correction after one correctly aligned affine step, so it cannot persist independently to a later payout | Proved here | `docs/repunit/payout_concentration_diffusion.md` Section 8 | Exact identity \(3S(u,2h)+2^{u+1}=2^{u+2h+1}\); `scripts/verify_repunit_general_payout_ancestry.py` |
| PCD7 | If \(Q_B\) is the valuation excess spent on GPA2-blocked payouts and \(N_B\) their effective ledger count, then \(2N_B\le Q_B\le Q_K\), and consequently \(D_K+2N_B\le K\log_2(3/2)\) | Proved here | `docs/repunit/payout_concentration_diffusion.md` Section 9 | Cauchy--Schwarz plus the exact valuation-excess budget; `scripts/verify_repunit_general_payout_ancestry.py` |
| PCD8 | For every \(M\), an abstract valuation word has \(M\) blocked \(q=3\) payouts whose post-payout deficits lie in a band of width \(\log_2(3/2)\) and whose effective count is at least \(4M/9\); a terminal valuation-one run then gives arbitrarily large strict record deficits | Proved here | `docs/repunit/payout_concentration_diffusion.md` Section 10 | Mechanical floor construction; finite prefixes checked by `scripts/verify_repunit_general_payout_ancestry.py` |
| PCD9 | A finite positive valuation word of total \(E\) is realised by an odd-indexed repunit tail iff its first valuation is at least two; in that case exactly one odd exponent class modulo \(2^E\) realises it | Proved here | `docs/repunit/payout_concentration_diffusion.md` Section 11 | Power-of-three subgroup modulo \(2^{E+2}\); `scripts/verify_repunit_general_payout_ancestry.py` |
| PCD10 | For nested balanced cylinders, every change of least representative gives \(n_{m+1}\ge2^{E_m}\), so plateau length at most \(L\) implies \(\operatorname{bitlen}(n_m)\ge E_m-6L+1\); the candidate universal bound \(L=2\) first fails at \(m=1198,1199,1200\) | Proved implication plus finite refutation | `docs/repunit/payout_concentration_diffusion.md` Section 12 | Nested residue classes; `scripts/explore_balanced_q3_cylinders.py --payouts 1500 --show 3`; see also: W13 calibrates the expected law as \(\ell_{\max}(m)\approx1+0.1845\log_2m\), which predicts the \(m=1198\) failure (`docs/density-cycles/extremal_law_calibration.md` §3) |
| PCD11 | A cylinder extended by a suffix of total valuation \(\delta\) has a unique starting-residue lift given by \(t\equiv((s-y)/2)3^{-K}\pmod{2^\delta}\), and its exponent lift is a discrete logarithm in a group of order \(2^\delta\), with normalized generators obeying \(h_{k+1}=h_k+2^{k+1}h_k^2\) | Proved here | `docs/repunit/payout_concentration_diffusion.md` Section 13 | Exact affine and power-of-three recurrences; `scripts/explore_balanced_q3_cylinders.py` |
| PCD12 | Through the first \(1500\) balanced payout prefixes, all \(32\) five-bit and all \(64\) six-bit exponent lifts occur; zero occurs \(39\) times, with plateau histogram \(\{1:1423,2:37,3:1\}\) | Finite certificate | `docs/repunit/payout_concentration_diffusion.md` Section 14 | `scripts/explore_balanced_q3_cylinders.py --payouts 1500 --show 3` |
| PCD13 | If a cylinder of total valuation \(E\) is extended by a suffix of total valuation \(\delta\), with starting lift \(t\), exponent carry \(\kappa\), and \(E+2\ge\delta\), then its exponent lift is \(z\equiv(t-\kappa)[h_E(2r+1)]^{-1}\pmod{2^\delta}\); hence a plateau occurs exactly when \(t=\kappa\) | Proved here | `docs/repunit/payout_concentration_diffusion.md` Section 15 | Binomial truncation; `scripts/explore_balanced_q3_cylinders.py` asserts the identity on every extension |
| PCD14 | With full carry \(C=(3^n-(2r+1))/2^{E+2}\), a plateau extension of total valuation \(\delta\) and starting lift \(t\) obeys \(C'=(C-t)/2^\delta\); iterated plateaus match consecutive carry bits against the concatenated affine lifts | Proved here | `docs/repunit/payout_concentration_diffusion.md` Section 16 | Exact carry identity and iteration |
| PCD15 | For either balanced suffix and every fixed \(M\ge\delta+1\), endpoint states equal modulo \(2^M\) have the same starting lift but successor residues differing by \(3^{\lvert\mathbf v\rvert}2^{M-\delta}\not\equiv0\pmod{2^M}\); endpoint-only fixed-width state is not closed | Proved here | `docs/repunit/payout_concentration_diffusion.md` Section 17 | Exact affine transition; `scripts/verify_repunit_general_payout_ancestry.py` |
| PCD16 | Every consecutive interval of the balanced mechanical block word has homogeneous multiplier \(\mu_W\) satisfying \(2/3<\mu_W<3/2\), independently of its length | Proved here | `docs/repunit/payout_concentration_diffusion.md` Section 18 | Mechanical floor discrepancy; `scripts/verify_repunit_general_payout_ancestry.py` |
| PCD17 | After the initial valuation-three payout and \(L\ge1\) balanced mechanical blocks, normalized correction storage satisfies \(L/2+7/8<Z_L<9L/8+33/32\) | Proved here | `docs/repunit/payout_concentration_diffusion.md` Section 19 | Affine storage recursion plus PCD16; `scripts/verify_repunit_general_payout_ancestry.py` |
| IEF1 | A nested exponent-cylinder branch with depths \(E_m\to\infty\) contains a positive integer iff its canonical representatives are eventually constant, equivalently iff its exponent-lift blocks are eventually zero | Proved here | docs/repunit/integral_escape_frontier.md Section 3 | Canonical residues equal the integer once \(2^{E_m}\) exceeds it |
| IEF2 | A sound residual tree has no positive-integer counterexample if every such counterexample would define an infinite branch and every infinite branch has nonzero exponent lifts infinitely often | Proved conditional framework | docs/repunit/integral_escape_frontier.md Section 4 | Immediate contradiction with IEF1 |
| IEF3 | For the balanced word, if the least endpoint residue \(q_L\equiv B_L2^{-E_L}\pmod{3^{R_L}}\) satisfies \(q_L-195L/128\to+\infty\), then no fixed positive integer realizes the infinite itinerary | Proved conditional reduction | docs/repunit/integral_escape_frontier.md Section 8 | PCD16 gives \(x_L<3x_0/2+195L/128\); eventually \(0<x_L<3^{R_L}\), forcing \(x_L=q_L\) |
| IEF4 | The balanced dual residue obeys \(q'=20+3^rh\), with \(h\equiv(q-23)2^{-5}\pmod{3^R}\) for the 3-step block and \(h\equiv(q-15)2^{-6}\pmod{3^R}\) for the 4-step block | Proved here | docs/repunit/integral_escape_frontier.md Section 9 | Exact inverse-block algebra; scripts/explore_balanced_q3_dual_frontier.py |
| IEF5 | A nonzero dual digit resets the endpoint residue above \(3^{R_s}/448\); after any following zero run, \(q_L>3^{R_s}/672\), so \(27^{s(L)}/L\to\infty\) suffices for IEF3 | Proved here | docs/repunit/integral_escape_frontier.md Section 10 | Dual-digit equation plus PCD16 |
| IEF6 | Through \(L=10000\), \(q_L\ge2^{5L-1}\); both 5-bit and 6-bit dual alphabets are full, zero occurs \(185+59\) times, and the longest zero run is two | Finite certificate | docs/repunit/integral_escape_frontier.md Sections 8--9 | scripts/explore_balanced_q3_dual_frontier.py --blocks 10000 --direct-check 2000 |
| IEF7 | The canonical balanced starting residue \(u_L\pmod{2^{E_L}}\) maps exactly to the canonical dual endpoint \(q_L\pmod{3^{R_L}}\), and its cylinder lift digit equals the dual digit at every block; any fixed positive integer making every finite composition integral forces the common stream to be eventually zero | Proved here | docs/repunit/integral_escape_frontier.md Section 11 | Induction through the affine composition; scripts/explore_balanced_q3_zero_cylinders.py; the converse gives affine integrality, not necessarily exact intermediate valuations |
| IEF8 | Bridge pairs compose exactly by \(u_{WV}=u_W+s2^{E_W}\), \(q_{WV}=q_V+t3^{R_V}\), where \(s\equiv(u_V-q_W)3^{-R_W}\pmod{2^{E_V}}\); at Sturmian standard scales it suffices that \(v_2(q_{S_{k-1}^{a_k}}-u_{S_{k-2}})<E_{k-2}\) infinitely often | Proved exact composition and conditional reduction | docs/repunit/integral_escape_frontier.md Section 12 | Mixed-radix bridge algebra; scripts/explore_balanced_q3_sturmian_renormalization.py |
| IEF9 | The full balanced shortcut parity positions are \(d_0=0\), \(d_i=i+2\lceil\gamma i\rceil\), \(\gamma=\log_2(3/2)/2\), and their unique inverse-conjugacy value is the critical \(2\)-adic Hecke--Mahler value \(\xi=-1/3-(4/3)\sum_{i\ge1}(2/3)^i4^{\lfloor\gamma i\rfloor}\); irrationality of \(\xi\) excludes the balanced itinerary | Proved exact representation and conditional reduction | docs/repunit/integral_escape_frontier.md Section 13 | Mechanical payout count and inverse parity conjugacy; scripts/verify_balanced_q3_hecke_mahler.py |
| IEF10 | No fixed positive integer realizes the complete deterministic balanced \(q=3\) itinerary | Proved here using known Baker linear-form bound | docs/repunit/integral_escape_frontier.md Section 14 | Periodic standard-word parity approximants have height \(O(E_k2^{E_k})\), agree for \(E_k+E_{k-1}\) bits, and Baker gives polynomial consecutive-denominator growth; scripts/verify_balanced_q3_periodic_approximants.py |
| IEF11 | An aperiodic residual parity word is not realized by any fixed integer if eventually periodic approximants with footprint \(N_k\) agree for \(N_k+G_k\) bits, have odd-denominator inverse height at most \(H(N_k)2^{N_k}\), and \(G_k-\log_2H(N_k)\to\infty\); every fixed phase shift of the balanced word satisfies this criterion | Proved here | docs/repunit/integral_escape_frontier.md Section 15 | Divisibility-versus-height contradiction; a fixed shift rotates the periodic approximants, loses only a fixed agreement depth, and changes height by a fixed factor; scripts/verify_balanced_q3_periodic_approximants.py --phase-blocks 100 |
| IEF12 | No fixed positive integer realizes a balanced critical-slope \(q=3\) itinerary whose block word is Sturmian, for any intercept | Proved here using the Bugeaud--Kim repetition theorem | docs/repunit/integral_escape_frontier.md Section 16 | Every Sturmian word has infinitely many prefix/period completions with block agreement ratio at least \(2.4\); after the \(3/4\) parity morphism the agreement excess is linear while inverse height is \(O(N^2 2^N)\); scripts/explore_balanced_q3_sturmian_intercepts.py |
| IEF13 | No fixed positive integer realizes an aperiodic \(q=3\) block itinerary having uniformly bounded critical factor discrepancy and Diophantine exponent greater than \(1\); consequently every such word of linear factor complexity is discharged | Proved here using Bugeaud--Kim repetition theory | docs/repunit/integral_escape_frontier.md Section 17 | Bounded discrepancy makes the parity-code length \(\lambda n+O_D(1)\), so every repetition ratio \(\rho>1\) gives linear agreement excess \(\lambda(\rho-1)n+O_D(1)\), while inverse height is \(O_D(N^2 2^N)\); IEF11; scripts/explore_balanced_q3_residual_axes.py is diagnostic only |
| IEF14 | An aperiodic \(q=3\) itinerary is not realized by a fixed positive integer if eventually periodic prefix approximants have parity footprint \(N_k\), agreement excess \(G_k\), and local critical-discrepancy budget \(K_k\) with \(G_k-2K_k-2\log_2N_k\to\infty\) | Proved here | docs/repunit/integral_escape_frontier.md Section 18 | The inverse height is \(O(N_k^2 2^{N_k+2K_k})\), so IEF11 applies; scripts/explore_balanced_q3_residual_axes.py reports a finite margin diagnostic |
| IEF15 | If cumulative block discrepancy \(S_{L_k}\to-\infty\) while the suffix partition \(Z_{L_k}=\sum_{j\le L_k}2^{S_{L_k}-S_j}\le B\), then a minimal counterexample on that itinerary satisfies \(x_0\le65B/64\); verification through that bound discharges the branch | Proved finite reduction | docs/repunit/integral_escape_frontier.md Section 19 | Exact affine expansion \(x_L=2^{S_L}x_0+\sum b_{r_j}2^{S_L-S_j}\), with \(b_r\le65/64\); scripts/explore_balanced_q3_residual_axes.py reports finite \(S,Z\) diagnostics; see also: W7 finds this is the **binding** IEF17 coordinate: it discharges the generic critical word by a factor \(1.7\times10^3\) (`docs/repunit/ief17_genericity.md`) |
| IEF16 | Every rational non-cyclic trajectory in the \(3/4\)-block language must satisfy \(\liminf S_L/L=0\); either sign of nonzero linear lower discrepancy is excluded | Known theorem translated here | docs/repunit/integral_escape_frontier.md Section 20 | Lopez--Stoll's necessary equality for lower parity density, together with \(R_L/E_L=(R_L/L)/(R_L/L+2)\) and \(S_L/L=cR_L/L-2\) |
| IEF17 | A non-cyclic positive-integer survivor in the terminal \(3/4\)-block language must simultaneously lie above \(10^6\), have \(\liminf S_L/L=0\), satisfy \(\operatorname{dio}(w)=1\) or \(\limsup S_L/L>0\), evade every divergent IEF18 margin (including every IEF21 directional-valley sequence), and satisfy \(Z_{L_k}>64\cdot10^6/65\) eventually along every subsequence with \(S_{L_k}\to-\infty\) | Proved survivor-profile intersection | docs/repunit/integral_escape_frontier.md Section 21 | Ordered contrapositives of FIN1 and IEF13--IEF16, sharpened by IEF18--IEF21; cyclic trajectories remain separate; see also: W7 shows coordinates 2–4 are generic in the critical ensemble; coordinate 5 (IEF15 + FIN1) carries all the content |
| IEF18 | An aperiodic \(q=3\) itinerary is not realized by a fixed positive integer if eventually periodic prefix approximants satisfy \(G_k-J(A_k)-J(B_k)-2\log_2N_k\to\infty\), where \(J(Y)\) is the maximum of zero, the total positive parity drift, and the largest positive suffix drift of \(Y\) | Proved here | docs/repunit/integral_escape_frontier.md Section 22 | Directional correction bound gives inverse height \(O(N_k^2 2^{N_k+J(A_k)+J(B_k)})\); IEF11 applies and IEF14 is a coarser corollary |
| IEF19 | No fixed positive integer realizes an aperiodic \(3/4\)-block itinerary with \(S_L=o(L)\) and \(\operatorname{dio}(w)>1\); hence every non-cyclic survivor satisfies \(\operatorname{dio}(w)=1\) or \(\limsup S_L/L>0\) | Proved here | docs/repunit/integral_escape_frontier.md Section 23 | The exact code-length identity \(E(j)=\lambda j+S_j/c\) converts every fixed block repetition surplus into linear parity-bit surplus; sublinear prefix drift also makes both directional budgets \(o(N_k)\); combine IEF18 and IEF16 |
| IEF20 | No fixed positive integer realizes an aperiodic \(3/4\)-block itinerary having periodic-prefix approximants with block footprint \(n_k\to\infty\), agreement at least \((1+\varepsilon)n_k\), and earlier drift envelope \(D_k=\max_{j\le m_k}\lvert S_j\rvert=o(n_k)\) | Proved here | docs/repunit/integral_escape_frontier.md Section 24 | Exact code-length identity gives linear agreement surplus and the drift envelope makes \(J(\chi(U_k))+J(\chi(V_k))=o(n_k)\), so IEF18 applies; this can discharge words with positive global drift limsup |
| IEF21 | For a full block word \(W\), \(J(\chi(W))=S_{\lvert W\rvert}-\min_{j\le\lvert W\rvert}S_j\) exactly; hence no fixed positive integer realizes an aperiodic itinerary having fixed-surplus periodic-prefix approximants with sublinear two-cut terminal draw-up \(H_k\) and sublinear footprint-to-agreement drift loss \(L_k\) | Proved here | docs/repunit/integral_escape_frontier.md Section 25 | Suffixes beginning inside \(1^r00\) are dominated by block-boundary suffixes; the exact code-length identity and IEF18 then give the discharge; scripts/explore_balanced_q3_residual_axes.py cross-checks the parity and block costs exactly |
| IEF22 | The integer graph \(\mathcal G\) of zero-digit transitions \(q\mapsto\Phi_3(q)=(27q+19)/32\) on \(q\equiv23\pmod{32}\) and \(q\mapsto\Phi_4(q)=(81q+65)/64\) on \(q\equiv15\pmod{64}\) has out-degree at most one and no infinite forward path | Proved here | `docs/repunit/dio1_cocycle_problem.md` Sections 7.1--7.6 (Theorem G) | Functional partition \(15\not\equiv23\pmod{32}\); finite AA/BB runs; infinite paths need infinitely many AB transitions, but AB-parameter nestings have moduli \(\to\infty\); `scripts/verify_zero_digit_orbits.py` |
| IEF23 | For every infinite word \(w\in\{3,4\}^{\mathbb N}\), the IEF4 dual-digit stream \(j(w)\) is not eventually zero | Proved here | `docs/repunit/dio1_cocycle_problem.md` Sections 2 and 7.6 (Problem D1, strong form) | An eventually-zero tail is an infinite path in \(\mathcal G\), contradicting IEF22; `scripts/verify_zero_digit_orbits.py`; `scripts/explore_cocycle_factor_complexity.py` is diagnostic only |
| IEF24 | No fixed positive integer makes every finite affine composition along an infinite \(\{3,4\}\)-block word integral; equivalently, no positive integer realizes an infinite itinerary in the terminal \(3/4\)-block language in the IEF7 integrality sense | Proved here | `docs/repunit/dio1_cocycle_problem.md` Section 9; depends on IEF7 and IEF23 | IEF7 forces any such integer to have eventually-zero dual digits, contradicting IEF23; does not by itself address trajectories that leave \(\mathcal L_{3/4}\) (atlas cover lemma L5) |
| REPLOW3 | The low-prefix classes are nested truncations of the unique odd \(\alpha\in\mathbb Z_2\) satisfying \(3^{\alpha+1}=-7\), and can extend beyond any prescribed finite recovery horizon | Proved here | `docs/repunit/repunit_low_prefix_obstruction.md` | Closed form \(v_2(3^{n+1}+7)\ge K+3\); `scripts/verify_repunit_low_prefix.py` |
| REPLOW4 | A positive exponent realising \((2,1^{K-1})\) satisfies \(K<\log_2(3)(n+1)-2\), so this 2-adic branch cannot shadow for \(3n\) steps | Proved here | `docs/repunit/repunit_low_prefix_obstruction.md` | Divisibility plus ordinary size bound |
| DEN1 | Almost every odd integer has finite stopping time, with the explicit bound stated in the note | Known theorem rederived | `docs/density-cycles/stopping_time_density.md` | Terras/Everett; verifier checks finite instances of the ingredients |
| POT1 | The decayed-bit potential decreases on the explicit recharge family under the stated parameter bound | Proved here | `docs/no-go/Exponential_Decay_Potential.md` | Proof uses a uniform ratio and fuel bound |
| POT2 | Epoch-potential descent for odd \(x\le10^6\) under \(c=r=0.2\) | Finite certificate | `docs/no-go/Exponential_Decay_Potential.md` | `scripts/verify_exponential_potential.py` |
| CYC1 | A \(K\)-odd-step cycle satisfies \(x(2^{E_K}-3^K)=c_K\) | Proved here | `docs/density-cycles/cycle_reduction.md` | `scripts/verify_cycle_reduction.py` checks the identity |
| CYC2 | The bounded valuation-pattern search implemented for \(K\le8\) finds only \(x=1\) | Finite certificate | `docs/density-cycles/cycle_reduction.md` | Not exhaustive over unbounded \(E_K\) |
| CYC3 | Minima of nontrivial cycles have natural density zero | Conditional corollary | `docs/density-cycles/cycle_reduction.md` | Depends on DEN1; does not imply the same for every cycle element |
| CYC4 | No nontrivial positive cycle has an element \(\le10^6\) | Finite certificate | `docs/density-cycles/cycle_reduction.md` | Any such cycle would have a minimum \(\le10^6\), contradicting FIN1 |
| TREE1 | The all-ones residue anchors every tested descent-tree depth and has minimal initial valuations | Proved burn + finite tree certificate | `docs/density-cycles/descent_tree_survivors.md` | `scripts/verify_tree_survivors.py` |
| TREE2 | Tree-survivor density is universally bounded by \(\rho^K\) | **Refuted** (exact computation; first failure \(K=195\)) | `docs/density-cycles/descent_tree_survivors.md` | `scripts/verify_survivor_density_rate.py`; see COR1–COR2 for the correct rate |
| COR1 | \(\operatorname{dens}(\tilde S_K)\le31\,\rho^{K/\theta}\) for all \(K\ge1\) | Proved here | `docs/density-cycles/corridor_rate.md` | `scripts/verify_corridor_rate.py` |
| COR2 | \(\lim \operatorname{dens}(\tilde S_K)^{1/K}=\rho^{1/\theta}=0.9659\ldots\) | Proved here | `docs/density-cycles/corridor_rate.md` | DP rate convergence (finite evidence for the limit; proof is human) |
| COR3 | Undischarged-class count grows with branching factor \(2\rho^{1/\theta}=1.9318\ldots\) | Proved here (from COR1/2) | `docs/density-cycles/corridor_rate.md` | Corollary 2 of `docs/density-cycles/corridor_rate.md` |
| PAR1 | Two trajectories with nonzero offset cannot follow the same parity-rule sequence indefinitely | Known theorem rederived | `docs/core/Collatz_Parity_Fragility_Corrected.md` | Terras 1976 / Everett 1977 parity-vector injectivity, restated for the C-map (k halvings in place of k T-steps); does not imply non-merging, repulsion, or absence of basins |

## Exploratory documents

These notes and directories are not dependencies of universal proofs in the
proved-results track. A specifically cited `explore_*.py` run may still be the
reproducible generator for an explicitly finite or mixed ledger row:

- `RESEARCH_ROADMAP.md`
- `RESIDUAL_ATLAS.md`
- `docs/residual-atlas/`
- `docs/fuse/fuse_map_theory.md`
- `docs/fuse/fuse_burn_attack.md`
- `docs/repunit/repunit_tail_attack.md`
- `docs/repunit/repunit_diagonal_survivor_notes.md`
- `docs/repunit/repunit_bad_automaton_notes.md`
- `docs/repunit/repunit_normal_form_notes.md`
- `docs/fuse/binary_fuel_bad_block_notes.md`
- `docs/repunit/repunit_equidistribution_reframing.md`
- `docs/repunit/next_generation_attack_program.md`
- `docs/no-go/outside_box_avenue_triage.md`
- `docs/no-go/outside_box_avenue_portfolio.md`
- `docs/no-go/avenue_a_comparison_dynamics.md`
- `docs/repunit/hecke_mahler_route_a.md`
- `docs/repunit/l4_coupling_analysis.md`
- `docs/nested-anchor/near_threshold_episode_notes.md`
- `docs/diagnostics/diagnostics_attractor_sieve_spike.md`
- the twelve Opus 5 wide-attack notes (W1–W13), synthesised in
  `OPUS5_WIDE_RESULTS.md`:
  - `docs/no-go/baker_explicit_constants_audit.md` (W9)
  - `docs/no-go/certificate_semigroup.md` (W2)
  - `docs/repunit/rotation_cocycle_rigidity.md` (W11)
  - `docs/no-go/digit_bridge_ceiling.md` (W10)
  - `docs/no-go/superposition_interaction_ledger.md` (W1)
  - `docs/no-go/two_tower_interference.md` (W8)
  - `docs/no-go/machine_synthesis_surviving_class.md` (W6)
  - `docs/density-cycles/extremal_law_calibration.md` (W13)
  - `docs/density-cycles/kl_rail_restricted_tree.md` (W4)
  - `docs/repunit/syracuse_3adic_conditioning.md` (W5)
  - `docs/repunit/ief17_genericity.md` (W7)
  - `docs/no-go/carry_cocycle_polynomial_model.md` (W3)
- all other `explore_*.py` programs

## Archived documents

Superseded heuristics, legacy summaries, and their bounded artifacts are
listed in `archive/README.md`. They are retained for provenance and are not
dependencies of maintained claims.

## Admission rule

A claim may be promoted to **Proved here** only when its quantifiers and domain
are explicit, the human proof covers all cases, its dependencies are already
proved, and any verifier tests the same statement without silently replacing a
universal quantifier by a finite range. Claims depending essentially on an
external theorem must instead identify that provenance in their status and
source note. Finite certificates must give the exact domain and a reproducible
command or artifact.

## Pending proposals (Opus 5 wide attack, not admitted)

The twelve wide-attack sessions proposed **25 rows** and admitted none. They
are consolidated, grouped by what they would be worth, in
`OPUS5_WIDE_RESULTS.md` §5. Each carries a verifier and a falsifier in its
source note; none has had a human proof read, which the admission rule above
requires.

Two points need a decision before any promotion:

- **DBC1 supersedes BAKEX3.** The general ghost identity
  \(v_2(3^n-A)=2+v_2(n-\alpha_A)\) (`docs/no-go/digit_bridge_ceiling.md` §1)
  contains the \(A=-7\) case stated separately in
  `docs/no-go/baker_explicit_constants_audit.md` §4.1. File as one row, not two.
- **BAKEX2 is the only proposal that changes a maintained result**: it would
  remove the Baker hypothesis from the Avenue A \(L=1\) gates, leaving
  \(K_\downarrow(n)\le6n\) as the sole condition. It is also the one most
  worth a proof read.

The remaining proposals are finite certificates or methodological notes. One
is worth keeping even if nothing else is admitted: **MSY4** — a SAT answer in
the potential-synthesis class is meaningless unless its coordinate compression
is published alongside it.

## General track (branch `no-go-general`, 2026-07-25)

Added on a branch, **not human-reviewed**. Every row carries a passing exact-arithmetic
verifier, but a passing verifier is not a proof read. Read `SUFF1`, `COST1` step 6, and
`UNIF1` first; those are the three where the label is doing the most work.

| ID | Claim | Status | Source | Verification |
|---|---|---|---|---|
| QLG1 | Quantized-log no-go: exact closure criterion \(s=E\,2^{j}-K\,L_j\in[0,K]\); certificates refuting \(\log_2x+g(\lfloor2^{j}\log_2x\rfloor,\tau,x\bmod16)\) | Proved + finite certificate | manuscript §6 (**not yet written**) | `scripts/verify_quantized_log_criterion.py`; supersedes the claim in `\section{The boundary}` that a certificate needs total gain in \((0,2^{-j})\) — see correction below |
| EXR1 | On a valuation-one step the storage coordinate and the deficit both scale by exactly \(3/2\); \(D_K-\log_2Z_K\) is invariant, so no argument using only valuation-one data can show deficit storage is unsustainable | Proved here | `docs/no-go/storage_exchange_rate.md` | `scripts/verify_storage_exchange_rate.py`; promoted from `repunit_extremal_principle.md` §9 |
| SHG1 | For \(T(x)=(ax+b)/c^{v_c(ax+b)}\), \(\gcd(a,c)=\gcd(b,c)=1\), \(c\) prime: an expanding rational cycle (\(c^E<a^K\)) implies no potential \(\log_cx+g(c\text{-adically local data})\) is nonincreasing; \(\mathrm{len}_c\) is covered iff \(a^K/c^E<c\). SH1 is the \((3,1,2)\) instance | Proved here | `docs/no-go/general_shadow.md` | `scripts/verify_general_shadow.py`; 17 cycles across 11 maps |
| QLG-GEN | The closure criterion is exactly \(\{K\log_ca\}\le K\{Q\log_ca\}/Q\) — an identity, unconditional, with the map absent | Proved (identity) | `docs/no-go/general_cost_law.md` | `scripts/verify_general_cost_law.py` |
| DICH1 | \(\log_ca\) rational \(\iff a=c^k\), and then no expanding quantized-log certificate exists at any precision. The mechanism is present exactly when \(\log_ca\) is irrational | Proved here | `docs/no-go/general_cost_law.md` | `scripts/verify_general_cost_law.py` |
| COST1 | Admissibility \(\iff\lfloor K\beta\rfloor/K\ge\lfloor Q\beta\rfloor/Q\) (the bound \(s\le K\) is vacuous); \(K_{\min}(Q)\le Q\); \(K_{\min}(Q)\) is a semiconvergent denominator of \(\beta\) | Proved here (steps 0–5); **step 6 is Khinchin applied, not reproved** | `docs/no-go/cost_law_proof.md` | `scripts/verify_cost_law_proof.py` |
| WITN1 | Independently re-mined certificates for \(j=3..8\), \(m=16\), each closing exactly with strict integer gain; first window \(2^{\,j+6}\) throughout (**exploratory**) | Finite certificate | `docs/no-go/quantized_log_witnesses.md` | `scripts/verify_quantized_log_witnesses.py` |
| CARRY1 | Under \(x\ge Q/(3\ln2(1-\varphi_Q))\), cell displacement is \(L_Q-Qe+\delta\), \(\delta\in\{0,1\}\); \(\sum\delta_i=s\), so \(s\) counts carrying edges | Proved here | `docs/no-go/sufficiency_reduction.md` | `scripts/verify_sufficiency_reduction.py`; height hypothesis shown necessary |
| WALK1 | The mod-\(2^m\) automaton has self-loops of weight 1 at \(2^m-1\) and weight 2 at \(1\) (identities, all \(m\ge3\)); with connectivity this gives closed walks of length \(K\) and valuation \(\lfloor K\log_23\rfloor\) for all \(K\ge2\) | Proved here | `docs/no-go/sufficiency_reduction.md` | `scripts/verify_sufficiency_reduction.py` |
| TAU1 | \(\tau\ge2\iff e=1\); \(e=1\Rightarrow\tau(f(x))=\tau(x)-1\); \(e\ge2\Rightarrow\tau=1\) with \(\tau(f(x))\) free. So \(\tau\) is a function of the \(e\)-word and imposes no extra constraint | Proved here | `docs/no-go/tau_coupling.md` | `scripts/verify_tau_coupling.py`; consistent with RUNLEN2 and the burn identity |
| UNIF1 | The cell dip \(\min_i(\lfloor i\log_23\rfloor-E_i)\) is \(-cK+O(1)\), \(c\approx0.24\), so one height serves all \(K\) edges | Proved here (**finite certificate for the rate, one word ordering, \(K\le800\)**) | `docs/no-go/uniformity.md` | `scripts/verify_uniformity.py` |
| SUFF-32 | \(x_1=2^n+27\), \(n\ge10\), gives an infinite family of closed certificates at \((j,m,K)=(3,16,2)\); \(n\ge10\) is sharp and predicted by CARRY1 | Proved here | `docs/no-go/uniformity.md` | `scripts/verify_uniformity.py`; verified to \(n=200\) |
| SUFF1 | For every \(j\), every admissible \(K\), and every \(m\) with the automaton strongly connected: a closed certificate exists from \(\Theta=m+K+j+\log_2(1/\min(\varphi_Q,1-\varphi_Q))+K/4+O(1)\) bits. Strict gain is automatic from \(3^K>2^{\lfloor K\log_23\rfloor}\) | **Proved here, unconditional** (its connectivity hypothesis is now CONN1) | `docs/no-go/suff1.md` | `scripts/verify_suff1_composition.py` |
| CONN1 | The mod-\(2^m\) suffix automaton is strongly connected for every \(m\ge3\), via the explicit hub \(h_m=3^{-1}(2^{m-1}-1)\bmod2^m\): \(v_2(3h_m+1)=m-1\) so \(h_m\) reaches all odd residues in one step, and the class-growth lemma gives every live node a path to \(h_m\) in \(\le m-1\) steps (sharp, attained at \(2^m-1\)). **Removes the last hypothesis from SUFF1** | Proved here | `docs/no-go/connectivity.md` | `scripts/verify_connectivity.py`; general \((a,b,c)\) hub not written |

### Correction history for this branch

### Audit correction (2026-07-25)

An earlier pass in the session that produced this branch asserted that the 2026-07-03
merge `82b317d` **dropped** eight ledger rows (SH1, SH2, NLP2, NLPD, TWR1, SPN1, BND1,
FFN1). **That assertion was wrong**, and the real git history says so:

- `82b317d` has parents `aa51f05` (26 rows) and `19eed41` (73 rows) and produces 77.
  It is a **union of two parallel development lines**, not a loss. No row present in
  either parent is absent from the merge.
- The eight rows were never in `CLAIM_LEDGER.md` before the merge either. They first
  appear at `b4317d7` (2026-07-13), where they were added deliberately.
- They are present on `main` today and have been since 2026-07-13.

What was historically true is narrower: between 2026-07-03 and 2026-07-13 the README and
manuscript referenced results whose canonical rows lived only in the source notes under
`docs/no-go/`, not in the central ledger. That gap was closed on 2026-07-13 without
outside prompting.

No repair is therefore included on this branch, and none is needed. The rows below are
all genuinely new — verified against `1af9514` to contain no duplicate IDs and no file
collisions.

- **Manuscript-affecting.** `\section{The boundary}` states that a closed certificate
  needs total gain in \((0,2^{-j})\), which "pure shadows cannot supply", with "no
  uniform construction known". **Refuted by construction.** The bound applies to
  single-witness chains only; multi-witness cycles reset in-cell position at each
  junction and the correct criterion is the exact integer one (QLG1, COST1). The
  Question posed in that section — whether a nonincreasing potential
  \(\log_2x+g(\lfloor2^{j}\log_2x\rfloor,\tau,x\bmod2^m)\) exists — is answered
  **no** for \(j\le8\) by explicit certificates (WITN1) and, at \((j,m)=(3,16)\), at
  every height by an infinite family (SUFF-32).

- **Simplification.** Theorem E(b)'s hypothesis \(\sum\varepsilon_i<1\) is **not
  required for sufficiency**: the gain is \((3^K/2^E)\prod(1+1/(3x_i))>3^K/2^E>1\)
  outright. Retain it only if E(b) is used for necessity.

- **Simplification.** The window \(s\in[0,K]\) is equivalent to \(s\ge0\); the upper
  bound is vacuous for irrational \(\log_ca\).

- **Corrections caught by the verifiers during this session, all pre-promotion.**
  (i) CARRY1 first stated without the height hypothesis — false for small \(x\) at
  large \(j\). (ii) TAU1(T3) first tested by bounded scan, which reported a spurious
  failure at \(t=16\); replaced by direct construction. (iii) SUFF-32 first claimed
  from \(n\ge5\); false at \(n=9\), where \(\delta=1\).