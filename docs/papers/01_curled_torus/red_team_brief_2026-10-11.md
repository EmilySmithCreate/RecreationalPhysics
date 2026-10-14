# Brief for an independent reviewer: try to break paper 1 and its fourth map

Prepared 11 October 2026 for Emily Smith, the repository's owner, by Claude (Anthropic), the assistant that did the
work under review. Because of that, this brief tells you where things are and what to test. It does not tell you
what was concluded. Please keep it that way for as long as you can: form your own answer first, then compare.

## 1. What you are asked to do

Assume the paper is wrong. For each thing it says, find the cheapest calculation, known result, limit, symmetry
argument or run most likely to show why, and do the cheap ones.

Two objects are under review.

1. **Paper 1**, "The curled torus burps": `docs/papers/01_curled_torus/paper.tex` (built as `paper.pdf`), its methods
   supplement `supplement.md`, its file list `release_manifest.json`, and its plain-language edition
   `paper_plain_language.tex`. It is an unpublished manuscript. No physicist has reviewed it.
2. **One pre-registered run that the paper does not yet quote**: `PREREGISTRATION.md`, the section headed
   "## T60." It is a fourth attempt at a measurement the paper currently reports as three inconclusive attempts.
   The owner wants to know what, if anything, the paper may say about it. **Nothing about T60 goes into the paper
   until your report is in.**

Out of scope: the owner's wider hypothesis about spacetime (`VISION.md`). Paper 1 claims none of it. In scope is
only whether the paper's statements about this toy model are true and fairly worded.

## 2. Ground rules

- **Read-only.** Do not commit, push, or edit tracked files. Work in a scratch directory or a private copy. The
  runners refuse to overwrite `results/`; send any output of your own elsewhere.
- **Evidence is data, code and history**: `configs/`, `results/` (CSV, `.meta.json`, saved graphs), `scripts/`,
  `src/graphity/`, `tests/`, and `git log`. **Narrative is the claim under test, not evidence**: `ASSUMPTIONS.md`,
  `docs/HANDOFF.md`, `TASKS.md`, `docs/papers/programme_draft.md`, the "Known state" half of `CLAUDE.md`, and every
  "Reading" subsection of `PREREGISTRATION.md`.
