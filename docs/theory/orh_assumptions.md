# Observer-relative histories: the assumption register

CLAUDE.md rule 1 for the program of `observer_relative_histories_research_handoff.md`. Each entry has a status:
**Sourced** (a published equation or number, with where), **Calibrated** (set to match a published result),
**Ours** (a modeling choice of this program, declared), **Unverified** (ours and not yet checked by anyone). The
detailed register lives here because `ASSUMPTIONS.md` was being edited by another session in the shared working
tree on 12 October 2026; `ASSUMPTIONS.md` carries one pointer entry to this file. Entries are numbered P1 onward.

## The quantum toy (Stages B to D; `src/orh/statevector.py`, `darwinism.py`, `histories.py`, `observers.py`)

- **P1. Unitary evolution, no collapse; a measurement is an entangling gate.** Sourced: Everett 1957, Secs. 3 and 5;
  the relative-state move. The controlled-NOT as the ideal measurement: Zurek 2003, Sec. II.1.1 and Eq. 7.1.
- **P2. Records of strength theta by a controlled tilt** (if the system is |1>, the record qubit goes from |0> to
  cos theta |0> + sin theta |1>). Ours: the standard one-parameter family of imperfect measurements; theta = pi/2 is
  Zurek's controlled-NOT. Everything is a function of the overlaps c_F = prod cos theta_i, which is the r(t) of Zurek
  2003 Eqs. 4.11 to 4.12 in a different parameterization.
- **P3. Visibility V = 2 sqrt(p(1 - p)) prod cos theta_i.** Sourced in substance: Zurek 2003 Eq. 4.12; Zurek 2009
  Eq. 5 (for p = 1/2, V = |<E_B|E_A>|). The general factor 2 sqrt(p(1 - p)) is elementary; checked by
  `test_orh_darwinism.py`.
