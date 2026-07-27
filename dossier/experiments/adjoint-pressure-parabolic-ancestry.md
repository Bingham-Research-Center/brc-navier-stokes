# Parabolic tail ancestry has a sharp \(7/6\) log-scale ceiling

- **Experiment:** EXP-ADJOINT-PRESSURE-PARABOLIC-ANCESTRY-001
- **Route:** ROUTE-R3B
- **Status:** adversarially recomputed conditional same-trajectory
  theorem plus smooth kinematic countermodel
- **Review:** [valid and nonduplicative in the stated
  scope](../review-ledger.md)
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Input:** adversarially recomputed
  [parabolic coefficient-tail theorem](adjoint-pressure-parabolic-coefficient-tail.md)

The reviewed coefficient-tail theorem says more than
superparabolic LP--Dyson escape.  At every fixed parabolic multiple
\(V=\kappa h^{-1/2}\), a selected feedback pressure packet forces

\[
D_{b,>V}^{\chi}(h)
\ge c_\kappa h^{-3}.
\tag{1}
\]

After physical pullback, this is actual dissipation of the common
Navier--Stokes coefficient above

\[
\Lambda=\frac{\kappa h^{-1/2}}{\sigma}.
\tag{2}
\]

This note asks what follows if that cutoff reaches the reciprocal next
Besov-event scale.  There is a new exact consequence:

\[
\boxed{
\frac{\sigma_j^7}{\sigma_{j+1}^6}\longrightarrow0,
\qquad
\limsup_{j\to\infty}
\frac{\log(1/\sigma_{j+1})}
     {\log(1/\sigma_j)}
\le\frac76.
}
\tag{3}
\]

Thus the physical zoom cannot make an arbitrary multiplicative jump
between consecutive events once the parabolic tail is genuinely tied
to the next event.

The exponent is sharp for the information used.  For every \(q>3\),
the exact power-law genealogy

\[
\sigma_j=h_j^q,
\qquad
\sigma_{j+1}
=\frac{\sigma_j}{\kappa h_j^{-1/2}}
\tag{4}
\]

has finite physical dissipation, exact cutoff/next-event matching,
divergent empirical mean logarithmic roof, and log-scale ratio tending to
\(1+1/(2q)<7/6\).  As \(q\downarrow3\), this approaches \(7/6\).

More strongly, the survivor can be realised by one smooth
divergence-free finite-energy path with:

1. a uniform weak-\(L^3\) ceiling;
2. finite spacetime enstrophy;
3. a terminal \(L^2\) trace carrying a fixed Besov detector mark at
   every \(\sigma_j\);
4. exact parabolic-cutoff/next-event matching; and
5. every nested physical Fourier-tail payment in (1).

That path is not a Navier--Stokes solution and does not realise the
feedback pressure antecedent.  It proves that endpoint geometry,
finite dissipation, exact ancestry, and the new tail theorem's
nonnegative consequence still do not supply event-index non-reuse.
The missing input must use the equation to prevent far-finer
dissipation from paying many earlier events, or must provide a
signed/vector/flux increment.

## 1. Fixed-parabolic physical tail

Fix a smooth radial multiplier \(\chi\) equal to one on the unit ball
and zero outside the ball of radius two, and write

\[
S_\Lambda=\chi(D/\Lambda).
\tag{5}
\]

Let \(v\) be one finite-energy Leray--Hopf trajectory on
\((0,T^*)\).  In particular,

\[
\int_0^{T^*}\|\nabla v(t)\|_2^2\,dt<\infty.
\tag{6}
\]

Let selected smooth genealogy layers be physical pullbacks

\[
b_j(x,\tau)
=
\sigma_j
v(x_j+\sigma_jx,t_j-\sigma_j^2\tau),
\qquad
0<\tau<h_j,
\tag{7}
\]

where

\[
h_j\downarrow0,
\qquad
\sigma_j\downarrow0,
\qquad
I_j=(t_j-\sigma_j^2h_j,t_j).
\tag{8}
\]

Assume the fixed feedback pressure floor required by the reviewed
coefficient-tail theorem.  For one fixed \(\kappa\ge1\), that theorem
and exact physical scaling give

\[
\boxed{
\mathcal E_j
:=
\int_{I_j}
\left\|
\nabla
\left(
I-S_{\Lambda_j}
\right)v(t)
\right\|_2^2\,dt
\ge
c_\kappa\sigma_jh_j^{-3},
}
\tag{9}
\]

