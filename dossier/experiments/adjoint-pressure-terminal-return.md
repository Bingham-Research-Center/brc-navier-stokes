# An energy-bounded adjoint pays a quadratic dissipation toll for a terminal return

- **Experiment:** EXP-ADJOINT-PRESSURE-TERMINAL-RETURN-001
- **Route:** ROUTE-R3B
- **Status:** independently reviewed proof-level high--high-to-low
  pressure-tail theorem
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Input:** the independently reviewed
  [dyadic Zeno-frequency countermodel](adjoint-pressure-frequency-zeno.md)
- **Review:** [accepted after two precision repairs and a tail-continuity audit](../review-response-adjoint-pressure-terminal-return-2026-07-24.md)

The Zeno countermodel identifies the sharp failure of a positive
weak-\(L^3\), \(L^1\)-state majorant: an upward path loses \(R_0/R_m\),
then a terminal pressure observation gains \(R_mR_0\).  That calculation
does not use the exact \(L^2\) energy identity of the transported
adjoint.

This note restores that missing physical constraint.

> A high-frequency adjoint tail above \(L\) can return pressure to a low
> output band \(S\ll L\) only through a comparable high-frequency piece
> of the drift.  Adjoint \(L^2\) energy, coefficient dissipation, and
> Littlewood--Paley orthogonality replace the apparent terminal gain
> \(L/S\) by the decay \(S/L\).

Quantitatively, if the integrated low-band return is at least \(p\),
then the resonant drift tail must spend at least

\[
D_{b,\ge L}
\gtrsim
\frac{p^2L^2}
     {S^2T\|z\|_{L^\infty_tL^2_x}^2}.
\]

Thus the exact scalar Zeno return cannot be realised by an
energy-bounded Oseen state and a fixed finite-dissipation coefficient on
one fixed window.  This does not yet close the physical event sequence:
after a new parabolic zoom, the normalised coefficient dissipation can
grow, and the physical event scale can make the pulled-back charge
summable.

## 1. Frequency-resolved pressure return

Fix a smooth dyadic Littlewood--Paley partition
\(\{\Delta_R\}_{R\in2^{\mathbb Z}}\) whose symbol is supported in

\[
\left\{\frac R2\le|\xi|\le2R\right\},
\qquad
\sum_{R\in2^{\mathbb Z}}\widehat{\Delta_R}(\xi)=1
\quad(\xi\ne0).
\tag{1}
\]

Put

\[
\widetilde\Delta_R
:=
\sum_{R/4\le R'\le4R}\Delta_{R'}.
\tag{2}
\]

Let \(S_S\) be a smooth low-frequency projection to
\(\{|\xi|\le2S\}\), and define

\[
P_{>L}:=\sum_{R\ge L}\Delta_R.
\tag{3}
\]

For \(L\ge16S\), define the resonant high--high tensor

\[
\mathcal H_{>L}(z,b)
:=
\sum_{\substack{R\in2^{\mathbb Z}\\R\ge L}}
\Delta_Rz\otimes\widetilde\Delta_Rb.
\tag{4}
\]

The enlarged annulus in (2) can be adjusted by a fixed factor without
changing any conclusion.  Indeed, if
\(\zeta\in\operatorname{supp}\widehat{\Delta_Rz}\) and
\(|\xi|\le2S\), then the product input frequency
\(\eta=\xi-\zeta\) obeys

\[
\frac{3R}{8}\le|\eta|\le\frac{17R}{8}.
\tag{5}
\]

With \(\Pi_S\) defined in (7) below, the partition in (1) therefore
gives the exact cutoff identity

\[
\boxed{
\Pi_S\bigl((P_{>L}z)\otimes b\bigr)
=
\Pi_S\mathcal H_{>L}(z,b).
}
\tag{6}
\]

Thus low--high interactions cannot reach \(S\ll L\); the complete low
output of the state tail is its comparable high--high part.

Write

\[
\mathbb Q:=I-\mathbb P,
\qquad
\Pi_SF:=S_S\mathbb Q\operatorname{div}F.
\tag{7}
\]

For a time interval \((0,T)\), put

