# Gap-Merger Algebra for Repunit Tails

**Building on:** `repunit_tail_merge_reduction.md`,
`repunit_enemy_episode_analysis.md`
**Status:** Exact collision-shell theorem, two explicit infinite merger
families, and finite classification data. This does not yet prove that every
repunit tail merges or descends.
**License:** CC-BY 4.0

---

## 1. Same-diagonal first mergers

Suppose the \(n\)-tail first merges with the \(m\)-tail, where \(m<n\), at

\[
x_i(n)=x_j(m),
\qquad
n+i=m+j=d.
\]

At the preceding diagonal \(d-1\), write the normal-form states as

\[
(d-1,E,A),
\qquad
(d-1,F,B).
\]

The predecessor states are distinct, but their successors coalesce. Therefore

\[
\boxed{
3A+2^{E+1}=3B+2^{F+1}.
}
\]

---

## 2. Collision-shell theorem

**Theorem 1.** At a first same-diagonal merger, \(E\ne F\). Set

\[
u=\min(E,F),
\qquad
|E-F|=2h.
\]

Then \(h\ge1\) is an integer. If \(C_{\rm low}\) is the correction belonging
to cumulative valuation \(u\), and \(C_{\rm high}\) belongs to \(u+2h\), then

\[
\boxed{
C_{\rm low}-C_{\rm high}
=
2^{u+1}\frac{2^{2h}-1}{3}.
}
\]

Moreover, if the outgoing valuations from the low- and high-cumulative states
are \(e_{\rm low}\) and \(e_{\rm high}\), then

\[
\boxed{
e_{\rm low}-e_{\rm high}=2h.
}
\]

*Proof.* Equality of successor corrections gives

\[
3(C_{\rm high}-C_{\rm low})
=2^{u+1}-2^{u+2h+1}.
\]

Hence

\[
C_{\rm low}-C_{\rm high}
=2^{u+1}\frac{2^{2h}-1}{3}.
\]

The quotient is integral only because \(2^{2h}\equiv1\pmod3\); conversely,
divisibility by \(3\) forces \(E-F\) even. Equality of successor cumulative
valuations gives

\[
u+e_{\rm low}=u+2h+e_{\rm high},
\]

proving the valuation relation.

If \(E=F\), the correction identity would give \(A=B\), contradicting that
the predecessor states are distinct. \(\blacksquare\)

The smallest shell \(h=1\) is especially simple:

\[
C_{\rm low}=C_{\rm high}+2^{u+1},
\qquad
e_{\rm low}=e_{\rm high}+2.
\]

This is the dominant observed merger mechanism.

---

## 3. Finite shell census

For odd \(7\le n\le10001\), all \(4783\) first mergers are same-diagonal.
Their predecessor valuation gaps are:

| \(|E-F|\) | mergers |
|---:|---:|
| 2 | 4527 |
| 4 | 192 |
| 6 | 60 |
| 8 | 4 |

Thus the smallest collision shell accounts for \(94.65\%\) of all observed
mergers.

For the three most common exponent gaps:

| exponent gap \(n-m\) | mergers | shell \(|E-F|=2\) | proportion |
|---:|---:|---:|---:|
| 2 | 1547 | 1496 | 96.70% |
| 4 | 806 | 769 | 95.41% |
| 6 | 505 | 470 | 93.07% |

Combined, the smallest shell accounts for \(2735\) of \(2858\), or
\(95.70\%\), of these mergers.

The shell is independent of the exponent gap. The gap determines how the two
tails reach a common diagonal; the collision itself is governed by the local
\((E,A)\) relation.

---

## 4. An infinite gap-\(2\) synchronization family

**Theorem 2.** If

\[
n\equiv31\pmod{64},
\]

then

\[
\boxed{x_2(n)=x_4(n-2).}
\]

Thus the \(n\)-tail merges into the \((n-2)\)-tail no later than its second
odd step.

*Proof.* Since \(v_2(n+1)=5\), the first valuation of the \(n\)-tail is \(6\),
and

\[
x_1(n)=\frac{3^{n+1}-1}{2^7}.
\]

A direct calculation modulo the required powers of \(2\) gives the first
three valuations of the \((n-2)\)-tail as

\[
(2,1,1),
\]

with

\[
x_3(n-2)=\frac{3^{n+1}+31}{2^5}.
\]

The next shortcut numerators are therefore the same:

\[
3x_1(n)+1
=\frac{3^{n+2}+125}{2^7},
\]

\[
3x_3(n-2)+1
=\frac{3^{n+2}+125}{2^5}.
\]

Their \(2\)-adic valuations differ by exactly \(2\), so division to odd part
produces the same integer. \(\blacksquare\)

At the predecessor diagonal, the states are

\[
(E,A)=(6,-1),
\qquad
(F,B)=(4,31),
\]

