<!-- DRAFT, 23 October 2026, sandbox (untracked). For PREREGISTRATION.md section T74, to go below "Reading of T74".
     Nothing here is committed, and nothing at L = 16 has been written or run. Every number below comes from the
     commands listed under "Sources". -->

### Amendment 6 (23 October 2026, before L = 16 runs): the held-out numbers

Rule 14 and T74's Standing requirement 1 ask for a number with a range for the held-out size L = 16, written from the
two stage-1 sizes before L = 16 runs. This amendment writes them from the 108 stage-1 files alone (L = 8 and 12, read
21 October, O145). No L = 16 config, job or result exists. The six-link track is kept by her decision of 23 October
(VISION Update 95), which released this work; the L = 16 runs still wait for her word below.

**What in T74 is a claim about size.** One registered claim, and three reads of whether stage 1 repeats:

1. **The period between births does not change with L** (Standing requirement 1, the registered size claim, and the
   only one the size verdict scores). T74 calls it "the period per point". The feed R, the cap c and the gate
   a N_slab are all proportional to N_slab, so the period in sweeps is the quantity that exact item 1 says does not
   depend on L: a N_slab / min(c, R), which is 16a at c = 2R and 32a at c = R/2. It is also what
   `scripts/analyse_t74.py` reads (the mean period over fed-phase births). *Ours: this reading of "per point" is for
   her to confirm.*
2. **The fed word.** The shared prediction says BURPS in every fed cell, at every λ and size (Amendment 2, item 5;
   Amendment 5). At stage 1 it failed in 6 cells of 108 (O145). What is read at L = 16 is whether the stage-1 rate
   repeats, failures included.
3. **The timing words.** The shared prediction says SAME TIMING, with SPREAD ONLY where c = 2R and the meals are large.
   At stage 1 it failed in the two λ = 1.10 settings of that kind (O145). Read the same way.
4. **The unfed words.** The shared prediction says cold DISSOLVES; warm FED BY ITS SURROUNDINGS; equal by the side of
   2a. At stage 1 it failed in 2 cold cells of 36 and in 12 of the 18 equal cells it could score (O145). Read the same
   way.

The other reads (the share of the feed that entered the slab, the loss rate against c, the length of digestion, the
residual) make no claim about size. They are reported at L = 16 as at stage 1 and are not scored.

**The fit and the range (ours; T74 names neither).** Every claim and read above says that something stays the same as
L grows. So the fit is a constant: L = 8 and 12 pooled. The range answers one question: what would L = 16 show if the
claim holds? Under that claim, stage 1 and L = 16 are two samples of replicas from one population, so the range has to
carry the error of both: the scatter of the L = 16 sample and the fit's own error. We drew both 10,000 times from the
stage-1 replicas themselves, with replacement (numpy seed 20261023): in each draw a fresh stage 1, as many replicas as
stage 1 had, and a fresh L = 16, as many as L = 16 will have. A number's range is its stage-1 value plus the middle
99.7 % of (fresh L = 16 value − fresh stage-1 value). For a word, the fresh L = 16 replicas are drawn from the fresh
stage 1, so the stage-1 rate itself varies from draw to draw. The sizes:

- Period and timing: per (λ, c, feed), a fresh 96 and a fresh 48 from the 96 of stage 1. The reservoir is isolated
  while fed, so the background does not touch the fed phase, and the analyzer pools the three backgrounds the same way.
- Fed word: per (λ, feed, c), a fresh 96 from its 96, then 16 per cell from those. Digestion is isolated too.
- Unfed word: per cell, a fresh 32 from the cell's 32 at L = 8 and 12, then 16 from those.

So the width of each period range is the spread of a 48-replica mean, plus the fit's own error, and nothing else. A
change with L larger than that is what a miss would show.

