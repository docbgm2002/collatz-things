# Fuse Map Theory: What Would a Proof Need?

**Status:** theoretical reduction; not a proof

This note tries to push the fuse-burn attack without relying on computation as
the argument. The goal is to understand whether the improved battlefield gives
an actual contradiction mechanism.

---

## 1. The global fuse map

For every odd integer `x > 1`, write

$$
x = 2^L m - 1,
\qquad
L = v_2(x+1),
\qquad
m \text{ odd}.
$$

Define the accelerated **fuse map**

$$
\Phi(x)=\operatorname{oddpart}(3^L m - 1).
$$

Equivalently, let

$$
s = v_2(3^L m - 1),
\qquad
u = \frac{3^L m - 1}{2^s}.
$$

Then

$$
\Phi(x)=u.
$$

This compresses one full trailing-one episode: the suffix of `L` ones burns
down, then the first nontrivial payout division is taken.

The original Collatz conjecture is equivalent to:

> For every odd `x > 1`, some iterate of `\Phi` falls below `x`.

This is not a shortcut proof. It is a change of coordinates that isolates the
two quantities that matter:

- `L`: available trailing-one fuel,
- `s`: payout valuation after the fuel burns.

---

## 2. Multiplicative ledger

The exact transition is

$$
x = 2^L m - 1
\quad\mapsto\quad
x'=\frac{3^L m - 1}{2^s}.
$$

Ignoring the harmless `-1` terms, the macro multiplier is approximately

