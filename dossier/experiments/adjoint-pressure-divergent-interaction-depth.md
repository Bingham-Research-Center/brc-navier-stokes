# A terminal feedback packet requires logarithmically divergent causal interaction depth

- **Experiment:** EXP-ADJOINT-PRESSURE-DIVERGENT-INTERACTION-DEPTH-001
- **Route:** ROUTE-R3B
- **Status:** conditional analytic reduction;
  [independently reviewed valid after repair](../review-response-adjoint-pressure-divergent-interaction-depth-2026-07-24.md)
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** independently reviewed
  [direct-response decomposition](adjoint-pressure-direct-response.md),
  [feedback-tail theorem](adjoint-pressure-feedback-tail.md),
  [intermediate-localisation theorem](adjoint-pressure-intermediate-localization.md),
  and [first-interaction theorem](adjoint-pressure-second-interaction.md)

The selected zero-data feedback remainder satisfies

\[
\partial_t r-\nu\Delta r-\mathbb P(b\cdot\nabla r)
=
\mathbb P(b\cdot\nabla q),
\qquad
r(0)=0,
\tag{1}
\]

and pays a fixed pressure floor

\[
\int_0^h
\|\mathcal T(r,b)(t)\|_1\,dt
\ge p_r>0.
\tag{2}
\]

Here

\[
\mathcal T(z,c)
:=
\nabla\Delta^{-1}\operatorname{div}
\bigl((z\cdot\nabla)c\bigr)
\tag{3}
\]

is the reviewed bilinear pressure-gradient operator.  Define the
heat-feedback operator

\[
(T_bz)(t)
:=
\int_0^t
e^{\nu(t-s)\Delta}
\mathbb P\operatorname{div}(z\otimes b)(s)\,ds,
\tag{4}
\]

where
\((z\otimes b)_{ik}=z_i b_k\).  Since \(\nabla\cdot b=0\),
\(\operatorname{div}(z\otimes b)=b\cdot\nabla z\).  Put

\[
u_0:=q,
\qquad
u_m:=T_b^m q
\quad(m\ge1).
\tag{5}
\]

The new fixed-order theorem is

\[
\boxed{
\forall m\ge1\text{ fixed},\qquad
\int_0^h\|\mathcal T(u_m,b)(t)\|_1\,dt
\longrightarrow0
\quad(h\downarrow0).
}
\tag{6}
\]

Consequently, for every fixed \(N\ge1\), the exact Dyson remainder

\[
R_{N+1}:=
r-\sum_{m=1}^{N}u_m
\tag{7}
\]

obeys, for all sufficiently small selected \(h\) depending on \(N\),

\[
\boxed{
\int_0^h\|\mathcal T(R_{N+1},b)(t)\|_1\,dt
\ge\frac{p_r}{2},
}
\tag{8}
\]

and

\[
\boxed{
\partial_tR_{N+1}-\nu\Delta R_{N+1}
-\mathbb P(b\cdot\nabla R_{N+1})
=
\mathbb P(b\cdot\nabla u_N),
\qquad
R_{N+1}(0)=0.
}
\tag{9}
\]

More quantitatively, there are constants \(c_{\rm dep}>0\) and
\(h_0>0\), depending only on the fixed reviewed data, such that

\[
\boxed{
N(h):=\left\lfloor c_{\rm dep}\log\frac1h\right\rfloor
\quad\Longrightarrow\quad
\int_0^h\|\mathcal T(R_{N(h)+1},b)(t)\|_1\,dt
\ge\frac{p_r}{2}
}
\tag{9a}
\]

for every selected \(0<h<h_0\).  Thus the pressure packet persists in
Dyson remainders whose causal depth grows at least logarithmically as
the terminal window collapses.  This is not a summation of the infinite
Dyson expansion.

## 1. Reviewed input and exponent ledger

Uniformly along the selected layers,

\[
\sup_{0\le t\le h}\|b(t)\|_{L^{3,\infty}}\le M.
\tag{10}
\]

The direct response \(q\) satisfies

\[
\|q(t)\|_1\le Ct^{1/4},
\qquad
\|q(t)\|_2\le Ct,
\qquad
\int_0^t\|\nabla q(s)\|_2^2\,ds\le Ct^2,
\tag{11}
\]

and, for \(R\ge2\),

