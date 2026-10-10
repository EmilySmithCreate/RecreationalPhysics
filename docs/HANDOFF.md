# Start here: handoff for the next assistant (state as of 2026-10-09, 05:10 ET by the clock; dated addenda below)

**Current interpretation, 9 October 2026:** read [the curled-torus measurement scope](papers/measurement_scope.md)
before reusing the historical claims below. Square counts do not certify geometry or a unique
front; `bath_T` is mean store energy; the seed scan measures escape; the persistence edge is
operational. O108 and the methods supplement give the evidence. Original dated predictions,
scores and failed tests remain on record; their stronger interpretations are superseded.

Written for the AI assistant that opens this repository next. Emily is the owner; she reads it too. It is
newer than `CLAUDE.md`'s "Known state". **Section 0 is the current state; the dated addenda under it are history,
newest first, kept because the record refers to them.** Sessions may share one working tree: add files by name, never
`git add -A`, and never switch branches under another session. `main` is current as of 8 October (PR #42) and Emily
merges; work goes on a fresh branch off `main` (on 9 October, `claude/read-t51-t53-2026-10-09`). The branch
`claude/vision-programme-updates-9sje7s`, which carried the record from 26 September to 8 October, is merged and deleted.

## Paper materials for readers

The current manuscript is `papers/curled_torus/paper.pdf`, with `supplement.md` and
`release_manifest.json` alongside it. It is an unpublished first-release manuscript; do not
describe it as published or scientifically endorsed. The 9 October corrections and dependent
document review are on `review/curled-torus-feedback-2026-10-09`. Historical submission and
endorsement logistics below are not evidence of scientific review. T38 is already read (O84);
its missing detector crossings must not be treated as unconverted survivors. Outstanding
work is the mechanism, not another claim of universal exponential conversion waits.

**Addendum, 10 October 2026 (branch `claude/paper1-plain-language-2026-10-10`, cut from the review
branch; written 07:20 ET by the clock).**
- **The plain-language edition of paper 1** is `papers/curled_torus/paper_plain_language.pdf` (source `.tex`,
  notes in `plain_language_README.md`), rewritten through the day from the owner's page-by-page notes. Her rules
  for such an edition: no term before it is defined; results in reading order; a diagram with callouts wherever
  the reader would have to build a picture; one metaphor per idea; everyday comparisons; her idea stated once.
  It has eleven chapters and ends on two upcoming papers and one line: "A push of twelve units opens a tube.
  What opens a space?"
- **Its interactive companion** is the artifact "The Tube's Curling Ladder",
  https://claude.ai/artifact/F4sBf955J5ZT7rCq8uebW8 (source `docs/public/curling_ladder_tube.html`; shared by the
  owner by link). It has not been seen rendered by the assistant that wrote it; its script was checked at every
  knob setting. The older artifact "The Curling Ladder" still shows the order-of-opening release chart set aside
  in VISION Update 50 and is owed a revision if it becomes the three-direction version.
- **The long waits (O109).** Read retrospectively from the saved rows (`scripts/read_wait_detector.py`;
  exploratory, no new run): T38's 190 missed detections, T24's two extreme waits and the fast share are tubes that
  converted inside the detector's 200-sweep resting window, and T38's yardstick was biased by them. The
  pre-registered verdict TWO POPULATIONS stands as scored. Three waits at λ = 1.30, N = 64 are unexplained.
- **The technical manuscript** was reordered to the plain edition's order at the owner's instruction (model; cost
  of leaving; first exit; conversion; sealed system; dependence on λ) and carries the O109 reading. Passages were
  moved, not reworded, except those on the detected tails. `python scripts/build_curled_paper.py` was rerun: the
  manifest's hashes are current.
- **A fresh prior-work search** for the coefficient above 1 is `reading/notes/2026-10-10_prior_work_lambda_above_one.md`
  (NOT FOUND for any finite λ above 1; a ban on surplus squares is described in the text of [KTB19] and [KT19];
  its quotations are from web conversions and are to be checked against the PDFs).
- **Owed to or by the owner.** Her prediction, then a pre-registered replay of the three T38 waits from their
  seeds (threshold and every exit and return recorded). The far tail at λ = 1.05 read the same way. A physicist's
  glance at the edition's one-paragraph description of Coleman's bounce, which is from general knowledge. Whether
  a paper on converting the model's units is added to the series (the edition says "a later paper").
- **The main checkout** was left on the stale `claude/read-t51-t53-2026-10-09` with uncommitted duplicates of this
  branch's work (ASSUMPTIONS, TASKS, REFERENCES and the new files); this branch is the source of truth for them.
