# Spatial shell localisation amplifies a terminal frequency return

- **Experiment:** EXP-ADJOINT-PRESSURE-SPATIAL-FREQUENCY-001
- **Route:** ROUTE-R3B
- **Status:** conditional analytic reduction;
  [adversarially recomputed valid after repair](../review-ledger.md)
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** adversarially recomputed
  [feedback-shell theorem](adjoint-pressure-feedback-shells.md),
  [intermediate-localisation theorem](adjoint-pressure-intermediate-localization.md),
  and [terminal-return theorem](adjoint-pressure-terminal-return.md)

The terminal-return theorem gives an \(S/F\) gain when an adjoint state
above frequency \(F\) returns pressure to a fixed output band \(S\).
Applied globally, that estimate sees the square root of the entire
coefficient dissipation, which can be stretched-exponentially large.
The feedback-shell theorem contains more information: on a spatial
annulus of radius \(L_k\), coefficient dissipation is at most \(CL_k\),
while the zero-data state has an \(L^2_{t,x}\) tail of size
\(h^{7/4}L_k^{-1/2}\).  These powers cancel shell by shell.

Combining the two estimates gives a stronger conclusion.  If a fixed
low-band pressure packet is simultaneously:

1. in the high state tail above \(F\); and
2. on the surviving spatially exterior feedback branch,

then

\[
\boxed{
D_b(h)
\ge
h^{-3}
\exp\!\left(c\frac FS h^{-7/4}\right).
}
\tag{1}
\]

Thus frequency escape multiplies, rather than merely adds to, the
existing logarithmic spatial-shell depth.

At the hypothetical dyadic causal top frequency

\[
F(h)=2^{\lfloor c_{\rm dep}\log(1/h)\rfloor}
\asymp h^{-\alpha_{\rm dep}},
\qquad
\alpha_{\rm dep}:=c_{\rm dep}\log2,
\tag{2}
\]

equation (1) becomes

\[
\boxed{
D_b(h)
\ge
h^{-3}
\exp\!\left(
c h^{-(7/4+\alpha_{\rm dep})}
\right).
}
\tag{3}
\]

This is a strict improvement over the reviewed
\(h^{-3}\exp(c h^{-7/4})\) floor.  It is still a cost, not a
contradiction.

## 1. Reviewed spatial ledgers

Retain the zero-data feedback remainder \(r\) and coefficient \(b\) on
\((0,h)\).  The reviewed energy and exterior-tail bounds are

\[
\boxed{
\int_0^h\|r(t)\|_2^2\,dt\le C_rh^3,
}
\tag{4}
\]

\[
\boxed{
\int_0^h
\|r(t)\|_{L^2(|x|>2L)}^2\,dt
\le
C_T\left(
h^{7/2}L^{-1}
+h^{5/2}L^{-15}
\right)
}
\tag{5}
\]

for \(L\ge2\).

Put

\[
R_0:=h^{-3}.
\tag{6}
\]

Use the reviewed source cutoff \(c_{\rm in}=\chi_{R_0}b\), and decompose
the exterior coefficient into annular pieces

\[
b=c_{\rm in}+\sum_{k\ge0}c_k,
\qquad
L_k:=2^kR_0,
\tag{7}
\]

where \(c_k\) is supported in a fixed enlargement of
\(\{L_k\lesssim|x|\lesssim L_k\}\).  Write

