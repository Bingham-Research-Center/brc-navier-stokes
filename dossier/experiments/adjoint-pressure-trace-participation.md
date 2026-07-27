# Band limitation forces bulk participation of the charged pressure window

- **Experiment:** EXP-ADJOINT-PRESSURE-TRACE-PARTICIPATION-001
- **Route:** ROUTE-R3B
- **Status:** conditional analytic reduction;
  [adversarially recomputed valid after topology repair](../review-ledger.md)
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** adversarially recomputed
  temporal-disintegration theorem,
  first-hitting polar-vacuum theorem,
  balanced Kato-polar compactness theorem,
  and finite-amplitude window theorem

The balanced finite-band branch has one fixed smooth
relative-amplitude observable \(W_h\) with positive signed pressure
pairing:

\[
-\int_0^h\!\!\int_{\mathbb R^3}W_h\cdot H_h
\ge p_{\rm win}>0.
\tag{1}
\]

The first version of this note combined (1) with the new estimate

\[
\int_0^h\|H_h(t)\|_2^2\,dt\le Ch
\tag{2}
\]

and obtained only an \(h^7\) source-cylinder participation fraction.
Its proposed sharp moving-tube model was wrong: it checked fixed cell
families while the reviewed capture theorem permits a different family
at every time. The active cells in that model would capture order-one
pressure mass although their moving-grid ceiling is \(O(h^{7/6})\).

Using that failed model adversarially exposes a stronger theorem. The
finite-band field \(H_h\) is supported in one fixed Fourier annulus at
frequency \(K\asymp h^{-1/2}\). A reproducing kernel controls the
pressure on the low-density part of any measurable set, while the
reviewed moving-grid law controls its high-density cells. If

\[
R=h^{-3},
\qquad
\mathfrak d_h(F):=\frac{|F|}{hR^3},
\tag{3}
\]

then every measurable
\(F\subset(0,h)\times B_{BR}\) satisfies

\[
\boxed{
\int_F|H_h|
\le
C_B\min\left\{1,\mathfrak d_h(F)^{1/7}\right\}.
}
\tag{4}
\]

After a fixed lower cutoff on \(|W_h|\), (1) and (4) force the positive
alignment set \(E_h\) to obey

\[
\boxed{
|E_h|\ge c\,hR^3\asymp c h^{-8}.
}
\tag{5}
\]

This matches the first-hitting upper scale. The charged compact window
therefore occupies a fixed positive source-cylinder fraction, not an
\(h^7\) fraction. Moreover, a fixed positive fraction of the
finite-band pressure-root law sees a compact-window profile with
nonzero strong full-time, local-in-space \(L^2\) norm.

This excludes the earlier **pure zero-profile moving thin-layer
mechanism**. It does not yet identify the signed pressure mark with a
conditional time trace of the nonzero limiting profile, close
concentration in the unwindowed Oseen products, or resolve the strict
sub-\(h^9\) branch.

## 1. Reviewed balanced finite-band input

Retain

\[
K=\kappa h^{-1/2},
\qquad
\ell=K^{-1},
\qquad
R=h^{-3},
\tag{6}
\]

\[
r^{\rm lo}=S_{AK}r,
\qquad
b^{\rm lo}=S_Kb^{\rm in},
\tag{7}
\]

\[
H_h
:=
P_{>K}
\nabla\Delta^{-1}\operatorname{div}
\bigl((r^{\rm lo}\cdot\nabla)b^{\rm lo}\bigr).
\tag{8}
\]

The zero-data feedback estimate holds at every terminal time:

\[
\boxed{
\|r(t)\|_2^2
+\nu\int_0^t\|\nabla r(s)\|_2^2\,ds
\le C_rt^2
\qquad(0\le t\le h).
}
\tag{9}
\]

The coefficient has the critical endpoint bound

\[
\sup_{t\le h}
\|b(t)\|_{L^{3,\infty}}
\le M.
\tag{10}
\]

The finite-band pressure satisfies

\[
p_{\rm pol}
\le
Z_h:=\int_0^h\!\!\int_{\mathbb R^3}|H_h|
\le C_{\rm pol}.
\tag{11}
\]

For every measurable time-dependent finite family
\(\mathcal F(t)\) of \(\ell\)-cubes, with
\[
U_{\mathcal F}(t)
:=
\bigcup_{m\in\mathcal F(t)}Q_m,
\qquad
N_{\mathcal F}(t):=|\mathcal F(t)|,
\tag{12}
\]
the reviewed moving-grid theorem gives

