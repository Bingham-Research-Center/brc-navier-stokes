# A finite weighted transfer budget forces q4 spectral-shell broadening

- **Experiment:** EXP-TYPE-II-SPECTRAL-QUANTILE-SPEED-001
- **Route:** ROUTE-R3C
- **Status:** complete conditional reduction with sharp broad-shell survivor;
  external review pending
- **Domain:** smooth finite-energy Navier--Stokes entrance on \(\mathbb R^3\)
- **Clay status:** unsolved
- **Input:** [radial triad spectrum](type-ii-radial-triad-spectrum.md)

## Verdict

The radial nonlinear transfer has a finite same-trajectory norm that was
invisible in the unweighted Gaussian-band budget.  Let

\[
\varepsilon_s(d\lambda)=e(\lambda,s)\,d\lambda,
\qquad
\mu_s(d\lambda)=m(\lambda,s)\,d\lambda
\tag{1}
\]

be the positive energy density and signed transfer density from the
preceding round, so

\[
\partial_se=m-\lambda e.
\tag{2}
\]

Define

\[
\boxed{
\mathfrak q(s)
:=
\int_0^\infty
\lambda^{-1/2}|m(\lambda,s)|\,d\lambda.
}
\tag{3}
\]

The exact quadratic relation and \(\dot H^{-1}\)--\(L^2\) duality give

\[
\boxed{
\mathfrak q(s)
\lesssim
\nu^{-1/2}\|v(s)\|_2
\|F(s)\|_{\dot H^{-1}}
\lesssim
\nu^{-1/2}\sqrt d\,M(s)Y(s),
}
\tag{4}
\]

where

\[
F=\mathbb P((U\cdot\nabla)v),
\quad
M=\|U\|_{L^{3,\infty}},
\quad
Y=\|\nabla v\|_2.
\tag{5}
\]

Consequently

\[
\boxed{
\int_0^{s_0}\mathfrak q(s)\,ds<\infty.
}
\tag{6}
\]

This is a real finite physical budget because \(M,Y\in L^2_s\).

Fix a physical low-frequency energy amount

\[
0<\eta<d/2
\tag{7}
\]

and define its radial quantile by

\[
\int_0^{\Lambda_\eta(s)}
e(\lambda,s)\,d\lambda
=
\eta.
\tag{8}
\]

Whenever this quantile is nondegenerate,

\[
\boxed{
e(\Lambda_\eta,s)\Lambda_\eta'
=
\int_0^{\Lambda_\eta}\lambda e(\lambda,s)\,d\lambda
-
\int_0^{\Lambda_\eta}m(\lambda,s)\,d\lambda.
}
\tag{9}
\]

On the descending-frequency set

