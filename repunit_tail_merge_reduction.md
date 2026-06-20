# A Merge Reduction for Repunit Tails

**Building on:** `repunit_normal_form_notes.md`,
`repunit_affine_tail_bound.md`
**Status:** Exact merge framework plus bounded computational certificate. This
does not prove that every repunit tail merges or descends.
**License:** CC-BY 4.0

---

## 1. Motivation

For odd \(n\), let

\[
a_n=\frac{3^n-1}{2},
\qquad
x_i(n)=f^{(i)}(a_n).
\]

The direct programme seeks to prove that every \(x_i(n)\) eventually falls
below \(2^n-1\). Computation reveals a second mechanism: many repunit tails
merge exactly into tails belonging to smaller exponents before their own first
descent.

Once two tails merge, all later iterates agree. A merge into a smaller exponent
therefore allows the larger exponent to inherit the smaller tail's descent.

---

## 2. The diagonal normal-form state

The repunit normal form is

\[
x_i(n)
=\frac{3^{n+i}+A_i(n)}{2^{E_i(n)+1}},
\]

where

\[
A_0=-1,\qquad E_0=0,
\]

and

\[
A_{i+1}=3A_i+2^{E_i+1},
\qquad
E_{i+1}=E_i+e_i.
\]

Define the diagonal coordinate

\[
d=n+i
\]

and the diagonal state

\[
\mathcal D_i(n)=\bigl(d,E_i(n),A_i(n)\bigr).
\]

**Lemma 1 (diagonal-state merge criterion).** If

\[
\mathcal D_i(n)=\mathcal D_j(m),
\]

then

\[
x_i(n)=x_j(m),
\]

and the two trajectories agree forever after the merge.

**Proof.** Equality of the diagonal states gives

\[
n+i=m+j,\qquad E_i(n)=E_j(m),\qquad A_i(n)=A_j(m).
\]

Substitution into the normal form makes the two integer states equal. The
shortcut Collatz map is deterministic, so all subsequent iterates agree.
\(\blacksquare\)

This explains why the repeated deficit blocks in
`repunit_diagonal_survivor_notes.md` occur at equal values of \(n+i\): they are
the same orbit segment, not merely similar valuation words.

**Lemma 2 (one-step diagonal collision).** Consider two diagonal states at the
same coordinate \(d\):

\[
(d,E,A),\qquad(d,F,B).
\]

Their successor states are equal if and only if

\[
\boxed{3A+2^{E+1}=3B+2^{F+1}.}
\]

**Proof.** The successor correction terms are

\[
A'=3A+2^{E+1},
\qquad
B'=3B+2^{F+1}.
\]

Thus equality of successor states requires \(A'=B'\). Conversely, if this
equality holds, both successor cumulative valuations are

