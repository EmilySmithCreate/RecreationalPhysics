# The owner's framework as an axiom system (family F of the framework eval)

Written 2026-10-30 (Fable). Form: the F family of `PLAN_FRAMEWORK_EVAL.md` gives a model "a small invented axiom
system that breaks one textbook habit, and questions about its consequences", scored by exact match, with a
**reversion foil**: the textbook answer, computed beside the framework answer, so that an answer matching the
textbook and not the framework is counted as a pull back. Every axiom below is labelled; the exact answers are
arithmetic from the axioms and were checked by hand here; the physics is the owner's hypothesis and is unverified.

The plan names four habits an F framework may break. Her framework instantiates all four:

| Habit the plan names | Where her framework breaks it |
|---|---|
| a quantity made of two parts that combine by a stated rule, not by addition | energy = 4·uncurl + 4(λ − 1)·curl (A3): the two parts carry different weights and the flat state is exactly zero |
| a speed limit that depends on a count | light moves one link per tick; a path's time is its link count (A6) |
| a count conserved in thirds | charge is the net count of signed thirds (A7) |
| a lattice distance defined by an invented rule | distance is the fewest links between two points; a curled direction of length 4 makes far points near (A4, A6) |

## The axioms

Notation: D directions (links per point 2D); N points; S squares; on a link e, S_e squares; flat value s₀ = D − 1
squares per link (2 at four links, 4 at six); curl C = Σ_e (S_e − s₀)₊, uncurl U = Σ_e (s₀ − S_e)₊; λ > 1 the curling
cost knob; a = 4(λ − 1) the release per point per direction.

- **A1 (hers, H1, confirmed 25 October).** The base has two degrees of freedom, curl and twist. Points and links are
  not in the base; they describe the three-dimensional space that emerges. Everything below A1 is a statement about
  that description.
- **A2 (hers, Updates 105 and 108, the hard rule).** Curl and uncurl total zero: C = U. In the toy, S = N·D(D − 1)/2
  exactly (S = N at four links, S = 3N at six). A move is allowed only if it keeps the count.
- **A3 (exact, O159).** H = 4U + 4(λ − 1)C. Under A2, H = 4λC. Flat space (C = U = 0) has energy exactly zero at every
  size, and no valid arrangement lies below it (exact, Q18: the hard-core rule forbids a triangle beside a square).
- **A4 (exact, the ladder; checked 30 October on every rung at D = 2, 3, 4).** A torus with c directions curled to
  length 4 has, per point: squares D(D − 1)/2 + c/4; surplus c; energy 4(λ − 1)c; local dimension D − c. The energies
  of the rungs are additive: each curled direction costs the same a per point, whatever the others do (untied).
- **A5 (exact, O13 and `docs/figures/ladder_kinds.json`).** The cheapest single move out of a rung costs
  −16 ΔS + 4λ ΔX for the cheapest kind (ΔS, ΔX); it does not depend on N once the open sides exceed 6. At four links,
  out of the tube (c = 1): 32 − 16λ, which is 12 at λ = 5/4; out of flat: 32. At six links, flat: 64; out of the slab
  (c = 1) at λ = 5/4: 36; out of the rod (c = 2): 16; out of the 6-cube: −4 (downhill). The release of opening one
  direction is aN and grows with N; the wall does not.
- **A6 (hers, Update 88).** Light moves one link per tick in open directions; matter moves less than one link per
  tick. Time between two events is counted in ticks; distance in links.
- **A7 (hers, Updates 97 and 101).** Every matter strand is three thirds; electric charge is the net count of signed
  thirds and is conserved as a count; charge needs mass present. Dark strands carry no charge.
- **A8 (hers, Updates 107 and 109).** Three 60° spin-twists make the half turn; spin is counted in halves.
- **A9 (hers, H5, confirmed).** A birth makes twins of opposite handedness; their curvatures are opposite in sign and
  total zero; ours is slightly negative, the parent slightly positive.
- **A10 (hers, H6 and Update 106, decided in principle).** Empty flat space grows at no cost by whole rows; regions
  holding matter or curl keep their size.