\[
\mathcal D_\eta
:=
\{s:\Lambda_\eta'(s)<0\},
\tag{10}
\]

equations (3) and (9) imply

\[
\boxed{
\int_{\mathcal D_\eta}
e(\Lambda_\eta(s),s)
\frac{|\Lambda_\eta'(s)|}
{\sqrt{\Lambda_\eta(s)}}\,ds
\le
\int_0^{s_0}\mathfrak q(s)\,ds
<\infty.
}
\tag{11}
\]

This is the exact quantile-speed charge.

It closes the dynamically adjacent-shell version of the Pell survivor.
Suppose along all sufficiently small times

\[
\Lambda_\eta(s)\asymp
L(s):=s^{-9/11}\ell(s)^{2/11},
\tag{12}
\]

\[
-\Lambda_\eta'(s)\gtrsim\frac{L(s)}s,
\tag{13}
\]

and define the effective local spectral width

\[
W_\eta(s)
:=
\frac{\eta}{e(\Lambda_\eta(s),s)}.
\tag{14}
\]

Then (11) forces

\[
\boxed{
\int_0
\frac{\sqrt{L(s)}}{sW_\eta(s)}\,ds<\infty.
}
\tag{15}
\]

In particular,

\[
\boxed{
W_\eta(s)\lesssim\sqrt{L(s)}
\quad\hbox{for every sufficiently small }s
}
\tag{16}
\]

is impossible.  An adjacent Pell pair has absolute
\(\lambda\)-width \(O(1)\), far below \(\sqrt L\).  Thus a
nondegenerate \(O(1)\)-width smoothing of such pairs cannot carry one
fixed energy quantile down the q4 shell at every small time.  The exact
atomic torus snapshots are outside the density hypothesis of the
quantile theorem and remain valid.

The conclusion is broadening, not q4 closure.  Choose a smooth probability
density

\[
\phi\in C_c^\infty((0,\infty)),
\qquad
0<a<1<b,
\qquad
\operatorname{supp}\phi=[a,b],
\qquad
\phi>0\quad\hbox{on }(a,b),
\qquad
\int\phi(y)\,dy
=
\int y\phi(y)\,dy
=1.
\tag{17}
\]

With the same \(L(s)\) as (12), put

\[
A(s)
:=
\frac d2
\exp\left(-\int_0^sL(\sigma)\,d\sigma\right),
\tag{18}
\]

\[
\boxed{
e_\phi(\lambda,s)
:=
\frac{A(s)}{L(s)}
\phi\left(\frac{\lambda}{L(s)}\right).
}
\tag{19}
\]

Its heat energy is

\[
\mathcal E_\phi(r,s)
=
A(s)\Phi(rL(s)),
\qquad
\Phi(x):=\int_0^\infty e^{-xy}\phi(y)\,dy,
\tag{20}
\]

and its exact characteristic transfer is

\[
\boxed{
\begin{aligned}
\Pi^\phi_r(s)
&=
(\partial_s-\partial_r)\mathcal E_\phi(r,s)\\
&=
\frac{A(s)}s
\left[
\alpha(s)xG(x)
-
sL(s)\bigl(\Phi(x)+\Phi'(x)\bigr)
\right],
\end{aligned}
}
\tag{21}
\]

where

\[
x:=rL(s),
\qquad
G(x):=-\Phi'(x)>0,
\qquad
\alpha(s):=-\frac{sL'(s)}{L(s)}.
\tag{22}
\]

This smooth positive spectrum:

1. has total energy \(A(s)\to d/2\);
2. has mean spectral frequency \(L(s)\);
3. has \(\Pi^\phi_r(s)>0\) for every \(r>0\) at all sufficiently small
   times;
4. satisfies the exact energy, characteristic, diagonal, and recycling
   laws;
5. reproduces the q4 \(M^2\), \(Y^2\), and \(MY^2\) ledgers;
6. obeys the pointwise heat and Gaussian-variation bounds;
7. places asymptotically all diagonal work in every fixed early-history
   fraction;
8. has quantile width \(W_\eta(s)\asymp L(s)\); and
9. pays the finite transfer budget because
   \[
   \mathfrak q_\phi(s)
   \lesssim
   A(s)
   \left(
   \sqrt{L(s)}
   +
   \frac1{s\sqrt{L(s)}}
   \right)
   \in L^1_s.
   \tag{23}
   \]

Thus the finite charge rules out persistent shells of width at most
\(\sqrt L\), including adjacent Pell shells, but a fixed-relative-width
shell remains exactly compatible with every current radial and temporal
budget.  The first Pell triad, dilated to high frequency, already shows
that fixed-relative-width positive quadratic transfer is instantaneously
admissible.

The exact live gate is now:

> Prove that the full-defect q4 entrance cannot broaden a fixed positive
> energy quantile to \(\lambda\)-width \(W_\eta\gg\sqrt L\) while
> repeatedly realising the required same-trajectory triadic transfer,
> or charge that broadening to a finite spatial, angular, or genealogical
> budget.

No such theorem is established here.  No Clay alternative is proved.

## 1. Radial energy balance

The preceding round proved

\[
\mu_s
=
\partial_s\varepsilon_s+\lambda\varepsilon_s
\tag{24}
\]

in radial spectral distributions.  At each positive smooth time the
Fourier pairings are integrable, so the pushforwards have densities away
from \(\lambda=0\).  Equation (24) becomes (2).

For later comparison, define

\[
\mathcal C(\Lambda,s)
:=
\int_0^\Lambda e(\lambda,s)\,d\lambda.
\tag{25}
\]

The fixed-heat boundary implies

\[
\mathcal C(\Lambda,s)\longrightarrow0
\qquad(s\downarrow0)
\tag{26}
\]

for every fixed \(\Lambda\).  Indeed, for any fixed \(r>0\),

\[
\mathcal C(\Lambda,s)
\le
e^{r\Lambda}\mathcal E(r,s)
\longrightarrow0.
\tag{27}
\]

Since the total energy tends to \(d/2\), every fixed quantile (7) exists
for sufficiently small positive \(s\) and satisfies

\[
\Lambda_\eta(s)\longrightarrow\infty.
\tag{28}
\]

## 2. A finite weighted nonlinear-transfer norm

### Theorem 1: the \(\lambda^{-1/2}\) transfer budget

Equations (4) and (6) hold.

#### Proof

Total variation cannot increase under radial pushforward.  Therefore

\[
\begin{aligned}
\mathfrak q(s)
&\le
\int_{\mathbb R^3}
(2\nu|\xi|^2)^{-1/2}
|\widehat F(s,\xi)|
|\widehat v(s,\xi)|\,d\xi\\
&\le
(2\nu)^{-1/2}
\|F(s)\|_{\dot H^{-1}}
\|v(s)\|_2.
\end{aligned}
\tag{29}
\]

For every solenoidal test field \(\psi\),

\[
\begin{aligned}
|\langle F,\psi\rangle|
&=
\left|
\int_{\mathbb R^3}
U_jv_i\partial_j\psi_i\,dx
\right|\\
&\lesssim
\|U\|_{L^{3,\infty}}
\|v\|_{L^{6,2}}
\|\nabla\psi\|_2\\
&\lesssim
MY\|\nabla\psi\|_2.
\end{aligned}
\tag{30}
\]

Thus

\[
\|F\|_{\dot H^{-1}}\lesssim MY.
\tag{31}
\]

The energy identity bounds \(\|v\|_2\le\sqrt d\), proving (4).
Finally,

\[
\int_0^{s_0}M(s)Y(s)\,ds
\le
\left(\int_0^{s_0}M^2\right)^{1/2}
\left(\int_0^{s_0}Y^2\right)^{1/2}
<\infty,
\tag{32}
\]

which proves (6).

### Interpretation

The unweighted total variation of \(\mu_s\) costs \(MY^2\) and diverges.
Multiplication by \(\lambda^{-1/2}\), one physical heat length, moves one
derivative from the transfer to the finite kinetic-energy factor.  This
turns the charge into \(MY\), whose time integral is finite.

## 3. Exact quantile speed

### Theorem 2: fixed-energy quantile law

Assume \(e\) is continuous and positive at
\(\lambda=\Lambda_\eta(s)\), and the quantile is differentiable.  Then
(9) holds.  On \(\mathcal D_\eta\), the finite charge (11) holds.

#### Proof

Differentiate (8), use (2), and obtain

\[
\begin{aligned}
0
&=
\int_0^{\Lambda_\eta}
\bigl(m-\lambda e\bigr)\,d\lambda
+
e(\Lambda_\eta,s)\Lambda_\eta'.
\end{aligned}
\]

This is (9).  If \(\Lambda_\eta'<0\), then

\[
\begin{aligned}
e(\Lambda_\eta,s)|\Lambda_\eta'|
&=
\int_0^{\Lambda_\eta}m\,d\lambda
-
\int_0^{\Lambda_\eta}\lambda e\,d\lambda\\
&\le
\left|
\int_0^{\Lambda_\eta}m\,d\lambda
\right|\\
&\le
\int_0^{\Lambda_\eta}|m|\,d\lambda\\
&\le
\sqrt{\Lambda_\eta}\,\mathfrak q(s).
\end{aligned}
\tag{33}
\]

Divide by \(\sqrt{\Lambda_\eta}\), integrate, and use (6).

### Smooth heat-quantile version

The same shell motion has a density-free Gaussian formulation.  Let
\(r_\theta(s)\) solve

\[
\mathcal E(r_\theta(s),s)
=
\theta\mathcal E(0,s),
\qquad 0<\theta<1.
\tag{34}
\]

Put

\[
\mathcal D(r,s)
:=
-\partial_r\mathcal E(r,s)
=
\nu\|\nabla e^{\nu r\Delta}v(s)\|_2^2.
\tag{35}
\]

Differentiating (34) and using
\(\Pi=(\partial_s-\partial_r)\mathcal E\) gives

\[
\boxed{
r_\theta'(s)
=
\frac{
\Pi_{r_\theta(s)}(s)
+
\theta\mathcal D(0,s)
}{
\mathcal D(r_\theta(s),s)
}
-1.
}
\tag{36}
\]

Equation (36) separates nonlinear shell motion from the spectral
dispersion caused by preferential viscous loss.

## 4. The q4 narrowing obstruction

Define the effective quantile width by (14).  On the moving-shell schedule
(12)--(13), the integrand in (11) obeys

\[
e(\Lambda_\eta,s)
\frac{|\Lambda_\eta'|}{\sqrt{\Lambda_\eta}}
\gtrsim
\frac{\eta\sqrt{L(s)}}{sW_\eta(s)}.
\tag{37}
\]

### Corollary 3: persistent narrow shells are impossible

Equation (15) holds.  In particular, (16) contradicts the finite transfer
budget.

#### Proof

Substitute (12)--(14) into (11).  If (16) held eventually, the resulting
integrand would be bounded below by a positive multiple of \(1/s\).

### Consequence for Pell transfer

The Pell triads from the preceding round transfer between

\[
\lambda_m=8\nu m^2,
\qquad
\lambda_m+2\nu.
\tag{38}
\]

Their absolute shell gap is fixed.  Therefore a hypothetical
nondegenerate \(O(1)\)-width smoothing carrying a fixed \(\eta\) in
those adjacent shells would have

\[
W_\eta=O(1)\ll\sqrt{\lambda_m},
\tag{39}
\]

and cannot persist along the continuous q4 descent.  The exact atomic
Pell snapshots do not satisfy the density hypothesis used here and
remain valid; their proposed identification with one narrow moving
spectral shell is closed.

More generally, if

\[
W_\eta(s)=L(s)^\gamma
\tag{40}
\]

up to fixed factors, then (15) requires

\[
\gamma>\frac12
\tag{41}
\]

at the power level.  The endpoint \(\gamma=1/2\) already costs
\(\int ds/s\) before logarithmic improvements.

## 5. A smooth broad-shell survivor

Choose \(\phi\) as in (17) and define (18)--(20).  Its mass and mean are

\[
\int_0^\infty e_\phi(\lambda,s)\,d\lambda=A(s),
\tag{42}
\]

\[
\int_0^\infty
\lambda e_\phi(\lambda,s)\,d\lambda
=
A(s)L(s).
\tag{43}
\]

Since

\[
A'(s)=-A(s)L(s),
\tag{44}
\]

the exact half-energy identity holds.

### Proposition 4: broad-shell characteristic flux

Equation (21) holds.  The spectrum is positive and smooth, and its
characteristic transfer density is

\[
\boxed{
\begin{aligned}
m_\phi(\lambda,s)
=
A(s)
\biggl[
\left(\frac{\lambda}{L(s)}-1\right)
\phi\left(\frac{\lambda}{L(s)}\right)
\\
\qquad
-
\frac{L'(s)}{L(s)^2}
\left(
\phi\left(\frac{\lambda}{L(s)}\right)
+
\frac{\lambda}{L(s)}
\phi'\left(\frac{\lambda}{L(s)}\right)
\right)
\biggr].
\end{aligned}
}
\tag{45}
\]

For every sufficiently small \(s>0\),

\[
\boxed{
\Pi^\phi_r(s)>0
\qquad\hbox{for every }r>0.
}
\tag{46}
\]

#### Proof

The heat transform of (19) is (20).  Differentiate it:

\[
\partial_s\mathcal E_\phi
=
A'\Phi+ArL'\Phi',
\qquad
\partial_r\mathcal E_\phi
=
AL\Phi'.
\]

Use (22) and (44) to obtain (21).  Direct differentiation of (19),
followed by \(m_\phi=\partial_se_\phi+\lambda e_\phi\), gives (45).

For positivity, introduce the exponentially tilted mean

\[
\overline y(x)
:=
\frac{G(x)}{\Phi(x)}.
\tag{47}
\]

It obeys, with \(\operatorname{Var}_x\) taken under the probability
density \(e^{-xy}\phi(y)/\Phi(x)\),

\[
\overline y(0)=1,
\qquad
\overline y'(x)
=
-\operatorname{Var}_x(y)<0.
\tag{48}
\]

Therefore

\[
H(x):=\Phi(x)+\Phi'(x)
=
\Phi(x)(1-\overline y(x))>0
\qquad(x>0).
\tag{49}
\]

Moreover,

\[
C_\phi
:=
\sup_{x>0}\frac{H(x)}{xG(x)}
<\infty.
\tag{50}
\]

Indeed, the quotient tends to the variance of \(\phi\) as \(x\downarrow0\)
and to zero as \(x\to\infty\), because the tilted mean tends to
\(a>0\).  Since \(\alpha(s)\to9/11\) and \(sL(s)\to0\), (21) gives

\[
\Pi^\phi_r(s)
\ge
\frac{A(s)}s xG(x)
\bigl(\alpha(s)-sL(s)C_\phi\bigr)>0
\tag{51}
\]

for all \(x>0\) and every sufficiently small \(s\).

### Proposition 5: all current q4 budgets survive

Set

\[
M_\phi(s):=\frac1{sL(s)},
\qquad
Y_\phi(s)^2:=\frac{A(s)L(s)}{\nu}.
\tag{52}
\]

Then

\[
\int_0^hM_\phi^2
\asymp
h^{7/11}\ell(h)^{-4/11},
\tag{53}
\]

\[
\int_0^hY_\phi^2
\asymp
h^{2/11}\ell(h)^{2/11},
\qquad
M_\phi Y_\phi^2
=
\frac{A(s)}{\nu s}.
\tag{54}
\]

Moreover,

\[
|\Pi^\phi_r(s)|
\lesssim
r^{-1/2}M_\phi(s)Y_\phi(s),
\tag{55}
\]

\[
\operatorname{Var}_{r>0}\Pi^\phi_r(s)
\lesssim
\frac{A(s)}s,
\tag{56}
\]

and for every fixed \(0<q<1\),

\[
\frac{
\int_0^{q\tau}\Pi^\phi_{\tau-s}(s)\,ds
}{
\int_0^\tau\Pi^\phi_{\tau-s}(s)\,ds
}
\longrightarrow1.
\tag{57}
\]

Finally, (23) holds, so the finite budget (6) is respected.

#### Proof

The power--log statements follow exactly as in the delta-shell model.
For (55), put \(x=rL(s)\).  The motion profile

\[
xG(x)
\tag{58}
\]

and the dispersion profile

\[
\Phi(x)+\Phi'(x)
\tag{59}
\]

are smooth and exponentially decreasing.  Because \(\int y\phi=1\),
the second profile vanishes at \(x=0\).  Thus

\[
x^{1/2}|xG(x)|
+
x^{1/2}|\Phi(x)+\Phi'(x)|
\lesssim1.
\tag{60}
\]

The motion coefficient is \(A/s\).  The dispersion coefficient is
\(AL\), smaller by the factor \(sL\to0\).  Comparing with

\[
r^{-1/2}M_\phi Y_\phi
=
\sqrt{\frac{A(s)}{\nu}}\,
\frac{x^{-1/2}}s
\tag{61}
\]

proves (55).  The same profiles have finite total variation, proving
(56).

The diagonal integral equals \(A(\tau)\) by the characteristic law and
the fixed-heat boundary.  On \(q\tau\le s\le\tau\), the motion term is
\(O_q(\tau L(q\tau))\) after integration.  Since (59) vanishes linearly
at zero, the dispersion term is

\[
O_q\bigl((\tau L(q\tau))^2\bigr).
\tag{62}
\]

Both tend to zero, proving (57).

For (23), substitute \(y=\lambda/L(s)\) in (45).  Compact support away
from zero gives

\[
\mathfrak q_\phi(s)
\lesssim
A(s)
\left[
\sqrt{L(s)}
+
\frac{|L'(s)|}{L(s)^{3/2}}
\right].
\tag{63}
\]

Since

\[
\frac{|L'(s)|}{L(s)^{3/2}}
\asymp
\frac1{s\sqrt{L(s)}},
\tag{64}
\]

the two singular powers are

\[
s^{-9/22}\ell(s)^{1/11},
\qquad
s^{-13/22}\ell(s)^{-1/11},
\tag{65}
\]

both integrable at zero.

### Quantile width

For fixed \(\eta<d/2\), let \(z_\eta(s)\in(a,b)\) solve

\[
\int_a^{z_\eta(s)}\phi(y)\,dy
=
\frac{\eta}{A(s)}.
\tag{66}
\]

Then

\[
\Lambda_\eta(s)=L(s)z_\eta(s),
\qquad
e_\phi(\Lambda_\eta(s),s)
=
\frac{A(s)}{L(s)}\phi(z_\eta(s)).
\tag{67}
\]

The \(A'\)-driven motion of \(z_\eta\) is \(O(L)\), while
\(|L'|/L\asymp1/s\); hence

\[
\Lambda_\eta'(s)
=
z_\eta(s)L'(s)(1+o(1)),
\tag{68}
\]

\[
W_\eta(s)\asymp L(s).
\tag{69}
\]

Its quantile charge has size

\[
\frac1{s\sqrt{L(s)}}\in L^1_s,
\tag{70}
\]

so the broad shell sharply survives Corollary 3.

## 6. Exact frontier

### Robust conditional findings, subject to external review

1. The actual nonlinear radial transfer has the finite
   \(\lambda^{-1/2}\)-weighted total-variation budget (6).
2. A descending fixed-energy spectral quantile obeys the exact speed law
   (9) and finite charge (11).
3. On the q4 shell schedule, persistent local width
   \(W_\eta\lesssim\sqrt L\) is impossible.
4. This excludes dynamic concatenation of fixed-energy adjacent Pell
   shells.
5. A smooth fixed-relative-width positive shell has strictly positive
   heat flux at every positive heat age for all sufficiently small
   times, satisfies the exact spectral energy law, every q4 scalar and
   Gaussian budget, the finite transfer charge, and asymptotically total
   early reuse.

### Closed shortcuts

1. The ideal delta-shell survivor is too narrow as stated.
2. Exact adjacent-shell Pell snapshots cannot be concatenated into the
   proposed continuously descending fixed-energy quantile.
3. A generic finite weighted-transfer norm does not close q4, because
   broad relative shells pay it finitely.
4. The sharp shell-speed threshold alone is width \(L^{1/2}\), not the
   full relative width \(L\).

### Things still to prove

1. Derive from the quadratic triad convolution a prohibition or finite
   cost for the necessary broadening \(W_\eta\gg\sqrt L\).
2. Couple radial width to angular mode count, spatial concentration, or
   the Hausdorff-one-null boundary energy measure.
3. Decide whether fixed-relative-width positive triads can be chained on
   one q4 trajectory without a nonsummable genealogy charge.
4. Use the strong-trace drift to constrain broad-shell steering.
5. Treat intermittent narrowing rather than an eventual pointwise width
   bound.
6. Treat slower clocks, divergent normalised energy, R3B, and the other
   Clay alternatives separately.

### Conjecture: no dynamically broad q4 descent

No same-trajectory full-defect q4 entrance with finite unweighted
dissipation can keep a fixed positive energy quantile descending at

\[
\Lambda_\eta(s)\asymp
s^{-9/11}\ell(s)^{2/11}
\tag{71}
\]

while maintaining the spectrally broad width

\[
W_\eta(s)\gg\sqrt{\Lambda_\eta(s)}
\tag{72}
\]

required by (11) and regenerating the full boundary defect through
positive early-history triadic work.

This conjecture is not proved.  The broad-shell spectrum is not a
velocity field, and a dilated fixed-relative-width triad is not one
evolution.  No q4 closure, regularity theorem, breakdown theorem,
energy-equality theorem, or Clay alternative is proved.
