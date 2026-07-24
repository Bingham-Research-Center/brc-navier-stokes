# Signed pressure laws have diffuse time marginals but a quadratic polar scale

- **Experiment:** EXP-ADJOINT-PRESSURE-TEMPORAL-001
- **Route:** ROUTE-R3B
- **Status:** conditional analytic reduction;
  [adversarially recomputed valid after sharpening](../review-ledger.md)
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** adversarially recomputed
  [Kato-polar signed aggregate](adjoint-pressure-signed-aggregate.md),
  [direct-response reduction](adjoint-pressure-direct-response.md), and
  [frequency-or-maximal-dust reduction](adjoint-pressure-feedback-dust.md)

The preceding theorem gives an event-normalised pressure law with positive
Kato-polar alignment. Its effective polar decoration is compact in space
at the positive-clock descendant scale, but no time structure was retained.

This note extracts the exact time structure already hidden in the reviewed
energy estimates. It also identifies why that structure is not yet a
limiting Oseen equation.

First, the signed early--late selection can be made using increase of the
regularised adjoint \(L^1\) mass, not merely completed pressure work. Hence
every selected terminal layer satisfies

\[
L_{\varepsilon_h}(a(h))-L_{\varepsilon_h}(\varphi)
\ge\gamma>0.
\]

Writing \(w=a-\varphi\), the reviewed estimate
\(\|w(h)\|_2\le F_\varphi h\) then forces

\[
\boxed{\varepsilon_h\le C h^2.}
\]

Moreover, every set carrying a fixed fraction of the resulting regularised
mass has volume at least \(ch^{-2}\), and therefore needs at least
\(ch^{-7/2}\) positive-clock descendant cells. A smooth divergence-free
kinematic family saturates all three powers. Thus the raw polar field may
live exactly at a singular quadratic regularisation scale; the available
\(O(h)\) adjoint-difference estimate alone cannot make it temporally
compact.

Second, let \(A\subset[0,1]\) be a measurable set of scaled adjoint times,
and let \(\eta_h\) be the normalised high-coefficient energy-time law.
The two charged source-localised branches satisfy different weighted
capture laws:

\[
\boxed{
\nu_h^{\rm hi}(A)
\le
C
\left(
\int_A s^2\,ds
\right)^{1/2}
\eta_h(A)^{1/2},
}
\]

whereas the finite-band branch satisfies the joint estimate

\[
\boxed{
\Gamma_h^{\rm fb}(A\times E\times\mathfrak M)
\le
C
\left(
|A|\int_A s^2\,ds
\right)^{1/2}
|E|^{1/6}.
}
\]

At the prelimit, \(E\) here is a macro-grid union; arbitrary Borel
spatial sets are obtained after taking the weak limit.

Consequently every limiting high-coefficient pressure density
\(g_{\rm hi}\) is coupled to the absolutely continuous part
\(e_{\rm hi}\,ds\) of the limiting energy law by

\[
\frac{g_{\rm hi}(s)^2}{s^2}
\le
Ce_{\rm hi}(s),
\qquad
\frac{g_{\rm hi}}s\in L^2(0,1).
\]

In particular its mass in \([0,\delta]\) is \(O(\delta^{3/2})\).
Every limiting finite-band law disintegrates as

\[
d\Gamma(s,\cdot)=ds\,d\Gamma_s(\cdot),
\]

with time density \(g_{\rm fb}(s)\le Cs\); for almost every \(s\), the
unnormalised spatial slice has a weak-\(L^{6/5}\) density whose norm is
at most \(Cs\). Its mass in \([0,\delta]\) is \(O(\delta^2)\). The
positive polar alignment occurs on a set of scaled times of positive
Lebesgue measure.