\[
\|q(t)\|_{L^{6,2}(|x|>R)}
\le
C\left(tR^{-7/2}+t^{1/4}R^{-15/2}\right).
\tag{12}
\]

Introduce

\[
A_0:=\frac14,
\qquad
A_m:=\frac13A_{m-1}+\frac76
\quad(m\ge1).
\tag{13}
\]

The exact solution is

\[
\boxed{
A_m=\frac74-\frac32\,3^{-m}.
}
\tag{14}
\]

The associated Lorentz and exterior-tail exponents are

\[
\boxed{
B_m:=\frac13A_m+\frac23
=\frac54-\frac12\,3^{-m},
}
\tag{15}
\]

and, for \(m\ge1\),

\[
\boxed{
\beta_m:=2B_{m-1}+3
=\frac{11}{2}-3^{-(m-1)}.
}
\tag{16}
\]

In particular,

\[
\beta_1=\frac92,
\qquad
\beta_m\uparrow\frac{11}{2}.
\tag{17}
\]

## 2. Global bounds at every fixed order

For each fixed \(m\ge0\), there is a constant \(C_m\), independent of
the selected \(h\), such that

\[
\boxed{
\|u_m(t)\|_1\le C_mt^{A_m},
\qquad
\|u_m(t)\|_2\le C_mt,
\qquad
\|u_m(t)\|_{L^{3/2,1}}\le C_mt^{B_m}.
}
\tag{18}
\]

For \(m\ge1\),

\[
\partial_tu_m-\nu\Delta u_m
=
\mathbb P\operatorname{div}(u_{m-1}\otimes b),
\qquad
u_m(0)=0.
\tag{19}
\]

Energy, Lorentz Hölder, and Lorentz--Sobolev give

\[
\begin{aligned}
\sup_{0\le s\le t}\|u_m(s)\|_2^2
+\nu\int_0^t\|\nabla u_m(s)\|_2^2\,ds
&\le
C_{\nu,M}\int_0^t
\|\nabla u_{m-1}(s)\|_2^2\,ds\\
&\le C_mt^2.
\end{aligned}
\tag{20}
\]

The base case is (11), and induction proves the second estimate in
(18) and

\[
\int_0^h\|\nabla u_m(t)\|_2^2\,dt\le C_mh^2.
\tag{21}
\]

The elementary real-interpolation inequality

\[
\|f\|_{L^{3/2,1}}
\le C\|f\|_1^{1/3}\|f\|_2^{2/3}
\tag{22}
\]

turns the first two estimates in (18) into the third.  Lorentz Hölder
then gives

\[
\|u_m(t)\otimes b(t)\|_1
\le C M\|u_m(t)\|_{L^{3/2,1}}
\le C_mt^{B_m}.
\tag{23}
\]

Let \(\mathcal K_\theta\) denote the kernel of
\(e^{\nu\theta\Delta}\mathbb P\operatorname{div}\).  The reviewed
Stokes-kernel estimate

\[
\|\mathcal K_\theta\|_1\le C_\nu\theta^{-1/2}
\tag{24}
\]

and the beta-integral identity yield

\[
\begin{aligned}
\|u_{m+1}(t)\|_1
&\le
C_m\int_0^t(t-s)^{-1/2}s^{B_m}\,ds\\
&\le C_mt^{B_m+1/2}.
\end{aligned}
\tag{25}
\]

Since
\(B_m+1/2=A_m/3+7/6=A_{m+1}\), this closes (18) and
proves (13).

## 3. A stable exterior \(H^1\) and Lorentz--Sobolev envelope

Besides (24), the differentiated off-diagonal Stokes kernel satisfies

\[
|\nabla\mathcal K_\theta(x)|
\le C_\nu(|x|+\sqrt\theta)^{-5},
\qquad
\|\mathbf1_{|x|>R}\nabla\mathcal K_\theta\|_2
\le C_\nu R^{-7/2}
\tag{26}
\]

whenever \(R\ge2\sqrt{\nu\theta}\).  The radii used in the pressure
argument diverge as \(h\downarrow0\), so this restriction holds for all
sufficiently small selected \(h\).

Squaring (12), integrating in time, and absorbing its cross term gives

\[
\int_0^h
\|q(t)\|_{L^{6,2}(|x|>R)}^2\,dt
\le
C\left(h^3R^{-7}+h^{3/2}R^{-15}\right).
\tag{27}
\]

