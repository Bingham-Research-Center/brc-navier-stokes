# Weak-\(L^3\) viscosity forces a lower-band flux decrement

- **Experiment:** EXP-ADJOINT-PRESSURE-FLUX-DECREMENT-001
- **Route:** ROUTE-R3B
- **Status:** adversarially recomputed conditional same-trajectory theorem
- **Review:** [valid and nonduplicative after five precision
  repairs](../review-ledger.md)
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Input:** the adversarially recomputed
  [terminal signed-flux ancestry theorem](adjoint-pressure-inherited-ancestry.md)

The terminal-flux theorem forces positive nonlinear input across a sharp
frequency \(K_j\), but its conservative shell ledger permits one almost
lossless cascade to cross arbitrarily many boundaries.  That ledger does
not respect one additional property of the conditional Navier--Stokes
trajectory: its uniform weak-\(L^3\) velocity ceiling.

Fix a smooth low-pass \(S_L\), put

\[
h=Q_{>K}v,
\qquad
u=S_Lv,
\qquad
m=P_{\le K}v-S_Lv,
\qquad
v=u+m+h,
\]

and choose \(L=\eta K\), where

\[
0<\eta
\le
\min\left\{
\frac18,
\left(\frac{\nu}{12C_{\rm lp}M}\right)^{1/2}
\right\}.
\]

The exact sharp high-pass flux density splits as

\[
\boxed{
\mathcal F_K
=
-\int_{\mathbb R^3}h_i h_j\partial_j u_i\,dx
+\mathcal R_{L,K},
}
\]

with

\[
\boxed{
\left|
\int h_i h_j\partial_j u_i
\right|
\le
C_{\rm lp}M\left(\frac LK\right)^2
\|\nabla h\|_2^2,
}
\]

and

\[
\boxed{
|\mathcal R_{L,K}|
\le
C_0M\|\nabla h\|_2\|\nabla m\|_2.
}
\]

The first term is far-low strain acting on high energy.  Its coefficient
is at most a fixed small fraction of viscosity.  Every other interaction
contains the lower comparable-band field \(m\).  The second estimate uses
only divergence-free cancellation, Lorentz--Sobolev,

\[
L^{3,\infty}\cdot L^{6,2}\cdot L^2\longrightarrow L^1,
\]

and the spectral gaps

\[
\|h\|_2\le K^{-1}\|\nabla h\|_2,
\qquad
\|m\|_2\le L^{-1}\|\nabla m\|_2.
\]

This turns the two terminal-flux alternatives into a genuine decrement.
If \(F=\Phi_K(J)>0\) is either the low-entrance event flux or the
half-to-full last-hitting flux, then

\[
\boxed{
\int_J\|\nabla m\|_2^2\,dt
\ge
c_0\frac{\nu}{M^2}F.
}
\]

In particular, for the pressure-tail floor \(T_j\),

\[
\boxed{
\int_{\widetilde J_j}
\left\|
\nabla
\left(
P_{\le K_j}-S_{\eta K_j}
\right)v
\right\|_2^2\,dt
\ge
c_1\frac{\nu^2}{M^2}T_j.
}
\]

The multiplier on the left is supported in

\[
\eta K_j\le|\xi|\le K_j.
\]

Thus a pressure-tail event cannot be paid by an arbitrarily lossless jump
from a far-low reservoir to frequencies far above \(K_j\).  A fixed
fraction of its signed input is dissipated in a comparable band
immediately below the boundary.

This is a strict improvement over the algebraic shell survivor, but it
is not yet a Clay contradiction.  The decrement factor may be small,
the physical floors \(T_j\) tend to zero, and comparable lower bands from
nearby event indices may overlap.  The new live question is whether the
recursive Besov-event geometry makes these decrements event-index
summable with a scale-zero lower bound, or whether an exponentially
decaying flux chain still survives.

## 1. Setup and notation

Let \(v\) be a smooth finite-energy unforced Navier--Stokes solution on
\(\mathbb R^3\times I\), where \(I=(a,b)\), and assume

\[
\operatorname*{ess\,sup}_{t\in I}
\|v(t)\|_{L^{3,\infty}(\mathbb R^3)}
\le M,
\qquad
M>0.
\tag{1}
\]

Let

