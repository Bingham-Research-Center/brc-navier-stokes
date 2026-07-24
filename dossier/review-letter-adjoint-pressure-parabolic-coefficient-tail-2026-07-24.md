# Independent review request: parabolic coefficient-tail theorem

**Date:** 2026-07-24

**Primary candidate:**
[`experiments/adjoint-pressure-parabolic-coefficient-tail.md`](experiments/adjoint-pressure-parabolic-coefficient-tail.md)

**Route:** ROUTE-R3B

**Clay status:** unsolved

## Requested disposition

Please classify the candidate as:

1. valid in its stated smooth-layer conditional scope;
2. repairable, with exact required repairs; or
3. invalid, identifying the first fatal implication.

The intended new conclusion is not regularity.  It is the conversion of
a fixed zero-data feedback pressure packet into a genuine
frequency-localised tail of the same smooth Navier--Stokes coefficient:

\[
\int_0^h
\|\nabla(I-S_{\kappa h^{-1/2}})b\|_2^2\,dt
\gtrsim_\kappa h^{-3},
\]

and, with a slowly growing cutoff,

\[
\int_0^h
\left\|
\nabla
\left(
I-S_{c_\varepsilon h^{-1/2}\sqrt{\log(1/h)}}
\right)b
\right\|_2^2\,dt
\gtrsim_\varepsilon h^{-3+\varepsilon}.
\]

## Points requiring adversarial verification

### 1. Low-coefficient resolvent

For

\[
c=S_Vb,\qquad V=\kappa h^{-1/2},
\]

check:

- Lorentz--Bernstein
  \(\|c\|_\infty\lesssim MV\);
- the \(Z_h=L^1_tL^{3/2,1}_x\) Volterra iterate
  \[
  \|T_c^mz\|_{Z_h}
  \lesssim
  \frac{(CMV\sqrt h)^m}{\Gamma(m/2+1)}
  \|z\|_{Z_h};
  \]
- the resolvent growth \(O(e^{A\kappa^2})\); and
- the complete auxiliary feedback pressure bound
  \[
  \|\mathscr P_{S,c}r_c\|_{L^1_{t,x}}
  \lesssim e^{A\kappa^2}h^{7/4}.
  \]

In particular, check that no convergence of the auxiliary coefficient
to a Navier--Stokes solution is being assumed or needed.

### 2. Exact last-high-coefficient identity

With

\[
d=(I-S_V)b,
\qquad
\delta q=q_b-q_c,
\qquad
\delta r=r_b-r_c,
\]

check the exact identities

\[
\delta q=T_d\varphi,
\]

\[
\delta r
=(I-T_c)^{-1}
\left[
T_c\delta q+T_d(q_b+r_b)
\right],
\]

\[
\mathscr P_{S,b}r_b-\mathscr P_{S,c}r_c
=
\mathscr P_{S,c}\delta r+\mathscr P_{S,d}r_b.
\]

The intended chronology is that the displayed \(d\)-factor is the last
high-coefficient occurrence and all later interactions use \(c\).

### 3. Endpoint Lorentz and time powers

Please recompute:

\[
\|\delta q\|_{Z_h}
\lesssim hE_d(h)^{1/2},
\]

\[
\|T_d(q_b+r_b)\|_{Z_h}
\lesssim h^{3/2}E_d(h)^{1/2},
\]

where

\[
E_d(h)=\int_0^h\|d(t)\|_2^2\,dt.
\]

The products use

\[
L^{6,2}\cdot L^2\longrightarrow L^{3/2,1},
\]

the Stokes kernel contributes a half-order time integral, and the
reviewed energy estimate supplies

\[
\int_0^h
\|\nabla(q_b+r_b)\|_2^2\,dt
\lesssim h^2.
\]

Check especially that there is no hidden \(L^\infty_t\dot H^1_x\)
assumption and no failed endpoint convolution.

### 4. Pressure comparison

Verify that the fixed low-output pressure multiplier has an integrable
tensor kernel of norm \(O(S)\), and that

\[
\|\mathscr P_{S,b}r_b-\mathscr P_{S,c}r_c\|_{L^1_{t,x}}
\lesssim
e^{A\kappa^2}h^{3/2}
\left(
\int_0^h\|\nabla d\|_2^2\,dt
\right)^{1/2}.
\]

The cancellation of the apparent factor \(\kappa\) uses

\[
\|d\|_2\le V^{-1}\|\nabla d\|_2,
\qquad
V=\kappa h^{-1/2}.
\]

### 5. Slowly growing cutoff and physical scaling

Check the choice

\[
\kappa_\varepsilon(h)^2
=
\frac{\varepsilon}{2A}\log\frac1h,
\]

the resulting exponent \(h^{-3+\varepsilon}\), and the exact pullback

\[
\sigma_jD_{b_j,>V_j}^{\chi}
=
\int_{I_j}
\left\|
\nabla(I-S_{V_j/\sigma_j})v
\right\|_2^2\,dt.
\]

Finally, verify that global physical Fourier-tail continuity gives only

\[
\sigma_jh_j^{-3+\varepsilon}\to0,
\]

not a contradiction or an event-index summation.

## Scope guard

Even if valid, the theorem does not prove:

- non-reuse or summability of nested physical frequency tails;
- a lower bound on the physical zoom;
- identification with the next Besov event;
- a rough-hull theorem;
- regularity, breakdown, or a Clay alternative A--D.