For every \(m\ge1\), the same two-term envelope propagates whenever

\[
R\ge R_m^{\min}:=C_\nu4^m.
\tag{27a}
\]

At fixed \(m\), this threshold holds at all radii used below for every
sufficiently small selected \(h\).  The estimate is

\[
\boxed{
\begin{aligned}
&\int_0^h
\|\nabla u_m(t)\|_{L^2(|x|>R)}^2\,dt\\
&\quad+
\int_0^h
\|u_m(t)\|_{L^{6,2}(|x|>R)}^2\,dt\\
&\hspace{35mm}\le
C_m\left(h^3R^{-7}+h^{3/2}R^{-15}\right).
\end{aligned}
}
\tag{28}
\]

To prove this, split
\(F_{m-1}:=u_{m-1}\otimes b\) at \(R/2\).
For the inner source, (23) and (26) give

\[
\begin{aligned}
\int_0^h
\left\|
\nabla\int_0^t
\mathcal K_{t-s}*
\bigl(\mathbf1_{|y|\le R/2}F_{m-1}\bigr)(s)\,ds
\right\|_{L^2(|x|>R)}^2dt
\le
C_mh^{\beta_m}R^{-7}.
\end{aligned}
\tag{29}
\]

For the outer source, the zero-data Stokes energy estimate gives

\[
\int_0^h\|\nabla u_m^{\rm out}(t)\|_2^2\,dt
\le
C_{\nu,M}
\int_0^h
\|u_{m-1}(t)\|_{L^{6,2}(|x|>R/2)}^2\,dt.
\tag{30}
\]

For \(m=1\), equation (27) controls the right-hand side.  Inductively,
the \(L^{6,2}\) part of (28) controls it.  Since
\(\beta_m\ge9/2>3\) and \(0<h\le1\), equations (29)--(30) prove the
gradient part of (28).

Finally, a cutoff supported outside \(R/2\), equal to one outside
\(R\), and Lorentz--Sobolev imply

\[
\|u_m(t)\|_{L^{6,2}(|x|>R)}^2
\le
C\left(
\|\nabla u_m(t)\|_{L^2(|x|>R/2)}^2
+R^{-2}\|u_m(t)\|_{L^2(|x|>R/2)}^2
\right).
\tag{31}
\]

The \(L^2\) term is controlled by the tail proved next.  Equations
(31), (33) below, and the already established gradient part close the
\(L^{6,2}\) induction in (28).  This simultaneous induction starts
from (27) and the first-interaction tail.  Each order first evaluates
the preceding \(L^{6,2}\) tail at \(R/2\), then obtains the current
\(L^{6,2}\) tail from the current gradient and \(L^2\) tails at
\(R/2\).  The two shrinkages compose to \(R/4\), explaining the
explicit \(4^m\) threshold in (27a).

## 4. The fixed-order exterior \(L^2\) tail

The undifferentiated off-diagonal estimate is

\[
\|\mathbf1_{|x|>R}\mathcal K_\theta\|_2
\le C_\nu R^{-5/2}.
\tag{32}
\]

The same inner/outer source split gives, for every fixed \(m\ge1\),

\[
\boxed{
\int_0^h
\|u_m(t)\|_{L^2(|x|>R)}^2\,dt
\le
C_m\left(
h^{\beta_m}R^{-5}
+h^4R^{-7}
+h^{5/2}R^{-15}
\right).
}
\tag{33}
\]

Indeed, (23) and (32) bound the inner-source response pointwise by

\[
C_m t^{B_{m-1}+1}R^{-5/2}.
\tag{34}
\]

Its squared time integral is
\[
C_mh^{2B_{m-1}+3}R^{-5}
=C_mh^{\beta_m}R^{-5}.
\]
For the outer source, time--space Young convolution and (24) give

\[
\begin{aligned}
\int_0^h\|u_m^{\rm out}(t)\|_2^2\,dt
&\le
C_\nu h
\int_0^h\|F_{m-1}^{\rm out}(t)\|_2^2\,dt\\
&\le
C_{\nu,M}h
\int_0^h
\|u_{m-1}(t)\|_{L^{6,2}(|x|>R/2)}^2\,dt\\
&\le
C_m\left(h^4R^{-7}+h^{5/2}R^{-15}\right).
\end{aligned}
\tag{35}
\]

