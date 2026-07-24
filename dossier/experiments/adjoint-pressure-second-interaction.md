# A terminal feedback packet requires at least two causal drift interactions

- **Experiment:** EXP-ADJOINT-PRESSURE-SECOND-INTERACTION-001
- **Route:** ROUTE-R3B
- **Status:** conditional analytic reduction;
  [independently reviewed valid in scope](../review-response-adjoint-pressure-second-interaction-2026-07-24.md)
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** independently reviewed
  [direct-response decomposition](adjoint-pressure-direct-response.md),
  [feedback-tail theorem](adjoint-pressure-feedback-tail.md),
  [feedback-shell theorem](adjoint-pressure-feedback-shells.md), and
  [intermediate-localisation theorem](adjoint-pressure-intermediate-localization.md)

The selected zero-data feedback remainder satisfies

\[
\partial_\tau r-\nu\Delta r-\mathbb P(b\cdot\nabla r)
=
\mathbb P(b\cdot\nabla q),
\qquad
r(0)=0,
\tag{1}
\]

and pays a fixed pressure floor

\[
\int_0^h
\|\nabla\pi^*_{[r,b]}(\tau)\|_1\,d\tau
\ge p_r>0.
\tag{2}
\]

Split off the first heat-mediated feedback interaction:

\[
\boxed{
r^{[1]}(\tau)
:=
\int_0^\tau
e^{\nu(\tau-s)\Delta}
\mathbb P\operatorname{div}
\bigl(q\otimes b\bigr)(s)\,ds.
}
\tag{3}
\]

Here
\((q\otimes b)_{ik}=q_i b_k\), so
\(\operatorname{div}(q\otimes b)=b\cdot\nabla q\) because
\(\nabla\cdot b=0\).
The overall sign convention is immaterial below.
Define

\[
r^{[\ge2]}:=r-r^{[1]}.
\tag{4}
\]

The new result is

\[
\boxed{
\int_0^h
\|\nabla\pi^*_{[r^{[1]},b]}(\tau)\|_1\,d\tau
\longrightarrow0.
}
\tag{5}
\]

Consequently every selected feedback packet obeys, for all sufficiently
small \(h\),

\[
\boxed{
\int_0^h
\|\nabla\pi^*_{[r^{[\ge2]},b]}(\tau)\|_1\,d\tau
\ge\frac{p_r}{2},
}
\tag{6}
\]

where

\[
\boxed{
\partial_\tau r^{[\ge2]}
-\nu\Delta r^{[\ge2]}
-\mathbb P(b\cdot\nabla r^{[\ge2]})
=
\mathbb P(b\cdot\nabla r^{[1]}),
\qquad
r^{[\ge2]}(0)=0.
}
\tag{7}
\]

Thus neither the direct detector response nor the first causal feedback
response can carry the terminal pressure packet. The payer lies at
feedback depth at least two.

## 1. Reviewed direct-response bounds

Retain

\[
\sup_{0\le\tau\le h}
\|b(\tau)\|_{L^{3,\infty}}
\le M
\tag{8}
\]

and the reviewed heat response

\[
\partial_\tau q-\nu\Delta q
=
\nu\Delta\varphi+\mathbb P(b\cdot\nabla\varphi),
\qquad
q(0)=0.
\tag{9}
\]

For every unit cube \(Q_k=k+[0,1)^3\), the direct-response theorem gives

\[
\|q(t)\|_{L^\infty(Q_k)}
\le
C_N
\left[
t^{1/4}\langle k\rangle^{-N}
+t\langle k\rangle^{-4}
\right],
\qquad N\ge8.
\tag{10}
\]

Summing (10) over cubes and using its reviewed energy estimate gives

\[
\|q(t)\|_1\le C(t^{1/4}+t)\le Ct^{1/4},
\qquad
\|q(t)\|_2\le Ct.
\tag{11}
\]

Real interpolation therefore yields

\[
\boxed{
\|q(t)\|_{L^{3/2,1}}
\le
C\|q(t)\|_1^{1/3}\|q(t)\|_2^{2/3}
\le Ct^{3/4}.
}
\tag{12}
\]

