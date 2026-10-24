*Draft for PREREGISTRATION.md, section T71, to sit under "Reading of T71". Written 23 October 2026 in `sandbox/out/`,
revised the same day after an independent check, and not committed. Nothing at L = 16 has been run, built or looked at.*

### Amendment 4 (23 October 2026, before L = 16 runs): the held-out numbers

The owner's decision of 23 October (VISION Update 95: the six-link track is kept as a model of three-dimensional space)
released this work. Every number below is written from L = 8 and 12 alone, as rule 14 requires. The source is the twelve
stage-1 files `results/t71_{model,layer,layerref,control}_lam{110,125,140}.csv`, fetched 19 October and read and scored
21 October (O144). Every six-link result carries VISION Update 24's caveat. It also carries Update 95's: the model's
author advised against the six-link version, and the field's prior is a two-dimensional base with the third dimension
emergent. At λ ≠ 1, and with a count of points that varies, this is our family around the published model, never
combinatorial quantum gravity.

**Commands.** The registered reader, at the stage-1 sizes:
`python3 scripts/analyse_t71.py results/t71_model_lam*.csv results/t71_layer_lam*.csv results/t71_layerref_lam*.csv`.
The predicted numbers and their ranges come from
`PYTHONPATH="src;scripts" python3 sandbox/heldout_2026-10-23/t71_heldout_numbers_v2.py`, whose output is saved beside it as
`t71_heldout_numbers_v2_2026-10-23.txt`. It replaces the first version, `t71_heldout_numbers.py`, which is kept with its
output; a check found that version's bands too narrow (section 3). Which stage-1 statistics fall outside the cross-check
in section 3 comes from `PYTHONPATH="src;scripts" python3 sandbox/heldout_2026-10-23/t71_heldout_crosscheck_misses.py` (output
`t71_heldout_crosscheck_misses_2026-10-23.txt`). The per-replica details (gate offsets, stores per point, clean moves,
end states, and the control read by `analyse_t68`'s rules) come from
`PYTHONPATH="src;scripts" python3 sandbox/heldout_2026-10-23/t71_heldout_look.py`. The cost comes from
`python3 sandbox/heldout_2026-10-23/t71_heldout_size.py`. `sandbox/out/` is not tracked, so before this amendment is committed the
numbers script moves to `scripts/` with a test, and the table is written to `configs/t71_heldout_prediction.csv`, as
T68 did.

#### 1. What in T71 is a claim about size

- **The size claim** (Definitions, "The size claim (rule 14)"): every per-cell word and median at L = 16 is written
  from L = 8 and 12; AS PREDICTED if they hold. The per-cell readings are:
  - the majority word;
  - the median first split, with its range across replicas;
  - the release against a N_slab;
  - the median energy above flat at the end;
  - the SPENT FIRST count.

  Under the daughter rule, four more readings sit beside the word: the median number of daughters, the energy per
  daughter, the period and the slab share.
- **Ours, f1 reference:** "t_gate = a N_slab / (2L² r) = 2a / r sweeps exactly ..., the same at every size."
- **Ours, daughter rule:** "since every threshold and the feed are per point, the daughters are born at the same
  sweeps at every L for the same seed (the held-out size then tests only this)."
  - As registered, a replica's seed includes N_slab (`scripts/run_layer_feed.py`, `seed_for`). So no L = 16 replica
    shares a seed with a stage-1 replica.
  - At L = 16 this claim can therefore be tested only in its weaker form: the same distribution at every size.
- **Exact, items 1 and 4 and the ledger:**
  - The split releases a N_slab, which at L = 16 is 409.6, 1,024 and 1,638.4 at λ = 1.10, 1.25 and 1.40.
  - Under layer moves alone, every daughter carries a N_slab to 1e-9.
  - The gate is 2a per pool point at every L.
  - The first clean switch step costs 64 (item 4, at λ = 1.10 and 1.25) and needs 8 per point in its pool of eight
    ends, at every L.
- **The one place where the count of points can matter:** the clean switch move. The model arm makes N attempts a
  sweep. At stage 1 the move fired only at λ = 1.10, r = 1/16, at both sizes (O144).

#### 2. Why most of it should not change with L (ours, from reading the code; not pinned by a test)

When no clean move fires, the layer moves do not depend on L, for five reasons:

- The proposal draws an axis, a position across the current width, and split or contract. None of these involves L.
- The feed is per point.
- A payment is drawn in proportion over whole layers.
- New layers start empty.
- A release and the gate both scale with L².

So given the same random draws, the history of widths and of stores per point is the same at every L, up to floating
rounding at exact ties. That covers arm B, the f1 reference, and the model arm in every cell but λ = 1.10, r = 1/16.
The stage-1 differences between L = 8 and 12 in those cells are therefore differences between seeds.

Two pieces of measured support:

- The kernel's exploratory check of 18 October found the births at the same sweeps at L = 6 and 8 for the same seed.
- At stage 1, the rows a replica logs do not grow with L: 415,694 rows in the nine layer-feed files, 207,204 of them
  at L = 12.

*Owed, not a condition:* a test in `tests/test_layer_feed.py` that runs layer moves alone at L = 6 and 8 with one seed
and asserts identical width histories and stores per point. That would make this paragraph exact for the kernel, and
it runs no held-out size.

#### 3. How each number and its range are set (declared before L = 16 exists; ours)

**What is scored.** Only the registered per-cell readings of section 1. Clean-move totals, the number of replicas with a
clean move, the f1 open share and refolds, and the control's median stop and energy fed are not among them; they are
written below and marked "reported, not scored". A range that covers every value its quantity can take cannot fail; it
is marked "reported, cannot fail" and left out of the scored count. Nine end-energy ranges are of that kind (Tables 1 to
3). The end energy of the model arm at λ = 1.10, r = 1/16 is reported by class and not scored (Table 2b says why).

**The level.** The scored numbers that a sample can miss are 42 under rule A, 3 under rule D, and 36 under rule B (a
median and a latest replica in each of 18 cells): 81 in all. Each gets a two-sided level of α = 0.10 / 81 = 0.00123, so
that the chance of any miss by sampling alone, if every rule's premise holds, is at most 0.10 (a Bonferroni bound).

- **Rule A, the cells with no clean move.** L = 16 is taken as a fresh sample from the same distribution as L = 8 and
  12.
  - The number is the median of the 32 pooled stage-1 replicas.
  - The range is predictive: the number, plus the α/2 and 1 − α/2 quantiles of (the median of 16 replicas drawn with
    replacement from the 32) minus (the median of 32 drawn the same way), 200,000 resamples, seed 20261023. So it
    carries the spread of the new median and the spread of the pooled one.
  - The range is stretched where needed to hold both stage-1 medians, and clipped to what the quantity can take.
- **Rule B, the first split.** The first split is t_gate plus a wait.
  - t_gate is the first sweep at which a pool of two layers holds a N_slab: 52, 13, 128, 32, 205 and 52 sweeps for
    (λ, r) = (1.10, 1/64), (1.10, 1/16), (1.25, 1/64), (1.25, 1/16), (1.40, 1/64), (1.40, 1/16). It is the same at
    L = 8, 12 and 16.
  - The wait is one coin flip a sweep, because a contraction is refused at width 4.
  - The 576 stage-1 replicas match this law: waits of 0, 1, 2 and 3 sweeps were seen 279, 155, 68 and 38 times,
    against 288, 144, 72 and 36 expected.
  - From that law (10⁶ simulated sets of 16 replicas): the median is t_gate + 0.5, with range t_gate to t_gate + 2
    (a miss has probability 0.00025 per cell).
  - Across replicas, the earliest split is at t_gate (a miss has probability 1.5 × 10⁻⁵ per cell) and the latest at
    most t_gate + 13 (a miss has probability 0.00098 per cell).
- **Rule C, exact.**
  - The release at the first split is a N_slab in every cell. No clean move can be paid before it: until then every
    store holds exactly r t, so a pool of eight ends holds 8 r t. That reaches the first clean step's 64 only at
    t = 8 / r, which is 76 to 460 sweeps after t_gate (the script prints the margin per cell). The price of 64 is
    item 4's, at λ = 1.10 and 1.25. At 1.40 it is our reading, not checked, and stage 1 saw no clean move there.
  - By the same arithmetic, SPENT FIRST is 0 of 16 in every model cell.
  - Every daughter carries a N_slab wherever no clean move fires.
- **Rule D, the cell where clean moves fire** (the model arm at λ = 1.10, r = 1/16). No form is registered, and two
  sizes cannot fix one. Ours:
  - The number is the line in L through the two stage-1 medians.
  - The range runs from L = 12's median (the trend stops) to the farthest of two forms in which the trend goes on: the
    line in N_slab at 1,024 points, and a power law in N_slab for the shortfall from the value with no clean move. That
    value is a N_slab for the energy per daughter, and arm B's pooled median for the other two (339.5 daughters, slab
    share 0.3716).
  - The two stage-1 points fit both forms equally well. The power law goes furthest for the energy per daughter: its
    shortfall from a N_slab grew 8.1 times (0.0130 to 0.1052) while N_slab grew 2.25 times, an exponent of 2.58,
    which gives 0.535 of a N_slab (219.2) at L = 16. For the daughters (281.4) and the slab share (0.208) the power
    law falls inside the other two forms' span.
  - The range is widened on each side by the predictive half-widths at the same level, from the L = 12 replicas alone
    (a new median of 16 against L = 12's), and clipped to what the quantity can take.
  - The range still assumes the shortfall grows no faster than that power law. A value below it would read: the
    clean-move effect accelerates with size faster than the two points suggest.
  - The period, which did not change, takes rule A.

**What chance alone can do.** The first version of these bands was too narrow. Between L = 8 and 12, which share one
distribution in these cells, 6 of 136 stage-1 statistics fell outside a nominal 99 % band built from the other size
alone (4.4 %; the same 6 at bootstrap seeds 1, 2, 3 and 20261023), because that band left out the spread of the
reference median. At the level above, the chance of any miss by sampling alone is at most 0.078: 0.056 from the 45
numbers under rules A and D, and 0.022 from rule B. So if every rule's premise holds, AS PREDICTED has a probability of
at least 0.92, and a miss is evidence, not expected noise. The same predictive construction, run between L = 8 and 12
(16 replicas against 16), puts 2 of 136 statistics outside at this level, and the same 2 at a per-number level of 1 %.
Neither is a number scored here:

- the f1 end energy at λ = 1.10, r = 1/64, where 9 of 16 replicas ended as the slab at L = 8 and 2 of 16 at L = 12 (its
  pooled range at L = 16 runs from 0 to a N_slab and cannot fail);
- an f1 open share at λ = 1.10, r = 1/16 (not scored).

Two limits, said now. The resampling can only spread what the replicas show, so a sample with few of one class, as at
L = 12 in the first case, still gives too narrow a band; that is why every L = 16 range is built from the 32 pooled
replicas. And the count leaves out clean moves in the five model cells of Table 2a. A few of them at L = 16 would be
consistent with stage 1 (Table 2a). They would leave the median energy per daughter and the median end energy where
they are unless they reached about half the replicas, but they could move a slab share or a daughter count. A miss in
such a cell, in a run where clean moves fired there, is read as clean moves reaching the cell at the larger size, not
as chance.

#### 4. The words at L = 16 (the registered words, unchanged)

Sections 4 and 5 are our predictions (the assistant's), written by the rules above. The owner's is asked for in
section 9.

- **CYCLES**, 16 of 16, in all twelve daughter-rule cells (the model arm and layer moves alone).
- **OSCILLATES**, 16 of 16, in all six f1 cells.
- **SPENT FIRST**, 0 of 16, in all six model cells.
- **SITS**, 16 of 16, in all six control cells.
- No ONE BURP, NEVER SPLITS, OPENS AND STAYS, OPENS, FRONT or BREAKS anywhere.

#### 5. The numbers

Each entry reads "L = 8, L = 12 → **L = 16** (range)". The energy per daughter and the release are a N_slab exactly
(rule C) in every cell of Tables 1 to 3, except the model cell at λ = 1.10, r = 1/16 (Table 2b).

**Table 1. Layer moves alone, daughter rule (arm B); rules A and B.**

| λ, r | first split (median's range; replicas' range) | daughters | period (sweeps) | slab share | end energy above flat |
|---|---|---|---|---|---|
| 1.10, 1/64 | 52, 53 → **52.5** (52 to 54; 52 to ≤ 65) | 83, 83 → **83** (82 to 84) | 23.5, 23.5 → **23.5** (22.25 to 25) | 0.8617, 0.8596 → **0.8611** (0.8439 to 0.8818) | **409.6** (409.6 to 409.6) |
| 1.10, 1/16 | 13, 13.5 → **13.5** (13 to 15; 13 to ≤ 26) | 340.5, 339 → **339.5** (322.5 to 354.5) | 4.75, 5 → **5** (4 to 6) | 0.3716, 0.3716 → **0.3716** (0.3509 to 0.3977) | **0** (0 to 409.6; reported, cannot fail) |
| 1.25, 1/64 | 129.5, 128.5 → **128.5** (128 to 130; 128 to ≤ 141) | 40, 40 → **40** (40 to 41) | 62, 61 → **62** (58.75 to 65.25) | 0.9393, 0.9400 → **0.9400** (0.9293 to 0.9531) | **1,024** (1,024 to 1,024) |
| 1.25, 1/16 | 32.5, 33 → **32.5** (32 to 34; 32 to ≤ 45) | 141, 140.5 → **141** (139 to 143) | 13, 13 → **13** (12 to 14) | 0.7709, 0.7738 → **0.7717** (0.7457 to 0.7907) | **1,024** (0 to 1,024; reported, cannot fail) |
| 1.40, 1/64 | 206, 205 → **205.5** (205 to 207; 205 to ≤ 218) | 40, 40 → **40** (39 to 40) | 101, 101.5 → **101** (97.5 to 104) | 0.9586, 0.9639 → **0.9622** (0.9519 to 0.9708) | **1,638.4** (1,638.4 to 1,638.4) |
| 1.40, 1/16 | 53, 54 → **52.5** (52 to 54; 52 to ≤ 65) | 83, 83 → **83** (82 to 84) | 23, 23 → **23** (22 to 24) | 0.8673, 0.8592 → **0.8640** (0.8427 to 0.8824) | **1,638.4** (1,638.4 to 1,638.4) |

**Table 2a. The model arm (arm A), the five cells with no clean move at stage 1; rules A to C.** The clean moves are
reported, not scored: they are not a registered per-cell reading. Stage 1 saw none in any of the 32 replicas of each
cell. In these cells the largest store per point (averaged over the points) in any replica was 1.07 to 6.62, below the
8 a pool of eight ends needs on average. That is about the average only: stores are not uniform across layers (new
layers start empty, and payments are drawn in proportion), so a pool of eight ends could hold 64 while the average is
below 8. Zero in 32 replicas (13,312 point-replicas) allows up to 3.7 clean moves a cell at L = 16, at 95 % (the rule of
three), if the rate per point does not depend on L, because at width 4 L = 16 makes 1,024 attempts a sweep where L = 8
and 12 made 256 and 576. So a few clean moves here at L = 16 would be consistent with that rate; only a count well
above it would point to an effect of size beyond the larger number of attempts.

| λ, r | first split (median's range; replicas' range) | daughters | period (sweeps) | slab share | end energy above flat |
|---|---|---|---|---|---|
| 1.10, 1/64 | 52, 52.5 → **52.5** (52 to 54; 52 to ≤ 65) | 83, 83 → **83** (82 to 84) | 23, 24 → **23.75** (22.25 to 24.75) | 0.8627, 0.8688 → **0.8678** (0.8471 to 0.8850) | **409.6** (204.8 to 409.6) |
| 1.25, 1/64 | 129, 128 → **128.5** (128 to 130; 128 to ≤ 141) | 40, 40 → **40** (40 to 41) | 61, 62 → **61.5** (58 to 65) | 0.9321, 0.9367 → **0.9348** (0.9256 to 0.9430) | **1,024** (1,024 to 1,024) |
| 1.25, 1/16 | 33, 32.5 → **32.5** (32 to 34; 32 to ≤ 45) | 140, 140 → **140** (137 to 143.5) | 13.5, 13.75 → **13.75** (12.75 to 14.75) | 0.7784, 0.7750 → **0.7769** (0.7451 to 0.8104) | **1,024** (0 to 1,024; reported, cannot fail) |
| 1.40, 1/64 | 206, 205 → **205.5** (205 to 207; 205 to ≤ 218) | 40, 40 → **40** (39 to 41) | 101, 101.25 → **101** (98 to 104) | 0.9597, 0.9581 → **0.9586** (0.9519 to 0.9671) | **1,638.4** (1,638.4 to 1,638.4) |
| 1.40, 1/16 | 52, 53 → **52.5** (52 to 54; 52 to ≤ 65) | 83, 83 → **83** (81.5 to 84.5) | 23, 23 → **23** (22 to 24) | 0.8558, 0.8549 → **0.8558** (0.8370 to 0.8754) | **1,638.4** (1,638.4 to 1,638.4) |

**Table 2b. The model arm at λ = 1.10, r = 1/16, where clean moves fire; rule D, except where noted.** Measured at
stage 1: clean moves in 12 and 13 replicas of 16 (17 and 23 moves in all), first between sweeps 335 and 1,703, never
before the first split.

- **Word:** CYCLES, 16 of 16. **SPENT FIRST:** 0 of 16 (rule C).
- **First split** (rule B): 13, 13 → **13.5** (13 to 15; replicas 13 to ≤ 26). **Release:** 409.6 exactly (rule C).
- **Energy per daughter:** 101.1, 206.2 (0.987 and 0.895 of a N_slab) → **328.7, that is 0.80 of a N_slab** (117.4
  to 409.6, that is 0.29 to 1).
- **Daughters:** 329.5, 311.5 → **293.5** (206.4 to 386.5).
- **Slab share:** 0.3597, 0.3166 → **0.2736** (0.0516 to 0.4723).
- **Period** (rule A): 5, 5 → **5** (4 to 6).
- **End energy above flat: reported by class, not scored.**
  - It is a snapshot that takes a few classes: the slab (a N_slab: 102.4 at L = 8, 230.4 at L = 12, 409.6 at L = 16),
    open and flat (0), or open with rewired patches, whose energies are local and do not grow with L.
  - At L = 8: 7 slabs, 6 open at 0, and 3 with patches (128, 192, 240); median 102.4, the slab.
  - At L = 12: 1 slab, 4 open at 0, and 11 with patches (128 six times, 192 three times, 240, 528); median 128.
  - Expected at L = 16: the median replica ends open, at 0 or with patches of 128 or more, not as the slab (409.6).
  - Not scored, because its classes change with L and two sizes give no declared range that keeps them apart. This is
    the one registered median left unscored, and it is said before L = 16 runs.
- **Clean moves in all** (reported, not scored): 17, 23 → 29 (4 to 50.4).
- **Replicas with a clean move** (reported, not scored): 12, 13 → a majority expected. At the pooled share of 0.78,
  8 or fewer of 16 has probability 0.012.

What the scored ranges can fail on:

- An energy per daughter below 117.4 (0.29 of a N_slab). At this level it can no longer fail at a N_slab: a new
  median of 16 against L = 12's can reach a N_slab by sampling alone.
- Daughters below 206.4 or above 386.5.
- A slab share below 0.0516 or above 0.4723.
- A period outside 4 to 6.

The ranges are wide because two sizes cannot fix a form and the 16 replicas of this cell spread widely. So at L = 16
this cell can show only a large change. That weakness is the honest state of the size claim in this one cell.

**Table 3. Layer moves alone, release kept in the stores (the f1 reference); rules A to C.**

- **Word:** OSCILLATES, 16 of 16.
- **Release:** a N_slab exactly.
- **End energy above flat:** **0**, with range 0 to a N_slab, in all six cells: reported, cannot fail. It is a
  snapshot of cells that spend 0.62 to 0.65 of their time open (the open shares below).
- The open share and the refolds are not per-cell readings in the registration. They are reported, not scored.

| λ, r | first split (median's range; replicas' range) | end energy (stage 1) | open share (not scored) | refolds (not scored) |
|---|---|---|---|---|
| 1.10, 1/64 | 53, 52.5 → **52.5** (52 to 54; 52 to ≤ 65) | 102.4, 0 | 0.6183, 0.6187 → 0.6183 (0.5978 to 0.6412) | 566, 563.5 → 565.5 (549.5 to 584) |
| 1.10, 1/16 | 13, 13 → **13.5** (13 to 15; 13 to ≤ 26) | 0, 0 | 0.6486, 0.6305 → 0.6436 (0.6210 to 0.6629) | 611, 603.5 → 609 (593 to 622.5) |
| 1.25, 1/64 | 129, 128 → **128.5** (128 to 130; 128 to ≤ 141) | 0, 0 | 0.6286, 0.6249 → 0.6272 (0.6120 to 0.6433) | 697.5, 698.5 → 698.5 (681 to 717) |
| 1.25, 1/16 | 33, 32 → **32.5** (32 to 34; 32 to ≤ 45) | 0, 0 | 0.6253, 0.6243 → 0.6243 (0.6034 to 0.6457) | 580, 588.5 → 585 (569 to 603) |
| 1.40, 1/64 | 206, 205.5 → **205.5** (205 to 207; 205 to ≤ 218) | 0, 0 | 0.6188, 0.6160 → 0.6186 (0.6027 to 0.6348) | 1,115.5, 1,119.5 → 1,117 (1,095.5 to 1,137) |
| 1.40, 1/16 | 53, 52 → **52.5** (52 to 54; 52 to ≤ 65) | 0, 0 | 0.6261, 0.6231 → 0.6246 (0.6037 to 0.6501) | 575, 570 → 572.5 (556.5 to 588.5) |

**Table 4. The control (arm C), as configured; T68's runner, read by T67's words through `analyse_t68`.**

- **Word:** SITS, 16 of 16, in every cell. No point opens and no point breaks.
- **Median stop** (the last record; reported, not scored): 2,000, 2,550 and 4,050 sweeps at λ = 1.10, 1.25 and 1.40.
- **Median energy fed** (reported, not scored): 31.25 and 125.00 at λ = 1.10; 39.84 and 159.38 at 1.25; 63.28 and
  253.12 at 1.40 (r = 1/64 and 1/16). That is the rate times the last record's sweep, as at stage 1, where every cell
  matched it.
- **Per point at N = 1,024:** 0.0305 to 0.2472.
  - At stage 1 the most any cell received was 0.9888 per point (λ = 1.40, r = 1/16, N = 256), and no point opened or
    broke anywhere.
  - So SITS at L = 16 is arithmetic on a measured fact.
- T67's per-size word reads MIXED at every (λ, N), as it did at stage 1, because nothing opens and not every cell
  breaks. It is reported, not part of T71's claim.

#### 6. The verdict at L = 16 (scored there alone)

- **AS PREDICTED** if every word in section 4 and every scored number in Tables 1 to 4 holds.
- Otherwise **not AS PREDICTED**. Each miss is named with its rule.
  - A miss in a number under rule A, B or D is evidence: if every rule's premise holds, the chance of any such miss is
    at most 0.078 (section 3).
  - A miss in rule C, a word, SPENT FIRST or the control's word is a failure of something exact or structural.
  - A miss in a model cell of Table 2a, in a run where clean moves fired in that cell, is read as clean moves reaching
    the cell at the larger size (section 3).

As Amendment 3 recorded, her words and ours now coincide in every arm, so L = 16 cannot tell her picture from ours: it
tests a shared expectation and the size claim. In 17 of the 18 arm cells nothing in the code depends on L (section 2),
and the route to the opened state is put in by hand (the layer split), so there L = 16 checks the kernel's arithmetic
at a third size. The one cell where size can matter is the model arm at λ = 1.10, r = 1/16, and there only a large
change would miss (Table 2b). The owner can weigh the twelve jobs against that.

The three predictions, set against these numbers:

- **The owner's, at stage 1** (Amendments 2 and 3). Every word of hers is in section 4. Her prediction of one a N_slab
  per daughter is predicted to fail again in one cell, the model arm at λ = 1.10, r = 1/16, where Table 2b puts the
  energy per daughter at 0.80 of a N_slab (0.29 to 1).
- **Ours, "the slab share above one half under g1".** Predicted to fail again at λ = 1.10, r = 1/16 (0.3716 in arm B,
  0.2736 in arm A).
- **Ours, "no clean switch move in any cell".** Predicted to fail again in that one cell.

#### 7. Found while writing this amendment (exact, from the stage-1 rows; nothing changed)

The control was fed far less per point than the arms it controls.

- **The mismatch.**
  - T68's runner treats the rate as the total per sweep, shared by every point. In its files, fed = r × sweep:
    31.25 at sweep 2,000 for r = 1/64. At L = 8 that is 0.12 per point.
  - The layer-feed runner gives r to every point every sweep, which is 31.25 to 125 per point over the run.
  - So per point the control received 1/N_slab of the other arms' feed: 1/256 at L = 8, 1/576 at L = 12, and 1/1,024
    at L = 16 if it runs as configured.
  - The design table says "r per point per sweep into every point's store" for the feed. The control's line names T68's
    runner, whose rate is a total.
- **What it changes.**
  - No stage-1 word changes as read.
  - Arm C's SITS, her prediction that the control does not cycle (holds) and our "BREAKS" (fails) all rest on a feed
    256 to 576 times weaker per point than the model's. So what the control showed is narrower than O144 first said.
  - This is now on the record: an addendum to ASSUMPTIONS O144, committed 23 October.
- **The owner's choice, not decided:**
  - (a) run the control at L = 16 as configured, for continuity with stage 1, where it SITS by arithmetic;
  - (b) leave the control out of the held-out stage, since at this feed its claim is settled by arithmetic at any size;
  - (c) register a matched control (the same per-point feed as the arms) as a new cell with its own prediction. It has
    no stage-1 sizes to fit from, so it cannot be a held-out test, and it asks a new question: do single switches
    break the slab under the arms' feed?

  Ours: (a) or (b). The choice is hers and stays open until she makes it.

#### 8. What the L = 16 runs would be (not written; nothing is queued)

- **Configs:** twelve, `configs/t71_{model,layer,layerref,control}_lam{110,125,140}_l16.json`. Each is identical to its
  stage-1 config except for five keys:
  - `"name"`, with `_l16` appended;
  - `"sizes": [16]`;
  - `"seed"`, the stage-1 seed + 12, so 20267113 to 20267124 in the stage-1 manifest's order (model, layer,
    layerref, control at λ = 1.10, then 1.25, then 1.40). None of these seeds is used in any config.
  - `"_purpose"` and `"written"`, naming this amendment and the date of her word.

  Each config has 16 replicas, r = 1/64 and 1/16, and its stage-1 length rule: max(2,000, 40 a / r) sweeps for the
  layer-feed runner; 2,000, 2,560 and 4,096 sweeps, recorded every 50 with the final graphs saved, for the control.
  The control's configs follow (a), (b) or (c) of section 7.
- **Seeds:** the runners' own rules. The layer-feed runner uses SeedSequence([seed, N_slab, λ index, rate index,
  replica]); T68's runner its mode-"all" rule. Both include the count of points, so the streams are new even apart
  from the new bases.
