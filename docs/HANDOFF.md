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

**The process changed on 11 October 2026 (VISION Update 55). Read `CLAUDE.md` rules 9 to 11 and 16 to 18 before recording anything: a result is written once (its Reading, and one O entry if it changes what is known); looking happens in `sandbox/`; next VISION number is Update 56.**

**Addendum, 11 October 2026 (the same branch; written 09:50 ET by the clock). Read this first.**
- **What the tube opens into is a tube** (ASSUMPTIONS O116; VISION Update 54; CLAUDE.md, "Added 2026-10-11").
  Read from the saved wiring, 9,208 of the 9,215 exactly flat end states of T8, T23, T24 and T60 stage 1 are the
  4 × L tube with its seam shifted by two: six steps around where the tube was four, the least a flat torus can
  be, at every size from 64 to 192. Every verdict stands (they are energies and counts). The picture "opens into a
  sheet" does not. **Paper 1 does not say this yet and must, before anyone is asked to read it.** The readers are
  `scripts/read_endpoint_width.py` and `scripts/read_open_shells.py` (exploratory; `tests/test_read_shapes.py`).
- **T57 read (O114): MELTS in all four groups**, with the owner's tie as without; 582 of 640 replicas MELTED, 58
  HEALED, none FOLDED. Her RE-CURLS fails; ours holds. **T56 stage 1 read (O115): no cell opens.** The slab STAYS
  at λ = 1.10 to 1.20 and ADVANCES ONLY at 1.25; the rod STAYS; the control NO DIFFERENCE. Her prediction fails,
  and ours. The tie as written charges a damaged point nothing, so the tied slab breaks; and the barrier is T54's
  patch, not the single move. Rule 11's four answers are in the O entries; the replacements are hers. T56's
  held-out prediction is "none" and its stage 2 is not queued (ours: do not run it as registered).
- **T60 stage 2 is read (11:16 ET; O117; PREREGISTRATION T60, "Reading ... stage 2"): AS PREDICTED AT THE
  HELD-OUT SIZE, and sharp at N = 288 at every window λ.** The largest converted piece landed within 0.04 of the
  line at every λ (0.751 against 0.754 at λ = 1.30). Her prediction holds, and ours. Ours, not scored: the same
  line reaches the 0.70 mark near 350 points, so one front at the top of the window is a property of short tubes.
  Paper 1 still does not quote T60: the red-team pass comes first. *As it stood that morning:*
  Her prediction for N = 288 was recorded at 09:14 ET (as ours), before anything was fetched.
  Six of the seven cells are accepted into `results/` and **unread**; `t60_lam135_n288` was still running on
  Batch at 09:27 ET. The analyzer registered before the run reads stage 2 only when all seven are in: when the
  last lands, fetch, accept, `python scripts/analyse_t60.py`, record the reading. Do not open the N = 288 files
  before that (`scripts/read_endpoint_width.py` leaves them out for this reason).
- **T54 is read at its held-out size (16:01 ET; O118; PREREGISTRATION T54, "Reading ... the held-out size").** The
  numbers hold exactly; under the tie a finite patch exists at every λ (barriers 145, 77, 45, 27 for λ = 1.10 to
  1.25); the verdict word is unscored in four rows (the wrapped patch) and FIXED WALL in two. A fresh review of the
  construction is owed (rule 12). **Corrected that evening, and not to be undone (O118, "Correction"): these are
  completed-patch energies, not barriers.** The states between patches go higher and a line of columns goes
  lower; do not quote 145, 77, 45 or 27 as a barrier, or "critical patch" as a seed's size. *As it stood that morning:*
  Stage 1 (L = 8, 12) is on this branch and read: ΔH(k) is the same exact quadratic at both sizes. The
  prediction for the held-out size is Amendment 4 (committed first, ed1970be). **L = 16 has been computing on the
  laptop since 10:08 ET** (`configs/t54_patch_heldout.json` → `results/t54_patch_heldout.csv`; a `.partial` file
  beside it means it is still running or was killed; the runner refuses to overwrite). Read it as the amendment
  says. The untied L = 24 cases are not run.
- **The red-team brief** for a fresh outside reviewer (rule 12) is
  `docs/papers/curled_torus/red_team_brief_2026-10-11.md`. It gives the questions and where things are, not the
  conclusions; the owner hands it over. Paper 1's sentence on the fourth map and the reader request to the
  model's author wait for the report.
- **The drafts of papers 5, 6 and 12** (`docs/papers/six_links/`, `fertile_window/`, `black_hole/`) were brought
  up to date and built. The owner has not read them.
