# Canonical notation

This file defines the notation used by the proved-results track. A note that
uses a different convention must say so explicitly.

## Maps

For a positive integer \(n\), the ordinary Collatz map is

\[
C(n)=
\begin{cases}
n/2,&n\text{ even},\\
3n+1,&n\text{ odd}.
\end{cases}
\]

For odd \(x\), the accelerated odd-step map is

\[
f(x)=\frac{3x+1}{2^{v_2(3x+1)}}.
\]

Unless a document explicitly says otherwise, an **odd-step** means one
application of \(f\), not one application of \(C\).

## Valuations and stopping time

- \(v_2(m)\): the exponent of the highest power of \(2\) dividing nonzero
  \(m\).
- \(\tau(x)=v_2(x+1)\) for odd \(x\): the number of trailing \(1\)-bits.
- \(x_i=f^{(i)}(x)\).
- \(e_i=v_2(3x_i+1)\).
- \(E_0=0\) and \(E_K=\sum_{i=0}^{K-1}e_i\).
- \(\sigma(x)=\min\{K\ge1:f^{(K)}(x)<x\}\), when this minimum exists.

## Special families

- \(M_n=2^n-1\): a Mersenne number.
- \(a_n=(3^n-1)/2=1+3+\cdots+3^{n-1}\): a base-\(3\) repunit.

## Claim-status vocabulary

Every maintained note should use one of these labels:

1. **Proved here** — a complete proof is given in the repository.
2. **Known theorem rederived** — a proof is supplied, but the theorem is
   attributed to prior literature.
3. **Finite certificate** — exhaustive only over an explicitly bounded set.
4. **Conditional result** — proved assuming named hypotheses.
5. **Conjecture / proof target** — open.
6. **Exploratory / retired** — intuition or experiments, not part of the
   theorem dependency chain.

A verifier supports a proof or certificate; passing a finite or randomized
test is not, by itself, a proof of a universally quantified statement.