\[
D_{b,>L}
:=
\int_0^T
\sum_{R\ge L}
\|\widetilde\Delta_R\nabla b(t)\|_2^2\,dt.
\tag{8}
\]

Finite overlap gives

\[
D_{b,>L}
\le
C_{\rm LP}
\int_0^T\|\nabla b(t)\|_2^2\,dt.
\tag{9}
\]

## 2. High--high-to-low pressure theorem

**Theorem.**
There is a constant \(C_{\rm ret}\), depending only on the fixed
Littlewood--Paley cutoffs and Fourier normalisation, such that for every
\(L\ge16S>0\),

\[
\boxed{
\int_0^T
\|\Pi_S\mathcal H_{>L}(z,b)(t)\|_1\,dt
\le
C_{\rm ret}
\frac SL
\sqrt T\,
\|z\|_{L^\infty(0,T;L^2)}
D_{b,>L}^{1/2}.
}
\tag{10}
\]

The assumptions needed for (10) are only

\[
z\in L^\infty(0,T;L^2),
\qquad
b\in L^2(0,T;\dot H^1).
\tag{11}
\]

No weak-\(L^3\) estimate is used.

### Proof

The localised pressure multiplier in (7) has symbol

\[
\chi(\xi/S)
\frac{\xi_\ell\xi_i\xi_k}{|\xi|^2}.
\tag{12}
\]

Its convolution kernel is integrable with \(L^1\) norm at most
\(C_\chi S\).  One way to see this is to apply one derivative and two
Riesz transforms to the fixed Schwartz low-pass kernel.  The derivative
of the double-Riesz far field is \(O(|x|^{-4})\), and scaling contributes
one power of \(S\).  Therefore

\[
\|\Pi_SF\|_1\le C_\chi S\|F\|_1.
\tag{13}
\]

At each time, (13), Hölder, and annular Bernstein give

\[
\begin{aligned}
\|\Pi_S\mathcal H_{>L}(z,b)\|_1
&\le
C_\chi S
\sum_{R\ge L}
\|\Delta_Rz\|_2
\|\widetilde\Delta_Rb\|_2\\
&\le
C_\chi S
\sum_{R\ge L}
\frac1R
\|\Delta_Rz\|_2
\|\widetilde\Delta_R\nabla b\|_2\\
&\le
C_\chi\frac SL
\left(\sum_{R\ge L}\|\Delta_Rz\|_2^2\right)^{1/2}
\left(
\sum_{R\ge L}
\|\widetilde\Delta_R\nabla b\|_2^2
\right)^{1/2}\\
&\le
C_{\rm ret}\frac SL
\|z\|_2
\left(
\sum_{R\ge L}
\|\widetilde\Delta_R\nabla b\|_2^2
\right)^{1/2}.
\end{aligned}
\tag{14}
\]

The last line uses Littlewood--Paley almost orthogonality and the fixed
overlap of the enlarged annuli.  Integrating (14) and applying
Cauchy--Schwarz in time proves (10).

## 3. Quadratic dissipation toll

If

\[
\int_0^T
\|\Pi_S\mathcal H_{>L}(z,b)(t)\|_1\,dt
\ge p>0
\tag{15}
\]

and

\[
\|z\|_{L^\infty_tL^2_x}\le Q,
\tag{16}
\]

then (10) forces

\[
\boxed{
D_{b,>L}
\ge
\frac{p^2L^2}
     {C_{\rm ret}^2S^2Q^2T}.
}
\tag{17}
\]

Equivalently, a coefficient tail with dissipation \(D\) can return
order-one pressure only from frequencies satisfying

\[
L
\le
\frac{C_{\rm ret}SQ\sqrt{TD}}p.
\tag{18}
\]

For one fixed \(z\), \(b\), and \(T\), the right side of (10) tends to
zero as \(L\to\infty\).  Consequently no fixed finite-dissipation Oseen
coefficient and uniformly energy-bounded state can support the Zeno
model's order-one terminal returns at unbounded top frequencies.

## 4. Exact adjoint-energy application

Let \(a\) solve the smooth Oseen adjoint