For \(m=1\), the last line uses (27); thereafter it uses (28).
Conversely, multiplying the three terms of (33) by \(R^{-2}\) in
(31) produces terms absorbed by
\(h^3R^{-7}+h^{3/2}R^{-15}\), since
\(\beta_m\ge9/2\), \(h\le1\), and \(R\ge2\).
This proves (28) and (33) together without circularity: at each order,
the gradient bound uses the preceding order's \(L^{6,2}\) bound, then
(33) is proved, and only then (31) supplies the current
\(L^{6,2}\) bound.

## 5. Every fixed iterate has vanishing complete pressure

Use the reviewed source radius

\[
R_{\rm src}:=h^{-3},
\qquad
c_h:=\chi_{R_{\rm src}}b,
\tag{36}
\]

with

\[
\int_0^h\|\nabla c_h(t)\|_2^2\,dt\le Ch^{-3}.
\tag{37}
\]

Split \(c_h\) once more at

\[
L=h^{-\alpha},
\qquad
\frac1{30}<\alpha<3.
\tag{38}
\]

The near-coefficient estimate uses the global \(L^2\) bounds
(18)--(20), while the far-coefficient estimate uses the reviewed
solenoidal Bogovskii replacement and (33).
They give

\[
\begin{aligned}
P_{m,\rm near}
&\le
C_m\left(
h^{3/2}L^{1/2}
+h^2L^{-1/2}
\right),
\tag{39}\\
P_{m,\rm far}
&\le
C_m\left(
h^{\beta_m/2-3/2}L^{-5/2}
+h^{1/2}L^{-7/2}
+h^{-1/4}L^{-15/2}
\right).
\tag{40}
\end{aligned}
\]

At \(\alpha=1/10\), the five powers of \(h\) are

\[
\boxed{
\frac{29}{20},
\qquad
\frac{41}{20},
\qquad
\frac{\beta_m}{2}-\frac54,
\qquad
\frac{17}{20},
\qquad
\frac12.
}
\tag{41}
\]

The third is smallest at \(m=1\), where it equals \(1\).  Thus every
term vanishes for each fixed \(m\).

For the complete exterior coefficient, use dyadic fixed-shape pieces
at

\[
R_k:=2^kR_{\rm src},
\qquad
\int_0^h\|\nabla b_k(t)\|_2^2\,dt\le CR_k.
\tag{42}
\]

The reviewed exterior Bogovskii truncation, CLMS, and (33) give

\[
\begin{aligned}
\sum_{k\ge0}
\int_0^h\|\mathcal T(u_m,b_k)(t)\|_1\,dt
\le C_m\left(
h^{\beta_m/2+6}
+h^{11}
+h^{89/4}
\right).
\end{aligned}
\tag{43}
\]

The first power is again smallest at \(m=1\), where it is \(33/4\).
Equations (39)--(43) prove (6).

## 6. Exponential constant ledger and logarithmic depth

The proof above can be made uniform in the interaction order up to an
exponential loss.  There are constants \(C_0>0\) and \(\Lambda\ge2\),
independent of \(m\) and \(h\), such that the norm coefficients in
(18), (20), and (21) are at most

\[
C_0\Lambda^m,
\tag{43a}
\]

while the squared-tail coefficients in (28) and (33) are at most

\[
C_0^2\Lambda^{2m}.
\tag{43b}
\]

Here is the constant audit.  The energy step multiplies the preceding
squared coefficient by one fixed \(C_{\nu,M}\).  The interpolation
exponents sum to one.  The beta factors in (25) stay uniformly bounded
because \(B_m\in[3/4,5/4)\).  In the exterior induction, replacing
\(R\) by \(R/4\) over one complete induction step costs at most the
fixed factor \(4^{15}=2^{30}\); the
zero-data energy and Young constants are fixed; and a source norm is
squared at most once.  Hence the vector of squared-tail coefficients is
bounded by a fixed multiple of its predecessor plus a fixed
exponential source coefficient.  Taking \(\Lambda\) larger than all
these fixed multipliers proves (43a)--(43b) by induction.  The
scaled-annulus Bogovskii, CLMS, cutoff, and dyadic-summation constants
are independent of \(m\).

More explicitly, let \(e_m,\ell_m,q_m,x_m\) denote respectively the
coefficients in the squared energy, \(L^1\), \(L^{3/2,1}\), and
squared exterior-tail estimates.  The proof gives order-independent
constants such that