$$
\frac{x'}{x}
\approx
\frac{3^L}{2^{L+s}}
=2^{L\log_2(3/2)-s}.
$$

Thus a single fuse episode is safely descending when

$$
s \gtrsim L\log_2(3/2).
$$

Since

$$
\log_2(3/2)\approx 0.5849625,
$$

large `L` can tolerate only small payout valuations before it grows.

This explains why long fuses are dangerous in the raw value ledger: the burn is
structurally exact, but if the payout valuation `s` is small, the episode can
grow by a factor close to `(3/2)^L`.

---

## 3. Recharge ledger

The next fuel length is

$$
K = v_2(x'+1)
  = v_2\!\left(\frac{3^L m - 1}{2^s}+1\right).
$$

Equivalently,

$$
3^L m - 1 = 2^s u,
\qquad
u \equiv -1 \pmod {2^K}.
$$

So producing next fuel at least `K` is equivalent to

$$
3^L m - 1 \equiv -2^s \pmod {2^{s+K}},
$$

or

$$
m \equiv 3^{-L}(1-2^s) \pmod {2^{s+K}}.
$$

Because `3` is invertible modulo every power of `2`, this is one exact residue
class modulo `2^{s+K}`.

This is the exact recharge cost:

> To have payout valuation `s` and next fuel at least `K`, the old odd cofactor
> `m` must land in one specified class modulo `2^{s+K}`.

---

## 4. Why rarity alone is not a proof

The tempting argument is:

> Long fuel is rare, so repeated long fuel should be impossible.

That is not enough. For every finite requested pattern of valuations, one can
often satisfy the corresponding congruences by choosing a sufficiently specific
starting residue. This is the usual trap in Collatz: finite low-bit patterns are
cheap to prescribe.

So the recharge congruence gives a density cost, but density cost alone does not
rule out one exceptional integer.

The proof must therefore show **incompatibility**, not merely rarity.

---

## 5. Pattern dynamics

A fuse-map orbit is described by a sequence

$$
(L_0,s_0), (L_1,s_1), (L_2,s_2), \dots
$$

where

$$
L_i = v_2(x_i+1),
\qquad
s_i = v_2(3^{L_i}m_i-1),
\qquad
x_{i+1}=\Phi(x_i).
$$

The value ledger over `N` fuse episodes is approximately

$$
\log_2\frac{x_N}{x_0}
\approx
\sum_{i=0}^{N-1}
\left(L_i\log_2(3/2)-s_i\right).
$$

Therefore descent follows if we can prove that every sufficiently long orbit
has

$$
\sum_{i<N} s_i
>
\log_2(3/2)\sum_{i<N} L_i
$$

up to bounded error.

This is the central inequality.

---

## 6. Why finite pattern exclusion is unlikely

There is an important obstruction to a simple congruence contradiction.

If a pattern

$$
(L_0,s_0,L_1),\ (L_1,s_1,L_2),\dots,\ (L_{N-1},s_{N-1},L_N)
$$

is prescribed, the cofactor recurrence is

$$
m_{i+1}
=
\frac{3^{L_i}m_i + (2^{s_i}-1)}
       {2^{s_i+L_{i+1}}}.
$$

Iterating gives an affine relation

$$
m_N
=
\frac{3^{L_0+\cdots+L_{N-1}}m_0 + C}
       {2^{\sum_{i<N}(s_i+L_{i+1})}},
$$

for an integer `C` determined by the pattern.

The coefficient of `m_0` is odd, hence invertible modulo every power of `2`.
Therefore, for many finite patterns, the integrality conditions specify a
single residue class for `m_0` modulo a large power of `2`; they do not
automatically contradict one another.

This is the central warning:

> Finite bad-looking valuation patterns may be rare, but rarity is not
> impossibility. A proof cannot rely only on ruling out finite patterns by
> congruence counting.

The contradiction, if it exists, must arise from either:

1. a cumulative value inequality that every admissible pattern eventually
   satisfies, or
2. an infinite 2-adic compatibility obstruction, not a finite one.

---

## 7. What Block-Fracture contributes

The Block-Fracture Lemma says long blocks of ones do not self-preserve under the
`3x` part of the map. In fuse-map language:

- `L_i` is real fuel, not a stable asset.
- A long `L_i` is consumed deterministically by the episode.
- A later long `L_{i+1}` must be newly created by the recharge congruence.

So Block-Fracture justifies treating high `L` as a **spent resource**. It does
not by itself bound future `L`; future `L` is exactly the recharge problem.

---

## 8. The viable proof target

The proof cannot be:

> Long fuses shrink.

They do shrink, but they may still produce a large value before the payout.

The proof also cannot be:

> Long recharges are rare.

They are rare in density, but finite rare patterns can still exist.

The proof-shaped target is:

> Any orbit that keeps the multiplicative ledger nonnegative must force an
> infinite sequence of recharge congruences whose combined requirements are
> incompatible with the cofactor recurrence.

Equivalently:

> Every sufficiently long admissible valuation pattern must satisfy
> $$
> \sum s_i
> \log_2(3/2)\sum L_i
> $$
> unless the orbit has already merged below its starting value.

This is now a precise theorem target.

---

## 9. Current obstruction

The remaining difficulty is serious: the fuse map still allows long finite
non-descending chains. For example, the earlier worst finite-window value
`626331` becomes a chain of `41` fuse episodes before dropping below its start.

This suggests there is no small local rule on `(L_i,s_i,L_{i+1})` that proves
descent. Any proof probably needs a cumulative inequality over a variable-length
block of fuse episodes.

The battlefield is improved, but the hard part is now clear:

> Prove a cumulative payout inequality for admissible fuse-map valuation
> sequences.

---

## 10. The Mersenne spine obstruction

The sharpest enemy case is the pure Mersenne cofactor `m=1`:

$$
x = 2^L - 1.
$$

Then

$$
\Phi(x)=\operatorname{oddpart}(3^L-1).
$$

By LTE,

$$
v_2(3^L-1)
=
\begin{cases}
1, & L \text{ odd},\\
2+v_2(L), & L \text{ even},
\end{cases}
$$

so the payout valuation is only logarithmic in `L` on even `L`, and constant
on odd `L`. Meanwhile the growth term is exponential in `L`:

$$
\frac{\Phi(2^L-1)}{2^L-1}
\approx
\frac{(3/2)^L}{2^{v_2(3^L-1)}}.
$$

Thus large Mersenne states are not dispatched by the fuse-map payout. They are
the cleanest form of the obstruction.

This does not contradict the Block-Fracture Lemma. Block-Fracture says the run
of ones erodes structurally; it does not say the value immediately falls. In
fact, the Mersenne spine shows exactly why structural erosion and numerical
descent are different.

Any successful proof along this route must therefore include a separate
Mersenne-spine theorem:

> Starting from `2^L-1`, the sequence of fuse-map episodes has cumulative payout
> large enough to overcome the initial huge growth.

The Rail-7 Mersenne alternation is one small part of this spine, but not the
whole theorem.

The first Mersenne step is exactly tractable. Let

$$
x_0 = 2^L-1,
\qquad
x_1 = \Phi(x_0)=\operatorname{oddpart}(3^L-1).
$$

Then

$$
s_0=v_2(3^L-1)
=
\begin{cases}
1, & L \text{ odd},\\
2+v_2(L), & L \text{ even}.
\end{cases}
$$

If `L` is odd, then

$$
x_1=\frac{3^L-1}{2},
\qquad
x_1+1=\frac{3^L+1}{2}.
$$

By LTE,

$$
v_2(3^L+1)=v_2(3+1)+v_2(L)=2,
$$

so

$$
v_2(x_1+1)=1.
$$

Thus odd Mersenne exponents always enter the low-fuel state immediately:

$$
L \text{ odd} \quad\Longrightarrow\quad (L,s_0,L_1)=(L,1,1).
$$

For even `L`, the first payout is also explicit, but the next fuel

$$
v_2\left(\frac{3^L-1}{2^{2+v_2(L)}}+1\right)
$$

does not collapse to a simple function of `v_2(L)`. This is visible in the
Mersenne-spine explorer: even exponents with the same `v_2(L)` can produce
different next fuel lengths. The Mersenne spine is therefore not solved by LTE
alone.
