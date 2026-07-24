# Type-II subgrid quantiles obey a cross-record persistence-or-clock law

- **Experiment:** EXP-TYPE-II-CROSS-RECORD-QUANTILE-001
- **Route:** ROUTE-R3C
- **Status:** complete analytic reduction with scalar power survivor
- **Clay status:** unsolved

This note continues the
[record-high residence theorem](type-ii-record-flux-residence.md). That
theorem controls one carrier backwards from its terminal trace defect. Here
the same physical Navier--Stokes trajectory is followed forwards to the next
selected first-record carrier.

## Verdict

In the energy-efficient terminal-trace branch, choose two fixed physical
subgrid-energy levels

\[
0<\eta_{\mathrm L}<\eta_{\mathrm H}.
\]

At each selected first record \(t_j\), let \(r_j^{\mathrm L}\) and
\(r_j^{\mathrm H}\) be their first Gaussian-filter crossing lengths. These
lengths are canonical, satisfy

\[
0<r_j^{\mathrm L}\le r_j^{\mathrm H},
\qquad
\frac{r_j^\alpha}{R_j}\longrightarrow0,
\]

and carry the same physical energy levels at every event.

Put

\[
q_j:=\frac{m_{j+1}}{m_j},
\qquad
\Delta t_j:=t_{j+1}-t_j,
\qquad
\ell_j^{\mathrm H}:=\frac{r_j^{\mathrm H}}{R_j}.
\]

For every sufficiently large \(j\), actual NSE evolution gives the
exhaustive alternative

\[
\boxed{
r_{j+1}^{\mathrm L}\le r_j^{\mathrm H}
}
\]

or

\[
\boxed{
\Delta t_j
\gtrsim
\frac{
\tau_j\ell_j^{\mathrm H}
}{
q_j^3
\log\!\left(e+C/(q_j^2\ell_j^{\mathrm H})\right)
}.
}
\]

Thus a rapid next record inherits a fixed positive amount of subgrid energy
below the previous event's physical high-quantile boundary. If that
quantile does not persist, the record gap must pay the displayed clock.
This is a genuine same-trajectory, cross-event theorem.

It is not freshness and it is not a contradiction. The compatible ledger

\[
m_j=2^{2j},
\quad
\ell_j^{\mathrm H}=2^{-j},
\quad
\varepsilon_j\asymp2^{-2j},
\quad
\tau_j\asymp2^{-10j}
\]

makes the residence charge \(\asymp2^{-j}/j\), the cross-record clock
\(\asymp2^{-11j}/j\), and even the worst first-record occupation
\(m_{j+1}^4\Delta t_j\asymp2^{-3j}/j\) all summable. Its physical quantile
length is \(r_j^{\mathrm H}\asymp2^{-5j}\), so every event may take the
persistence branch through an accelerating Zeno scale chain.

The remaining theorem must therefore turn persistence of an energy amount
into a non-reusable fresh charge, impose a nonsummable dynamical cost on the
passage between two subgrid quantiles, or constrain the record ratios \(q_j\)
and their clocks by new NSE structure.

## 1. One physical subgrid-energy function

Let \(u\) be one smooth finite-energy Navier--Stokes solution on
\([0,T^*)\), and use the centred Gaussian

\[
\Gamma_r(x)
:=
(2\pi r^2)^{-3/2}
\exp\left(-\frac{|x|^2}{2r^2}\right).
\]

Define

\[
\mathbf K(r,t)
:=
\frac12
\left(
\|u(t)\|_2^2-\|\Gamma_r*u(t)\|_2^2
\right).
\]

For every fixed \(t<T^*\), the function \(r\mapsto\mathbf K(r,t)\) is
continuous and nondecreasing, with \(\mathbf K(0,t)=0\).

For the carrier

\[
v_j(y,s)
:=
\frac1{a_j}
u(x_j+R_jy,t_j+\tau_js),
\qquad
b_j:=a_j^2R_j^3,
\]