\[
P_{\le K}
:=
\mathbf 1_{\{|\xi|\le K\}}(D),
\qquad
Q_{>K}:=I-P_{\le K},
\tag{2}
\]

and set

\[
h:=Q_{>K}v,
\qquad
E_K(t):=\|h(t)\|_2^2,
\qquad
D_h(I):=\int_I\|\nabla h(t)\|_2^2\,dt.
\tag{3}
\]

Use the forward-time flux convention

\[
\Phi_K(I)
:=
-
\int_I
\left\langle
Q_{>K}\mathbb P\operatorname{div}(v\otimes v),
h
\right\rangle\,dt.
\tag{4}
\]

The exact high-pass identity is

\[
\boxed{
\Phi_K(I)
=
\frac12\bigl(E_K(b)-E_K(a)\bigr)
+\nu D_h(I).
}
\tag{5}
\]

Fix a real even radial symbol
\(\chi_{\rm lp}\in C_c^\infty(\mathbb R^3)\) satisfying

\[
0\le\chi_{\rm lp}\le1,
\qquad
\chi_{\rm lp}(\xi)=1
\quad(|\xi|\le1),
\qquad
\chi_{\rm lp}(\xi)=0
\quad(|\xi|\ge2),
\tag{6}
\]

and define

\[
S_L:=\chi_{\rm lp}(D/L).
\tag{7}
\]

For \(0<L<K/4\), put

\[
u:=S_Lv,
\qquad
m:=P_{\le K}v-S_Lv.
\tag{8}
\]

Then

\[
v=u+m+h,
\tag{9}
\]

all three fields are divergence free, and

\[
\operatorname{supp}\widehat u
\subset\{|\xi|\le2L\},
\qquad
\operatorname{supp}\widehat m
\subset\{L\le|\xi|\le K\},
\qquad
\operatorname{supp}\widehat h
\subset\{|\xi|>K\}.
\tag{10}
\]

The sharp projectors in (2) are used only in \(L^2\).  No
\(L^{3,\infty}\) boundedness of a sharp ball multiplier is assumed.

## 2. Exact flux decomposition

At a fixed smooth time, the instantaneous nonlinear input is

\[
\mathcal F_K
:=
-
\left\langle
Q_{>K}\mathbb P\operatorname{div}(v\otimes v),
h
\right\rangle
=
\int_{\mathbb R^3}
v_i v_j\partial_jh_i\,dx.
\tag{11}
\]

Since \(4L<K\), Fourier support gives

\[
\int u_i u_j\partial_jh_i\,dx=0.
\tag{12}
\]

Incompressibility gives

\[
\int h_i u_j\partial_jh_i\,dx=0,
\qquad
\int h_i h_j\partial_jh_i\,dx=0,
\tag{13}
\]

and

\[
\int u_i h_j\partial_jh_i\,dx
=
-
\int h_i h_j\partial_ju_i\,dx.
\tag{14}
\]

Therefore the part with no \(m\)-factor is precisely

\[
\mathcal A_{L,K}
:=
-
\int h_i h_j\partial_ju_i\,dx.
\tag{15}
\]

Using

\[
v\otimes v-(u+h)\otimes(u+h)
=
m\otimes v+(u+h)\otimes m,
\tag{16}
\]

the remainder is

\[
\mathcal R_{L,K}
=
\int
\left[
m_i v_j+(u_i+h_i)m_j
\right]\partial_jh_i\,dx.
\tag{17}
\]

The first term in (17) may be integrated by parts:

\[
\int m_i v_j\partial_jh_i\,dx
=
-
\int h_i v_j\partial_jm_i\,dx.
\tag{18}
\]

Lorentz Hölder and Lorentz--Sobolev give

\[
\left|
\int h_i v_j\partial_jm_i\,dx
\right|
\le
C_{\rm LS}
\|v\|_{L^{3,\infty}}
\|h\|_{L^{6,2}}
\|\nabla m\|_2
\le
C_{\rm LS}M
\|\nabla h\|_2
\|\nabla m\|_2.
\tag{19}
\]

For the second term in (17), incompressibility of \(m\) gives