\[
\partial_ta-\nu\Delta a-b\cdot\nabla a+\nabla\pi^*=0,
\qquad
\nabla\cdot a=\nabla\cdot b=0,
\qquad
a(0)=\psi.
\tag{19}
\]

Skew transport gives

\[
\|a(t)\|_2^2
+2\nu\int_0^t\|\nabla a(s)\|_2^2\,ds
=
\|\psi\|_2^2.
\tag{20}
\]

Taking \(z=a\) in (10) therefore yields

\[
\boxed{
\int_0^T
\|\Pi_S\mathcal H_{>L}(a,b)(t)\|_1\,dt
\le
C_{\rm ret}
\frac SL
\sqrt T\,\|\psi\|_2D_{b,>L}^{1/2}.
}
\tag{21}
\]

This estimate controls the complete resonant high-frequency adjoint
tail returning to the selected low pressure band.  It is not an
estimate for one chosen Fourier monomial only, so unwanted
high--high cancellations or cross-interactions do not evade it.

## 5. Why the scalar packet ledger misses the toll

At frequency \(R\), place both fields in a volume \(R^{-3}\).  An
energy-normalised state has amplitude \(R^{3/2}\), while a critical
drift packet has amplitude \(R\).  The exact norm ledger is

\[
\|z_R\|_2^2\asymp1,
\qquad
\|b_R\|_2^2\asymp R^{-1},
\qquad
\|\nabla b_R\|_2^2\asymp R.
\tag{22}
\]

Moreover,

\[
\|z_R\otimes b_R\|_1^2\asymp R^{-1}.
\tag{23}
\]

Thus a fixed low output \(S\) has squared pressure scale

\[
S^2R^{-1},
\tag{24}
\]

which exactly matches the square of the right side of (14):

\[
\left(\frac SR\right)^2
\|z_R\|_2^2
\|\nabla b_R\|_2^2
\asymp
\frac{S^2}{R}.
\tag{25}
\]

The factor \(S/R\) in (10) is therefore sharp at the norm-scaling
level.

By contrast, if one tries to localise the scalar Zeno path's top
\(L^1\) mass \(R^{-1}\) inside the critical volume \(R^{-3}\), the
resulting packet has

\[
\boxed{
\|z_R\|_2^2
\asymp
\frac{R^{-2}}{R^{-3}}
=R.
}
\tag{26}
\]

It violates a uniform adjoint-energy ceiling.  If
\(\|z_R\|_2\le1\), Cauchy--Schwarz instead forces support volume at
least \(R^{-2}\), one factor \(R\) larger than the critical drift
packet.  The lost overlap is precisely what the terminal-return
estimate detects.

The kinematic coefficient ledger in the Zeno note is still correct: a
critical drift packet active for one heat time \(R^{-2}\) spends
dissipation \(R^{-1}\).  But then its terminal pressure acts for only
that short time and cannot generate the scalar model's order-one
finite-window return.  Maintaining that return for order-one time would
cost the quadratic tail dissipation in (17).

## 6. Terminal-layer consequence

For the reviewed zero-data feedback remainder on a layer of length
\(h\),

\[
\sup_{0<t<h}\|r(t)\|_2\le C_rh.
\tag{27}
\]

If a fixed pressure fraction \(p\) is produced by inputs above \(L\)
and returned to a fixed output band \(S\), equations (17) and (27) give

\[
\boxed{
D_{b,>L}(h)
\ge
c\frac{p^2L^2}{S^2h^3}.
}
\tag{28}
\]

In particular, if \(L=h^{-\alpha}\), the necessary coefficient
dissipation has power

\[
D_{b,>L}(h)\gtrsim h^{-(3+2\alpha)}.
\tag{29}
\]

This is a frequency-localised necessary condition, not merely a lower
bound on total coefficient dissipation.

## 7. Physical scaling and exact frontier

Let \(\sigma\) be a physical event length and use the parabolic pullback

\[
b_\sigma(x,\tau)
:=
\sigma
v(x_0+\sigma x,t_0-\sigma^2\tau).
\tag{30}
\]

The band dissipation transforms as

\[
D_{b_\sigma}^{\rm norm}
=
\sigma^{-1}D_v^{\rm phys}.
\tag{31}
\]

