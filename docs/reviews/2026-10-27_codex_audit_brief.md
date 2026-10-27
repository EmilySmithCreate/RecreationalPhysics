# Brief for a fresh reader: the record of 26 to 27 October 2026 (the held-out readings of T71 and T74, the ledger check, the hard-rule move counts, the row segment, the guard fix)

*Written 27 October 2026 for a reviewer who starts with no history of this work (CLAUDE.md rules 12 and 22). The owner,
Emily Smith, will start the session and pass this page to you. You are meant to be a different model from the one that
wrote the record (Claude); Codex is the intended reader. Four earlier briefs covered the record up to VISION Update 128;
their reports are in `docs/reviews/`, and the fourth is recorded as ASSUMPTIONS O159. You may read them, but write your
own findings first. This brief has two parts, and the first is to be done blind: it names what not to read until it is
finished.*

## Who you are and what you may do

You are a fresh, skeptical reader of a hobbyist physics research programme. You have not seen the conversations that
produced its record. **Work read-only:** do not edit, commit or push anything in the repository. You may run the
repository's scripts and tests. The sandbox scripts write only to `sandbox/out/`, which is not tracked, so you will have
to regenerate any output you want to check unless it is still on the machine. Do not run anything that writes to
`results/`. Return your report as your final message, in Markdown; the owner will save it as
`docs/reviews/2026-10-27_codex_report.md`, and the next working session will record it as ASSUMPTIONS O163 (rule 12).

**Repository:** `https://github.com/EmilySmithCreate/RecreationalPhysics`, branch `claude/particle-sector-2026-10-24`,
**at commit `9f43c2a4`** (full `9f43c2a49e88e6d3bf26ea2ea77b0554918bc2f3`). This brief is committed just after it; read
nothing else from later commits. The record of 26 October up to Update 128 was audited (O159) and corrected in place;
the record from Update 129 on, and everything dated 27 October, has had no audit.

**Setup:** Python 3.10+, `pip install -e ".[dev]"`, then run scripts with `PYTHONPATH=src:scripts` (on Windows
`"src;scripts"`). The tests that cover the code used here (`tests/test_layer_feed.py`, `test_layer_feed_guard.py`,
`test_contraction.py`, `test_t71_heldout_numbers.py`, `test_t74_heldout.py`, `test_t71_t74_ledger_checks.py`,
`test_read_t71_births.py`) take a few minutes; the full suite takes about fifteen minutes and you do not need it.
Running costs: the two held-out scorers and the per-birth reader take seconds; the ledger checks a few minutes, and
their `--null` bucket longer (it replays every birth of 162 cells). The row-segment look takes seconds, the size census
minutes, the triples look about five minutes on eight cores. The restricted four-switch count took about eighty minutes
on twelve cores; its saved rows may still be on the machine under `sandbox/out/hard_rule_quads/restricted_rows/`
(untracked), and the classifier runs on them in seconds. The cube-face and vertex-link looks read the push look's
saved end states (`sandbox/out/pair_tie_push/`, untracked, about four hours of CPU to regenerate); if they are absent,
run those two looks on the tori only.

**Read first:** `CLAUDE.md` (the rules; especially 1, 4 to 7, 10 to 17 and 19 to 22) and the top of `VISION.md` (the
hypothesis, claims 1 to 6, and the bar).

## Part A, blind: five questions on the held-out stages and the guard fix

Do this part **before** reading ASSUMPTIONS O160, O161 and O162, VISION Updates 130 and 131, the two sections of
`PREREGISTRATION.md` headed "Reading of T71 at the held-out size L = 16" and "Reading of T74 at the held-out size
L = 16", `docs/HANDOFF_2026-10-26.md`, `docs/design/next_experiments_2026-10-26.md` and
`docs/design/two_stories_brief_2026-10-26.md`. Write your answers down, then go on to Part B. The blindness is by
instruction, not by a pin: say in your report whether you kept to it.