\[
\begin{aligned}
\int(u_i+h_i)m_j\partial_jh_i\,dx
&=
-
\int h_i m_j\partial_j(u_i+h_i)\,dx
\\
&=
-
\int h_i m_j\partial_ju_i\,dx.
\end{aligned}
\tag{20}
\]

The smooth low-pass kernel and Lorentz Young inequality give

\[
\|\nabla u\|_\infty
\le
C_{\rm lp}ML^2.
\tag{21}
\]

Plancherel and (10) give

\[
\|h\|_2
\le K^{-1}\|\nabla h\|_2,
\qquad
\|m\|_2
\le L^{-1}\|\nabla m\|_2.
\tag{22}
\]

Because \(0\le\chi_{\rm lp}\le1\), Plancherel also gives

\[
\boxed{
\int_J\|\nabla m\|_2^2\,dt
\le
\int_J
\|\nabla
Q_{L<|\xi|\le K}v\|_2^2\,dt
}
\tag{22a}
\]

on every time interval \(J\).  Thus a lower bound for \(D_m\) is
genuinely a lower bound for sharp annular dissipation; no cancellation
inside the multiplier can inflate the left side.

Consequently

\[
\left|
\int h_i m_j\partial_ju_i\,dx
\right|
\le
C_{\rm lp}M\frac LK
\|\nabla h\|_2
\|\nabla m\|_2.
\tag{23}
\]

Combining (17)--(23), and using \(L<K\), proves

\[
\boxed{
|\mathcal R_{L,K}|
\le
C_0M
\|\nabla h\|_2
\|\nabla m\|_2,
}
\tag{24}
\]

where \(C_0\) depends only on the fixed cutoff and the
Lorentz--Sobolev constants.

The far-low term instead satisfies

\[
\begin{aligned}
|\mathcal A_{L,K}|
&\le
\|\nabla u\|_\infty\|h\|_2^2
\\
&\le
C_{\rm lp}M
\left(\frac LK\right)^2
\|\nabla h\|_2^2.
\end{aligned}
\tag{25}
\]

Equations (15), (24), and (25) prove the claimed decomposition.

## 3. A quantitative lower-band decrement

Choose

\[
\boxed{
\eta
:=
\min\left\{
\frac18,
\left(\frac{\nu}{12C_{\rm lp}M}\right)^{1/2}
\right\},
\qquad
L:=\eta K.
}
\tag{26}
\]

Then \(4L<K\), and (25) gives

\[
\int_I|\mathcal A_{L,K}(t)|\,dt
\le
\frac{\nu}{12}D_h(I).
\tag{27}
\]

Put

\[
D_m(I)
:=
\int_I\|\nabla m(t)\|_2^2\,dt,
\qquad
F:=\Phi_K(I).
\tag{28}
\]

Integrating (24) and applying Cauchy--Schwarz gives

\[
\left|
\int_I\mathcal R_{L,K}(t)\,dt
\right|
\le
C_0M\sqrt{D_h(I)D_m(I)}.
\tag{29}
\]

We now record the two interval types supplied by the terminal-flux
ancestry theorem.

### 3.1 Low-entrance dissipation interval

Suppose for some \(T>0\) that

\[
E_K(a)<\nu T,
\qquad
D_h(I)>\frac{3T}{4}.
\tag{30}
\]

Equation (5) and \(E_K(b)\ge0\) give

\[
F
>
-\frac{\nu T}{2}
+\frac{3\nu T}{4}
=
\frac{\nu T}{4}.
\tag{31}
\]

They also give

\[
\nu D_h(I)
=
F+\frac12\bigl(E_K(a)-E_K(b)\bigr)
<
F+\frac{\nu T}{2}
<
3F.
\tag{32}
\]

Since

\[
F
=
\int_I\mathcal A_{L,K}\,dt
+\int_I\mathcal R_{L,K}\,dt,
\tag{33}
\]

equations (27) and (32) imply

\[
\int_I\mathcal R_{L,K}\,dt
\ge
F-\frac{\nu}{12}D_h(I)
>
\frac{3F}{4}.
\tag{34}
\]

Combining (29), (32), and (34) yields

\[
\boxed{
D_m(I)
\ge
\frac{3}{16C_0^2}
\frac{\nu}{M^2}F
\ge
\frac{3}{64C_0^2}
\frac{\nu^2}{M^2}T.
}
\tag{35}
\]

