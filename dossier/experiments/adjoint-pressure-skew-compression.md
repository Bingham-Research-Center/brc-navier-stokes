# Skew Oseen compression does not by itself sum critical pressure depth

- **Experiment:** EXP-ADJOINT-PRESSURE-SKEW-COMPRESSION-001
- **Route:** ROUTE-R3B
- **Status:** adversarially recomputed proof-level structural theorem,
  including the strong-zero-trace refinement
- **Domain:** \(\mathbb R^3\) for the PDE identities; finite-dimensional
  Hilbert space for the countermodel
- **Clay status:** unsolved
- **Input:** the adversarially recomputed
  [critical Oseen--Volterra audit](adjoint-pressure-critical-volterra.md)

The scalar Volterra audit showed that critical causality alone need not
decay with interaction depth.  This note restores the first structures
erased by that scalar model: the Leray projection, the orthogonal pressure
component, and the skewness of divergence-free transport.

The outcome is exact but negative.  For a divergence-free drift \(b\), the
selected pressure operator is precisely the gradient component discarded
by the projected Oseen drift:

\[
\mathcal T(z,b)
=
(I-\mathbb P)(b\cdot\nabla z).
\]

The projected part is skew in \(L^2\), but skewness is not a pressure
telescope.  An exact three-dimensional skew block, combined with the
critical Hardy--Volterra time operator, has a feedback residual whose
pressure stays of fixed size after every finite interaction truncation.
A monomial refinement takes \(r(t)=t e_1\), so the same nondecay occurs
with a genuine linear zero right trace.  The model is uniformly
energy-stable for every real coupling parameter.

Even replacing the skew generator by one unitary transport step gives only
a **squared** projection-defect telescope.  In an exact small-step family,
the squared leakage tends to zero while the sum of absolute leakages tends
to two.  This is the precise mismatch with the required
\(L^1_tL^1_x\) adjoint-pressure cost.

This is not an Oseen or Navier--Stokes counterexample.  It closes only the
shortcut based on abstract skewness, orthogonal Hodge splitting, real
coupling stability, a prescribed algebraic zero-trace order, or a generic
projection-energy defect.  A successful infinite-depth argument must use
structure not present in the model: componentwise spatial transport tied
to heat, the Navier--Stokes evolution of the same coefficient, a
non-reusable signed ancestry law, or an equivalent quantitative input.

## 1. Exact Leray and pressure identities

Let

\[
P:=\mathbb P,
\qquad
Q:=I-P
\tag{1}
\]

be the orthogonal Leray and gradient projections on vector \(L^2\).
For a smooth divergence-free drift \(b\), define

\[
B_bz:=b\cdot\nabla z.
\tag{2}
\]

On smooth decaying vector fields,

\[
B_b^*=-B_b.
\tag{3}
\]

If \(b\) and \(z\) are both divergence free, then

\[
\begin{aligned}
\operatorname{div}(b\cdot\nabla z)
&=
\partial_i b_k\,\partial_k z_i,\\
\operatorname{div}(z\cdot\nabla b)
&=
\partial_i z_k\,\partial_k b_i.
\end{aligned}
\tag{4}
\]

Interchanging the dummy indices \(i\) and \(k\) in the second scalar
shows that the right sides agree.  Therefore

\[
\boxed{
Q(b\cdot\nabla z)
=
Q(z\cdot\nabla b)
=
\mathcal T(z,b)
=
\mathcal T(b,z).
}
\tag{5}
\]

Thus the tensor orientation in the reviewed pressure operator is not a
second unrelated interaction: it is exactly the gradient part of the
transport interaction used by the Oseen equation.

On the solenoidal Hilbert space \(PH\), set

\[
A_b:=PB_bP,
\qquad
C_b:=QB_bP.
\tag{6}
\]

Then

\[
\boxed{
A_b^*=-A_b,
\qquad
C_b=[Q,B_b]P,
\qquad
B_bz=A_bz+C_bz
\quad(z\in PH).
}
\tag{7}
\]

In particular,

\[
\boxed{
\|B_bz\|_2^2
=
\|A_bz\|_2^2+\|C_bz\|_2^2.
}
\tag{8}
\]

The second-order compression identity is

\[
\boxed{
PB_b^2P
=
A_b^2-C_b^*C_b,
}
\tag{9}
\]

or equivalently

\[
\boxed{
-PB_b^2P
=
A_b^*A_b+C_b^*C_b.
}
\tag{10}
\]

Indeed,

\[
\begin{aligned}
PB_b^2P
&=
PB_b(P+Q)B_bP\\
&=
A_b^2+PB_bQB_bP,
\end{aligned}
\]

while