The reviewed exterior Lorentz bound is, for \(R\ge2\),

\[
\boxed{
\|q(t)\|_{L^{6,2}(|x|>R)}
\le
C\left(
tR^{-7/2}
+t^{1/4}R^{-15/2}
\right).
}
\tag{13}
\]

Finally,

\[
\int_0^h\|\nabla q(t)\|_2^2\,dt\le Ch^2.
\tag{14}
\]

## 2. Energy of the first feedback response

Put

\[
F:=q\otimes b.
\tag{15}
\]

Lorentz Hölder and Lorentz--Sobolev give

\[
\|F(t)\|_2
\le
C M\|q(t)\|_{L^{6,2}}
\le
CM\|\nabla q(t)\|_2.
\tag{16}
\]

Pairing the equation for \(r^{[1]}\) with \(r^{[1]}\) and using Young's
inequality yields

\[
\boxed{
\sup_{0\le t\le h}\|r^{[1]}(t)\|_2^2
+\nu\int_0^h\|\nabla r^{[1]}(t)\|_2^2\,dt
\le Ch^2.
}
\tag{17}
\]

In particular,

\[
\int_0^h\|r^{[1]}(t)\|_2^2\,dt\le Ch^3.
\tag{18}
\]

This global estimate alone does not distinguish \(r^{[1]}\) from the
full feedback remainder. Its exterior tail does.

## 3. Strong exterior tail from the Stokes kernel

Let \(\mathcal K_\theta\) be the kernel of

\[
e^{\nu\theta\Delta}\mathbb P\operatorname{div}.
\tag{19}
\]

The nonstationary Stokes-kernel bounds are

\[
|\mathcal K_\theta(x)|
\le
C_\nu(|x|+\sqrt\theta)^{-4},
\qquad
\|\mathcal K_\theta\|_1
\le
C_\nu\theta^{-1/2},
\tag{20}
\]

and, when \(R\ge2\sqrt{\nu\theta}\),

\[
\|\mathbf1_{|x|>R}\mathcal K_\theta\|_2
\le
C_\nu R^{-5/2}.
\tag{21}
\]

All radii used below diverge as \(h\downarrow0\), so the condition in
(21) holds uniformly for all sufficiently small selected \(h\).

For a fixed \(R\ge2\), split \(F(s)\) into
\(|y|\le R/2\) and \(|y|>R/2\). Equations (8) and (12) give

\[
\|F(s)\|_1
\le
CM\|q(s)\|_{L^{3/2,1}}
\le Cs^{3/4}.
\tag{22}
\]

Equations (8) and (13) give

\[
\|F(s)\|_{L^2(|y|>R/2)}
\le
C\left(
sR^{-7/2}
+s^{1/4}R^{-15/2}
\right).
\tag{23}
\]

Young's inequality, (20)--(23), and the beta-integral identity imply

\[
\begin{aligned}
\|r^{[1]}(t)\|_{L^2(|x|>R)}
\le C\bigl(
&t^{7/4}R^{-5/2}\\
&+t^{3/2}R^{-7/2}\\
&+t^{3/4}R^{-15/2}
\bigr).
\end{aligned}
\tag{24}
\]

Indeed, the first term uses
\(\int_0^t s^{3/4}\,ds\), while the other two use

\[
\int_0^t(t-s)^{-1/2}s^\gamma\,ds
=
B\!\left(\frac12,\gamma+1\right)t^{\gamma+1/2}.
\tag{25}
\]

After squaring and integrating in time,

\[
\boxed{
\int_0^h
\|r^{[1]}(t)\|_{L^2(|x|>R)}^2\,dt
\le
C\left(
h^{9/2}R^{-5}
+h^4R^{-7}
+h^{5/2}R^{-15}
\right).
}
\tag{26}
\]

Unlike the \(R^{-1}\) tail of the full Oseen feedback remainder, every
term in (26) is summable after pairing with the centre-uniform
scale-critical coefficient energy shell by shell.

## 4. The inverse-cubic coefficient piece cannot pay

Set

\[
R_{\rm src}:=h^{-3},
\qquad
c_h:=\chi_{R_{\rm src}}b.
\tag{27}
\]