- **T58, pre-registered 10 October, 07:47 ET, and run on the laptop** (`scripts/make_t58_configs.py`,
  `scripts/analyse_t58.py`): the replay owed above, with the owner's idea of that morning as her prediction (the
  three tubes curled a second direction and the energy sat in the new curl; ASSUMPTIONS O110) and ours (their own
  detectors' thresholds). Her "maybe" is recorded as her prediction until she confirms or replaces it. *Confirmed by her as her
  prediction on 10 October, 11:45 ET, after both readings; the verdict (it fails) is unchanged.*
  **Looked at sweep by sweep the same day, at her question (exploratory; O110, addendum of 12:22 ET;
  `configs/t58_exploratory_sweeps_lam130_n64.json`, `scripts/read_t58_sweeps.py`):** no second curl at any
  sweep in the nine traced decays, and no single switch of a tube adds a square (exact, from the neutral-class
  census already on the record); a waiting tube makes a neutral re-gluing switch about every two sweeps and stays
  a tube with the same ways out; decay 2748 sat at every sweep, decay 3072 made a three-sweep exit between
  two looks (sweeps 3,166 to 3,168). **One long wait is left in the cell, of the size chance produces, not two.**
  *Corrected at her word the same day:* the two papers and the supplement now say one tube sat and one made an
  exit between two looks; PDFs and blog pages rebuilt, and the folder copied to the marketing branch again.
  **Read the same day:** gates passed; no second curl in any of 4,000 tubes; of the three waits one was the
  detector and two were real waits of the perfect tube (11 to 12 times the mean); with no detector the first exit
  is one memoryless population at 1.07 of the counted rate. Her follow-up (does a knot turn back into tube; why
  not a closed system) is answered exactly in O110: a knot above λ = 1 runs downhill to tube-like points, so no
  box can hold it (`scripts/exact_knot_descent.py`).
- **Later the same morning (written 09:12 ET by the clock), all at the owner's instruction.**
  - *The technical manuscript, plain-wording pass:* simpler statements carrying the plain edition's ideas (the
    energy as a price list, the push, the opened door that is not a departure, enough room or not, the scrap), at
    the same page count (10; six lines longer than before, which is the replay's result and its limits). Two
    small tables became sentences; the per-cell
    numbers of the detector reading and the illustrative rarity bounds moved to the supplement; the Introduction's
    roadmap sentence went. The abstract lost the detector sentences at her instruction; "All three registered
    conversion maps remain inconclusive" was kept (rule 7) and she may still cut it. **A fresh read-only agent
    compared the text before and after for any changed claim** and found no wrong number, formula, label or
    cross-reference, but five added sentences that asserted more than the original, six strengthened phrasings
    and seven dropped caveats, and replay wording without the limits its registered readings carry. All were
    corrected the same morning: the added interpretive sentences removed or qualified ("a necessary condition
    for a change that starts locally"; "measured waits would exceed Eq. (2)"; the "sharp change" rationale for
    the pre-registration; "the detector does not see the first exit"; "metastable" without the enumerated
    sizes), the hedges restored, the per-cell numbers of the detector reading put back, and the replay stated
    as one cell, by counting signature, at five-sweep blocks, 7 % and four standard errors off the count, with
    the two real waits called rare and unexplained. The lesson for the next pass: a gloss borrowed from the
    plain edition is a claim, and is checked like one.
  - *Source numbers:* a number now means the same source in both editions. The plain edition's sources 1 to 8 are
    the technical paper's reference list, 9 to 12 its own. `REFERENCES.bib` gained T17 and Creutz83, both marked
    not read, titles to verify.
  - *The two editions as web pages ("the Side Nerd Blog"):* `docs/public/mainnerd/` (a front page, the plain
    edition at `01thecurledtorusburpsPL/`, the technical one at `01thecurledtorusburps/`, `assets/`), generated
    from the LaTeX by `scripts/build_main_nerd_pages.py` with `main_nerd_latex.py` (converter),
    `main_nerd_site.py` (the frame: a 1990s home page in Side Nerd's colors, advertisements for Side Nerd,
    question headings, quick answers, glossary, guestbook, JSON-LD, UTM links) and `make_main_nerd_assets.py`
    (the cow GIF she supplied, cropped; the share image). Chapters and sections link to each other across the two
    pages. Each edition's footer has "all posts | next post"; until a second post exists "next post" lands on a
    placeholder (`comingsoon/`, "not up yet", noindex), and a second post replaces `SOON` in `NEXT_POST`. Two of
    the plain page's advertisements show Ither on a phone in the logo's place (cut by the stylesheet out of the
    site's one Ither picture, the three-phone hero); the cow is on the two editions and not on the front page
    (her notes of 10 October). The interactive companion is hosted on the blog as well
    (`01thecurledtorusburpsKnobs/`, built whole and unchanged from `docs/public/curling_ladder_tube.html`, which is
    byte for byte what the Claude artifact was published from); the editions' web pages link to that copy, the
    PDFs still to the artifact.
    At her instruction of the same day the folder was copied, file for file, to `sites/sidenerdapps/mainnerd/`
    on a new pushed branch of the SideNerdMarketing repository, `feat/sidenerdapps-main-nerd-blog` (commit
    `4522930`), with the sitemap entries. She merged that first copy into the marketing `main` the same day
    (pull request 56). After the correction to both editions (one long wait, not two) the folder was copied to
    the same branch again (commit `17acde2`, pushed after the merge), so **the marketing `main` holds the first
    copy and the correction needs a second pull request; nothing deployed** as of that push. Copy again after any
    rebuild;
    `docs/public/mainnerd_PORTING.md` has the steps and the cautions (root-absolute links; no analytics on
    that site yet, so the UTMs record nothing; do not deploy from a stale checkout). Her addresses were typed
    "...01thecurledtourusburps"; the pages are built with "torus", and asked which she wanted she said to spell
    it as mathematics and the source papers do, so "torus" stands (one constant, `SLUG`). The first build of the morning was at `/ownedmediaphysics/`, the second was "Primary Nerd" at
    `/primarynerd/`; she renamed the blog **Main Nerd** (`/mainnerd/`) the same day, and the scripts, test and
    notes carry that name.
  - *Her notes on the pages, the same morning, applied:* the masthead is "Welcome to the Side Nerd Blog, Main
    Nerd" (first "Primary Nerd") and the papers are posts; each chapter opens with a commonly searched question ("What was there before
    the Big Bang?") and an answer that claims nothing the paper does not; advertisements are labelled with the
    one word and carry the Side Nerd logo; a call for a scientist to volunteer as a reader opens an e-mail to
    her; a guestbook form sends entries by e-mail; the PDFs ship with the pages because the GitHub links point
    at `main`, which lacks this branch's files until it is merged.
  - *Uncommitted when this was written:* the two papers, the web pages and their scripts, awaiting her review.
    T58 and its record are committed.
- **Next record numbers:** ASSUMPTIONS **O111**, VISION **Update 52**, PREREGISTRATION **T59**.

## 0. The first ten minutes (as of 9 October 2026)

1. **Fetch first.** `git fetch --all --prune`, then `git log --oneline -8 origin/main` and `git branch -a`. On 5 October
   the working copy was 40 commits behind the record; on 9 October its branch had been merged and deleted on GitHub.
   Start a fresh branch from `origin/main`; never commit on `main`. `gh` is not installed; Emily opens the pull request
   from `https://github.com/EmilySmithCreate/RecreationalPhysics/compare/main...<branch>`.
2. **Run `date` before writing any clock time** (CLAUDE.md, "Added 2026-10-05", item 6). Guessed times have been wrong
   three times. Next record numbers (as of 9 October, 06:35 ET): ASSUMPTIONS **O109**, VISION **Update 49**,
   PREREGISTRATION **T57**.
3. **What is running, and how results come in.** Batch jobs are submitted by pushing a manifest in `cloud/queue/` on
   any branch but `main` (`.github/workflows/run_queue.yml`, which skips any config whose result is already in the
   bucket); the queue's state is written to `cloud/status/latest.md` by a workflow. Results come down by adding patterns
   to `cloud/fetch/request.txt` and pushing: the `fetch_results` workflow commits them into `cloud/inbox/` on the same
   branch within minutes; then `git pull --rebase`, `python scripts/accept_inbox.py --move` (checks each run against
   its committed config and moves it into `results/`), commit the data by name, and read with the test's analyzer.
   **Running on 9 October:** one resubmitted T53 cell (`t53_l72_lam125_g30`, `cloud/queue/2026-10-09_t53_resubmit.txt`;
   about thirteen hours); and T52 (the hidden count) on the laptop, restarted at 05:12 ET with the runner's new
   `--resume` (its 5 October run had died at 66 rows), log in the session scratchpad; it has days to go, no verdict
   until it finishes. **T56 stage 1, launched 06:43 ET** on the owner's prediction ("opens into one flat space"):
   68 Batch jobs (`cloud/queue/2026-10-09_t56_stage1.txt`; the slab and the rod in a warm bath under her tie "all at
   the last", with four untied controls), the longest about seven hours. To read: `t56_*` in `cloud/fetch/request.txt`,
   accept, `python scripts/analyse_t56.py`; then write the held-out prediction as a dated amendment under T56 and run
   `python scripts/make_t56_configs.py --held-out` for the 32 stage-2 cells (L = 16 and 72), which run only after that.
   **T57, launched about 07:27 ET** on her prediction (RE-CURLS; VISION Update 51): 16 Batch jobs, T34's protocol
   under her tie with untied controls (`cloud/queue/2026-10-09_t57.txt`); read with `scripts/analyse_t57.py` after
   `t57_*` is fetched and accepted. **T54 stage 1** (L = 8, 12, exact) is computing on the laptop (log in the session
   scratchpad; it writes `results/t54_patch_stage1.csv` when done); then the held-out amendment, then L = 16 by a
   config of its own.
4. **Read on 9 October** (ASSUMPTIONS O104, O105, O107; VISION Updates 46 to 48; the "Reading" subsections of T51,
   T53 and T55; TASKS, the 9 October section): **T51 CLIFF** (the columns heal off a cliff as the cooling slows; P1,
   the fair clock, fails at one point of two; P2 holds); **T53 ADVANCES ONLY** at every (L, λ), **SEVERAL** (the
   spaghetti X opens one direction in a bath and not the second); **T55 KNOT** at both sizes (the pieces no cooling
   removes are an eight-point knot of two kinds of point, in kind O15's twist, and double columns; not scars, not
   seams). The owner's predictions failed in part on all three; rule 11's four answers are in the O entries. **Her
   decisions of the same morning (Update 47):** the tie is "all at the last"; untied runs are a stepping stone; her
   shape for X is the slab (two open, one curled). Exact under that tie: O106 (the slab's wall 30 to 4 for λ = 1.10
   to 1.25 against flat space's 64).
5. **Next, in order** (TASKS, 9 October): T56 launched on her prediction, then read, then its held-out stage; T54's
   script and its exact definitions of "patch" and "grows", untied and under the tie (Amendment 1), then L = 8 and
   12, the L = 16 prediction as a dated amendment, then L = 16; the enumeration of the paths out of each knot (why the
   column heals and the others do not; exploratory unless pre-registered); T53's cell accepted when it lands; then the
   5 and 6 October items (T9; the two extreme T24 waits; the warm sheet's correlation length; the commit hash in
   `.meta.json`; the reading before any citation; the prior-work note for paper 1; the first fresh red-team review
   under rule 12, which another session began on 9 October for paper 1: `docs/papers/curled_torus/
   author_feedback_2026-10-09.md`, untracked, to be checked against the record as O103 did). The programme artifact
   "A Phase-Changing Reality" was republished from the 9 October draft (Versions 58 to 60, 9 October, shortly after
   07:00 ET; Version 59 carries the revised claim of Update 50, confirmed by the owner at 07:33 ET; Version 62 says so).
6. **The rules that changed most recently:** CLAUDE.md rules 10 to 15 (6 and 8 October): four kinds of statement; the
   four questions before any patch, in the form "previous claim → failed because → replacement → new falsification
   test"; a fresh read-only red-team reviewer at each milestone; outside theories as targets; a held-out size for every
   size claim; a written prior-work search behind every "we have not found". PREREGISTRATION's standing requirements of
   8 October apply to every new section.
7. **Read section 3 before writing anything public or anything to a physicist.** The programme page is the Claude
   artifact "A Phase-Changing Reality" (the owner's request of 4 October); its text source is
   `docs/papers/programme_draft.md`, current to 9 October; the artifact was last republished on 6 October and is owed a
   republish from the 9 October draft. `docs/public/programme.html` is older and not maintained by hand.
8. **Environment.** The interpreter with the project's dependencies is the Microsoft Store one,
   `~/AppData/Local/Microsoft/WindowsApps/python3` (NumPy 2.0, Numba, pytest); bare `python` and `.venv` lack NumPy.
   Run `pytest -q > log; echo $?` and read the status; never pipe pytest through `tail`. Long scripts go in a file with
   the Write tool (the shell cuts long heredocs). Background runs: `nohup <py> scripts/... > log 2>&1 &`.

## Addendum, 9 October 2026

- The branch `claude/vision-programme-updates-9sje7s` was merged to `main` on 8 October (PRs #40 to #42) with VISION
  Update 45 (three working methods adopted: a fresh read-only reviewer, a held-out size, a written prior-work search),
  the owner's predictions for T51 (GENTLE), T53 (confirmed) and T54 (CRITICAL PATCH), T54's held-out size (L = 16),
  and paper 1's citation of Kelly's thesis. This page had not been brought up to date since 6 October; section 0 above
  is the rewrite of 9 October, and the section it replaces is kept below as "the first ten minutes as of 25 September".
- T51 and T53 fetched, accepted (120 of 120 pass) and read; `scripts/analyse_t51_amendment3.py` written and tested for
  Amendment 3's reported-not-scored items; T53's failed cell resubmitted; the record updated (O104, O105; Update 46;
  the two readings; TASKS; the programme draft). Details in section 0, item 4.

## 0 (superseded). The first ten minutes, as of 25 September 2026

1. **Two sessions may be working this repository at once.** Run `git status` and `git log -5` before assuming
   the tree is as described, and re-read a file if the tool says it changed on disk.
2. **The owner's direction of 25 September (memory `pace-and-scale`):** run the programme at full speed and scale while
   she is on vacation, many pre-registered tests at once, the cloud used generously, literature read in parallel, still by
   the book. **Running on AWS Batch (25 September, 13:00 ET)**, all submitted by `.github/workflows/run_queue.yml` from
   manifests in `cloud/queue/` (the workflow now reads several queue files per push; it failed on the first such push and
   was fixed, commit 590f6ff): **T34** (two 512-point jobs left), **T37** (34 jobs, many natural seeds in long tubes,
   paper 2; `scripts/analyse_t37.py`), **T38** (48 jobs, the rare long wait, paper 1; `analyse_t38.py`), **T39** (15 jobs,
   the cascade window, six and eight links; `analyse_t39.py`; its eight-link cells are expected to stall, see O62), **T40**
   (11 jobs, the push that starts the change in four directions; `analyse_t40.py`). The compute environment runs 30 jobs at
   once since about 14:50 ET on 25 September (raised with the owner's permission, matching terraform's `max_vcpus = 30`); 30 is the
   account's Fargate quota, and going higher needs a quota request to AWS. **Downloading:** the project account's keys are in the git-ignored `.env`; the 25 September session's
   scratchpad scripts `download_results.ps1` and `check_and_copy.py` load them into their own process, sync the bucket and
   compare each set's recorded config with the committed one before copying into `results/`; `aws_jobs.ps1` counts jobs
   by status, read only. Never print or commit the keys. **Read each finished test with its analyzer** and record it in
   ASSUMPTIONS (next number O63), the pre-registration and the programme page (dated, clock time, US Eastern).
   **Read and recorded on 25 September:** T36 TRANSIENT (O59), the six-link relic search negative (O58), T30 corrected
   (O54: the first direction opened fully in 28 of 84), the walls halve exactly only at one setting (O55), four literature
   reviews (O60; notes in `docs/reading/notes/`), the exact field-on-the-points calculation (O61), T33 NO CASCADE with every
   replica stalled after one move (O62). **T34 at 216 points reads MELTS; its verdict waits for the 512-point cells.**
   **Waiting on the owner:** the gravity rule (`docs/design/gravity_brief.md` section 6: a massless field on the points
   with relics as its sources, recommended; flat space in this family has an energy gap, so no pull at a distance is
   possible without a new ingredient); the exchange sign's convention (O60 (b)); her confirmation of the inferred
   predictions in T36 to T40. **Exploratory pilots of T37 (disclosed in its pre-registration) are in the scratchpad, not
   `results/`:** at 4 × 1024 and g = 1.5 the change started in 37 places and ended in a defected space 2.5 per point
   above flat, which is why T37 scores the scrap by the energy left.
3. **Read section 3 before writing anything public or anything to a physicist.**
4. Interpreter with numba: `C:\Users\emily\AppData\Local\Microsoft\WindowsApps\python.exe`. Run
   `pytest -q > log; echo $?` and read the status; never pipe pytest through `tail`.

## Addendum, 26 September, early morning (branch `claude/vision-programme-updates-9sje7s`)

- **VISION Update 33**: five positions of the owner's (a ledger for the three releases, 44 / 12 / 0; gravity and the count
  of hidden degrees of freedom; vantage points; how a strange loop is sized; time as an outcome of open space), each
  with what the model says. **O71** (her ledger against the model: walls are returned, not spent; no λ gives her shares;
  the follow tie's walls never fall in her order) and **O72** (the counting drive comes from the points, not the three
  directions, and grows with the number of curled cells; corrects O55). Next ASSUMPTIONS number: **O73**.
- **T44 launched** (six Batch jobs, `cloud/queue/2026-09-26_t44.txt`): the gas of 6-cubes under the follow tie. New
  kernel `graphity.sealed_tie_d` (tests in `tests/test_sealed_tie_d.py`); the runner takes `"kappa"`; read with
  `scripts/analyse_t44.py`.
- **Unread in the bucket, all finished:** the rest of T37 and T38, and T39 to T43. Download and read them next.
- **05:08 ET: the programme regrouped into four groups, twelve pieces** (VISION Update 34; the mapping from old numbers is in
  `docs/papers/series_plan.md`'s last section). Old piece numbers in earlier records (VISION, ASSUMPTIONS, PREREGISTRATION)
  are left as written; the page and the draft carry "was piece N". Allotropes parked (`docs/parked/allotropes.md`; a local
  copy in the gitignored outreach folder). Decided: a charge per opening direction, form not chosen
  (`docs/design/direction_charge_brief.md`). O73 recorded. The dark-charge reading is owed: arXiv was blocked by this
  session's network.
- **11:00 ET: VISION Update 35, O74, T45 launched** (the owner's budget fit: dark energy first fits best; locked predictions in
  PREREGISTRATION T45; eight Batch jobs; read with `scripts/analyse_t45.py`). New kernel: `run_sealed_bath_table_d` (a tie of any
  shape). Next ASSUMPTIONS number: **O75**.
- **11:40 ET: VISION Update 36, O75, T46 launched** (the owner's order as a mechanism: dark energy, dark matter free, ordinary,
  time; T45 setting C in three directions, her prediction for it added after launch and before any result; four eight-link
  Batch jobs, `cloud/queue/2026-09-26_t46.txt`, read with `scripts/analyse_t46.py`; `analyse_t44.read_replica` takes `dim`).
  Next ASSUMPTIONS number: **O76**.
- **14:40 ET: T47 pre-registered** (the owner adopted time curling behind the present, time keeping energy): part A
  on the laptop (`results/t47_front_*`), part B two Batch jobs (`cloud/queue/2026-09-26_t47.txt`); read with
  `scripts/analyse_t47.py`.
- **27 Sep, 04:45 ET: hand-over to a session with AWS credentials.** Download from `s3://recphys-results-<account>/`
  (listing in `cloud/status/latest.md`), check against configs, commit, then read by the pre-registered analyzers:
  T44 (`analyse_t44.py`), T45 (`analyse_t45.py`), T46 (`analyse_t46.py`), T47 part B (`analyse_t47.py`), T39 to T43
  (`analyse_t39.py` ... `analyse_t43.py`), and T38's six missing files (λ = 1.30, N = 192, `_02` to `_07`), then re-read
  T38 (O78 is provisional). Read so far this session: T47 part A (O76, MIXED by the letter; fair-clock reading proposed,
  the owner's call), T37 (O77), T38 provisional (O78). Owner decisions pending: the fair clock; confirming T37's inferred
  prediction; the next build (front slowing near matter is proposed first); charge form; gravity field. Next ASSUMPTIONS
  number: **O79**.
- **27 Sep, 09:45 ET: everything finished is fetched, checked and read** (from the laptop, which cannot reach the
  project account: the new `fetch_results` workflow copies runs named in `cloud/fetch/request.txt` into `cloud/inbox/`,
  and `scripts/accept_inbox.py --move` checks each against its config and moves it into `results/`). O79 to O84 and
  VISION Update 37: nothing opened all directions in three or four dimensions; T47 part B HEALS; T42 interchangeable
  HEALS against named MELTS (*corrected 12:10 ET, O82: the named MELTED replicas are one to a few flickering scars, not a
  melt; T34 the same; nothing curled*); T43 DISSOLVES; T38 TWO POPULATIONS.
- **27 Sep, 12:50 ET: O85** (read from the wiring): the openings' "damage" is joints between cubes that opened
  separately and seams, not scorched space; exactly (Mulder's theorem), a fully curled X is a gas of pieces of at most
  4^D points. **T48 and T49 launched** (28 Batch jobs, `cloud/queue/2026-09-27_t48_t49.txt`): fetch with
  `cloud/fetch/request.txt` (`t48_*`, `t49_*`), check with `scripts/accept_inbox.py`, read with `analyse_t48.py` and
  `analyse_t49.py`. **T50 launched** 13:25 ET (5 jobs, `cloud/queue/2026-09-27_t50.txt`, `scripts/run_front_matter.py`,
  read with `analyse_t50.py`). **15:45 ET, before any result:** the owner's predictions recorded (T48 ADVANCES ONLY
  on the two- and three-curled tori; T50 SPEEDS), and VISION Update 39 (X may start with one direction open; points
  interchangeable before, after or both; the three and the fourth tied evenly or unevenly; the foam held open). Next
  ASSUMPTIONS number: **O86**.
- **The programme page has no global change log any more** (the owner's request): each piece opens with a "Latest"
  row, dated, newest first, and the scorecard tiles show each piece's last date. Keep it that way: add new entries at the
  top of the piece they touch, in the HTML and in `programme_draft.md`'s "Each piece's log".

## Addendum, 6 October 2026 (read this first, then the 5 October addendum)

- **Three AI-generated reviews of the programme were checked against the record** (ASSUMPTIONS O103) and the owner
  decided on them (VISION Update 44): the framing of the pages stays (no frozen "version 1"); each piece is to be
  killed, the hypothesis adjusted; CLAUDE.md rules 10 to 13 adopted (four kinds of statement, never silently promoted;
  decisive tests before patches, with the form "previous claim → failed because → replacement → new falsification
  test"; a red-team pass at each milestone; outside theories as targets and a close number not a result); her
  conjecture that a loop's turn ends when all matter has gathered into black holes and nothing moves is recorded for
  the first time, as a conjecture. Two of the reviews call the hypothesis "Omega", its old name; it is X (glossary).
- **Corrected on 6 October:** dark energy's share at 4 MeV is about 10⁻³⁷, not the 10⁻³⁵ that belongs to 1 MeV (O89,
  O103 (a); the programme draft, VISION Update 41). The draft's "T53 not yet launched" (launched 5 October, 15:17 ET).
  The curling-ladder page's release labels and run table. Paper 1's entry and the (D, λ) map in `series_plan.md`. The
  programme draft's "What is new" now names the decompactification relatives read on 25 September ([GM04], [CJR09],
  [BSV10], [GHR10], added to `REFERENCES.bib`). This page's §9 counts, and its line of 5 October saying the programme
  artifact was untouched that day (it carries 5 October content).
- **Pre-registration:** T51 amendment 3, written before any result was read (the shape of the fall as a power-law
  exponent; the size distribution; the size caveat). T54, a draft: the true barrier in three directions, awaiting the
  owner's prediction before any run; first in the order.
- **Still owed by the owner:** her T51 prediction; her T54 prediction; the open items of Update 44 (claim 4's wording;
  piece 10's attachment to the toy; dark energy as release or kept energy; paper 1's revision; the Fife reference).
- **Not done, in TASKS (6 October):** the two extreme T24 waits read from their wiring; T9; the warm sheet's correlation
  length before any pull; the git commit hash in `.meta.json`; the reading of Pathria, Popławski and Fife before any
  citation.
- Next numbers (6 October, by the clock): ASSUMPTIONS **O104**, VISION **Update 45**, PREREGISTRATION **T55**. Running:
  T51 (91 Batch jobs), T52 (laptop), T53 (30 Batch jobs). The programme draft is current to 6 October; the artifact
  "A Phase-Changing Reality" was republished on 6 October (Version 57) from the corrected draft, and the Curling Ladder
  artifact from the rebuilt page; `docs/public/programme.html` in the repository is older than the artifact and is not
  maintained by hand (the artifact is the programme page, her request of 4 October).

## Addendum, 5 October 2026

- **Fetch before anything else.** On 5 October the laptop's working copy was still on the 25 September commit of
  `feat/cloud-runs-and-3d`, 40 commits behind this branch, with three files uncommitted. Run `git fetch` and
  `git branch -a -vv`; the record lives on `claude/vision-programme-updates-9sje7s`. The queue guard of 26 September is
  merged into it (run_queue never runs on main and skips a config whose result is in the bucket), so merging this branch
  to main cannot resubmit finished jobs. `gh` is not installed: Emily opens the pull request from
  `https://github.com/EmilySmithCreate/RecreationalPhysics/compare/main...claude/vision-programme-updates-9sje7s`.
- **The chat sessions of 4 and 5 October** worked from a copy of the 26 September `main` and pushed nothing. Their
  hand-over is `docs/HANDOFF_2026-10-05_chat.md`; it is now recorded, with corrections, in VISION Updates 40 and 41 and
  ASSUMPTIONS O86 to O94. **Read the corrections before quoting that file:** the long warm T37 tubes melted and are not
  a mosaic (O88); "the scrap is not the dark matter by a factor of ten" is withdrawn (O88, O89); the hidden count is
  taken over the model's own wirings, `graphity.hidden`, not the script as received (O87); the tie it calls
  "Update 30's" is the withdrawn form (O86).
- **The owner's decisions of 4 and 5 October** (VISION Update 41): the first opening is dark energy's; the
  cosmological-constant problem is carried openly; the target is the shares at spacetime's **birth**; the fair clock
  for new kinetic runs (one fair sweep = N/96 chain sweeps, O90); the scrap-share reading stays out of paper 2; the
  gravity decision of 25 September stands (Update 40). **The shares at birth include the light** (O89, ours,
  unverified, for a physicist): do not fit a tie to 5.36 as a ratio of releases.
- **Read on 5 October:** T48 (O91), T49 (O92), T50 (O93), fetched through `cloud/fetch/request.txt` and accepted with
  `scripts/accept_inbox.py` (on Windows a move can fail on a file lock after the copy; compare the copies, remove the
  inbox one, move the rest). T37's cold cell is complete at 12 replicas. Nothing is left unread in the bucket from
  before 5 October.
- **Pre-registered on 5 October:** T51, the frozen scrap against cooling time in tubes that seed themselves, on the
  fair clock (`scripts/run_scrap_freeze.py`, `scripts/analyse_t51.py`, queue file `cloud/queue/2026-10-05_t51.txt`,
  91 Batch jobs, the longest about 8 hours on Batch). **Two amendments were made before any run**, both forced by
  one cost check of the runner: the opening ends when 90 % of points are flat and no stretch of tube three or more
  columns long is left, and the scored ratios compare two coolings of the same opened sheet, with no baseline count.
  **Launched 5 October** by pushing the queue file. To read it: add `t51_*` to `cloud/fetch/request.txt`, push, pull,
  `python scripts/accept_inbox.py --move`, commit the data, then `python scripts/analyse_t51.py`. **The owner's
  prediction is owed before any T51 result is read.**
- **Waiting on the owner** (each is a question, in TASKS.md's section of 5 October): her prediction for T51 before it
  is read; which tie the reservoir test carries (none, "all at the last", "all at the second"; O89, O94); what a plane
  opening is in the model; whether dark matter is the leftover (Update 16) or a direction's release (Update 30), both
  open again under the birth shares; how her front maps onto a clock (T50 SPEEDS). **And one question for a physicist,
  which decides more than any run:** at the start of the hot era, what share of the energy was dark matter?
- **Paper 1:** on hold at arXiv pending a reader or a journal. The reader request to the model's author is drafted in
  `docs/outreach/reader_request_draft_2026-10-05.md` (local only) and waits until after his talk; Gate C's question
  rides with it. Nothing is sent from a session. **Paper 2:** the draft has a section on tubes that seed themselves and
  the plain-language page (`docs/public/paper2-the-scrap.html`) is corrected; the published artifact of that page still
  shows the version from chat until Emily asks for it to be republished.
- **The programme page** is the Claude artifact "A Phase-Changing Reality", a state-of-the-programme page with no
  revision status (her request of 4 October). `docs/public/programme.html` in the repository is older than the
  artifact. The artifact was republished on 5 October with the birth shares and the T37 correction; `programme.html` was not. *(Corrected 6 October: the line first written here said neither was touched.)*
- **Also pre-registered on 5 October:** T52, the hidden count round a relic, exact (`graphity.hidden`,
  `scripts/exact_hidden_relics.py`).
- Next numbers (15:19 ET, 5 October): ASSUMPTIONS **O103**, VISION **Update 44**, PREREGISTRATION **T54**. Running: T51 (91 Batch jobs), T52 (the hidden count, on the laptop; no verdict until it finishes), T53 (30 Batch jobs, launched 15:17 ET; the owner's inferred prediction is to be confirmed or replaced before it is read). The programme draft `docs/papers/programme_draft.md` is current to 5 October.

## 1. What this project is

Emily's hypothesis (`VISION.md`, claims 1–6): spacetime is one settled arrangement of something deeper, X; the
change from X to spacetime was sharp and released a bounded lump of energy (claim 4); a leftover remains
(claim 5); an energy-like quantity is conserved (claim 6); X must give back known physics (claim 2). **The
question is a change from one order to another, never from disorder.** The test bed is built from
Trugenberger's combinatorial quantum gravity (CQG, `src/graphity/cqg.py`; H = 16(N − S) + 4λX). The model's
stand-in for X is the curled torus (the 4 × L torus, "the tube"), metastable for 1.05 ≤ λ ≤ 1.35 at g = 1.5.

**Naming, settled 24 September (the model's author's condition for endorsing paper 1):** only λ = 1 is CQG.
At any other λ the energy is not a curvature. The tube work is at λ > 1, so it is about a close cousin of CQG
and is **never** called combinatorial (quantum) gravity. Anything about gravity is tested in 3D only; no 2D
number is carried into a claim about gravity.

## 2. Verdicts on the record (pre-registered; `PREREGISTRATION.md`; details in `ASSUMPTIONS.md`)

| Test | Verdict |
|---|---|
| T6, λ = 0 (control) | FIRST ORDER (amendment 4) |
| T6, λ ≥ 1 | INCONCLUSIVE, final; one hump, any lump < 1.3 per point at N = 100 |
| T7, tube → sheet, λ = 1.25 | TWO-STATE CHANGE at N = 64, 96, 192 |
| T8, the λ map | INCONCLUSIVE by the letter (memoryless criterion too tight); sharp wherever stuck, 1.05 to 1.35; edge between 1.35 and 1.40 (O38) |
| T23, the λ map again at 120 decays | Window INCONCLUSIVE by the letter: the energy gate, unchanged from T8, fails at λ = 1.30 at every size (3 to 5 decays of 120); memoryless in 20 of 20 cells to 1.25. Edge: BREAK-UP BEGINS AT THE EDGE, as predicted (O44) |
| T9 sealed tube | BONFIRE WITH A THRESHOLD |
| T10 leftover vs size | ONE RING, HOWEVER LARGE |
| T11 | NEITHER |
| T12 | the coarse law does not govern |
| T13, λ = 1 at N = 4p² | INCONCLUSIVE: protocol E fails its gate at 484 and 676 |
| T15 rung 0 / 0b / 1 / 3a | INCONCLUSIVE / INCONCLUSIVE (loop not a resonator) / AGREES / CLASSICAL by argument |
| T16, correlation length | NONE (O31): nothing grows with N; susceptibility peak flat at 0.18 |
| T17, leftover per seed | BETWEEN: 1.10, 2.15, 2.50, 3.40 for k = 1, 2, 4, 8 |
| T18, room needed vs λ | PROPORTIONAL |
| T19, does the leftover last | ANNEALS at every fixed coupling |
| T21, sealed sheet with interchangeable points | MELTS EITHER WAY at N = 64 |
| T22, recrossings near λ = 1 | FALL-BACKS: first exit on time; κ = 0.56 to 0.68 |
| O40, O41 (exact) | 2D: a gas of knots is never stuck for λ > 1. 3D: the 6-cube is stuck only for 1 < λ < 1.2 |
| T23, T24, T25, T26, T27 | window INCONCLUSIVE by the letter (edge BREAK-UP); INCONCLUSIVE a third time; FREEZES IN; MELTS; STAYS MELTED |
| T30, T32, T33, T34 | NEVER OPENS (tori; first read FIRST ONLY); FIXED WALL; NO CASCADE; MELTS at 216 (scars, not a melt, O82) |
| T37, T38, T42, T43 | KJMA exponent; the long warm tubes melted (O88); TWO POPULATIONS; HEALS either way (O82); DISSOLVES |
| T44, T45, T46, T47, T48, T49, T50 | no cascade; no setting opens all; NOT ALL; A MIXED, B HEALS; ONE SPACE / ADVANCES ONLY / DAMAGED / STAYS by torus (O91); part way, fully in a minority (O92); SPEEDS at 6 and 10 (O93) |
| T51 (9 Oct) | CLIFF; P1 fails at one point of two; P2 holds (O104) |
| T53 (9 Oct) | ADVANCES ONLY at every (L, λ); SEVERAL; one cell resubmitted (O105) |

## 3. The model's author, and what is public

- **Correspondence is private and not in this repository.** `docs/outreach/` is gitignored and local only
  (removed from the public tree on 24 September; older commits still hold copies, and whether to rewrite
  history is Emily's decision, deferred). Never commit anything from it. Never quote or closely paraphrase a
  private email in a tracked file.
- **Decided (Emily, 24 September): leave as they are.** Tracked files written before that rule paraphrase his
  emails (VISION Update 18, TASKS Gate B, ASSUMPTIONS O26/O27, PREREGISTRATION T13 and T16); that is ordinary
  "private communication" practice in science. New text follows the rule above.
- **His note of 24 September** (paraphrased locally): he will endorse paper 1 for gr-qc, on the naming condition
  above; he asks whether our moves are single switches and suspects low-coupling equilibration needs global
  moves; allotropes decay, and the question is how long they take ([T25] Fig. 9); his focus is the order of the
  transition. **Emily's reply was sent on 24 September** (local copy `docs/outreach/reply_sent_2026-09-24.md`).
  In it she says the moves are single switches, with replica exchange the only non-local ingredient; that the
  title and abstract carry his naming condition; and she asks for the allotrope's adjacency list (from him or
  Eryk Kopczyński; RogueViz may produce one), to predict its lifetime at λ = 1. Allotropes wait until after his
  work on the order of the transition. **Not yet asked:** Gate C's question (O43: [T22] Fig. 3's protocol,
  moves and weight). Keep it for his reply, one question at a time.
- **His reply of 25 September, evening** (paraphrase and a draft answer in `docs/outreach/reply_draft_2026-09-25_carlo.md`,
  local only): the allotrope has no finite adjacency list, so piece 12 is now T36, a numerical search he suggested; and he
  asked for a figure, drawn as `docs/figures/t13_n676_replica_exchange.{png,pdf}` by `scripts/plot_t13_n676_tempering.py`.
  The draft answer carries Gate C's one question (O53). Emily sends; nothing is sent from here.
- **S5, 25 September (the owner's report):** paper 1 has been submitted to arXiv, the model's author having endorsed it;
  it should appear within days, and she expects him to read it and respond within a couple of weeks. Do not prompt him.
  The pages say the door is open and the record is not yet read by a physicist.
- **Paper 1** (`docs/papers/curled_torus/`): retitled "…in a graph model of emergent geometry"; abstract and
  text say only λ = 1 is CQG; content from his private emails removed ("hybrid", the N = 4p² advice). The PDF
  was rebuilt with Tectonic (not installed system-wide; fetched into a session scratchpad). **Plan:** send the
  reply with the PDF, he endorses, submit to arXiv, then publish the web page linking to it.
  **Revised the same afternoon after a review Emily obtained from ChatGPT** (ASSUMPTIONS O42; disclosed in the
  paper's acknowledgments): the dynamics is named wherever
  kinetics appear (Introduction, Discussion); "the nucleation barrier" became the minimum energetic barrier to the
  first exit, with κ as the rest of nucleation; Eq. (2)'s ordered-proposal count is explicit, with the twisted
  same-energy family and the distant-edge exits it leaves out; labelled vs interchangeable has its own paragraph;
  "however large" and "no coexistence temperature" were softened to what was measured; d(v) is defined as an order
  parameter; a "why deform λ" paragraph; Fig. 2(c) survival panel and SE bars on Fig. 3(a); Table I's N = 192
  rerun filled in; both barrier fits quoted. Title now "...decompactification between ordered states in a graph
  model of emergent geometry" (Emily, 24 September); the cow line kept. Now 7 pages. The programme page was brought
  into line (pieces 1, 2, 5), light on numbers as she wants it; the plain-language page was left alone by her
  decision.
- **Web pages.** `/physics` on sidenerdapps.com is now the plain-language page
  (`docs/public/did-space-snap-open_v1.html` → `scripts/make_site_page.py` → `docs/public/site/physics/index.html`;
  Emily pastes it into the SideNerdMarketing repository, which deploys). Version 2 carries today's corrections.
  The whole-account page (`the-loop-and-the-floor_v1.html`) is corrected to version 2 but **not published**;
  its build writes to `docs/public/site/account/` with a placeholder URL. Do not publish either without her.
  The programme page is `docs/public/programme.html`, mirrored as the private artifact
  https://claude.ai/artifact/JLtR2aqHmL2FghWmNZU8xW; its text source is `docs/papers/programme_draft.md`, and the
  two are updated together.
  Every claim says whose it is; no process narration.

## 4. Waiting on Emily

0. **T26's prediction is hers (confirmed 24 September, night).** T25's (FREEZES IN, which held) and T27's (FOLDS
   BEFORE IT FLATTENS, which failed) stay marked inferred; she may confirm or disown them. Her decision of the same
   night is on the record as VISION Update 24: proceed with the six-link work now, reproduction later. Decide whether to
   send any of the per-paper letters proposed in `docs/papers/series_plan.md` ("Who to ask"), none drafted or sent.
   **T28, the gravity test:** its dynamic form cannot run at equilibrium (O51); its exact counting rung can, and a
   sealed form would need a new protocol declared first. Her prediction is still wanted before anything runs.
1. Whether to send the reply to Carlo (and the PDF), and when to submit to arXiv.
2. The allotrope of [T25] Fig. 9: the reply asks for its adjacency list. **Do not build it from the drawing:**
   every coloured face looks four-sided, which does not fit the caption. Exact and ready once the graph exists:
   if no edge carries three squares, the local term is zero and the question does not depend on λ.
3. The quantum leg after rungs 3a and 0b (redefine the object as the cap; a rule for cancelling versions;
   her position that it comes from the loop). Nothing is built until she decides.
4. T15 rung 0's two post-hoc readings; T8's proposed repair.

## 5. Natural next lines (pre-register before running)

0. **Decided, 25 September late afternoon (VISION Update 29, her "Proceed"):** the exchange phase on loops is the first
   rule of the new model; its fermionic form is a selection rule (O57, `scripts/exact_exchange_sign.py`). Next for it: the
   rule inside the interchangeable chain against the exact averages at N = 16 and 18 (`scripts/exact_small_averages.py`
   is the reference), then the anyonic form. Gravity step 1, the six-link relic search (`scripts/exact_relic_search_d.py`),
   is recorded as O58 when read.
0. **The owner's direction, 25 September afternoon (VISION Update 28):** other models with loop and exchange rules
   (`docs/design/loop_exchange_brief.md`, candidate rules for her to choose under S1; nothing built); gravity as the
   target, at least directionally, at one λ (`docs/design/gravity_brief.md`: definitions, observable, targets, protocol,
   what is missing). The four-, six- and eight-link runs are groundwork for the new model.
0. **Papers:** five drafts exist (`curled_torus`, `relic`, `fertile_window`, `black_hole`, `six_links`), all in line
   with the record as of 25 September morning, none with a PDF, none read by the owner. The six-link one has an empty
   eight-link section waiting for T33. The programme page now carries a dated change log and a per-piece date; keep both
   current whenever a result comes in (the owner asked for this on 25 September).
1. Gate C: failed (O43). Gate C′ (O46) is running: if reading (iv) holds in 3D and the 2D width says two powers, the
   gate is passed under that reading and the six-link track reopens; if the 2D width says one power, the next build is
   a six-link kernel that allows triangles and pentagons (the paper's own ground states have them); if A fails, the
   question goes to the model's author. Report P2 when it lands. **The gravity test (piece 7) is designed as T28 in
   `docs/papers/series_plan.md` and waits on this gate; its exact rungs (energetic and counting pull of two 3D relics
   at fixed wiring) need no gate and can be computed now.**
2. T23: read (O44). Piece 2 is being settled by T24 (running), whose gate 3′ was fixed before the run.
3. The allotrope, once the graph arrives: stuck or not at λ = 1, its barrier, its lifetime against size.
4. If not yet done: a cloud result checked bit for bit against the same config run on the laptop.
5. The scrap race (does it freeze in as the box cools?), and the local-spark protocol (TASKS T14).
6. `replica_ids` for the tempering and sweep runners, with the seeding test, before large cloud runs.
7. The long tail at λ = 1.05 (O42, unexplained): 3 of 200 waits near 80,000 sweeps where an exponential gives 0.19.
   **Emily, 24 September: not a priority**; it does not bear on paper 1's point, and it is left for later or for
   anyone who wants it. If taken up: many first exits at λ = 1.05 (a few hundred replicas), pre-registered.

## 6. Corrections that must not be undone

- **Only λ = 1 is CQG** (section 1). Titles, abstracts, captions and page footers are checked for this.
- **The model has no time.** Piece 13 (VISION Update 25) tests the pattern in which four curled directions open; which
  direction is time it cannot say, and no page says so.
- **Every six-link result carries the caveat that the reproduction gate is open** (VISION Update 24), and O41's windows
  are for the tori it listed: the two-curled state with a long open side is stuck to λ = 1.5 (O49), not 1.2.
- **Matter is the structured leftover or the released energy, not the melt** (Emily, VISION Update 19). What
  [T25] calls matter is his.
- The four-point remnant is one column of the tube left curled; it comes at 4, 9 or 14 units.
- The loop of four is not a resonator inside the sheet (O30). Counting versions of a fixed arrangement is a
  hidden-variable theory and cannot violate Bell (O29).
- The waiting-time law: plain mean ratio 0.98, weighted 0.88 ± 0.06, over twelve conditions. Never "three
  parts in a thousand" or "half a per cent".
- The model's hot phase is not X; write "the random phase". Never present T7 as having cleared S2′. Never
  write "nobody has done this"; write "we have not found". **Read positions before naming a geometry.**

## 7. How Emily works

- She is a software engineer, not a physicist. Lead with the answer, plain English, analogies. She pushes
  back; take it seriously and check it.
- **Predictions are hers.** Put options to her, record her choice and ours beside it, labelled.
- Rule changes after seeing data are proposed, never enacted. Pre-register before running.
- Results are append-only; only a crashed run's `*.partial` may be deleted. Every CSV has a `.meta.json`.
- Tests before every commit. Commit and push on the feature branch; she merges; never push to `main`. `gh` is
  not installed; give her the compare URL.
- Toward the model's author: no expectation of pace; no "I will send". She collaborates only on work that
  includes the order → order question.
- Her coined term: **curve-first gravity** (`docs/papers/glossary.md`).

## 8. Environment

- Bash's bare `python` and `.venv` lack numpy; use the full interpreter path above for pytest and runs.
- `pdftoppm` is missing, so the Read tool cannot render PDFs; PyMuPDF or pypdf extract text. arXiv HTML
  sometimes omits figures; render the PDF page instead. Downloaded papers go in `docs/reading/` (gitignored).
- Bash heredocs eat `\n` inside Python strings; write scripts with the Write tool.
- **Which Python (6 October):** `python` and `py` on this laptop resolve to a bare `.venv` with no NumPy and no pytest, so `pytest` there exits reporting that pytest is missing and a script that imports the kernel fails. The interpreter with the project's dependencies is the Microsoft Store one, `~/AppData/Local/Microsoft/WindowsApps/python3` (NumPy 2.0, Numba, pytest 9.1). The shell also cuts off long heredocs: a script over a few thousand characters is written to a file with the Write tool and run from there.
- Background runs: `nohup <py> scripts/... > log 2>&1 &`; progress from `results/*.partial`.

## 9. Where things are

`VISION.md` (claims; Updates 1–46) · `TASKS.md` (its numbering map matters) · `PREREGISTRATION.md` ·
`ASSUMPTIONS.md` (Q1–Q23, O1–O105) · `REFERENCES.bib` · `docs/papers/` (paper 1, `series_plan.md`,
`programme_draft.md`, `glossary.md`) · `docs/design/` · `docs/parked/` · `docs/public/` · `docs/figures/` ·
`scripts/analyse_*.py` with tests in `tests/` · `terraform/`, `Dockerfile`, `.github/workflows/` ·
`src/graphity/` (`cqg.py`, `cqg_d.py` for any D, `sealed.py` (now with per-vertex stores and stream carry-on), `spark.py` (the local spark, Q22), `tempering.py`, `symmetry.py`,
`interchangeable.py`, `connectivity.py`, `small_graphs.py`) · `cloud/queue/` (push-triggered Batch manifests).
