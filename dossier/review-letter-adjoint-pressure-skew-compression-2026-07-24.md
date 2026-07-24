# Independent review request: skew Oseen compression and pressure depth

**Date:** 2026-07-24

Please review
[`experiments/adjoint-pressure-skew-compression.md`](experiments/adjoint-pressure-skew-compression.md)
as a proposed structural reduction on `ROUTE-R3B`.

The preceding independently reviewed result is
[`experiments/adjoint-pressure-critical-volterra.md`](experiments/adjoint-pressure-critical-volterra.md).
It excluded critical causality and positive norm majorants as sufficient
sources of infinite-depth decay.  The new note restores the orthogonal
Leray split and skew transport algebra.

## Claimed scope

The note claims only that the following abstract inputs are still
insufficient:

1. \(B_b=b\cdot\nabla\) is skew in vector \(L^2\);
2. \(P=\mathbb P\) and \(Q=I-P\) form an orthogonal Hodge split;
3. the projected drift is \(A_b=PB_bP\);
4. the pressure observation is \(C_b=QB_bP\);
5. critical causal time ordering is represented by the already reviewed
   normalised Hardy--Volterra operator;
6. the real coupling family is energy-stable; and
7. a unitary one-step dilation supplies a squared projection-defect
   telescope.

It does **not** claim that the finite-dimensional model is an Oseen or
Navier--Stokes realisation.  In particular, it does not encode the
componentwise spatial transport/heat relation, the Navier--Stokes evolution
of \(b\), or the strong zero right trace of the actual feedback remainder.

## Requested checks

### 1. PDE pressure identity

For smooth divergence-free \(b,z\), is

\[
Q(b\cdot\nabla z)
=
Q(z\cdot\nabla b)
=
\mathcal T(z,b)
\]

correct with the repository's tensor convention?

### 2. Compression algebra

With \(A= PBP\), \(C=QBP\), and \(B^*=-B\), please check

\[
A^*=-A,
\qquad
PB^2P=A^2-C^*C,
\qquad
-PB^2P=A^*A+C^*C.
\]

In particular, does the last identity fail to telescope over \(A^m\) for
the reason stated?

### 3. Exact countermodel

Please recompute

\[
B=
\begin{pmatrix}
0&-1&-1\\
1&0&-1\\
1&1&0
\end{pmatrix},
\quad
A=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix},
\quad
C=
\begin{pmatrix}
1&1
\end{pmatrix}.
\]

For \(q=-(e_1+e_2)\), \(r=e_1\), and
\(\mathbb T=\mathsf H_\gamma\otimes A\), check

\[
r=\mathbb T(q+r),
\qquad
|\mathbb C\mathbb T^Nr|=1
\quad(N\ge0).
\]

Does the explicit caveat about the missing strong zero right trace make the
model's scope honest?

### 4. Coupling parameter

Please check the formula

\[
r_\lambda
=
\frac{\lambda}{1+\lambda^2}
\binom{1+\lambda}{\lambda-1},
\qquad
\|r_\lambda\|^2
=
\frac{2\lambda^2}{1+\lambda^2},
\]

and the conclusion that real-axis energy stability does not control the
Dyson coefficients at \(\lambda=1\).

### 5. Unitary leakage mismatch

For

\[
c_n=\frac{n^2-1}{n^2+1},
\qquad
s_n=\frac{2n}{n^2+1},
\]

please verify

\[
\sum_{m=0}^{n-1}|s_nc_n^m|
=n(1-c_n^n)\to2,
\]

whereas

\[
\sum_{m=0}^{n-1}|s_nc_n^m|^2
=1-c_n^{2n}\to0.
\]

Does this correctly show that the unitary energy-defect telescope has the
wrong summability index for the linear \(L^1\) pressure cost?

### 6. Same-trajectory identity and frontier

Please check the signs in

\[
\partial_\tau(a\cdot b)
=
\operatorname{div}
\left[
b(a\cdot b)
+\nu\sum_j(b_j\nabla a_j-a_j\nabla b_j)
-\pi_ab-p_ba
\right].
\]

Finally, is the stated surviving frontier exhaustive within the proposed
scope: a heat/spatial commutator estimate, a same-trajectory signed law, or
an actual event-ancestry relation?

## Adversarial questions

Please distinguish:

- a fatal algebraic or logical error;
- an overclaim about actual Oseen dynamics;
- a repairable precision issue; and
- a valid but narrow no-go theorem.

The Clay problem remains unsolved.  No regularity or breakdown alternative
is claimed.

## Supplemental strong-trace strengthening

After the first review identified the missing strong zero right trace as a
live distinction, the theorem was strengthened.  For \(\eta\ge0\), define

\[
\mu_{\gamma,\eta}
:=
\frac{B(\gamma,1-\gamma+\eta)}
     {B(\gamma,1-\gamma)},
\qquad
A_{\gamma,\eta}:=\mu_{\gamma,\eta}^{-1}
\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]

The revised claim is

\[
\mathsf H_\gamma(t^\eta)
=
\mu_{\gamma,\eta}t^\eta,
\]

and, for

\[
q_\eta(t)=-t^\eta(e_1+e_2),
\qquad
r_\eta(t)=t^\eta e_1,
\]

\[
r_\eta
=
(\mathsf H_\gamma\otimes A_{\gamma,\eta})(q_\eta+r_\eta),
\]

\[
\left|
C(\mathsf H_\gamma\otimes A_{\gamma,\eta})^Nr_\eta(t)
\right|
=t^\eta
\qquad(N\ge0).
\]

In particular, \(\eta=1\) gives
\(\mu_{\gamma,1}=1-\gamma\) and a genuine linear strong zero right trace.
Please additionally check:

1. the beta ratio and reciprocal-compression algebra;
2. that the displayed \(3\times3\) completion remains skew;
3. the feedback and residual indexing;
4. whether this now closes **trace order alone** while honestly leaving the
   actual heat-linked spatial Oseen structure open.

## Reproduce

```bash
make adjoint-pressure-skew-compression
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_skew_compression -v
make check
```
