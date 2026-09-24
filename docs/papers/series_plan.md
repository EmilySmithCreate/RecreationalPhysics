# The series: what each paper claims, what is established, what is missing

Written 23 September 2026, night, at the owner's request ("work through each of the other pieces with
similar detail; where needed design new experiments and predictions"). One entry per paper, in the
order they depend on each other. Every claim is at the level of the model; what it would mean for the
universe is the owner's framework, stated in paper 7 with its status beside each piece.

**Status words, used the same way throughout.** *Established*: pre-registered, run, verdict on the record.
*Exact*: arithmetic or exhaustive enumeration, no sampling. *Failed*: pre-registered and the prediction did
not hold. *Designed*: pre-registered or drafted, not yet run. *Idea*: the owner's, recorded, no test yet.

---

## Paper 1. Metastable curled tori and their front-driven decay (drafted)

**Claim.** In combinatorial quantum gravity with the local term's coefficient λ above 1, a torus with one
direction curled is metastable and opens into flat space sharply: a memoryless start, one front, two orders
side by side, an exact release, a local push of fixed size, one leftover of fixed size.

**Status.** Established at λ = 1.25 (T7, T9, T10, T11); exact results for all λ (ground state, ladder,
window, exit moves). The λ map (T8) is running; the analysis is written and tested.

**Missing.** Section V from T8. Then the owner's review, then the endorsement request to Carlo
(`docs/outreach/reply_draft_2026-09-23_second.md`).

**Draft.** `docs/papers/curled_torus/paper.tex`, `paper.pdf`; review page
https://claude.ai/artifact/3TcXFYr51m955zTkgitXwR.

---

## Paper 2. The leftover: size, number, and what makes it

**Claim to test.** The change leaves remnants of a fixed size, and their number is set by how the change
started (per seed), not by the size of the space. That is the model-level version of "dark matter is the
scrap of the change, abundant through many seeds" (VISION Update 16).

**Established.** One leftover per converted tube, however large (T10, ONE RING, HOWEVER LARGE, N up to 288);
its position is uniform, neither at the seed nor where fronts meet (T11, NEITHER); read from its wiring, it
is one column of the tube left curled, costing 24λ − 16, occasionally a two-point twist (20 units) or a
combination of small defects (8 to 45 units) (O13, O15, O28).

**Exact, new tonight (T8 pre-registration).** Near λ = 1 the column keeps a large share of the lump:
(24λ − 16)/(4(λ − 1)N), 22 % at λ = 1.25 and 72 % at λ = 1.05 for N = 64, falling with N.

**Established the same night (T17, O33): BETWEEN.** One to eight planted seeds in one tube leave 1.10, 2.15,
2.50, 3.40 leftovers on average; slope 0.29 ± 0.04 per extra seed. More seeds, more scrap, but fewer than one
each; both the owner's ONE PER SEED and our ONE PER TUBE failed. Next: where do the extra leftovers go when
fronts meet (merge, anneal)?

**Still to design.**
- *Does a leftover move?* Needed by papers 2 and 5. A column in a flat sheet, fixed coupling, followed for
  a long run; record its position every block. Cheap. Draft below (T19).
- *Does the leftover's share depend on λ as the exact formula says?* Read from T8's saved final states.

**What would have counted against the owner's picture, and did not happen.** ONE PER TUBE in T17. What did
happen is weaker than her hypothesis: the scrap grows with the number of seeds, but less than one per seed.

---

## Paper 3. The fertile window: which λ makes a lump, a stuck X, and a clean birth

