# Observer-relative histories, Stage A: the literature-to-math map

Written 2026-10-12 from five reading notes made the same day by assistant agents, each of which read the papers
named below in full or in the sections it names (`docs/reading/notes/2026-10-12_orh_*.md`), and from the prior-work
search `docs/reading/notes/2026-10-12_prior_work_observer_relative_histories.md`. **Everything here is ours and
unverified** (CLAUDE.md rule 10): a reading of published work by AI agents, not reviewed by a physicist. Equation
numbers were checked against the papers' own labels where the notes say so and are marked "to verify" where they
rest on the order of labels in a TeX source.

Verdicts: **STANDARD** (stated in the paper, with the place); **SIMPLIFYING ASSUMPTION** (a special case the papers
allow but warn is not general, or a modeling choice the handoff declares); **NOVEL** (not found in the fourteen papers;
the prior-work note says where else it was looked for). A NOVEL *definition* is not a NOVEL *result*.

## 1. The answer in one paragraph

The handoff's quantum core is standard physics restated: unitary evolution with no collapse (Everett 1957, Sec. 3);
class operators, the decoherence functional and probabilities for a decoherent family (Gell-Mann and Hartle 1993,
Eqs. 4.1 to 4.8; 2018, Eqs. 8 to 14); records as orthogonal environment states and visibility as their overlap
(Zurek 2003, Eqs. 4.11 to 4.12; Zurek 2009, Eq. 5); redundant records read by many observers (Zurek 2009; Zwolak and
Zurek 2017). Its "key intuition" (section 2), the nested compatible set with nonincreasing measure, is Everett's own
Sec. 5 (Eqs. 26, 33, 34) in set language, and in decoherent-histories language it is Gell-Mann and Hartle's conditional
probability of the past given present records (2018, Eqs. 18, 20, 21). The one quantity the fourteen papers do not name is the
record surprisal I(R_n) = -log2 mu; it is the Shannon self-information of the record alternative, a definition and not
a result, and the prior-work search found it already defined on nested record algebras elsewhere (Martellini 2026,
to be read in full). The cosmic-time part (section 5) is a declared self-location rule of the Sebens-Carroll form (their Eqs. 39
and 42) applied to a population model whose published core is Loeb, Batista and Sloan 2016 (Eqs. 2.1 to 2.4); Loeb et
al. already compute the equivalent of F(t_0) and give about 0.1 % for the full stellar range, and three other published
calculations under other rules give 68 %, at most 8 % and below 1 % (prior-work note, claim C). What the handoff adds that
is not in the fourteen papers: the observer-moment density n_obs as the object (the papers count planets or leave the
rate unspecified; Hanson et al. 2021 come closest), the within-history interaction factor (Hanson et al.'s preemption
is a published rule of that kind), the end criterion T_support with t_99.99, and the demand that the joint record
distribution of interacting observers be modeled (Everett 1957 Sec. 5 already computes the agreement of several
observers). None of these is a prediction; each is a modeling device whose consequences Stages B to E compute. **No new
falsifiable consequence has been identified in Stage A, and the prior-work search returned FOUND on all three of the
handoff's candidate-novel claims** (`docs/reading/notes/2026-10-12_prior_work_observer_relative_histories.md`). The
places where the handoff is weaker than it reads are listed in section 4.

## 2. The map, section by section

### Handoff section 1, the commitments