*A check of the rule, on data already read (not a prediction):* the same rules fitted on L = 8 alone put every L = 12
number inside: 18 of 18 periods, 12 of 12 timing words, all 48 fed cells that had to BURPS, all 32 unfed cells that had
to repeat, and 19 of the other 22 unfed cells on their most likely word (range 15 to 22). That is weak evidence. A rule
that leaves out the fit's own error, and so is too narrow (each period range covering about 96 % when a fit of 48
replicas predicts 48, and 89 and 91 % at λ = 1.10, c = 2R with meals), would still put all 18 periods inside about
four times in ten (0.43 by resampling). So the check shows the rule is not grossly wrong, not that it holds its stated
99.7 %.

*Said plainly:* the size verdict below reads 18 ranges at once. If the claim is true, at least one misses by chance
about one time in seventeen: 0.060, measured with a separate two-level draw of 40,000, in which each range missed 0.25
to 0.48 % of the time against 0.3 % nominal (1 − 0.997¹⁸ = 0.053). A single miss is reported as a miss, by name, and
then examined (rule 11).

**1. The period between fed-phase births, in sweeps, at L = 16** (48 replicas, the three backgrounds pooled; stage-1
values measured; fit and range ours; a N_slab / min(c, R) exact):

| λ | c | feed | L = 8 | L = 12 | **L = 16: fit (range)** | a N_slab / min(c, R) |
|---|---|---|---|---|---|---|
| 1.10 | 2R | steady | 6.428 | 6.431 | **6.430 (6.415 to 6.445)** | 6.40 |
| 1.10 | 2R | meals of 16 | 6.463 | 6.438 | **6.451 (6.405 to 6.512)** | 6.40 |
| 1.10 | 2R | meals of 256 | 6.532 | 6.460 | **6.496 (6.311 to 6.749)** | 6.40 |
| 1.10 | R/2 | steady | 12.787 | 12.783 | **12.785 (12.778 to 12.792)** | 12.80 |
| 1.10 | R/2 | meals of 16 | 12.785 | 12.787 | **12.786 (12.779 to 12.793)** | 12.80 |
| 1.10 | R/2 | meals of 256 | 12.784 | 12.787 | **12.786 (12.777 to 12.794)** | 12.80 |
| 1.25 | 2R | steady | 15.953 | 15.956 | **15.954 (15.940 to 15.968)** | 16.00 |
| 1.25 | 2R | meals of 16 | 15.969 | 15.965 | **15.967 (15.954 to 15.980)** | 16.00 |
| 1.25 | 2R | meals of 256 | 15.651 | 15.659 | **15.655 (15.637 to 15.674)** | 16.00 |
| 1.25 | R/2 | steady | 31.880 | 31.871 | **31.875 (31.845 to 31.905)** | 32.00 |
| 1.25 | R/2 | meals of 16 | 31.904 | 31.897 | **31.901 (31.870 to 31.931)** | 32.00 |
| 1.25 | R/2 | meals of 256 | 31.885 | 31.879 | **31.882 (31.847 to 31.915)** | 32.00 |
| 1.40 | 2R | steady | 25.452 | 25.468 | **25.460 (25.422 to 25.498)** | 25.60 |
| 1.40 | 2R | meals of 16 | 25.431 | 25.437 | **25.434 (25.407 to 25.463)** | 25.60 |
| 1.40 | 2R | meals of 256 | 25.124 | 25.139 | **25.132 (25.103 to 25.162)** | 25.60 |
| 1.40 | R/2 | steady | 50.877 | 50.907 | **50.892 (50.816 to 50.969)** | 51.20 |
| 1.40 | R/2 | meals of 16 | 50.896 | 50.900 | **50.898 (50.832 to 50.967)** | 51.20 |
| 1.40 | R/2 | meals of 256 | 50.896 | 50.933 | **50.915 (50.839 to 50.988)** | 51.20 |