\[
C_b^*
=
PB_b^*Q
=
-PB_bQ.
\]

Equations (8)--(10) are positive identities, but their right side is
weighted by \(B_b^*B_b\).  It is not
\(\|z\|_2^2-\|A_bz\|_2^2\), so it does not telescope over powers of
\(A_b\).

There is also an exact nonlinear interpretation.  Define the
pressure-gradient map

\[
\boldsymbol\Pi(v):=Q(v\cdot\nabla v).
\tag{11}
\]

Its Fréchet derivative at a divergence-free \(b\) in a divergence-free
direction \(z\) is

\[
\boxed{
D\boldsymbol\Pi(b)[z]
=
Q(z\cdot\nabla b+b\cdot\nabla z)
=
2C_bz.
}
\tag{12}
\]

Hence the adjoint pressure is one half of the linearised nonlinear
pressure gradient.  The selected adjoint \(z\), however, is not a primal
tangent solution, so (12) is not by itself a trajectory telescope.

## 2. Exact critical skew-compression countermodel

Let

\[
H=\mathbb R^3,
\qquad
P=\operatorname{diag}(1,1,0),
\qquad
Q=I-P,
\tag{13}
\]

and take the skew matrix

\[
\boxed{
B=
\begin{pmatrix}
0&-1&-1\\
1&0&-1\\
1&1&0
\end{pmatrix}.
}
\tag{14}
\]

Then \(B^*=-B\).  Relative to \(PH\cong\mathbb R^2\),

\[
\boxed{
A:=PBP
=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix},
\qquad
C:=QBP
=
\begin{pmatrix}
1&1
\end{pmatrix}.
}
\tag{15}
\]

Thus \(A\) is the quarter-turn and

\[
A^me_1
\in
\{e_1,e_2,-e_1,-e_2\}.
\tag{16}
\]

The pressure observation obeys

\[
\boxed{
|CA^me_1|=1
\qquad(m\ge0).
}
\tag{17}
\]

This does not contradict (8): applying the full generator \(B\) is not a
unitary **step**, even though the flow \(e^{sB}\) is unitary.

Now restore critical causal time.  For \(0<\gamma<1\), let

\[
(\mathsf H_\gamma f)(t)
:=
\frac1{B(\gamma,1-\gamma)}
\int_0^t
(t-s)^{\gamma-1}s^{-\gamma}f(s)\,ds.
\tag{18}
\]

On constant functions,

\[
\mathsf H_\gamma 1=1.
\tag{19}
\]

On \(L^\infty(0,T;\mathbb R^2)\), define

\[
\mathbb T:=\mathsf H_\gamma\otimes A,
\qquad
\mathbb C:=I\otimes C.
\tag{20}
\]

Take the constant source and feedback fields

\[
q:=-(e_1+e_2),
\qquad
r:=e_1.
\tag{21}
\]

Since

\[
A(q+r)
=
A(-e_2)
=
e_1,
\tag{22}
\]

equations (19)--(22) give the exact weak-endpoint feedback relation with no
initial term

\[
\boxed{
r=\mathbb T(q+r).
}
\tag{23}
\]

Iterating (23) \(N\) times yields

\[
\boxed{
r
=
\sum_{m=1}^{N}\mathbb T^mq
+\mathbb T^Nr.
}
\tag{24}
\]

The exact remainder after the first \(N\) interactions is therefore

\[
R_{N+1}:=\mathbb T^Nr=A^Ne_1,
\tag{25}
\]

and its pressure observation satisfies

\[
\boxed{
|\mathbb C R_{N+1}(t)|
=
1
\qquad
(t\in(0,T),\ N\ge0).
}
\tag{26}
\]

Thus critical causal ordering, orthogonal Hodge splitting, and a skew full
generator can coexist with a pressure floor at every interaction depth.
The model is posed at the weak critical endpoint in \(L^\infty(0,T)\):
the value of \(r\) at \(t=0\) may be assigned to be zero, but \(r\) has no
strong zero right trace.  The next refinement shows that this trace defect
is not essential to the abstract obstruction.

### A linear strong zero right trace still need not decay

For every \(\eta\ge0\), the exact beta identity gives

\[
\mathsf H_\gamma(t^\eta)
=
\mu_{\gamma,\eta}t^\eta,
\qquad
\mu_{\gamma,\eta}
:=
\frac{B(\gamma,1-\gamma+\eta)}
     {B(\gamma,1-\gamma)}
>0.
\tag{26a}
\]

Let

\[
J:=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix},
\qquad
A_{\gamma,\eta}:=\mu_{\gamma,\eta}^{-1}J,
\qquad
C:=
\begin{pmatrix}
1&1
\end{pmatrix}.
\tag{26b}
\]

