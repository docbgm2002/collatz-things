# Nested Anchors and the All-Ones Escape Branch

**Status:** Exact reduction plus finite exploration. No universal stopping-time
bound is claimed.

## 1. Exact nested-anchor identity

There are two related identities, and the map convention matters.

For the shortcut map

\[
U(n)=
\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd},
\end{cases}
\]

suppose the first \(k\) steps from \(a\) contain \(\rho\) odd steps. Then

\[
\boxed{
U^k(a+2^k m)=U^k(a)+3^\rho m.
}
\]

The added multiple of \(2^k\) preserves all \(k\) parities, and each odd step
multiplies its coefficient by \(3\) while every step divides it by \(2\).
This is the clean identity motivating the nested-anchor construction.

It is not valid with the same exponent for the ordinary map whose odd step is
\(3n+1\). For example, the ordinary trajectory of \(5\) reaches \(1\) in five
steps, but \(37=5+2^5\) reaches \(7\), not \(4=1+3\), after five steps.

For the accelerated odd-only map \(f\), let the first \(j\) valuations be
\(e_0,\ldots,e_{j-1}\), with

\[
E=e_0+\cdots+e_{j-1}.
\]

To preserve the final valuation exactly, one additional low bit is needed.
Thus the first \(E+1\) low bits determine the complete accelerated valuation
prefix. Therefore, for every integer \(q\geq0\),

\[
\boxed{
f^{(j)}(x+2^{E+1}q)=f^{(j)}(x)+2\cdot3^j q.
}
\]

Adding another anchor layer fixes more low bits and concatenates another
parity or valuation prefix.

If \(f^{(j)}(x)<x\) and \(3^j<2^E\), the identity certifies descent for the
entire progression \(x+2^{E+1}q\):

\[
f^{(j)}(x+2^{E+1}q)
=f^{(j)}(x)+2\cdot3^j q
<x+2^{E+1}q.
\]

Using only modulus \(2^E\) is generally insufficient: the perturbation can
change the final exact valuation. This is the off-by-one boundary at which a
fixed residue certificate must branch.

## 2. The all-ones survivor is not a positive infinite branch

At every fixed depth \(K\), the residue

\[
r_K=2^K-1\pmod{2^K}
\]

survives the initial valuation-one burn. These residue classes are nested, but
their \(2\)-adic intersection is the integer \(-1\), not a positive integer.

Indeed, a fixed positive odd \(x\) satisfies

\[
x\equiv-1\pmod{2^K}
\]

exactly for \(K\leq v_2(x+1)\). Thus every positive integer leaves the
all-ones branch after finitely many refinements.

This matters strategically: the Mersenne residue at each depth rules out one
finite modulus covering all integers, but it does not rule out an adaptive
tree in which every positive branch is eventually discharged.

### Exact equivalence with stopping time

For the shortcut map, the adaptive anchor tree can be characterized exactly.
Let \(r\) be an odd representative modulo \(2^K\). After \(t\leq K\) steps
containing \(\rho_t\) odd steps,

\[
U^t(2^Kq+r)
=2^{K-t}3^{\rho_t}q+U^t(r).
\]

If \(U^t(r)<r\), the positive affine correction in the Collatz formula forces

\[
3^{\rho_t}<2^t.
\]

Consequently the whole residue class descends:

\[
U^t(2^Kq+r)<2^Kq+r
\qquad(q\geq0).
\]

Conversely, uniform descent includes the case \(q=0\), so it implies
\(U^t(r)<r\). Therefore:

\[
\boxed{
\text{the class }r\bmod 2^K\text{ is discharged by depth }K
\iff
\text{the representative }r\text{ has stopping time at most }K.
}
\]

Here \(r>1\); the class represented by \(1\) is accepted separately as the
strong-induction base.

This is both useful and limiting. The tree is a prefix-code organization of
stopping-time certificates, not an independent descent mechanism. A universal
proof still needs a theorem forcing every positive representative to acquire
a finite leaf.

## 3. What happens at the exit

Write the finite all-ones prefix as

\[
x=2^L m-1,\qquad m\ \text{odd}.
\]

Compressing its full burn and payout gives the exact fuse transition

\[
\Phi(x)=\operatorname{oddpart}(3^L m-1).
\]

A tempting induction would say that either \(\Phi(x)<x\), or its new odd
cofactor is smaller than \(m\). This fails immediately:

\[
7=2^3\cdot1-1
\quad\longmapsto\quad
13=2^1\cdot7-1.
\]

Both the value and the odd cofactor increase. The finite scan in
`scripts/explore_nested_anchor_escape.py` finds many such transitions. Hence the state
\((L,m)\) needs cumulative history; no lexicographic one-fuse descent is
available.

## 4. The sharpened proof target

The nested-anchor route reduces the conjecture to the following adaptive-tree
statement:

> Every positive branch acquires, after finitely many refinements, an
> accelerated valuation prefix of depth \(E+1\) whose affine image is below
> its starting affine class.

The all-ones branch itself is harmless in the limit. The unresolved issue is
uniform control of the finite exits \(2^L m-1\), particularly the Mersenne
cofactor \(m=1\), whose exit is the repunit

\[
\operatorname{oddpart}(3^L-1).
\]

The accompanying explorer measures the exact certificate depth required by
these Mersenne starts. A linear bound on that depth would be a genuinely useful
new theorem: it would give a quantitative escape rule for the extremal branch.

The shortcut-tree computation reaches \(95.55\%\) of odd classes at depth
\(22\). Its repeating discharge counts come from prefix leaves: a certificate
born at depth \(t\) has exactly \(2^{K-t}\) refinements at every later depth
\(K\). Thus the apparent self-similarity is exact, but by itself does not form
a finite-state automaton.

