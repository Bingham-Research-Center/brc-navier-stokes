# A prescribed multistage Oseen itinerary retains its initial inverse frequency

- **Experiment:** EXP-ADJOINT-PRESSURE-MULTISTAGE-PATH-001
- **Route:** ROUTE-R3B
- **Status:** independently reviewed conditional analytic reduction
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** independently reviewed
  [one-return theorem](adjoint-pressure-one-return.md) and
  [cross-band kernel theorem](adjoint-pressure-frequency-zeno.md)
- **Review:** [valid in the stated conditional scope](../review-response-adjoint-pressure-multistage-path-2026-07-24.md)

The one-return theorem controls a high state which makes one
heat--Leray return to an annulus \(R_0\), then immediately generates
pressure below a fixed frequency \(S\).  Its unresolved complement can
make further state interactions before the pressure is observed.

This note treats one prescribed finite itinerary

\[
R_0\longrightarrow R_1\longrightarrow\cdots
\longrightarrow R_m\longrightarrow S.
\]

The intermediate frequency ratios do not accumulate.  After every heat
kernel is normalised to have unit mass, they telescope exactly against
the final pressure multiplier.  The only surviving frequency loss is
\(S/R_0\), inherited from the first return.

Let

\[
\lambda_j:=c_0\nu R_j^2
\qquad(0\le j\le m),
\tag{1}
\]

and let \(X_0,\ldots,X_m\) be independent exponential random variables
with respective rates \(\lambda_0,\ldots,\lambda_m\).  Define the exact
finite-window heat clock

\[
\boxed{
\Theta_{\boldsymbol R}(h)
:=
\mathbb P\!\left(
X_0+\cdots+X_m\le h
\right).
}
\tag{2}
\]

For the path component and pressure functional defined below,

\[
\boxed{
\mathfrak R_{\boldsymbol R}(h)
\le
C_{\rm src}
A_pA_x^m
\frac{S}{R_0}
\Theta_{\boldsymbol R}(h)
\mathcal B(h,R_0),
}
\tag{3}
\]

where \(A_x=C_xM/(c_0\nu)\), \(A_p=C_pM/(c_0\nu)\), and

\[
\boxed{
\begin{aligned}
\mathcal B(h,R_0)
:=
1
&+h^{7/4}
\left[
1+\log_+\!\bigl(D_b(h)h^3\bigr)
\right]\\
&+h^{21/4}
+h^{89/4}
+h^{103/4}
+h^6R_0^{-2}.
\end{aligned}}
\tag{4}
\]

Here \(C_x,C_p,c_0\) depend only on the fixed annular and low-output
cutoffs.  Equivalently, with

\[
A:=\max\{A_x,A_p\},
\tag{5}
\]

equation (3) has the simpler upper bound

\[
\boxed{
\mathfrak R_{\boldsymbol R}(h)
\le
C_{\rm src}
A^{m+1}
\frac{S}{R_0}
\Theta_{\boldsymbol R}(h)
\mathcal B(h,R_0).
}
\tag{6}
\]

The exact clock satisfies

\[
\boxed{
\Theta_{\boldsymbol R}(h)
\le
\min\{1,c_0\nu R_0^2h\}
}
\tag{7}
\]

and

\[
\boxed{
\Theta_{\boldsymbol R}(h)
\le
\min\left\{
1,\,
\frac{h^{m+1}}{(m+1)!}
\prod_{j=0}^{m}\lambda_j
\right\}.
}
\tag{8}
\]

At fixed \(m\), a fixed positive floor for this particular path with
\(R_0=h^{-\beta}\) forces the same stretched exponent as one return:

\[
\boxed{
D_b(h)
\ge
h^{-3}\exp\!\left(
c_mh^{-\gamma_1(\beta)}
\right),
\qquad
\gamma_1(\beta)
=
\frac94+\left|\beta-\frac12\right|.
}
\tag{9}
\]

This is a theorem about one prescribed iterated Oseen component.  It
does not decompose the complete returned-low state into such paths, sum
all itineraries, control their pressure recombination, or prove that
this component carries a positive pressure fraction.

## 1. Reviewed input

Retain the zero-data feedback remainder \(r\) and divergence-free drift
\(b\) from the one-return theorem, with

\[
\sup_{0<t<h}\|b(t)\|_{L^{3,\infty}}\le M.
\tag{10}
\]