\[
\boxed{
\int_0^h\int_{U_{\mathcal F}(t)}|H_h|
\le
C_{\rm mov}h^{3/2}
\left(
K\int_0^hN_{\mathcal F}(t)^{1/3}\,dt
\right)^{1/2}.
}
\tag{13}
\]

For fixed \(B>32\) and every \(N_0\),

\[
\int_0^h\int_{|x|>BR}|H_h|
\le C_{B,N_0}(KR)^{-N_0}.
\tag{14}
\]

The low-pass factors in (8) have Fourier support below fixed multiples
of \(K\). Thus

\[
\boxed{
\operatorname{supp}\widehat H_h(t,\cdot)
\subset
\{\xi:c_AK\le|\xi|\le C_AK\}
}
\tag{15}
\]

for almost every \(t\), after harmless adjustment of the fixed annular
constants.

On the balanced branch,

\[
0<\theta_-
\le
\theta_h:=\frac{\varepsilon_h}{h^9}
\le\theta_+<\infty.
\tag{16}
\]

The reviewed amplitude theorem constructs one fixed smooth map
\(\mathcal W:\overline{B_1(0)}\to\mathbb R^3\) such that

\[
W_h
=
\mathcal W\left(
\frac{a_h}{\sqrt{|a_h|^2+\varepsilon_h^2}}
\right),
\qquad
\|W_h\|_\infty\le C_W,
\tag{17}
\]

\[
\operatorname{supp}W_h
\subset
\left\{
\underline r
\le
\frac{|a_h|}{\varepsilon_h}
\le
\overline r
\right\},
\qquad
0<\underline r<\overline r<\infty,
\tag{18}
\]

and (1).

## 2. A useful but non-sharp spacetime \(L^2\) estimate

Multiplication by the fixed source cutoff preserves the weak-\(L^3\)
bound. Lorentz--Bernstein and (6), (7), and (10) give

\[
\|\nabla b^{\rm lo}(t)\|_\infty
\le
CK^2\|b^{\rm in}(t)\|_{L^{3,\infty}}
\le C_MK^2.
\tag{19}
\]

The low-pass is \(L^2\)-bounded, so (9) gives

\[
\|r^{\rm lo}(t)\|_2\le Ct.
\tag{20}
\]

The two pressure multipliers in (8) are order-zero on \(L^2\).
Consequently

\[
\begin{aligned}
\|H_h(t)\|_2
&\le
C\|(r^{\rm lo}\cdot\nabla)b^{\rm lo}\|_2\\
&\le
C\|r^{\rm lo}(t)\|_2
\|\nabla b^{\rm lo}(t)\|_\infty\\
&\le C_MK^2t.
\end{aligned}
\tag{21}
\]

Integration and \(K=\kappa h^{-1/2}\) yield

\[
\boxed{
\int_0^h\|H_h(t)\|_2^2\,dt
\le C_MK^4h^3
\le C_{M,\kappa}h.
}
\tag{22}
\]

By itself, (22) and Cauchy--Schwarz give only a lower volume
\(ch^{-1}\). Section 4 uses the spatial band limitation and recovers
the seven missing powers.

## 3. A thresholded positive alignment retains fixed charge

Choose \(B\), then \(h\) sufficiently small, so that (14) and (17)
give

\[
\int_0^h\int_{|x|>BR}|W_h||H_h|
\le\frac{p_{\rm win}}4.
\tag{23}
\]

Thus

\[
-\int_0^h\int_{B_{BR}}W_h\cdot H_h
\ge\frac{3p_{\rm win}}4.
\tag{24}
\]

Choose one fixed

\[
0<\eta<\frac{p_{\rm win}}{4C_{\rm pol}}.
\tag{25}
\]

The absolute pairing on \(\{|W_h|<\eta\}\) is at most
\(\eta Z_h\le p_{\rm win}/4\). Define

\[
E_h
:=
\left\{
(t,x)\in(0,h)\times B_{BR}:
-W_h(t,x)\cdot H_h(t,x)>0,
|W_h(t,x)|\ge\eta
\right\}.
\tag{26}
\]

The positive part dominates the remaining signed integral, hence

\[
\boxed{
\int_{E_h}|W_h||H_h|
\ge
p_1:=\frac{p_{\rm win}}2.
}
\tag{27}
\]

First hitting gives the complementary crude upper bound. Put

\[
\Phi(r):=\sqrt{1+r^2}-1,
\qquad
\Phi_-:=\Phi(\underline r)>0.
\tag{28}
\]

Since

\[
\int_{\mathbb R^3}
\rho_{\varepsilon_h}(a_h(t))\,dx
\le M_\rho,
\qquad
\rho_{\varepsilon_h}(a)
=
\varepsilon_h\Phi(|a|/\varepsilon_h),
\tag{29}
\]

