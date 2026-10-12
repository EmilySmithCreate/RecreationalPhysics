# Observer-relative histories: technical implementation plan

Written 2026-10-12, before any Stage E number was computed and after the Stage B to D code and its exact tests were
in place. The program it implements is `observer_relative_histories_research_handoff.md` in this folder (the owner's
handoff of the same day). The literature-to-math map that Stage A asks for is `orh_stage_a_literature_map.md`, built
from the reading notes `docs/reading/notes/2026-10-12_orh_*.md`.

**Kind of statement (CLAUDE.md rule 10).** Everything in this plan is *ours*: a working plan drafted with Claude and
not reviewed by a physicist. The handoff itself is the owner's commission. Nothing here is a claim about reality.

## 1. What this program is, and what it is not

It is a research program inside established Everettian quantum mechanics and decoherent-histories theory, as the
handoff says in its section 0. Its job is to find out which of the handoff's statements are standard results, which
are modeling assumptions, and whether any new, falsifiable consequence comes out; and to build small exact models that
show the standard results at work.

It is **not** a run of the project's toy (the graph model of `src/graphity`). It adds no knob to that toy, so VISION
S1 is not touched and no VISION decision is needed for the work below. Where it meets the hypothesis is the
programme's pieces 9 (quantum behavior from counting versions), 10 (time) and 12 (the loop and its measure): the
owner's "versions all standing at once until an interaction tells them apart" is, in this program's language,
Everett's relative states with records; and the strange-loop measure of VISION Updates 23, 26 and 43 is an
observer-counting rule of the kind Stage E makes explicit. Whether this program becomes a piece of the programme page
is the owner's decision; this plan proposes a card for it and marks it as ours.

## 2. Where everything lives