This is genuine temporal nonconcentration, but not temporal continuity.
The disintegration does not relate \(\Gamma_s\) and \(\Gamma_{s'}\), and
the quadratic regularisation ceiling defeats the elementary polar
chain-rule estimate. The next gate is now a time-translation estimate,
same-trajectory telescope, or limiting Oseen balance for the effective
polar decoration.

## 1. Reviewed inputs and two zero-data estimates

On one selected terminal layer, retain the smooth reversed coefficient and
its solenoidal Oseen adjoint:

\[
\partial_\tau a-\nu\Delta a
-b\cdot\nabla a+\nabla\pi^*=0,
\qquad
\nabla\cdot a=\nabla\cdot b=0,
\qquad
a(0)=\varphi.
\tag{1}
\]

Here \(\varphi\in\mathcal S_\sigma(\mathbb R^3;\mathbb R^3)\) is the one
fixed band-limited event detector. Put

\[
w(\tau):=a(\tau)-\varphi.
\tag{2}
\]

The reviewed difference-energy theorem gives, uniformly over the selected
genealogy,

\[
\boxed{
\|w(\tau)\|_2\le F_\varphi\tau
\qquad(0\le\tau\le h).
}
\tag{3}
\]

The later direct-response split writes \(w=q+r\), where

\[
\partial_\tau q-\nu\Delta q
=
\nu\Delta\varphi+\mathbb P(b\cdot\nabla\varphi),
\qquad
q(0)=0,
\tag{4}
\]

\[
\partial_\tau r-\nu\Delta r
-\mathbb P(b\cdot\nabla r)
=
\mathbb P(b\cdot\nabla q),
\qquad
r(0)=0.
\tag{5}
\]

The reviewed proof of the feedback-energy estimate may be stopped at every
\(0<t\le h\), not only at the terminal value \(h\). Indeed,

\[
\sup_{\tau\le t}\|q(\tau)\|_2\le F_\varphi t,
\qquad
\int_0^t\|\nabla q\|_2^2
\le
\frac{F_\varphi^2}{2\nu}t^2.
\tag{6}
\]

Pairing (5) with \(r\), using the skew drift and

\[
L^{3,\infty}\cdot L^{6,2}\cdot L^2
\longrightarrow L^1,
\qquad
\|q\|_{L^{6,2}}\lesssim\|\nabla q\|_2,
\tag{7}
\]

and then applying Young's inequality gives

\[
\boxed{
\|r(t)\|_2^2
+\nu\int_0^t\|\nabla r(\tau)\|_2^2\,d\tau
\le C_r t^2
\qquad(0\le t\le h).
}
\tag{8}
\]

This pointwise-in-terminal-time form is the input that prevents temporal
atoms below.

On the source-localised feedback branch, retain

\[
R=h^{-3},
\qquad
K=\kappa h^{-1/2},
\qquad
\ell=K^{-1},
\tag{9}
\]

\[
r^{\rm lo}=S_{AK}r,
\qquad
b^{\rm lo}=S_Kb^{\rm in},
\qquad
b^{\rm hi}=b^{\rm in}-b^{\rm lo}.
\tag{10}
\]

The two charged fields are

\[
J_h^{\rm hi}
:=
P_{>K}\mathcal T(r^{\rm lo},b^{\rm hi}),
\qquad
H_h
:=
P_{>K}\mathcal T(r^{\rm lo},b^{\rm lo}).
\tag{11}
\]

In the applicable branch, each obeys

\[
p_{\rm pol}
\le
Z_h
:=
\int_0^h\int_{\mathbb R^3}|J_h|
\le
C_{\rm pol}.
\tag{12}
\]

For the high-coefficient child,

\[
E_{\rm hi}(h)
:=
\int_0^h\|\nabla b^{\rm hi}\|_2^2\,d\tau
\le Ch^{-3}.
\tag{13}
\]

For the finite-band child, the reviewed kernel and grid argument gives

\[
\int_0^h\int_{U_{\mathcal F}}|H_h|
\le
C_{\rm cap}h^{7/4}|\mathcal F|^{1/6},
\tag{14}
\]

where \(U_{\mathcal F}\) is a union of physical cubes of side
\(\ell\).

## 2. The stopping alternative retains regularised mass gain

For \(\varepsilon>0\), recall

\[
\rho_\varepsilon(z)
:=
\sqrt{|z|^2+\varepsilon^2}-\varepsilon,
\qquad
L_\varepsilon(f)
:=
\int_{\mathbb R^3}\rho_\varepsilon(f(x))\,dx,
\tag{15}
\]

\[
\zeta_\varepsilon(a)
:=
\frac{a}{\sqrt{|a|^2+\varepsilon^2}}.
\tag{16}
\]

The exact Kato-polar identity is

\[
-\int_0^s\!\!\int
\zeta_\varepsilon(a)\cdot\nabla\pi^*
=
L_\varepsilon(a(s))-L_\varepsilon(\varphi)
+\nu\int_0^s\mathcal K_\varepsilon(a),
\qquad
\mathcal K_\varepsilon(a)\ge0.
\tag{17}
\]

At event \(m\) and smooth genealogy index \(n\), let

\[
\Delta_{m,n,\varepsilon}(s)
:=
L_\varepsilon(a_{m,n}(s))
-L_\varepsilon(\varphi).
\tag{18}
\]

The reviewed running-\(L^1\) estimate gives an excess

\[
Q_m(T_0)
\ge
\frac{c_0}{2C_{\rm adj}M}\sqrt{\nu T_0}.
\tag{19}
\]

Choose \(s\) within \(Q_m(T_0)/4\) of the running \(L^1\) supremum, then
choose \(\varepsilon\) so that
\(L_\varepsilon(a(s))\) is within another \(Q_m(T_0)/4\) of
\(\|a(s)\|_1\). Since
\(L_\varepsilon(\varphi)\le\|\varphi\|_1\), the proof supplies the
stronger conclusion

\[
\sup_{\substack{\varepsilon>0\\0<s\le T_0}}
\Delta_{m,n,\varepsilon}(s)
\ge q_0,
\tag{20}
\]

for every sufficiently deep genealogy member, where

\[
q_0
:=
\frac{c_0}{4C_{\rm adj}M}\sqrt{\nu T_0}.
\tag{21}
\]

Define the relaxed running mass gain

\[
\mathcal M_{m,n}(t)
:=
\sup_{\substack{\varepsilon>0\\0\le s\le t}}
\Delta_{m,n,\varepsilon}(s),
\qquad
\gamma:=\frac{q_0}{4}.
\tag{22}
\]

There is an exhaustive alternative.

### Alternative I: mass-gain terminal layers

Suppose that, for every rational \(0<\eta<1\), infinitely many event
indices \(m\) obey

\[
\limsup_{n\to\infty}
\mathcal M_{m,n}(\eta T_0)
\ge2\gamma.
\tag{23}
\]

Choose \(\eta_j\downarrow0\), increasing event indices \(m_j\), and then
increasing genealogy indices \(n_j\) from the same unscaled smooth
genealogy. Approximate the two suprema in (23) to obtain

\[
h_j\le\eta_jT_0,
\qquad
h_j\longrightarrow0,
\tag{24}
\]

and \(\varepsilon_j>0\) such that

\[
\boxed{
\Delta_{m_j,n_j,\varepsilon_j}(h_j)
\ge\gamma.
}
\tag{25}
\]

Equation (17) simultaneously gives

\[
-\int_0^{h_j}\!\!\int
\zeta_{\varepsilon_j}(a_{m_j,n_j})
\cdot\nabla\pi^*_{m_j,n_j}
\ge\gamma.
\tag{26}
\]

Thus this is a valid input to the entire reviewed signed branch tree, with
the additional mass-gain information (25).

### Alternative II: mass-gain late packets

If Alternative I fails, there is a rational \(0<\eta<1\) such that all
but finitely many events satisfy

\[
\limsup_{n\to\infty}
\mathcal M_{m,n}(\eta T_0)
<2\gamma.
\tag{27}
\]

For any finite family of those events, choose one common sufficiently deep
member \(n\) of the same unscaled smooth genealogy so that

\[
\mathcal M_{m,n}(\eta T_0)<2\gamma.
\tag{28}
\]

By (20)--(22), choose one
\(\varepsilon_{m,n}>0\) and \(s_{m,n}\le T_0\) with

\[
\Delta_{m,n,\varepsilon_{m,n}}(s_{m,n})
\ge3\gamma.
\tag{29}
\]

The same regularisation at the early endpoint obeys

\[
\Delta_{m,n,\varepsilon_{m,n}}(\eta T_0)
<2\gamma.
\tag{30}
\]

Subtracting (17) at the two times therefore yields

\[
\boxed{
-\int_{\eta T_0}^{s_{m,n}}\!\!\int
\zeta_{\varepsilon_{m,n}}(a_{m,n})
\cdot\nabla\pi^*_{m,n}
\ge\gamma.
}
\tag{31}
\]

The same physical-annulus thinning as in the preceding theorem makes the
containing late annuli pairwise disjoint.

This proves the earlier signed early--late alternative with the stronger
selection rule. Mass gain is retained on the terminal branch; the late
branch needs only the signed work in (31).

## 3. Terminal mass gain forces a quadratic regularisation scale

Work on the terminal sequence (24)--(26), and abbreviate

\[
a_h:=a_{m_j,n_j},
\qquad
w_h:=a_h-\varphi,
\qquad
\varepsilon_h:=\varepsilon_j.
\tag{32}
\]

Because \(\varphi\) is Schwartz, choose one fixed radius
\(R_\varphi\) such that

\[
\int_{|x|>R_\varphi}|\varphi(x)|\,dx
\le\frac{\gamma}{8}.
\tag{33}
\]

The map \(\rho_\varepsilon\) is one-Lipschitz. Therefore (3) gives

\[
\left|
\int_{B_{R_\varphi}}
\left[
\rho_{\varepsilon_h}(\varphi+w_h(h))
-\rho_{\varepsilon_h}(\varphi)
\right]dx
\right|
\le
|B_{R_\varphi}|^{1/2}F_\varphi h.
\tag{34}
\]

For all sufficiently small \(h\), the right-hand side is at most
\(\gamma/8\). On the exterior, one-Lipschitz continuity also gives

\[
\rho_{\varepsilon_h}(\varphi+w_h)
\le
\rho_{\varepsilon_h}(w_h)+|\varphi|.
\tag{35}
\]

Equations (25), (33)--(35) imply

\[
\boxed{
\int_{\mathbb R^3}
\rho_{\varepsilon_h}(w_h(h))\,dx
\ge
\frac{3\gamma}{4}.
}
\tag{36}
\]

Pointwise,

\[
\rho_\varepsilon(z)
=
\frac{|z|^2}
{\sqrt{|z|^2+\varepsilon^2}+\varepsilon}
\le
\frac{|z|^2}{2\varepsilon}.
\tag{37}
\]

Combining (3), (36), and (37) gives

\[
\frac{3\gamma}{4}
\le
\frac{F_\varphi^2h^2}{2\varepsilon_h}.
\tag{38}
\]

Hence

\[
\boxed{
\varepsilon_h
\le
\frac{2F_\varphi^2}{3\gamma}h^2.
}
\tag{39}
\]

This is an upper ceiling on the selected regularisation: retaining the
mass-gain charge forces \(\varepsilon_h\) to vanish at least as fast as
the quadratic scale. It is not a lower bound.

There is a matching spatial consequence. Let \(E_h\) be any measurable
set carrying a fixed amount \(c_\gamma>0\) of the mass in (36):

\[
\int_{E_h}
\rho_{\varepsilon_h}(w_h(h))\,dx
\ge c_\gamma.
\tag{40}
\]

Since \(\rho_\varepsilon(z)\le|z|\), Cauchy--Schwarz and (3) give

\[
c_\gamma
\le
|E_h|^{1/2}\|w_h(h)\|_2
\le
F_\varphi h|E_h|^{1/2}.
\tag{41}
\]

Thus

\[
\boxed{
|E_h|
\ge
\frac{c_\gamma^2}{F_\varphi^2}h^{-2}.
}
\tag{42}
\]

At the positive-clock descendant length
\(\ell=\kappa^{-1}\sqrt h\), every union of descendant grid cubes
carrying the mass in (40) consequently has at least

\[
\boxed{
N_{\rm Kato}(h)
\ge
c_{\gamma,\varphi}\kappa^3h^{-7/2}
}
\tag{43}
\]

cubes. The exponent agrees with the independently forced
coefficient-dissipation cell count, although no cellwise coupling between
the two measures is inferred.

### Kinematic saturation

Let
\(W\in C^\infty_{c,\sigma}(\mathbb R^3;\mathbb R^3)\) be nonzero and
fix arbitrary translations \(y_h\). Define

\[
w_h^{\rm mod}(x)
:=
h^2W\!\left(h^{2/3}(x-y_h)\right),
\qquad
\varepsilon_h^{\rm mod}:=h^2.
\tag{44}
\]

Then

\[
\|w_h^{\rm mod}\|_2^2
=
h^2\|W\|_2^2,
\qquad
\|w_h^{\rm mod}\|_1
=
\|W\|_1,
\tag{45}
\]

\[
L_{\varepsilon_h^{\rm mod}}(w_h^{\rm mod})
=
\int_{\mathbb R^3}
\left(\sqrt{|W(y)|^2+1}-1\right)dy,
\tag{46}
\]

and

\[
|\operatorname{supp}w_h^{\rm mod}|
=
h^{-2}|\operatorname{supp}W|.
\tag{47}
\]

Its support uses \(\asymp\kappa^3h^{-7/2}\) descendant cells. Moreover,

\[
\zeta_{\varepsilon_h^{\rm mod}}(w_h^{\rm mod})
=
\frac{W(h^{2/3}(x-y_h))}
{\sqrt{|W(h^{2/3}(x-y_h))|^2+1}},
\tag{48}
\]

so changing \(W\) to \(-W\) changes the polar mark by order one while
changing the field by only \(O(h)\) in \(L^2\).

This is a smooth divergence-free kinematic family, not an Oseen or
Navier--Stokes construction. It proves only that (39), (42), and (43)
cannot be improved from the mass and \(L^2\) ledgers alone.

The same obstruction can be placed in the effective-polar band at the
reviewed spatial-gradient power. Set

\[
L_h:=h^{-2/3},
\qquad
K_h:=\kappa h^{-1/2},
\tag{48a}
\]

choose a nonzero
\(\eta\in C_c^\infty(\mathbb R^3)\), and define the exact solenoidal
carrier

\[
V_h
:=
K_h^{-1}
\nabla\times
\left[
\eta\!\left(\frac{x-y_h}{L_h}\right)
\cos(K_hx_1)e_3
\right].
\tag{48b}
\]

Its leading term is a unit-amplitude wave at frequency \(K_h\); the
envelope corrections are \(O((K_hL_h)^{-1})=o(1)\). For any smooth
\(\sigma_h:[0,h]\to[-1,1]\) which vanishes on
\([0,h/3]\) and satisfies \(\sigma_h(h)=1\), define

\[
w_h^{\rm osc}(\tau,x)
:=
h^2\sigma_h(\tau)V_h(x).
\tag{48c}
\]

Uniformly over the number of sign changes of \(\sigma_h\),

\[
\|w_h^{\rm osc}(\tau)\|_2\lesssim\tau,
\qquad
\sup_{\tau\le h}\|w_h^{\rm osc}(\tau)\|_2^2
\lesssim h^2,
\qquad
\int_0^h\|\nabla w_h^{\rm osc}\|_2^2\,d\tau
\lesssim h^2.
\tag{48d}
\]

Indeed, the spatial gradient squared is of order

\[
h^4K_h^2L_h^3\asymp h,
\tag{48e}
\]

and the layer has length \(h\). When
\(\varepsilon_h=h^2\), the polar field has an order-one fundamental
component at \(K_h\). A fixed multiplier equal to one near that component
therefore retains an order-one descendant-rooted effective polar at bulk
roots, equivalently in a fixed local norm, which changes sign with
\(\sigma_h\). If \(|\sigma_h|\) is bounded below on a fixed fraction of
the layer, the gradient power in (48d) is also attained from below.
Arbitrary admissible \(\sigma_h\) only satisfies the displayed upper
bound. The number of temporal flips is not seen by either norm in (48d).

This band-resolved family is still only kinematic: it need not solve the
Oseen equation and carries no asserted pressure alignment. It shows that
even spatial band projection plus the reviewed
\(L^\infty_tL^2_x\cap L^2_t\dot H^1_x\) estimates cannot by themselves
give time-translation compactness of the effective polar mark.

In particular, the elementary polar Lipschitz estimate has coefficient
\(\varepsilon_h^{-1}\). Combining it with the available \(O(h)\)
adjoint-difference bound produces a formal upper bound of size

\[
\frac h{\varepsilon_h},
\tag{49}
\]

which may be \(h^{-1}\) or worse under (39). This estimate is therefore
incapable of proving a vanishing temporal modulus. It does not prove that
the actual Oseen polar oscillates.

## 4. High-coefficient pressure is coupled to diffuse energy time

Let \(A\subset[0,1]\) be measurable and set

\[
hA:=\{\tau\in[0,h]:\tau/h\in A\}.
\tag{50}
\]

Smooth multiplier boundedness, the pointwise Hardy div--curl estimate,
and Cauchy--Schwarz in time give

\[
\begin{aligned}
\int_{hA}\|J_h^{\rm hi}(\tau)\|_1\,d\tau
&\le
C
\left(
\int_{hA}\|r^{\rm lo}(\tau)\|_2^2\,d\tau
\right)^{1/2}\\
&\quad\times
\left(
\int_{hA}\|\nabla b^{\rm hi}(\tau)\|_2^2\,d\tau
\right)^{1/2}.
\end{aligned}
\tag{51}
\]

By (8) and \(L^2\)-boundedness of \(S_{AK}\),

\[
\int_{hA}\|r^{\rm lo}(\tau)\|_2^2\,d\tau
\le
C\int_{hA}\tau^2\,d\tau
=
C h^3\int_A s^2\,ds.
\tag{52}
\]

The charged high-coefficient branch has
\(E_{\rm hi}(h)\asymp h^{-3}\). Define its normalised energy-time law by

\[
\eta_h(A)
:=
\frac1{E_{\rm hi}(h)}
\int_{hA}\|\nabla b^{\rm hi}(\tau)\|_2^2\,d\tau.
\tag{53}
\]

This is a probability measure on \([0,1]\). Let
\(\nu_h^{\rm hi}\) be the \(\tau/h\) marginal of the
pressure-mass-normalised marked law. Equations (12), (13), and
(51)--(53) give the coupled estimate

\[
\boxed{
\nu_h^{\rm hi}(A)
\le
C_{\rm hi}
\left(
\int_A s^2\,ds
\right)^{1/2}
\eta_h(A)^{1/2}.
}
\tag{54}
\]

Equivalently, rerunning the same weighted Cauchy--Schwarz argument gives,
for every nonnegative \(\chi\in C([0,1])\),

\[
\boxed{
\left(
\int_0^1\chi\,d\nu_h^{\rm hi}
\right)^2
\le
C_{\rm hi}
\left(
\int_0^1\chi(s)s^2\,ds
\right)
\left(
\int_0^1\chi\,d\eta_h
\right).
}
\tag{54a}
\]

In particular,

\[
\nu_h^{\rm hi}(A)
\le
C_{\rm hi}|A|^{1/2}.
\tag{55}
\]

After common subsequence selection, let

\[
\nu_h^{\rm hi}\rightharpoonup\nu^{\rm hi},
\qquad
\eta_h\rightharpoonup\eta.
\tag{56}
\]

Equation (54a) passes termwise under the joint weak convergence in (56).
Compact approximation then recovers the Borel-set form of (54) for the
two limiting measures. Equation (55) makes
\(\nu^{\rm hi}\) absolutely continuous:

\[
d\nu^{\rm hi}(s)=g_{\rm hi}(s)\,ds.
\tag{57}
\]

Write the Lebesgue decomposition of the limiting energy law as

\[
d\eta(s)=e_{\rm hi}(s)\,ds+d\eta^\perp(s).
\tag{58}
\]

Apply the limiting form of (54) to shrinking intervals about a common
Lebesgue point of \(g_{\rm hi}\) and \(e_{\rm hi}\) at which the singular
part has zero Lebesgue density. Dividing the squared estimate by the
squared interval length gives

\[
\boxed{
g_{\rm hi}(s)^2
\le
C_{\rm hi}^2s^2e_{\rm hi}(s)
\quad\hbox{for almost every }s.
}
\tag{59}
\]

Consequently

\[
\boxed{
\frac{g_{\rm hi}}s\in L^2(0,1),
\qquad
\int_0^1\frac{g_{\rm hi}(s)^2}{s^2}\,ds
\le
C_{\rm hi}^2.
}
\tag{60}
\]

Here the value at \(s=0\) is irrelevant. Cauchy--Schwarz now yields the
terminal-edge estimate

\[
\boxed{
\nu^{\rm hi}([0,\delta])
\le
C\delta^{3/2}.
}
\tag{61}
\]

Thus the pressure law forces an absolutely continuous component of the
high-frequency energy-time law and cannot concentrate at the terminal
edge of the scaled layer. The estimate does not control its spatial
marginal or produce time continuity.

## 5. Finite-band pressure has a joint time--space capture law

Assume the finite-band branch. For a finite grid family
\(\mathcal F\), recall

\[
U_{\mathcal F}
=
\bigcup_{m\in\mathcal F}Q_m,
\qquad
N=|\mathcal F|,
\tag{62}
\]

and the weight

\[
w_{\mathcal F}(y)
:=
\int_{U_{\mathcal F}}|L_K(x-y)|\,dx.
\tag{63}
\]

The reviewed kernel interpolation gives

\[
\|w_{\mathcal F}\|_\infty\le C_A,
\qquad
\|w_{\mathcal F}\|_{L^{3,1}}
\le
C_AN^{1/3}\ell.
\tag{64}
\]

Restrict the reviewed weighted Cauchy--Schwarz argument to \(hA\):

\[
\begin{aligned}
\int_{hA}\int_{U_{\mathcal F}}|H_h|
&\le
C_A
\left(
\int_{hA}\int|r^{\rm lo}|^2w_{\mathcal F}
\right)^{1/2}\\
&\quad\times
\left(
\int_{hA}\int
|\nabla b^{\rm lo}|^2w_{\mathcal F}
\right)^{1/2}.
\end{aligned}
\tag{65}
\]

Equations (8) and (64) give

\[
\int_{hA}\int|r^{\rm lo}|^2w_{\mathcal F}
\le
C h^3\int_A s^2\,ds.
\tag{66}
\]

At each time, Lorentz--Bernstein gives

\[
\|\nabla b^{\rm lo}(\tau)\|_{L^{3,\infty}}
\le C_AKM.
\tag{67}
\]

Using
\(L^{3/2,\infty}\cdot L^{3,1}\to L^1\), (64), and (67),

\[
\int_{hA}\int
|\nabla b^{\rm lo}|^2w_{\mathcal F}
\le
C h|A|K N^{1/3}.
\tag{68}
\]

Substitution into (65) gives

\[
\boxed{
\int_{hA}\int_{U_{\mathcal F}}|H_h|
\le
C_{\rm mix}h^{7/4}
\left(
|A|\int_A s^2\,ds
\right)^{1/2}
N^{1/6}.
}
\tag{69}
\]

All dependence on the one fixed \(\kappa\), multiplier shapes,
\(M\), and the detector is absorbed into \(C_{\rm mix}\).

In source coordinates \(y=x/R\), the grid mesh is

\[
\delta_h
:=
\frac{\ell}{R}
=
\kappa^{-1}h^{7/2}.
\tag{70}
\]

If
\(\widehat U_{\mathcal F}=R^{-1}U_{\mathcal F}\), then

\[
|\widehat U_{\mathcal F}|
=
N\delta_h^3.
\tag{71}
\]

Normalising by \(Z_h\ge p_{\rm pol}\), equations (69)--(71) become

\[
\boxed{
\Gamma_h^{\rm fb}
\left(
A\times\widehat U_{\mathcal F}\times\mathfrak M
\right)
\le
C
\left(
|A|\int_A s^2\,ds
\right)^{1/2}
|\widehat U_{\mathcal F}|^{1/6},
}
\tag{72}
\]

where \(\mathfrak M\) denotes all polar, pressure-direction, effective
profile, and branch marks.

The prelimit statement (72) applies to macro-grid unions. Covering open
sets by macro-grid cubes gives the corresponding estimate with an
asymptotically negligible boundary enlargement. In the weak limit,
open-set Portmanteau followed by outer regularity extends it to arbitrary
Borel time and spatial sets.

## 6. Limiting finite-band laws disintegrate over Lebesgue time

Let \(h_j\downarrow0\) be a finite-band subsequence and let

\[
\Gamma_{h_j}^{\rm fb}\rightharpoonup\Gamma^{\rm fb}.
\tag{73}
\]

The preceding off-diagonal theorem gives, for every fixed \(B>32\) and
every \(N_0\),

\[
\int_0^h\int_{|x|>BR}|H_h|
\le
C_{B,N_0}(KR)^{-N_0}.
\tag{74}
\]

Together with \(Z_h\ge p_{\rm pol}\), this puts the limiting spatial
coordinate inside one fixed ball, for example \(\overline{B_{64}}\).
Passing (72) to the limit gives, for all Borel
\(A\subset[0,1]\) and \(E\subset B_{64}\),

\[
\boxed{
\Gamma^{\rm fb}
\left(
A\times E\times\mathfrak M
\right)
\le
C
\left(
|A|\int_A s^2\,ds
\right)^{1/2}
|E|^{1/6}.
}
\tag{75}
\]

Taking \(E=B_{64}\) shows that the time marginal is absolutely continuous
with an \(L^\infty\) density. Standard disintegration on the compact
Polish mark space therefore gives a measurable family of finite measures
\(\Gamma_s\) such that

\[
\boxed{
d\Gamma^{\rm fb}(s,\cdot)
=
ds\,d\Gamma_s(\cdot),
\qquad
g_{\rm fb}(s)
:=
\Gamma_s(B_{64}\times\mathfrak M)
\in L^\infty([0,1]).
}
\tag{76}
\]

For each member \(E\) of a countable algebra of rational spatial boxes,
(75), applied to intervals shrinking to \(s\), implies

\[
\Gamma_s(E\times\mathfrak M)
\le
Cs|E|^{1/6}
\tag{77}
\]

for almost every \(s\). Intersecting those full-measure time sets and
using regularity extends (77) simultaneously to every Borel \(E\), for
almost every \(s\).

Let \(\mu_s\) be the unnormalised spatial marginal of \(\Gamma_s\). Then

\[
\boxed{
\mu_s(E)\le Cs|E|^{1/6}
\quad\hbox{for every Borel }E,
\quad\hbox{for almost every }s.
}
\tag{78}
\]

Consequently

\[
\boxed{
d\mu_s(y)=f_s(y)\,dy,
\qquad
f_s\in L^{6/5,\infty}(\mathbb R^3),
}
\tag{79}
\]

with weak-\(L^{6/5}\) norm at most \(Cs\) for the unnormalised slices.
In particular,

\[
\boxed{
g_{\rm fb}(s)\le Cs,
\qquad
\Gamma^{\rm fb}
\left(
[0,\delta]\times B_{64}\times\mathfrak M
\right)
\le C\delta^2.
}
\tag{80}
\]

If one
normalises \(\Gamma_s\) to a conditional probability by dividing by
\(g_{\rm fb}(s)\), this uniform bound may be lost where
\(g_{\rm fb}(s)\) is small; no stronger assertion is made.

Let

\[
F_{\rm pol}
:=
-\mathsf A(0)\cdot\omega
\tag{81}
\]

be the continuous effective-polar alignment mark from the preceding
theorem. Its positive expectation becomes

\[
\int_0^1
\left(
\int F_{\rm pol}\,d\Gamma_s
\right)ds
\ge
\frac{p_{\rm pol}}{C_{\rm pol}}
=:c_{\rm align}>0.
\tag{82}
\]

Put

\[
q(s):=\int F_{\rm pol}\,d\Gamma_s.
\tag{83}
\]

Since \(|F_{\rm pol}|\) is uniformly bounded and
\(g_{\rm fb}\in L^\infty\), there is a constant \(C_q\) with
\(|q(s)|\le C_q\) almost everywhere. Equation (82) therefore implies

\[
\boxed{
\left|
\left\{
s\in[0,1]:q(s)>0
\right\}
\right|
\ge
\frac{c_{\rm align}}{C_q}
>0.
}
\tag{84}
\]

Thus the causal alignment is not hidden at one exceptional scaled time:
positive aligned slices occupy a set of positive Lebesgue measure.

## 7. Exact consequence and remaining gate

The signed aggregate now has genuine, branch-dependent temporal
nonconcentration:

1. in the charged high-coefficient branch, every limiting time marginal
   has a density \(g_{\rm hi}\) with
   \(g_{\rm hi}/s\in L^2\), coupled to the absolutely continuous part of
   the high-frequency energy-time law;
2. in the charged finite-band branch, the limiting law has an
   \(L^\infty\) time density bounded by \(Cs\) and almost-every-time
   diffuse weak-\(L^{6/5}\) spatial slices with norm at most \(Cs\);
3. finite-band positive Kato-polar alignment occurs on a positive-measure
   set of scaled times.

The refined mass-gain stopping rule simultaneously proves that every
terminal-layer polar regularisation retaining the charge obeys
\(\varepsilon_h\lesssim h^2\). The accompanying regularised adjoint cloud
uses at least \(h^{-2}\) volume and \(h^{-7/2}\) descendant cells. Those
powers are sharp for the stated norm ledgers.

This closes **time atoms and vanishing terminal-edge concentration** as
explanations for loss of either signed local charge. It does not close
ROUTE-R3B.
In particular, nothing here proves:

- temporal continuity, bounded variation, or translation compactness of
  the raw or effective polar mark;
- a limiting Oseen equation for \(\Gamma_s\);
- that positive slices at different events are compatible or additive;
- a same-trajectory telescope or finite critical budget;
- a spatial or common-field coupling of the pressure slices to the
  high-frequency energy law, beyond the time-marginal inequality (59);
- exclusion of the direct inverse-\(15/4\), exterior
  stretched-exponential, or signed late-annulus branches;
- regularity, breakdown, or any Clay alternative A--D.

The exact next question is narrower:

> Can one control time translations of the finite-band effective polar
> decoration, or identify one finite same-trajectory functional whose
> increments equal its positive slice alignment? The raw chain rule cannot
> do this because the mass-gain selection itself forces the Kato
> regularisation down to the quadratic scale.

Run the exact power ledger with:

```bash
make adjoint-pressure-temporal
```