Gaussian covariance gives the exact identity

\[
\boxed{
\mathbf K(R_j\ell,t_j+\tau_js)
=
b_j\mathcal K_\ell[v_j(s)].
}
\]

In the energy-efficient branch, pass to the already available subsequence
on which

\[
b_j\longrightarrow b>0.
\]

Suppose its terminal trace-defect measure has

\[
\Delta_\chi
:=
\int\chi\,d\mathcal T_0>0,
\qquad
0\le\chi\le1.
\]

The fixed-filter trace recovery from the preceding theorem says

\[
\lim_{\ell\downarrow0}\lim_{j\to\infty}
\int\chi k_\ell(v_j(0);y)\,dy
=
\frac{\Delta_\chi}{2}.
\]

Choose once and for all

\[
0<\eta_{\mathrm L}<\eta_{\mathrm H}
<
\frac{b\Delta_\chi}{2}.
\]

For each \(\alpha\in\{\mathrm L,\mathrm H\}\), and all sufficiently large
\(j\), define \(r_j^\alpha\) as the first length satisfying

\[
\boxed{
\mathbf K(r_j^\alpha,t_j)=\eta_\alpha.
}
\]

Equivalently, if

\[
\ell_j^\alpha:=\frac{r_j^\alpha}{R_j},
\]

then

\[
\mathcal K_{\ell_j^\alpha}[v_j(0)]
=
\frac{\eta_\alpha}{b_j}.
\]

The local filtered energy is bounded by the global filtered energy. The
iterated trace limit and \(b_j\to b\) therefore show that every sufficiently
small fixed \(\ell>0\) crosses both levels eventually. Continuity and
monotonicity give the first crossings and imply

\[
\ell_j^\alpha\longrightarrow0.
\]

Since \(R_j\to0\), also \(r_j^\alpha\to0\).

These are fixed **physical-energy quantiles**. Unlike a normalised threshold,
their values do not change when two consecutive carriers have different
energy normalisers.

## 2. Physical flux ceiling between records

Let

\[
\Phi(r,t)
:=
\int_{\mathbb R^3}\Pi_r[u(t)]\,dx
\]

be the global signed flux through the Gaussian boundary \(r\). The physical
form of the endpoint Lorentz estimate is

\[
\boxed{
|\Phi(r,t)|
\le
\frac{C\,m(t)^3}{r}
\log\left(
e+\frac{CE_0}{m(t)^2r}
\right),
}
\]

where

\[
m(t):=\|u(t)\|_{L^{3,\infty}},
\qquad
E_0:=\|u(0)\|_2^2.
\]

The value at \(m(t)=0\) is understood by continuity.

Every \(t_j\) is a first record time. Hence

\[
m(t)\le m_{j+1}
\qquad
(0\le t\le t_{j+1}).
\]

The function

\[
L^3\log\left(e+\frac{CE_0}{L^2r}\right)
\]

is increasing for \(L>0\). Therefore, throughout
\([t_j,t_{j+1}]\),

\[
|\Phi(r,t)|\le F_j(r),
\]

where

\[
F_j(r)
:=
\frac{C\,m_{j+1}^3}{r}
\log\left(
e+\frac{CE_0}{m_{j+1}^2r}
\right).
\]

The exact global subgrid balance is

\[
\boxed{
\mathbf K(r,t_2)-\mathbf K(r,t_1)
=
\int_{t_1}^{t_2}\Phi(r,t)\,dt
-
\nu
\int_{t_1}^{t_2}\!\!\int_{\mathbb R^3}
d_r[u]\,dx\,dt,
}
\]

with \(d_r[u]\ge0\). Define the physical terminal dissipation tail

\[
D_j
:=
\nu
\int_{t_j}^{T^*}\|\nabla u(t)\|_2^2\,dt.
\]

Energy equality and absolute continuity give

\[
D_j\longrightarrow0,
\]

and