- **P4. The partial-information plot I(S:F) = f(c_all) + f(c_F) - f(c_rest)** with f the entropy of a two-state
  mixture of overlap c. Ours, derived in `darwinism.py`'s docstring from the purity of the global state; the
  quantum-Darwinism note gives the same form (its Sec. 3) and names Blume-Kohout and Zurek 2005 as the source to
  verify it against (not read). The von Neumann mutual information is used, which rises to 2h(p) for the whole
  environment; the Holevo quantity (plateau at h(p)) is not computed. Declared choice (the note's point).
- **P5. Redundancy R_delta = N / m_delta** with m_delta the smallest fragment carrying (1 - delta) h(p). Sourced as
  the definition of Zurek 2009 (the note, Sec. 1); Zwolak and Zurek 2017 Eqs. 11 and 15 use a definition that differs
  by ln(1/delta). delta = 0.1 here. Ours: the choice between the two.
- **P6. Class operators as branch-independent chains of computational-basis projectors; D as the Gram matrix of
  branch vectors.** Sourced: Gell-Mann and Hartle 1993 Eqs. 4.1 and 4.5; 2018 Eq. 8 (pure initial state). Ours: the
  branch-independent form, a special case the papers call not general (1993 Eq. 4.4), and the final condition of
  indifference rho_F proportional to the identity (Hartle 2020 Eq. 5.1), which a one-boundary functional assumes.
- **P7. "Decoherent" means medium decoherence (every off-diagonal D vanishes).** Sourced: 1993 Eq. 4.8. Ours: the
  choice to test the sufficient condition; `histories.sum_rule_violations` reports the sum rules separately, which is
  what weak decoherence (1993 Eq. 4.6) governs.
- **P8. A record R_n is a set of (step, alternative) pairs; C(R_n) is the set of labels carrying them.** Sourced as a
  coarse graining (1995 Eq. 2.4). Ours: perfect records in the kept-record families; partial records are run as
  well. This is the IGUS's memory, not Gell-Mann and Hartle's generalized record (1995 Eq. 3.1); the two are kept
  apart in Stage D.
- **P9. Observers are register sets; forgetting is a swap into a fresh environment qubit; death is every register
  swapped away; duplication is a controlled-NOT into a fresh qubit.** Ours. Unitary by construction; the world keeps
  what the observer loses.
- **P10. "The arrow of records" in the toy is the growth of the number of registers correlated with S along a circuit
  started from blank registers.** Ours. Hartle 2020 says arrows arise from the asymmetry between initial and final
  conditions; the toy's blank start is the initial condition and its implicit final condition is indifference (P6).
  Nothing about experienced time is modeled.

## The population model (Stage E; `src/orh/cosmic.py`)

- **P11. Flat matter + Lambda background, Planck 2018 Table 2 (TT,TE,EE+lowE+lensing): H_0 = 67.36, Omega_m = 0.3153,
  Omega_Lambda = 0.6847, age 13.797 Gyr.** Sourced ([Planck18], Table 2; the cosmic-time note Sec. 4). Radiation
  omitted: it changes the age by 0.006 Gyr (the note's check). The closed-form a(t) and t(z) are textbook.
- **P12. Star-formation history: Madau and Dickinson 2014 Eq. 15,** shape only (its normalization cancels), with a
  Salpeter calibration that Loeb et al. combine with a Chabrier IMF (harmless for the shape; the note Sec. 3).
  Sourced and verified at source. Continued into the future through a(t) > 1 and cut off by exp(-t/50 Gyr):
  Calibrated to Loeb et al. 2016 Sec. 2.6 (their t_1 = 50 Gyr; 20 Gyr as the alternative; no cutoff as a third
  branch of ours).
- **P13. First stars at 30 Myr.** Sourced: Loeb et al. 2016 Sec. 2.3.
- **P14. Chabrier IMF, Loeb et al. Eq. 2.2,** with a = 790, sigma = 0.69, m_c = 0.08; the placement of the 1/m factor
  read from the text layer and marked to verify in the note; the two pieces meet at one solar mass to 3 %.
  Sourced, with that caveat. Mass range 0.08 to 3 solar masses (Loeb et al. Sec. 2.2).
- **P15. Main-sequence lifetimes, Loeb et al. Eq. 2.3** (piecewise; tau(0.08) = 1.07 x 10^13 yr). Sourced.
- **P16. eta_Earth and p(life|HZ) constant in mass and time**, so they cancel. Calibrated to Loeb et al. Sec. 2.7
  (their choice, stated as such with its reasons).
- **P17. The evolutionary delay tau_evo (0, 1, 4.5, 8 Gyr)** before observers appear on a planet. Ours; synthetic.
  Loeb et al. have none (their delays enter only through m_max); 4.5 Gyr is Earth's, marked.
- **P18. The observer window L_obs** (the star's whole life; 1 Gyr; 10 Myr). Ours; synthetic. Nothing measured sets
  it; Hanson et al. 2021 and Kipping 2025 use truncated windows of their own.
- **P19. The lower mass cutoff m_min: 0.08, 0.5, 0.9 solar masses.** Calibrated to Loeb et al.'s scan (0.08 to 1.64);
  the physics for 0.5 is in Lingam and Loeb 2018 and Kipping 2025 (abstracts only).
- **P20. Reference classes: uniform over observer-moments; uniform over inhabited planets counted once at origin;
  observer-moments weighted linearly by the age of the planet's observer era.** Ours. The first is the handoff's and
  Sebens and Carroll's (their Eq. 42); the second is Lineweaver and Egan 2007's and Hanson et al. 2021's kind; the
  third is the simplest form of Loeb et al.'s remark (Sec. 4) that a given observer is more likely later in a planet's
  existence. Unverified against any data; nothing could verify it.
- **P21. The interaction factor (n(t)/n_max)^gamma, gamma in {0, 0.5, -0.5}.** Ours; speculative, as the handoff
  says of its interactions scenario. Hanson et al. 2021's preemption rule is the published relative.
- **P22. Exotic late observers at a constant rate per physical volume (eps a^3 per comoving volume).** Ours, as the
  handoff's late-time stress test; the reason it diverges is Bousso, Freivogel and Yang 2008 Sec. V.E.
- **P23. Two ways to combine histories: pooled (the handoff's F(t_0); Sebens and Carroll Eq. 39/42) and averaged
  within each history then weighted (Srednicki and Hartle 2010 Eqs. B3 to B4).** Sourced, both; the note on Everett
  and self-location, Sec. 6(b). Which is right is not decided by anything here.
- **P24. F(13.8 Gyr) is a description under a declared rule and is never used as evidence for a measure.** Sourced:
  Hartle and Srednicki 2007 Eq. 4.2; Srednicki and Hartle 2010 Sec. III.