Throughout, \(h,\nu,S,R_j>0\), \(M<\infty\), and every
\(\Delta_R\) is a dilation of one fixed smooth annular symbol.  Choose
\(c_0>0\) no larger than either heat-decay constant in the reviewed
source and cross-band bounds.  For the path and pressure tensors use
the reviewed Oseen convention

\[
(z\boxtimes b)_{ik}:=z_i b_k.
\tag{10a}
\]

For an annular frequency \(R_0\), let

\[
w_0(t)
:=
\int_0^t
\Delta_{R_0}e^{\nu(t-s)\Delta}
\mathbb P\operatorname{div}
\left(
(P_{>64R_0}r(s))\boxtimes b(s)
\right)\,ds.
\tag{11}
\]

The reviewed one-return proof constructs a nonnegative source
\(G_{R_0}\) such that

\[
\|w_0(t)\|_1
\le
C_{\rm src}
\int_0^t
e^{-c_0\nu R_0^2(t-s)}
G_{R_0}(s)\,ds
\tag{12}
\]

and

\[
\int_0^hG_{R_0}(s)\,ds
\le
\mathcal B(h,R_0).
\tag{13}
\]

The full tensor divergence is retained in (11).  In particular, this
note does not repeat or alter the spatial-cutoff cancellation already
checked in the one-return review.

For an annular state \(z_R\), the reviewed positive cross-band
majorant is

\[
\begin{aligned}
&\left\|
\Delta_Qe^{\nu(t-s)\Delta}
\mathbb P\operatorname{div}
(z_R\boxtimes b)(s)
\right\|_1\\
&\qquad\le
C_xMRQ
e^{-c_0\nu Q^2(t-s)}
\|z_R(s)\|_1.
\end{aligned}
\tag{14}
\]

The estimate is valid without asserting that the positive scalar
majorant equals the signed vector operator.

Finally, for annular \(z_R\), the fixed low-output pressure
observation obeys

\[
\left\|
\Pi_S(z_R\boxtimes b)
\right\|_1
\le
C_pMSR\|z_R\|_1.
\tag{15}
\]

For the returned-low interpretation one may take every \(R_j\ge16S\).
The norm calculation below only needs the stated annular support.

## 2. The prescribed path component

Fix \(m\ge0\) and positive annular frequencies
\(\boldsymbol R=(R_0,\ldots,R_m)\).  Starting with (11), define
recursively for \(1\le j\le m\)

\[
\boxed{
w_j(t)
:=
\int_0^t
\Delta_{R_j}e^{\nu(t-s)\Delta}
\mathbb P\operatorname{div}
\left(
w_{j-1}(s)\boxtimes b(s)
\right)\,ds.
}
\tag{16}
\]

Every \(w_j\) is solenoidal and supported in the fixed annulus selected
by \(\Delta_{R_j}\).  Define its terminal pressure cost by

\[
\boxed{
\mathfrak R_{\boldsymbol R}(h)
:=
\int_0^h
\left\|
\Pi_S\left(w_m(t)\boxtimes b(t)\right)
\right\|_1\,dt.
}
\tag{17}
\]

Equation (14) gives

\[
\|w_j(t)\|_1
\le
C_xMR_{j-1}R_j
\int_0^t
e^{-\lambda_j(t-s)}
\|w_{j-1}(s)\|_1\,ds.
\tag{18}
\]

Introduce the unit-mass exponential kernels

\[
e_j(t):=
\lambda_je^{-\lambda_jt}\mathbf 1_{t\ge0}.
\tag{19}
\]

The initial kernel in (12) is

\[
e^{-\lambda_0t}\mathbf 1_{t\ge0}
=
\lambda_0^{-1}e_0(t),
\tag{20}
\]

whereas every later transition has the exact normalisation

\[
\begin{aligned}
C_xMR_{j-1}R_j
e^{-\lambda_jt}\mathbf 1_{t\ge0}
&=
\frac{C_xM}{c_0\nu}
\frac{R_{j-1}}{R_j}
e_j(t)\\
&=
A_x\frac{R_{j-1}}{R_j}e_j(t).
\end{aligned}
\tag{21}
\]

Iterating (12) and (18) therefore yields

\[
\begin{aligned}
\|w_m(t)\|_1
\le{}&
\frac{C_{\rm src}}{\lambda_0}
A_x^m
\left(
\prod_{j=1}^m\frac{R_{j-1}}{R_j}
\right)\\
&\quad{}\times
\bigl(
(e_0*\cdots*e_m)*G_{R_0}
\bigr)(t).
\end{aligned}
\tag{22}
\]