where

\[
\Lambda_j
:=
\frac{\kappa h_j^{-1/2}}{\sigma_j}.
\tag{10}
\]

Because \(\Lambda_j\to\infty\), Fourier dominated convergence in
\(L^2_{t,x}\) gives

\[
\int_0^{T^*}
\left\|
\nabla
\left(
I-S_{\Lambda_j}
\right)v(t)
\right\|_2^2\,dt
\longrightarrow0.
\tag{11}
\]

Consequently

\[
\boxed{
\sigma_jh_j^{-3}\longrightarrow0.
}
\tag{12}
\]

This fixed-\(\kappa\) conclusion is stronger than the
\(h^{-3+\varepsilon}\) floor at a growing logarithmic cutoff.

## 2. Conditional next-event distortion theorem

Suppose that the physical cutoff in (10) reaches the next selected
event frequency: there is one \(a_0>0\) such that

\[
\boxed{
\Lambda_j
\ge
\frac{a_0}{\sigma_{j+1}}
}
\tag{13}
\]

for all sufficiently large \(j\).  Exact identification corresponds
to \(a_0=1\).

Equation (13) is equivalent to

\[
\frac{\sigma_{j+1}}{\sigma_j}
\ge
\frac{a_0}{\kappa}h_j^{1/2}.
\tag{14}
\]

Therefore

\[
h_j^{-3}
\ge
\left(\frac{a_0}{\kappa}\right)^6
\left(\frac{\sigma_j}{\sigma_{j+1}}\right)^6.
\tag{15}
\]

Multiplying by \(\sigma_j\) and using (12) proves

\[
\boxed{
\frac{\sigma_j^7}{\sigma_{j+1}^6}
\longrightarrow0.
}
\tag{16}
\]

Put

\[
x_j:=\log\frac1{\sigma_j}.
\tag{17}
\]

Taking logarithms in (16) gives

\[
6x_{j+1}-7x_j\longrightarrow-\infty.
\tag{18}
\]

In particular, eventually \(x_{j+1}<7x_j/6\), and hence

\[
\boxed{
\limsup_{j\to\infty}\frac{x_{j+1}}{x_j}
\le\frac76.
}
\tag{19}
\]

This is a conditional theorem on the common physical trajectory.  It
does not prove (13).  It states the exact reward for proving it.

### General exponent ledger

The number \(7/6\) is not accidental.  If a physical tail has size
\(\sigma h^{-a}\), its normalised cutoff is \(h^{-b}\), and that
cutoff reaches the next event, the same argument yields

\[
\frac{\sigma_j^{1+a/b}}
     {\sigma_{j+1}^{a/b}}
\longrightarrow0,
\qquad
\limsup\frac{x_{j+1}}{x_j}
\le1+\frac{b}{a}.
\tag{20}
\]

Here \(a=3\) and \(b=1/2\).

## 3. Sharp power-law survivor

Fix

\[
q>3,
\qquad
\kappa\ge1,
\qquad
0<h_1<1,
\tag{21}
\]

and define recursively

\[
\boxed{
h_{j+1}
=
\kappa^{-1/q}
h_j^{\,1+1/(2q)}.
}
\tag{22}
\]

Set

\[
\begin{aligned}
\sigma_j&:=h_j^q,\\
V_j&:=\kappa h_j^{-1/2},\\
\Lambda_j&:=V_j/\sigma_j,\\
\delta_j&:=\sigma_j^2h_j,\\
\tau_j&:=\sigma_jh_j^{-3}=h_j^{q-3}.
\end{aligned}
\tag{23}
\]

Equation (22) gives the exact ancestry identities

\[
\boxed{
\sigma_{j+1}
=
\frac{\sigma_j}{V_j},
\qquad
\Lambda_j
=
\frac1{\sigma_{j+1}}.
}
\tag{24}
\]

Since \(q>3\),

\[
\tau_j\downarrow0,
\qquad
\sum_{j\ge1}(\tau_j-\tau_{j+1})=\tau_1<\infty.
\tag{25}
\]

Moreover,

\[
\boxed{
\frac{\sigma_j^7}{\sigma_{j+1}^6}
=
\kappa^6\tau_j
\longrightarrow0.
}
\tag{26}
\]