- **Hold back these files and passages until sections 3 A and 3 F are done**, so that your work is blind: in
  `PREREGISTRATION.md`, everything under T60 after the heading "### What this cannot show" (the T60 readings, the
  amendment with numbers for the held-out size, the owner's held-out prediction); `ASSUMPTIONS.md` entries O113 and
  later; `VISION.md` Updates 53 and later; in `CLAUDE.md`, the paragraph that begins "Added 2026-10-11";
  `configs/t60_heldout_prediction.json`; `docs/HANDOFF.md`; `TASKS.md`; `docs/papers/programme_draft.md`; the
  scripts `read_endpoint_width.py` and `read_open_shells.py` with `tests/test_read_shapes.py`; the other paper
  drafts under `docs/papers/` (`06_fertile_window/`, `05_six_links/`, `12_black_hole/`), which quote results under review;
  the output of `scripts/analyse_t60.py`. Commit messages written after the T60 registration state our readings,
  so until then list history with hashes and dates only:
  `git log --format="%h %ad" --date=iso -- <path>`.
- Anything you reason about the physics is unreviewed, like ours. Label it so. Say what you did not check.
- The repository's own rules are the numbered list under "Non-negotiable rules" in `CLAUDE.md` (rules 1 to 15).
  Hold the work to them. Rules 4, 5, 10, 12, 14 and 15 matter most here.

## 3. The questions

### A. Derive T60's verdict yourself, blind

Read the T60 registration from its heading down to "### What this cannot show", and stop. It defines several
quantities by reference to three earlier registrations (T8, T23, T24, in the same file); read those definitions
in the registrations' words. The run's column meanings are in `scripts/run_tube_decay.py`. A saved graph loads as
`numpy.load(path)["adj"]`, an (N, 4) integer array of neighbors.

Then, **with code you write yourself** (do not import `scripts/analyse_t60.py`, `analyse_t24.py`, `analyse_t23.py`
or `analyse_t8.py`), compute from `results/t60_lam*_n*.csv` and `results/t60_*_adj/`:

1. for each of the 28 stage-1 cells: the gates, each of the three criteria, and whether the cell is "sharp" as
   registered;
2. the window verdict and the edge verdict, in the registration's own labels;
3. the numbers the registered recipe gives for the held-out size from stage 1 alone;
4. for the 7 held-out cells (N = 288), if they are in `results/`: the same quantities, and the registered
   comparison with the numbers of step 3. If they are not there, say so.

Write your verdicts down. Only then open the held-back passages and run `python scripts/analyse_t60.py`. Report
every difference between your numbers and ours, however small, and whose is right. Check once, by brute force on a
sample of saved graphs, that the library's square count and its per-vertex count `d(v)` (`src/graphity/`) do what
their docstrings say; after that you may use them.

### B. Was it registered honestly?

From `git log` alone, establish the order in which these came to exist on the branch: the T60 registration text;
`scripts/analyse_t60.py` and `tests/test_t60.py`; the configs; the queue manifests in `cloud/queue/`; the results
(fetched into `cloud/inbox/`, then moved into `results/`); each reading; the held-out numbers; the stage-2 queue;
the owner's held-out prediction; the stage-2 results. Flag anything written or changed after data it depends on
existed. In particular:

- Was any analyzer that T60 calls changed after stage-1 results arrived?
- Are T60's seeds fresh, that is, shared with no earlier run of the same grid? Are the decays in a cell independent?
- Does each result's `.meta.json` config equal the committed config?
- Pick the cheapest cell and rerun it from its config into a scratch directory. Does it reproduce the stored CSV?
  (The stored runs used Python 3.12.10, NumPy 2.0.0, Numba 0.67.0 on Linux.)

### C. The fourth-attempt problem

T8, T23 and T24 are three earlier registered runs of the same map. Each later run changed something. For each
change, decide: is it a repair to the instrument that could be justified without knowing the answer, or a
criterion moved until it passed?

- T60 changes how a decay's wait is timed and over which decays the memoryless check is taken. The old
  detector's columns are still in T60's CSVs. What does the old criterion give on T60's data? What does the new
  one give on the earlier runs, where it can be reconstructed?
- Is the band used for the memoryless check right for the sample size? Recompute it. Does the text of the
  registration agree with the function it calls, and does any cell sit near either limit?
- The wait is read every five sweeps. Does that rounding matter to the check?
- **Does the check have power?** Simulate waits from a plausible non-memoryless alternative (for example a mixture
  of two populations, or a minimum dwell before leaving) at 120 decays a cell, and report how often the registered
  check would catch it. A test that cannot fail tells us nothing.
- List the forks: the other reasonable ways a fourth run could have been scored. Would the verdict survive each?

### D. Do the criteria mean what the words say?

Two of the three criteria are counts of a per-vertex square-count signature and of a largest connected component,
taken at snapshots. `docs/papers/measurement_scope.md` records limits that an earlier review placed on what such
counts establish. Does T60's verdict label claim more than its measurements support? Would the paper's wording,
if it quoted the label, mislead a physicist?

### E. The size claim

One size was held out and predicted from the four smaller ones before it ran (rule 14).

- Is the recipe a real prediction, one that could have failed? Or are its ranges so wide that almost any outcome
  counts as predicted? Quantify it.
- How does each criterion trend with size inside the map? What does a defensible extrapolation say about tubes
  much longer than 288? Other runs in `results/` used far longer tubes under other protocols (T37, T51); consult
  them if they bear on it.
- Name the cheapest additional run or calculation most likely to break the size claim.

### F. The rest of the paper, in the same spirit

Take each claim in the abstract and the closing section of `paper.tex`. For each, name the cheapest way to show
it wrong; do the cheap ones. Targets worth your time:

- **The exit count and the first-exit formula** (the paper's Eq. for the mean first-exit time, with its two
  kinds of exit and how many of each the chain offers per sweep). Verify the count by your own enumeration at one
  size. Check the claim that the waiting torus's neutral family makes the first exit exactly memoryless
  (`scripts/analyse_curled_revision.py --neutral` is ours; write your own).
- **The move-by-move timing runs** (PREREGISTRATION T58 and T59; `scripts/run_first_exits.py`,
  `src/graphity/exits.py`, `scripts/analyse_t59.py`). Is the paper's account of why a five-sweep reading runs late
  the only one the data allow?
- **The sealed threshold** (energy-conserving runs with a reservoir; the escape budget and the enumeration behind
  its lower bound).
- **What the end states are.** The paper says a conversion ends on a flat torus and that growth of both periods
  has not been measured. Measure it. From the saved final graphs, determine what an exactly flat end state is as
  a graph, not by its counts, and how that depends on size. Then say whether the paper's words for the product of
  the change, in both editions, are words you would sign.
- **Retrospective readings.** Where the paper leans on an analysis made after the data were seen (ASSUMPTIONS
  O109 is one), is it labeled as such and given no more weight than that?
- **Wording.** Any sentence that says something has not been studied or found, without a search note in
  `docs/reading/notes/` behind it (rule 15). Any place the model at λ ≠ 1 is called combinatorial quantum gravity
  (only λ = 1 is the published model). Any place the plain-language edition says more than the technical paper.

### G. What should the paper say?

1. The strongest sentence about the λ map that you would sign.
2. A sentence about it that you would refuse to sign, and why.
3. What result, had you found it, would mean no sentence about T60 should be added at all. Did you find it?
4. The changes you consider necessary before the paper is shown to a physicist, most important first.

## 4. Orientation, so you do not lose an hour

Definitions only; verify them against `src/graphity/cqg.py` and `docs/papers/glossary.md`.

- A state is a 4-regular bipartite graph on N vertices in which no two vertices share more than two neighbors.
  S is its number of squares (4-cycles). An edge carrying more than two squares has surplus; X is the total surplus.
- The energy is H = 16(N − S) + 4λX. Only λ = 1 is the published model (combinatorial quantum gravity; Trugenberger,
  Kelly and Biancalana). The paper's runs are at λ > 1, in a family next to it.
- "The tube" or "curled torus" is a 4 × L torus (N = 4L). "Flat" is a torus with both sides at least 6.
- The chain proposes switches of two edges; one sweep is 2N proposals; g is the coupling, used like a temperature.
- d(v) is the number of the six pairs of edges at v that close no square.
- Setup: `pip install -e ".[dev]"`, Python 3.10 or later. `pytest` takes about ten minutes. No network is needed.
- T60's stage 1 is 28 CSVs and 3,360 saved graphs; reading them all takes minutes, not hours. You do not need to
  rerun the simulations to answer anything above except the one-cell reproduction in B.
- An earlier outside review (9 October, a different model) is in `author_feedback_2026-10-09.md` beside this
  file, with our responses in `feedback_resolution_2026-10-09.md`. It predates T58 to T60. Read it last.

## 5. What to hand back

One Markdown report, in your own words:

- At the top: the model and version you are, the date, the commit hash you reviewed, and roughly how long you spent.
- **Your blind verdicts for section A, in a table beside ours**, with every difference explained.
- Findings, most serious first, each marked **BLOCKER** (the paper or the T60 sentence must not go out until it is
  fixed), **SHOULD FIX**, or **NOTE**. For each: the claim, the evidence (file and line, commit hash, the command
  that reproduces it), and how sure you are.
- Your answers to section G.
- What you did not check, and anything you took from our narrative and not from data.

The report will be entered in the project's record as it stands, with a note of what it found and what it got
wrong. The owner decides what changes.