### 3.2 Half-to-full hitting interval

Suppose instead that for some \(\Theta>0\),

\[
E_K(a)=\frac{\Theta}{2},
\qquad
E_K(b)=\Theta.
\tag{36}
\]

Then

\[
F
=
\frac{\Theta}{4}
+\nu D_h(I),
\qquad
\nu D_h(I)\le F.
\tag{37}
\]

Equations (27), (29), and (37) give

\[
C_0M\sqrt{D_h(I)D_m(I)}
\ge
\frac{11F}{12}.
\tag{38}
\]

Therefore

\[
\boxed{
D_m(I)
\ge
\frac{121}{144C_0^2}
\frac{\nu}{M^2}F
\ge
\frac{121}{576C_0^2}
\frac{\nu}{M^2}\Theta.
}
\tag{39}
\]

The weaker common constant in (35) is sufficient in both cases.
Equivalently,

\[
\boxed{
\nu D_m(I)
\ge
c_{\rm dec}
\left(\frac{\nu}{M}\right)^2
F,
\qquad
c_{\rm dec}:=\frac{3}{16C_0^2}.
}
\tag{40}
\]

This is the promised uniform decrement.  It is scale invariant, and
its constant is independent of \(K\), \(I\), and the event index.

## 4. Application to every terminal pressure-tail event

Assume, as in the conditional ROUTE-R3B genealogy, that for some
\(t_{\rm w}<T^*\),

\[
\operatorname*{ess\,sup}_{t_{\rm w}<t<T^*}
\|v(t)\|_{L^{3,\infty}}
\le M.
\tag{40a}
\]

Retain the notation of the reviewed terminal-flux theorem:

\[
T_j
=
\frac{c_\kappa}{C_{\rm tail}^2}
\sigma_jh_j^{-3},
\qquad
\Lambda_j
=
\frac{\kappa h_j^{-1/2}}{\sigma_j},
\qquad
K_j=R_j\Lambda_j,
\qquad
R_j\longrightarrow1.
\tag{41}
\]

Here \(C_{\rm tail}\) is the smooth-to-sharp multiplier constant from
the reviewed input; it is unrelated to the kernel constant
\(C_{\rm lp}\) in (21).

The adaptive annulus was chosen so that

\[
\int_{I_j}
\|\nabla
Q_{\Lambda_j<|\xi|\le K_j}v\|_2^2\,dt
<
\frac{T_j}{4}.
\tag{42}
\]

Since the sharp tail above \(\Lambda_j\) has dissipation at least
\(T_j\), one has

\[
D_{h_j}(I_j)
:=
\int_{I_j}\|\nabla Q_{>K_j}v\|_2^2\,dt
>
\frac{3T_j}{4}.
\tag{43}
\]

There are two exhaustive cases.

If

\[
E_{K_j}(t_j^-)<\nu T_j,
\tag{44}
\]

take

\[
\widetilde J_j:=I_j.
\tag{45}
\]

Equations (43)--(44) put this interval in the low-entrance case
(30).

If instead

\[
E_{K_j}(t_j^-)\ge\nu T_j,
\tag{46}
\]

the reviewed last-hitting theorem gives

\[
s_j<t_j^-,
\qquad
E_{K_j}(s_j)=\frac{\nu T_j}{2}.
\tag{47}
\]

Let \(r_j\) be the first time after \(s_j\) at which

\[
E_{K_j}(r_j)=\nu T_j.
\tag{48}
\]

It exists by (46), and

\[
\widetilde J_j:=(s_j,r_j)
\tag{49}
\]

is a half-to-full hitting interval with \(\Theta=\nu T_j\).  Since
\(s_j,r_j\to T^*\) along every infinite high-entrance index set, the
inherited weak-\(L^3\) ceiling is available on these intervals for
every sufficiently late index in that set.

Applying (35) or (39), respectively, gives one common conclusion:

\[
\boxed{
\int_{\widetilde J_j}
\left\|
\nabla
\left(
P_{\le K_j}-S_{\eta K_j}
\right)v(t)
\right\|_2^2\,dt
\ge
c_*
\frac{\nu^2}{M^2}T_j,
}
\tag{50}
\]

