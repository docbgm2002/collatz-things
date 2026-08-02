# Krasikov–Lagarias counting on the rail-restricted backward tree  [W4]

**Task:** `OPUS5_WIDE_TASKS.md` W4 (session 9 of the recommended order).
**Building on:** `corridor_rate.md` (COR1–COR3),
`../no-go/certificate_semigroup.md` (W2, which named W4 as its only live
descendant), `../core/Mod8_Rail_Descent.md` (the rails),
`../no-go/avenue_a_comparison_dynamics.md` (the survivor set W4 aims to
shrink), `extremal_law_calibration.md` (W13, the companion barrier-2 note).
**Script:** `scripts/explore_kl_rail_restricted_tree.py`.
**Status:** **Deliverable answered; avenue closed.** The comparison W4 asks
for returns *equality*, and the target it aims at is unreachable by a density
argument at any exponent.
**License:** CC-BY 4.0

---

## 0. Verdict

W4's first deliverable: "The K–L inequality system written for the mod-8
rail-restricted tree … compare the exponent obtained against the unrestricted
0.84."

> **W4-A (proved here).** The restriction is **free**. For the odd backward
> tree \(x=P_e(y)=(2^{e}y-1)/3\),
> \[
> P_e(y)\equiv-3^{-1}\pmod{2^{m}}\quad\text{for every }e\ge m,
> \]
> independently of \(y\). So a node's residue mod \(2^{m}\) is determined by
> the *terminal* segment of its \(e\)-word whose valuations sum to at least
> \(m\) — a bounded-suffix condition. Restricting to one rail therefore
> multiplies the count by a constant and leaves the exponent untouched.
>
> **The answer to the comparison is therefore: equality.** The rail-restricted
> exponent is the unrestricted exponent, whatever that is.

> **W4-B (the kill).** Even at the right exponent, no density theorem can
> serve Avenue A. The repunit family has counting function \(O(\log x)\);
> the complement of an \(x^{\gamma}\) set has counting function \(\sim x\)
> for every \(\gamma<1\). The shortfall is a factor \(x/\log x\) at every
> scale, so no improvement of the exponent — 0.84 to 0.99 to anything below
> 1 — closes it, and \(\gamma=1\) would need an explicit error term better
> than \(x/\log x\).