What you may read for Part A: `PREREGISTRATION.md` section T71 through Amendment 4 and section T74 through Amendment 6
(both written before their L = 16 runs; the "Reading" subsections that follow each are what you must not read yet);
`configs/t71_heldout_prediction.csv` and `configs/t74_heldout_prediction.json`; the drafts in
`sandbox/heldout_2026-10-23/`; the scripts `scripts/t71_heldout_score.py`, `scripts/t74_heldout_score.py`,
`scripts/make_t74_configs.py`, `scripts/read_t71_births.py`, `scripts/analyse_t74.py`; the result files
`results/t71_{model,layer,layerref}_lam{110,125,140}_l16.csv` (nine) and `results/t74_*_L16_*.csv` (54) with their
`.meta.json`; `src/graphity/layer_feed.py`, `src/graphity/contraction.py` and their tests; the git history of all of
these (`git log --format='%H %cI %s' -- <path>`).

1. **Is T74's size claim an arithmetic identity?** Read how the feed, the cap and the gate scale with the slab
   (`make_t74_configs.py`; the T74 registration's definitions) and how many layer proposals are made a sweep. If every
   quantity that sets the period between births is proportional to N_slab, what does a third size test that two sizes
   did not? State what the held-out stage at L = 16 could show and what it could not, in your own words, before you
   read the record's own statement of it.
2. **Could the L = 16 files have shaped the prediction?** Check whether `scripts/t74_heldout_score.py` or
   `configs/t74_heldout_prediction.json` was written or changed after any L = 16 result existed: commit times of the
   prediction file, the scorer and the 54 result files; the drafts in `sandbox/heldout_2026-10-23/` against the committed
   prediction file (rerun the drafting script if there is one and compare); whether the scorer reads anything from the
   data that could move a range. There is no commit hash in `.meta.json` yet (TASKS, 6 October, item 5), so timestamps
   and diffs are the only evidence; say how strong that evidence is.
3. **Are the ranges' coverage claims consistent with the observed miss rate?** For each pooled period at L = 16, how
   wide is the registered range against the spread between replicas and against the distance from the fit? At stage 1
   (L = 8 and 12), how many of the same quantities fell inside the same kind of range? Could a period plausibly have
   fallen outside, or are the ranges wide enough that "inside" was close to certain? The same question for T71's 152
   numbers and words (`configs/t71_heldout_prediction.csv`): how many are size-independent arithmetic, and how many
   could have failed.
4. **Does the per-birth reader count the first logged row?** Run `scripts/read_t71_births.py` on the T71 files for
   λ = 1.10, r = 1/16 at L = 8 and L = 12 (the two clean-switch cells) and say whether it gives 5,148 and 4,620 births
   (the fourth audit's own counts) and what it reports for births above one curling cost (a N_slab). Then read its
   test.
5. **Is the guard fix complete?** `layer_feed.py` now has `can_pay(pool, bill)`; a threshold at the gate keeps a 1e-12
   tolerance; `contraction.run_feed` was changed in one line. Across every release mode (`release_to` of "stores" and
   "twins", the paid contraction, the split, the gate), can any store go below zero now, and could it before? Does the
   kept 1e-12 at the gate ever spend energy? Did the fix change the output of a registered run: rerun one stage-1
   replica of T71 or T74 from its config with the current code and compare it row for row with the committed CSV
   (do not write into `results/`). Say whether the four tests in `tests/test_layer_feed_guard.py` would have failed on
   the old guard.

## Part B: the record of 26 to 27 October

### The question

From the evening of 26 October to the morning of 27 October the record did six things:

- read T71 and T74 at their held-out size L = 16 against numbers written from L = 8 and 12 beforehand (rule 14), and
  recorded the words AS PREDICTED and HOLDS AT L = 16, with REPEATS STAGE 1 for T74's secondary reads (O160, O161,
  Updates 130, 131);
- read, exactly and with no run, whether the fed slab's burp is anything beyond the ledger's bookkeeping, building a
  graph-free "bucket" that is compared birth for birth with the registered files (O162;
  `scripts/t71_t74_ledger_checks.py`);
- ran six sandbox looks on the owner's hard rule (the square count held at 3N with six links, at N with four): whether
  any compound move of up to four switches takes clean flat space anywhere, by a cube-face reading, a vertex-link
  count, a four-link size census with a held-out size inside the look, a triples count, a four-switch count in a seam
  window and in a restricted word, and a classifier of what the count found (LOG lines of 26 and 27 October);
- at the owner's reading of that count's closing line, built and read a row segment inserted between two existing flaws
  (`sandbox/row_segment_look.py`, 27 October), with her prediction recorded first;
- fixed the layer form's affordability guard after both held-out stages were read (O158 addendum of 27 October);
- wrote two design briefs for her (`docs/design/next_experiments_2026-10-26.md`,
  `docs/design/two_stories_brief_2026-10-26.md`), recorded the fourth audit (O159, Update 129), and republished the
  programme page five times (Versions 128 to 132; copy in `docs/public/programme.html`) with every statement of the
  assistant's labelled "Fable".

The record's own headline words, which are what you are checking and not what you should take as true: both held-out
stages hold; the burp's births, timing and energies are the bucket's and the wiring adds only a rare clean move at
λ = 1.10; no count-keeping move of up to four switches, local to one neighborhood, takes clean six-link space anywhere
(every form found is two points renamed); in four links the only count-keeping moves out of clean space are
wrap-around effects of a short side; a segment between two existing end flaws lengthens at no cost, the end flaw costing
21 a position.

**Your job: find what is wrong.** Assume there are errors in the code, the arithmetic, the enumeration, the attribution
of ideas, the labelling of statements (rule 10: exact, measured, interpretation, hers), the sandbox discipline (rule 16:
a look can kill a claim but never crown it; its words are declared before it runs; a look says whether its starting
state obeys every rule she has adopted) and the process, and look for them. A clean bill is a possible answer, but it
should be earned.

### What to read

1. `VISION.md`, **Updates 129 to 131**; Update 129 is the record of the fourth audit (check it against
   `docs/reviews/2026-10-26_codex_report.md` and ASSUMPTIONS **O159**), and the in-place corrections marked "O159" in
   Updates 124, 125, 127 and 128. Note that 27 October has no VISION update: its results are in the LOG, the notebook,
   the handoff, an O158 addendum and the page.
2. `sandbox/NOTEBOOK.md`, entries dated 2026-10-26 from 22:37 UTC on, and 2026-10-27: her words, verbatim.
3. `sandbox/LOG.md`, the lines dated 2026-10-26 from `cube_face_look.py` on, and the three dated 2026-10-27.
4. `docs/HANDOFF_2026-10-26.md`, all of it, including the sections appended after the one-hour session.
5. ASSUMPTIONS **O158** with its addenda of 26 and 27 October, **O159**, **O160**, **O161**, **O162**.
6. `PREREGISTRATION.md`: T71 Amendment 4 and its "Reading at the held-out size L = 16"; T74 Amendments 5 and 6 and its
   "Reading at the held-out size L = 16".
7. The sandbox looks: `sandbox/cube_face_look.py`, `hard_rule_triples_look.py`, `vertex_link_look.py`,
   `hard_rule_size_census_look.py`, `hard_rule_quads_look.py` (its `--seam`, `--restricted`, `--rows`, `--sum` and
   `--slice` modes), `hard_rule_quads_classify.py`, `row_segment_look.py`; and the corrected
   `hard_rule_pairs_look.py` they build on.
8. The readers and the code: `scripts/t71_heldout_score.py`, `t74_heldout_score.py`, `t71_t74_ledger_checks.py`,
   `read_t71_births.py`, `make_t74_configs.py`; `src/graphity/layer_feed.py`, `contraction.py`, `cqg_d.py`
   (the six-link model, H = 16(3N − S) + 4λX, and its switch move), `cqg.py` (four links), `dimension.py`.
9. The two briefs, `docs/design/next_experiments_2026-10-26.md` and `docs/design/two_stories_brief_2026-10-26.md`,
   and the three reading notes `docs/reading/notes/2026-10-26_*.md`.
10. `docs/design/owner_questions_2026-10-24.md`, Q1 to Q4 at the top, and `docs/public/programme.html` (search for
    `who fable`).

### What to check

Write each finding with where it is, what is wrong, what is right, how you know (a computation you ran, a source, an
argument), and how sure you are. Cover at least:

1. **The held-out readings as recorded.** Rerun both scorers and compare every number and word in O160, O161 and the
   two pre-registration readings with their output. Is "her prediction is ours, so the run cannot separate her picture
   from ours" right for each (T71 Amendment 4; T74 Amendment 5), and is it said everywhere the verdict is quoted? Is
   the correction in Update 130 (her "Confirm" of 25 October did not cover the T74 go-ahead; her go-ahead is of
   26 October) supported by the notebook and the predictions sheet? Was the L = 16 code stage 1's (O160 says a stage-1
   replica rerun reproduced its rows; check one)? Compare your Part A answers with what the record says about what
   the held-out stage tested.
