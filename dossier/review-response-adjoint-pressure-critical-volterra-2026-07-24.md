# Review response: critical scalar Oseen--Volterra obstruction

**Date:** 2026-07-24
**Route:** ROUTE-R3B
**Verdict:** valid after two precision repairs
**Clay status:** unsolved

The independent adversarial reviewer audited
[the reduction](experiments/adjoint-pressure-critical-volterra.md)
against the
`review-letter-adjoint-pressure-critical-volterra-2026-07-24.md` (archived in Git at `c277792`),
the exact cached Barker source, and the executable ledger.

No fatal analytic flaw was found.

## Accepted scalar theorem

For \(0<\gamma<1\),

\[
(\mathsf H_\gamma f)(t)
=
B(\gamma,1-\gamma)^{-1}
\int_0^t(t-s)^{\gamma-1}s^{-\gamma}f(s)\,ds
\]

is a positive contraction on \(L^\infty(0,T)\) and

\[
\mathsf H_\gamma^m1=1
\quad(m\ge1).
\]

Hence \(r(\mathsf H_\gamma)=1\): the exact critical weak-endpoint scalar
majorant is causal but not quasi-nilpotent.

For the perturbed weight \(s^{-\gamma+\varepsilon}\),
\(\varepsilon>0\), the reviewer confirmed

\[
\mathsf H_{\gamma,\varepsilon}^{\,m}1(t)
=
t^{m\varepsilon}
\prod_{j=1}^m
\frac{B(\gamma,1-\gamma+j\varepsilon)}
     {B(\gamma,1-\gamma)}
\]

and

\[
\left\|\mathsf H_{\gamma,\varepsilon}^{\,m}\right\|
\le
\frac{(C_{\gamma,\varepsilon}T^\varepsilon)^m}
     {(m!)^\gamma}.
\]

Thus every fixed positive time-power gain gives a summable scalar
interaction series.

## First precision repair

The pointwise beta identity for \(t^\lambda\) is finite when
\(\lambda>\gamma-1\), but \(t^\lambda\) belongs to the declared
\(L^\infty(0,T)\) domain only when \(\lambda\ge0\).  The theorem now
states both facts separately.  The eigenvector and subcritical iteration
arguments use only nonnegative exponents, so no conclusion changes.

## Accepted Oseen threshold

From

\[
\nabla b\in L^{2+\delta}_{x,t},
\qquad 0\le\delta<1,
\]

homogeneous Sobolev, with the inherited whole-space normalisation,
gives

\[
b\in L^p_tL^q_x,
\qquad
p=2+\delta,
\qquad
q=\frac{3(2+\delta)}{1-\delta}.
\]

The projected differentiated heat kernel has exponent

\[
\vartheta
=
\frac12+\frac3{2q}
=
\frac3{2(2+\delta)}.
\]

The reviewer confirmed the exact time margin

\[
\boxed{
\varepsilon_{\rm O}
=
1-\vartheta-\frac1p
=
\frac{2\delta-1}{2(2+\delta)}
=
\frac12\left(1-\frac2p-\frac3q\right).
}
\]

It is positive exactly when \(\delta>1/2\).  In that case, a finite
time partition makes every diagonal causal block arbitrarily small.
The spectrum of the resulting finite lower-triangular block operator is
the union of its diagonal spectra, proving \(r(T_b)=0\) on the stated
\(L^\infty_tL^a_x\) space.

The varying-exponent audit was also accepted:

\[
\sum_{m=1}^N\varepsilon_m
=
N\varepsilon_{\rm O}
-\frac32
\left(\frac1{a_0}-\frac1{a_N}\right).
\]

The endpoint correction is bounded, so a negative base margin cannot
support an arbitrarily long staircase of positive heat-kernel/Hölder
margins.  Interpolation with
\(L^\infty_tL^{3,\infty}_x\) remains strictly above the Serrin line for
every positive interpolation weight when \(\delta<1/2\).

## Accepted Barker audit and second precision repair

The reviewer checked the exact arXiv v2 proof.  It constructs

\[
\delta_B
=
\frac{3C_{5,\rm univ}}
     {12M+6C_{5,\rm univ}}
=
\frac{C_{5,\rm univ}}
     {4M+2C_{5,\rm univ}}.
\]

The note initially said “for every \(M>0\)”.  The rational expression is
algebraically in \((0,1/2)\) for every positive \(M\), but Barker's
theorem assumes \(M\) sufficiently large.  The statement now retains
that source hypothesis.

For every admissible \(M\),

\[
\delta_B<\frac12,
\qquad
\varepsilon_{\rm O}(\delta_B)
=
-\frac{2M}{8M+5C_{5,\rm univ}}<0,
\]

and

\[
\frac2p+\frac3q-1
=
\frac{4M}{8M+5C_{5,\rm univ}}>0.
\]

The packet scaling

\[
\int|\nabla b_R|^{2+\delta}\,dx\,dt
=
R^{1-2\delta}
\int|\nabla B|^{2+\delta}\,dx\,dt
\]

was accepted.  Barker's gain leaves the radius power positive, so fine
packets become cheaper.

## Exact retained boundary

At \(\delta=1/2\),

\[
p=\frac52,\qquad q=15,\qquad \frac2p+\frac3q=1.
\]

The reviewer confirmed that this is already the classical
Prodi--Serrin regularity line for the actual velocity.  Raising the
gradient exponent to \(5/2\) would therefore be a regularity-strength
theorem, not a routine improvement of Barker's small exponent.

The accepted reduction does not:

- prove that the true Oseen operator is not quasi-nilpotent;
- replace a weak scalar time endpoint by Barker's strong \(L^p\) input;
- sum the global \(L^1\) adjoint-pressure functional;
- exclude the selected feedback remainder or direct-response branch; or
- prove regularity, breakdown, or any Clay alternative A--D.

It closes only a positive norm-majorant shortcut.  The live causal
input must exploit Oseen-specific solenoidal/tensor cancellation,
pressure cancellation, or actual same-trajectory ancestry.

## Validation

The reviewed state passed:

- `make adjoint-pressure-critical-volterra`;
- all 9 focused tests;
- records, links, and mathematical-markup validation;
- the full repository suite with 635 tests; and
- `git diff --check`.

The reviewer made no file edits.
