# EPOCH: the epoch map, the 2–3 transform of words, and bias propagation

**Status:** EPOCH1 is an exact identity (proved below, machine-checked).
EPOCH2 is a finite sampling diagnostic. §4 is a research hypothesis, not a
claim. Script: `scripts/explore_epoch_bias.py`.
**License:** CC-BY 4.0

---

## 1. The epoch map

For \(x\ge1\) with bit length \(\ell=\ell(x)\) define the *epoch map*
\(\Phi(x)=T^{\ell}(x)\): apply \(T\) exactly as many times as \(x\) has bits.
By Terras, the first \(\ell\) letters of the parity word of \(x\) are
determined by \(x\bmod2^{\ell}\), i.e.\ by \(x\) itself; so an epoch consumes
exactly the information \(x\) carries.

**EPOCH1 (identity).** Let \(w\) be the parity word of \(x\) of length
\(\ell\), \(k\) its number of odd letters, and
\(c(w)=\sum_{i<k}3^{k-1-i}2^{E_i}\) with \(E_i\) the position of the \(i\)-th
odd letter. Then
\[
\Phi(x)=\frac{3^{k}x+c(w)}{2^{\ell}},\qquad
\frac{3^{k}}{2}\le\Phi(x)<\frac{3\cdot3^{k}}{2},\qquad
\Phi(x)\equiv c(w)\,2^{-\ell}\pmod{3^{k}} .
\]
Consequently \(\Phi(x)\in\{\rho(w),\ \rho(w)+3^{k}\}\), where \(\rho(w)\) is the
least nonnegative residue of \(c(w)2^{-\ell}\) modulo \(3^{k}\): **the next
epoch's integer is determined by the parity word of the current one up to a
single bit.** Descent in an epoch (\(\Phi(x)<x\)) holds iff
\(3^{k}+c/x<2^{\ell}\), essentially iff \(k/\ell<1/\log_23=0.631\).

*Proof.* The first is the usual unrolling of \(\ell\) steps of \(T\); the
bounds follow from \(2^{\ell-1}\le x<2^{\ell}\) and \(0\le c(w)<3^{k}2^{\ell}/2\);
the congruence from \(2^{\ell}\Phi(x)=3^{k}x+c(w)\). \(\square\)

Checked exactly on \(2000\) random \(x\) of \(8\)–\(59\) bits in the script.

**Reading.** The dynamics is the alternation
\[
\text{binary word }w\ \longrightarrow\ \text{residue }\rho(w)\bmod3^{k}\ \longrightarrow\ \text{binary word of }\rho(w)\ (\text{or }\rho(w)+3^{k})\ \longrightarrow\cdots
\]
A typical word has \(k/\ell\approx\tfrac12<0.631\) and then
\(\Phi(x)\approx x^{0.79}\). The orbit of \(x\) fails to reach small values
only if a positive fraction of its epochs have \(k/\ell\ge0.631\).

## 2. The memoryless hypothesis

Let \(B=\{x:\Phi(x)\ge x\}\) (no descent in one epoch) and
\(p(L)=\Pr[x\in B\mid\ell(x)=L]\). By the Terras bijection,
\(p(L)=\Pr[\mathrm{Bin}(L,\tfrac12)>L/\log_23]\) up to the boundary term, i.e.\
\(p(L)=2^{-cL+o(L)}\) with \(c=1-H(1/\log_23)=0.0500\) (the exponent of
manuscript Theorem G).

**Hypothesis (2–3 memorylessness).** Conditional on the length of
\(\Phi(x)\), the event \(\Phi(x)\in B\) is independent of \(x\in B\), and more
generally the bias \(k/\ell-\theta\) of consecutive epochs is uncorrelated,
except along the shadows of rational cycles, where bias persists for a
bounded number of epochs (manuscript Theorems A, E, F).

