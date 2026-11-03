# FD: How Often Must a Local Potential Fail?

**Building on:** SH1 (`shadow_certificate.md`), RATCYC1 / QLG2 (manuscript
§7), the Terras parity-word bijection.
**Status:** Proved here (manuscript §8, Theorem G and Proposition 8.8).
Machine-checked in `scripts/verify_failure_density.py` (exact arithmetic;
\(\log_23\) carried as a formal symbol). **Not human-reviewed.**
**Ledger:** FD1, FD2, FD3
**License:** CC-BY 4.0

---

## 1. The question

Every no-go theorem in the repository says that a potential
\(\Phi_g(x)=\log_2x+g(\text{local data})\) increases somewhere. This note
asks how rarely it can be made to increase. Fix the depth \(m\) and let

\[
F(g)=\{x\ \text{odd},\ x>1:\ \Phi_g(f(x))>\Phi_g(x)\},\qquad
\Phi_g(x)=\log_2x+g(x\bmod2^{m}),
\]

with \(g\) an arbitrary real function on the odd residues. Let \(\delta_m\)
be the infimum over \(g\) of the lower natural density of \(F(g)\) among the
odd integers.

Write \(\theta=1/\log_23=0.6309\ldots\), \(H\) for binary entropy, and

\[
c=1-H(\theta)=0.05004\ldots
\]

## 2. Theorem (FD1 + FD2; manuscript Theorem G)

For \(m\ge12\):

1. **(FD1, lower bound.)** For every \(g\), \(F(g)\) contains a union of
   residue classes of odd integers of density at least
   \(2^{-cm}/\bigl(16(m+2)^{5}\bigr)\).
2. **(FD2, upper bound.)** There is a \(g\) for which \(F(g)\) is contained in
   a set of natural density at most \(4\cdot2^{-cm}\) together with a finite
   set.

Hence \(2^{-cm}/(16(m+2)^5)\le\delta_m\le4\cdot2^{-cm}\) and
\(\frac1m\log_2\delta_m\to-c\).

**(FD3, local coordinates.)** The lower bound persists, with the constant
halved and for \(m\) large in terms of \(|E|\), for corrections
\(g(\alpha(x),x\bmod2^m)\) where \(\alpha\) is constant on classes modulo
\(2^m\) except on the classes of a finite set \(E\subset\mathbb Z_2\). The
fuel \(\tau\) (\(E=\{-1\}\)) and the detectors \(\lambda_d\)
(\(E\ni t_d=1-2^{2d+1}3^{-d}\)) are of this kind, so
\(g(x\bmod2^m,\tau,\lambda_1,\dots,\lambda_D)\) has the same failure
exponent.

## 3. Proof outline (full proof in manuscript §8)

