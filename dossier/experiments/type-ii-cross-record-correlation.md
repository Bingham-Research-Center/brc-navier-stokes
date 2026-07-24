# Frozen Type-II bands retain correlation or pay fixed replacement work

- **Experiment:** EXP-TYPE-II-CROSS-RECORD-CORRELATION-001
- **Route:** ROUTE-R3C
- **Status:** complete analytic reduction with Hilbert rotation survivor
- **Clay status:** unsolved

This note strengthens the
[cross-record quantile theorem](type-ii-cross-record-quantile.md). Persistence
of a scalar subgrid-energy amount does not say whether the old spectral
content survives. A frozen positive Gaussian band does.

## Verdict

Let \(r_j^{\mathrm L}<r_j^{\mathrm H}\) be two fixed physical-energy
quantiles at a selected first-record time \(t_j\), and put

\[
\gamma:=\eta_{\mathrm H}-\eta_{\mathrm L}>0.
\]

There is a positive self-adjoint Gaussian band operator \(B_j\) such that

\[
\|B_ju(t_j)\|_2^2=2\gamma.
\]

At the next selected record, one of three things must happen:

1. the old band remains genuinely correlated,
   \[
   \langle B_ju(t_{j+1}),B_ju(t_j)\rangle\ge\gamma;
   \]
2. the nonlinear term performs fixed work of magnitude at least
   \(\gamma/2\) against the frozen old band; or
3. viscosity performs fixed work of magnitude at least \(\gamma/2\) against
   that band.

The first branch retains at least \(\gamma/4\) kinetic energy in the old
band at the new record. The nonlinear replacement branch forces

\[
\boxed{
t_{j+1}-t_j
\gtrsim
\frac{
\tau_j\ell_j^{\mathrm L}
}{
q_j^2\log(e+C/\ell_j^{\mathrm L})
},
}
\]

while the viscous replacement branch forces

\[
\boxed{
t_{j+1}-t_j
\gtrsim
\frac{
\tau_j(\ell_j^{\mathrm L})^2
}{
\varepsilon_j d_j
},
\qquad
d_j:=
\frac{
\nu\int_{t_j}^{T^*}\|\nabla u\|_2^2\,dt
}{b_j}
\longrightarrow0.
}
\]

This upgrades persistence of an amount to a precise trichotomy for old
spectral content. It also improves the record-ratio loss in the nonlinear
clock from \(q_j^3\) to \(q_j^2\).

It still does not close R3C. An exact Hilbert-space rotation can move one
fixed energy quantum through orthogonal bands. Every old-band correlation is
destroyed by fixed work, while total energy stays bounded and the event
clocks, weak-\(L^3\) occupation, and viscous-action ledger remain summable.
The tests change with the events, so fixed work is not yet a charge against
one finite common budget.

## 1. The positive Gaussian band

Retain the hypotheses and notation of the cross-record theorem. In
particular,

\[
\mathbf K(r_j^{\mathrm L},t_j)=\eta_{\mathrm L},
\qquad
\mathbf K(r_j^{\mathrm H},t_j)=\eta_{\mathrm H}.
\]

Write

\[
G_rf:=\Gamma_r*f.
\]

Since Gaussian convolution is self-adjoint, define

\[
S_j
:=
G_{r_j^{\mathrm L}}^2-G_{r_j^{\mathrm H}}^2.
\]

Its Fourier multiplier is

\[
e^{-(r_j^{\mathrm L})^2|\xi|^2}
-
e^{-(r_j^{\mathrm H})^2|\xi|^2}
\ge0.
\]

Thus \(S_j\) is positive and has a positive self-adjoint square root

\[
B_j:=S_j^{1/2}.
\]

The two quantile identities give

\[
\begin{aligned}
\|B_ju(t_j)\|_2^2
&=
\langle u(t_j),S_ju(t_j)\rangle\\
&=
\|G_{r_j^{\mathrm L}}u(t_j)\|_2^2
-
\|G_{r_j^{\mathrm H}}u(t_j)\|_2^2\\
&=
2\left[
\mathbf K(r_j^{\mathrm H},t_j)
-
\mathbf K(r_j^{\mathrm L},t_j)
\right]\\
&=
2\gamma.
\end{aligned}
\]

This is a fixed positive energy gap, not just a lower bound.

Set

\[
\psi_j:=S_ju(t_j).
\]

It is smooth, divergence-free, and belongs to \(L^2\). For
\(t\in[t_j,t_{j+1}]\), define the frozen-band correlation

\[
\mathcal C_j(t)
:=
\langle u(t),\psi_j\rangle
=
\langle B_ju(t),B_ju(t_j)\rangle.
\]

At its creation time,

\[
\boxed{
\mathcal C_j(t_j)=2\gamma.
}
\]

## 2. Exact two-time correlation identity

Pair the smooth physical Navier--Stokes equation with the fixed
divergence-free field \(\psi_j\). Pressure vanishes, and integration by
parts gives

