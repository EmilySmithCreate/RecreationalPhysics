# Design brief: where the phase would have to come from, and what a wave rule would let us test

Written 2026-09-23, after T15 rung 3a was settled by argument (PREREGISTRATION T15 rung 3a; ASSUMPTIONS
O29) and the author said the quantum predictions "have to be there". This is a brief, not a decision:
the rule it proposes is a new ingredient, and under VISION S1 it needs a dated decision of hers before
anything is run against it. Physics reasoning is *ours, unverified* unless a source is named. Sources
are keyed to `REFERENCES.bib`, whose `note` fields say how much of each was read.

## 1. The gap, stated exactly

Rung 0 found what Update 17 said was there: a small closed loop has versions (its renamings, four for
a loop of four within sides) and a spectrum (its Laplacian eigenvalues, 0, 2, 2, 4). Rung 3a showed
what combining versions by **counting** can never do: a renaming of a fixed arrangement is a complete
instruction set, so counted versions are a classical probability space and Bell's theorem applies.

The whole difference between that picture and quantum mechanics is one thing: **the same set of
versions, carrying positive weights against carrying complex amplitudes.** Counts add and never
cancel. Amplitudes add with a phase and can cancel, and every quantum fact that is not also a
classical fact, interference and the Bell correlations alike, is a cancellation.

Two sources fix this precisely, and neither gets the phase from counting.

- **[Hardy01]** derives quantum theory from five axioms. The first four hold for classical
  probability too. The fifth, *there exists a continuous reversible transformation between any two
  pure states*, is what rules out the classical case: a classical system has finitely many pure states
  with nothing between them. Drop that axiom, or only the word "continuous", and classical probability
  returns. Discrete renamings fail it. A vibration, whose phase advances continuously, passes it.
- **[Gorard20]**, the closest cousin of "every version at once", runs every rewriting order at once and
  reads the branches as a superposition. Its amplitudes are not counts of branches: they are path
  weights under a "multiway norm" whose complex signature is argued from needing three signs in a
  metric, so the phase is put in through the norm; the Born rule is then imposed as the square; and
  Bell is met by making the theory explicitly non-local across branches, "in much the same way as
  de Broglie–Bohm". So even the nearest programme adds the phase by hand and escapes Bell by
  non-locality.

## 2. The bridge that is exact: versions are the loop's Hilbert space, vibrations are its momentum states

*Exact; checked numerically on 2026-09-23 for loops of four and eight.* The versions of a closed loop
of N points, its rotations, form the cyclic group Z_N. The space of complex functions on those
versions, the group algebra, is C^N: one amplitude per point. Its natural basis change is the Fourier
transform on Z_N, and the Fourier modes are exactly the eigenvectors of the loop's Laplacian, with
eigenvalue 2 − 2 cos(2πk/N) for momentum k. In words: **the vibrations of the loop are the irreducible
ways its versions can be combined**, and "the frequency sets the type" is the statement that momentum
labels the mode. So the author's identification of *what* is in superposition survives intact; the
picture was missing only the rule for *how* versions combine.

One detail from the model's own rule that renamings keep each point on its side. Side-preserving
rotations of a loop are the rotations by an even number of steps, Z_{N/2}. Their characters on the
modes are the phases a version can carry:

| loop | side-preserving rotations | phases on the modes |
|---|---|---|
| four points | by 0 or 2 steps | 1, −1, 1, −1 for k = 0, 1, 2, 3: signs only, no complex phase |
| eight points | by 0, 2, 4, 6 steps | 1, i, −1, −i, 1, i, −1, −i for k = 0 … 7: the full quarter-turn phases |

So the smallest loop that carries a genuinely complex phase under the model's own rule is the loop of
eight, which is also the loop the CHSH design needed for its 45° settings. A coincidence worth
noticing and not yet worth believing.

## 3. The proposed rule (for the author to decide; nothing runs against it until she does)

**Rule.** The state of a small closed loop is a complex amplitude on each of its points (its versions).
Amplitudes evolve by i dψ/dt = Lψ, where L is the loop's Laplacian, the operator whose eigenvalues rung
0 already computed. The probability of finding the loop's excitation at a point is |ψ|². A measurement,
a detector attaching at a point, projects onto the classes the attachment leaves. Everything else in
Update 17 stays as it is.

