# Paper 1: changes proposed for a possible v2 (not applied)

Paper 1 (`paper.tex` here) has been submitted to arXiv and is **not edited**. This file lists the changes a
referee reading of 25 September 2026 proposed, **only those checked against the record and the committed data and
found to hold**, with the exact line, the current text, a proposed replacement, and the record entry that supports
it. Most serious first. Whether to replace the arXiv version is the owner's decision.

The referee report was written by an AI agent; each point below was checked against `ASSUMPTIONS.md`,
`PREREGISTRATION.md` and, where a number was at stake, rerun from `results/` (T8, T23, T24 analyzers; the T8 and T24
CSVs directly). Line numbers are those of `paper.tex` as submitted.

---

## 1. "Every verdict quoted was pre-registered": two headline results were exploratory, and the two-state verdict came after four gate amendments

These three items go together; `ASSUMPTIONS.md` O64 names them as the most serious for this paper.

### 1a. Abstract, line 37

- **Current:** `... The release vanishes at $\lambda = 1$, the CQG value. Every verdict quoted was pre-registered.`
- **Proposed:** `... The release vanishes at $\lambda = 1$, the CQG value. The Arrhenius test and the seed threshold
  were exploratory; every verdict quoted was pre-registered, and the two-state verdict at $\lambda = 1.25$ was reached
  after amendments to its energy gate, three of them written after the data they judged.`
- **Record:** ASSUMPTIONS section D, "The wall measured against temperature" (`configs/cqg_tube_arrhenius_lam125.json`;
  EXPLORATORY) and "Sealed runs" (`configs/cqg_spark_threshold_lam125.json`; EXPLORATORY; the config's `_purpose`
  begins "EXPLORATORY"); PREREGISTRATION T7, amendments 1 to 4; O64.

### 1b. Sec. III, line 145 (the Arrhenius test)

- **Current:** `separate question, answered in Sec.~\ref{sec:lambda}. Over twelve conditions ($g = 1.4$ to 2.5, $N = 64$ and 144,`
- **Proposed:** `separate question, answered in Sec.~\ref{sec:lambda}. In an exploratory test (the prediction was
  written into the run's configuration before it ran, but not pre-registered), over twelve conditions ($g = 1.4$ to
  2.5, $N = 64$ and 144,`
- **Record:** ASSUMPTIONS section D, "The wall measured against temperature: a prediction with nothing fitted
  (2026-09-20; `configs/cqg_tube_arrhenius_lam125.json`; EXPLORATORY, sixteen replicas)".

### 1c. Sec. IV, line 223 (the seed threshold)

- **Current:** `\emph{A local, size-independent threshold.} With one store holding a seed $s$ and nothing else, the torus`
- **Proposed:** `\emph{A local, size-independent threshold (exploratory).} With one store holding a seed $s$ and
  nothing else, the torus`
- **Record:** ASSUMPTIONS section D, "Sealed runs: what becomes of the energy given off (2026-09-20;
  `configs/cqg_spark_threshold_lam125.json`; EXPLORATORY, eight replicas)". The abstract's sentence at lines 31 to 33
  quotes this result and would be covered by 1a.

### 1d. Sec. III, lines 206 to 208 (how TWO-STATE CHANGE was reached)

- **Current:** `45 units. The pre-registered verdict, a two-state change, holds at $N = 64$, 96 and 192; at $N = 144$ one
  decay changed state inside its final measuring window and the size was set aside by the energy gate as
  written, with all three predictions holding there too.`
- **Proposed:** `45 units. The pre-registered verdict, a two-state change, holds at $N = 64$, 96 and 192, under an
  energy gate the author amended four times: once after the first runs, to fix when the release is read, and three
  times after the rerun whose verdict each amendment bore on (to allow the four-point relic, to replay the decays
  that reached the settle cap, and to read unusual resting states from their wiring); every amendment is on the
  record with its timing \cite{repo}. The three predictions, which concern the first switch, were not amended and
  held on both sets of seeds. At $N = 144$ one decay changed state inside its final measuring window and the size was
  set aside by the energy gate as written, with all three predictions holding there too.`
