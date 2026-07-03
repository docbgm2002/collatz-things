# Bibliography Pass — no-go program (2026-07-02)

**Purpose.** Pre-submission literature check for the manuscript
*Mersenne Obstructions to Local Lyapunov Functions for the 3x+1 Map*
(Theorems A, B, C = NLP1, Tower, NLP-finite-set) and for the repository
notes `docs/no-go/no_local_potential.md`, `docs/no-go/nlp2_alternation.md`, `docs/no-go/tower_theorem.md`.

## Queries run (three sessions, independent framings)

1. Collatz / no Lyapunov function / monotone potential / impossibility
2. Collatz / monotone decreasing function / residue class mod 2^k /
   no-go theorem
3. Collatz / "no function" / "cannot exist" / decreasing weight /
   potential, every step
4. Lagarias annotated bibliography / Lyapunov / monotone / invariant
5. Wirsching / predecessor sets / 3-adic / chains
6. Andaloro / 3x+1 tree / chains / Mersenne preimages

## Findings

**No collision with the theorems.** No prior impossibility theorem for
any concrete class of one-step potentials was located: surveys and
secondary sources state the absence of a known monotone invariant as an
empirical/folklore fact only. The claim in the manuscript is now
formulated as: a search including the annotated bibliographies
(arXiv:math/0309224, math/0608208) located no prior impossibility
theorems; references welcomed.

**Attribution obligation found and discharged (burn identity).**
Lagarias's annotated bibliography II records, under Andaloro (2000),
On total stopping times under 3X+1 iteration, Fibonacci Quart. 38
(2000) 73-78: integers of the form 2^m k - 1 iterate to 3^m k - 1
(with companions 2^{3m}k-5 -> 3^{2m}k-5 and 2^{11m}k-17 -> 3^{7m}k-17,
tied to the rational cycles at -1, -5, -17). This is exactly the
iterated fuse identity underlying the burn family (our family is the
k = 3^j specialization). ACTION TAKEN: attribution remark added after
the burn lemma in the manuscript; Andaloro (2000) added to references.
The manuscript's contribution at that point is explicitly narrowed to
the coordinate-freezing use of the family, not the identity.

Repo-side: `docs/no-go/recharge_nogo.md` and `docs/no-go/no_local_potential.md` should carry
the same attribution note on their burn lemmas when next edited.

**Positioning (predecessor structure).** Wirsching (LNM 1681, 1998)
develops the backward/predecessor structure of the Collatz graph at the
level of counting functions, 3-adic averages, and density. The ancestry
tower (Theorem B) is a distinguished explicit chain in that graph; its
closed form w_d(M), the congruence domain M = 1 mod 2*3^(d-1), the
carry-free periodic normal form, and the 2-adic freezing were not found
anywhere. Andaloro's identities are forward orbits anchored at the
additive constants of rational cycles - a different object from
backward Mersenne ancestry at uniform e=2. Kontorovich-Lagarias
(pruned 3x+1 trees determined by a mod 3^{k+1}, leaf count (4/3)^k)
is adjacent background for mod-3-power backward structure; not a
collision. ACTION TAKEN: Wirsching cited and positioned in the
manuscript's literature paragraph.

## Residual risk assessment

- Theorem A (NLP1) mechanism: both ingredient families are classical or
  near-classical (burn: Andaloro/folklore; recharge: elementary), so the
  residual risk is that the *scissors argument itself* appears in some
  uncatalogued preprint or forum post. Three search framings found
  nothing. Risk: low, not zero. Mitigation already in the text
  ("we would welcome references").
- Theorem B (Tower): no trace of the family or its normal form. Risk:
  very low for the assembled statement; individual small-d instances
  (d=1 recharge form) certainly appear in ad hoc computations across
  the amateur literature.
- Theorem C: depends on A and B; no independent risk located.

## Not done (out of scope for web search)

Full manual read of the two annotated bibliographies (about 350 entries)
and of Wirsching's monograph chapters 2-3. Recommended before actual
submission; expected yield: further attribution notes of the Andaloro
kind, not collisions with the theorems.