the support condition (18) gives

\[
|E_h|
\le
\frac{M_\rho h}{\varepsilon_h\Phi_-}
\le C h^{-8}
=C hR^3.
\tag{30}
\]

## 4. Band limitation and moving capture give source-volume absolute continuity

We prove (4) for an arbitrary measurable
\[
F\subset(0,h)\times B_{BR}.
\tag{31}
\]

Choose a Schwartz multiplier \(\Psi_K\) whose symbol is one on the
annulus (15). Then

\[
H_h=\Psi_K*H_h,
\qquad
|\Psi_K(x)|
\le C_NK^3(1+K|x|)^{-N}
\tag{32}
\]

for every fixed \(N\).

Use the grid

\[
Q_m:=\ell(m+[0,1)^3),
\qquad m\in\mathbb Z^3.
\tag{33}
\]

For almost every \(t\), set

\[
d_m(t)
:=
\frac{|F_t\cap Q_m|}{\ell^3},
\qquad
F_t:=\{x:(t,x)\in F\},
\tag{34}
\]

and

\[
w_m(t)
:=
\int_{\mathbb R^3}
\left(1+K\,\operatorname{dist}(y,Q_m)\right)^{-N}
|H_h(t,y)|\,dy.
\tag{35}
\]

For \(x\in Q_m\), (32) gives

\[
|H_h(t,x)|
\le C_N\ell^{-3}w_m(t).
\tag{36}
\]

If \(N>3\), lattice summability gives

\[
\sum_{m\in\mathbb Z^3}w_m(t)
\le C_N\|H_h(t)\|_1.
\tag{37}
\]

Fix \(0<\lambda<1\). On cells with \(d_m(t)\le\lambda\),
(36), (37), and (11) give

\[
\begin{aligned}
\int_0^h
\sum_{d_m(t)\le\lambda}
\int_{F_t\cap Q_m}|H_h|
&\le
C_N\lambda\int_0^h\sum_mw_m(t)\,dt\\
&\le C\lambda Z_h\\
&\le C\lambda.
\end{aligned}
\tag{38}
\]

Let

\[
\mathcal F_\lambda(t)
:=
\{m:d_m(t)>\lambda\},
\qquad
N_\lambda(t):=|\mathcal F_\lambda(t)|.
\tag{39}
\]

Because \(F_t\subset B_{BR}\), this is a measurable finite family. Its
count obeys

\[
N_\lambda(t)
\le
\frac{|F_t|}{\lambda\ell^3}.
\tag{40}
\]

Jensen's inequality therefore gives

\[
\begin{aligned}
\int_0^hN_\lambda(t)^{1/3}\,dt
&\le
h^{2/3}
\left(
\frac{|F|}{\lambda\ell^3}
\right)^{1/3}\\
&=
h
\left(
\frac{\mathfrak d_h(F)N_{\rm src}}{\lambda}
\right)^{1/3},
\end{aligned}
\tag{41}
\]

where

\[
N_{\rm src}:=\left(\frac R\ell\right)^3
\asymp h^{-21/2}.
\tag{42}
\]

Apply the moving-grid estimate (13) to
\(\mathcal F_\lambda(t)\). Equations (41), (42), and (6) yield

\[
\begin{aligned}
\int_0^h
\int_{U_{\mathcal F_\lambda}(t)}|H_h|
&\le
Ch^{3/2}(Kh)^{1/2}
N_{\rm src}^{1/6}
\left(
\frac{\mathfrak d_h(F)}{\lambda}
\right)^{1/6}\\
&=
Ch^2KR^{1/2}
\left(
\frac{\mathfrak d_h(F)}{\lambda}
\right)^{1/6}\\
&\le
C_\kappa
\left(
\frac{\mathfrak d_h(F)}{\lambda}
\right)^{1/6}.
\end{aligned}
\tag{43}
\]

The critical cancellation in the last line is exact:

\[
h^2KR^{1/2}
=
\kappa h^{2-1/2-3/2}
=\kappa.
\tag{44}
\]

Combining (38) and (43),

\[
\int_F|H_h|
\le
C\left[
\lambda+
\left(
\frac{\mathfrak d_h(F)}{\lambda}
\right)^{1/6}
\right].
\tag{45}
\]

If \(0<\mathfrak d_h(F)\le1\), choose

\[
\lambda=\mathfrak d_h(F)^{1/7}.
\tag{46}
\]

Both terms in (45) then equal
\(\mathfrak d_h(F)^{1/7}\). If
\(\mathfrak d_h(F)>1\), use the global bound (11).
This proves (4).