For \(\kappa=1\), the log-scale ratio is exactly

\[
\frac{x_{j+1}}{x_j}
=
1+\frac1{2q}
<
\frac76.
\tag{27}
\]

For general fixed \(\kappa\), it tends to the same value.  Letting
\(q\downarrow3\) proves sharpness of (19) among power-law survivors.

The logarithmic roof

\[
\ell_j:=x_{j+1}-x_j
\tag{28}
\]

is not integrable in event index.  Indeed,

\[
x_{j+1}
=
\left(1+\frac1{2q}\right)x_j+\log\kappa,
\tag{29}
\]

so \(x_j\) and \(\ell_j\) grow geometrically and

\[
\frac{x_n-x_1}{n-1}\longrightarrow\infty.
\tag{30}
\]

Thus the \(7/6\) ceiling does not force a finite empirical roof mean.
This is the \(r=\infty\) compactified roof boundary; the survivor does
not construct a stationary probability law with an infinite-mean roof.

## 4. A smooth kinematic realisation with terminal events

The scalar survivor can be strengthened.  Start sufficiently far down
(22) that

\[
\frac{\sigma_{j+1}}{\sigma_j}\le\frac14
\tag{31}
\]

for every \(j\).

### 4.1 Terminal Besov-event tower

Choose a nonzero

\[
G\in C^\infty_{c,\sigma}(\mathbb R^3;\mathbb R^3),
\qquad
\operatorname{supp}G
\subset\{1<|x|<2\},
\tag{32}
\]

and put

\[
G_j(x):=\sigma_j^{-1}G(x/\sigma_j),
\qquad
g:=\sum_{j\ge1}G_j.
\tag{33}
\]

The spatial supports are disjoint by (31).  Critical scaling and the
geometric support volumes give

\[
g\in L^2(\mathbb R^3)\cap L^{3,\infty}(\mathbb R^3),
\tag{34}
\]

because

\[
\sum_j\|G_j\|_2^2
=
\|G\|_2^2\sum_j\sigma_j<\infty
\tag{35}
\]

and

\[
\left|
\left\{
|g|>\lambda
\right\}
\right|
\lesssim\lambda^{-3}.
\tag{36}
\]

Let

\[
(\mathscr S_\sigma f)(x):=\sigma f(\sigma x)
\tag{37}
\]

and choose the fixed solenoidal detector \(\varphi=G\).  At scale
\(\sigma_j\), every coarser packet lies outside the support of
\(\varphi\), every finer packet lies inside its central hole, and the
\(j\)-th packet becomes exactly \(G\).  Hence

\[
\boxed{
\left\langle
\mathscr S_{\sigma_j}g,\varphi
\right\rangle
=
\|G\|_2^2
=:c_0>0
}
\tag{38}
\]

for every \(j\).  This is an exact terminal Besov regeneration
sequence.

### 4.2 Smooth approach to the terminal tower

Use reverse terminal time \(s>0\).  Choose
\(\alpha\in C^\infty([0,\infty))\) with

\[
0\le\alpha\le1,
\qquad
\alpha=1\ \hbox{on }[0,1],
\qquad
\alpha=0\ \hbox{on }[2,\infty),
\tag{39}
\]

and define

\[
B(s,x)
:=
\sum_{j\ge1}
\alpha(s/\sigma_j^2)G_j(x).
\tag{40}
\]

For every \(s>0\), this is a finite sum of smooth solenoidal fields.
The same distribution-function argument as in (36) gives

\[
\sup_{s>0}\|B(s)\|_{L^{3,\infty}}<\infty.
\tag{41}
\]

Also,

\[
\sup_{s>0}\|B(s)\|_2<\infty,
\qquad
B(s)\longrightarrow g
\quad\hbox{strongly in }L^2
\quad(s\downarrow0),
\tag{42}
\]

and

\[
\begin{aligned}
\int_0^{\delta_1}
\|\nabla B(s)\|_2^2\,ds
&\le
C_G
\sum_j
\sigma_j^{-1}\min\{\delta_1,2\sigma_j^2\}\\
&<\infty.
\end{aligned}
\tag{43}
\]

Thus the event tower itself has a smooth finite-dissipation approach.

### 4.3 Add all nested parabolic tail payments

For the physical cutoff in (23), define the baseline tail