The empty product and empty sequence of later transitions are
understood when \(m=0\).

The frequency ratios telescope:

\[
\boxed{
\prod_{j=1}^m\frac{R_{j-1}}{R_j}
=
\frac{R_0}{R_m}.
}
\tag{23}
\]

By (15), (17), Tonelli's theorem, and nonnegativity,

\[
\begin{aligned}
\mathfrak R_{\boldsymbol R}(h)
&\le
C_pMSR_m
\frac{C_{\rm src}}{\lambda_0}
A_x^m\frac{R_0}{R_m}\\
&\quad{}\times
\int_0^hG_{R_0}(s)
\int_0^{h-s}
(e_0*\cdots*e_m)(\tau)
\,d\tau\,ds.
\end{aligned}
\tag{24}
\]

The inner integral is the distribution function of the sum of the
independent exponential clocks:

\[
\int_0^u(e_0*\cdots*e_m)(\tau)\,d\tau
=
\mathbb P(X_0+\cdots+X_m\le u)
\le
\Theta_{\boldsymbol R}(h).
\tag{25}
\]

Since \(\lambda_0=c_0\nu R_0^2\), the prefactors in (24) reduce to

\[
\begin{aligned}
C_pMSR_m
\frac1{\lambda_0}
A_x^m
\frac{R_0}{R_m}
&=
\frac{C_pM}{c_0\nu}
A_x^m\frac{S}{R_0}\\
&=
A_pA_x^m\frac{S}{R_0}.
\end{aligned}
\tag{26}
\]

Equations (13), (24)--(26) prove (3), and (6) follows from (5).
No monotonicity or spacing condition on the intermediate frequencies
was used.

## 3. Exact heat-clock ceilings

Because \(X_0+\cdots+X_m\ge X_0\),

\[
\begin{aligned}
\Theta_{\boldsymbol R}(h)
&\le
\mathbb P(X_0\le h)\\
&=
1-e^{-\lambda_0h}
\le
\min\{1,\lambda_0h\},
\end{aligned}
\tag{27}
\]

which is (7).

The joint exponential density is bounded above by
\(\prod_{j=0}^m\lambda_j\).  The positive simplex

\[
\left\{
(x_0,\ldots,x_m):
x_j\ge0,
x_0+\cdots+x_m\le h
\right\}
\]

has volume \(h^{m+1}/(m+1)!\).  Integration over this simplex proves
(8).

More generally, for every nonempty
\(J\subseteq\{0,\ldots,m\}\),

\[
\boxed{
\Theta_{\boldsymbol R}(h)
\le
\min\left\{
1,\,
\frac{h^{|J|}}{|J|!}
\prod_{j\in J}\lambda_j
\right\}.
}
\tag{28}
\]

Indeed, the full clock event implies
\(\sum_{j\in J}X_j\le h\).  This subset form is useful because clocks
with \(\lambda_jh\gg1\) need not be included in a small-time ceiling.

### Dyadic descent

For the exact descending path

\[
R_j=2^{-j}R_0,
\qquad 0\le j\le m,
\tag{29}
\]

the full rate product is

\[
\boxed{
\prod_{j=0}^m\lambda_j
=
(c_0\nu)^{m+1}
R_0^{2(m+1)}
2^{-m(m+1)}.
}
\tag{30}
\]

Suppose \(n\) consecutive clocks in this descent begin at an index
\(j_*\) satisfying

\[
h\lambda_{j_*}\le1.
\tag{31}
\]

For \(J=\{j_*,\ldots,j_*+n-1\}\),

\[
h\lambda_{j_*+\ell}
\le4^{-\ell},
\qquad0\le\ell<n.
\tag{32}
\]

Thus (28) gives the dimensionless ceiling

\[
\boxed{
\Theta_{\boldsymbol R}(h)
\le
\frac{2^{-n(n-1)}}{n!}.
}
\tag{33}
\]

For a complete dyadic descent from \(R_0=h^{-\beta}\) to a fixed
terminal scale,

\[
n
=
\min\left\{\beta,\frac12\right\}
\log_2(1/h)+O(1).
\tag{33a}
\]

Hence (33) is
\(\exp[-c(\log(1/h))^2]\) up to lower-order factors.  It beats the
factor \(A^{m+1}\) whenever \(m=O(\log(1/h))\).  This statement concerns
the clock-times-interaction prefactor of one path.  The potentially
large factor \(\mathcal B(h,R_0)\), the existence of a complete path
decomposition, and the count and recombination of different paths
remain separate issues.