\[
\nu
\int_{t_j}^{t_{j+1}}\!\!\int d_r[u]
\le D_j
\]

for every \(r>0\).

## 3. Cross-record persistence or clock

Set

\[
\gamma:=\eta_{\mathrm H}-\eta_{\mathrm L}>0,
\qquad
F_j^{\mathrm H}:=F_j(r_j^{\mathrm H}).
\]

### Theorem 1

For every sufficiently large \(j\), at least one of the following holds:

1. **Physical quantile persistence**

   \[
   r_{j+1}^{\mathrm L}\le r_j^{\mathrm H}.
   \]

2. **Record-clock payment**

   \[
   \Delta t_j
   \ge
   \frac{3\gamma}{4F_j^{\mathrm H}}.
   \]

Moreover, whenever

\[
0\le t-t_j\le
\min\left\{
\Delta t_j,\frac{\gamma}{4F_j^{\mathrm H}}
\right\},
\]

one has

\[
\mathbf K(r_j^{\mathrm H},t)
\ge
\eta_{\mathrm H}-\frac{\gamma}{2}
>
\eta_{\mathrm L}.
\]

### Proof

Take \(j\) large enough that

\[
D_j\le\frac{\gamma}{4}.
\]

The balance and the absolute flux ceiling give

\[
\eta_{\mathrm H}
-
\mathbf K(r_j^{\mathrm H},t)
\le
F_j^{\mathrm H}(t-t_j)+D_j
\]

for \(t_j\le t\le t_{j+1}\). This proves the stated forward persistence
interval.

If the first alternative fails, then

\[
r_j^{\mathrm H}<r_{j+1}^{\mathrm L}.
\]

By the first-crossing definition at \(t_{j+1}\),

\[
\mathbf K(r_j^{\mathrm H},t_{j+1})
<
\eta_{\mathrm L}.
\]

Consequently

\[
\gamma
<
\eta_{\mathrm H}
-
\mathbf K(r_j^{\mathrm H},t_{j+1})
\le
F_j^{\mathrm H}\Delta t_j+D_j.
\]

The bound on \(D_j\) yields

\[
F_j^{\mathrm H}\Delta t_j
>
\frac{3\gamma}{4},
\]

which is the second alternative.

### What persistence means

The first alternative says that at least \(\eta_{\mathrm L}\) physical
energy remains below the old high-quantile filter at the next record. It
does not identify fluid particles, a Fourier packet, or a one-way transfer.
Oppositely directed transfers can cancel in the signed global balance. The
theorem is therefore persistence of a positive **amount**, not freshness of
a packet.

## 4. Carrier form and the new summable budget

The exact amplitude-layer bounds give

\[
c_*m_j\le a_jR_j\le m_j,
\qquad
b_j=a_j^2R_j^3,
\qquad
\tau_j=\frac{R_j}{a_j}.
\]

With

\[
q_j:=\frac{m_{j+1}}{m_j},
\qquad
\ell_j^{\mathrm H}:=\frac{r_j^{\mathrm H}}{R_j},
\]

one obtains

\[
F_j^{\mathrm H}
\le
\frac{
Cq_j^3b_j
}{
\tau_j\ell_j^{\mathrm H}
}
\log\left(
e+
\frac{CE_0}
{q_j^2b_j\ell_j^{\mathrm H}}
\right).
\]

Since \(b_j\to b>0\), the clock branch implies

\[
\boxed{
\Delta t_j
\gtrsim
\frac{
\tau_j\ell_j^{\mathrm H}
}{
q_j^3
\log\!\left(e+C/(q_j^2\ell_j^{\mathrm H})\right)
}.
}
\]

Let \(\mathcal C\) be the indices on which quantile persistence fails. The
record intervals are disjoint, so

\[
\boxed{
\sum_{j\in\mathcal C}
\frac{
\tau_j\ell_j^{\mathrm H}
}{
q_j^3
\log\!\left(e+C/(q_j^2\ell_j^{\mathrm H})\right)
}
<\infty.
}
\]