| Commitment | Verdict | Where, and what the papers add |
|---|---|---|
| 1. Level 2 only; no interference between different-law universes | SIMPLIFYING ASSUMPTION, declared | Not addressed in the fourteen papers; Srednicki and Hartle 2010, App. A, warn that notions of location rest on classical spacetime. |
| 2. Everett, no fundamental collapse; records correlate observer state with outcome | STANDARD, with a wording caveat | Everett 1957, Secs. 3 and 5. Gell-Mann and Hartle accept "no collapse" (collapse is conditioning, 2018 Secs. III, IVe) but reject "all alternatives remain" phrased as many worlds: "one cannot assign 'reality' simultaneously to different alternatives" (2018 Sec. XIII). Zurek 2009 is interpretation-neutral and skeptical of the universal state's reality. The handoff is Everettian where two of its sources are not. |
| 3. No external selector or privileged consciousness; observers evolve as physical subsystems | STANDARD | Everett 1957 Sec. 5 (the observer as a machine with memory); Gell-Mann and Hartle 2018 Sec. XII (the IGUS, defined by what it does, not by consciousness); Zurek 2003 Sec. VI.2 (memory as an open register). |
| 4. No objectively advancing universal now; passage associated with ordered observer states and the arrow of records; cosmic time a model coordinate | Half STANDARD, half NOVEL | STANDARD: the arrow of time is an asymmetry between initial and final conditions of the decoherence functional, with "past" the end next to rho by convention (Gell-Mann and Hartle 1993 Sec. VIIc; 2018 Sec. IVd; Hartle 2020, finding (3) and conclusion); cosmic time as a fixed-background approximation (2018 Sec. IVa; Hartle 2020 Secs. III, VI). NOVEL relative to all fourteen: that *experienced* passage is associated with ordered observer states; none of the papers discusses experienced time ("arrow of records" is not Hartle's phrase). And Hartle's explanatory order is the reverse of the handoff's: the boundary asymmetry explains why records can exist; records do not explain the direction (Hartle 2020 p. 4: "arrows of time do not generally arise just from special initial conditions alone"; "the arrows arise by differences between initial and final conditions"). |
| 5. Amplitudes matter; probabilities only for a decoherent family | STANDARD | Gell-Mann and Hartle 2018 Secs. II to IV; 1993 Eq. 4.6 (weak decoherence, necessary and sufficient for the sum rules) and Eq. 4.8 (medium, sufficient); Sebens and Carroll 2018 Sec. 3 (why branch counting is not Born). |
| 6. Observers coexist and interact within histories; joint, not independent, probabilities | STANDARD in content, SIMPLIFYING in form | Gell-Mann and Hartle only ever use joint probabilities (2018 Eqs. 12, 18); Zurek's quantum Darwinism is the account of consensus from one redundant record (2009 Fig. 2; 2003 Sec. VII.3.1), but the papers never write P(R_A, R_B | alpha). Hartle and Srednicki 2007 refute independent factors for two observers directly ("the probability that one of us is human is obviously not independent of the status of the other"). |
| 7. Cosmic-time domain from the Big Bang to negligible observer support; a 99.99 % sterility threshold only if well defined | NOVEL as a program; its caveat is the papers' | Loeb et al. 2016 use the same domain (first stars to the longest stellar lifetimes, about 10^13 yr). Bousso, Freivogel and Yang 2008 Sec. V.E is the published reason a sterility time may not exist (late Boltzmann brains per physical volume make the comoving rate grow as a^3). |

### Handoff section 2, the key intuition

| Statement | Verdict | Where |
|---|---|---|
| The set of histories compatible with a retained record is nested and its measure nonincreasing | STANDARD; Everett's own Sec. 5 | Everett 1957 Eqs. 23 to 24 (the branching tree of memory sequences), Eqs. 33 to 34 (the measure of a sequence is a product of per-record factors, each at most one). In decoherent histories: "the records nest" (Gell-Mann and Hartle 1995, Eq. 3.15), and the probability of the past given present data (2018, Eq. 20). The handoff should cite these as the origin, under its own ninth check. |
| No global branch is destroyed by conditioning; the total measure is conserved | STANDARD | Everett 1957 Eq. 26 (additivity, which is also his derivation of the squared amplitude); Gell-Mann and Hartle 1995 Eq. 2.5 (the class operators sum to the identity). |
| Not a sequence of smaller infinities; a statement about nested subsets | STANDARD (plain measure theory) | No source needed; Everett's product measure makes it explicit. |
| A falling record measure does not by itself make early observer-moments more probable | STANDARD | Hartle and Srednicki 2007 Secs. IV and V; Srednicki and Hartle 2010 Sec. VI ("no prediction whatsoever" without a xerographic distribution). |

### Handoff section 3, the quantum foundation

| Formula or statement | Verdict | Where, and what the papers add |
|---|---|---|
| rho(t) = U rho_0 U^dagger | STANDARD | Schrodinger-picture form of Gell-Mann and Hartle's Heisenberg picture (2018 Eq. 3; 1995 Eq. 2.2). |
| C_alpha = P_{alpha_n}(t_n) ... P_{alpha_1}(t_1) | STANDARD in form, SIMPLIFYING in generality | 1993 Eq. 4.1; 1995 Eq. 2.3; 2018 Eq. 8. The general objects are branch-dependent chains (1993 Eq. 4.4; 1995 Eq. 2.1) and sums of chains; all three papers say realistic families are branch-dependent. Note: 2018 Sec. X carries a statement about branch dependence that 1993 footnote 3 withdrew; the 2018 re-posting says it was not updated. |
| D(alpha, beta) = Tr(C_alpha rho_0 C_beta^dagger) | STANDARD, with one silent assumption | 1993 Eq. 4.5; 2018 Eq. 8. It is the special case rho_F proportional to the identity of Hartle 2020's time-neutral functional (his Eq. 4.5 with 5.1). A one-boundary formalism is time-neutral only by taking a final condition of indifference, which the handoff should name as an assumption. |
| Negligible off-diagonal D, then p_alpha = D(alpha, alpha), sum about 1 | STANDARD, with a naming point | This is medium decoherence (1993 Eq. 4.8), sufficient not necessary; weak decoherence Re D = 0 (1993 Eq. 4.6) is what the sum rules need. Stage C tests medium decoherence and says so. |
| No unique preferred branch partition; no rigorous generic decomposition into complete classical histories | STANDARD, the papers' own | 2018 Sec. VI ("No such coarse graining is determined by pure quantum theory alone"), Sec. XIII; 1995 Sec. V; 1993 Sec. X. Set selection is an open question the authors pose themselves; Zurek 2003 Sec. VII.3 calls consistency "both not enough and too much". |
| C(R_n) = {alpha consistent with R_n} | STANDARD as a coarse graining; SIMPLIFYING in "consistent" | A record defines the coarser history that is the sum of the chains sharing it (1995 Eq. 2.4). But a record is correlated with the past only "with high probability" (2018 Sec. X), and an IGUS's memory is "assumed perfect; not always such a good approximation!" (2018 Sec. XII). The handoff's idealization of perfect records is declared in Stage B's model (perfect copies are the pi/2 case; partial records are run too). |
| C(R_{n+1}) subset of C(R_n), mu nonincreasing, "using a common decoherent history family" | STANDARD in substance; its precondition is the papers' main caveat | Nesting at the level of labels is trivial. That both sets still carry probabilities needs the extended family to remain decoherent, which is what strong-decoherence Conditions I and II (1995 Eqs. 3.9, 3.22) secure and which Dowker and Kent's final-condition examples show can fail (1995 footnote 2). Extending a family forward in time is a fine graining that "may no longer decohere" (1993 Sec. IVa). Stage C makes this exact: a kept record keeps the family decoherent; an erased one does not (test `test_an_erased_record_is_not_a_permanent_fact_about_the_past`). |
| mu(A) = sum of p_alpha over A | STANDARD | The additivity that decoherence buys (2018 Eq. 13). |
| I(R_n) = -log2 mu(C(R_n)), the record surprisal | FOUND outside the fourteen (prior-work note, claim A); within them a definition, not a result | Not in the fourteen papers. It is the Shannon self-information of the record alternative. The prior-work search found it defined, up to base and a constant, on nested record algebras as the "surprisal clock" of Martellini, arXiv:2607.25307 (July 2026; read in part through a page reader, to be read in full before it is cited); the normalized conditional measure is Hartle, gr-qc/9712001, Eq. 7; the measure of the set of worlds in which an observer with given memories exists is Vaidman's "measure of existence" (to verify against Vaidman 1998 and 2012). Nearest relatives inside the fourteen: the Jaynes entropy of a set of histories (2018 Sec. VII, Eqs. 31 to 32); the 1995 Sec. V entropy; algorithmic information content (Zurek 2003 Eqs. 7.3 to 7.4). No sentence of the form "we have not found" may be written about this quantity. |
| Erasure can lower I; redefining the family changes it | STANDARD caution | 1993 Sec. IVa; 1995 Sec. I; the generalized record (1995 Eq. 3.1) is "complete information somewhere in the universe" that need not be accessible, which is a different object from an IGUS's memory. The handoff conflates the two in places; Stage D keeps them apart (forgetting moves the record into the environment; the world keeps it). |
| V = \|<E_B\|E_A>\| | STANDARD for a balanced interferometer; "balanced" is SIMPLIFYING | Zurek 2003 Eqs. 4.11 to 4.12 (r(t) = <E_up\|E_down>); Zurek 2009 Eq. 5; in general V = 2\|a\|\|b\|\|r\| (ours; Stage B's `darwinism.visibility`). |
| Recombination and erasure possible; decoherence not an absolute ban; records emergent and approximate | STANDARD in principle | Zurek 2003 Sec. II.1.3 footnote 3 (recurrences) and Sec. VII.3.1 (conjugate-basis readout); Gell-Mann and Hartle 2018 Sec. XI (irreversibility as the cost of restoring phases); 2021 ("true in an approximation that need not be exactly defined"). The papers stress practical impossibility at scale; small toys recohere easily, which is a size artifact Stage B must not mistake for physics. |

### Handoff section 4, within-history observers

| Statement | Verdict | Where |
|---|---|---|
| Many observers in one history, correlated through shared environments; joint distributions, not products | STANDARD in content | Quantum Darwinism: the environment holds many copies, and "consensus" among observers who read different fragments (Zurek 2009 Fig. 2 caption; Zurek 2003 Secs. VII.1.1, VII.3.1; Zwolak and Zurek 2017 intro). Hartle and Srednicki 2007 Sec. IV on two authors. |
| Two observers reading one redundant error-free record report identical values | STANDARD | The Schmidt or branch structure (Zurek 2009 Eq. 6; 2003 Eq. 7.1). Nontrivial only for imperfect records (Zwolak and Zurek 2017 Eqs. 6 to 7, the error probability). Stage B and D compute the disagreement rate exactly. |
| Interactions change which records exist, the number of observer-moments, survival; model the whole history jointly | SIMPLIFYING ASSUMPTION / program | Not modeled in the papers beyond the IGUS as a coarse graining of one quasiclassical realm (2018 Sec. XII). |
| Quantum Darwinism as the framework for redundant records | STANDARD | Zurek 2009; Zwolak and Zurek 2017 (redundancy with irrelevant environment bits, Eqs. 11 to 15; two definitions of R_delta differ by ln(1/delta), so delta and the definition must be fixed, as Stage B does: R_delta = N / m_delta). |

### Handoff section 5, the cosmic-time measure

| Construction | Verdict | Where, and what the papers add |
|---|---|---|
| A finite comoving reference region | STANDARD | Loeb et al. 2016 Secs. 1, 2.1 and footnote 1 (one comoving Hubble volume, no multiverse measure); Bousso et al. 2008 Eq. 36. |
| n_obs as an observer-moment density generated from habitability, evolution, lifetimes and interactions, not planet counts | A refinement of FOUND work (prior-work note, claim C) | Loeb et al. compute habitable-planet-years (their Eq. 2.1 with a top-hat window); Bousso et al. leave f(tau) unspecified. Loeb et al. name the two refinements the handoff asks for and do not make them: life as a Poisson process in time, and re-weighting by the number of observers on a planet (their Sec. 4). The prior-work search found the cumulative fraction of observers by today computed at least four times under different rules: 68 (+14/-10) % of observers already emerged (Lineweaver and Egan 2007, astro-ph/0703429; the planet formation rate shifted by 4 Gyr, no lifetime weighting); 0.1 % at most (Loeb et al. 2016); Earth earlier than at least 92 % of Earth-like planets (Behroozi and Peeples 2015, arXiv:1508.01202); below 1 % among advanced-life origin dates when planet lifetimes beyond a trillion years are allowed (Hanson et al. 2021, arXiv:2102.01522, with a preemption interaction). That spread, 0.1 % to 68 % from the reference class and the lifetime assumptions, is already the sensitivity result the handoff plans. What Stage E adds is only several classes and knobs in one model. |
| W(t) = sum_alpha p_alpha integral of n_obs | SIMPLIFYING ASSUMPTION on a STANDARD object | The form is Sebens and Carroll 2018 Eq. 42 (Born weight times observer count, with its divergence condition). Within one history it is Bousso et al. Eq. 36. Neither sums over branches with different observer populations. |
| p(t \| sampled observer-moment) = W / integral of W | SIMPLIFYING ASSUMPTION, correctly declared | A uniform-on-a-class self-location rule (Srednicki and Hartle 2010 Sec. III: "it is also possible to assume that we are atypical"). Cirkovic and Balbi 2020 argue typicality in time is not well defined without a restricting context. |
| F(t_0), the share at or before today | STANDARD construction; the handoff's normalization is one of two | Loeb et al. compute P(< t) (Fig. 4, bottom) and give about 0.1 % for 0.08 to 3 solar masses, near unity for ranges narrow around a solar mass (read from a log plot, to verify). **Two normalizations exist and differ:** the handoff's pooled form (sum over histories of p_alpha N_alpha(<= t_0), over the pooled total) is Sebens and Carroll's Eq. 39/42; Srednicki and Hartle's xerographic recipe normalizes within each history and then averages with the third-person probabilities (their Eqs. B3 to B4). They agree only if every history holds the same total of observer-moments. Stage E computes both (`cosmic.pooled_and_averaged_F`). |
| "A uniformly sampled observer-moment is a proposed self-location distribution, not an automatic consequence" | STANDARD, and the papers' own warning | Srednicki and Hartle 2010 Sec. III; Hartle and Srednicki 2007 Eq. 4.2 (the selection fallacy): today's percentile may be reported under a declared rule, never used as evidence for a measure unless the typicality assumption sits in a declared prior and is competed. |
| T_support, F_sterile, t_99.99 | Modeling devices not in the fourteen papers; no search note backs a "not found" for them | Anchors: Loeb et al. ("expected to vanish beyond" about 10^13 yr; the exp(-t/50 Gyr) cutoff); Bousso et al. Sec. V.E for why a cutoff may not exist; Hanson et al. 2021 use a maximum planet lifetime as the same kind of cutoff. |
| The five core scenarios | STANDARD ingredients except one | Baseline and red-dwarf-friendly are Loeb et al.'s own (their headline is the friendly case); red-dwarf-suppressed is their m_min knob with the physics in Lingam and Loeb 2018 and Kipping 2025 (abstracts only); the interactions scenario is NOVEL and speculative; the late-time stress test is Bousso et al.'s caution (Secs. I.B, V.E). |
| Proper time along worldlines in r_i | SIMPLIFYING ASSUMPTION | Flagged by Bousso et al. Sec. III.A (FRW proper time against a congruence time). |

### Handoff section 6, the methodological checks

All but two are the papers' own: do not count worlds (Gell-Mann and Hartle 2018 Secs. III, XIII; Sebens and Carroll 2018
Sec. 3, with the caution that their own derivation counts equal-amplitude components after an environment unitary, so
the check should read "do not count decoherence-defined branches"); do not multiply correlated observer probabilities
(Hartle and Srednicki 2007 Sec. IV); one history's falling measure is not the total's (1995 Eq. 2.5); no early-time
typicality from nesting (Hartle and Srednicki 2007 Secs. IV to V); no permanent classical histories in generic systems
(1995 abstract and footnote 2; Kent 2014 Sec. 1); no consciousness from a qubit (2018 Sec. XII; Zurek 2003 Sec.
VII.2); no common foliation in exact GR (2018 Sec. IVa; Srednicki and Hartle 2010 App. A). The two that are not in the
papers: "entropy and record surprisal are not equivalent" (the distinction is 1995 Sec. V's; the quantity is the
handoff's), and the ninth check, which this document carries out.

## 3. What the papers say that the handoff does not

1. **The arrow of time is an asymmetry between two boundary conditions, not a consequence of records.** Hartle 2020:
   "arrows of time do not generally arise just from special initial conditions alone as has sometimes been
   suggested"; a one-boundary formalism silently assumes a final condition of indifference. The handoff's research
   question ("apparently directional histories inside a time-neutral, unitary quantum universe") is standard only once
   rho_F is named. In the toy this appears as: records form from blank registers and un-form when the circuit is run
   backwards; a register that is not in a low-entropy state cannot hold a record (Stage D tests).
2. **Decoherent histories is not Everett.** Two of the handoff's seven priority sources would decline its commitment 2
   as worded. The program can be Everettian; its sources should be cited for what they say.
3. **The generalized record is not the observer's memory.** The nesting theorem (1995 Eq. 3.15) is about the first;
   the erasure remarks are about the second.
4. **Medium decoherence is sufficient, not necessary.** A family can obey every sum rule with Re D = 0 and nonzero
   imaginary off-diagonal terms. Stage C reports the maximum |D| off the diagonal and the sum-rule violations
   separately, so that the two conditions can be told apart.
5. **Loeb et al. already give the number.** F(t_0) about 10^-3 for the full stellar range, as cumulative habitable-
   planet-years; and their first author's later paper (Lingam and Loeb 2018) reverses the headline under the
   red-dwarf-suppressed physics. Behroozi and Peeples 2015 imply a planet-count cumulative fraction of order 0.07
   (ours, from their abstract). Haqq-Misra, Kopparapu and Wolf 2018 recast the question as a reference-class choice,
   which is the handoff's own point.
6. **Bousso et al.'s youngness paradox does not transfer** to a single fixed background with a finite comoving region:
   its exp(-3 H tau) factor comes from the exponentially growing count of bubbles under a global proper-time cutoff
   (their Eqs. 35 to 40). In one bubble their Eq. 36 reduces to the handoff's W, and their Sec. V.E is the warning that
   remains: late observers per physical volume make the comoving integral diverge ("a poisoned chalice").
7. **Sebens and Carroll's Two-Branch-Beauty**: within-branch duplication changes first-person credence (2/3) without
   changing Born weight (1/2). The handoff's W(t) is that rule applied to observer-moments and should say so; Stage D's
   duplication test is its toy form.
8. **Kent's objections to Sebens and Carroll** (arXiv:1408.1944, read in full by the agent): no principled ontology of
   "copies"; branch count is the modeler's choice; recoherence. These transfer to Stage B and D: results should be
   reported under more than one system-environment split.

## 4. Where the handoff is weaker than it reads (ours)

- The sentence in Stage C, "demonstrate that the sum of exhaustive history weights stays one, even as one record's
  compatible set shrinks", is true of every family, decoherent or not, because the class operators sum to the full
  evolution; it is therefore not a test of anything. The two-slit family has total weight exactly one and still
  interferes (its off-diagonal terms cancel in pairs). The test of a family is its sum rules, one per coarse graining
  (Stage C computes them).
- "Persistent observer records explain the apparent direction and continuity of experienced time" reverses Hartle's
  explanatory order and adds "experienced", which none of the sources addresses. What the toy can show is narrower:
  that in a unitary world records accumulate in one direction because the registers start blank, and that a chain of
  kept records is consistent along a branch; nothing about experience follows.
- F(t_0) under a uniform-over-observer-moments rule is Loeb et al.'s calculation with a different weight; the number
  itself cannot be evidence for or against anything (Hartle and Srednicki 2007 Eq. 4.2).
- The handoff's success criterion 5 asks whether anything is a new prediction. As of Stage A the answer is no: the
  quantum stages are consistent restatements, and the cosmic stage is a parameterized population model whose outputs
  depend on declared, unmeasured knobs (delay, observer lifetime, reference class, interactions). A falsifiable
  consequence would need an observable that the knobs do not absorb; none has been found in this reading.

## 5. The physics limitations the papers themselves state, carried into the program

A fixed classical background with a preferred time (2018 Sec. IVa; Hartle 2020 throughout, with the quantum-gravity
case "remain[ing] to be carried out"); a pure initial state for the record theorems (1995 Sec. I); probabilities
approximate "to the accuracy to which they are used" (2018 Sec. II); a finite environment is eventually exhausted so
that record states stop being orthogonal (1993 footnote 7), which Stage B's small environments show directly; set
selection open; the cosmological inputs valid only for life as we know it in Lambda-CDM with a fixed IMF, no
metallicity dependence and a constant eta_Earth (Loeb et al. Secs. 2.2 to 2.7).
