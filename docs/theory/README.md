# The theory, part by part: where everything lives

Written 2026-09-22 at the author's request. The repository is organised by *time* (VISION updates,
pre-registrations, ASSUMPTIONS entries, commits), because that is what keeps the record honest: nothing
is moved, nothing is rewritten, and a reader can follow how each idea arrived. This page organises the
same material by *part of the theory*, the five parts of `docs/public/the-loop-and-the-floor_v1.html`,
so that the paper can be assembled from it without moving a single file. Update it when a part gains a
measurement; do not put content here, only pointers.

**Status words.** *Exact*: follows from the rules by argument or complete enumeration; no run can
overturn it. *Measured*: a pre-registered run with a verdict. *Exploratory*: a run without a
pre-registration, a first look. *Argument*: reasoning only, ours and unreviewed. *Untested*: nothing yet.

## Foundation: the model, and whether our tools are right

| What | Where | Status |
|---|---|---|
| The model (dots, links, squares, the penalty λ, the hard-core rule) | `ASSUMPTIONS.md` Q1–Q3; `src/graphity/cqg.py` | exact |
| Ergodicity and exact averages at N ≤ 18; the sampler checked against them | Q9, Q11, Q14; `results/ergodicity_small.csv`; `scripts/exact_small_averages.py` | exact |
| Reproduction of the published 2019 curve (rms 0.005) and of the λ = 0 shattering | VISION Updates 3, 4, 6; Gate A (TASKS); ASSUMPTIONS section D | measured |
| The disagreement with the 2025 figure, and the author's reply | Gate B (TASKS); O19, O26 | open; T13 running |
| The order of the disorder → order transition (the published question) | PREREGISTRATION T6; O11, O12, O17 | measured: FIRST ORDER at λ = 0; INCONCLUSIVE, bound stated, at λ ≥ 1 |
| The author's "hybrid" jump at N = 1024: equilibrium or metastable ascent | PREREGISTRATION T13; `configs/t13_*.json` | running (2026-09-22 night) |

## Part I. From X to space

| What | Where | Status |
|---|---|---|
| The claims (1, 3, 4, 5, 6) and what X is | `VISION.md` top; Updates 5, 13 | the hypothesis |
| The ladder: sheet, tube, knot; dimension as a count at a vertex | Update 7; `tests/test_cqg.py::test_sheet_tube_cube_ladder` | exact |
| The tube opens sharply: by chance, one front, 99 % one or the other | PREREGISTRATION T7; O13 | measured: TWO-STATE CHANGE at 64, 96, 192 |
| The push is 12, the same at every size; the drop is 4(λ − 1) per point | Q13; O23; ASSUMPTIONS section D ("the wall measured") | exact and measured |
| Waiting times follow the barrier-crossing law with nothing fitted | ASSUMPTIONS section D ("Arrhenius") | exploratory |
| Sealed: bonfire with a threshold; energy conserved to the last unit | PREREGISTRATION T9; O14; Q12 | measured |
| The leftover: one four-point remnant, however large; not a seam | PREREGISTRATION T10, T11; O15, O16 | measured |
| The leftover as dark matter; the sliver it needs | Update 16; O18 | hypothesis + exploratory |
| Matter as the melted phase (the published reading) | [T25] Sec. VI.1; Update 8 | published + argument |
| Design brief for X | `docs/design/model_x_brief.md` | brief |
| Figures | `docs/figures/tube_uncurls.png`, `sealed_story.png`, `leftover_determined.png`, `equilibrium_curves.png` | |

## Part II. Gravity

| What | Where | Status |
|---|---|---|
| Space is the floor: nothing lies below the flat sheet | Q18 | exact |
| A cold sheet accepts no move at all | O21 (1) | exploratory |
| No long-range force between leftovers at fixed wiring | O22; `tests/test_defect_interaction.py` | exact |
| A force that never fades, between regions of different order | O23 | exact |
| Gravity as a slope in the count of ways (entropic) | `docs/design/strange_loop_note.md` item 4 and "counting reframes O20"; Part II of the public document | argument |
| The measurement that would test it: free energy against separation | `docs/design/known_physics_plan.md` rung 3; TASKS T13 | untested |

## Part III. Black holes and the loop

| What | Where | Status |
|---|---|---|
| The author's extension (tube opens; gravity refolds; black holes re-curl; a new space elsewhere) | `docs/parked/extension_2026-09-22.md` | the hypothesis, parked |
| Concentrated energy melts a sealed sheet; it does not fold it | O20 (with its correction) | exploratory |
| Out of order no single move builds; out of a melt thousands do, downhill | O25 | exact |
| The strange-loop reading, and the one part of it tested | `docs/design/strange_loop_note.md`; PREREGISTRATION T12; O24 | argument; T12 NOT ESTABLISHED |
| The return leg's middle: what a squeezed melt rebuilds into | needs the local-spark protocol, TASKS T14 | untested |
| Tolman's objection and the answer offered | Part III of the public document; strange-loop note | argument |

## Part IV. Why you are in a loop

| What | Where | Status |
|---|---|---|
| Finite states must recur; the loop's time-fractions are counts | `docs/design/quantum_loop_design.md` section 2; Part IV of the public document | established mathematics, applied by us |
| Where a loop spends its time (the barrier-crossing law) | ASSUMPTIONS section D ("Arrhenius") | exploratory measurement |
| The three shapes; the observer constraint; the closure argument | `docs/design/strange_loop_note.md` "Why a loop at all" | argument, labelled philosophy; not on the scorecard |

## Part V. Why the world is quantum

| What | Where | Status |
|---|---|---|
| The author's hypothesis (interchangeable points; versions; measurement as a relationship) | VISION Update 17 | the hypothesis |
| The version counts already measured: melt 1, sheet 320, knots 10^29 | Q15; `scripts/measure_symmetry_cost.py` | exact |
| The design: rung 0 to 3, GHZ before CHSH, the predicted probabilities | `docs/design/quantum_loop_design.md`; TASKS T15 | brief; nothing run |
| What was read, and what it fixed | `REFERENCES.bib` (Zurek05, CSW14, AB11, Mermin90, …) | read in part |

## The written forms

| What | Where |
|---|---|
| The account told whole, no hedges (the paper's narrative spine) | `docs/public/the-loop-and-the-floor_v1.html` |
| The honest short page, every claim tagged with whose it is | `docs/public/did-space-snap-open_v1.html`; `docs/public/site/` |
| The draft post | `docs/public/medium_post.md` |
| Correspondence with the model's author | private; not in this repository |

## How the paper would be assembled

Take the five parts above in order. For each, the narrative comes from the loop document, the evidence
column comes from this page's "Where" pointers, and the status word is the honest label. The paper's
one extra job is the interconnections: the same landscape read both ways (Parts I and III), the same
count read as gravity and as superposition (Parts II and V), and the same recurrence read as "every
version exists" and as "why the floor" (Parts IV and V). Those three sentences are the theory's claim to
be one thing rather than five.
