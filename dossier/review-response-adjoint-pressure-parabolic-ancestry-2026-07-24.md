# Independent review response: parabolic tail ancestry

**Date:** 2026-07-24

**Reviewed request:**
[`review-letter-adjoint-pressure-parabolic-ancestry-2026-07-24.md`](review-letter-adjoint-pressure-parabolic-ancestry-2026-07-24.md)

**Primary note:**
[`experiments/adjoint-pressure-parabolic-ancestry.md`](experiments/adjoint-pressure-parabolic-ancestry.md)

**Verdict:** valid and nonduplicative in the stated
conditional/kinematic scope

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI recomputed the cutoff direction, the
fixed-parabolic exponents, the sharp power-law survivor, and every
functional-analytic step in the smooth kinematic construction.  It
found no fatal or repairable analytic gap.

The result is not duplicative of the earlier scalar ancestry survivor.
The reviewed coefficient-tail theorem newly permits the fixed-parabolic
\(7/6\) same-trajectory ceiling, and the new countermodel realises the
nested payments in an actual smooth-for-positive-time divergence-free
finite-energy path rather than only a nonnegative measure.

## Accepted conditional theorem

From

\[
\int_{I_j}
\|\nabla(I-S_{\Lambda_j})v\|_2^2\,dt
\ge c_\kappa\sigma_jh_j^{-3},
\qquad
\Lambda_j
=
\frac{\kappa h_j^{-1/2}}{\sigma_j},
\]

global physical Fourier-tail continuity gives

\[
\sigma_jh_j^{-3}\longrightarrow0.
\]

No nesting or disjointness of the physical intervals is needed for
this step.  If

\[
\Lambda_j\ge\frac{a_0}{\sigma_{j+1}},
\]

then

\[
\frac{\sigma_{j+1}}{\sigma_j}
\ge
\frac{a_0}{\kappa}h_j^{1/2},
\]

and hence

\[
\boxed{
\frac{\sigma_j^7}{\sigma_{j+1}^6}\longrightarrow0.
}
\]

With \(x_j=\log(1/\sigma_j)\), the logarithmic signs are

\[
\log\frac{\sigma_j^7}{\sigma_{j+1}^6}
=
6x_{j+1}-7x_j
\longrightarrow-\infty.
\]

Therefore

\[
\boxed{
\limsup_{j\to\infty}\frac{x_{j+1}}{x_j}\le\frac76.
}
\]

The general exponent ledger

\[
\sigma h^{-a}\to0,
\qquad
\frac{h^{-b}}{\sigma}
\gtrsim
\frac1{\sigma_{\rm next}}
\]

likewise gives

\[
\frac{\sigma^{1+a/b}}
     {\sigma_{\rm next}^{a/b}}
\to0,
\qquad
\limsup\frac{x_{\rm next}}x
\le1+\frac ba.
\]

## Accepted sharp survivor

For \(q>3\),

\[
\sigma_j=h_j^q,
\qquad
h_{j+1}
=
\kappa^{-1/q}h_j^{1+1/(2q)}
\]

gives exactly

\[
\sigma_{j+1}
=
\frac{\sigma_j}{\kappa h_j^{-1/2}},
\qquad
\frac{\kappa h_j^{-1/2}}{\sigma_j}
=
\frac1{\sigma_{j+1}}.
\]

The physical tail mass and distortion are

\[
\tau_j=h_j^{q-3}\to0,
\qquad
\frac{\sigma_j^7}{\sigma_{j+1}^6}
=
\kappa^6\tau_j.
\]

For fixed \(\kappa\),

\[
\frac{x_{j+1}}{x_j}
\longrightarrow
1+\frac1{2q}<\frac76.
\]

Letting \(q\downarrow3\) proves sharpness for this information.
Meanwhile the Cesàro mean of the deterministic roof gaps diverges.
The reviewer requested one precision: this is the empirical
\(r=\infty\) compactification boundary, not a stationary
infinite-mean probability law constructed by the note.

## Accepted smooth kinematic construction

The reviewer checked:

1. annular support separation leaves exactly one terminal detector
   packet after scaling;
2. the geometric packet tower lies in
   \(L^2\cap L^{3,\infty}\);
3. the locally finite activated tower converges strongly in \(L^2\)
   to its terminal trace;
4. its integrated enstrophy is bounded by
   \(C\sum_j\sigma_j\);
5. the baseline tail majorant decreases to zero and its increments
   telescope;
6. for
   \(W_K(x)=K^{1/2}W(Kx)\),
   \[
   \|\nabla W_K\|_2=1,\quad
   \|W_K\|_{3,\infty}=K^{-1/2}\|W\|_{3,\infty},\quad
   \|W_K\|_2=K^{-1}\|W\|_2;
   \]
7. arbitrarily large \(K_j\) simultaneously enforce the high-pass,
   weak-\(L^3\), and terminal \(L^2\) requirements;
8. disjoint compact time supports make the correction smooth for
   every \(s>0\) and give exact cumulative tail mass;
9. the high-pass telescope is exact because every later packet lies
   beyond \(2\Lambda_j\); and
10. the Hilbert inequality
    \[
    \|X+Y\|^2\ge\frac12\|Y\|^2-\|X\|^2
    \]
    and the factor four in the majorant absorb all cross terms.

The second accepted precision is that the path is
\(C^\infty\) for \(s>0\) and has a strong \(L^2\) terminal trace.  It
is not claimed smooth through \(s=0\).

## Exact accepted frontier

If the fixed-parabolic coefficient tail reaches the next event
frequency, consecutive physical event scales obey the sharp relative
logarithmic ceiling \(7/6\).  That ceiling does not force finite
empirical roof mean.

Even exact cutoff/next-event matching does not make the nonnegative
tail payments fresh.  A smooth kinematic path can place the required
mass arbitrarily far above the cutoff, where the same finer packets
pay every earlier nested tail.

The next PDE theorem must provide comparable-annulus localisation,
signed frequency flux, a cascade-speed ceiling, or a theorem that
far-finer mass creates an intervening actual event.

The subsequent independently reviewed
[parabolic tail-to-flux theorem](experiments/adjoint-pressure-parabolic-flux.md)
now forces the actual NSE payment into a comparable annulus, inherited
entrance high-frequency energy, or positive signed cumulative flux.
Its shell and Zeno ledgers close the ordinary high-pass balance as a
source of freshness; a quantitative PDE decrement, locality, non-Zeno
speed, ancestry, or event-index telescope remains open.

## Validation

- Targeted executable tests: 10 passed.
- Current canonical repository validation:
  105 experiments, 813 local-link targets, 31,722 mathematical
  delimiters, and 786 tests passed.
- Whitespace validation: passed.