- **Queue:** one manifest, `cloud/queue/<date of her word>_t71_heldout.txt`, with twelve lines in stage 1's order:
  `run_layer_feed` nine times and `run_slab_feed` three times. That is within one batch of the 96-job capacity.
- **Compute:**
  - 978,688 replica-sweeps in all.
  - At width 4 that is 1.0 × 10⁹ point-sweeps, against 8.1 × 10⁸ for stage 1. Each L = 16 job is 1.23 times its
    stage-1 job, if the cost of a sweep grows with the number of points, as the kernels' loops suggest (ours, not
    measured).
  - Stage 1's wall times are not recorded in the repository.
  - Output: about 207,000 rows and 36 MB for the nine layer-feed files, if the rows a replica logs do not depend on L
    (they did not at stage 1). The control writes about 1.9 MB of saved graphs per job.
- **To read:**
  1. Put `t71_*_l16` into `cloud/fetch/request.txt`, then accept and commit unread.
  2. Run the registered reader on the nine named layer-feed files only:
     `python3 scripts/analyse_t71.py results/t71_{model,layer,layerref}_lam{110,125,140}_l16.csv`. Not a glob such as
     `results/t71_*_l16.csv`: that would also take the control's files, which T68's runner writes without the columns
     `L` and `gate`, and the reader stops on them (checked: on `results/t71_control_lam110.csv` it raises
     `KeyError: 'L'`).
  3. If the control runs, read it by `analyse_t68`'s rules on the three files
     `results/t71_control_lam{110,125,140}_l16.csv` only. Its loader takes every file that starts with the prefix it is
     given, and `t71_control_` would also take the stage-1 files, which differ only in N; so pass each file's full name
     as the prefix, or keep only the rows at N = 1,024.
  4. Score against `configs/t71_heldout_prediction.csv` and this amendment.

#### 9. The owner's word

She is asked for three things: her prediction for L = 16, or her word that her stage-1 prediction stands for it; her
choice on the control, (a), (b) or (c) of section 7; and the go-ahead for the twelve jobs.

Her word: ______

Nothing runs until her word is recorded here.