\[
v_2(3^{d+1}+A')-1.
\]

Hence their successor pairs \((E',A')\) agree, and so do the full diagonal
states. \(\blacksquare\)

In particular, a first coalescence is governed by a collision of the scalar
quantity

\[
H(E,A)=3A+2^{E+1}.
\]

---

## 3. Merge inheritance

Let

\[
\sigma_n=\min\{K\ge1:x_K(n)<2^n-1\},
\]

when this minimum exists.

**Theorem 3 (merge inheritance).** Let \(m<n\). Suppose

\[
x_i(n)=x_j(m)
\]

for some \(i\ge0\) and \(0\le j\le\sigma_m\). Then \(\sigma_n\) is finite and

\[
\sigma_n\le i+\sigma_m-j.
\]

**Proof.** After the merge,

\[
x_{i+t}(n)=x_{j+t}(m)
\]

for every \(t\ge0\). Set \(t=\sigma_m-j\). Then

\[
x_{i+\sigma_m-j}(n)
=x_{\sigma_m}(m)
<2^m-1
<2^n-1.
\]

Thus the \(n\)-tail has descended by the stated time. \(\blacksquare\)

**Corollary 4 (strong-induction programme).** Suppose that for every odd
\(n\ge N\), at least one of the following holds:

1. the \(n\)-tail descends below \(2^n-1\) directly; or
2. before descent it merges into the pre-descent tail of some odd \(m<n\).

If every odd exponent below \(N\) descends, then every odd exponent descends.

This turns the universal repunit problem into a **merge-or-descend** problem.

---

## 4. Finite merger certificate

`explore_repunit_tail_merges.py` processes exponents in increasing order. For
each exponent it follows the exact tail until first descent or until it reaches
a state already visited by a smaller exponent. Fingerprints are used only as
an index; every reported merge is verified by recomputing and comparing the
full integer states.

For odd \(7\le n\le10001\):

- total exponents: \(4998\);
- exact mergers into smaller tails: \(4783\);
- primitive tails reaching their own first descent without an earlier merge:
  \(215\);
- unresolved within \(3n\): \(0\);
- merge fraction: \(95.70\%\);
- off-diagonal exact mergers: \(0\);
- the most frequent merge gaps are \(2,4,6,8,10\);
- the worst primitive stopping ratio remains
  \[
  \sigma_{23}/23=63/23.
  \]

The primitive counts in initial ranges are:

| largest exponent | primitive tails |
|---:|---:|
| \(1001\) | \(89\) |
| \(2001\) | \(117\) |
| \(3001\) | \(140\) |
| \(4001\) | \(152\) |
| \(5001\) | \(165\) |
| \(10001\) | \(215\) |

These are finite observations. They suggest that the primitive set is much
sparser than the full exponent family, but do not establish an asymptotic
rate.

The primitive proportion falls over the tested initial ranges:

| largest exponent | primitive proportion |
|---:|---:|
| \(1001\) | \(17.87\%\) |
| \(2001\) | \(11.72\%\) |
| \(3001\) | \(9.35\%\) |
| \(4001\) | \(7.61\%\) |
| \(5001\) | \(6.61\%\) |
| \(10001\) | \(4.30\%\) |

The primitive exponents still occupy every odd residue class modulo \(32\)
and 31 of the 32 odd classes modulo \(64\). Thus the observed thinning is not
explained by exclusion of a fixed small collection of low-bit classes.

---

## 5. New proof target

The diagonal recurrence gives a deterministic state machine:

\[
(d,E,A)
\longmapsto
\left(
d+1,\,
E+e,\,
3A+2^{E+1}
\right),
\]

where

\[
e=v_2\!\left(3^{d+1}+3A+2^{E+1}\right)-(E+1).
\]

Every odd exponent \(n\) starts at diagonal state

\[
(n,0,-1).
\]

The merge problem is therefore:

> Show that every sufficiently large start state \((n,0,-1)\) either crosses
> the exact descent boundary or coalesces with a state generated by some
> smaller start \((m,0,-1)\).

This is more structured than comparing full Collatz values: coalescence occurs
inside a common diagonal layer and can be studied through the pair \((E,A)\).

### Immediate diagnostics

1. Classify primitive start exponents modulo powers of two.
2. Measure the first diagonal at which nonprimitive tails merge.
3. Determine whether primitive diagonal states have a reusable obstruction to
   coalescence.
4. Compare severe deficit blocks only among primitive tails; merged copies
   should be removed to avoid counting the same orbit segment repeatedly.
5. Search for local conditions forcing a gap-\(2\), gap-\(4\), or gap-\(6\)
   merge.

---

## 6. What this does and does not prove

**Proved:**

- equality of diagonal normal-form states forces exact trajectory merging;
- the scalar one-step collision criterion of Lemma 2;
- a merge into a smaller pre-descent tail transfers finite descent;
- the merge-or-descend strong-induction principle.

**Finite certificate:**

- the merger counts and same-diagonal observations stated for odd
  \(n\le10001\).

**Not proved:**

- that every nonprimitive merge is detected by a finite diagonal rule;
- that the primitive exponent set is finite or density zero;
- that every primitive tail obeys a uniform surplus bound;
- universal Mersenne descent.

---

## 7. Verification

```bash
python explore_repunit_tail_merges.py --limit 10001
python verify_repunit_tail_merges.py
```