These are again the \(PBP\) and \(QBP\) blocks of the skew matrix

\[
B_{\gamma,\eta}
:=
\begin{pmatrix}
0&-\mu_{\gamma,\eta}^{-1}&-1\\
\mu_{\gamma,\eta}^{-1}&0&-1\\
1&1&0
\end{pmatrix}.
\tag{26c}
\]

Define

\[
\mathbb T_{\gamma,\eta}
:=
\mathsf H_\gamma\otimes A_{\gamma,\eta},
\qquad
q_\eta(t):=-t^\eta(e_1+e_2),
\qquad
r_\eta(t):=t^\eta e_1.
\tag{26d}
\]

Because \(J(-e_2)=e_1\), equations (26a)--(26d) give

\[
\boxed{
r_\eta
=
\mathbb T_{\gamma,\eta}(q_\eta+r_\eta).
}
\tag{26e}
\]

Moreover,

\[
\boxed{
\mathbb T_{\gamma,\eta}^{\,N}r_\eta(t)
=
t^\eta J^Ne_1,
\qquad
\left|
C\mathbb T_{\gamma,\eta}^{\,N}r_\eta(t)
\right|
=
t^\eta
\quad(N\ge0).
}
\tag{26f}
\]

The case \(\eta=0\) is the constant mode above.  For the linearly
vanishing mode \(\eta=1\),

\[
\mu_{\gamma,1}=1-\gamma,
\qquad
r_1(0)=q_1(0)=0,
\tag{26g}
\]

and both fields have a strong zero right trace.  Nevertheless,

\[
\boxed{
\int_0^T
\left|
C\mathbb T_{\gamma,1}^{\,N}r_1(t)
\right|\,dt
=
\frac{T^2}{2}
\qquad(N\ge0).
}
\tag{26h}
\]

Thus neither a strong zero right trace nor any fixed algebraic vanishing
order forces depth decay in the abstract critical skew/Hodge model.  What
remains available to the actual Oseen problem is not trace alone, but its
quantitative linkage to the spatial heat operator and to the same
Navier--Stokes coefficient.

## 3. Real coupling stability still does not control Dyson depth

Introduce a real coupling parameter:

\[
r_\lambda
=
\lambda\mathbb T(q+r_\lambda).
\tag{27}
\]

On the constant subspace this is

\[
(I-\lambda A)r_\lambda
=
\lambda Aq.
\tag{28}
\]

Since

\[
(I-\lambda A)^{-1}
=
\frac1{1+\lambda^2}
\begin{pmatrix}
1&-\lambda\\
\lambda&1
\end{pmatrix},
\tag{29}
\]

one obtains

\[
\boxed{
r_\lambda
=
\frac{\lambda}{1+\lambda^2}
\begin{pmatrix}
1+\lambda\\
\lambda-1
\end{pmatrix},
\qquad
\|r_\lambda\|^2
=
\frac{2\lambda^2}{1+\lambda^2}
\le2
\quad(\lambda\in\mathbb R).
}
\tag{30}
\]

In particular \(r_1=e_1\).  The real coupling family is uniformly
energy-stable, while its Taylor coefficients at zero are the nondecaying
rotations \(A^mq\).  The nearest complex resolvent poles are
\(\lambda=\pm i\), so real-axis stability gives no decay of the Dyson
coefficients at \(\lambda=1\).

This closes the proposed real-coupling shortcut.  A useful complex
coupling theorem would need enough uniform complex control to estimate the
expansion at \(\lambda=1\); real-axis energy alone supplies no such
coefficient estimate.

## 4. A unitary step telescopes only squared leakage

There is a positive identity for a genuinely unitary one-step transport.
Let \(U\) be unitary and put

\[
A_U:=PUP,
\qquad
C_U:=QUP
\tag{31}
\]

on \(PH\).  Then

\[
\boxed{
A_U^*A_U+C_U^*C_U=I_{PH}.
}
\tag{32}
\]

Consequently,

\[
\boxed{
\sum_{m=0}^{N}
\|C_UA_U^mx\|^2
=
\|x\|^2-\|A_U^{N+1}x\|^2
\le\|x\|^2.
}
\tag{33}
\]

This is the tempting projection-defect telescope.  It has the wrong
summability index for the adjoint-pressure cost, and it degenerates in
the continuous-step limit.

For an exact example, let \(P\) project \(\mathbb R^2\) onto
\(\mathbb Re_1\).  For an integer \(n\ge1\), set

\[
c_n:=\frac{n^2-1}{n^2+1},
\qquad
s_n:=\frac{2n}{n^2+1},
\qquad
U_n:=
\begin{pmatrix}
c_n&-s_n\\
s_n&c_n
\end{pmatrix}.
\tag{34}
\]