This is the arithmetic form of the \(2\)–\(3\) independence philosophy
(Furstenberg): the binary digits of a \(3\)-adically defined residue carry
no memory of the binary structure that produced it. If it held with no
exceptions beyond bounded shadows, the \(3x+1\) conjecture would follow
(no integer could pass the \(0.631\) test in a positive fraction of epochs
forever). It cannot be proved with current tools: it contains the base-2
normality of base-3-defined numbers, where the best known results
(Stewart) are logarithmic.

## 3. The experiment (EPOCH2)

`scripts/explore_epoch_bias.py --l 32 --n 4000000` and
`--importance --l 32 --n 6000000 --J 6` (Terras inversion gives uniform
samples of \(B\) at a fixed length):

- Correlation of consecutive epoch biases \(k/\ell-\theta\): \(r=+0.0017\)
  on \(2\times10^{5}\) random \(32\)-bit integers; the mean output bias is
  \(-0.1306\) in every input-bias bin.
- Chains \(x_0\in B\), \(x_{j+1}=\Phi(x_j)\), with \(6\times10^{6}\) uniform
  samples of \(B\) at \(32\) bits:

| \(j\) | tested | mean length | observed \(\Pr[x_j\in B\mid x_0..x_{j-1}\in B]\) | length-matched independent prediction | ratio |
|---|---|---|---|---|---|
| 1 | 5 999 680 | 34.5 | \(0.06380\pm0.00010\) | 0.06389 | 0.999 |
| 2 | 382 751 | 36.2 | \(0.06004\pm0.00038\) | 0.05958 | 1.008 |
| 3 | 22 979 | 38.0 | \(0.05583\pm0.00151\) | 0.05663 | 0.986 |
| 4 | 1 283 | 39.5 | \(0.0585\pm0.0066\) | 0.05403 | 1.08 |
| 5 | 75 | 41.3 | \(0.040\pm0.023\) | 0.05244 | 0.76 |

Through four epochs the chain is memoryless given length to within sampling
error. The small rise in \(j=4\) is one standard error. Each further epoch
costs a factor of about \(16\) in samples.

Note the baseline \(p(L)\) oscillates with \(L\bmod4\) (e.g.\ \(p(28)=0.094\),
\(p(32)=0.055\), \(p(36)=0.066\)): the threshold \(k^{*}=\lceil L/\log_23\rceil\)
is a Diophantine function of \(L\), the same continued-fraction effect as in
the cost law of manuscript §7.

## 4. What could be done with this

1. **Approximate fixed points.** Search, over structured families (not
   random sampling), for words whose image word is at least as biased:
   the only known such families are the cycle shadows and the Mersenne
   burn. A new family would be a serious finding either way.
2. **Exponents of the \(j\)-fold sets.** \(B_j=\{x:x,\Phi(x),\dots,\Phi^{j-1}(x)\in B\}\)
   should have counting exponent \(1-c_j\) with \(c_j\to\infty\) under the
   hypothesis; a stabilising \(c_j\) would be evidence for divergent orbits.
3. **A restricted theorem.** For words \(w\) in a class where \(\rho(w)\) is
   explicitly invertible (e.g.\ words with a single block structure), prove
   that the image word has \(k'/\ell'<\theta\) outside the shadow families.
   This is the natural successor of the Mersenne-spine notes, which treated
   one such family.

## 5. Search for structured multi-epoch survivors (2026-11-04)

`scripts/explore_epoch_survivors.py` and further runs of
`scripts/explore_epoch_bias.py`. The question: is there any family of
integers, beyond the shadows of rational cycles, that survives several
epochs more often than chance?

**Bit-budget bound.** A shadow of a rational cycle at depth \(m\le\ell\)
follows it for at most \(m\) \(T\)-steps, since each step consumes at least
one bit of agreement. An \(\ell\)-bit integer therefore cannot shadow any
cycle for more than one epoch; multi-epoch survival is never a cycle shadow.