2. **The ledger reading (O162).** Check the identity it states at a sample of births; the definition of the
   wiring-free share; the bucket null (does `--null` reproduce 1,708 of 1,728 stage-1 replicas and 793 of 864 at
   L = 16, and is every non-reproduced replica explained as the entry says: a clean move, or a pool-equals-gate tie
   resolved by the registered code's 1e-12 tolerance); the memoryless test (its null, its seed, its power); the
   per-birth switches against N (the exponent w and its interval; is "UNDECIDED" the declared word?); the note about
   `contract_layers` at x0 = w − 1 (is it right, and does the null copy it faithfully?); whether "no graph mechanism for
   the burp" is labelled ours and crowns nothing; and whether the item's prediction is correctly attributed (her words
   of 22:42 UTC, "Agre with your hypothesis", against item 4's "Ours" paragraph as it stood then: check the commit that
   added the paragraph against the notebook's time).
3. **The hard-rule counts as enumerations.** For each: is the search complete for the word it claims; is the prune
   exact (a switch's largest possible gain in squares under the hard-core rule); is the undo excluded in both written
   forms; are "returns the start edge set" and "renaming" tested exactly (edge sets; the transposition test's
   neighbor-set identity; networkx isomorphism) and is "real move" the complement of both; are the counts the LOG
   quotes reproducible (3,514 first switches; 715,453,184 third switches and 0 restoring triples; 407,171,104 third and
   15,639,347,840 fourth switches, 8,174,640 back to the start, FOUND 9,216, all transpositions on 60 pairs)? What
   exactly is the "restricted word" (every switch's points within one link of the first switch's four), what does it
   exclude, and is the LOG's statement of what remains open (the exhaustive word, five or more switches, non-local
   moves) complete? Is the estimate of the exhaustive count (about 9 × 10¹⁰ trials) sound? In the size census, was the
   L = 12 prediction written before L = 12 ran (the look says a time; check the commit), and is "a wrap-around effect
   needing (L − 4)/2 parallel switches" shown or inferred? Is the reread of the 16 × 10 seam move as a wrap effect
   consistent with the triples look's description of the same move?
4. **The cube-face and vertex-link looks.** Is the claim that every 4-cycle of the rod is a face of a 3-cube subgraph
   right, and does it make the defects note's check 1 ill posed by wiring at side 4? Is C = N on the flat torus and
   C = 2N on the rod right, and what is "C"? In the vertex-link look, is the link graph's definition exact (edges with
   multiplicity equal to squares through the point and a neighbor), is "ALL OCTAHEDRA" the right word for a flat
   point, and is the stacked sphere identified correctly? Were the starting states' rule status stated, as the O159
   section of TASKS asks?