\[
e_m\le C_Ee_{m-1},
\qquad
q_m\le C_I\ell_m^{1/3}e_m^{1/3},
\qquad
\ell_{m+1}\le C_Kq_m,
\tag{43c}
\]

and

\[
x_m\le C_T2^{30}
\left(x_{m-1}+q_{m-1}^2\right).
\tag{43d}
\]

After enlarging \(\Lambda\), these recurrences directly give
\(e_m+x_m\le C_0^2\Lambda^{2m}\) and
\(\ell_m+q_m\le C_0\Lambda^m\).

For the quantitative truncation, optimise the still-admissible
intermediate radius by taking

\[
\alpha_*:=\frac14,
\qquad
L=h^{-1/4}.
\]

The five powers in (39)--(40) are then

\[
\frac{11}{8},
\qquad
\frac{17}{8},
\qquad
\frac{\beta_m}{2}-\frac78,
\qquad
\frac{11}{8},
\qquad
\frac{13}{8}.
\]

The order-dependent power is at least \(11/8\), with equality at
\(m=1\).  This choice maximises the minimum of the five powers over
\(1/30<\alpha<3\).  Indeed, that minimum is

\[
\mu(\alpha)=
\min\left\{
\frac32-\frac\alpha2,\,
\frac34+\frac{5\alpha}{2},\,
\frac12+\frac{7\alpha}{2},\,
-\frac14+\frac{15\alpha}{2}
\right\}.
\]

If \(\alpha\le1/4\), its third displayed candidate is at most
\(11/8\); if \(\alpha\ge1/4\), its first candidate is at most
\(11/8\).  Equality is attained at \(\alpha=1/4\).  Therefore

\[
\boxed{
\int_0^h\|\mathcal T(u_m,b)(t)\|_1\,dt
\le C_0\Lambda^m h^{11/8}
}
\tag{43e}
\]

whenever the intermediate radius
\(L=h^{-1/4}\) satisfies \(L\ge C_\nu4^m\).  Choose

\[
0<c_{\rm dep}\le
\min\left\{
\frac{11}{32\log\Lambda},
\frac{1}{16\log2}
\right\}.
\tag{43f}
\]

For \(N(h)\) in (9a), and all sufficiently small \(h\),

\[
\Lambda^{N(h)}\le h^{-11/32},
\qquad
4^{N(h)}\le h^{-1/8}\ll L.
\tag{43g}
\]

Thus the radius threshold holds simultaneously through order \(N(h)\),
and summing (43e) geometrically gives

\[
\boxed{
\sum_{m=1}^{N(h)}
\int_0^h\|\mathcal T(u_m,b)(t)\|_1\,dt
\le Ch^{33/32}
\longrightarrow0.
}
\tag{43h}
\]

This proves the logarithmic-depth assertion (9a).

## 7. Exact Dyson consequence and retained boundary

Equation (1) has the mild identity

\[
r=T_bq+T_br.
\tag{44}
\]

Equations (5) and (44) imply both

\[
\boxed{
R_{N+1}=T_b^Nr
}
\tag{44a}
\]

and (9), without assuming convergence of an infinite series.  By
bilinearity,

\[
\mathcal T(r,b)
=
\sum_{m=1}^N\mathcal T(u_m,b)
+\mathcal T(R_{N+1},b).
\tag{45}
\]

For fixed \(N\), the finite sum tends to zero by (6).  Equations
(2), (45), and the triangle inequality prove (8).  With
\(N=N(h)\), the same argument and (43h) prove (9a).

This closes every bounded-depth interaction-order child and forces at
least logarithmically growing causal depth.
It does **not**:

- improve the exponential ledger enough to sum every interaction order;
- prove convergence or pressure summability of the infinite Dyson series;
- exclude the full feedback remainder;
- exclude the inverse-\(15/4\) direct-response branch; or
- prove regularity, breakdown, or any Clay alternative A--D.

The next exact question is:

> Can critical Oseen time ordering improve the exponential
> interaction-order ledger to a summable or quasi-nilpotent bound, or
> can an independent causal compactness or analyticity argument exclude
> a pressure packet persisting beyond \(c\log(1/h)\) interactions?

## Reproduce

```bash
make adjoint-pressure-interaction-depth
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_interaction_depth -v
make check
```