- **A11 (hers, claim 6; exact in every sealed run, Q12).** Across a change the total of the arrangement's energy and
  the stores is conserved exactly. After space exists and expands there is no global bookkeeping.
- **A12 (hers, the loop; Updates 23, 26, 43, 44).** Spacetime is one turn of a loop. A turn ends when everything has
  gathered into black holes and nothing moves, so there is no time; observers are most likely found in the loop whose
  turn holds the most of them. *(Not modeled in any toy; kept here because the eval's C family needs the whole
  framework stated.)*

## The question bank (twelve; exact answers; the reversion foil beside each)

Each question is answerable from the axioms alone. "Framework" is the exact answer; "Textbook habit" is the answer a
model gives when it reaches for standard physics instead (ours; it is the reversion foil, not a claim that the
textbook is wrong about the real universe). Numbers use λ = 5/4 unless stated, so a = 1.

| # | Question | Framework (exact) | Textbook habit (the reversion) | Axioms |
|---|---|---|---|---|
| 1 | A six-link arrangement has curl 40 and uncurl 40 at λ = 5/4. Its energy? | 4·40 + 4·(1/4)·40 = **200** | "Net curvature zero, so energy zero": **0** | A2, A3 |
| 2 | The same arrangement with uncurl 40 and curl 0 (allowed if A2 is not imposed). Energy? | **160** | "Curvature either sign costs the same": 160 only by luck; the habit answer treats curl and uncurl alike, giving 160 for curl 40 too (framework: 40) | A3 |
| 3 | The rod 4 × 4 × 18 (N = 288, c = 2) opens one direction at λ = 11/10. Energy released? | aN = 4·(1/10)·288 = **115.2** | "The whole curling energy comes out": 230.4; or "energy is conserved, nothing is released": 0 | A4 |
| 4 | The tube 4 × L at λ = 5/4: the activation to start opening, at N = 48 and at N = 192? | **12 and 12** | "A barrier scales with the system": 12 and 48 | A5 |
| 5 | Two scars in a flat sheet, 20 links apart, each costing 32 alone. Energy of both? And at 200 links apart? | **64 and 64** (additive; no pull at a distance) | "They attract with an inverse-square law": less than 64, more at 20 than at 200 | A3 |
| 6 | Light leaves a point and reaches one 10 links away. Fewest ticks? A matter strand on the same path? | **10; more than 10** | "Speed in meters per second; distance in meters"; or the strand can arrive in 10 | A6 |
| 7 | Readings on the rung D = 4, c = 2: squares per point, surplus per point, local dimension? | **6.5, 2, 2** | A guess that "half curled" is half the squares: 3.5 | A4 |
| 8 | Three strands carry thirds +1, +1, −2 (in units of a third). Net charge? Is a lone strand of +1 third allowed? | **0; yes** (charge is a count of thirds) | "Charge comes in whole units; a lone third is forbidden" | A7 |
| 9 | A sealed tube of 96 points at λ = 5/4 starts with 12 in its store and opens fully to flat. Store at the end? | 12 + 96 = **108** | "Some is lost as heat": less than 108 | A4, A5, A11 |
| 10 | The daughter's curvature is −k. The parent's? Their total? | **+k; 0** | "Each universe's curvature is set by its own matter"; no constraint | A9 |
| 11 | A region of 1,000 empty flat points doubles in size. Its energy before and after? | **0 and 0** | "Vacuum energy scales with volume": E and 2E | A3, A10 |
| 12 | Under A2 at four links, 18 points. How many squares? Can the 4-cube (S = 24) occur? | **18; no** | "The ground state is the most tightly bound": the 4-cube | A2, A4 |

Two side notes for the scorer. Question 2 shows a foil the plan warns about: a habit answer can coincide with the
framework answer by accident (uncurl alone); the generator should vary the numbers so that the two differ. Question
5 is measured as well as exact in this record (O22, T13 rung 3), so it can double as a C-family item if a model
insists on an attraction.

## What this bank does not contain

Nothing about the loop (A12) has an exact consequence a question can score; nothing about twist has a rule yet
(A8 is a count, not a dynamics). The world family (`world_family_curl_store.md`) carries the dynamics the record
actually has: feeds, walls, releases, cascades.
