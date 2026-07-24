# Independent review request: one separated returned-low Oseen step

**Date:** 2026-07-24

**Route:** ROUTE-R3B

**Clay status claimed by author:** unsolved

Please review
[`experiments/adjoint-pressure-one-return.md`](experiments/adjoint-pressure-one-return.md)
adversarially.  The proposed theorem extends the reviewed
spatial--frequency estimate from a terminal high state to the component
which:

1. begins in the zero-data state tail above \(64F\);
2. makes one actual heat--Leray Oseen interaction into the annulus
   \(F\); and
3. immediately generates pressure in a fixed low band \(S\).

The claimed bound is

\[
\begin{aligned}
\mathfrak R^{(1)}_{S,F}(h)
\le
C_\nu M\frac SF
\min\{1,F^2h\}
\bigg\{
1
&+h^{7/4}
\left[
1+\log_+\!\bigl(D_b(h)h^3\bigr)
\right]\\
&+h^{21/4}
+h^{89/4}
+h^{103/4}
+h^6F^{-2}
\bigg\}.
\end{aligned}
\]

Please try to falsify, in particular:

1. the Oseen tensor convention in (13)--(15), including the fact that
   the spatial cutoff pieces need not be solenoidal;
2. the uniform annular kernel estimate
   \(CF e^{-c_\nu F^2(t-s)}\);
3. the support claim that output at \(F\) from state input above
   \(64F\) sees only coefficient frequencies comparable to the state;
4. the \(K^{-1}\) Bernstein gain and dyadic summation in (20)--(21);
5. the transfer of the reviewed local and off-diagonal shell ledgers to
   (17) and (26);
6. the inner constant \(h^{3/2}h^{-3/2}=1\);
7. the exact heat clock \(\min\{h,F^{-2}\}\);
8. the final Lorentz--Bernstein estimate
   \(\|\Pi_S(w_F\otimes b)\|_1\lesssim MSF\|w_F\|_1\);
9. the combined prefactor
   \((S/F)\min\{1,F^2h\}\);
10. the inversion
    \[
    \gamma_1(\beta)
    =
    \frac74+\beta+(1-2\beta)_+
    =
    \frac94+\left|\beta-\frac12\right|;
    \]
11. the physical scaling; and
12. the scope boundary: the note charges only one separated final
    returned-low interaction and does not cover multistage
    comparable-band descent or prove its participation floor.

Please classify the disposition as:

- valid in the exact stated conditional scope;
- repairable, with precise corrections; or
- invalid, identifying the first fatal implication.

The executable certificate is:

```bash
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_one_return -v
PYTHONPATH=lab python -m \
  navier_lab.adjoint_pressure_one_return
```