| What | Where |
|---|---|
| The handoff (the owner's) | `docs/theory/observer_relative_histories_research_handoff.md` |
| Stage A, the literature-to-math map | `docs/theory/orh_stage_a_literature_map.md` |
| The reading notes, one per group of papers | `docs/reading/notes/2026-10-12_orh_*.md`; the prior-work search `docs/reading/notes/2026-10-12_prior_work_observer_relative_histories.md` |
| The assumption register for this program | `docs/theory/orh_assumptions.md` (one pointer entry in `ASSUMPTIONS.md`) |
| The simulator and the models | `src/orh/` (`statevector.py`, `darwinism.py`, `histories.py`, `observers.py`, `cosmic.py`) |
| The exact tests | `tests/test_orh_*.py` |
| The scripts that write results and figures | `scripts/orh_stage_bcd.py`, `scripts/orh_stage_e.py`, from `configs/orh_*.json` |
| Results (append-only, with `.meta.json`) | `results/orh_*.csv` |
| Figures | `docs/figures/orh_*.png` |
| The findings, in one place | `docs/theory/orh_findings.md` |

## 3. Method, stage by stage

### Stage A: literature-to-math map

Each formula and commitment of the handoff is set against the fourteen references, read in full or in the named
sections by assistant agents on 12 October 2026, and marked STANDARD (with the paper, section and equation), a
SIMPLIFYING ASSUMPTION, or NOVEL (not found in the papers; then the prior-work note says where else it was looked for).
The map also lists what the papers say that the handoff does not.

### Stage B: the exact small Hilbert-space model

*The model.* A system qubit S in sqrt(1 - p)|0> + sqrt(p)|1>; N environment qubits each written on by a controlled
tilt of angle theta (theta = pi/2 is Zurek's controlled-NOT, a perfect copy); observer registers that copy fragments
by controlled-NOTs. All of it is unitary; nothing collapses (`src/orh/statevector.py`).

*The exact benchmarks, written before the simulator was run and encoded in `tests/test_orh_darwinism.py`
(`src/orh/darwinism.py` holds the formulas):*

- visibility V = 2 sqrt(p(1 - p)) prod_i cos(theta_i), which is |<E_B|E_A>| for p = 1/2 (handoff section 3);
- the partial-information plot I(S:F) = f(c_all) + f(c_F) - f(c_rest), with f(c) the entropy of a two-state mixture of
  overlap c and c_X = prod_{i in X} cos(theta_i); its classical plateau at h(p) and quantum rise to 2h(p) for perfect
  records;
- redundancy R_delta = N / m_delta;
- the disagreement rate of two observers copying different fragments, p(cos^2 theta_i sin^2 theta_j + sin^2 theta_i
  cos^2 theta_j), zero for perfect records;
- the quantum eraser (full visibility in each sorted subensemble, none overall) and recombination (the inverse
  interaction restores V = 1).

*Output.* Visibility against the environment overlap; the partial-information plot for several record strengths;
redundancy against record strength; the eraser and recombination rows (`results/orh_stage_bcd.csv`, figures
`docs/figures/orh_stage_b_*.png`).

### Stage C: the history-measure model

*The construction.* Class operators as chains of projectors on the simulator's branch vectors, C_alpha |psi_0> =
P_{alpha_n} U_n ... P_{alpha_1} U_1 |psi_0>, and the decoherence functional D(alpha, beta) = <psi_beta|psi_alpha>
(`src/orh/histories.py`). Families are fixed in advance (branch-independent), which the map records as a simplifying
assumption against Gell-Mann and Hartle's branch-dependent chains.

*What is checked, exactly (`tests/test_orh_histories.py`):*

1. The two-slit family interferes: off-diagonal D = 1/4, the sum rule for "output 0" fails (fine-grained sum 1/2
   against coarse-grained probability 1), and yet the diagonal sums to 1 because the off-diagonal terms cancel in
   pairs. So "the exhaustive weights sum to one" is a weaker statement than decoherence; the sum rules, one per
   coarse graining, are the test.
2. The same family with a perfect record written between the two times is exactly decoherent; with a record of
   strength theta the off-diagonal term is cos(theta)/4.
3. Nested records: for a sequence of records that extends, the compatible sets nest, mu is nonincreasing, the
   surprisal -log2 mu is nondecreasing, the conditional measure inside each set sums to one and the total stays one.
4. Two observers of one record: mu(C(R_A = 0, R_B = 0)) = mu(C(R_A = 0)), not its square; mu(C(R_A = 0, R_B = 1)) = 0.
5. An erased record is not a permanent fact: once the record is undone, the family that includes its earlier value has
   off-diagonal D = 1/4 again (the "permanence of the past" caveat, made exact).
6. Born weights are not branch counts (p = 0.9 gives weights 0.1 and 0.9 for two histories), and duplicating a
   register changes no weight.

### Stage D: within-history observers

Observers are register sets in one world (`src/orh/observers.py`): they read fragments, tell each other, forget (a
swap into a fresh environment qubit; the world keeps the information), are duplicated, and die. What is reported is
the joint distribution of their records, never a product of marginals. Exact checks (`tests/test_orh_observers.py`):
two observers of one error-free record never disagree while the product of marginals says they do 21 % of the time;
telling correlates an observer who had nothing; forgetting leaves the observer ignorant and the world informed and
widens the observer's compatible set; duplication changes the register count and not the Born weights; a register
that is not in a low-entropy state cannot hold a record (reading it is a coin toss); the forward circuit run
backwards unwrites every record, so the growth of records along the circuit comes from the blank initial registers.

### Stage E: a separate cosmological population model

**Declared here before any number is computed; changes after computing are new, dated entries.**

*Background.* One fixed flat FLRW cosmology with the Planck 2018 parameters transcribed in the cosmic-time reading
note; cosmic time from redshift by the standard integral. A finite comoving region (1 comoving Gpc^3; the results are
per unit comoving volume and the region only makes the integrals finite).

*Inputs, each with its source in the reading note and in `orh_assumptions.md`:*

- the cosmic star-formation history psi(z) of Madau and Dickinson 2014, Eq. (15), extended into the future by the
  exponential fall of its own high-redshift-to-present trend (a declared extrapolation, not data); a second future
  branch that cuts star formation off at a declared time, to show the sensitivity;
- a stellar initial mass function (the form Loeb, Batista and Sloan 2016 use, from the reading note) between 0.08 and
  3 solar masses; main-sequence lifetime t_MS(M) = 10 Gyr (M / M_sun)^(-2.5), capped at the age at which the model
  stops (Loeb et al.'s relation; to be matched to the note);
- habitable-planet occurrence per star eta (a synthetic constant, scanned), with a metallicity factor only if the
  note supplies a published form;
- an evolutionary delay tau_evo before observers appear (synthetic: 1, 4 and 8 Gyr, with Earth's 4.5 Gyr marked);
- an observer window: observers exist from t_birth + tau_evo until min(t_birth + t_MS, t_birth + tau_evo + L_obs), with
  the observer-moment rate per inhabited planet r (synthetic constant; it cancels in F(t_0) unless it varies);
- an interaction factor: a multiplicative function of the local density of inhabited planets, speculative and
  scanned (none, mild positive, mild negative), as the handoff's "interactions and civilizations sensitivity";
- the low-mass cutoff of habitability (the red-dwarf question): 0.08 M_sun (friendly) or 0.5 M_sun (suppressed).

*Outputs.* W(t) per comoving volume; p(t | sampled observer-moment); F(13.8 Gyr); T_support and t_99.99 where the
integral converges; all on a logarithmic time axis from 10^8 to 10^14 years; a table of F(13.8 Gyr) under every
scenario and three reference classes (uniform over observer-moments; uniform over observers, which divides by the
observer lifetime; uniform over inhabited planets).

*Our expectation before computing (ours; recorded so that it can be wrong).* Under the red-dwarf-friendly scenario
F(13.8 Gyr) is small, a few per cent at most, because the integrated star-formation of the far future is dominated
by stars that live 10^12 to 10^13 years; under the suppressed scenario (0.5 M_sun cutoff) F(13.8 Gyr) lies between
0.2 and 0.6; no scenario makes 13.8 Gyr the median unless the cutoff is raised to near a solar mass or star formation
is cut off within a few Gyr. We also expect that the t_99.99 is undefined (the integral does not converge) in any
scenario that admits an observer-supporting process with no end, and defined otherwise by the longest stellar
lifetime admitted. The number that the handoff's reading of "we are early" needs is the comparison of F(13.8 Gyr)
across reference classes, and our expectation is that the reference class moves F(13.8 Gyr) by more than the stellar
inputs do.

### Stage F: outputs

(1) visibility against environment overlap; (2) the decoherence functional, diagonal and off-diagonal, for the
two-slit family at four record strengths; (3) the measure of one record's compatible set against the conserved total;
(4) the joint distribution of two observers' records against the product of marginals; (5) W(t) on a logarithmic
axis under the scenarios; (6) F(13.8 Gyr) under every scenario and reference class. With: the exact tests (rule 6),
the input uncertainty where an input is published with one, the commit and dirty flag in every `.meta.json`
(`graphity.results.provenance`), and the reasons any model fails.

## 4. Process rules applied

- Tests pass before every commit (rule 6); results are append-only and come from a config through a script (rule 5).
- Every input to Stage E has a source or is marked synthetic (rule 1), in `orh_assumptions.md`; the detailed
  register lives there because `ASSUMPTIONS.md` is being edited by another session in the shared working tree, and one
  pointer entry is added to `ASSUMPTIONS.md` instead.
- Anything that has not been found in the literature is written as "we have not found", with the prior-work note
  behind it (rule 15).
- The four kinds of statement (rule 10) are used on everything a reader outside the project will see; the handoff's
  own commitments are the owner's; the readings of results are ours.
- Nothing here is promoted to the hypothesis's claims; VISION is not changed by this program.