\[
\mathcal B_j
:=
\int_0^{\delta_j}
\left\|
\nabla(I-S_{\Lambda_j})B(s)
\right\|_2^2\,ds.
\tag{44}
\]

By (43), \(\delta_j\downarrow0\), and absolute continuity,

\[
\mathcal B_j\longrightarrow0.
\tag{45}
\]

Put

\[
\overline{\mathcal B}_j
:=
\sup_{k\ge j}\mathcal B_k,
\qquad
M_j:=4(\overline{\mathcal B}_j+\tau_j).
\tag{46}
\]

Then \(M_j\downarrow0\).  Let

\[
m_j:=M_j-M_{j+1}\ge0
\tag{47}
\]

and

\[
A_j:=(\delta_{j+1},\delta_j).
\tag{48}
\]

Choose a real solenoidal Schwartz field \(W\) with

\[
\operatorname{supp}\widehat W
\subset\{3\le|\xi|\le4\},
\qquad
\|\nabla W\|_2=1,
\tag{49}
\]

and scale it by

\[
W_K(x):=K^{1/2}W(Kx).
\tag{50}
\]

Then

\[
\|\nabla W_K\|_2=1,
\qquad
\|W_K\|_{L^{3,\infty}}
=
K^{-1/2}\|W\|_{L^{3,\infty}},
\qquad
\|W_K\|_2=K^{-1}\|W\|_2.
\tag{51}
\]

For each \(m_j>0\), choose
\(\eta_j\in C_c^\infty(A_j)\) such that

\[
\int_{A_j}\eta_j(s)^2\,ds=1
\tag{52}
\]

and choose \(K_j\) so large that

\[
\begin{aligned}
K_j&\ge\Lambda_j,\\
\sqrt{m_j}\|\eta_j\|_\infty
\|W_{K_j}\|_{L^{3,\infty}}&\le1,\\
\sqrt{m_j}\|\eta_j\|_\infty
\|W_{K_j}\|_2&\le2^{-j}.
\end{aligned}
\tag{53}
\]

There is no obstruction to (53), because the last two norms in (51)
vanish as \(K_j\to\infty\).  Define

\[
H(s,x)
:=
\sum_{j:m_j>0}
\sqrt{m_j}\eta_j(s)W_{K_j}(x).
\tag{54}
\]

The time supports are disjoint.  Therefore \(H\) is smooth for every
\(s>0\),

\[
\sup_{s>0}\|H(s)\|_{L^{3,\infty}}\le1,
\qquad
H(s)\longrightarrow0
\quad\hbox{strongly in }L^2
\quad(s\downarrow0),
\tag{55}
\]

and

\[
\int_0^{\delta_1}\|\nabla H(s)\|_2^2\,ds
=
\sum_jm_j
=M_1<\infty.
\tag{56}
\]

For \(k\ge j\), the Fourier support of \(W_{K_k}\) lies beyond
\(2\Lambda_j\).  Consequently

\[
\boxed{
\int_0^{\delta_j}
\left\|
\nabla(I-S_{\Lambda_j})H(s)
\right\|_2^2\,ds
=
\sum_{k\ge j}m_k
=M_j.
}
\tag{57}
\]

Finally put

\[
v_{\rm kin}:=B+H.
\tag{58}
\]

The Lorentz quasi-triangle inequality, (41), and (55) give a uniform
weak-\(L^3\) ceiling.  Equations (43) and (56) give finite total
spacetime enstrophy, and

\[
v_{\rm kin}(s)\longrightarrow g
\quad\hbox{strongly in }L^2
\quad(s\downarrow0).
\tag{59}
\]

For vectors \(X,Y\) in a Hilbert space,

\[
\|X+Y\|^2
\ge\frac12\|Y\|^2-\|X\|^2.
\tag{60}
\]

Apply (60) to the high-pass gradients of \(B\) and \(H\), integrate
over \((0,\delta_j)\), and use (44), (46), and (57):

\[
\begin{aligned}
\int_0^{\delta_j}
\left\|
\nabla(I-S_{\Lambda_j})v_{\rm kin}(s)
\right\|_2^2\,ds
&\ge
\frac12M_j-\mathcal B_j\\
&\ge
2(\overline{\mathcal B}_j+\tau_j)-\mathcal B_j\\
&\ge
\tau_j.
\end{aligned}
\tag{61}
\]

By (23)--(24), this is exactly

