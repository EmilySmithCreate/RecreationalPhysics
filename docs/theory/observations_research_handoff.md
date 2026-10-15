# From the toy to the sky: handoff for connecting the hypothesis to observations

**Written 14 October 2026, for an AI assistant starting a new line of work in this repository. Emily, the owner,
reads it too.** Her request, in her words: "I need another bot to begin work on connecting the theory to
observations and explaining the unexplainable."

## 0. What this work is, and what it is not

**The job.** For each observation that standard physics measures well but does not explain (the dark matter, the
size of dark energy, the conditions at the birth, the excess of matter over antimatter, what happens inside black
holes), write down:
1. the measured numbers, with uncertainties, from sources you have read;
2. what the owner's hypothesis says about it;
3. what the toy model in this repository has shown, exactly or by measurement, and what it cannot show;
4. which published work already does something close, and what its numbers and limits are;
5. a test: what a version of the hypothesis would have to output to match, and what observation would rule it out.

**Not the job.** Making the hypothesis look good. A target is something it must reproduce, never evidence that it
does (CLAUDE.md rule 13). "Already published" is good news to the owner: she wants existing mathematics she can apply
to her theory for predictions and constants, not novelty for its own sake. A clear "this observation rules that
reading out" is as useful as a match.

**Status of the hypothesis.** A hobbyist's hypothesis, tested so far only on a toy graph model. No physicist has
reviewed any of it. Physics reasoning produced by an AI (including you) is unreviewed: label it "ours, unverified".

## 1. Read first, in this order

1. `CLAUDE.md`: the rules. Especially rule 10 (four kinds of statement), 13 (a close number is not a result), 15
   (a written search behind every "we have not found"), 16 (the sandbox), 17 (one fact, one home).
2. `docs/papers/programme_draft.md`, section "The claim, in the author's words": her current best guess, confirmed
   9 October (VISION Update 50). Then chapters 2 (the scrap) and 6 (black holes and the loop).
3. `docs/design/reality_targets.md`: six targets and six constraints (7 to 12) already written against observation.
   **Build on it; do not start a parallel list.** Targets 3 and 5 as first written predate VISION Update 41 and are
   annotated there.
4. `VISION.md`: claims 1 to 6 at the top; then Updates 41 (the target is the make-up at birth, not today), 50 (the
   three-shares story set aside), 52 (her lean: the burp is the hot lump, the scrap is the best guess for the dark
   matter, dark energy is what does not thin), 54 and 56.