Because \(c_n^2+s_n^2=1\), \(U_n\) is exactly orthogonal.  Its compressed
and discarded parts on \(\mathbb Re_1\) are multiplication by \(c_n\)
and \(s_n\).  Across \(n\) steps,

\[
\begin{aligned}
L_n
&:=
\sum_{m=0}^{n-1}
|s_nc_n^m|
=
n(1-c_n^n),\\
E_n
&:=
\sum_{m=0}^{n-1}
|s_nc_n^m|^2
=
1-c_n^{2n}.
\end{aligned}
\tag{35}
\]

Since

\[
c_n=1-\frac{2}{n^2+1},
\tag{36}
\]

the elementary logarithmic expansion gives

\[
\boxed{
L_n\longrightarrow2,
\qquad
E_n\longrightarrow0.
}
\tag{37}
\]

The time step is of order \(n^{-1}\), the discarded amplitude per step is
of order \(n^{-1}\), and there are \(n\) steps.  The absolute pressure
impulse survives, while the squared energy loss is only of order
\(n^{-1}\).  Thus even the exact unitary telescope (33) cannot control a
linear \(L^1\) pressure cost without another transversality, sign, or
integrability input.

More exactly, the rotation angle is

\[
\vartheta_n=2\arctan(1/n),
\tag{38}
\]

and

\[
s_nc_n^m
=
\int_0^{\vartheta_n}
\cos(s)c_n^m\,ds.
\tag{39}
\]

Thus each term of \(L_n\) is already the generator leakage integrated
over its one-step time interval.  No additional time-step factor is
missing from the comparison with a time-\(L^1\) pressure impulse.

## 5. Same-trajectory structure that remains available

The countermodel deliberately does not encode the Navier--Stokes equation
for the drift.  That omission identifies the remaining live structure.
For a reversed smooth Navier--Stokes coefficient and its forward adjoint,
write

\[
\partial_\tau b+\nu\Delta b-b\cdot\nabla b+\nabla p_b=0,
\tag{40}
\]

\[
\partial_\tau a-\nu\Delta a-b\cdot\nabla a+\nabla\pi_a=0.
\tag{41}
\]

A direct calculation gives the local bilinear conservation law

\[
\boxed{
\partial_\tau(a\cdot b)
=
\operatorname{div}
\left[
b(a\cdot b)
+\nu\sum_{j=1}^3
\left(b_j\nabla a_j-a_j\nabla b_j\right)
-\pi_a b-p_ba
\right].
}
\tag{42}
\]

For decaying fields, its spatial integral is the reviewed conserved
primal--adjoint pairing.  Equation (42) is signed.  Its pressure flux is
\(\pi_ab\), not the unweighted quantity
\(\|\nabla\pi_a\|_{L^1}\), so no lower bound for the latter follows from
the conservation law alone.

The remaining causal gate is therefore narrower than before:

1. derive a parabolic trace--heat, spatial-commutator, or
   frequency-normalised colligation estimate that uses the actual spatial
   Oseen operator, rather than trace order alone, to couple \(A_b\),
   \(C_b\), and heat strongly enough to sum **linear** pressure leakage;
2. use (12) or (42), together with the same Navier--Stokes trajectory, to
   make the signed event pressure non-reusable on nested histories; or
3. connect the interaction remainder to the next physical Besov event by
   a genuine ancestry law.

Abstract skewness, Hodge orthogonality, real coupling energy, any fixed
algebraic zero-trace order, and a squared projection-defect telescope are
now excluded as sufficient inputs.

The later adversarially recomputed
[spatial cutoff-flux audit](adjoint-pressure-spatial-pairing.md) tests
(42) directly.  Reciprocal amplitudes of an exact periodic Beltrami NSE
field make its displayed-gauge current vanish pointwise and make every
gauge-invariant cutoff flux vanish, while the adjoint-pressure history
remains positive.  Thus the unseparated signed current in (42) is also
closed as a coercive event charge.

## Verdict

This theorem closes one precise ROUTE-R3B shortcut:

> Solenoidal projection and the skew \(L^2\) Oseen drift do not, by
> themselves, improve the critical scalar Volterra interaction depth.
> Even an exact unitary-step defect identity controls the wrong
> summability index for the global \(L^1\) adjoint-pressure functional.

It does **not** prove that the actual heat-normalised Oseen operator has the
countermodel's persistent mode.  It does not exclude the selected feedback
branch, prove regularity, or establish any Clay alternative A--D.

## Reproduce

```bash
make adjoint-pressure-skew-compression
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_skew_compression -v
make check
```