**Claim to test.** There is a window of λ above 1 in which X is stuck for now, the change releases a lump,
and the new space can take the lump without melting; the owner's λ ≈ 1.25 sits inside it. With the rules
fixed between generations (the owner's decision of 23 September), the reason our λ is where it is would be
counting across loops, not evolution: a universe drawn at random belongs to the most prolific loop.

**Established.** At λ = 1.25: all of paper 1, and T9 (BONFIRE WITH A THRESHOLD: the new space survives only
if its surroundings can hold the lump; the needed room scales with N). At λ = 1.5: X is not stuck (T7).

**Running.** T8, the λ map of stuckness, sharpness, release and scrap.

**Measured the same night (T18, O34): PROPORTIONAL.** The room needed is 12, 36, 72 stores at λ = 1.10, 1.25,
1.40 (N = 96): it grows faster than the lump. A bigger λ gives a bigger lump and a harder birth.

**Honest limit.** The model has no black holes, so it cannot count offspring. It can map the ingredients
(stuckness, push, lump, room, scrap); fertility itself is the owner's framework.

---

## Paper 4. Closed regions: can concentrated energy re-curl space? (the black-hole piece)

**Claim to test.** In a closed region, energy concentrated into space can fold it back towards X (a black hole
in the owner's picture is a re-curled region that can "burp" a new space when it gets the activation energy).

**Established, and against.** O20: a sealed sheet given a budget of energy melts rather than folds, at every
budget and every λ tried; with named points. The exact move census (corrected 23 September): from perfect
space no single move adds a square, so a fold must run through a seam.

**Why it is the hardest.** The owner's theory has points interchangeable, and under that weighting a complete
fold (a whole closed piece, e.g. a 4-cube with 192 symmetries) gains enormously while a partial fold gains
nothing. That is the one route by which folding could win, and it is exactly the one named-points runs
cannot see. Doing it properly needs the symmetry count of every proposed state, which costs 0.1 to 24 s per
count at N = 160 with the present tool (Q15).

**Designed, and the blocking tool now exists.**
1. ~~*Exact, small.*~~ *Withdrawn the same night:* at N = 16 and 18, the only enumerable sizes, there is no flat
   sheet at all (the 4 x 4 torus is the 4-cube; the first flat torus is 6 x 6 = 36), so fold against melt cannot
   be posed there.
2. *A fast symmetry count: done (Q20).* igraph counts in about a millisecond where the old counter took up to
   45 s, agreeing exactly; a chain with interchangeable points built on it reproduces the exact interchangeable
   averages at N = 18. Per-move counting is affordable up to about N = 64.
3. *Next:* pre-register the closed-region test with the owner's prediction (her statement: open space spreads
   and heals; a closed region folds): O20's sealed sheet at N = 36 and 64, λ = 1.25, the same budgets, run with
   named and with interchangeable points side by side; the reading is the folded share of the damage.

**Measured the same night (T21, O36): MELTS EITHER WAY at N = 64**, the size where complete folds exist; a
fragile lean towards folding at N = 36 under the bath. The owner's closed-region fold is not seen for energy
spread through a box. The untested route is a local push with cold space around it.

---

## Paper 5. Gravity as the wish to refold: do leftovers pull on each other?

**Claim to test.** Leftovers attract at a distance through counting (entropy), and the pull depends only on
their energy, not their wiring (the equivalence principle). The owner allows kinds of dark matter to differ
slightly; ordinary matter must not (measured to one part in 10¹⁵).

**Established, exact.** No energetic force at a distance: defects sharing no square are exactly additive in
energy, with an attraction of 16 only where they touch (O22). So anything gravity-like must come from
counting.

**Designed tonight.**
- T19, *mobility*: does a leftover column move through the sheet at fixed coupling, and how far? Without
  motion there is no pull to measure by watching; with it, two columns can be released and their separation
  followed.
- *The interchangeable-points pull, exactly.* For two identical defects in a torus, the interchangeable weight
  of each placement is its symmetry count. Computable exactly for every separation. Our expectation: the
  count is large only at special placements (exactly opposite, aligned), so the "force" it makes is a set of
  preferred symmetric placements, not a smooth attraction. If so, that is a clean negative for the simplest
  version of the mechanism, and it should be said.
- **Run the same night (O32), and it came out that way:** at 18 separations in a 12 x 12 torus, two identical
  simple defects have 1 or 2 symmetries at every ordinary distance and 4 only when exactly opposite. No pull;
  a factor-2 preference for maximum separation. What remains open is the entropic force when the surroundings
  are free to rearrange, which the interchangeable chain (Q20) can now measure.

**What would count against.** Immobile leftovers, or a pull that depends on wiring for defects of equal energy.

---

## Paper 6. Quantum behaviour from counting versions

**Claim (VISION Update 17).** Superposition is the set of undetectably different versions of the world;
measurement is an interaction that makes them distinguishable.

**Status, plainly: the weakest leg.**
- Rung 0 (T15): INCONCLUSIVE by the letter; versions exist in the parts, and in a world with three different
  things there is exactly one, as in a melt.
- Rung 3a: CLASSICAL for every arrangement, by argument. Counting versions of one fixed arrangement is a
  hidden-variable theory and cannot violate Bell. The owner's prediction failed.
- Rung 0b: the loop of four is not a resonator in the sheet. Prediction failed.

**What the reading of Smolin adds (23 September).** His real-ensemble quantum mechanics ([Smolin11]) gets
Schrödinger's equation from real copies that *interact* (a non-local copy rule) and carry a *phase*. Those
are exactly the two ingredients the counting lacks. His "classical because it has no copies" matches rung 0.
And there is a prediction that separates the owner from him: a system unique in the universe but isolated
and symmetric should behave quantum-mechanically for her and not for him.

**Next, needing no decision.** Rung 1: do the chain's time-fractions equal the counts in the interchangeable
ensemble at N = 16 and 18? Validation, exact. Draft pre-registration below (T20).

**Needing the owner's decision first.** Whether to add an interaction among versions (Smolin's route, a new
rule, VISION decision under S1); whether to redefine the object as the cap; whether Part V of the public page
is restated.