The ranges reach no more than 0.15 % from the fit everywhere except at λ = 1.10, c = 2R. There they reach up to 0.25,
0.96 and 3.90 % from the fit, because rare clean switch moves (O144, O145) take energy from a few daughters. Every fit
lies within 2.2 % of exact item 1's a N_slab / min(c, R). That number is the same at every L by arithmetic; it is
shown, not scored, and it is not a floor: 15 of the 18 fits lie below it. Every range also lies well inside ±10 % of
its fit, the registration's own tolerance for "the same mean period" (SAME TIMING). So a period that misses its range
but stays within 10 % is reported as MISSES, with that said beside it.

*Verdict word:* T74 names none for its size claim. We propose **HOLDS** if the L = 16 period lies in its range and
**MISSES** if not, as in T54 and T56, for her word.

**2. The fed word at L = 16.** Its words are unchanged: BURPS / NEVER BURPS / MIXED per cell, read by
`scripts/analyse_t74.py` as at stage 1.

- *Measured:* 51 of 54 cells BURPS at L = 8 and 51 of 54 at L = 12. Of the 96 replicas of each (λ, feed, c), 16 of
  the 18 settings had every replica's fed daughters exact. The exceptions are at λ = 1.10, c = 2R: 7 of 96 replicas
  short with the large meals and 1 of 96 with the small, each after a clean switch move in the fed phase. That is 4 of
  144 such replicas at L = 8 and 4 of 144 at L = 12 (7 moves at each): too few to tell a constant rate from one that
  grows with the points. A rise at L = 16 would show as MIXED where stage 1 had none, or as more MIXED among the six
  cells below, which their allowance cannot detect.
- **L = 16, read cell by cell:** the 48 cells of the 16 settings in which every stage-1 replica was exact must BURPS;
  every draw gives BURPS there. The six λ = 1.10, c = 2R meal cells BURPS in about 0.86 of the draws with the small
  meals and 0.33 with the large, once the stage-1 rate's own error is counted. Any mix of BURPS and MIXED among those
  six lies inside their 99.7 % range (0 to 6 of 6 BURPS), so they are reported, and they change the read only by
  NEVER BURPS, which no draw gives (every stage-1 replica made at least 156 fed daughters).

**3. The timing words at L = 16.** Its words are unchanged: SAME TIMING / SPREAD ONLY / DIFFERENT TIMING, the
backgrounds pooled.

- **The same word as at both stage-1 sizes in all 12 settings.** SPREAD ONLY applies to c = 2R with the large meals
  at λ = 1.25 and 1.40. SAME TIMING applies to the other 10, including λ = 1.10, c = 2R, large meals, where SPREAD
  ONLY was first predicted. Every one of the 10,000 draws gave these words.
- Written beside the words, and not part of the verdict (ours): the ratios with their 99.7 % ranges. For c = 2R and
  large meals:

| λ | mean ratio | cv ratio |
|---|---|---|
| 1.10 | 1.010 (0.982 to 1.048) | 1.30 (1.22 to 1.40) |
| 1.25 | 0.981 (0.980 to 0.983) | 3.26 (3.19 to 3.33) |
| 1.40 | 0.987 (0.985 to 0.989) | 2.66 (2.58 to 2.74) |

  In the other nine settings the ranges of the mean ratio lie within 0.9954 to 1.0129, and those of the cv ratio
  within 0.87 to 1.10.

**4. The unfed words at L = 16** (18 cells per background). The words are unchanged: WAITS / DISSOLVES / FED BY ITS
SURROUNDINGS / MIXED. For the equal background, the shared prediction is still SPLIT and not scored where replicas
lie on both sides of 2a (Amendment 4, item 3).

- **Read cell by cell. 33 cells must repeat their stage-1 word**, the one word given at both L = 8 and 12 and in at
  least 99.7 % of the draws:
  - cold, DISSOLVES: 14 cells, all but λ = 1.10 with c = 2R (steady and small meals) and λ = 1.10 with c = R/2
    (steady and large meals);
  - warm, FED BY ITS SURROUNDINGS: 16 cells, all but λ = 1.10 with c = 2R (steady and small meals);
  - equal: λ = 1.10, small meals, c = R/2, MIXED; λ = 1.25 and 1.40, large meals, c = 2R, WAITS.