where \(c_*>0\) depends only on the fixed multiplier and universal
Lorentz constants.  Moreover,

\[
\frac{K_j}{\Lambda_j}\longrightarrow1,
\qquad
\alpha_j,\beta_j\longrightarrow T^*
\quad
\text{for }
\widetilde J_j=(\alpha_j,\beta_j).
\tag{51}
\]

The multiplier in (50) is supported in one fixed lower annulus,

\[
\eta K_j\le|\xi|\le K_j.
\tag{52}
\]

In particular, (22a) and (50) imply the sharp annular statement

\[
\boxed{
\int_{\widetilde J_j}
\|\nabla
Q_{\eta K_j<|\xi|\le K_j}v(t)\|_2^2\,dt
\ge
c_*
\frac{\nu^2}{M^2}T_j.
}
\tag{52a}
\]

Thus the frequency at which the decrement is paid is comparable to the
reviewed parabolic pressure-tail boundary.

## 5. Consequence for the conservative shell survivor

In the conservative shell ledger, let \(F_n\) be the cumulative upward
flux through boundary \(n\) and let \(V_n\) be the viscosity-weighted
dissipation in the immediately preceding comparable band.  The
near-lossless choice used there has

\[
\frac{V_n}{F_n}\longrightarrow0
\tag{53}
\]

over an arbitrarily long depth.

Equation (40) instead gives, for every terminal interval to which the
theorem applies,

\[
\boxed{
\frac{\nu D_m}{F}
\ge
c_{\rm dec}
\left(\frac{\nu}{M}\right)^2
>0.
}
\tag{54}
\]

Hence that near-lossless ledger is not compatible with the weak-\(L^3\)
Navier--Stokes flux mechanism proved here.  A repeated cascade must lose
a uniform fraction at every charged comparable boundary.  If those
bands and intervals are fresh or distinct, its retained flux can
therefore decay at least geometrically with depth.

This closes the specific **near-lossless scalar shell ledger**, whose
distinct shell losses satisfy \(V_n/F_n\to0\).  It does not prove that
the physical event-index charges are fresh, and it does not close an
arbitrarily deep geometrically decaying cascade, because the event
floors \(T_j\) themselves may decay.

## 6. What this advances and what it does not

This theorem adds an NSE-specific input absent from the exact shell
ledger:

1. sharp high-pass flux separates into far-low strain and interactions
   containing a comparable lower-band factor;
2. uniform weak \(L^3\) makes the far-low strain smaller than a fixed
   fraction of viscosity;
3. the terminal low-entrance and half-to-full intervals both force
   lower-band dissipation comparable to their signed flux;
4. every late pressure-tail event therefore pays a fixed physical
   dissipation fraction in
   \(\eta K_j\le|\xi|\le K_j\); and
5. the specific distinct-shell, asymptotically lossless ledger is
   excluded at each charged boundary in this conditional
   same-trajectory setting.

It does **not** prove:

1. that the intervals \(\widetilde J_j\) are disjoint;
2. that lower bands from all event indices have bounded overlap;
3. a scale-zero lower bound independent of \(T_j\);
4. that a geometrically decaying flux chain has finite depth;
5. an intervening selected Besov event;
6. exclusion of the inverse-\(15/4\) direct ancestor;
7. finiteness of the limiting adjoint-pressure cost;
8. exclusion of the conditional ancient profile; or
9. regularity, breakdown, or any Clay alternative A--D.

The revised live question is:

> Does recursive Besov-event spacing give bounded overlap or a
> scale-zero lower bound for the forced lower-band decrements, or can
> one common Navier--Stokes trajectory realise an infinite
> geometrically decaying cascade whose physical costs remain summable?

## 7. Executable certificate

The companion module checks:

1. the admissible ratio \(\eta\);
2. the far-low viscosity fraction;
3. the low-entrance flux and upper bound for \(D_h\);
4. the half-to-full hitting identity;
5. the common lower-band decrement constant;
6. the pressure-tail corollary; and
7. geometric decay forced by repeated uniform decrements.

Run

```text
make adjoint-pressure-flux-decrement
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_flux_decrement -v
```

These computations certify only the scalar constant ledger.  The proof
is the exact Fourier decomposition, divergence-free cancellations, and
Lorentz estimates above.