which lie on the smallest collision shell:

\[
31=-1+2^5.
\]

---

## 5. Further gap-\(2\) synchronization families

Before turning to gap \(4\), the next gap-\(2\) synchronization layer can
also be classified exactly.

**Theorem 3.** If \(n\) lies in any of the four classes

\[
n\equiv79\pmod{128},
\qquad
n\equiv199\pmod{256},
\qquad
n\equiv323\pmod{512},
\qquad
n\equiv1289\pmod{4096},
\]

then

\[
\boxed{x_3(n)=x_5(n-2).}
\]

*Proof.* The required predecessor prefixes and states are:

| exponent class | \(n\)-prefix | \((E,A)\) at step 2 | \((n-2)\)-prefix | \((F,B)\) at step 4 |
|---|---|---:|---|---:|
| \(79\bmod128\) | \((5,2)\) | \((7,61)\) | \((2,1,1,1)\) | \((5,125)\) |
| \(199\bmod256\) | \((4,4)\) | \((8,29)\) | \((2,1,2,1)\) | \((6,157)\) |
| \(323\bmod512\) | \((3,6)\) | \((9,13)\) | \((2,2,2,1)\) | \((7,269)\) |
| \(1289\bmod4096\) | \((2,10)\) | \((12,5)\) | \((4,3,2,1)\) | \((10,2053)\) |

Each row is a direct modular valuation calculation. In every row, the
low-cumulative correction exceeds the high-cumulative correction by
\(2^{F+1}\), so the predecessor states lie on the smallest collision shell.
Their next iterates therefore coincide. \(\blacksquare\)

The fourth family is invisible in a classification based only on the first
smaller tail returned by the merger index: its members also meet the
\((n-4)\)-tail at the same diagonal. Pairwise synchronization must therefore
be classified independently of source-selection order.

At modulus \(4096\), Theorems 2 and 3 cover \(121\) of the \(2048\) odd
residue classes.

---

## 6. An infinite gap-\(4\) synchronization family

**Theorem 4.** If

\[
n\equiv2047\pmod{4096},
\]

then

\[
\boxed{x_2(n)=x_6(n-4).}
\]

Thus the \(n\)-tail merges into the \((n-4)\)-tail no later than its second
odd step.

*Proof.* Here \(v_2(n+1)=11\), so the first valuation of the \(n\)-tail is
\(12\), and

\[
x_1(n)=\frac{3^{n+1}-1}{2^{13}}.
\]

Direct modular calculation gives the first five valuations of the
\((n-4)\)-tail:

\[
(3,1,2,3,1).
\]

Their cumulative valuation is \(10\), and the normal-form correction is
\(2047\), giving

\[
x_5(n-4)=\frac{3^{n+1}+2047}{2^{11}}.
\]

Again the next shortcut numerators agree:

\[
3x_1(n)+1
=\frac{3^{n+2}+8189}{2^{13}},
\]

\[
3x_5(n-4)+1
=\frac{3^{n+2}+8189}{2^{11}}.
\]

Their valuations differ by \(2\), and the odd outputs coincide.
\(\blacksquare\)

The predecessor states are

\[
(12,-1),
\qquad
(10,2047),
\]

with

\[
2047=-1+2^{11}.
\]

---

## 7. What the gap-\(6\) data says

Gap-\(6\) mergers use the same collision shells:

- \(470\) of \(505\) observed gap-\(6\) mergers use \(|E-F|=2\);
- \(28\) use \(|E-F|=4\);
- \(7\) use \(|E-F|=6\).

No comparably shallow, broad residue family was found in the tested range.
The first observed gap-\(6\) merger by large-tail step occurs at \(n=6723\),
step \(4\), on the \(|E-F|=4\) shell.

This is a useful distinction: the local collision law is uniform across
gaps, but reaching the shell becomes less rigid as the exponent gap grows.

---

## 8. Strategic consequence

The merger programme now separates into two problems:

1. **Local collision:** completely characterized by the collision shells.
2. **Shell hitting:** prove that a large repunit start reaches one of these
   shells against a smaller tail before descent.

The first problem is solved algebraically. The second remains the substantive
inductive target.

The explicit gap-\(2\) and gap-\(4\) families show that shell hitting can be
forced by exponent congruences. The step-\(2\) and step-\(3\) gap-\(2\)
families already form the first levels of a synchronization residue tree.

The next diagnostic should extend that tree by:

1. classifying all gap-\(2\) shell hits at step \(4\);
2. measuring the new residue mass after removing the proved earlier levels;
3. determining whether the uncovered odd residue mass shrinks geometrically;
4. performing the same construction for gap \(4\), then gap \(6\).

---

## 9. Reproduction

```bash
python explore_repunit_gap_mergers.py --limit 10001
python verify_repunit_gap_mergers.py
```