- **Record:** PREREGISTRATION T7, amendments 1 ("written after the first runs ... and before the rerun"), 2
  ("Written after the rerun `t7b_lam125_n*`, which it would change the verdict of. Stated first."), 3 and 4 ("It
  changes a gate after the data it judges were seen"); O13 and its addenda; O64.

---

## 2. Abstract, line 29: "and the wait is memoryless"

- **Current:** `Arrhenius law with nothing fitted, and the wait is memoryless. After the first exit the conversion spreads as a`
- **Proposed:** `Arrhenius law with nothing fitted, and the wait is close to memoryless (the pre-registered checks pass in
  most cells and fail in some, on a check band too tight or on rare very long waits; Sec.~\ref{sec:lambda}). After
  the first exit the conversion spreads as a`
- **Record:** T8 reading (criterion (a) fails in 9 cells); T23 reading ((a′) fails at λ = 1.30, N = 64, CV 2.63);
  T24 reading and O52 ((a′) fails in 4 of 28 cells, including λ = 1.25, N = 64); O42 (the whole-distribution test is
  post hoc: p = 0.03 on all 865 pre-registered waits with nothing set aside, 0.55 after the detection artifact is
  set aside; an unexplained tail at λ = 1.05). At λ = 1.25 itself the T7 check passed at every size and T23's did,
  but T24's failed at N = 64 on one wait of 24 τ.

---

## 3. Abstract, lines 35 to 37: "keeps its two-order, single-front character wherever it is"

- **Current:** `from 64 to 288 vertices. Mapped from $\lambda = 1.05$ to 1.45, the torus is metastable
  up to 1.35 and the change keeps its two-order, single-front character wherever it is, finishing cleanly near
  $\lambda = 1$ and leaving more defects as $\lambda$ grows.`
- **Proposed:** `from 64 to 288 vertices. Mapped from $\lambda = 1.05$ to 1.45 in three pre-registered runs, each
  inconclusive by the letter of its rules, the torus is metastable up to 1.35; the change keeps its two-order,
  single-front character from 1.05 to 1.30 in all three runs and begins to break up at 1.35, finishing cleanly near
  $\lambda = 1$ and leaving more defects as $\lambda$ grows.`
- **Record:** T23 reading (at λ = 1.35, N = 192, (c) fails, largest piece 0.67; N = 64 and 96 "count as not stuck
  (median f_200 = 0.25, on the line)"); T24 rerun of `scripts/analyse_t24.py` (λ = 1.35, N = 192: largest piece 0.69,
  below the 0.70 of (c)); T8 reading ((b) and (c) hold everywhere stuck, 1.05 to 1.35); O38, O44, O52.

---

## 4. Sec. V, lines 285 to 286: the count of memoryless failures in T8 is 9, not 5

- **Current:** `be memoryless, with a coefficient of variation between 0.7 and 1.3; at thirty decays that band is about two
  standard errors wide, and it fails in five of the 28 stuck cells (at $\lambda = 1.10$, 1.30 and 1.35). At`
- **Proposed:** `be memoryless, with a coefficient of variation between 0.7 and 1.3; at thirty decays that band is about two
  standard errors wide, and it fails in 9 of the 24 stuck cells the map ran (at two sizes at $\lambda = 1.10$,
  three at 1.30 and all four at 1.35). At`
- **Record:** T8 reading ("1.10: ... (a) fails at N = 64 (CV 0.64) and N = 192 (1.36). 1.30: ... (a) fails at N = 96,
  144, 192 ... 1.35: ... (a) fails (0.37 to 0.62)"); `scripts/analyse_t8.py` rerun: CVs at 1.35 are 0.46, 0.46, 0.62,
  0.37, all outside the band. The map ran six stuck λ at four sizes (24 cells); 28 counts T7's λ = 1.25, which the map
  did not rerun.

---

## 5. Sec. V, lines 293 to 302: the second repeat's gate was not an energy check; the extreme waits are multiples of τ, at N = 64

- **Current:** `then held in every stuck cell up to $\lambda = 1.25$ and in three of four sizes at 1.30, but the unchanged energy
  check failed one cell per size at 1.30, because it compared a window average of the energy with the exact energy of
  the final graph and the sheet's own thermal excitations at $g = 1.5$ exceed its 1\% tolerance in a few decays per
  hundred. The second repeat read the energy exactly from each decay's saved final graph, and that check passed in all
  28 cells, with two orders and one front in every cell as before; the memoryless check now failed in four cells, each
  on one or two waits of 24 to 76 times the mean at $N = 64$ and 192. So three runs have tripped three different
  criteria, on a band, a catalog, and a single extreme wait in 120, while the physics has read the same each time.`
- **Proposed:** `then held in every stuck cell up to $\lambda = 1.25$ and in three of four sizes at 1.30, but the unchanged energy
  check failed at every size at 1.30; read after the fact and not scored, it compared a window average of the energy
  with the exact energy of the final graph, and the sheet's own thermal excitations at $g = 1.5$ exceed its 1\%
  tolerance in a few decays per hundred. The second repeat replaced that check with one that asked only that each
  decay's saved final graph exist and be valid, which held in all 28 cells, and read the energy exactly from those
  graphs, reporting it rather than gating on it; two orders and one front held in every cell up to 1.30 as before.
  The memoryless check now failed in four cells: at $N = 64$ ($\lambda = 1.25$ and 1.30), each on a single wait 24
  and 76 times the predicted mean $\tau$, and at $N = 192$ (1.30) and 144 (1.35), with coefficients of variation of
  1.53 and 1.41 against a band ending at 1.38. So three runs have tripped three different criteria, on a band, a
  catalog, and the far tail of the waits, while the physics has read the same each time.`
- **Record:** T24 definitions ("Gate 3′ ... That is all the gate asks: it is a check that the record is complete";
  resting states "read exactly and reported, never gated"); T24 Why ("Read after the fact (not scored)"); T24 reading
  ("20,070 sweeps (24 τ) at 1.25 and 31,955 (76 τ) at 1.30, both at N = 64"). Recomputed from `results/t24_*.csv`:
  against the cell means these waits are 16 and 39 times; the N = 192 (λ = 1.30) and N = 144 (1.35) cells have no
  wait beyond 6 times their mean. "Two orders and one front in every cell" holds in the window (1.05 to 1.30); at
  1.35, N = 192, the largest piece is 0.69 (item 3).

---

## 6. Sec. III, lines 202 to 205, and Sec. IV, line 242: which resting state is common, and what the relic's geometry is

### 6a. Lines 202 to 205

- **Current:** `release $\varepsilon$ per vertex to within 1\%. The others settle on metastable defected sheets, read from
  their wiring: most often one column of the torus left curled, four vertices at $d = 1$ with $S = N + 1$,
  $X = 6$, costing $24\lambda - 16$ (14 at $\lambda = 1.25$), the relic defect of Sec.~IV; more rarely combinations of small defects of 8 to
  45 units.`
- **Proposed:** `release $\varepsilon$ per vertex to within 1\%. The others settle on defected sheets, read from their
  wiring: most often combinations of small defects of 8 to 45 units, and less often the four-point relic of
  Sec.~IV, a closed loop of four vertices at $d = 1$ with $S = N + 1$ and, in its commonest form, $X = 6$, costing
  $24\lambda - 16$ (14 at $\lambda = 1.25$). Whether these states are stable or only slow is not known.`
- **Record:** O13, first addendum (at the end of the settle, 0 to 1 decays per size on the one-relic ledge against
  2, 4, 2 and 6 on neither) and third addendum (12 of the 14 replayed decays rest on combinations of small defects;
  "Not claimed. Which of the twelve are stable rather than slow beyond the six already seen unchanged"); O28 addendum
  (the loop of four; its 4-, 9- and 14-unit forms).

### 6b. Line 242 (the geometry of the cold-box relic)

- **Current:** `a slope of $0.0003 \pm 0.0003$ per vertex, standard error); the defect is the curled column above (14 units),`
- **Proposed:** `a slope of $0.0003 \pm 0.0003$ per vertex, standard error); the defect is the four-point loop above
  (14 units), whose points in these cold boxes span one to four of the torus's original columns, lying along it,`
- **Record:** O16 ("it is not a ring ... the four d = 1 vertices span one to four columns, mostly two or three, lying
  along the tube"; CLAUDE.md lists this among the corrections that must not be undone); O28 addendum (read from the
  wiring of two decays, the loop is a closed 4-cycle; in one, `t7d` N = 144 replica 3, it is an original column).
  Figure 1's definition of a column (lines 101 to 102) can stay; the paper should not call the cold-box relic "one
  column".

---

## 7. Sec. II, lines 123 to 125, and Sec. IV, lines 226 to 228: the twisted family was checked along a walk, not exhaustively

- **Current (123 to 125):** `every neighbourhood as it was, and every arrangement they lead to has the same counts of A and B (checked by
  enumeration along a walk of such switches \cite{repo}).`
- **Proposed:** `every neighbourhood as it was, and every arrangement met along a 60-step walk of such switches (three
  classes up to relabelling) has the same counts of A and B \cite{repo}.`
- **Current (226 to 228):** `spare the torus never converts, although the flat torus is lower. That nothing below 12 can set it off holds
  for any energy-conserving dynamics made of single switches, since no switch out costs less; that 12 always`
- **Proposed:** `spare the torus never converts, although the flat torus is lower. That nothing below 12 can set it off,
  from the perfect torus and from the twisted arrangements the walk met, holds for any energy-conserving dynamics
  made of single switches, since no switch out of them costs less; that 12 always`
- **Record:** O42 ("Every arrangement met along a 60-step walk has exactly the perfect torus's 3N A, 2N B and N/2
  neutral switches ... The walk met 3 isomorphism classes").

---

## 8. Abstract line 24, Introduction line 62 and Sec. II lines 86 to 88: the ground state is a family

- **Current (24 to 25):** `For $\lambda \ge 1$ the flat lattice torus is
  the ground state exactly,`
- **Proposed:** `For $\lambda \ge 1$ the flat lattice torus is a ground state exactly,`
- **Current (62 to 63):** `For $\lambda > 1$ the flat torus is the unique ground
  state and each curled direction costs a known energy per vertex.`
- **Proposed:** `For $\lambda > 1$ the ground states are the arrangements with two squares on every edge, the flat torus
  and its twisted relatives, and each curled direction costs a known energy per vertex.`
- **Current (86 to 88):** `for any graph with two squares on every edge: the flat lattice torus. For $\lambda > 1$ nothing else
  reaches zero.`
- **Proposed:** `for any graph with two squares on every edge: the flat lattice torus and its twisted relatives, of
  which there can be several (three classes at $N = 18$). For $\lambda > 1$ nothing else reaches zero.`
- **Record:** O57, addendum ("of the three classes with S = 18 and X = 0 (the flat energy, no curling)"), from the
  complete enumeration of T4.

---

## 9. Introduction, lines 67 to 68: the attribution of the chain

- **Current:** `edge switch with Metropolis acceptance, as used to sample the model \cite{KTB19}. It samples the model's`
- **Proposed:** `edge switch used to sample the model \cite{KTB19}, with Metropolis acceptance and an ordered-pair proposal
  that are our choices (Ref.~\cite{T25} uses Glauber acceptance). It samples the model's`
- **Record:** ASSUMPTIONS Q4 ("'Edge switches': [KTB19] Sec. 4. Details: ours. Metropolis: [NB99]. Glauber: [T25]
  Eq. (28)"). The rates, and so every kinetic number, depend on these choices.

---

## 10. Sec. V, lines 280 to 281: "falls apart everywhere at once" beyond the edge

- **Current:** `a feature of the larger coefficients, and near $\lambda = 1$ the change is clean. Beyond the edge
  ($\lambda \ge 1.40$) the torus falls apart everywhere at once and ends mostly as a defected sheet.`
- **Proposed:** `a feature of the larger coefficients, and near $\lambda = 1$ the change is clean. Beyond the edge
  ($\lambda \ge 1.40$) the change starts more and more often in several places at once (in about half the decays at
  $N = 64$ and in all of them at $N = 192$) and ends mostly as a defected sheet.`
- **Record:** `results/t8_lam140.csv`, `t8_lam145.csv`: converted region in more than one piece at 25 % conversion in
  15, 22, 27, 30 of 30 decays at N = 64 to 192 (λ = 1.40) and 14, 25, 30, 30 (1.45); largest piece at half conversion
  0.89 at N = 64, 0.47 at 192 (λ = 1.40).

---

## 11. Sec. V, lines 257 to 258: where Eq. (2) gives 200 sweeps

- **Current:** `The torus is stuck from $\lambda = 1.05$ to 1.35 at every size and not at 1.40 or 1.45; Eq.~(\ref{eq:tau}) puts
  the mean wait at 200 sweeps near $\lambda = 1.33$.`
- **Proposed:** `The torus is stuck from $\lambda = 1.05$ to 1.35 at every size and not at 1.40 or 1.45; Eq.~(\ref{eq:tau}) puts
  the mean wait at 200 sweeps at $\lambda = 1.345$, just above $4/3$, where move B takes over.`
- **Record:** Eq. (2) evaluated: τ = 259 at λ = 1.33 and 200.0 at 1.345 (g = 1.5). T8's prediction 2 (b) put the edge
  "at about 1.33, where move B takes over and the predicted wait falls through 200 sweeps"; the two coincide only
  roughly.

---

## 12. Table 2 caption, lines 310 to 313

- **Current:** `\caption{The map along $\lambda$ at $g = 1.5$ (ranges over $N = 64$ to 192; thirty decays per cell; $\lambda = 1.25$
  from Table~\ref{tab:t7}). Two orders: share of vertices at $d \in \{1,2\}$ at half conversion. Flat: share of
  decays ending at the flat torus.}`
- **Proposed:** add the row `1.25 & 845 & 660--1428 & 0.988--0.998 & 87\% \\` between 1.20 and 1.30, and change
  "$\lambda = 1.25$ from Table~\ref{tab:t7}" to "$\lambda = 1.25$ from the two runs of Table~\ref{tab:t7}, not rerun
  in the map". (Or, without the row, say that λ = 1.25 is in Table 1 and Sec. III.)
- **Record:** the table has no λ = 1.25 row; τ(1.25) = 845 (Eq. (2); T8 table); Table 1 gives the waits (660 to 1428)
  and the two-order shares (0.988 to 0.998); T8 reading gives "13 % at 1.25 in T7b" ending on a defected sheet.

---

## 13. Missing caveats (additions, no text removed)

### 13a. The coarse front law (T12), after line 162

- **Add:** `A separate pre-registered test of whether a coarse law of a single front governs these decays (T12 in
  Ref.~\cite{repo}; 64 decays at two couplings) came out NOT ESTABLISHED: 21 of the 59 that nucleated converted in more
  than one patch, mostly at the warmer coupling, and the front's rate fell roughly as $N^{-0.7}$.`
- **Record:** PREREGISTRATION T12 verdict; O24.

### 13b. The λ = 1.5 runs of the same pre-registration, after line 162

- **Add:** `The same pre-registration listed $\lambda = 1.5$; there the torus is not metastable at $g = 1.5$ (its
  square density falls to 0.95 per vertex, below the flat torus's 1, within 50 sweeps in every replica), and no
  verdict was applied.`
- **Record:** PREREGISTRATION T7, closing note; O13 ("λ = 1.5 is the unstable case").

### 13c. Gate B, in Methods, line 388

- **Current:** `square density of Ref.~\cite{KTB19} (Fig.~8a) at $N = 160$ to rms 0.005. Every kinetic quantity quoted is`
- **Proposed:** `square density of Ref.~\cite{KTB19} (Fig.~8a) at $N = 160$ to rms 0.005; it does not reproduce the steeper
  curve of Ref.~\cite{T25} (Fig.~3) at the same size, from which it differs by up to 0.41 between $g = 2$ and 6.3, a
  disagreement between the two published figures that is still open. Every kinetic quantity quoted is`
- **Record:** TASKS Gate B; O27; CLAUDE.md "Gates".

### 13d. The random-phase contrast, line 212

- **Current:** `at $N = 100$ and falling with $N$ \cite{repo}. At this $\lambda$ the sharp change is between orders.`
- **Proposed:** `at $N = 100$ and falling with $N$ \cite{repo}; the pre-registered verdict there is INCONCLUSIVE, because one
  of its criteria cannot be read where the cold phase sits at zero energy. At this $\lambda$ the sharp change is
  between orders.`
- **Record:** O17; PREREGISTRATION T6, amendment 5; VISION Update 15.

### 13e. The interchangeable-points estimate, line 370

- **Current:** `factor of order $N$, and the waiting time would grow with the system instead of staying flat. We have not run
  the decay with interchangeable vertices.`
- **Proposed:** `factor of order $N$, and the waiting time would grow with the system instead of staying flat. This is
  transition-state reasoning: the choice fixes the equilibrium weights but not the kinetics, so "of order $N$" is the
  change in the effective barrier, not a derived clock. We have not run the decay with interchangeable vertices.`
- **Record:** PREREGISTRATION T8, "Named or interchangeable points" ("this is transition-state reasoning ... 'N times
  rarer' is the change in the effective barrier, not a derived clock").

### 13f. The Outlook, lines 379 to 381

- **Current:** `fixed size and about one per change at every size we reached, is the kind of object a dark-matter relic of such a
  change would have to be, and that the change`
- **Proposed:** `fixed size and about one per change at every size we reached, is the kind of object a dark-matter relic of such a
  change would have to be, though it anneals away at every fixed coupling we tried and its number grows with the
  number of seeds that start the change \cite{repo}; and that the change`
- **Record:** PREREGISTRATION T19 (ANNEALS at g = 1.0, 1.25, 1.5; O35) and T17 (BETWEEN; O33); T25 (FREEZES IN on
  cooling; O47) could be named in the same clause.

### 13g. The definition of "stuck", lines 253 to 255

- **Current:** `stuck at ($\lambda$, $N$) when more than half its decays are still at least 75\% torus after the 200-sweep rest
  that defines the waiting time.`
- **Proposed:** `stuck at ($\lambda$, $N$) when more than half its decays are still at least 75\% torus after the 200-sweep rest
  that defines the waiting time (the pre-registered definition, PREREGISTRATION T8 in Ref.~\cite{repo}).`
- **Record:** PREREGISTRATION T8, "Definitions, fixed now" (metastable: f_200 < 0.25 in more than half the decays).

---

## Referee points on paper 1 not carried here

None of the referee's points on paper 1 failed the check; each was verified before being listed. Two remarks:

- Item 11: the referee's "It is move B that takes over at 4/3" is right; the paper's "near 1.33" came from the T8
  pre-registration, which conflated the two nearby values.
- Item 1d proposes disclosure only. It does not change the verdict: the amendments are on the record and were the
  owner's decisions.
