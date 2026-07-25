# Handoff: R3C amplitude-slab pincer

**Updated:** 2026-07-25 · **Clay status:** unsolved

**Live route:** `ROUTE-R3C` · **Checkpoint:**
`EXP-TYPE-II-ADJOINT-AMPLITUDE-PINCER-001`

## Load only

- [Amplitude-slab pincer](dossier/experiments/type-ii-adjoint-amplitude-pincer.md)
- [`ROUTE-R3C`](dossier/records/routes.json)

## Exact q4 survivor

- On every terminal interval, with
  \(M=\|u\|_{L^{3,\infty}}\), \(Y=\|\nabla a\|_2\),
  \[
  |\{M>\lambda\}|\lesssim
  \lambda^{-11/2}/\log(e+\lambda),\qquad
  \int Y^2<\infty,\quad\int MY^2=\infty.
  \]
- The exact sufficient gate is
  \[
  \int_0^{|I|}s^{-2/11}
  \log(e+|I|/s)^{-2/11}(Y_I^*(s))^2\,ds<\infty.
  \]
- Every survivor instead has divergent slab cost
  \(\sum 2^n\int_{\{2^n<M\le2^{n+1}\}}Y^2=\infty\) and adjoint-gradient
  spikes essentially \(Y\gtrsim M^{9/4}\), up to summable logarithmic loss.

## Exact live question

Can the same-trajectory cross defect force the displayed gate to be finite,
or equivalently force summable anti-correlation across the amplitude slabs?

## Closed shortcuts

- \(L_t^{22/9,2}\) is sufficient but stronger than the exact gate; strong
  \(L_t^{22/9}\) alone is insufficient.
- Differentiated energy retains \(\|\nabla u\|_2^4\).
- Generic heat smoothing gives no temporal \(2+\epsilon\) gain.
- Current BMO-skew Meyers theory is nonuniform across record amplitudes and
  meets projected pressure only at the base \(L^2\) forcing exponent.

## Next bounded cycle

Use the pressure-free Fourier commutator identity from the
[input round](dossier/experiments/type-ii-cross-current-anomaly.md) to seek
a cross-defect-specific, summable anti-correlation between \(M\) and \(Y^2\)
on high-amplitude slabs. Stop if the argument supplies only generic
parabolic gain, local pressure \(L^2\), or another restatement of the gate.

These are conditional repository theorems pending external review. Keep
slower clocks, divergent normalised energy, and R3B separate. No Clay
alternative is proved.