Therefore (17) gives the physical charge

\[
\boxed{
D_{v,\rm band}^{\rm phys}
\ge
c\sigma
\frac{p^2L^2}{S^2Q^2T}.
}
\tag{32}
\]

This closes the following proposal:

> The Zeno path's reciprocal terminal gain can persist on one fixed
> finite-dissipation coefficient while the transported state obeys its
> exact \(L^2\) energy identity.

It cannot.  A normalised band \(R\) in (8) is the physical frequency
band \(R/\sigma\) in (31), so the tail \(R\ge L\) corresponds to
physical frequencies at least \(L/\sigma\).

Equation (32) still need not contradict finite dissipation along an
event sequence.  The physical high-frequency tails are nested rather
than disjoint and may reuse the same finer dissipation, while the full
weights

\[
\sigma_j
\frac{p_j^2L_j^2}{S_j^2Q_j^2T_j}
\tag{33}
\]

may shrink fast enough to remain summable.

On the terminal layer, \(Q_j\lesssim h_j\), \(T_j=h_j\), and fixed
\(p_j,S_j\) make the forced physical charge

\[
\boxed{
D_{v,\rm tail}^{\rm phys}
\gtrsim
\sigma_jL_j^2h_j^{-3}.
}
\tag{34}
\]

There is nevertheless a same-trajectory consequence which does not
require disjoint bands.  For a finite-energy Navier--Stokes trajectory
before a first singular time \(T^*\), define the global physical
dissipation tail

\[
\mathcal E_{\ge\Lambda}(v)
:=
\int_0^{T^*}
\sum_{K\ge\Lambda}
\|\widetilde\Delta_K\nabla v(t)\|_2^2\,dt.
\tag{35}
\]

Littlewood--Paley finite overlap and the energy inequality give

\[
\mathcal E_{\ge\Lambda}(v)
\longrightarrow0
\qquad(\Lambda\to\infty).
\tag{36}
\]

For an event pullback \(b_j\) on its physical time interval, scaling
and restriction to that interval give

\[
\sigma_jD_{b_j,>L_j}
\le
C_{\rm LP}
\mathcal E_{\ge cL_j/\sigma_j}(v).
\tag{37}
\]

Consequently, whenever \(L_j/\sigma_j\to\infty\), equations (32),
(36), and (37) force the exact upper ceiling

\[
\boxed{
\sigma_j
\frac{p_j^2L_j^2}{S_j^2Q_j^2T_j}
\longrightarrow0.
}
\tag{38}
\]

On the terminal layer with fixed \(p_j,S_j\), this becomes

\[
\boxed{
\sigma_jL_j^2h_j^{-3}\longrightarrow0.
}
\tag{39}
\]

Thus if \(L_j=h_j^{-\alpha}\), the terminal-return branch requires

\[
\sigma_j=o\!\left(h_j^{3+2\alpha}\right).
\tag{40}
\]

For the reviewed logarithmic interaction depth

\[
N(h)=\left\lfloor c_{\rm dep}\log\frac1h\right\rfloor,
\qquad
L(h)=2^{N(h)},
\tag{41}
\]

put \(\alpha_{\rm dep}:=c_{\rm dep}\log2\).  Then
\(L(h)\asymp h^{-\alpha_{\rm dep}}\), up to a fixed dyadic factor, and
the dyadic Zeno terminal-return mechanism can survive only if

\[
\boxed{
\sigma_j
=
o\!\left(h_j^{3+2\alpha_{\rm dep}}\right).
}
\tag{42}
\]

The weaker condition \(\sigma_j=o(L_j^{-2})\) is not sufficient.

The remaining theorem must contradict (38) using a lower
top-frequency law, make the vanishing nested charges quantitatively
non-reusable, or couple the top frequency to the actual next-event
scale.

This note does not derive a lower top-frequency law strong enough to
contradict (38), sum the intermediate Oseen itinerary, prove a
Navier--Stokes event-ancestry law, establish regularity, or resolve any
Clay alternative.

## Reproduce

```bash
make adjoint-pressure-terminal-return
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_terminal_return -v
```