**Lower bound.** Let \(P=m+1\). Every cyclic binary word \(w\) of length
\(P\) with more than \(\theta P\) letters \(\mathtt O\) is *expanding*
(\(3^{\#\mathtt O}>2^P\)) and is the parity word of a rational 2-adic cycle
(RATCYC1). For each of its odd members \(y_i\), the class
\(A_i=\{x\equiv y_i \bmod 2^{m+e_i}\}\) realises one edge of a closed walk in
the coordinate graph; the \(K\) monotonicity constraints along the walk sum
to \(0\le-(K\log_23-P)<0\), so one \(A_{i(w)}\) lies entirely in \(F(g)\).
The windows of length \(\ge P\) that define these classes contain a full
period, so distinct cyclic words give disjoint classes. Counting the
expanding cyclic words without long \(\mathtt E\)-runs by the entropy bound
gives \(\ge2^{PH(\theta)}/(8P(P+1))\) classes, each of density
\(\ge2^{-m}/(2P^{3})\).

**Upper bound.** With \(\gamma(\mathtt O)=\log_23-1\), \(\gamma(\mathtt E)=-1\)
and \(h(r)=\sum_{l<m}(1-\tfrac{l+1}{m})\gamma(p_l)\) on parity words,
\(\Psi(x)=\log_2x+h(x\bmod2^m)\) satisfies the exact identity

\[
\Psi(T(x))-\Psi(x)=\frac{k\log_23-m}{m}+[x\ \text{odd}]\log_2\Bigl(1+\frac1{3x}\Bigr),
\]

\(k\) the number of \(\mathtt O\) among the first \(m\) letters. Along \(f\)
the differences telescope over \(T\)-steps, so a failure needs a window with
\(k>\theta m\) somewhere in the block, an event of density
\(\le2\Pr[\mathrm{Bin}(m,\tfrac12)>\theta m-1]\le4\cdot2^{-cm}\), or one of
finitely many small \(x\).

## 4. Reading

The exponent is the large-deviation rate of "no descent within \(m\) parity
steps", the event behind Terras's stopping-time density. A local correction
with \(m\) bits of information can do no better than wait for the orbit to
descend, and plain lookahead already does exactly that. Theorems A–E locate
the failures; this theorem says the shadows of *all* expanding cycles are
needed to account for them, and that they do account for them.

## 5. Exact small-\(m\) data (from the verifier)

| \(m\) | expanding cyclic words of length \(m+1\) | lower-bound sum \(\mathrm{LB}_m\) | lookahead failure density |
|---|---|---|---|
| 8 | 16 | \(53/2048=2^{-5.27}\) | \(2^{-1.79}\) |
| 10 | 52 | \(271/16384=2^{-5.92}\) | — |
| 12 | 85 | \(459/65536=2^{-7.16}\) | — |
| 13 | 251 | \(2251/262144=2^{-6.86}\) | — |
| 16 | — | — | \(2^{-2.25}\) |
| 40 | — | — | \(2^{-3.63}\) |

The stated constants are far from tight at these sizes (the proof's
polynomial factors cost about \(2^{-17}\) at \(m=13\)); the content is the
exponent.

## 6. What is not done

- The exact value of \(\delta_m\) for small \(m\) (a minimum-measure
  feedback set for the positive cycles of the coordinate graph) has not been
  computed; the verifier only checks that explicit potentials respect the
  lower bound.
- Archimedean coordinates (bit length, the quantized logarithm) are not
  covered by FD1; the multi-witness cycles of QLG2 at every scale should
  give the same exponent for fixed precision (manuscript Remark 8.9(iii)).
- The general \((a,b,c)\) transfer is stated as a remark only.

## 7. Verification

```bash
python3 scripts/verify_failure_density.py    # ALL PASS, ~25 s
```

(T) Terras bijection to \(n=14\); (I) the lookahead identity as an exact
identity in the symbol \(\log_23\), all residues mod \(2^{m+1}\), \(m\le12\);
(U) exact lookahead failure density \(\le4\cdot2^{-cm}\) for \(8\le m\le40\)
and a direct exact check of every failure below \(2^{17}\) for
\(m=6,8,10\); (Lw) every expanding cyclic word of length \(m+1\), \(m\le13\):
cycle, edge classes, positive gain, distinct windows, and
\(\mathrm{LB}_m\ge2^{-cm}/(16(m+2)^5)\) for \(m=12,13\); (A) six explicit
potentials at \(m=6,8\) fail on at least \(\mathrm{LB}_m\).

## 8. Ledger rows

| ID | Claim | Status | Source | Verification |
|---|---|---|---|---|
| FD1 | For every \(m\ge12\) and every \(g\), the failure set of \(\log_2x+g(x\bmod2^m)\) contains a union of odd residue classes of density \(\ge2^{-cm}/(16(m+2)^5)\), \(c=1-H(1/\log_23)=0.0500\ldots\): one shadow class per expanding cyclic parity word of length \(m+1\), pairwise disjoint | Proved here (not human-reviewed) | manuscript §8, Theorem G(1); `docs/no-go/failure_density.md` | `scripts/verify_failure_density.py` (Lw), (A) |
| FD2 | The lookahead potential \(h(r)=\sum_{l<m}(1-\frac{l+1}m)\gamma(p_l)\) satisfies \(\Psi(Tx)-\Psi(x)=(k\log_23-m)/m+[x\text{ odd}]\varepsilon(x)\) exactly, and its failure set along \(f\) has density \(\le4\cdot2^{-cm}\) up to a finite set (\(m\ge8\)); hence \(\delta_m=2^{-cm+O(\log m)}\) | Proved here (not human-reviewed) | manuscript §8, Lemma (lookahead identity), Theorem G(2) | `scripts/verify_failure_density.py` (I), (U) |
| FD3 | FD1 persists (constant halved, \(m\ge m_0(|E|)\)) for \(g(\alpha(x),x\bmod2^m)\) with \(\alpha\) constant on classes mod \(2^m\) off a finite \(E\subset\mathbb Z_2\); \(\tau\) is \((m,\{-1\})\)-local and \(\lambda_d\) is \((m,\{t_d\})\)-local, so residues, fuel and detectors together have failure exponent \(c\) | Proved here (not human-reviewed) | manuscript §8, Lemma (local), Proposition (local coordinates) | detector locality identity checked numerically for \(d\le5\), \(s<40\) in the session; no separate script |