- **The other 21 cells are read together:** the number of them that give their most likely word at L = 16 lies in
  **14 to 21** (median 19). Their most likely words:

| background | cells | most likely word at L = 16 (share of draws) |
|---|---|---|
| cold | λ = 1.10, c = 2R, steady and small meals | MIXED, both bars (0.58, 0.57); stage 1 gave DISSOLVES at one size and MIXED, both bars, at the other |
| cold | λ = 1.10, c = R/2, steady and large meals | DISSOLVES (0.995, 0.994) |
| warm | λ = 1.10, c = 2R, steady and small meals | FED BY ITS SURROUNDINGS (0.99, 0.98) |
| equal | λ = 1.10, c = 2R, steady | FED BY ITS SURROUNDINGS (0.73) |
| equal | λ = 1.10, c = 2R, small meals | FED BY ITS SURROUNDINGS (0.58); stage 1 gave MIXED at L = 8 and FED BY ITS SURROUNDINGS at L = 12 |
| equal | λ = 1.40, c = 2R, small meals | WAITS (0.73) |
| equal | the other 12: λ = 1.10, steady with c = R/2 and large meals with either cap; λ = 1.25, steady and small meals with either cap and large meals with c = R/2; λ = 1.40, steady with either cap and small and large meals with c = R/2 | MIXED (0.84 to 0.996) |

- If the stage-1 rates hold, this read repeats stage 1 in 0.997 of the draws.
- *Reported, not scored:* the tallies per background, and the number of equal cells the SPLIT rule leaves scorable.

| background | count | L = 8 | L = 12 | L = 16: median of the draws (range) |
|---|---|---|---|---|
| cold | DISSOLVES | 17 | 17 | 17 (15 to 18); the rest MIXED, both bars met |
| warm | FED BY ITS SURROUNDINGS | 18 | 18 | 18 (17 to 18) |
| equal | cells scored (not SPLIT) | 8 | 10 | 10 (7 to 14) |
| equal | WAITS | 3 | 3 | 3 (2 to 6) |
| equal | MIXED | 14 | 13 | 13 (10 to 16) |
| equal | FED BY ITS SURROUNDINGS | 1 | 2 | 1 (0 to 3) |

The shared prediction (Amendment 5) is scored per cell at L = 16 exactly as at stage 1 and reported. At stage 1 the
equal-background prediction held in 3 scored cells at each size; the draws put it at 3 (2 to 6) for L = 16, reported.

**The verdicts at L = 16** (ours, proposed with the words above, for her word):

- **The size verdict** (the registered claim, Standing requirement 1, scored alone): **HOLDS AT L = 16** if all 18
  periods lie in their ranges; **MISSES AT L = 16** otherwise, naming every period outside its range. A miss is
  followed by rule 11's four answers before any new run.
- **Three secondary reads,** reported beside the size verdict and not part of it: fed, timing and unfed, each
  **REPEATS STAGE 1** if every cell or setting meets its rule above (fed: the 48 cells BURPS and none of the six NEVER
  BURPS; timing: all 12 words as written; unfed: the 33 cells repeat and the count of the other 21 lies in 14 to 21),
  and **CHANGES** otherwise, naming each cell. If the stage-1 rates hold, the fed and timing reads repeat in every
  draw and the unfed read in 0.997 of them.
- What is scored for items 2 to 4 is the stage-1 rate, including the failures of O145, not the shared prediction,
  which is scored per cell and reported separately.
- **NOT READ** for any number whose cell is missing, failed, or has fewer than 16 replicas, with the reason. The ranges
  assume 16 replicas a cell.

The per-cell words, the shared prediction, the tallies and the reads that make no size claim are reported beside the
verdicts. They do not enter them.

**What L = 16 would run** (nothing is written or launched by this amendment):