5. `ASSUMPTIONS.md` entries O89 (the shares at birth: settled cosmology applied by us), O103 (three outside reviews
   and the constraints they raised), O107 (what the scraps are), O114 (concentrated energy does not curl space),
   O126 (the column's wiring).
6. `sandbox/NOTEBOOK.md`, entries of 14 October: her newest ideas, which this work starts from (section 3).

Glossary: `docs/papers/glossary.md`. Older notes may say "Omega"; it is X.

## 2. What the toy can and cannot say

**Exact, and the most useful single fact for this work** (ours, from the energy's definition): the toy's energy is
H(λ) = H(1) + 4(λ − 1)·X, where H(1) is the published model of combinatorial quantum gravity (CQG) and X counts the
surplus squares on links that sit on three squares. X is zero on flat space and on the curved background of the
published model ([T25] Fig. 7; O67). So the extra term, which the owner calls the **curling cost**, is invisible
wherever space is smooth and acts only where space is curled tight. In words she agreed to on 14 October: the cost is
masked in smooth space, and "mass pays" it where enough energy gathers. *Ours, general knowledge, to verify:* that is
the shape physicists expect of corrections to general relativity: silent at low curvature, active near black holes
and at the birth.

**What the toy has shown** (measured, in two directions unless stated): a curled arrangement stuck for now opens from
a seed as a front and releases a fixed amount per point (paper 1); what it opens into is a tube six around, not an
endless sheet (O116); it leaves a few small stuck knots of fixed energy whose number is set at the opening, not by the
cooling (O104, O107). In three directions nothing opens all the way under any rule tried (T44 to T49, T53, T56), and
concentrated energy breaks flat space rather than curling it, with or without her tie (T57, O114).

**What the toy cannot say, ever, as it stands:** anything in physical units (no map from toy units to GeV or metres
exists); anything about expansion, so nothing about how a component thins as space grows (constraint 7 of
`reality_targets.md`); anything about time; anything about gravity at a distance (its flat space is gapped, O60).
Its sizes are hundreds to a few thousand points. **Naming:** only λ = 1 is CQG; at λ ≠ 1 write "our family around the
published model", never "combinatorial quantum gravity" (the model's author's condition).

## 3. The owner's newest ideas (14 October), the starting point

In her words, from `sandbox/NOTEBOOK.md`:
- Too much energy, or too much of a particular type, in one concentration "can curl space paying three dimensions at
  once"; it "can be different force or mechanism than reg gravity".
- "I don't think random energy folds the space. It's a specific type of energy, generated by black hole, maybe that is
  dark matter unseen mass, the black hole connects open space to a relic." Asked which of three readings she means:
  (a) the relic is the seed a fold grows from; (b) the black hole makes a different kind of energy that folds; (c) the
  dark matter is that energy or the relics: "all are the case".
- "the blackhole starts when you have high density dark matter, which is more of space in curled relic form that
  carries curling energy, is concentrated and curls the 3 dimensions into one"; a new space then opens with its own
  relic, releasing "the various types that are released at the big bang and their proportions".

**Tested the same day, in the sandbox (not evidence, rule 16):** a relic in two-direction space, with ordinary energy
packed beside it, sealed, grows no curled region at any energy up to 2.7 times the price of curling the whole space;
energy beside the relic and far from it read alike (`sandbox/LOG.md`, 14 October). Not yet tried: energy that may
only curl (her (b)) delivered at one relic or at a cluster of them. Reading (b) is a new ingredient and needs her dated
decision (VISION S1) before any registered run; it would reverse Update 32 ("one kind of energy").

So the picture you are connecting to the sky is, as of today: **dark matter as relics, small stuck curled knots that
carry curling energy; black holes forming where such relics are concentrated; a new space opening from a black hole
with a relic of its own.** Every link of that chain is hers to propose and ours to test; none is established.

## 4. The unexplained observations, in a suggested order

For each: the observation; what her picture offers; where the toy stands; relatives to read (none of these has been
read by anyone on this project unless marked); the first deliverable. Every number below is general knowledge and
must be checked at its source before it is written anywhere else.

### 4.1 Dark matter (the best candidate)

- **Observed:** about 5.4 times the ordinary matter; seen only through gravity (galaxy rotation, lensing, colliding
  clusters, the cosmic microwave background); every direct-detection search so far has found nothing; it sits in
  diffuse halos because it cannot radiate and cool.
- **Her picture:** relics, stuck curled knots of space carrying curling energy (Updates 16, 52; 14 October).
- **Toy:** three kinds of knot, stuck (every move out costs 11), fixed energy each (8, 14, 20 to 30 units), number set
  at the opening; the stubborn ones hold about 1 % of the release where the birth can afford far less than a millionth
  (O89, O107), so the reading rests on the seed count. Part of each knot's energy is curling cost (the column is
  24λ − 16: 14 at λ = 1.25, 8 at λ = 1; a second kind of column, 16λ − 16, costs nothing at λ = 1; O126). Open and
  exact: whether the stubborn knots are still stuck at λ = 1; if not, the curling cost is what makes them stuck.
- **Relatives:** Planck-mass black-hole relics as dark matter (MacGibbon, Nature 1987, and later work); primordial
  black holes as dark matter and their mass windows; asymmetric dark matter (a leftover excess like ordinary matter's;
  [KLZ09], [PV13], abstracts read; Update 42).
- **First deliverable:** a target sheet. What would heavy, rare relics interacting only by gravity have to satisfy:
  allowed mass range, number density, the limits from lensing, the microwave background, structure formation and
  direct detection; and the birth share, about 0.67 eV divided by the temperature of birth (O89). Then: what a map
  from toy units to physical ones would need (a length per link, an energy per unit) and whether any published
  argument fixes it (the model's author identifies an emergent scale of the network with the Planck length; where in [T25], to verify). **Do not fit anything to 5.36** (O74, O89: that ratio compares two slivers, not two releases).

### 4.2 Black holes forming from concentrated dark matter

- **Observed:** black holes whose outsides match general relativity; supermassive ones already present when the
  universe was young (to verify how early, and how puzzling that is held to be); the inside is unobserved.
- **Her picture:** a black hole starts where relics are dense; it curls the three directions together; it later opens
  a new space with its own relic.
- **The first hard question, ours:** dark matter is observed in diffuse halos because it cannot shed energy and
  collapse. A picture in which dense dark matter makes black holes has to say how it gets dense. Find what is
  published on dark matter collapsing directly into black holes, dark-matter spikes around black holes (Gondolo and
  Silk 1999) and seeds of the early supermassive black holes.
- **Toy:** no fold from any push, in two, three or four directions (O114 lists them); a relic plus ordinary energy
  grows nothing (sandbox, 14 October). Constraint 10 of `reality_targets.md` lists what anything must show before it
  is called a black hole, and the entropy question (a black hole holds the most entropy anything its size can; an
  ordered re-curled interior is the opposite) must be answered before a referee asks.
- **Relatives** (as targets, never evidence): Smolin's cosmological natural selection ([Smolin06], read); Pathria;
  Popławski (a universe inside a black hole); the Fife paper an outside review cited (reference to obtain from the
  owner).

### 4.3 The birth, and a signal it could leave

- **Observed:** the hot era began no later than about 4 to 5 MeV ([deSalas15]); the light elements and the
  microwave background bound extra light species (N_eff); pulsar-timing arrays reported a background of
  gravitational waves in 2023, for which an early sharp change spreading by bubbles or fronts is one proposed source.
- **Her picture:** a burp: a sharp, front-driven change releasing a fixed lump that becomes the hot era (claim 4,
  worded since Update 56 as "a jump in energy").
- **The open number:** the temperature of birth. A front-driven change makes gravitational waves at a frequency set
  by that temperature: near the MeV-to-GeV range for the pulsar-timing band, higher for LISA, and far beyond any
  detector if the burp was near the Planck scale (to verify the scaling). **First deliverable:** that table, temperature
  against frequency band against what has been seen or bounded, so the owner can see which births are testable.

### 4.4 Dark energy

- **Observed:** a density that does not thin as space grows, about 70 % of the total today and nothing measurable at
  birth (O89); its size is the cosmological-constant problem; recent survey results have been read as hints that it
  changes with time (to verify which, and how strongly).
- **Her picture:** the energy of space itself, its source open (claim; Update 52). One candidate in the toy is the
  curling cost of a direction that stays curled, which is far too large (O103 (e)).
- **First deliverable:** what each candidate would predict for whether dark energy changes with time, set against
  the survey results. Low priority until 4.1 and 4.3 have target sheets.

### 4.5 Matter over antimatter

- **Observed:** one extra particle of matter per billion or so, made somehow in the early universe.
- **Relevance:** the standard routes need a moment out of balance, and the best-studied one makes the excess at the
  walls of bubbles in a sharp transition (Update 42, from abstracts). A front-driven burp supplies such walls; the toy
  has nothing that comes in opposite kinds. A pointer for later, not a first task.

### 4.6 Lower priority for this work

Gravity's own shape (target 2 and constraint 9: a carrier on the points is decided in principle, Update 40, and not
designed); three large directions (target 1); time; the quantum world. These are theory-first problems and have
their own pieces on the programme page.

## 5. How to work

- **Where.** A fresh branch off `origin/main` in a worktree (`git worktree add -b claude/<topic>-<date>
  .worktrees/<topic> origin/main`); never the primary checkout, which may be parked on an old branch with other
  sessions' files. Commit with `git commit -o <paths>`, never a sweep. Tests (`pytest`) before every commit that
  touches code.
- **Reading.** Search the text of a paper, do not rely on a summary. Each paper read gets a note in
  `docs/reading/notes/` and its read status in `REFERENCES.bib` (read in full, abstract only, not read). Never invent
  a citation; if unsure of a detail write "to verify". Before any sentence says something has not been studied, write
  the search note (rule 15; template `docs/reading/notes/prior_work_template.md`).
- **Writing.** Target sheets go beside `docs/design/reality_targets.md` (for example `docs/design/observations/`),
  and `reality_targets.md` links them (one fact, one home). Every sentence says its kind: measured, exact, ours
  unverified, published (read or not), or the owner's.
- **Ideas.** Hers and yours go into `sandbox/NOTEBOOK.md`, hers in her words, worded as things she wants tested,
  each followed by how it could be tested. A quick check may run in `sandbox/` with one line in `sandbox/LOG.md`;
  it can narrow a claim, never support one.
- **Numbers that come out close** to a measured one: apply constraint 12 of `reality_targets.md` before anyone
  calls it a match.
- **Do not:** quote or paraphrase private correspondence (`docs/outreach/` is local only and gitignored); call the
  toy at λ ≠ 1 "combinatorial quantum gravity"; describe paper 1 as published or reviewed; promote anything to the
  programme page without a registered test behind it.

## 6. Open decisions that are the owner's

- Reading (b): a kind of energy that only curls. A new ingredient (S1); reverses Update 32 if adopted.
- Her prediction for the exact check: are the double column and the twist still stuck at λ = 1? The wording is not
  settled (`sandbox/NOTEBOOK.md`, 14 October).
- Her replacement for the fold mechanism after T57 (O114, rule 11).
- Whether dark matter is the relics, the energy the relics carry, or both, as she put it on 14 October; the target
  sheet for 4.1 should be written so that it serves all three.

## 7. A suggested first week

1. Read section 1's list and `docs/design/reality_targets.md` in full.
2. Target sheet 4.1 (dark matter as relics): numbers, limits, the published relic and primordial-black-hole work,
   and what a toy-to-physical unit map would need.
3. Table 4.3 (temperature of birth against gravitational-wave band).
4. The hard question of 4.2 (how dark matter gets dense enough to make a black hole), as a reading note.
5. A short summary for the owner, in plain language: for each, what would have to be true, what is already ruled
   out, and the one test that would tell most.