- **A test that had been failing on GitHub since 10 October** (the entropy-action fit read every saved graph, so
  T60's end states moved its recorded number) is fixed: the script reads only the runs O111 was computed on.
- **Two decisions of the owner's, 11 October, evening (VISION Update 56):** claim 4 says "a jump in energy", not "first order" (her words; Update 44's open item (a) is closed); and the toy is to be tested with a price on loops of six, μ × (a link's loops of six − 6) where positive. Sandbox looks only so far (`sandbox/LOG.md`); a registered test needs a tested kernel, a held-out size and her prediction.
- **12 October: the reviewer's rewrite of paper 1 is in main (the owner merged it, PR 46), and the work goes on on `claude/paper1-after-review-2026-10-12`.** That branch holds everything: main, the eight commits of 11 October that main does not have yet (T61 read, T54 corrected, O120, O121, Update 56), the reviewer's entry restored as O122, and paper 1's two editions revised from the owner's notes on the reviewer's text (why two humps are not enough; the curling cost as something she wants tested; the jump in energy; the trapped-heat result; what "melted" can mean). **Main's ASSUMPTIONS.md is missing O118 and O119 until this branch is merged.** A sealed tube cannot melt (O123). Paper 1's PDFs are rebuilt (11 and 36 pages; the plain-language edition was trimmed of a repeated point and given one figure later on 12 October, from the owner's read) and the release manifest regenerated; the Side Nerd site was refreshed later on 12 October as a branch in the marketing repository (`feat/main-nerd-post01-2026-10-12`; hers to merge and deploy). She has asked to review a four-part restructure of the plain-language edition before any rewrite (TASKS, item 10).
- **The six-loop price is tested code** (`src/graphity/sixloop.py`; O124): the term of Update 56 with an exact incremental update, checked move for move against full recomputation, and `cqg.run_chain` draw for draw at zero price. Exact listing: `scripts/exact_sixloop_walls.py`. **The push used in the sandbox looks of 11 October was long-range** (it joins links seven steps apart); do not describe those looks as a local seed and a front. No registered run yet: T62 needs its design chosen (which push, or none), a held-out size and the owner's prediction.
- **T62 is registered and queued on the cloud (12 October):** the tube six around under a price on loops of six, no push, five prices with μ = 0 as the control, two couplings, N = 96 and 192, held-out 384 (`cloud/queue/2026-10-12_t62_stage1.txt`, 20 jobs). **The owner's predictions for T62 and T63 were recorded on 12 October, before anything was fetched** (PREREGISTRATION, the last section: WIDENS at every price above zero in both; her guess stands where it differs from ours, at four settings). **T63 is registered and queued too** (the curled tube itself, five prices with μ = 0 as the control, g = 1.5, same sizes; `cloud/queue/2026-10-12_t63_stage1.txt`, 10 jobs; read with `scripts/analyse_t63.py`); her prediction for it is recorded with T62's. To fetch: `t62_*` in `cloud/fetch/request.txt`, accept, commit unread; then, after her prediction, `python scripts/analyse_t62.py results`.
- **A second branch is open and its numbers collide with this one's: `claude/observer-relative-histories-2026-10-12`** (another session, the owner's handoff of 12 October; pieces 13 and 14, `docs/theory/orh_*`, `src/orh/`). It left main before PR 48, so its ASSUMPTIONS.md has the reviewer's entry as "O118" and its own entry as "O125", placed after the Provenance section. Here and on main O118 is T54 and O125 is the count of flat tori; the reviewer's entry is O122 here. **When that branch is merged: do not add its "O118" again, renumber its "O125" to O125, and put it before Provenance.** Its programme draft is the newer arrangement (a book in seven chapters); keep its structure and carry this branch's paragraphs of 11 and 12 October into it. The published page (Version 81) already has both. *Done, later on 12 October: this branch was merged into `claude/observer-relative-histories-2026-10-12`; the entry is O125 and sits before Provenance; the draft keeps the seven-chapter arrangement with this branch's paragraphs of 11 and 12 October; the notebook's entries of both sides are kept in day order; the published page (Version 85) already carried both.*
- **T62's stage 1 is read (12 October; PREREGISTRATION T62, "Reading"): WIDENS at μ = 0.20, 0.25 and 0.30, STAYS SIX AROUND at 0.10 and at the control, at both sizes.** Her prediction holds at three prices of four; one end state of 480 is clean and wide (a flat torus eight around). The held-out numbers are written and N = 384 is queued (`cloud/queue/2026-10-12_t62_stage2.txt`); to read it: fetch `t62_*n384`, accept, `python scripts/analyse_t62.py results`, then one O entry for T62 (O126). **T63's stage 1 is read: NOT READ at every price, by its own rule.** Its control ended six around in 0.79 and 0.88 of runs and the bar was 0.9; paper 1's own maps give 0.80 to 0.91, so the bar was ours and too high (PREREGISTRATION T63, "Reading"). Its rows are described there and support nothing. **T64 is T63 again on fresh seeds with the control written from paper 1's record** (PREREGISTRATION T64; her T63 prediction carried; `cloud/queue/2026-10-12_t64_stage1.txt`, 10 jobs; read with `scripts/analyse_t64.py`). To read it: fetch `t64_*`, accept, suite, commit unread, read, then `--write-prediction`, a dated amendment, `make_t64_configs.py --held-out`, queue. It is a second attempt and is quoted as one. **T64's stage 1 is read (PREREGISTRATION T64, "Reading"): the control holds; WIDENS at μ = 0.05, 0.10 and 0.20 and MIXED at 0.025, at both sizes; her prediction holds at three prices of four.** Read from positions, the wide product has a flaw within three steps of nine points in ten (`scripts/read_clear_points.py`). Its held-out numbers are written and N = 384 is queued (`cloud/queue/2026-10-12_t64_stage2.txt`, 5 jobs); to read it: fetch `t64_*n384`, accept, suite, commit unread, `python scripts/analyse_t64.py results`, then one O entry for T63 and T64 (O127). **Read from positions the same day (O116, addendum of 12 October; `scripts/read_leftover_width.py`): paper 1's end states that keep a leftover, 17 in 100, are not all six around; about half hold a stretch of a few tens of points that is wider.** "Ends six around" is exact for the exactly flat end states only.
- **13 October: the plain-language edition of paper 1 redrafted from the owner's notes (branch `claude/paper1-plain-structure-2026-10-13`; not read by her, not merged).** Chapter 1 is one page in her order, Chapter 2 two pages on the reproduction and the one change, and Chapter 3 says what the shapes are: the tube a thin ring, the sheet a fatter doughnut, flat about each dot's surroundings and wide about the whole, with the count an inhabitant could make. The rest is shorter (32 pages, 26 figures), with a table or a list where a paragraph listed outcomes, and without the account of the detector and the long waits, which the technical paper keeps. **Her rule for this edition: its reader is a lay person who enjoys mathematics and physics; a section stays only if it says what the toy shows, for or against, or leads to the next question.** The blog pages are rebuilt, and post 01's plain page is a pull request in the marketing repository. What changed is in `papers/curled_torus/plain_language_README.md`. **To remember when talking with her: nothing in any toy of the programme has an open-ended direction, at four, six or eight links; "opening" a direction means its way around becoming longer than one square.**
- **13 October: a vocabulary pass for condensed-matter readers (branch `claude/chern-group-vocabulary-2026-10-13`).** At the owner's request the process words of paper 2's draft were set beside those of G.-W. Chern's group at the University of Virginia, four insertions and two references went into paper 1's technical manuscript (rebuilt with `scripts/build_curled_paper.py`; the plain-language edition is unchanged), and pointers went to the drafts of papers 5, 6 and 12 and to the series plan. The one home for what was read and the map of terms is `reading/notes/2026-10-13_chern_group_vocabulary.md`. One sandbox look (T51's fall as a floor plus one exponential; `sandbox/LOG.md`), not promoted. Nothing was sent to anyone. **Later the same day:** paper 2's technical draft (`papers/relic/paper.tex`) was rewritten with T51, T55, O116's wording and O123, and given a draft plain-language edition (`papers/relic/paper_plain_language.tex`); the owner has read neither. M. Vucelja's papers were read by abstract (the note, section 8): she and G.-W. Chern are the two natural readers for the measurement side of paper 1, and the work that would serve them is in `papers/curled_torus/handoff_2026-10-13_measurement_side.md` (none of it registered or run; TASKS, 13 October). **The blog build now carries more than one post:** each post is an entry in `scripts/main_nerd_posts.py` (its slug, sources, summary, question headings and FAQ), `scripts/build_main_nerd_pages.py --only N` builds one, and post 01's pages are unchanged by the refactor apart from their "next post" link. Post 02, "What the burp leaves behind", is up in `docs/public/mainnerd/02whattheburpleavesbehindPL/` as a plain-language edition only (the technical edition is offered as a PDF), and the whole folder was copied to the marketing repository as the branch `feat/main-nerd-post02-2026-10-13`: not merged, not deployed. Paper 1's release manifest was regenerated after its plain edition's source list changed.
- **14 October: the owner's notes on both plain-language editions applied (same branch, `claude/paper1-plain-structure-2026-10-13`; not read by her, not merged).** Paper 2 is renamed *What the change leaves behind* (her words: the change makes both the burp and the remainder); the blog post moves to `/mainnerd/02whatthechangeleavesbehindPL/`, so the marketing site needs a new branch when she ports it. Paper 1, plain: Chapter 5 names the fair clock and says what it does and does not change; Chapter 6 is shorter, with one new figure (the shifted seam as two spirals wound round the doughnut, and the six-step walk unrolled); the clean finish is six around, and finishes that kept a scrap can mix widths (O116); Chapter 8 separates free scraps from joints and draws the common scrap link by link. Paper 2, plain: the authors' own predictions are no longer a character (the technical paper keeps them); the curled loop is no longer called a ring of the old tube; three kinds drawn on a tube, and the joint drawn in 3D; a table of what the kinds share and what sets them apart. The drawings show wiring, not placement: **O126** (new) reads the column's wiring in 2,045 saved columns and finds none that goes around the new tube. The technical paper 1 names the size-fair clock in two places; the technical paper 2 corrects the column sentence. Later the same day, at her request, paper 1's plain Chapter 8 (the scrap) was folded away: a tease at the end of Chapter 6 and one paragraph in Chapter 7 ("What a cold box leaves", with the failed prediction that it grows); the edition now has ten chapters, and the technical paper's "PL, Ch." pointers were renumbered. Then, also at her request, both editions were tightened: named versus interchangeable vertices, the trapped-heat widening test (T61, now one paragraph), the exploratory Arrhenius scan (one sentence), the allotrope questions at lambda = 1, and in the plain edition the six- and eight-link figure, the random-tangle jump table, the bounce, the backwards rehearsal, the Klein-bottle aside and the six-loop price; the plain edition is 30 pages. Every registered result still has its sentence, and the technical reference list is unchanged.
- **14 October, later: the owner's notes on paper 1 applied to the other papers (branch `claude/papers-apply-feedback-2026-10-14`, cut from the paper 1 branch).** Her rules are in `docs/papers/feedback_2026-10-14.md`. The technical drafts of papers 2, 5, 6, 10, 11 and 12 had a plain-wording pass, readable equations and the consistency facts (six around for clean finishes, free scraps and joints, the column not a ring, paper 2's title, the size-fair clock); the plain notes of papers 10 and 11 likewise; the glossary, programme draft and series plan updated, the plan with where paper 1's cut material now belongs and the figures each technical draft owes. Fixed on the way: fertile window's "leaving a flat torus costs 32" (16 lambda for the torus six around; 32 from eight around up), its "what makes a flat torus widen is next" (T61 and T62/T64 now cited), and a "we have found" sentence in the gravity draft with no search note behind it (reworded). Not read by the owner.
- **15 October: the owner's answers to the programme page's open items (branch `claude/owner-answers-2026-10-15`, cut from the relic-seed sandbox branch; neither merged).** Piece 9 adopts the published amplitude rule; curling energy is adopted as an ingredient, reversing Update 32 for the fold, its form owed in a design brief before any registered run; pieces 13 and 14 undecided (VISION Update 57). Her picture of the fold (a relic seeds a doughnut, which unzips into a stable-for-now tube that is the black hole's inside, and a second activation opens it wide again) is in `sandbox/NOTEBOOK.md` with ten questions put to her; her knots prediction is still owed. The programme artifact (Version 90) carries the questions. **16 October, early:** T62's ten held-out cells accepted and read: AS PREDICTED at every price (O127); the owner's T65 prediction "Opens in room" is on the record; T65 is registered and launched on her word "Launch in cloud" (8 Batch jobs, `cloud/queue/2026-10-16_t65_stage1.txt`): the tied slab given a spark, with and without a hand-opened patch, after the sandbox look showed a bare patch is a dip and not a push. The relic search at λ = 1.25 found no dip (log). **Evening:** her whole picture, drawn on a whiteboard and described, is in the notebook in her words with the photos in `docs/figures/whiteboard_2026-10-15/`, and is read element by element against the record in `docs/design/whiteboard_picture_2026-10-15.md` (aligned: the slice, number for number, and her tie's bookkeeping; not found: a relic inside three-direction space, O56, O58; not seen: energy curling flat space; three exact listings named).
- **16 October, later: the owner withdrew the tie "all at the last" (VISION Update 58).** The rule is curvature plus a curling cost, untied; X is the slab, whose one remaining opening releases a per point. Tied verdicts stand as scored; T65 is read as registered with its untied control as the cell that speaks to the hypothesis (PREREGISTRATION T65, amendment of 16 October). Open to her: whether Update 57's curling energy stays, since its stated reason was the tie. Same morning, in the notebook: her questions on the fold's price and where unspent energy goes; her prediction that three-direction damage heals in fewer sweeps than two-direction untied, tried in the sandbox (`sandbox/heal_time.py`, LOG when read); her statement that a coherent story is the programme's purpose.
- **16 October, later still: T66 registered and launched** (the healing-time comparison, promoted from the sandbox look on her "Yes proceed"; her prediction FASTER IN 3D; 4 Batch jobs). A feed look (`sandbox/slab_feed.py`) is running for her "flow rather than spark" idea; her word for T65's untied control is still owed.
- **16 October, midday: T66 stage 1 and T64's held-out size fetched, accepted unread, committed (8ee58427) and read.** T66: FASTER IN 3D at N = 216, MIXED at 512 (O129); the registered observable is a fluctuation below the equilibrium damage at large N, disclosed; held-out numbers written; three repairs proposed to the owner, none enacted; her N = 1000 prediction owed. T64 held-out: the control misses its bar by one run at N = 384, NOT READ above μ = 0 (O128). T65: six of eight cells accepted unread; `t65_a_lam120_l12` and `t65_a_lam125_l12` still running; the analyser is not run until all eight are in.
- **16 October, evening: T65 read, all eight cells (O130).** No cell OPENS; tied PARTIAL at λ = 1.20, DAMAGED at 1.25; the untied control FALLS BACK in 31 of 32. Her two words fail; ours holds on the tied word at 1.25 and fails on the control. The end graphs read as a sprinkle of pairs, never a front. Rule 11's fifth use on piece 5: her replacement is a feed; the next test is a registered feed run with her prediction. Owed by her: the L = 16 word (and whether the untied control runs there at all); T66's repair choice (she leans (a) and (b)) and N = 1000 word.
- **16 October, late evening: the owner's relational cosmology handoff recorded.** Her document (drafted in another conversation of hers; "Omega" is X; its T1 to T8 are H1 to H8 here) is kept as received in `docs/theory/relational_cosmology_handoff_2026-10-16.md` and read against the record in `docs/theory/relational_cosmology_review_2026-10-16.md` (O131). Two decisions in VISION Update 59: the black hole's inside is the parent's own geometry curled, not a slab inside it; the whole-universe reset is no longer required, so a daughter may form while the hole stays in the parent. Her priority, adopted: the feed run (energy-coupled nucleation, three outcomes recorded) before any daughter-universe work (TASKS, 16 October section). Carried into the programme page (pieces 5, 11, 12) and paper 12 (a new section; its PDF is stale, no LaTeX on this machine); series paper 15 outlined. She confirmed both decisions the same evening; piece 12's count is the branching one (each universe ends when its last black hole has dissolved; every black hole births many; the tree multiplies at equal cold time). **Launched on her words "the rates may not be fixed but it's good to run that way for starting. if the untied control is still relevant run it":** T67, the feed run on the untied slab (PREREGISTRATION T67; 6 Batch jobs, `cloud/queue/2026-10-16_t67_stage1.txt`; her prediction inferred, OPENS from one spot; ours BREAKS everywhere), and T65's held-out control at L = 16 (1 job, `cloud/queue/2026-10-16_t65_heldout.txt`; her prediction inferred as PARTIAL; ours FALLS BACK). To read T67: `t67_*` in `cloud/fetch/request.txt`, accept, commit unread, `python scripts/analyse_t67.py`, then `--write-prediction`, the held-out amendment, her L = 16 word, `python scripts/make_t67_configs.py --held-out`. To read T65's held-out: `t65_control_lam125_l16`, accept, `python scripts/analyse_t65.py`. Owed by her: her own words for both predictions before they are read.
- **17 October, 01:45 UTC by the clock: the programme page stripped to the current picture at the owner's word** ("Strip the tie from phase changing reality and any idea that are not our current best ideas"). `docs/papers/programme_draft.md`: the claim carries her decisions since 9 October (tie withdrawn, a feed not a spark, the black hole as the parent's geometry curled, daughters and the branching count, the amplitude rule adopted), with its changed sentences marked ours in wording until she confirms them; "Where the programme is" is one current section (picture, shown, set aside, next, papers); pieces 3, 5, 6, 9, 11 and 12 rewritten without the tie, the order-of-opening story, the spaghetti X or the reset; the piece logs and the record keep every dated verdict. Nothing scored is rescored.
- **17 October, 02:14 UTC by the clock: T65's held-out control and T67 stage 1 fetched, accepted unread, committed (df81fd9a) and read.** T65 at L = 16: FALLS BACK in 16 of 16, AS PREDICTED; one spark of 128 opens the untied slab at no size run (O130, addendum). T67: no replica of 96 opens or reaches a front; BREAKS in 22 cells of 24, SITS in 2 (the slowest feed at N = 576, out of time with the damage still rising, a break the run did not live to see); her inferred OPENS fails; ours (BREAKS everywhere) fails by the letter at N = 576 because the damage threshold scales with N and our fed range did not (O132; PREREGISTRATION T67, "Reading of stage 1"). Rule 11's sixth use on piece 5: her replacement is hers to propose. **T67's held-out size launched** (3 jobs, `cloud/queue/2026-10-17_t67_heldout.txt`) with the numbers written first (SITS at r = 1/16, BREAKS at the rest, no front); her word for L = 16 is owed and the inferred one is marked. To read: `t67_*l16` into `cloud/fetch/request.txt`, accept, commit unread, `python scripts/analyse_t67.py`. Next numbers: ASSUMPTIONS **O133**, VISION **Update 60**, PREREGISTRATION **T68**.
- **17 October, 08:32 UTC by the clock: T67's held-out size fetched, accepted unread, committed (058696cb) and read (O133).** At 1,024 points every cell's word is as written before it ran (SITS at r = 1/16 in all three modes, BREAKS at r = 1/4, 1 and 4), the medians inside the written ranges in 11 cells of 12 (one named miss: the spot feed at r = 1/4 broke at 6,200 sweeps, below 7,000), no front in 96 of 96; her inferred OPENS fails, ours holds. T67 is complete: a feed at a fixed rate opens the untied slab at no rate from 1/16 to 4 and no size from 256 to 1,024. Nothing is running in the cloud. Owed by her: her replacement for piece 5's mechanism (rule 11, sixth use; untried: a varying rate, a feed at many points); T66's repair and N = 1000 word; the curling-energy brief's answers. Next numbers: ASSUMPTIONS **O134**, VISION **Update 60**, PREREGISTRATION **T68**.
- **17 October, 15:20 UTC by the clock: T68 registered and launched on the owner's "proceed with these".** The two variants T67 named as untried, on T67's runner extended (`scripts/run_slab_feed.py`: schedules fixed, ramp, pulse as a cumulative feed; places shared, spot, spots of 16, all; T67's cells and seeds unchanged, `tests/test_t68.py`), at λ = 1.25, 1.40 and 1.60 (her question: T67 and T65 were at 1.25 only), L = 8 and 12 in one job, L = 16 held out; 36 Batch jobs (`cloud/queue/2026-10-17_t68_stage1.txt`, seeds 20266901 to 20266936); her prediction inferred (OPENS at some setting, from one spot) and marked so; ours, no (λ, N) reads OPENS. To read: `t68_*` into `cloud/fetch/request.txt`, accept, commit unread, `python scripts/analyse_t68.py` (all 36 cells in first), then `--write-prediction`, the dated amendment, her L = 16 word, `python scripts/make_t68_configs.py --held-out`. Her words of the day are in the notebook. Owed by her: her own word for T68; T66's repair and N = 1000 word; the curling-energy brief's answers (the ten questions of 15 October in the notebook); confirmation of the programme page's claim wording of 17 October. Next numbers: ASSUMPTIONS **O134**, VISION **Update 60**, PREREGISTRATION **T69**.
- **17 October, 15:40 UTC by the clock: the owner's answers on curling energy and X (VISION Update 60).** The curl-only store pays only for moves that add a surplus square without lowering the square count (the strict rule); X is the curled slab L × L × 4, likely with relics. The design brief is drafted, `docs/design/curling_energy_brief.md`, with the relic recap she asked for and the 64-point knot priced; it waits on two of her answers (what carries curling energy; what counts as a fold). Her idea of a slab patch's release opening a knot, her seam question and her FREE lean are recorded in the notebook, not decided. She was told T67 and T65 ran at λ = 1.25 only (T68 scans 1.25, 1.40, 1.60). Running: T68 stage 1, 36 jobs; to read as the 15:20 line says. Next numbers: ASSUMPTIONS **O134**, VISION **Update 61**, PREREGISTRATION **T69**.
- **17 October, 16:30 UTC by the clock: the fold defined (VISION Update 61, her "agree")**: a connected region of open space at two open directions, at least T54's completed patch, still there after the stores are empty; the seam's shift reported, not scored. The curling-energy brief now waits on one answer, what carries curling energy. A sandbox look the same afternoon (LOG): one 64-point knot given 0 to 1024 units opens at once and breaks past one direction's worth; not promoted. Her questions and ideas of the afternoon (a slab patch's release opening a knot; smaller curling costs; points created by the uncurling; the square count; a melted knot inside flat space) are in the notebook with the toy's arithmetic beside each. Next numbers: ASSUMPTIONS **O134**, VISION **Update 62**, PREREGISTRATION **T69**.
- **17 October, 22:35 UTC by the clock: T68 stage 1 fetched, accepted unread, committed (f7802417) and read (O134).** No replica of 1,728 opens or reaches a front at λ = 1.25, 1.40 or 1.60 under any schedule (fixed, ramp, pulse) or place (shared, one spot, 16 spots, every point); BREAKS in 166 cells of 216, SITS in 48, MIXED in 2; per (λ, N) MIXED everywhere. Two things learned: the break comes sooner and on less energy as λ rises, never a front; and a feed split over every point's own store is a threshold at the single-move wall, not a bath (37 cells frozen at 0 open, 0 broken), a property of per-vertex stores, disclosed. Her inferred OPENS fails; ours holds in its claim, wrong on one detail (pulses break on more energy). Rule 11's seventh use on piece 5: her replacement is hers; T69 (her other session, 17 October) is the exact test. **The held-out size launched**, 36 jobs (`cloud/queue/2026-10-17_t68_heldout.txt`) with every cell's word written first by one rule (`configs/t68_heldout_prediction.csv`). To read: `t68_*_l16` into `cloud/fetch/request.txt`, accept, commit unread, `python scripts/analyse_t68.py`. Owed by her: her own word for T68's held-out size.
- **17 October, 22:49 UTC by the clock: T69, the lowest path out of the slab, registered on her "I think yes, can we check?" and stage 1 read (O135).** A best-first search on the saddle over local switches (`scripts/exact_lowest_path.py`, tests, two configs). L = 8: no clean opening below a saddle of 64 at λ = 1.10 and 1.25 (the first clean state is two switches away with 16 open points), none at or below 53.6 at 1.40, nothing clean past 16 points below 64; MIXED, MIXED, NOT REACHED; her PAYS fails on its second half within the reach, ours not scorable and its 36 wrong. Memory set the reach (5,000 pops, up to 19 million children). **L = 12 running on the laptop** with its numbers written (the amendment of 17 October). Next: a second stage using the slab's symmetries, as an amendment before it runs. Also this evening: pandas declared as a dev dependency (CI had failed on it; green at d9e63148); her answers on net energy (a hill, not a toll) in the notebook. Next numbers: ASSUMPTIONS **O136**, VISION **Update 62**, PREREGISTRATION **T70**.
- **18 October, 01:15 UTC by the clock: T69's held-out size read (O135, addendum).** AS PREDICTED at λ = 1.10 and 1.40; at 1.25 the budget exhausted saddle 62, two below the predicted 64, so that cell is untested with nothing against the prediction. The price of a clean opening is 64 at both sizes where reached. Nothing of T69 is running; the second stage (the slab's symmetries, to reach past saddle 64) waits on her word and is registered as an amendment before it runs. Next numbers unchanged: ASSUMPTIONS **O136**, VISION **Update 62**, PREREGISTRATION **T70**.
- **18 October, 02:15 UTC by the clock: the owner's picture run as a rule, and three knobs adopted (VISION Update 62, her "All 3 yes").** Her words of the night are in the notebook (antimatter as the threshold payment; why opening must lose squares; pricing cubes; a count that grows; the whirlpool's closed point; only closed and open). Exact, in the notebook: every single switch from the slab leaves four broken points, so with breaking forbidden the toy's one move cannot move the slab. Sandbox (`sandbox/clean_feed.py`, LOG): with two switches at once and no point left broken, the slab fed at every point opens as ONE growing region (72 % at L = 8, 55 % at L = 12 when the look ended) climbing 4 units per point opened, no release before completion; the breaking control melts. A price on cubes was counted and runs the wrong way (LOG). Adopted: the move, the no-break store rule, pooled payment. Next: the kernel with rule-6 tests, then T70 (the climb at L = 12, 16, held out) with her prediction before launch. T68's held-out size reads at the 05:44 UTC check-in. Next numbers: ASSUMPTIONS **O136**, PREREGISTRATION **T70**, VISION **Update 63**.
- **18 October, 05:50 UTC by the clock: T68's held-out size, 30 of 36 cells fetched and accepted into `results/` unread.** Still running: `t68_ramp_spots_lam160_l16`, `t68_ramp_all_lam{125,140,160}_l16`, `t68_pulse_spots_lam160_l16`, `t68_pulse_all_lam160_l16`. Nothing of T68's held-out size has been read; `scripts/analyse_t68.py` is not run until all 36 are in (it prints each cell). To finish: a comment line in `cloud/fetch/request.txt` (the pattern `t68_*_l16` is already there), push, pull the inbox commit, `python3 scripts/accept_inbox.py --move`, commit unread, then read against `configs/t68_heldout_prediction.csv` and the amendment of 17 October 22:35 UTC. A check-in is armed for about four hours on.
- **18 October, 09:53 UTC by the clock: T68's held-out size, all 36 cells fetched, accepted unread (77f853c1) and read (O136).** 106 of 108 cells as written before the run; the two misses are marginal cells (the shared store at r = 1/16, λ = 1.60, fixed and ramped: SITS where the rule said they would break at about 18,400 to 18,700 sweeps); one matched BREAKS cell's medians 4 % over range; no front in 864 replicas; MIXED at every λ as written. Not AS PREDICTED by the letter, misses named; her inferred OPENS fails, ours holds; she has not given her own L = 16 word. T68 is complete at three sizes. Nothing is running in the cloud. Next: the clean-move kernel as a module with rule-6 tests, then T70 with her prediction before launch (VISION Update 62). Next numbers: ASSUMPTIONS **O137**, PREREGISTRATION **T70**, VISION **Update 63**.
- **18 October, 11:55 UTC by the clock: the contraction model (VISION Update 63, her "Okay let's adjust the model").** Points compact instead of breaking; the count varies. Her words in the notebook; the brief `docs/design/contraction_model_brief.md` holds the glossary, the mathematics (H unchanged with N varying; pair removal and insertion; the layer move, exactly the slab; the seam table), the three models side by side, and the tests in order. Exact looks (LOG, `sandbox/pair_moves.py`, `sandbox/partial_contraction.py`): only the whole layer compacts cleanly; every patch breaks 26 to 80 rim points and costs more than the slab, the same at L = 6 and 8. Owed by her: which form (local or layer) and the no-break rule under it. Nothing registered runs before that; nothing is running in the cloud. Next numbers: ASSUMPTIONS **O137**, PREREGISTRATION **T70** (fixed count) and **T71** (contraction), VISION **Update 64**.
- **18 October, 13:35 UTC by the clock: VISION Update 64 (hers: X is the straight curl; the spiral is the product's seam).** Prompted by `sandbox/spiral_contraction.py`: a shifted layer contraction is flat and stores nothing. Her antimatter question answered in the notebook (the energy is in the stores; "pooled" is where payment is drawn, not a place). Dynamical triangulations: a reading note from search summaries only (`docs/reading/notes/2026-10-18_dynamical_triangulations.md`; [Loll19] added, not read); the proxy refused every paper host. Still owed by her: the brief's questions 1 and 2. Next numbers: ASSUMPTIONS **O137**, PREREGISTRATION **T70**, **T71**, VISION **Update 65**.
- **18 October, 13:50 UTC by the clock: VISION Update 65 (hers: the whole-layer form).** The brief's questions 1 and 2 are closed (2 moot: no breaking move in the set). Exact for it: the ladder 10 → 8 → 6 → 4 is free until the last step, which costs 4(λ − 1) N exactly at L = 6 and 8 (LOG). Also hers: the shaped/unshaped split of energy confirmed; the fixed-count practice of dynamical triangulations adopted as a method (the brief, E5); time's clock is sweeps, the slab has none. Under the layer form the opening is one move: no front, no cancellation in the ledger; T71 tests timing and the ledger. Next: the kernel for the layer moves with rule-6 tests, E4 (reach), E5, then T71 with her prediction. Nothing is running in the cloud. Next numbers: ASSUMPTIONS **O137**, PREREGISTRATION **T70**, **T71**, VISION **Update 66**.
- **18 October, 14:50 UTC by the clock: her "Proceed" and "Confirmed"; two kernels built; T71 drafted.** The layer form's move set is decided (VISION Update 65, addendum): layer moves + the clean two-switch move; the single switch a control. `src/graphity/contraction.py` (layer moves, stores, feed, leak, gate, μ_N, a thermal chain over widths) and `src/graphity/clean_move.py` (the two-switch move) both carry rule-6 tests and pass. Exact, from the kernels: the slab's split is downhill, so a gate (a new knob, hers) is what makes X stable for now; the lump in the stores pays the fold back unless it leaks; with layer moves alone the width is exactly Boltzmann in μ_N N; the first clean switch step out of the slab costs 64 and opens 16 points (T69's state). PREREGISTRATION **T71** is drafted with three gate candidates and the leak arithmetic; **owed by her before launch:** the gate's value, her prediction, whether the feed stops at the burp; the runner and the analyzer are written and tested (`graphity.layer_feed`, `scripts/run_layer_feed.py`, `scripts/analyse_t71.py`); nothing is owed by us before launch. Nothing is running in the cloud. Next numbers: ASSUMPTIONS **O137**, PREREGISTRATION **T70** (reserved for the fixed-count switch-path test), **T72**, VISION **Update 66**.
- **18 October, afternoon: her ideas on flatness, inflation's stages, the scraps as seeds of structure and the black hole as a machine** are in `sandbox/NOTEBOOK.md` (18 October, last entry) in her words, each set against what the toy says exactly; nothing decided, nothing run. Her question about Brian Cox and Katie Mack: `docs/reading/notes/2026-10-18_cox_mack.md` (search summaries; nothing found that bears on the toy). T71's three owed items are unchanged. Later the same afternoon: her stages of a turn's yield (the eras, observers per planet, the observation window, heat death against a rip) in the notebook, with `docs/reading/notes/2026-10-18_far_future_and_observation_window.md` (search summaries) as the published terms for piece 12's function. On her "Proceed": the sandbox look at the knots' positions in the 600 saved T51 sheets (`sandbox/knot_positions.py`; LOG, 18 October): clustered on a few columns, random beyond, set at the opening; the scraps' own layout is white noise at large scales, so "scraps as the seeds of structure" survives only as scraps falling into seeds laid by something else.
- **18 October, 20:25 UTC by the clock: VISION Update 66 (hers: after the burp the lump leaves one way into a daughter; the slab reforms; the feed continues).** Built into the T71 protocol as a daughter ledger (`graphity.layer_feed` release_to "daughter"; runner, analyzer and tests updated: words CYCLES / ONE BURP, the energy per daughter, the period). Exact from the kernel: the parent converts the whole feed into daughters of exactly a N_slab each (61 × 144 = 8,784 = the energy fed at L = 6, r = 1/16, 600 sweeps); the gate sets only how long X sits; the births fall at the same sweeps at L = 6 and 8 for the same seed. T71's draft carries Amendment 1 (f3 the model, f1 the reference, f2 not run; our predictions rewritten). **Still owed by her before launch: the gate's value and her prediction.** Piece 12's function is written as `docs/design/loop_measure_brief.md` (ours; the terms, the stages, the combination rule left to her). Nothing is running in the cloud.
- **18 October, 20:54 UTC by the clock: VISION Update 67 (hers: piece 12's combination rule).** Per universe for universes of one setting that differ only by a quantum outcome; the growth-rate rule for when an observer is most likely to exist between a universe's birth and the end of its life-supporting stars. The brief (`docs/design/loop_measure_brief.md`, section 4) carries the decision and, ours and unverified, the youngness consequence of the second rule. Her "Yes this makes sense" on the converter reading is in the notebook.
- **18 October, 21:30 UTC by the clock: her question on the youngness consequence, answered in the brief (section 4) and the notebook.** Late observers (red dwarfs to 10^13 years, the last at 10^100) cannot balance the across-the-tree weight; only late births can, and more than about three daughters per universe in the first 10^10 years already sets the weight; her instinct (count per universe, every universe lined up at its birth) is the reading her own picture supports, since the hypothesis has no common clock across universes. Her red-dwarf point bites the other way in the per-universe count ([LBS16]: at most 0.1 % chance of an observer as early as now), and her observation-window term W(t) is what answers it. Also hers: the versions are Everett's branches ("I believe they are"), recorded as her position in the brief's rule (i). Her word on which reading rule (ii) means is still owed; T71's gate and prediction are still owed.
- **18 October, 21:45 UTC by the clock: her lean toward late births ("yes this makes sense"; holes birthing now still running at 10^50 years), set against the published infall history.** Under the converter a hole births only while fed; the far-future literature (search summaries) has the feed front-loaded, a late minority tranche at about 10^20 years, and nothing after; and the early floor is per universe over all its holes, so 10^20 holes birthing once each early gives e^(−60) at our age. Across the tree, trillions of daughters and the converter do not fit our age together; the per-universe reading needs none of it. Notebook, brief section 4, the far-future reading note. Her word on the reading and T71's gate and prediction are still owed.
- **18 October, 21:55 UTC by the clock: VISION Update 68 (hers: rule (ii) read per universe by each universe's own age; clocks exist only inside a universe).** Her words in the notebook; the brief's sections 4 and 7 carry the decision and what the function now predicts (an observer at the age its universe forms habitable planets, inside the observation window; W(t) load-bearing against [LBS16]'s 10^13 years; not scored on our age, rule 13). Piece 12 is fully specified as a function; nothing in it is a knob or a run. T71's gate and prediction are still owed.
- **18 October, 22:10 UTC by the clock: her shorteners for "when we are" (a rip; dark energy pulling galaxies apart; no interaction between planets) put through the Stage E population model as a sandbox look** (`sandbox/when_we_are_shorteners.py`; LOG). A rip brings the peak forward but the data lean away and it cuts against her heat-death argument; a constant dark energy shortens only the window she already has; "no interaction" does nothing as a factor and much as a rule for who counts (each civilization once: peak near 5 Gyr, nine tenths before today). Notebook and the brief's section 7. Nothing decided; T71's gate and prediction still owed.
- **18 October, 22:15 UTC by the clock: her two proposed sentences for paper 1 (the fixed count a setting; breaking allowed and required under the published move) drafted as candidates in `docs/papers/curled_torus/v2_changes.md`, not applied (the paper is hers and held).** T71's registration gains a plain-words block ("What the owner is asked") on the gate and the prediction, and a dated correction of one arithmetic slip (g2 is reached before g1 at every size run). Still owed: her gate and her prediction.
- **19 October, about 01:30 UTC by the clock: VISION Update 69 (hers: the gate is g1, a N_slab); her T71 prediction recorded (Amendment 2, verbatim, scored by the move sets she names since her letters A and B are swapped against the registration's); T71 launched, 12 Batch jobs** (`cloud/queue/2026-10-19_t71_stage1.txt`: per curling cost 1.10, 1.25, 1.40 the model arm, layer moves alone with the daughter rule, layer moves alone with the release to the stores (the f1 reference), and the single-switch control under `run_slab_feed`; L = 8 and 12; r = 1/64, 1/16; 16 replicas; max(2000, 40 a / r) sweeps). Before launch the kernel's logging changed: rows at every move and every 50th sweep (`layer_feed` `log_events`), the analyzer reading the release from the last row before the split and the shares time-weighted, with a test that it reads the same as logging every sweep. To read: `t71_*` is in `cloud/fetch/request.txt`; push a comment line when the jobs finish, `python3 scripts/accept_inbox.py --move`, commit unread, `python3 scripts/analyse_t71.py`, then the held-out words for L = 16 as a dated amendment, her word for L = 16, and the L = 16 configs. The control cells are read with T68's analyzer's words (BREAKS / SITS) from the `t71_control_*` files.
- **19 October, about 01:35 UTC by the clock: her T71 prediction for layer moves alone revised to CYCLES in every cell (Amendment 3), on the kernel's exploratory check, after launch and before any cell was fetched or read; her original words stay in Amendment 2.** The two predictions now agree in every arm.
- **19 October, about 02:10 UTC by the clock: the programme artifact brought to today's state (Version 92, https://claude.ai/artifact/JLtR2aqHmL2FghWmNZU8xW), now published from `docs/public/programme.html`, which had drifted (the file at 5 October, the artifact at 15 October, the draft at 17 October); the claim carries her decisions of 16 to 19 October, marked hers once she confirms; pieces 3, 5, 7, 11, 12 and 14 and the waiting-on list rewritten; `docs/papers/programme_draft.md` gains a 19 October addendum.** A handoff on how the process and the toy could improve is `docs/HANDOFF_2026-10-19_process_and_toy.md` (ours; nothing decided): a two-lane test rule for her word, one home for the programme page, a fixed form for her predictions, what T71 can decide, the gate against a wall, the daughter as a ledger, what the toy supplies to the measure.
- **19 October, about 02:10 UTC by the clock: her question on the supernova age-bias claim (the expansion no longer accelerating; Son, Lee et al. 2025; rebutted by Wiseman, Riess, Schmidt 2026; replied to May 2026) answered in the notebook and the far-future reading note from search summaries (the proxy refused every source).** Unresolved; if it held, the observation window that rescues our age under Update 68 would lengthen, and dark energy as a constant of space would need a source that changes. Nothing decided.
- **Next record numbers (19 October, 02:10 UTC):** ASSUMPTIONS **O137**, PREREGISTRATION **T70** (reserved), **T72**, VISION **Update 70**.
- **The outside review of 11 October is recorded as O120.** Its proposed rewrite of paper 1 is the branch `codex/paper1-review-corrections-2026-10-11` (33be5462), not merged: adopting it is the owner's decision. That branch numbers its own geometry audit O118, which is T54 here; renumber at merging. Its reports are local, `.tools/independent-review-2026-10-11/`.
- **The flat end states by kind** (O116, last addendum; `scripts/read_flat_kind.py`): one torus six around in 98 %, the rest separate pieces, a few of them one-sided (Klein bottles). An end state with H = 0 is not thereby one torus.

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
  **Her word later that day:** the second-curl prediction is not discussed on the programme page unless real
  evidence appears of an unknown mechanism adding to the tail; the page says what was found (Version 64), and the
  registration keeps the prediction as written.
- **T59, pre-registered 10 October, 17:50 ET, and launched on the laptop** (`scripts/make_t59_configs.py`,
  `scripts/run_first_exits.py`, `scripts/analyse_t59.py`; 54 configs `configs/t59_*`). The owner asked whether
  closing paper 1's two loose ends on the count would make it more complete. Stage A1: T8's decay 11 at N = 96
  (78,205 sweeps) replayed block by block. Stage A2: T22's seven first exits later than four mean waits at
  λ = 1.05 replayed with what the chain was offered tallied. Stage B: fresh first exits at λ = 1.05 counted move by
  move, 2,000 at N = 64 and 1,000 at N = 96. Stage C: 4,000 at λ = 1.30, N = 64, on the move clock and on a look
  every five sweeps. What is exact going in: the waiting torus's three classes share one census, so the first exit
  should be exactly memoryless; T22's two first exits near 9.7 mean waits then have a chance of about 1 in 70,000.
  One target was seen before the registration (T22's replica 7 at N = 64, offered three cheapest exits a sweep
  throughout) and is disclosed there. **Her prediction was recorded at 18:17 ET, before any reading: chance, and
  exits hidden between two looks (both as ours). Nothing of T59 has been read; when every file is in, run
  `python scripts/analyse_t59.py` and read the four parts in its order.**
  **VISION Update 53 (18:22 ET):** her clarification that "her bar" of Update 26 meant continued interest, not a
  lower bar for scoring; a fourth map, if she asks for one, keeps the registered bar, times the waits without
  the detector, and names a held-out size first.
  **Read at 18:29 ET, stages A1 and C only** (PREREGISTRATION T59, "Reading"): T8's long wait at N = 96 read as
  the tube at every look for 78,205 sweeps (TRUE WAIT); at λ = 1.30 the first exit counted by the move is
  1.005 ± 0.016 of the count and a look every five sweeps reads it 0.096 ± 0.007 later, 94 % of that from first
  exits that came back before the look (HIDDEN EXITS; her prediction and ours hold). **Read in full by 22:38 ET
  (O112):** T22's seven long first exits were offered exits at the counted rate throughout and took none
  (OFFERED AS COUNTED); 3,000 fresh first exits at λ = 1.05 have means 0.992 ± 0.023 (N = 64) and 0.946 ± 0.031
  (N = 96) of the count with one beyond 8 mean waits where 1.0 is expected (ON THE COUNT; her "chance" holds).
  Both editions of paper 1, the supplement, the manifest (57 files) and the blog pages carry it (commit
  dec10c6e); the marketing branch has the copy.
- **T60, the λ map a fourth time, pre-registered 10 October, 18:45 ET, at the owner's "Proceed"**
  (`scripts/make_t60_configs.py`, `scripts/analyse_t60.py`, 28 configs `configs/t60_*`,
  `cloud/queue/2026-10-10_t60_stage1.txt`). T24's grid and protocol with fresh seeds; the one repair is the clock:
  the wait is the first look at which a decay stopped being the tube, with no watch and no threshold. The bar is
  T23's and T24's. Her prediction stands from those runs (sharp across the window; break-up at the edge). Rule 14:
  N = 288 is held out; after stage 1 is read, `python scripts/analyse_t60.py --write-prediction`, a dated
  amendment, **her prediction for N = 288**, then `python scripts/make_t60_configs.py --held-out` and a queue file.
  Ours for 288: one front is the criterion at risk at the top of the window. No fifth run is planned.
  **State at 22:46 ET, 10 October:** the queue workflow succeeded at 19:16 ET; 27 of the 28 cells are fetched,
  checked and in `results/` (commit c864aac7); `t60_lam135_n192` had not finished after three fetches. **Nothing
  of T60 has been read.** Do not run `scripts/analyse_t60.py` until all 28 are in. T53's resubmitted cell came
  with the same fetch and is read (DAMAGED; its window verdict is no longer provisional).
  **Stage 1 read at 23:13 ET, 10 October (O113; PREREGISTRATION T60, "Reading"): SHARP ACROSS THE WINDOW, and
  BREAK-UP BEGINS AT THE EDGE.** The memoryless check holds in all 28 cells with the new clock; T24's three window
  failures do not recur. The numbers for N = 288 were written from stage 1 alone and committed (c484d2ec) and
  stage 2 was queued in the same push. **Her prediction for N = 288 is owed before stage 2 is read.** Paper 1 does
  not yet say any of this: it waits for stage 2 and for a red-team pass by a fresh read-only reviewer (rule 12).
  New in the kernel folder: `graphity.exits.first_exit_clocks` and `offers_until_exit` (T22's chain, draw for
  draw), and `graphity.results.provenance` (the commit and a dirty flag in a run's meta; TASKS, the reviews of
  6 October, item 5, for new runners only so far).
- **Bianconi's entropy action on our wirings (O111, 10 October; series paper 10).** At the owner's request for a
  letter to Ginestra Bianconi with a replication and a question: `scripts/exact_entropy_action.py` builds the
  operators of [Bia24] on the flat torus, the tube, a re-glued tube and a gas of 4-cubes at 64 points and evaluates
  her action. In her vacuum it is one number per cell; at the identity metric the order is the same; both ways it
  grows more negative with every square; across 445 saved wirings it acts like this model's energy with a
  coefficient below 1. The draft letter is local (`docs/outreach/`), and nothing is sent from a session.
- **Drafts of series papers 10 and 11, in two versions each (10 October, at the owner's request).** Paper 10:
  `docs/papers/entropy_action/paper.tex` (three pages) and `plain_language.md`. Paper 11:
  `docs/papers/gravity/paper.tex` (the 25 September draft, retitled "A pull between leftovers" and given a section
  on where the two routes stand) and `plain_language.md`. Both connect to piece 8 of the programme page; paper 11
  also rests on piece 7's knots. Neither has been read by her yet. **VISION Update 52** (her lean on the three
  shares) and the programme page's piece 6 (Version 65) are hers to confirm or correct.
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
    the same branch again (commit `17acde2`, pushed after the merge), which she also merged (pull request 57) and deployed: **the blog is
    live** with the corrected text. Later the same day, at her note that "mathematicians call the shape a torus"
    read as if torus meant the flat sheet only, the plain edition says every shape in the paper is a torus, told
    apart as flat, curled and knot (four sentences and a row of the translations table; the web page's quick
    answer too); rebuilt and copied to the same branch again, which needs a third pull request. No analytics tag
    of the site's own is on sidenerdapps.com, so nothing counts the blog's visits yet. Copy again after any
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
- **Next record numbers (superseded by the 11 October addendum):** ASSUMPTIONS **O114**, VISION **Update 54**, PREREGISTRATION **T61**.

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
   `docs/papers/programme_draft.md`, current to 10 October (pieces 1 and 2, the papers' state and what is waiting
   to be read; the rest is the state of 9 October); the artifact was republished from it on 10 October as Version 63. `docs/public/programme.html` is older and not maintained by hand.
8. **Environment.** The interpreter with the project's dependencies is the Microsoft Store one,
   `~/AppData/Local/Microsoft/WindowsApps/python3` (NumPy 2.0, Numba, pytest); bare `python` and `.venv` lack NumPy.
   Run `pytest -q > log; echo $?` and read the status; never pipe pytest through `tail`. Long scripts go in a file with
   the Write tool (the shell cuts long heredocs). Background runs: `nohup <py> scripts/... > log 2>&1 &`.

## Addendum, 12 October 2026 (a second line of work; the toy's state above is unchanged; the branch's state at the end of the day is the last three bullets)

- The owner's handoff `docs/theory/observer_relative_histories_research_handoff.md` (observer-relative histories in a
  Level-2 Everettian universe) was worked through its Stages A to F on the branch
  `claude/observer-relative-histories-2026-10-12`, in a separate git worktree because the shared working tree was
  72 commits behind `main` and held another session's uncommitted edits. Everything is in one place:
  `docs/theory/orh_findings.md` (read it first), then the Stage A map, the assumption register (P1 to P24), the
  plan, the six reading notes of 12 October and the prior-work note (FOUND on all three of the handoff's candidate
  claims). Code `src/orh/` with `tests/test_orh_*.py`; results `results/orh_stage_bcd.csv`, `results/orh_stage_e_*.csv`;
  figures `docs/figures/orh_*.png`. ASSUMPTIONS O125 is the pointer. At the owner's request the programme artifact and `programme_draft.md` were
  arranged the same afternoon as a book in seven chapters (the burp to the view from outside the loop), with two
  draft pieces from this line, marked ours: 13 (interference and records, beside piece 9) and 14 (observers inside
  the loop, the last chapter); hers to keep or drop.
- Later on 12 October: `origin/main` merged into this branch (main had used O120 and O121; this branch's entry, numbered O119 there, collided with main's O119 (the flat tori counted) and was renumbered O125 at the merge of 12 October). The owner's framing recorded: she does not need this line to be new; "already published" is the result wanted, to be applied to her theory. Her question on the loop answered in section
  10 of the findings page (ours, unverified: a Born-weighted measure, the view from outside as the decoherence functional, a record-erasing turn boundary; a two-turn toy test proposed, not registered). Piece 9 updated on the page and the draft; the claim's last sentence revised for her confirmation; the provenance
  paragraph under the claim removed at her request.
- **State of the branch, end of 12 October.** `claude/observer-relative-histories-2026-10-12` is merged with `main` as
  it stood after PR #49 (main's merge of the paper 1 branch `claude/paper1-after-review-2026-10-12`); three conflicts,
  all bookkeeping (the queue status and inbox snapshots take main's newer copies; the sandbox notebook keeps both
  sides' 12 October entries in day order); no code or result changed in the merge. Then a fresh reviewer's findings on
  the branch were fixed in the working tree, uncommitted at this writing (Emily commits; nothing under `results/`
  changed, which `git status` confirms). One line each:
  - **Provenance helper** (`graphity.results.provenance`): now runs `git status` with untracked files included, so an
    untracked file makes `git_dirty` true, with two new fields, `git_untracked_count` and `git_untracked`; tested in a
    temporary repository. Why: the three ORH meta files name commit e59d87ba, which holds nothing under `src/orh` (the
    code was first committed with the results as c23803cf). The meta files stand (rule 5); a dated provenance note on
    the findings page and an addendum to O125 record it; a re-run reproduced all three CSVs line for line.
  - **Stage E reference classes:** the run's `late` class was never declared and the declared "uniform over observers"
    never ran (two of three ran as declared). Dated entries in the plan, in P20 and on the findings page say exactly
    what was written when: the three run classes were in P20 at c23803cf; the replacement was noted nowhere until
    12 October. No number is claimed for the class that did not run.
  - **Findings page:** the fifth kind of statement, "model output", withdrawn with a dated line (Stage E is exact
    arithmetic on declared inputs, exploratory, every reading ours); the nested-records, conditional-total and
    conserved-weight checks relabeled as checks of the code, not findings.
  - **Figure 6** (`docs/figures/orh_stage_e_f_today.png`) redrawn: four late-weighted values below the axis floor are
    shown on the floor as open markers, the three classes labeled, the legend pointing to
    `results/orh_stage_e_summary.csv`; `scripts/orh_stage_e.py --figures-only` redraws it without touching `results/`.
  - **REFERENCES.bib:** ten entries added for works cited on the ORH pages with none (Kipping 2025 and 2021, Behroozi
    and Peeples, Lingam and Loeb, Cirkovic and Balbi, Blume-Kohout and Zurek, Page and Wootters, Vaidman's SEP entry,
    1998 and 2012); each note gives the read status; author-and-year-only entries say "details to verify".
  - **Programme draft:** piece 9's status softened to a candidate proposed to the author (ours, unverified; it reads the
    model's renamings as Everett's branches, untested), with the softening line placed newest first in its log; piece
    13's "are Everett's branches" marked an identification, not a result; piece 14's Stage E sentence marked an
    exploratory population model and its Born-weighting made conditional; header date 12 October, no clock time.
  - **ASSUMPTIONS and CLAUDE.md:** O123's heading carries the λ dependence (the floor 1 − (λ − 1)/4 less the push's
    share, zero at λ = 5); O125 gains the provenance addendum; CLAUDE.md's 12 October paragraph is split into lessons
    and facts. **Plain-language edition:** four sentences that said "melted" of a sealed box reworded, PDF rebuilt.
  - **Left as nits, not fixed:** British "labeled" on the findings page and at line 1492 of the plain-language
    edition; the programme draft's piece 14 row still says "model output on published equations"; the share by today
    reaches 0.96 in the summary CSV where the draft says 0.9 and the findings page 0.92; the claim paragraph reads
    firmer than piece 9's status (hers to settle, below).
- **State of the branch, 13 October.** Merged with `main` again, as it stood after PRs #51 and #52 (the vocabulary
  pass for condensed-matter readers, paper 2's rewrite, blog post 02), so that it merges into `main` without
  conflict. Four conflicts: the bibliography, this page and the sandbox notebook keep both sides' additions in day
  order; paper 1's plain-language PDF, which each side had built, is rebuilt from the merged source (the four
  reworded "melted" sentences of 12 October together with main's two added sources; 36 pages). From that source
  the release manifest was regenerated (three hashes change: ASSUMPTIONS.md and the plain edition's source and PDF)
  and post 01's plain-language page was rebuilt with its PDF copy (`scripts/build_main_nerd_pages.py
  --skip-figures`; three lines of the page change). **The copy in the marketing repository
  (`feat/main-nerd-post02-2026-10-13`) was made from main's pages before this, so by that account it lacks those
  three lines and the new PDF; not checked there.** No code or result changed; 1069 tests pass on the merged tree.
- **Open for the owner, exactly:** (1) whether the T64 rerun and its bar stand as her decision (T64 is T63 on fresh
  seeds with the control's rule written from paper 1's record, a second attempt; its held-out size N = 384 is queued
  and O127 waits on it); (2) whether the Stage E numbers stay on the programme page (piece 14) while the config that
  produced them is exploratory, which she tabled; (3) the claim's last sentence, the amplitude-and-record rule, awaits
  her confirmation (until then the 9 October sentence, "the rule that lets them cancel is still to be found", is the
  confirmed one); (4) the cloud `.meta.json` files say `git_commit: unknown` (40 in `results/`: T62, T63 and T64),
  because the Batch container has no checkout; a container issue, not fixed here.
- **Next record numbers after this branch:** ASSUMPTIONS **O126** (the "O122" written here earlier was stale: main had
  used O120 to O124 by the merge), VISION **Update 57**, PREREGISTRATION **T65**.

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