- **54 configs**, `configs/t74_lam{110,125,140}_L16_{steady,meals16,meals256}_{c2R,cRhalf}_{cold,equal,warm}.json`.
  They come from a `--held-out` option to be added to `scripts/make_t74_configs.py`, with a test. Every key is as in
  stage 1 except L = 16, the seed, and a `_purpose` naming this amendment. That `_purpose` carries VISION Update 24's
  caveat and Update 95's statement: the model's author advised against the six-link version, and the field's prior is a
  two-dimensional base with the third dimension emergent.
- **Each cell** (`scripts/run_layer_outside.py`'s own evaluation, done in memory): N_slab = 1,024, R = 64, c = 128 or
  32, gate a N_slab = 409.6, 1,024 or 1,638.4, n_out = 1,024. The meals are 64 every sweep, 1,024 every 16 sweeps or
  16,384 every 256 sweeps. The warm background is 4a = 1.6, 4 or 6.4. Each cell runs 16 replicas: fed 4,096 sweeps,
  then digestion of up to 4,096, then unfed 4,096.
- **Seeds (ours, for her word): 20267901 to 20267954, one per cell,** in the order λ, feed, c, background. Replica
  seeds are SeedSequence([seed, replica]) as in stage 1. Two other choices would collide:
  - the generator as written restarts at 20267401 and would reuse stage-1 seeds;
  - continuing after stage 1 (20267509 onward, as T56's generator does) would reuse ten of T75's seeds
    (20267509 to 20267518).

  The block 20267901 to 20267954 is used by no config in `configs/` as of 23 October.
- **A prediction file and a scorer, committed with this amendment** (as T60's was): `configs/t74_heldout_prediction.json`,
  holding the numbers and the cell lists above, and a tested scorer. `--held-out` refuses to write configs until the
  prediction file exists.
- **The manifest:** 54 jobs, one wave under the 96-at-once Batch limit.
- **Compute, and the Batch ceiling:** each Batch job is stopped after 86,400 s (24 h), with one attempt
  (`terraform/_variables.tf`, `job_timeout_seconds = 86400`; `terraform/batch.tf`, `attempts = 1`). One job runs a
  cell's 16 replicas in turn, so a stopped job loses all 16. No per-job time is recorded: the `.meta.json` files carry
  none, and the queue status file predates the launch. The only bound: the launch commit (f680737a) is at 12:34 UTC on
  20 October and the fetch of all 108 at 11:11 UTC on 21 October (`cloud/inbox/FETCHED.md`), so every stage-1 job
  finished within about 22.6 h, queueing included. L = 16 has 1,024 points against 576 at L = 12, 1.78 times as many.
  How a sweep's cost grows with the points has not been measured; if it grows in proportion, an L = 12 job longer than
  about 13.5 h (86,400 s / 1.78) means an L = 16 job past the ceiling. **Before launch:** read the L = 12 job
  durations from the `queue_status` workflow (it lists each job's created, started and stopped times) while Batch
  still holds the records, or time one L = 16 replica in memory. If an L = 12 job took more than about 13.5 h, split
  each cell's replicas across jobs (a runner option, with a test) or raise the ceiling; raising it is an
  infrastructure decision for her. The stage-1 files were 3.4 to 19 MB each (`cloud/inbox/FETCHED.md`).

**Disclosed.**

- Stage 1 already shares eight seeds with T75: 20267501 to 20267508 are T74's last eight L = 12 cells at λ = 1.40
  and T75's first eight cells. The two use different kernels and different experiments and are never compared, so
  nothing scored changes. The overlap is recorded here so that it is not repeated.
- O145's answer (3) puts an exact look before any run: the distribution of the pool's stored energy at the common
  mean, against 2a, from the saved rows. The saved rows cannot give it: they log the slab's total stores (`stores`),
  the common mean (`g_common`) and the slab's mean before the flow (`g_in_before`), with no column for the two layers
  beside the cut. Making the look needs a run that logs the pool. Whether L = 16, the registered held-out run and not
  a new mechanism, goes ahead before that look is for her word.
- The rule for the ranges (the two-level draw), the 99.7 %, the cell-by-cell rules, the seed block, and the words
  HOLDS / MISSES and REPEATS STAGE 1 / CHANGES are ours. They were written after stage 1 was read and before anything
  at L = 16 exists.

**Our expectation (ours):** HOLDS AT L = 16, and REPEATS STAGE 1 for the three secondary reads. With the feed, the cap
and the gate all proportional to N_slab, and one layer proposal a sweep whatever L is, the period is arithmetic by
construction. The numbers most at risk are the ones set by rare clean switch moves at λ = 1.10, c = 2R, whose rate (4
of 144 replicas at both L = 8 and 12) is too poorly known to say whether it grows with the points.

Her prediction is ours (Amendment 5); L = 16 cannot separate them. What it tests is whether the kernel reproduces the
stage-1 rates at a larger slab. The registered prediction she agreed to ("I agree with your t74 predictions",
Amendment 5) already says "at every λ and size" (Amendment 2, item 5), and it is scored per cell at L = 16 as at
stage 1.

Her word: ______

Her prediction for L = 16, if she gives one: ______ (if none, the registered prediction is scored per cell as above;
the numbers above are the stage-1 fit, neither her prediction nor ours).

**Nothing runs until her word is recorded here.** No config, manifest or prediction file is written before it.

*Sources (each command run 23 October 2026 in the worktree; the scratch scripts and their outputs are in `sandbox/out/`,
untracked):*

- `python scripts/analyse_t74.py $(python -c "import sys; sys.path.insert(0, 'scripts'); import make_t74_configs as m;
  print(' '.join('results/%s.csv' % c['name'] for c in m.cells()))")` gives the stage-1 words and periods, the 108 files
  by name (`t74_analyse_stage1_2026-10-23.txt`).
- `python sandbox/heldout_2026-10-23/t74_heldout_numbers_2026-10-23.py` gives the per-size periods, the per-cell counts and the timing
  ratios (`t74_heldout_numbers_2026-10-23.txt`).
- `python sandbox/heldout_2026-10-23/t74_heldout_resample_2026-10-23.py` writes the per-replica cache,
  `t74_stage1_replicas_2026-10-23.json`, that the next two scripts read; `--cached` reuses it.
- `python sandbox/heldout_2026-10-23/t74_heldout_twolevel_2026-10-23.py` gives the period ranges, the timing ratios and words, the
  fed shares and allowance, the reported tallies, each range's miss rate under the claim (a separate draw of 40,000,
  numpy seed 4243), the back-test of the periods, and the clean switch count (it reads the 18 stage-1 files at
  λ = 1.10, c = 2R by name) (`t74_heldout_twolevel_2026-10-23.txt`).
- `python sandbox/heldout_2026-10-23/t74_heldout_cells_2026-10-23.py` gives the cell-by-cell unfed rule, the count of the other 21
  cells, the chance that the read repeats, and the back-test of the cell-by-cell rules and the timing words
  (`t74_heldout_cells_2026-10-23.txt`).
- `python sandbox/heldout_2026-10-23/t74_l16_cells_2026-10-23.py` gives the L = 16 cell numbers, in memory
  (`t74_l16_cells_2026-10-23.txt`).
- `python sandbox/heldout_2026-10-23/t74_seed_map_2026-10-23.py` gives the seed blocks in `configs/`.
- The Batch ceiling: `terraform/_variables.tf` and `terraform/batch.tf`. The launch and fetch times: `git log -1
  f680737a` and the header of `cloud/inbox/FETCHED.md`. The saved columns: the header row of the stage-1 files.

All the scripts read the stage-1 files `results/t74_lam{110,125,140}_L{08,12}_*.csv` by name, or the cache made from
them, and nothing else in `results/`.