\[
\boxed{
\begin{aligned}
\mathcal C_j(t)-2\gamma
={}&
\int_{t_j}^{t}\!\!\int_{\mathbb R^3}
u\otimes u:\nabla\psi_j\,dx\,ds\\
&-
\nu
\int_{t_j}^{t}\!\!\int_{\mathbb R^3}
\nabla u:\nabla\psi_j\,dx\,ds.
\end{aligned}
}
\]

Denote the two terms on the right by

\[
\mathcal W_j^{\mathrm N}(t),
\qquad
\mathcal W_j^\nu(t).
\]

### Theorem 1: correlation or replacement work

At \(t_{j+1}\), at least one of the following holds:

\[
\boxed{
\mathcal C_j(t_{j+1})\ge\gamma,
}
\]

\[
\boxed{
|\mathcal W_j^{\mathrm N}(t_{j+1})|
\ge\frac{\gamma}{2},
}
\]

or

\[
\boxed{
|\mathcal W_j^\nu(t_{j+1})|
\ge\frac{\gamma}{2}.
}
\]

Indeed, if the first alternative fails, the exact identity gives

\[
\left|
\mathcal W_j^{\mathrm N}(t_{j+1})
+
\mathcal W_j^\nu(t_{j+1})
\right|
>
\gamma,
\]

so one work term has magnitude at least \(\gamma/2\).

In the correlation branch, Cauchy--Schwarz and
\(\|B_ju(t_j)\|_2^2=2\gamma\) yield

\[
\|B_ju(t_{j+1})\|_2^2
\ge
\frac{\gamma}{2}.
\]

Hence at least

\[
\frac12\|B_ju(t_{j+1})\|_2^2
\ge
\frac{\gamma}{4}
\]

kinetic energy remains in the frozen old Gaussian band.

## 3. Rate of nonlinear correlation replacement

The endpoint estimate used in the residence theorem gives, for every
Gaussian length \(r>0\),

\[
\|\nabla G_r^2u(t_j)\|_{L^{3,1}}
\le
\frac{Cm_j}{r}
\log\left(
e+\frac{CE_0}{m_j^2r}
\right).
\]

Since \(r_j^{\mathrm L}<r_j^{\mathrm H}\),

\[
\boxed{
\|\nabla\psi_j\|_{L^{3,1}}
\le
\frac{Cm_j}{r_j^{\mathrm L}}
\log\left(
e+\frac{CE_0}{m_j^2r_j^{\mathrm L}}
\right).
}
\]

The next first-record value bounds

\[
\|u(t)\|_{L^{3,\infty}}
\le m_{j+1}=q_jm_j
\]

throughout \([t_j,t_{j+1}]\). Lorentz Hölder therefore gives

\[
\left|
\int u\otimes u:\nabla\psi_j
\right|
\le
\frac{
Cq_j^2m_j^3
}{
r_j^{\mathrm L}
}
\log\left(
e+\frac{CE_0}{m_j^2r_j^{\mathrm L}}
\right).
\]

Using

\[
r_j^{\mathrm L}=R_j\ell_j^{\mathrm L},
\qquad
c_*m_j\le a_jR_j\le m_j,
\qquad
\frac{b_j}{\tau_j}=a_j^3R_j^2,
\]

and the positive upper and lower bounds on \(b_j\), this becomes

\[
\left|
\int u\otimes u:\nabla\psi_j
\right|
\le
\frac{
Cq_j^2
}{
\tau_j\ell_j^{\mathrm L}
}
\log\left(
e+\frac{C}{\ell_j^{\mathrm L}}
\right).
\]

Consequently the nonlinear-work branch of Theorem 1 forces

\[
\boxed{
\Delta t_j
\gtrsim
\frac{
\tau_j\ell_j^{\mathrm L}
}{
q_j^2
\log(e+C/\ell_j^{\mathrm L})
}.
}
\]

Unlike scalar subgrid balance, this work detects decorrelation of the actual
old band. It remains a signed pairing with an event-dependent test.

## 4. Rate of viscous correlation replacement

Ordinary Gaussian convolution bounds give

\[
\|\nabla\psi_j\|_2
\le
\frac{C\sqrt{E_0}}{r_j^{\mathrm L}}.
\]

Let

\[
D_j
:=
\nu
\int_{t_j}^{T^*}\|\nabla u(t)\|_2^2\,dt.
\]

Then Cauchy--Schwarz in time gives

\[
\begin{aligned}
|\mathcal W_j^\nu(t_{j+1})|
&\le
\nu
\|\nabla\psi_j\|_2
\int_{t_j}^{t_{j+1}}\|\nabla u(t)\|_2\,dt\\
&\le
\frac{
C\sqrt{\nu E_0D_j\Delta t_j}
}{
r_j^{\mathrm L}
}.
\end{aligned}
\]

Thus the viscous-work branch forces

\[
\boxed{
\Delta t_j
\gtrsim
\frac{
\gamma^2(r_j^{\mathrm L})^2
}{
\nu E_0D_j
}.
}
\]