The *supporting* role W4 carefully reserved for itself ("shrink the survivor
set that Avenue A schedules must handle; never present density as descent")
also fails, for a reason worth stating: **there is no positive-density
survivor set to shrink.** Avenue A's survivors are indexed by \((n,i)\) along
repunit orbits, a set of counting function \(O(\log^2x)\), not a
positive-density set of integers.

---

## 1. Scope: what is and is not attempted

This session does **not** re-derive the Krasikov–Lagarias exponent \(0.84\);
that needs their full nonlinear programme over mod-\(3^k\) difference
inequalities and is not reproduced here. The question actually posed — does
the rail restriction *move* the exponent — is answered without needing the
value, because §2 shows the restriction acts on a different coordinate
(2-adic) from the one that sets the exponent (3-adic branching).

For orientation, §1.1 records where the *heuristic* exponent sits.

### 1.1 The variational set-up, and an exact coincidence

A depth-\(d\) node with valuation sum \(E\) has size \(\approx2^{E}a/3^{d}\),
so it lies below \(x\) iff \(E\le d\log_23+L\), \(L=\log_2(x/a)\). Counting
compositions and writing \(u\) for the occupancy fraction,

\[
\gamma(u)=\frac{H(u)}{2-u\log_23},\qquad H=\text{binary entropy}.
\]

The maximum is \(\gamma=1\), attained at \(u=3/4\), and it is exact:

\[
H'(3/4)=\log_2\tfrac{1/4}{3/4}=-\log_23,
\qquad
H(3/4)=\tfrac34\log_2\tfrac43+\tfrac12=2-\tfrac34\log_23,
\]

so both the stationarity condition and the value \(\gamma=1\) hold on the
nose at \(u=3/4\). This reproduces the *heuristic* "almost every integer is
in the tree" — the conjecture's own prediction, not a theorem. The proved
\(0.84\) is what survives once mod-\(3^k\) admissibility and node collisions
are imposed.

---

## 2. The restriction is free

### 2.1 The structural reason

\(P_e(y)=(2^{e}y-1)/3\). Modulo \(2^{m}\), the term \(2^{e}y\) vanishes as
soon as \(e\ge m\), leaving \(P_e(y)\equiv-3^{-1}\). Verified for
\(m\in\{3,4,6,8\}\), all \(e\in[m,m+5]\), all admissible \(y<400\).

Consequently the residue of a node mod \(2^m\) is a function of a bounded
suffix of its \(e\)-word: read backwards until the cumulative valuation
reaches \(m\). Everything earlier is invisible.

### 2.2 Measured

The K–L exponent is a property of the *counting scheme* — how many
\(e\)-words fit a given valuation budget — not of the realised integer set,
which is conjecturally all of \(\mathbb N\) and so tells one nothing.
Counting words under the budget \(\sum e\le S\) (the exact proxy for
"node \(\le2^{S}a/3^{d}\)") and tabulating the endpoint's residue mod 8:

| \(S\) | words | share in 1 / 3 / 5 / 7 |
|---:|---:|---|
| 12 | 49 | 0.2041 / 0.2041 / 0.5102 / 0.0816 |
| 16 | 156 | 0.1859 / 0.1731 / 0.5641 / 0.0769 |
| 20 | 487 | 0.1910 / 0.1889 / 0.5667 / 0.0534 |
| 24 | 1533 | 0.1944 / 0.1898 / 0.5662 / 0.0496 |
| 28 | 4842 | 0.1929 / 0.1904 / 0.5618 / 0.0549 |
| 32 | 15289 | 0.1886 / 0.1888 / 0.5630 / 0.0596 |

The shares stabilise (largest change 0.0046 between the last two budgets) and
all four are bounded away from zero. Each rail keeps a fixed positive share
of the words, so the growth rate is common to all of them.

**The dominant rail is \(5\bmod8\), with share \(0.563\), and that is not an
accident:** \(-3^{-1}\equiv5\pmod8\), so every word whose final valuation is
at least 3 lands there. It is exactly the residue of the \(\sigma\)-ghost
\(-1/3\) of W2, whose image is precisely \(\{x\equiv5\bmod8\}\). The
mod-8 rail structure of the backward tree is the \(\sigma\)-ghost seen at
depth 3.

---

## 3. The gap to Avenue A

The repunit family's counting function:

| \(x\) | repunits \(\le x\) | \(x^{0.84}\) | complement of an \(x^{0.84}\) set |
|---|---:|---|---|
| \(2^{64}\) | 21 | \(2^{53.8}\) | \(\sim2^{64}\) |
| \(2^{256}\) | 81 | \(2^{215.0}\) | \(\sim2^{256}\) |
| \(2^{1024}\) | 323 | \(2^{860.2}\) | \(\sim2^{1024}\) |
| \(2^{4096}\) | 1292 | \(2^{3440.6}\) | \(\sim2^{4096}\) |

A K–L theorem says the tree contains **at least** \(x^{0.84}\) integers below
\(x\). Its complement still has counting function \(\sim x\), larger than the
repunit family by \(x/\log x\). The theorem is therefore consistent with
every single repunit being uncovered.

To cover a family of counting function \(g(x)\) by a density argument one
needs \(x-x^{\gamma}<g(x)\): impossible for any \(\gamma<1\), and for
\(g(x)=O(\log x)\) impossible even at \(\gamma=1\) without an explicit error
term better than \(x/\log x\). **The shortfall is not an exponent problem and
cannot be fixed by sharpening the exponent.**

### 3.1 The rails do not isolate the repunit family either

Over the 31 187 pre-descent states of \(a_n\), \(n\le301\):

| | 1 mod 8 | 3 mod 8 | 5 mod 8 | 7 mod 8 |
|---|---:|---:|---:|---:|
| repunit states | 0.2454 | 0.2448 | 0.2503 | 0.2594 |
| backward-tree words | 0.1886 | 0.1888 | 0.5630 | 0.0596 |

The repunit states are spread almost uniformly across the four rails, while
the tree's words concentrate on rail 5. So the rail restriction does not even
*align* with the target family — it is not merely free, it points the wrong
way.

---

## 4. W2's hand-off, closed

Session 2 found the certificate-transport semigroup is either thin
(\(\Theta((\log X)^2)\)) or, with unrestricted predecessor selectors, exactly
the "reaches 1" set, and named the intermediate regime — finitely many
valuations, \(|E|\ge2\) — as W4's territory.

That regime is a bounded-valuation backward tree, i.e. a condition on the
\(e\)-word alphabet. §2's rail restriction is a bounded-*suffix* condition on
the same word. The two compose without interacting, so the exponent is
unchanged, and §3 applies verbatim.

> **W4-C.** W2's only live descendant is closed by the same gap. Neither task
> retains a surviving branch.

---

## 5. Barrier check

1. *Finite-state information.* §2 is a finite-state statement about the
   \(e\)-word, used negatively (to show the restriction is inert). Consistent
   with barrier 1.
2. *Density / entropy.* **This is the binding barrier and §3 is its sharpest
   form.** W4 anticipated barrier 2 for the *descent* claim and reserved a
   supporting role; the finding is that the supporting role fails too,
   because the object to be supported is not of positive density. Nothing
   here is presented as descent.
3. *Variable-height Diophantine.* Not invoked.
4. *Virtual sources.* Not invoked; §3.1 uses actual repunit orbits.

**Explicit non-claims.** The exponent \(0.84\) is not re-derived, improved,
or disproved. No statement here bears on whether K–L's bound is sharp. The
claim is only about what a bound of that shape can and cannot do for this
repository's target.

---

## 6. Falsifier

- **W4-A** is falsified by a modulus \(2^m\) and an \(e\ge m\) with
  \(P_e(y)\not\equiv-3^{-1}\), or by a rail whose word-share tends to zero as
  the valuation budget grows. Neither occurs in the tested range.
- **W4-B** is falsified by a density theorem with an *explicit* error term
  smaller than \(x/\log x\) — which would be a far stronger result than
  anything in the K–L lineage and would immediately be interesting for other
  reasons.
- **§3.1** is falsified by a modulus (not necessarily a power of 2) under
  which the repunit pre-descent states concentrate. A quick scan of moduli
  is the cheap follow-up if anyone wants to revisit: the claim here is only
  about the mod-8 rails W4 named.

---

## 7. Reproduction

```bash
python3 scripts/explore_kl_rail_restricted_tree.py
```

Prints `KL-RAIL: consistent`. Runs in well under a second; the word
enumeration is exact, and floats appear only in reported shares and in §1.1's
entropy formula, which is a heuristic anyway.

---

## 8. Ledger

**No rows proposed.** W4-A is a small exact lemma but of no independent
interest; W4-B and W4-C are negative scoping results about a method. The
appropriate home is this note plus the portfolio entry, and the useful
downstream effect is that the mod-8 rails should not be revisited as a
density-restriction device.

Pairs with `extremal_law_calibration.md` (W13): that note calibrates what the
extremal targets *look like*; this one records that density arguments cannot
reach them at all. Together they fence off the whole distributional side of
the programme.