## 4. Fixed-depth inversion

Fix \(S,M,\nu>0\), \(m<\infty\), and \(\beta>0\).  Along a sequence
\(h\downarrow0\), take

\[
R_0(h)\asymp h^{-\beta}.
\tag{34}
\]

Assume that this prescribed component carries a fixed pressure floor:

\[
\mathfrak R_{\boldsymbol R}(h)\ge\eta>0.
\tag{35}
\]

Using (7), the scale--clock factor in (6) obeys

\[
\frac{S}{R_0}\Theta_{\boldsymbol R}(h)
\lesssim
h^{p(\beta)},
\qquad
p(\beta):=
\beta+(1-2\beta)_+.
\tag{36}
\]

For fixed \(m\), \(A^{m+1}\) is independent of \(h\).  The constant
term and every explicit positive power in (4), multiplied by (36),
tend to zero.  Equations (6) and (35) therefore force

\[
\log_+\!\bigl(D_b(h)h^3\bigr)
\ge
c_mh^{-\{7/4+p(\beta)\}},
\tag{37}
\]

for all sufficiently small \(h\).  This proves (9), since

\[
\begin{aligned}
\frac74+p(\beta)
&=
\frac74+\beta+(1-2\beta)_+\\
&=
\frac94+\left|\beta-\frac12\right|.
\end{aligned}
\tag{38}
\]

The antecedent (35) is not derived.

## 5. Logarithmically growing depth

The preceding inversion needs a minor but important qualification when
the depth depends on \(h\).  Retain \(M>0\), so \(A>0\), and suppose

\[
m(h)\le\kappa\log(1/h),
\tag{39}
\]

and put

\[
\delta:=
\kappa\log_+A,
\qquad
\log_+A:=\max\{0,\log A\}.
\tag{40}
\]

Then

\[
A^{m(h)+1}
\le
\max\{1,A\}h^{-\delta}.
\tag{41}
\]

The coarse clock bound (7) consequently gives

\[
\mathfrak R_{\boldsymbol R}(h)
\lesssim
h^{p(\beta)-\delta}
\left\{
1+h^{7/4}
\left[
1+\log_+\!\bigl(D_b(h)h^3\bigr)
\right]
+o(h^{7/4})
\right\}.
\tag{42}
\]

To infer a dissipation cost from a fixed path floor using (42), one
must require

\[
\boxed{\delta<p(\beta),}
\tag{43}
\]

not merely
\(\delta<7/4+p(\beta)\).  Otherwise the constant term in
\(\mathcal B\) need not vanish and the upper bound cannot identify the
logarithmic term as the payer.

Under (43), the fixed floor implies

\[
\boxed{
D_b(h)
\ge
h^{-3}
\exp\!\left(
c h^{-\{\gamma_1(\beta)-\delta\}}
\right).
}
\tag{44}
\]

The exact clock ceilings (28) and (33) can be much stronger than this
coarse ledger and may absorb \(A^{m+1}\) without the restriction (43).

## 6. What this closes, and what it does not

The theorem closes one possible loophole:

> No prescribed finite sequence of annular Oseen transitions can
> recover the inverse initial frequency by multiplying intermediate
> cross-band scale ratios.  Those ratios telescope, leaving
> \(S/R_0\).

The dyadic corollary adds:

> A prescribed logarithmic-depth descent containing logarithmically
> many subparabolic dyadic clocks has a super-polynomially small heat
> clock, which beats any fixed interaction constant raised to that
> depth.

It does **not** establish any of the following:

1. a convergent decomposition of the complete returned-low state into
   the components (16);
2. an admissible count of all frequency itineraries;
3. an estimate for cancellations or reinforcement when their pressure
   outputs recombine;
4. a positive floor such as (35);
5. non-reuse of the coefficient field or physical dissipation along
   different paths;
6. blow-up or regularity of an Oseen or Navier--Stokes solution; or
7. any Clay alternative.

The remaining frequency gate is therefore no longer a scale-factor
question for one path.  It is a path decomposition, entropy,
recombination, or participation question.

## 7. Executable certificate

The exact telescoping, simplex clock, dyadic exponent, and
fixed/logarithmic-depth exponent ledgers are checked by

```bash
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_multistage_path -v
PYTHONPATH=lab python -m \
  navier_lab.adjoint_pressure_multistage_path
```