**Structured probes.**
- Periodic words (= rational-cycle shadows), all 157 expanding primitive
  words of length \(\le9\), shadows up to 64 bits: 115 survive one epoch, 35
  two, 4 three; the only "five-epoch" cases are the integers 27 and 55, a
  small-number effect. As predicted, the second epoch of a shadow is the
  binary expansion of \(3^k\) minus a small number, and it is generic.
- Epoch-fixed points \(\Phi(x)\equiv x\pmod{2^{\ell(x)}}\) below \(2^{20}\):
  two (2151 and 3227), each surviving exactly two epochs.
- Sturmian words with slope in \((\theta,1)\): survival counts 181/13/1 for
  one/two/three epochs, the chance rate.

**Census of all \(x<2^{26}\).** Survivors by number of epochs:
515 077, 44 109, 4 058, 354, 37, 0 for \(j=2,\dots,7\). The champions
(six epochs) fall into three orbit families (\(1501353\) with \(2x,4x,8x\)
and merging neighbours; \(4003609\); \(5338145\)), all random-looking in
binary. Members of a family share one chain after the first epoch, so the
raw counts are clumpy; the family-collapsed counts behave like independent
coins.

**A finite-size deviation.** Against the length-matched independent
prediction, the probability that a survivor's image survives again is

| start length | stage 1 | stage 2 | stage 3 | stage 4 |
|---|---|---|---|---|
| 26 bits (4M samples of \(B\), baseline \(2\times10^5\)/length) | 1.000 | \(1.045\pm0.007\) | \(1.18\pm0.025\) | \(0.93\pm0.08\) |
| 32 bits (6M) | 0.999 | 1.008 | 0.986 | \(1.08\pm0.12\) |
| 40 bits (6M) | 0.985 | 0.991 | 1.021 | \(1.35\pm0.30\) |

So at 26–31 bits there is a real few-percent excess at the second and third
stage, not explained by the dyadic position of the image or its residue
modulo \(9\) (both were conditioned on in the census), with a per-length
structure at the third stage (excess for images of 29–34 bits, deficit at
35–38), and it is gone by 32–40 bits. It is a small-number correction to
the memoryless model, not a structured family and not long-range memory;
its mechanism is not identified (the carry term \(c/x\) in the exact
non-descent condition is the natural suspect, since it is relatively larger
for short integers).

**Conclusion.** No structured family survives more than chance beyond the
bounded shadows of rational cycles. The independent-miracles model holds
to within sampling error from 32 bits upward through four epochs, with
finite-size deviations of a few percent below 32 bits. This is the state of
the evidence for the hypothesis of §2, and it is evidence only.

## 6. Ledger rows

| ID | Claim | Status | Source | Verification |
|---|---|---|---|---|
| EPOCH1 | For \(\Phi(x)=T^{\ell(x)}(x)\): \(\Phi(x)=(3^kx+c(w))/2^{\ell}\in[3^k/2,\,3\cdot3^k/2)\) and \(\Phi(x)\equiv c(w)2^{-\ell}\pmod{3^k}\), so \(\Phi(x)\in\{\rho(w),\rho(w)+3^k\}\) is determined by the parity word \(w\) of \(x\) up to one bit | Proved here | `docs/no-go/epoch_transform.md` §1 | `scripts/explore_epoch_bias.py` (exact check on 2000 random \(x\)) |
| EPOCH2 | Bias propagation across epochs is memoryless given length through four epochs at \(32\) and \(40\) bits (ratios \(0.999,1.008,0.986,1.08\) and \(0.985,0.991,1.021\)); at \(26\) bits a finite-size excess of \(4.5\%\) and \(18\%\) at stages 2–3. No structured family (periodic words, epoch-fixed points, Sturmian words, census champions below \(2^{26}\)) survives beyond chance; cycle shadows cannot last more than one epoch by the bit budget | Finite diagnostic (sampling + census) | `docs/no-go/epoch_transform.md` §3, §5 | `scripts/explore_epoch_bias.py`, `scripts/explore_epoch_survivors.py`; not a universal claim |