### A clean Mersenne target

For odd \(n\), let

\[
M_n=2^n-1
\]

and let \(\sigma_U(M_n)\) be its first strict descent time under the shortcut
map \(U\). Exact finite computation for every odd \(7\leq n\leq10001\) gives

\[
\sigma_U(M_n)<6n.
\]

The record ratio is

\[
\frac{\sigma_U(M_{23})}{23}
=\frac{137}{23}
\approx5.9565217.
\]

This suggests the sharper proof target

\[
\boxed{\sigma_U(2^n-1)<6n\quad\text{for every odd }n\geq7.}
\]

This remains a conjecture. Proving it would settle uniform linear escape for
the extremal all-ones/Mersenne branch, but not for all shortcut-tree branches.

The shortcut budget splits exactly. The Mersenne burn reaches \(a_n\) in
\(n+1\) shortcut steps. If

\[
H(n)=\min\{t:U^t(a_n)<2^n-1\},
\]

then

\[
\sigma_U(M_n)=n+1+H(n).
\]

Consequently the sharper integer-valued target is

\[
\boxed{H(n)\leq5n-2,}
\]

which implies \(\sigma_U(M_n)\leq6n-1<6n\). The finite record \(n=23\)
saturates this proposed tail allowance:

\[
H(23)=113=5\cdot23-2,
\qquad
\sigma_U(M_{23})=137=6\cdot23-1.
\]

An accelerated odd episode of valuation \(e=v_2(3x+1)\) consumes exactly
\(e\) shortcut steps, so \(H(n)\) is a cumulative valuation budget, truncated
at the particular division inside the final episode where the target is
crossed.

### Odd-density reduction

There is a useful sufficient condition for the \(5n-2\) tail budget. Suppose
the repunit tail has not descended during its first

\[
t=5n-2
\]

shortcut steps, and let \(\rho\) be the number of odd shortcut steps in that
prefix. Before descent every encountered value is at least
\(T=2^n-1\). Multiplying the exact odd-step ratios gives

\[
\frac{U^t(a_n)}{T}
\le
\frac{a_n}{T}
\frac{3^\rho}{2^t}
\left(1+\frac1{3T}\right)^\rho.
\]

For every odd \(n\ge9\),

\[
\rho\le\left\lfloor\frac{11n}{4}\right\rfloor
\quad\Longrightarrow\quad
\frac{U^t(a_n)}T<1.
\]

Here is a uniform proof for \(n\ge19\). First,

\[
\frac{a_n/T}{(3/2)^n}
=
\frac{1-3^{-n}}{2(1-2^{-n})}
<
\frac{64}{127}
\]

for \(n\ge7\). Also,

\[
\left(1+\frac1{3T}\right)^\rho
<
\exp\left(\frac{\rho}{3T}\right)
\le
\exp\left(\frac{99}{6132}\right)
\]

for \(n\ge9\), since \(\rho\le11n/4\) and
\(n/(2^n-1)\) decreases. Therefore

\[
\frac{U^t(a_n)}T
<
\frac{256}{127}
\exp\left(\frac{99}{6132}\right)
\left(
\frac{(3/2)3^{11/4}}{32}
\right)^n.
\]

For a wholly rational envelope, the base is less than
\(0.962=481/500\) (raise both sides to the fourth power),
\(256/127<2.016\), and

\[
\exp(99/6132)<\frac1{1-99/6132}<1.017.
\]

Thus at \(n=19\) the right-hand side is less than

\[
2.016\cdot1.017\cdot0.962^{19}<0.983<1,
\]

and it decreases thereafter. The cases \(n=9,11,13,15,17\) are checked
exactly with rational arithmetic in `scripts/explore_mersenne_shortcut_budget.py`.

Thus the Mersenne \(6n\) target reduces to an odd-density exclusion:

> A surviving repunit prefix of length \(5n-2\) would need more than
> \(\lfloor11n/4\rfloor\) odd positions.

Equivalently, it would need odd density asymptotically above \(55\%\), rather
than the neutral parity density \(50\%\). The remaining task is arithmetic:
exclude the repunit exponent from these high-odd-density survivor classes.

### Size of the exceptional residue set

For the shortcut map, parity words of length \(t\) are in bijection with
residue classes modulo \(2^t\). Hence the number of residue classes that could
survive the \(5n-2\) window is at most

\[
\sum_{r>\lfloor11n/4\rfloor}\binom{5n-2}{r}.
\]

Using the binary entropy bound

\[
\sum_{r\ge pt}\binom tr\le2^{tH_2(p)}
\qquad(p>1/2),
\]

and \(p\to11/20=0.55\), the possible-survivor density is

\[
2^{-\,\left(5(1-H_2(0.55))+o(1)\right)n}
=
2^{-(0.0361277\ldots+o(1))n}.
\]

Thus the bad residue set is exponentially thin. This still does not exclude
the explicit repunit sequence: a sparse algebraic sequence can lie in sparse
residue classes. The exact remaining statement is a non-concentration theorem
for

\[
a_n=\frac{3^n-1}{2}
\]

against this particular high-odd-density prefix code.

## 5. Verification

```bash
python scripts/explore_nested_anchor_escape.py
python scripts/explore_shortcut_anchor_tree.py
python scripts/explore_mersenne_shortcut_budget.py
python scripts/verify_nested_anchor_work.py
```

The script verifies the affine lifting identity, checks the all-ones
intersection claim on samples, prints counterexamples to simple fuse orders,
and reports finite Mersenne certificate-depth records. The shortcut-tree
explorer verifies the original \(2^k\)-anchor identity directly and measures
its finite residue coverage.
