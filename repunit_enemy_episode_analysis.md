# Enemy-Episode Analysis for Primitive Repunit Tails

**Building on:** `repunit_baker_applicability_census.md`,
`repunit_affine_tail_bound.md`, `repunit_tail_merge_reduction.md`
**Status:** Exact episode identities and finite diagnostics. The proposed
terminal-payout dichotomy is refuted by the finite data.
**License:** CC-BY 4.0

---

## 1. Definition

Let

\[
e_i=v_2(3x_i+1).
\]

An **enemy episode** begins at a maximal run

\[
e_s=e_{s+1}=\cdots=e_{s+L-1}=1
\]

and includes its terminating valuation

\[
q=e_{s+L}>1.
\]

The enemy coordinate \((m,d)\) from
`repunit_baker_applicability_census.md` remains fixed through the \(L\)
valuation-one transitions.

The complete \(L+1\)-step episode has raw valuation surplus

\[
\boxed{
\Delta S=L+q-(L+1)\log_2 3.
}
\]

Thus the terminal payout repairs the one-run deficit exactly when

\[
q\ge
\left\lceil (L+1)\log_2 3-L\right\rceil.
\]

This is an exact arithmetic test; it does not depend on an asymptotic
approximation.

---

## 2. Proposed dichotomy and outcome

The motivating candidate was:

> Every high-height persistent enemy episode either earns enough terminal
> valuation to repair its deficit, or exits into an enemy coordinate already
> controlled by a smaller exponent.

`explore_repunit_enemy_episodes.py` refutes this as a universal local model.

For the \(215\) primitive tails through odd \(n\le10001\), including all
terminated one-runs of length \(L\ge1\):

| quantity | count |
|---|---:|
| terminated episodes | 219,850 |
| Case B episodes with entry height ratio at least \(0.75\) | 219,847 |
| terminal payout repairs the episode | 92,168 |
| exit enemy coordinate occurred on a smaller primitive tail | 51 |
| terminal repair or prior exit coordinate | 92,195 |

Thus the proposed alternatives cover only

\[
\frac{92{,}195}{219{,}847}\approx41.94\%
\]

of Case B episodes.

For persistent runs of length \(L\ge2\), terminal repair falls further to
\(34.60\%\), while prior-coordinate exits occur in only \(21\) of
\(110{,}628\) Case B episodes.

The terminal payout therefore behaves as an ordinary local valuation, not as
a forced compensation for the preceding run.

---

## 3. Long episodes and delayed recovery

The longest observed episode through \(n\le10001\) occurs on \(n=7477\):

\[
L=21,\qquad q=2,
\]

with raw episode surplus

\[
\Delta S
=23-22\log_2 3
\approx-11.869175.
\]

It recovers its local deficit after \(36\) transitions from the episode
start, fourteen transitions after the terminal payout.

The slowest observed recovery begins on \(n=2449\) with

\[
L=1,\qquad q=2.
\]

Although its immediate deficit is only about \(-0.169925\), local surplus
does not become nonnegative until \(129\) transitions after the episode
start.

Restricting to \(L\ge2\), the maximum observed recovery time is \(127\)
transitions. The largest observed ratio of recovery time to episode length
\(L+1\) is:

\[
64.5\quad(L\ge1),
\qquad
39.667\quad(L\ge2).
\]

Hence no bound of the form \(O(L)\) is supported by the data.

---

## 4. Why eventual recovery is not a new theorem

Every sampled episode eventually recovers its local raw surplus before first
descent. This is not independent evidence for a short recovery theorem.

Suppose an episode begins at state \(x_s\), before first descent below
\(T=2^n-1\). Then

\[
x_s\ge T>x_{\sigma_n}.
\]

Over \(t=\sigma_n-s\) odd steps, positivity of every affine correction gives

\[
x_{\sigma_n}
>
\frac{3^t x_s}{2^{E_{\sigma_n}-E_s}}.
\]

Since \(x_{\sigma_n}<x_s\), it follows that

\[
E_{\sigma_n}-E_s-t\log_2 3>0.
\]

Thus every local deficit beginning before first descent must recover by first
descent. Using this fact to prove a bound on \(\sigma_n\) would be circular.

The meaningful target would need an independently bounded recovery window.
The finite data rules out a window controlled only by the one-run length.

---

## 5. Strategic assessment

Enemy episodes remain useful for:

- identifying the precise Case B obstruction;
- measuring where cumulative surplus is lost;
- testing proposed adaptive blocks;
- separating Baker-applicable low-height runs from generic high-height runs.

They should not be the primary proof architecture. The data gives no local
terminal-compensation law, and enemy-coordinate recurrence is too rare.

The strongest current architecture is:

1. **Merge first.** Use exact diagonal-state coalescence to remove the large
   majority of tails by strong induction.
2. **Restrict surplus work to primitive tails.** These are \(215\) of \(4998\)
   tested exponents through \(n\le10001\).
3. **Use Baker selectively.** Eliminate exceptional low-height enemy
   families, but do not ask Baker to control generic Case B.
4. **Seek adaptive cumulative blocks, not one-run episodes.** A useful block
   must produce a positive surplus record within a window bounded
   independently of the unknown first-descent time.
5. **Exploit high-height structure through merger.** The next concrete target
   is to derive exact local conditions forcing the common gap-\(2\),
   gap-\(4\), and gap-\(6\) diagonal mergers.

This is a more credible division of labour:

- Baker handles structured low-height branches;
- merger handles repeated arithmetic states;
- cumulative surplus handles the residual primitive dynamics.

---

## 6. Reproduction

```bash
python explore_repunit_enemy_episodes.py --limit 10001 --min-run 1
python explore_repunit_enemy_episodes.py --limit 10001 --min-run 2
```