**What it is, said plainly.** It is Hardy's fifth axiom adopted as a postulate: e^{−iLt} is a continuous
reversible transformation between pure states. It is the continuous-time quantum walk on a graph
(standard; Farhi and Gutmann 1998 and Childs's work, from general knowledge, not read). It puts quantum
mechanics in; it does not derive it. Claim 2 then reads "X, with a wave rule on its loops, reproduces
quantum mechanics", which is the position every other programme is in, [Gorard20] included, and it is
honest to say so on the page.

**What it costs.** The loop no longer *explains* superposition; it hosts it. The sentence in Update 17
that "all versions hold at once because there is no vantage point" becomes philosophy, not mechanism.

**What it buys.** A programme in which the model, not the rule, supplies the content: which loops exist
(the model makes a closed loop of four and the 3-cube by itself, rung 0), their spectra (their "particle
types"), whether those vibrations survive as localised modes when the loop sits in a sheet (section 5),
and how a detector's attachment splits them. Each of those can come out either way.

## 4. The interference test, drafted for pre-registration once the rule is decided

**Scenario.** The loop of four, excited at one point at t = 0. Two routes lead to the opposite point,
round each side of the loop, of equal length; this is the smallest two-slit arrangement the model
makes by itself.

**Under the rule, exactly.** The amplitude at the opposite point is (1 − e^{−2it})²/4, so the
probability there is sin⁴ t: it rises to **exactly 1 at t = π/2**, the excitation having crossed the
loop entirely, and falls to **exactly 0 at t = π**, the two routes cancelling. Under counting (a random
walk on the same loop, generator −L) the same probability is (1 − e^{−2t})²/4, which rises
monotonically to 1/4 and never reaches 0 again or 1 at all. So the two rules differ by more than a
number: one has a time at which the excitation is certainly across and a time at which it is certainly
not, the other has neither.

**Predictions** to be the author's, chosen from: (i) the wave rule holds on the model's loops as they
are, including the loop of four inside a sheet; (ii) it holds on the isolated loop and fails inside the
sheet, the sheet's own modes swallowing the loop's; (iii) it is not adopted.

**What it can show.** Only consistency, and the model's contribution: whether the model's own objects
carry the rule's behaviour when embedded. It cannot show that quantum mechanics follows from the
model, because the rule is where the quantum mechanics is.

## 5. A rung that needs no decision: does the loop's vibration survive inside the sheet?

*Exact, on committed data, pre-register first.* If a particle is a vibration of a small closed loop,
then a loop sitting in a sheet must vibrate as a thing of its own: the Laplacian of the **whole**
arrangement must have eigenvectors concentrated on the loop, at or near the isolated loop's
frequencies, rather than the loop's modes dissolving into the sheet's band. This is a bound-state
question, and it is answerable now on `results/t7d_lam125_n144_adj/N144_rep3.npz` and the other saved
states with two loops of four: compute the whole graph's Laplacian spectrum and each eigenvector's
participation ratio, and ask whether any mode lives on the eight loop points. It uses nothing beyond the
Laplacian rung 0 already used, so it is not a new ingredient and needs only a pre-registration and the
author's prediction. If no localised mode exists, "a particle is a vibration of a small closed loop"
fails in this model whatever rule is adopted for how amplitudes combine.

## 6. Order of work, proposed

1. The author decides on the rule of section 3 (adopt, adopt with changes, or hold).
2. Whether or not she adopts it: pre-register and run section 5, which decides whether the loop is a
   resonator at all.
3. If adopted: pre-register section 4 with her prediction and run it, isolated loop first, then the loop
   in its sheet.
4. Only then any return to Bell, and then on a different footing: with amplitudes, the GHZ and CHSH
   designs of `quantum_loop_design.md` become ordinary quantum computations on the model's graphs, and
   the question becomes whether the model's *objects and links* realise the entangled states those
   designs need, which is a construction question and not a counting one.