\[
\boxed{
\int_0^{\delta_j}
\left\|
\nabla
\left(
I-S_{1/\sigma_{j+1}}
\right)
v_{\rm kin}(s)
\right\|_2^2\,ds
\ge
\sigma_jh_j^{-3}.
}
\tag{62}
\]

Thus one smooth kinematic path carries the terminal events and all the
new physical tail payments with exact next-event matching.

## 5. What is proved and what survives

The conditional same-trajectory theorem (16)--(19) is genuine new
control: if the fixed-parabolic tail reaches the next event, a
consecutive event jump larger than the \(7/6\) log-scale ceiling is
impossible.

The smooth construction proves that the following package is still
compatible:

1. finite kinetic energy;
2. finite physical spacetime enstrophy;
3. a uniform weak-\(L^3\) ceiling;
4. strong \(L^2\) terminal convergence;
5. infinitely many fixed terminal Besov marks;
6. nested terminal event intervals;
7. the full fixed-parabolic inverse-cubic tail payment;
8. exact identification of that cutoff with the next event frequency;
9. global physical Fourier-tail continuity; and
10. a divergent empirical mean event roof.

The construction exploits one precise freedom: the mass required only
to lie **above** \(1/\sigma_{j+1}\) is placed at much finer frequencies
\(K_j\).  Those finer packets are then counted in every earlier nested
tail.  A nonnegative high-pass lower bound cannot distinguish this
reuse.

The construction does **not**:

- solve the Navier--Stokes equation;
- realise the selected feedback pressure floor;
- satisfy a local energy inequality derived from that equation;
- construct a stationary event law or identify the packet tower with
  the inherited Albritton--Barker event process;
- identify the far-finer \(K_j\) packets with actual event states;
- construct a singularity; or
- establish regularity, breakdown, or any Clay alternative A--D.

The exact next theorem must therefore add at least one of:

1. a PDE upper localisation showing that the forced mass lies in a
   comparable annulus, not arbitrarily far above \(\Lambda_j\);
2. a frequency-flux identity whose signed fresh increments telescope;
3. a cascade-speed bound preventing \(K_j/\Lambda_j\to\infty\) on the
   shrinking event interval; or
4. an event detector theorem forcing far-finer tail mass to generate
   an intervening Besov event.

Bare next-scale identification is now closed as a route to
contradiction.

The subsequent adversarially recomputed
[parabolic tail-to-flux theorem](adjoint-pressure-parabolic-flux.md)
now extracts the exact NSE consequence absent from this kinematic path.
At every farther factor, the actual trajectory must pay in a comparable
annulus, inherit enough high-frequency entrance energy, or receive
positive signed nonlinear input.  An exact conservative shell ledger
and Zeno heat-clock schedule show that the last input is cumulative and
need not be fresh under the ordinary high-pass balances alone.  At that
stage the remaining theorem had to quantify flux decrement, frequency
locality, non-Zeno cascade speed, inherited-state ancestry, or
event-index telescoping.

The subsequent adversarially recomputed
terminal signed-flux ancestry theorem
now resolves the inherited-state bookkeeping alternative.  A
fixed-time \(H^1\) tail and last hitting force pre-event cumulative
flux, while an event-adaptive sharp-annulus squeeze gives
\[
\frac{K_j}{\Lambda_j}\to1,
\qquad
\Phi_{K_j}(J_j)\ge\frac{\nu T_j}{4}
\]
on terminal intervals for every sufficiently late event.  What
remains is event-index freshness of that forced flux, not its
existence.

The subsequent adversarially recomputed
[weak-\(L^3\) lower-band decrement theorem](adjoint-pressure-flux-decrement.md)
then closes the near-lossless shell-ledger alternative.  Every late
charged boundary pays a fixed fraction of its signed input in a lower
frequency band.  It does not yet make those bands or intervals fresh
across event indices, and therefore leaves bounded overlap, a
scale-zero floor, non-Zeno speed, an intervening event, or a
cross-event telescope as the live gate.

## 6. Executable ledger

The exact ancestry identity, inverse-cubic tail, \(7/6\) exponent,
infinite-mean roof, annular tail telescope, and weak-\(L^3\) carrier
frequency are checked by

```bash
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_parabolic_ancestry -v
PYTHONPATH=lab python -m \
  navier_lab.adjoint_pressure_parabolic_ancestry
```
