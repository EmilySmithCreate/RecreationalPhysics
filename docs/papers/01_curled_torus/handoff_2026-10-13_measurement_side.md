# Hand-off: the measurement side of paper 1 (13 October 2026)

Written for the assistant who takes this up next, and for the owner. It is a plan, not a result: **nothing
below has been registered or run**, and every proposal is *ours, unverified*. The ideas are also in
`sandbox/NOTEBOOK.md` (13 October) in a line or two each; this page is their one home in full.

## Why this exists

On 13 October the owner asked whether running the toys of G.-W. Chern's group beside ours would help paper 1,
"especially because we can ask trugenburger to read the first couple questions but we don't have an identified
reader for the measurement side". The answer given, and the reason for this page:

- **Their toys are different and running them would test nothing of ours.** Electrons on a fixed lattice
  ([JC26]) and spins on a fixed lattice ([LLC26a]); in our toy the wiring itself is what changes.
- **Their measurements on our toy would help**, and so would checking our measuring tools once on a model
  whose answer is known exactly. Each item below is one of those.
- **The measurement side has two natural readers, who publish together:** M. Vucelja (relaxation and first
  passage in Markov chains under Metropolis dynamics) and G.-W. Chern (defects and energy landscapes). What
  was read of their work, and how, is in `docs/reading/notes/2026-10-13_chern_group_vocabulary.md`
  (sections 2, 7 and 8).

## What changed in paper 1 on 13 October

- The technical manuscript gained four insertions and two references ([JC26], [LLC26a]): "minimax barrier"
  where the text says what the 12 units is not; "isolated ... microcanonical" where the system is sealed;
  "domains separated by defects" for T61's endpoints; a paragraph of relatives in the Discussion, marked
  context and not validation. Rebuilt with `scripts/build_curled_paper.py`.
- The plain-language edition's source list now carries those two as sources 9 and 10, so that a number means
  the same source in both editions; its own sources moved to 11 to 14. Its text is otherwise unchanged.
- No claim, number or verdict in paper 1 changed.

## What not to do

- Do not build the Holstein model or any other toy of theirs. It would reproduce published work, test nothing
  in the hypothesis, and add code nothing here builds on.
- Do not put anything from a sandbox look into paper 1 as evidence (rule 16). A look can narrow a sentence;
  a new number needs a registered test or, for an exact count, a tested script.
- Do not quote a patch energy as a barrier (O118, "Correction").

## The work, cheapest first

### 1. Check the measuring tools on a known answer

**What.** A chain of up-or-down spins, each wanting to match its neighbors, started at random and run cold
with single-spin flips. The borders between up and down regions wander, meet and cancel, and their number is
known exactly to fall as one over the square root of time (general knowledge; **read the source and write the
exact formula into ASSUMPTIONS before coding**: Glauber 1963; Bray's 1994 review).

**Why.** Paper 1 and paper 2 report waits, counts of leftovers and fitted exponents from tools that have only
ever been run on our own toy. A reader from kinetics will ask what those tools give on a case with a known
answer. The project did exactly this for the flat-histogram sampler before trusting it (TASKS T6).

**How.** A small script that runs the chain, then pushes its output through the *same* functions the papers
use: the border count, the exponent fit with resampled errors (`scripts/analyse_t51_amendment3.py`), the
survival reading. No part of `src/graphity` changes.

**Accept when** the fitted exponent is −0.5 within its stated error over two decades of time, and the
prefactor matches the formula. **Lands in** the methods supplement (one paragraph) and `tests/`. **Cost:**
an afternoon; minutes of computing. Sandbox first; the test file is its promotion.

### 2. The lowest wall on any route out of the curled tube

**What.** Paper 1 says the 12 units is a first-exit cost and "not a proven minimum of the maximum energy
along a complete conversion path". That quantity has a name, the minimax barrier ([LLC26a]), and at small
sizes it can be computed exactly: raise a ceiling on the energy one unit at a time (energies at
λ = 1.25 are whole numbers) and list every arrangement reachable from the tube by swaps without going
above the ceiling. The lowest ceiling at which the list contains an arrangement with every link on two
squares is the answer, and the list gives a route.

**Why.** It is the gap the paper names in itself, and the first thing a landscape reader would compute.
T22 found that about a third of first exits fall back; the route should pass through the states where they do.

**How.** Start from the move listing already used for the neutral classes (`scripts/exact_torus_level.py`,
`src/graphity/small_graphs.py`). Begin at 32 and 48 dots. The list can grow fast: count arrangements up to
renaming where possible, stop and report if a ceiling's list passes a few million. Report the ceiling, one
witness route, and the list's size at each ceiling.

**Accept when** it returns 12 as the lowest ceiling that leaves the tube's own family (a check against the
paper), and either a ceiling that reaches a zero-energy arrangement or a stated bound. **Lands in** a tested
script and one sentence in "The cost of leaving" for the sizes done. Sandbox first. The same calculation is
what T54 lacks in three directions and what paper 2 needs for its three kinds of scrap.

### 3. One map of the outcomes (no new run)

**What.** T9 and T61 already hold, cell by cell, what an isolated tube ends as for each amount of room
(stores per dot) and each curling cost: six around and clean, regions of differing width joined at defects,
or damaged. Draw them on one pair of axes. In the group's words this is a dynamical phase diagram ([JC26],
Fig. 1).

**Accept when** every cell is transcribed from the registered readings and none is interpolated.
**Lands in** the supplement, or a figure in a later revision. **Cost:** an hour.

### 4. What the stores are doing

**What.** Paper 1 says the stores' mean energy is not a calibrated temperature because their histograms
were not saved. Save them in a fresh isolated run and test whether they follow the expected falling-off
curve. Then ask the notebook's question: does it matter for how fast the box settles whether the push sits
in one store or is spread over many? That second question is [KV26]'s subject.

**Needs** a registration (it is a measurement with a claim attached) and the owner's prediction.

### 5. Whether a first exit commits

**What.** Paper 1's plain edition already names this as the next experiment: save the arrangement after each
of the first few swaps, restart many runs from each, and count how often each returns to the tube and how
often it goes on to convert. With item 2 it separates opening the door from walking through it.

**Needs** a registration with a held-out size (rule 14) and the owner's prediction.

Counting leftovers against time the way the group does belongs to paper 2, and is in that paper's draft.

## The readers

Nothing is drafted or sent, and nothing is sent from a session. The owner's rules apply: one narrow question,
the AI disclosure sentence, a check of the reader's recent papers first.

- **M. Vucelja.** Her recent work is on how fast a system relaxes under Metropolis dynamics and on mean first
  passage times ([WV22], [TBLRV25], [KV26]; abstracts only so far). The question already written for her in
  the series plan stands: for a barrier of one move under a local switch chain, is a share of about 0.6 of
  first exits going on, unchanged by the barrier's height, what she would expect? **Read [WV22] and
  [TBLRV25] in full first.**
- **G.-W. Chern.** The question is in the note, section 7: two defects with nearly the same first-exit cost,
  one of which anneals. That is paper 2's, and item 2 above is its paper 1 half.

## For the owner to decide

1. Whether items 1 and 3 are done before anyone is asked to read paper 1 (ours: yes; they are cheap and they
   answer the first two questions a measurement-side reader would ask).
2. Whether item 2's number, once it exists, goes into paper 1 now or into its next revision
   (`v2_changes.md`).
3. Her predictions for items 4 and 5 before either is registered.