The exponent \(1/7\) is not asserted optimal. It is the exact output of
the one-sixth moving-grid capture exponent and the cell-density split.

## 5. The charged window has fixed source-bulk participation

Apply (4) to \(E_h\). Equations (17) and (27) give

\[
p_1
\le
C_W\int_{E_h}|H_h|
\le
C\mathfrak d_h(E_h)^{1/7}.
\tag{47}
\]

Therefore

\[
\boxed{
\mathfrak d_h(E_h)\ge c_*>0,
\qquad
|E_h|\ge c_*hR^3\asymp c_*h^{-8}.
}
\tag{48}
\]

Together with (30),

\[
\boxed{
c_*
\le
\frac{|E_h|}{hR^3}
\le C_*.
}
\tag{49}
\]

Since \(|W_h|\ge\eta\) on \(E_h\),

\[
\boxed{
\frac1{hR^3}
\int_0^h\int_{B_{BR}}|W_h|^2
\ge
\eta^2c_*.
}
\tag{50}
\]

Thus the earlier \(h^7\) participation floor was not sharp. It discarded
the annular Fourier structure of \(H_h\). The corrected lower bound is
order one on the source cylinder and matches the first-hitting upper
scale.

More generally, (4) says that no family
\(F_h\subset(0,h)\times B_{BR}\) with
\(\mathfrak d_h(F_h)\to0\) can carry a fixed amount of either
\(|H_h|\)-mass or the bounded-window absolute pairing.

## 6. A fixed fraction of pressure roots sees a nonzero window profile

The bulk statement can be tied to the already compact pressure-root
profile law. Let

\[
\mathcal I_B:=\{m:Q_m\cap B_{BR}\ne\varnothing\}.
\tag{51a}
\]

For \(m\in\mathcal I_B\), define its full spacetime alignment duty

\[
q_m
:=
\frac{
|E_h\cap((0,h)\times Q_m)|
}{h\ell^3}
\in[0,1].
\tag{51}
\]

There are at most \(C_BN_{\rm src}\) such cells. For
\(0<\delta<1\), put

\[
\mathcal G_\delta
:=
\{m\in\mathcal I_B:q_m>\delta\}.
\tag{52}
\]

The part of \(E_h\) in cells outside \(\mathcal G_\delta\) has

\[
\mathfrak d_h
\left(
E_h\cap
\bigl((0,h)\times
U_{\mathcal I_B\setminus\mathcal G_\delta}\bigr)
\right)
\le C_B\delta.
\tag{53}
\]

By (4), its absolute windowed pairing is at most
\(C\delta^{1/7}\). Choose a fixed \(\delta_0>0\), independent of \(h\),
so small that this is at most \(p_1/2\). Equations (27) and (53) then
give

\[
\int_0^h\int_{U_{\mathcal G_{\delta_0}}}|H_h|
\ge
\frac{p_1}{2C_W}.
\tag{54}
\]

Recall the finite-band pressure-root probability

\[
d\Gamma_h^{\rm fb}(t,x)
:=
\frac{|H_h(t,x)|}{Z_h}\,dt\,dx.
\tag{55}
\]

Using \(Z_h\le C_{\rm pol}\), (54) implies

\[
\Gamma_h^{\rm fb}
\{(t,x):x\in U_{\mathcal G_{\delta_0}}\}
\ge
q_0
:=
\frac{p_1}{2C_WC_{\rm pol}}>0.
\tag{56}
\]

For a root \(x\), define

\[
\mathsf W_{h,x}(s,y)
:=
W_h(hs,x+\ell y).
\tag{57}
\]

If \(x\in Q_m\) and \(q_m>\delta_0\), then
\(Q_m\subset B_{\sqrt3\ell}(x)\), and hence

\[
\boxed{
\|\mathsf W_{h,x}\|_
{L^2((0,1)\times B_{\sqrt3})}^2
\ge
\eta^2q_m
>
\eta^2\delta_0.
}
\tag{58}
\]

Consequently a fixed \(\Gamma_h^{\rm fb}\)-probability \(q_0\) sees a
window profile bounded away from zero in strong full-time,
local-in-space \(L^2\). Because
\(W_h=\mathcal W(\mathsf Z_h)\) with fixed smooth
\(\mathcal W\), the reviewed full-time strong-topology tightness of the
polar profile laws also applies to \(\mathsf W_{h,x}\) on

\[
\mathcal X_W
:=
L^2\!\left(
(0,1);L^2_{\rm loc}(\mathbb R^3)
\right).
\tag{58a}
\]