\[
D_k
:=
\int_0^h
\|\nabla b(t)\|_{L^2(A_k')}^2\,dt,
\qquad
Y_k
:=
\left(
\int_0^h\|\nabla c_k(t)\|_2^2\,dt
\right)^{1/2}.
\tag{8}
\]

The reviewed local-energy, weak-\(L^3\), and finite-overlap estimates
give

\[
\boxed{
\sum_{k\ge0}D_k\le CD_b(h),
\qquad
D_k\le CL_k,
}
\tag{9}
\]

\[
\boxed{
Y_k
\le
C\left(
\sqrt{D_k}
+h^{1/2}L_k^{-1/2}
\right).
}
\tag{10}
\]

The same local-energy calculation gives the inner budget on every
feedback layer, independently of which shell alternative survives:

\[
\boxed{
\int_0^h\|\nabla c_{\rm in}(t)\|_2^2\,dt
\le
C_{\rm in}h^{-3}.
}
\tag{11}
\]

Indeed, the coefficient-gradient term costs \(CR_0\), while the cutoff
term is bounded by
\[
CR_0^{-2}\int_0^h\|b\|_{L^2(B_{8R_0})}^2\,dt
\lesssim hR_0^{-1}.
\]

Let

\[
X_k
:=
\left(
\int_0^h
\|r(t)\|_{L^2(|x|>cL_k)}^2\,dt
\right)^{1/2}.
\tag{12}
\]

Equation (5) gives

\[
\boxed{
X_k
\le
C\left(
h^{7/4}L_k^{-1/2}
+h^{5/4}L_k^{-15/2}
\right).
}
\tag{13}
\]

The logarithmic shell calculation already reviewed in the input note
then yields

\[
\boxed{
\begin{aligned}
\sum_{k\ge0}X_kY_k
\le C\bigg[
&h^{7/4}
\left(
1+\log_+\!\bigl(D_b(h)h^3\bigr)
\right)\\
&+h^{21/4}
+h^{89/4}
+h^{103/4}
\bigg].
\end{aligned}}
\tag{14}
\]

## 2. A spatially local terminal-return lemma

Use the Littlewood--Paley conventions of the terminal-return theorem.
Let

\[
\Pi_S:=S_S\mathbb Q\operatorname{div},
\qquad
P_{>4F}:=\sum_{K>4F}\Delta_K,
\tag{15}
\]

where throughout this note

\[
(z\otimes c)_{ij}:=c_i z_j.
\]

Thus, when \(z\) is solenoidal,

\[
\operatorname{div}(z\otimes c)=(z\cdot\nabla)c,
\qquad
\Pi_S(z\otimes c)=S_S\mathcal T(z,c).
\]

This convention is the transpose of the convention sometimes used for
the transport \(c\cdot\nabla z\).  The global pressure projection agrees
for the two transport orders when both fields are solenoidal; the
frequency and tensor-norm estimate below is unchanged by transposition.
Suppose \(F\ge16S\).

**Lemma.**  Let \(c\in H^1(\mathbb R^3)\) be supported in a fixed-shape
annulus \(A_L\) of radius \(L\), with \(FL\ge16\).  Fix nested
fixed-shape enlargements

\[
A_L\Subset A_L^+\Subset A_L^{++}
\]

whose two separating distances are comparable to \(L\).  For every
\(z\in L^2(\mathbb R^3)\),

\[
\boxed{
\begin{aligned}
\|\Pi_S((P_{>4F}z)\otimes c)\|_1
\le
C\frac SF
\bigg[
&\|z\|_{L^2(A_L^{++})}\\
&+(FL)^{-2}\|z\|_2
\bigg]
\|\nabla c\|_2.
\end{aligned}}
\tag{16}
\]

Here \(A_L^{++}\) is one fixed enlargement of the support annulus, and
the constant is independent of \(F\) and \(L\).

### Proof

Low output below \(S\) from a state frequency \(K>4F\) sees only
coefficient frequencies comparable to \(K\).  Therefore the exact
support identity used in the terminal-return theorem is

\[
\boxed{
\Pi_S\bigl((P_{>4F}z)\otimes c\bigr)
=
\sum_{K>4F}
\Pi_S\left(
\Delta_Kz\otimes\widetilde\Delta_Kc
\right).
}
\tag{17}
\]

In the upper bounds below this exact sum may be enlarged to
\(K\ge2F\).

The low-output pressure multiplier has \(L^1\) kernel norm \(O(S)\).
The Schwartz kernels of \(\Delta_K\) and
\(\widetilde\Delta_K\) also give the off-diagonal estimates

\[
\|\Delta_Kz\|_{L^2(A_L^+)}
\le
C\left[
\|z\|_{L^2(A_L^{++})}
+(KL)^{-2}\|z\|_2
\right],
\tag{18}
\]

\[
\|\widetilde\Delta_Kc\|_{L^2((A_L^+)^c)}
\le
CK^{-1}(KL)^{-2}\|\nabla c\|_2.
\tag{19}
\]

Split the product in (17) across \(A_L^+\), use (18)--(19), and use
annular Bernstein on the coefficient factor.  This gives

\[
\begin{aligned}
\|\Pi_S(
\Delta_Kz\otimes\widetilde\Delta_Kc
)\|_1
\le
CSK^{-1}
\bigg[
&\|z\|_{L^2(A_L^{++})}
\|\widetilde\Delta_K\nabla c\|_2\\
&+(KL)^{-2}
\|z\|_2\|\nabla c\|_2
\bigg].
\end{aligned}
\tag{20}
\]

Finally,

\[
\sum_{K\ge2F}
K^{-1}
\|\widetilde\Delta_K\nabla c\|_2
\le
\left(\sum_{K\ge2F}K^{-2}\right)^{1/2}
\left(
\sum_K\|\widetilde\Delta_K\nabla c\|_2^2
\right)^{1/2}
\le
CF^{-1}\|\nabla c\|_2,
\tag{21}
\]

while the off-diagonal geometric sum is at most
\(CF^{-1}(FL)^{-2}\).  Equations (20)--(21) prove (16).

The same proof applies to fixed-shape balls.  This lemma is a
frequency-resolved refinement of the spatial shell estimate, not a new
regularity assumption.

For the application below, the raw pieces \(c_k=\chi_kb\) satisfy the
lemma.  Indeed, weak \(L^3\) on each finite annulus gives the required
local \(L^2\) control and

\[
\nabla c_k
=
\chi_k\nabla b+b\otimes\nabla\chi_k
\in L^2.
\]

## 3. Complete high-state exterior estimate

Define the selected low-output high-state pressure

\[
\mathfrak P_{S,F}(h)
:=
\int_0^h
\left\|
\Pi_S\bigl(
(P_{>4F}r(t))\otimes b(t)
\bigr)
\right\|_1\,dt.
\tag{22}
\]

For the inner coefficient, the global terminal-return estimate, (4),
and (11) give

\[
\begin{aligned}
\mathfrak P_{S,F}^{\rm in}(h)
&\le
C\frac SF
\left(
\int_0^h\|r(t)\|_2^2dt
\right)^{1/2}
\left(
\int_0^h\|\nabla c_{\rm in}(t)\|_2^2dt
\right)^{1/2}\\
&\le C\frac SF.
\end{aligned}
\tag{23}
\]

Apply (16) to every exterior shell and use Cauchy--Schwarz in time.
Equations (12)--(14) control the local part.  For the off-diagonal
part, (4), (9), and (10) give

\[
\begin{aligned}
&\left(
\int_0^h\|r(t)\|_2^2dt
\right)^{1/2}
F^{-2}
\sum_{k\ge0}L_k^{-2}Y_k\\
&\qquad\le
Ch^{3/2}F^{-2}R_0^{-3/2}
\le
Ch^6F^{-2}.
\end{aligned}
\tag{24}
\]

Summing (16), adding (23), and using (14) proves

\[
\boxed{
\begin{aligned}
\mathfrak P_{S,F}(h)
\le
C\frac SF\bigg\{
1
&+h^{7/4}
\left[
1+\log_+\!\bigl(D_b(h)h^3\bigr)
\right]\\
&+h^{21/4}
+h^{89/4}
+h^{103/4}
+h^6F^{-2}
\bigg\}.
\end{aligned}}
\tag{25}
\]

This is the claimed spatial--frequency amplification estimate.

## 4. Inverting a fixed high-tail pressure floor

Fix \(S>0\).  Suppose that along a selected sequence \(h\downarrow0\),

\[
F(h)\ge16S,
\qquad
F(h)\longrightarrow\infty,
\tag{26}
\]

and

\[
\boxed{
\mathfrak P_{S,F(h)}(h)\ge p_{\rm sf}>0.
}
\tag{27}
\]

The high-state floor (27) is an additional antecedent.  It is not
inferred from the fixed floor for the complete feedback pressure, from
survival on the exterior spatial-shell branch, or from logarithmically
divergent causal interaction depth.

For all sufficiently small selected \(h\), equations (25)--(27) force

\[
\boxed{
\log\!\bigl(D_b(h)h^3\bigr)
\ge
c_{\rm sf}
\frac{F(h)}S h^{-7/4}.
}
\tag{28}
\]

Equivalently,

\[
\boxed{
D_b(h)
\ge
h^{-3}
\exp\!\left(
c_{\rm sf}\frac{F(h)}S h^{-7/4}
\right).
}
\tag{29}
\]

For \(F(h)=h^{-\beta}\), with fixed \(S\) and \(\beta>0\),

\[
\boxed{
D_b(h)
\ge
h^{-3}
\exp\!\left(
c h^{-(7/4+\beta)}
\right).
}
\tag{30}
\]

In particular, using the dyadic frequency in (2) gives (3).

The earlier terminal-return theorem by itself gives only the polynomial
tail floor

\[
D_{b,>F}(h)\gtrsim F^2h^{-3}.
\tag{31}
\]

Equation (29) is stronger because it also uses the spatial genealogy of
the same zero-data state and the centre-uniform local-energy cap on
every coefficient shell.

## 5. Physical scaling and exact surviving boundary

On one common physical trajectory at zoom \(\sigma_h\), the selected
layer dissipation is

\[
E_h=\sigma_hD_b(h)\longrightarrow0.
\tag{32}
\]

Equations (29) and (32) imply

\[
\boxed{
\sigma_h
=
o\!\left[
h^3
\exp\!\left(
-c_{\rm sf}\frac{F(h)}S h^{-7/4}
\right)
\right].
}
\tag{33}
\]

At the dyadic logarithmic depth this is

\[
\boxed{
\sigma_h
=
o\!\left(
h^3e^{-c h^{-(7/4+\alpha_{\rm dep})}}
\right).
}
\tag{34}
\]

This is a strictly stronger necessary zoom law than the preceding
polynomial ancestry ceiling.  It still does not contradict finite
physical dissipation: the scalar nested-history construction can
accelerate the zoom beyond any prescribed stretched-exponential floor.

## 6. Exact route consequence

The theorem closes one concrete part of the spatial/frequency gap:

> A fixed low-output pressure packet cannot simultaneously live above a
> growing state frequency \(F\) and use the exterior shell genealogy
> while paying only the old
> \(h^{-3}e^{c h^{-7/4}}\) coefficient cost.

At the reviewed dyadic logarithmic depth, such a packet forces the
strictly stronger exponent
\(7/4+\alpha_{\rm dep}\).  Therefore every surviving feedback sequence
has an exhaustive frequency alternative:

1. the selected low-output packet is not uniformly carried by the state
   tail above the proposed \(F(h)\); or
2. coefficient dissipation and physical zoom obey (29) and (33).

This does not prove that causal interaction depth produces the
frequency \(F(h)=2^{N(h)}\); interaction order and frequency ascent are
different statements.  It does not make nested physical dissipation
charges non-reusable, construct an Oseen or Navier--Stokes singularity,
prove regularity, or resolve any Clay alternative A--D.

The next sharp question is whether the surviving below-\(F\) packet can
persist through \(N(h)\) causal interactions without either making a
high excursion or entering a frequency corridor to which the reviewed
factorial colligation theorem applies.

## Reproduce

```bash
make adjoint-pressure-spatial-frequency
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_spatial_frequency -v
make check
```