The reviewed local-energy and cutoff estimates give

\[
\int_0^h\|\nabla c_h\|_2^2\,dt\le Ch^{-3}.
\tag{28}
\]

Split \(c_h\) again at \(L=h^{-\alpha}\), with

\[
\frac1{30}<\alpha<3.
\tag{29}
\]

The near coefficient obeys

\[
\int_0^h
\|\nabla c_{h,L}^{\rm near}\|_2^2\,dt
\le C(L+hL^{-1}).
\tag{30}
\]

CLMS, (18), and (30) give

\[
P_{\rm near}^{[1]}
\le
C\left(
h^{3/2}L^{1/2}
+h^2L^{-1/2}
\right).
\tag{31}
\]

For the far coefficient, use the reviewed scale-invariant Bogovskii
correction of \(r^{[1]}\), which equals \(r^{[1]}\) on every component
of the far coefficient-gradient support. Equations (26) and (28) give

\[
\begin{aligned}
P_{\rm far}^{[1]}
\le C\bigl(
&h^{3/4}L^{-5/2}\\
&+h^{1/2}L^{-7/2}\\
&+h^{-1/4}L^{-15/2}
\bigr).
\end{aligned}
\tag{32}
\]

At the concrete choice \(\alpha=1/10\), equations (31)--(32) have
powers

\[
\boxed{
\frac{29}{20},
\qquad
\frac{41}{20},
\qquad
1,
\qquad
\frac{17}{20},
\qquad
\frac12.
}
\tag{33}
\]

They all vanish. Therefore

\[
\int_0^h
\|\nabla\pi^*_{[r^{[1]},c_h]}(t)\|_1\,dt
\longrightarrow0.
\tag{34}
\]

## 5. The complete exterior coefficient cannot pay

Write the exterior coefficient as fixed-shape dyadic pieces at

\[
R_k:=2^kR_{\rm src},
\qquad
k\ge0.
\tag{35}
\]

The reviewed centre-uniform local energy and weak-\(L^3\) cutoff bound
give, for every piece,

\[
\int_0^h\|\nabla b_k(t)\|_2^2\,dt
\le CR_k.
\tag{36}
\]

Use the reviewed solenoidal exterior truncation of \(r^{[1]}\) on the
support of \(\nabla b_k\). CLMS, (26), and (36) give

\[
\begin{aligned}
\int_0^h
\|\nabla\pi^*_{[r^{[1]},b_k]}(t)\|_1\,dt
\le C\bigl(
&h^{9/4}R_k^{-2}\\
&+h^2R_k^{-3}\\
&+h^{5/4}R_k^{-7}
\bigr).
\end{aligned}
\tag{37}
\]

All radius powers are summable. Since \(R_{\rm src}=h^{-3}\),

\[
\boxed{
\sum_{k\ge0}
\int_0^h
\|\nabla\pi^*_{[r^{[1]},b_k]}(t)\|_1\,dt
\le
C\left(
h^{33/4}
+h^{11}
+h^{89/4}
\right)
\longrightarrow0.
}
\tag{38}
\]

Combining (34) and (38) proves (5).

## 6. Exact causal consequence

Subtracting the heat equation for \(r^{[1]}\) from (1) proves (7)
exactly. Pressure is linear in its first entry:

\[
\nabla\pi^*_{[r,b]}
=
\nabla\pi^*_{[r^{[1]},b]}
+
\nabla\pi^*_{[r^{[\ge2]},b]}.
\tag{39}
\]

Equations (2), (5), and the triangle inequality prove (6).

This closes the first finite interaction-order child. It does not yet
show that every fixed interaction order vanishes uniformly in the order,
sum the remaining Dyson series, control the constants as the interaction
depth grows, exclude the inverse-\(15/4\) direct branch, or prove any
Clay alternative A--D.

The next exact question is:

> Does the Stokes-kernel tail in (26) propagate through every fixed
> heat-feedback iterate with controlled constants, forcing the payer to
> infinite causal depth; or can a finite later interaction lose the
> summable exterior tail?

## Reproduce

```bash
make adjoint-pressure-second-interaction
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_second_interaction -v
make check
```