The projective topology on \(\mathcal X_W\) is generated by the
full-time norms
\(\|\cdot\|_{L^2((0,1)\times B_D)}\); it is local only in space. Hence

\[
\mathcal C_0
:=
\left\{
w\in\mathcal X_W:
\|w\|_{L^2((0,1)\times B_{\sqrt3})}^2
\ge\eta^2\delta_0
\right\}
\tag{58b}
\]

is closed. If \(\mu_h\) is the window-profile pushforward of
\(\Gamma_h^{\rm fb}\) and \(\mu_h\Rightarrow\mu\) in
\(\mathcal X_W\), (58) and the closed-set Portmanteau inequality give

\[
q_0
\le
\limsup_{h\downarrow0}\mu_h(\mathcal C_0)
\le
\mu(\mathcal C_0).
\tag{58c}
\]

Thus every such limiting window-profile law assigns probability at
least \(q_0\) to profiles bounded away from zero.

This is a nonzero compact-window **profile-law** statement. It is not a
nonzero amplitude-normalised Oseen solution, and it does not yet say
that the original signed point trace is represented by evaluation of
that limiting profile.

## 7. The former moving-tube model is a rejected countermodel

The failed sharpness proposal used

\[
N_{\rm src}=h^{-21/2}
\tag{59}
\]

source cells, scaled-time duty

\[
\delta_h=h^7,
\tag{60}
\]

and actual-time pressure amplitude \(2hs\) at scaled time \(s\). An
idealised equidistributed schedule then has

\[
\int|H_h^{\rm mod}|=1,
\qquad
\int|H_h^{\rm mod}|^2=\frac43h,
\qquad
|E_h^{\rm mod}|=h^{-1}.
\tag{61}
\]

At each time, however, all of its mass lies in only

\[
N_{\rm act}
=
N_{\rm src}\delta_h
=h^{-7/2}
\tag{62}
\]

cells. Selecting those cells at that time and applying (13) gives

\[
\int|H_h^{\rm mod}|
\le
Ch^{7/4}
\left(h^{-7/2}\right)^{1/6}
=Ch^{7/6}
\longrightarrow0,
\tag{63}
\]

contradicting (61). The former calculation considered only fixed
partial families and missed this moving selector. The amplitude in
(61) is written as a function of the actual scaled time, rather than an
interval centre, so no separate terminal-boundary artefact is involved.

The model remains useful only as a rejected test: the spacetime
\(L^2\) estimate permits an \(h^7\) trace, but band limitation together
with moving capture does not.

## 8. Exact consequence and remaining gate

On every norm-gated balanced first-hitting charged finite-band
subsequence:

1. the finite-band pressure satisfies
   \(\|H_h\|_{L^2_{t,x}}^2\lesssim h\);
2. its total variation has the source-volume absolute-continuity
   modulus (4);
3. the thresholded positive compact-window alignment occupies a fixed
   positive fraction of the entire inverse-cubic source cylinder;
4. the compact window has uniformly positive source-averaged
   spacetime \(L^2\) occupation;
5. a fixed positive fraction of pressure roots sees a compact-window
   profile bounded away from zero in strong full-time, local-in-space
   \(L^2\);
6. the former \(h^7\)-duty moving-tube countermodel violates the
   reviewed moving-grid law and is rejected.

This closes disappearance of the whole charged window into a
source-volume-vanishing moving layer. It does not prove:

- that the signed pressure-selected point trace equals an evaluation or
  integral of the nonzero limiting compact-window profile;
- conditional decorrelation or absolute continuity of pressure time
  given that profile;
- closure of unwindowed amplitude concentration in the Oseen drift and
  pressure products;
- a finite charge for the strict sub-\(h^9\) amplitude cascade;
- an event-index telescope, finite same-trajectory budget, limiting
  Oseen rigidity theorem, regularity theorem, breakdown theorem, or
  Clay alternative A--D.

The exact balanced question is now:

> Can the transformed Oseen equation and the source-volume
> absolute-continuity modulus identify the surviving signed pressure
> mark with the nonzero compact-window profile law, and then close the
> remaining unwindowed Oseen products?

The subsequent adversarially recomputed
product-law pressure-trace theorem
answers the first clause conditionally: the complete spatially
reproduced compact-window mark survives as a positive pairing against a
weak-\(L^{7/6}\) density over independent full-layer time and the
uniform-root profile law. The remaining balanced gate is now the second
clause: close and identify the unwindowed Oseen products.

## Reproduce

```bash
make adjoint-pressure-trace-participation
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_trace_participation -v
make check
git diff --check
```