5. **The row-segment look.** Is the construction what the docstring says (a double row inserted over k positions; the
   canonical end closure; parity of the two kinds)? Is every state it reads valid under the hard-core rule, and does
   the reader check validity? The declared word was CLEAN SEGMENT or FLAWED; the look returned FLAWED and the LOG then
   reports "in substance exact within scope" with the reasons given as the reader's own (its range reached the wrap;
   it failed a lone pair outside her claim). Is that a fair report of a look under rule 16, or a word reworded after
   the fact? Check the numbers (H = 42 and 8 off-flat points for 2 ≤ k ≤ L − 4 at 16 × 10 and 24 × 12; H = 252 and 48
   on the 12 × 6 × 8 strip; 21 a position; 42 equal to the cheapest lone pair of 20 October; the canonical closure the
   cheapest of 21 single cuts tried, 53 next). Is "the end flaw is a dislocation" (four points at local dimension 3 in
   two directions, a line of 24 at dimension 4 in three) a reading or a name given from a count (CLAUDE.md: read
   positions before naming a geometry)? Is the attribution right: her idea of 20 October (VISION Update 75), her
   reading of 02:51 UTC, her prediction of 03:02 UTC, the "ours, exact: this is locality" sentence?
6. **Her words against our readings.** Any reading of the assistant's presented as her decision; any decision recorded
   that she did not make; any of her words misquoted, cut or dropped; any assistant conclusion listed among her
   answers. In particular:
   - her three messages of 22:37, 22:41 and 22:42 UTC on 26 October: what each quoted from the page or the program,
     what each added, and what was acted on as "her word" (the four-switch count; item 3; item 4's prediction);
   - whether "a four-switch seam move exists" is recorded as Fable's hypothesis that she agreed with, or as hers;
   - her two messages of 27 October (02:51 and 03:02 UTC) and the notebook's "Fable" glosses under them;
   - the programme page: is every statement of the assistant's labelled "Fable", is any statement of hers labelled as
     the assistant's or the reverse, and does the page say anything a look cannot support (rule 16 (a))?
7. **The O159 record.** Does ASSUMPTIONS O159 report the fourth audit fairly, including what it got wrong (it says
   nothing was found wrong)? Are the in-place corrections in Updates 124, 125, 127 and 128 right and complete against
   the report's findings F1 to F37? Was anything in the report left out of the record?
8. **Process.** Rule 16: starting states and their rule status stated in each look's docstring; words declared before
   running (check the commit order: a look committed "running" before its reading). Rule 17: the row-segment and
   four-switch results are written in the LOG, the handoff, the notebook and the page; is any of those a second full
   home? Rule 22: 26 October carries Updates 125 to 131 and 27 October none; was the choice to leave 27 October in the
   LOG and the handoff right? Rule 14 inside a look (the size census): does a held-out prediction inside a sandbox look
   mean anything, and is it presented as a measurement anywhere? Clock times: the record says `date` is run before any
   time is written; the handoff corrected one (23:27 to 23:25 UTC); check the commit times against the times written.
   The next-experiments brief's item 12 said this audit would be recorded as O162; O162 was used for the ledger
   reading, so it will be O163; note any other number or cross-reference that has drifted. Anything in the two briefs
   or the reading notes that is decided rather than proposed.
9. **Physics and mathematics from memory.** Each was written in the two briefs, the reading notes and the LOG, and
   should be marked "general knowledge, to verify" where it was not read: kinetically constrained models and what is
   known of their ergodicity (Ritort and Sollich 2003; Fredrickson and Andersen 1984; Kawasaki 1966); Nishimura 2017
   ([Swap17]) on fixed triangle counts needing moves of 8 or more links; the Gauss–Bonnet reading of curl and
   anticurl (Bowick and Giomi 2009); dislocations and disclinations and their energy per length; Costeniuc et al. 2006
   on when a soft constraint equals a hard one; Jaffe 2005 on the Casimir force. Check each is stated correctly.

### What to return

A single Markdown report, in plain American English (the owner is a software engineer, not a physicist; define terms):

1. **Summary** (ten lines at most): the most important things to fix, in order.
2. **Part A answers**, as written before you read the record, then a line each on how they compare with the record.
3. **Findings**, numbered, under the nine headings above, each with where, what, what is right, how you know, and how
   sure you are.
4. **What you ran:** each script or test, with its output where it disagrees with the record.
5. **Missing published work:** the published models, theorems or measurements most relevant here, with authors and
   years, "to verify" where unsure. Topics: ergodicity of count-preserving switch moves on regular graphs, and known
   cases where a conserved count splits the state space into compartments; dislocation lines in lattices and their
   energy per unit length; feed-and-gate (reservoir, cap, threshold) accounting models whose period is set by
   construction, and how such a model is told from a mechanism; growth of a lattice by inserting rows or planes. Her
   stated aim is to apply existing mathematics to her ideas, so a good match is welcome news.

Do not write "nobody has done X"; write "I did not find X" and say where you looked. Mark anything you did not check at
its source as such.

### What not to do

Do not propose new mechanisms for her hypothesis and do not rewrite her ideas; judge what was recorded, computed,
coded, run and answered. Do not read commits after the one named above (this brief excepted). Do not change any file.
Do not read the Part A exclusions until Part A is written.