---

## Paper 7. The framework, for the public page

**What it is.** The owner's claims 1 to 6 and the cosmological cycle, each with a status box: which paper
tests it, the verdict, and what would count against it. Told in her words, with every claim saying whose it is.

**What it must not be.** A claim that the framework is established. Today one piece is established (paper 1),
several are designed or running, and the quantum leg has failed as stated. VISION S5 (a physicist has read it)
is not met.

**Can it be published within a week?** Paper 1 as a preprint: yes, if Carlo or another physicist endorses.
Papers 2 and 3: possibly, if T17, T18 and T8 come out clean and the owner reviews them. Papers 4 to 6: not
honestly within a week; they can be published as a *programme*, with their tests named and their current
status shown, which is a stronger thing to publish than a framework stated as settled.

---

## Draft pre-registrations written tonight

T17 (leftover per seed) is committed and running. T18 (room needed against λ) is committed before its runs
(see PREREGISTRATION.md). T19 (leftover mobility) and T20 (quantum rung 1) are drafted in this file only, for
the owner's predictions in the morning; nothing is run under them.

### T19 (pre-registered and run): ANNEALS at every coupling (O35)

Take the final states of T10 or T17 that hold exactly one curled column in an otherwise flat torus. Continue
each at λ = 1.25 and g = 1.5 (and a warmer g = 2.0) for 100,000 sweeps, recording every 500 sweeps the
columns of the vertices at d = 1. Observable: the column position's mean squared displacement against time,
and whether the leftover survives. Predictions for the owner: (a) it moves (diffuses) at g = 1.5; (b) it
moves only at the warmer coupling; (c) it does not move before it anneals away or at all. Ours: (c) at
g = 1.5, since T10's leftovers stayed in place over 30,000 sweeps in a cold box; unknown at 2.0.

### Quantum rung 1 (pre-registered as T15 rung 1): AGREES (O37)

As `docs/design/quantum_loop_design.md` rung 1: at N = 16 and 18, the interchangeable-ensemble probability of
each class (exact, from the counts) against the chain's long-run time-fraction with the renaming correction
applied per recorded configuration. Prediction (validation, not physics): agreement within sampling error.