This is an actual same-trajectory clock budget. Its summability is necessary,
not contradictory.

## 5. Joint power survivor

Take the exact representative scalar powers

\[
m_j:=2^{2j},
\qquad
e_j:=b_j:=1,
\qquad
\nu:=1.
\]

Then

\[
a_j:=2^{6j},
\qquad
R_j:=2^{-4j},
\qquad
\tau_j:=2^{-10j},
\qquad
\varepsilon_j:=2^{-2j},
\]

and

\[
q_j=4.
\]

Choose

\[
\ell_j^{\mathrm H}:=2^{-j},
\qquad
r_j^{\mathrm H}
=R_j\ell_j^{\mathrm H}
=2^{-5j}.
\]

Because \(\eta_{\mathrm H}/b_j\) stays between fixed positive constants, the
backward proof of the preceding residence theorem applies uniformly at this
physical quantile. It forces only

\[
\frac{
\varepsilon_j
}{
\ell_j^{\mathrm H}
\log(e+C/\ell_j^{\mathrm H})
}
\asymp
\frac{2^{-j}}{j},
\]

whose sum is finite. The new cross-record clock scale is

\[
\frac{
\tau_j\ell_j^{\mathrm H}
}{
q_j^3
\log(e+C/(q_j^2\ell_j^{\mathrm H}))
}
\asymp
\frac{2^{-11j}}{j},
\]

also summable.

Choose

\[
\Delta t_j:=c_t\frac{2^{-11j}}{j},
\qquad
t_j:=T^*-\sum_{k\ge j}\Delta t_k,
\]

and interpolate a continuous increasing scalar history through
\(m(t_j)=m_j\). Then \(t_{j+1}-t_j=\Delta t_j\), and these are consecutive
first-record gaps.

Even if the weak-\(L^3\) size stayed at its worst allowed value
\(m_{j+1}\) throughout each gap,

\[
\sum_jm_{j+1}^4\Delta t_j
\lesssim
\sum_j\frac{2^{-3j}}{j}
<\infty.
\]

The remaining forward carrier horizon satisfies

\[
\frac{T^*-t_j}{\tau_j}
\asymp
\frac{2^{-j}}{j}
\longrightarrow0.
\]

Thus the residence law, cross-record persistence-or-clock law, finite
weak-\(L^3\) occupation, finite physical time, energy efficiency, and the
zero-clock carrier cell all coexist at the level of exact powers. One may
take

\[
r_j^{\mathrm L}:=\frac12r_j^{\mathrm H},
\qquad
r_{j+1}^{\mathrm L}
=\frac1{64}r_j^{\mathrm H}
\]

at every event, so the same positive energy amount descends an accelerating
sequence of physical filter boundaries.

This is a scalar scaling ledger. It is not a velocity field, does not solve
Navier--Stokes, and does not prove that one physical packet realizes the
linked quantiles.

## 6. Route consequence

The terminal-trace branch now has the exact cross-event partition

\[
\boxed{
\text{rapid next record}
\Longrightarrow
\text{positive physical subgrid amount persists},
}
\]

while failure of persistence pays a quantified, summable record clock.

The next closing theorem must add at least one of:

1. a non-reuse or one-way-transfer law assigning fresh energy or enstrophy
   to successive quantile crossings;
2. a nonsummable dynamical charge for traversing the gap between
   \(r_j^{\mathrm L}\) and \(r_j^{\mathrm H}\), since bounded width alone
   still permits the displayed power ledger;
3. an NSE constraint coupling the record ratio \(q_j\), the remaining horizon,
   and the quantile length;
4. a spatial recentering theorem tying the global quantile to the retained
   amplitude layer;
5. coherent-trace propagation and ancient-Euler rigidity; or
6. separate control of the divergent-normalised-energy branch.

No alternative A--D of the Clay problem is proved.
