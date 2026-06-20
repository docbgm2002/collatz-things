# The Primitive 256-Block Target

**Building on:** `repunit_affine_tail_bound.md`,
`repunit_tail_merge_reduction.md`
**Status:** Conditional reduction plus finite certificate. The universal
256-block floor is a proof target, not yet proved.
**License:** CC-BY 4.0

---

## 1. The block floor

For odd \(n\), let

\[
x_i(n)=f^{(i)}(a_n),
\qquad
e_i(n)=v_2(3x_i(n)+1).
\]

Call an orbit segment **active** if it occurs before either:

1. descent below \(2^n-1\); or
2. an exact merge into the pre-descent tail of a smaller odd exponent.

The proposed block statement is:

> **256-Block Floor.** Every active block of 256 consecutive valuations
> satisfies
> \[
> \sum_{j=i}^{i+255}e_j(n)\ge425.
> \]

The threshold exceeds neutral Collatz growth:

\[
\delta
=425-256\log_2 3
=19.2495998\ldots>0.
\]

---

## 2. Conditional descent theorem

**Theorem 1.** Assume the 256-Block Floor. Then every odd-indexed repunit tail
with \(n\ge3\) descends below its Mersenne target \(2^n-1\). More precisely,
every active primitive tail with \(n\ge7\) must descend or merge by

\[
K_n=256\left\lceil\frac n{32}\right\rceil
\le8n+248
\]

odd-steps.

**Proof.** Use strong induction on odd \(n\). The finitely many odd
\(3\le n<33\) are checked directly.

Assume every smaller odd exponent descends. Follow the \(n\)-tail. If it
descends, we are done. If it merges into a smaller pre-descent tail, merge
inheritance (`repunit_tail_merge_reduction.md`, Theorem 3) gives descent.

It remains to rule out an active tail lasting through \(K_n\). Put

\[
B=\left\lceil\frac n{32}\right\rceil,
\qquad
K_n=256B.
\]

Partition the first \(K_n\) valuations into \(B\) consecutive 256-blocks. By
the assumed floor,

\[
E_{K_n}\ge425B.
\]

Therefore the raw surplus satisfies

\[
\begin{aligned}
S_{K_n}(n)
&=E_{K_n}-K_n\log_2 3
 -\log_2\left(\frac{a_n}{2^n-1}\right)\\
&>
B\delta-n\log_2(3/2).
\end{aligned}
\]

Since \(B\ge n/32\),

\[
S_{K_n}(n)
>
n\left(\frac{\delta}{32}-\log_2(3/2)\right)
=0.01658749\ldots\,n.
\]

For \(n\ge33\), this exceeds the affine allowance

\[
K_n\log_2\left(1+\frac1{3(2^n-1)}\right)
\]

from `repunit_affine_tail_bound.md`. Hence the affine-safe descent criterion
forces \(x_{K_n}(n)<2^n-1\), contradicting activity through \(K_n\).

For completeness, \(K_n\le16n\) when \(n\ge33\), so the affine allowance is
less than

\[
\frac{16n}{3(2^n-1)\ln2},
\]

which is already smaller than \(0.01658749\,n\) at \(n=33\) and decreases
thereafter.

Thus each \(n\)-tail descends or merges by \(K_n\), and either outcome gives
finite descent. \(\blacksquare\)

The constant \(8\) is not intended to be sharp. It arises from the first
stable block floor found by the diagnostic search.

---

## 3. Finite certificate

`verify_repunit_256_block.py` processes odd exponents in increasing order.
For each exponent it examines valuations only until first descent or first
exact merge into a smaller tail.

For odd \(7\le n\le10001\):

- complete active 256-blocks checked: \(1{,}712{,}672\);
- minimum total valuation: \(425\);
- blocks below \(425\): \(0\);
- the unique minimum begins at \(n=2449\), step \(306\);
- exact mergers and the active stopping rule are independently checked.

This is a bounded certificate, not a proof of the universal floor.

---

## 4. Why this target is preferable to a fixed 3n claim

The empirical \(3n\) window is stronger numerically but does not yet expose a
local mechanism. The 256-block floor has three advantages:

1. it is stated entirely in exact integer valuations;
2. it combines naturally with the proved affine-tail bound;
3. it only needs to hold before descent or merger, so repeated merged orbit
   segments do not need to be proved again.

It also survived the failure of the analogous 128-block statement. At
\(n=2449\), active 128-blocks with total valuation \(197<203\) occur, but the
enclosing 256-block has total valuation \(425\).

---

## 5. Next proof questions

The universal floor can be attacked through the diagonal state machine:

\[
(d,E,A)
\longmapsto
\left(
d+1,\,
v_2(3^{d+1}+3A+2^{E+1})-1,\,
3A+2^{E+1}
\right).
\]

Promising formulations are:

1. **Low-block forces merge:** if a 256-block has total valuation at most
   \(424\), then its diagonal path collides with a path from a smaller exponent.
2. **Low-block forces prior descent:** the same valuation shortage makes the
   exact value cross below \(2^n-1\) before the block completes.
3. **Finite-state exclusion:** after normalising \(A\) by the current
   valuation scale, no active diagonal state admits a 256-extension of weight
   at most \(424\).

The first formulation directly unifies the merge and surplus programmes.

---

## 6. What remains open

No universal 256-block floor is proved here. In particular:

- finite verification cannot exclude a later active block of weight \(424\)
  or less;
- the diagonal state space has not yet been reduced to finitely many
  normalised cases;
- no universal primitive-tail bound follows without the block floor.

The note isolates one exact statement whose proof would close the repunit-tail
problem.

### Adversarial obstruction

`repunit_low_prefix_obstruction.md` constructs an explicit exponent class whose
first 256 valuations have weight only \(257\), with no prior descent and no
possible collision through equality of full diagonal states. Therefore a proof
of the 256-Block Floor would require a different merger mechanism for every
exponent in that class.

This substantially raises the burden of the fixed block-floor target. The
conditional reduction remains correct, but a variable-window recovery theorem
depending only on the finite deficit is also excluded by the nested low-prefix
classes. The remaining routes are an off-diagonal merge mechanism or a global
linear-window non-shadowing theorem.