Set

\[
d_j:=\frac{D_j}{b_j}.
\]

Terminal absolute continuity and \(b_j\to b>0\) give \(d_j\to0\). Since

\[
\frac{(r_j^{\mathrm L})^2}{\nu}
=
\frac{
\tau_j(\ell_j^{\mathrm L})^2
}{
\varepsilon_j
},
\]

the fixed physical factors may be absorbed to obtain

\[
\boxed{
\Delta t_j
\gtrsim
\frac{
\tau_j(\ell_j^{\mathrm L})^2
}{
\varepsilon_jd_j
}.
}
\]

If \(D_j=0\), the viscous work vanishes and this branch is absent.

## 5. Exact rotation survivor

Use the exact representative powers from the cross-record theorem:

\[
m_j:=2^{2j},
\quad
a_j:=2^{6j},
\quad
R_j:=2^{-4j},
\quad
\tau_j:=2^{-10j},
\quad
\varepsilon_j:=2^{-2j},
\quad
q_j:=4,
\quad
\nu:=1.
\]

Take

\[
\ell_j^{\mathrm H}:=2^{-j},
\qquad
\ell_j^{\mathrm L}:=\frac12\,2^{-j}.
\]

Then the nonlinear replacement clock is

\[
\frac{
\tau_j\ell_j^{\mathrm L}
}{
q_j^2\log(e+C/\ell_j^{\mathrm L})
}
\asymp
\frac{2^{-11j}}{j}.
\]

Attach the summable residence-action ledger

\[
c_j\asymp\frac{2^{-j}}{j},
\qquad
d_j:=\sum_{k>j}c_k
\asymp\frac{2^{-j}}{j}.
\]

Here the \(j\)-th backward residence interval ends at \(t_j\), so the
terminal tail beginning at \(t_j\) contains the later charges \(k>j\).

The viscous replacement clock is then

\[
\frac{
\tau_j(\ell_j^{\mathrm L})^2
}{
\varepsilon_jd_j
}
\asymp
j2^{-9j},
\]

also summable but much longer than the nonlinear clock.

Choose

\[
\Delta t_j\asymp\frac{2^{-11j}}{j}.
\]

As before,

\[
\sum_jm_{j+1}^4\Delta t_j
\lesssim
\sum_j\frac{2^{-3j}}{j}
<\infty,
\qquad
\frac{T^*-t_j}{\tau_j}
\asymp
\frac{2^{-j}}{j}
\longrightarrow0.
\]

Now let \((e_j)_{j\ge1}\) be an orthonormal basis of an abstract Hilbert
space. On the \(j\)-th interval, rotate

\[
\sqrt{2\gamma}\,e_j
\quad\hbox{to}\quad
\sqrt{2\gamma}\,e_{j+1}
\]

through angle \(\pi/2\) at constant angular speed. The squared norm
\(2\gamma\), hence kinetic energy \(\gamma\), is constant. The old
correlation falls from \(2\gamma\) to zero, and the integrated work against
the frozen old vector has magnitude \(2\gamma\). Choosing the angular speed
of order \(\Delta t_j^{-1}\) saturates the nonlinear replacement-rate scale.

The same energy quantum therefore pays every fixed old-band work event while
moving through mutually orthogonal bands. The attached \(c_j\) charges have
finite sum and terminal tail \(d_j\to0\). They may be paid from an additional
orthogonal reservoir whose initial energy exceeds \(\sum_jc_j\); the rotating
quantum then stays fixed while total Hilbert energy decreases by exactly the
prescribed summable charges.

This rotation ledger is exact finite-dimensional Hilbert dynamics on each
event, but it is not a velocity field, does not satisfy the Navier--Stokes
nonlinearity, and does not prove that such band rotations occur on one
physical trajectory. It shows only that energy, orthogonality, fixed
correlation work, the known rate ceilings, and all current scalar budgets do
not contradict one another.

## 6. Route consequence

The terminal-trace branch now has a stronger same-trajectory event law:

\[
\boxed{
\text{old band survives at the next record}
\quad\text{or}\quad
\text{fixed nonlinear/viscous replacement work is paid}.
}
\]

The nonlinear clock loses only \(q_j^2\), but its fixed work is paired with a
new frozen test at every event. The rotation survivor shows why fixed work is
not additive without a common budget.

The next closing theorem must add at least one of:

1. an adjoint or square-function estimate summing the event-dependent
   nonlinear band works against one finite same-trajectory quantity;
2. bounded overlap of the frozen bands together with persistence long enough
   to accumulate their correlated energies at one time;
3. a Navier--Stokes obstruction to the conservative orthogonal-band rotation;
4. spatial recentering of the correlated band on the retained amplitude
   layer;
5. coherent-trace propagation and ancient-Euler rigidity; or
6. separate control of the divergent-normalised-energy branch.

No alternative A--D of the Clay problem is proved.
