# Prior-work search: the three "might be new" proposals of the observer-relative-histories handoff

CLAUDE.md rule 15. Written before any write-up says "we have not found" about any of the three claims below. `date`
was run before the date was written (Mon Oct 12 07:49 EDT 2026).

**The sentences it backs** (candidates from `docs/theory/observer_relative_histories_research_handoff.md`, 12 October
2026; none has yet appeared in a write-up):

- **Claim A** (handoff Secs. 2 and 3): for an observer with a retained record sequence R_n, the set of decoherent
  histories compatible with the record is nested and its Born measure is nonincreasing, the normalized conditional
  measure sums to one, and the record surprisal I(R_n) = −log₂ μ(C(R_n)) quantifies the specificity of what has been
  recorded.
- **Claim B** (Sec. 4): interacting observers within a history must be modeled with joint distributions over their
  records, not products; two observers reading one redundant error-free record have perfectly correlated reports.
- **Claim C** (Sec. 5): the distribution of observer-moments over cosmic time W(t), built from habitability,
  evolutionary delay, observer lifetime and interactions in a fixed FLRW background with a finite comoving region, and
  the cumulative fraction F(13.8 Gyr) under declared reference classes.

**Date of the search:** 2026-10-12.

**Who searched:** an assistant agent (fresh session, read-only on the repository, no history from the handoff's
writing). The owner has read none of the sources below. Every "read in part" below means read through a page-reader
tool that paraphrases; quotations are to be checked against the source before any of them is cited. Journal volumes
and pages marked "to verify" come from the agent's general knowledge, not from the fetched pages.

## Where was searched

Common to all three claims. Google Scholar could not be reached from this session; Semantic Scholar's citation graph
was used instead for forward citations. The INSPIRE "refersto" query returned 49 unrelated records for one relevant
one, so its result is recorded as unreliable. The arXiv API searches abstracts, not full text. NASA ADS was not used
(needs a token).

| Source | Terms used | Results looked at | Nearest hit |
|---|---|---|---|
| arXiv API (abstracts) | `"observer moments" OR "observer-moments"`; `surprisal AND ("decoherent histories" OR "consistent histories" OR records OR "many worlds" OR Everett)`; `ti:"red sky paradox"` | 34 + 47 (of 147) + 1 | A: arXiv:2607.25307 (Martellini); C: arXiv:2106.11207 (Kipping) |
| Web search, extended mode (26 queries) | A: decoherent histories + records + conditional probability; Vaidman "measure of existence"; Page "Sensible Quantum Mechanics"; surprisal + quantum history + record; Everett memory sequence; Zurek existential interpretation; Greaves–Myrvold, Wallace; IGUS records. B: quantum Darwinism + observers + agreement; Frauchiger–Renner + consistent histories; Everett several observers; Wigner's friend + records. C: observer-moments + cosmic time; Loeb 2016 follow-ups; Bostrom SSSA; Olson civilizations; Sandora, Ćirković; Gott 1993; "fraction of observers" + cosmic time | about 190 result links; 31 abstract pages and 9 full texts fetched | A: Martellini 2026; B: Everett 1957 (full text searched); C: Lineweaver & Egan 2007 (full text searched), Loeb et al. 2016 (full text searched) |
| Google Scholar | not reachable | — | — |
| INSPIRE-HEP | `refersto:arxiv:1606.08448` | 50 records, 49 unrelated (noise) | 1606.08926 (Loeb's review chapter) |
| Forward citations (Semantic Scholar) | citations of arXiv:1606.08448 (Loeb et al. 2016); of arXiv:astro-ph/0703429 (Lineweaver & Egan 2007) | 65 and 21 titles; 14 flagged by title, 6 of them then fetched | C: 2102.01522 (Hanson et al.), 1907.08947 (Ćirković & Balbi), 1705.07813 (Haqq-Misra et al.), 2510.01215 (Kipping) |
| The closest sources' own reference lists | Martellini's refs 9–12 (consistent/decoherent histories) seen in passing; Lineweaver & Egan's and Hanson et al.'s lists not walked | — | — |
| `REFERENCES.bib` and earlier notes in this folder | keys Saunders21, Rovelli96, Zurek05, Freivogel11, BHKP07, Bostrom11; `2026-10-05_loops_and_comparing_infinities.md` | 6 entries, 1 note | none of the three claims; the note covers the measure problem only. No near miss below is in the bib |

## What came closest

### Claim A: nested compatible histories, nonincreasing measure, record surprisal

- **Martellini, "The Emergence of Time from Quantum Records: Actualization and the Surprisal Clock", arXiv:2607.25307
  (v1 July 2026, v3 September 2026).** *Abstract and about 90 % of the HTML full text read in part by the page reader;
  the last 11,000 characters not read.* Defines, for a recorded sequence h_n = (r₁, …, r_n), an accumulated clock
  reading τ_A(h_n) = −σ ln P(h_n) (its Eq. 13), with P(h_n) the joint Born probability of the recorded sequence, the
  chain rule P(h_n) = Π_k p(r_k | h_{k−1}) giving the telescoping sum of conditional surprisals, and nested record
  algebras Σ₀ ⊆ Σ₁ ⊆ ⋯ (its Assumption II.1). **This is the handoff's I(R_n) up to the base of the logarithm and a
  constant**, because the Born measure of the set of fine-grained decoherent histories compatible with a record equals
  the joint probability of the record (additivity of decoherent probabilities). Differences: it works with sequential
  projective records and instruments, not class operators and a decoherence functional (it cites the histories
  formulations as related work); it does not state the compatible set's measure as nonincreasing or total probability
  as one (both are implicit); observers, memory and self-location appear only in passing; and it reads the surprisal as
  internal time, not as record specificity. No forward citations were checked (too new).
- **Vaidman, "Many-Worlds Interpretation of Quantum Mechanics", Stanford Encyclopedia of Philosophy.** *Read in part
  by the page reader (first 100,000 characters).* The measure of existence of world i is μ_i = |α_i|²; an observer "also
  possesses a measure of existence, which is the sum of the measures of existence across all the different worlds in
  which I exist", with "I" fixed by a classical description of body and brain, memories included; the Born–Vaidman rule
  is a postulate for self-location. **Answer to the brief's question: yes, the observer's measure of existence is the
  handoff's μ(C(R_n)) in substance**, once a present world is identified with the bundle of histories that end in it
  and the observer is identified by its records. It is not formed into a nested sequence over a record history, no
  surprisal is taken, and the worlds are defined by macroscopic states rather than by a decoherent family. To verify
  against Vaidman's own papers (1998 and 2012, cited in the entry; not read).
- **Hartle, "Quantum Pasts and the Utility of History", arXiv:gr-qc/9712001, Phys. Scripta T76, 67 (1998).** *Full
  text read in part by the page reader.* Eq. 7 is the handoff's normalized conditional measure: p(past history |
  present data) = p(past history and present data) / p(present data). His information measures are the algorithmic
  information content of a history and a missing-information entropy of a set of alternatives, neither of which is
  −log p of a record. Sec. III.3, "A Past is Not Necessarily Permanent": a fine graining of a decoherent set need not
  decohere, so retrodictions can be lost as data grows, which is the handoff's "it need not increase if ... the history
  family is redefined" caveat, published.
- **Gell-Mann and Hartle, "Quantum Mechanics in the Light of Quantum Cosmology", arXiv:1803.04605 (the 1990
  proceedings paper).** *Abstract only here; it is item 2 of the handoff's own reading list.* Observers as IGUSes that
  use probabilities for histories conditioned on their present records (Gell-Mann's lecture slides, read in part:
  "compute probabilities on the basis of present data, make predictions ... acquire further data"). The conditioning
  mechanics are not in the abstract; to read before any citation.
- **Everett, "Relative State" Formulation of Quantum Mechanics, Rev. Mod. Phys. 29, 454 (1957).** *Full text
  downloaded and searched by sentence.* "The 'trajectory' of the memory configuration of an observer performing a
  sequence of measurements is thus not a linear sequence of memory configurations, but a branching tree" (note added in
  proof); "In order to establish quantitative results, we must put some sort of measure (weighting) on the elements of
  a final superposition." The nesting of record-compatible sets is this tree read from a leaf; he does not form the
  measure of the leaf's ancestry into a sequence or a surprisal.
- **Page, "Sensible Quantum Mechanics: Are Only Perceptions Probabilistic?", arXiv:quant-ph/9506010, and "Are
  Probabilities only in the Mind?", gr-qc/9507024; "Consciousness and the Quantum", 1102.5339.** *Abstracts only.* A
  measure on perceptions (Bostrom's observer-moments) as the expectation value of an awareness operator, m(p) =
  Tr[E(p)ρ]. The ancestor of Born-weighted observer-moment counting; not a record-compatible set and not a surprisal.
- **Strasberg, Schindler, Wang, Winter, "Approximate Decoherence, Recoherence and Records in Isolated Quantum
  Systems", arXiv:2601.19703 (January 2026).** *Abstract only.* The number of reliable records can be far smaller than
  the number of events; self-location treated as coherent state discrimination; a "branch selection problem" for
  internal observers. Bears on the handoff's Sec. 3 caveats (records are approximate), not on the surprisal.
- **Greaves and Myrvold, "Everett and Evidence" (in *Many Worlds?*, Saunders, Barrett, Kent, Wallace eds., OUP 2010;
  general knowledge, to verify); Wallace, *The Emergent Multiverse* (OUP 2012).** *Not read; search summaries only.*
  Conditionalizing on observed outcome sequences updates credence in branch weights; records as such are not treated.
- **Aguirre and Tegmark, "Born in an Infinite Universe", arXiv:1008.1066, Phys. Rev. D 84, 105002 (2011).**
  *Abstract only.* Born probabilities as frequencies among copies of an observer in an infinite space; no records or
  memories in the abstract.
- **Riedel, Zurek, Zwolak, "The Objective Past of a Quantum Universe: Redundant Records of Consistent Histories",
  arXiv:1312.0331, Phys. Rev. A 93, 032126 (2016);** **Strasberg, "Redundant Records of the Past", arXiv:2610.09845
  (7 October 2026).** *Abstracts only.* Which histories leave redundant records; the selection of a quasiclassical past
  by records. Supply the "records" of Claim A and the "redundant record" of Claim B; no measure of a record-compatible
  set is taken.

### Claim B: joint, not product, distributions over observers' records; perfectly correlated readings of one record

- **Everett 1957 (as above), Sec. 5, the paragraph on several observers.** *Full text searched.* "When several
  observers have separately observed the same quantity in the object system and then communicated the results to one
  another they find that they are in agreement." "This agreement persists even when an observer performs his
  observation after the result has been communicated to him by another observer who has performed the observation."
  The state he writes down, Σ_i φ_i ψ^{O1}[α_i] ψ^{O2}[α_i], is the handoff's Stage D case: in every element both
  records carry the same result, so P(A records 0, B records 1) = 0 although both outcomes occur across elements.
  **The handoff's example is Everett's 1957 calculation.** Its closing sentence names "the interrelationship of several
  observers" as a subject the formalism treats. (The SEP entry "Everettian Quantum Mechanics", Sec. 5.1, read in part:
  a record "that agrees with the records of other ideal observers".)
- **Zurek, "Quantum Darwinism", Nature Physics 5, 181 (2009) (item 4 of the handoff's list; general knowledge, to
  verify the pages).** *Not read here; search summaries.* Redundant environmental records let many observers find out
  the state independently and agree. The handoff already names it as the framework to study.
- **Riedel, Zurek, Zwolak 2016 (as above).** *Abstract only.* Observers who reconstruct the past from redundant records
  "arrive at compatible conclusions in the present."
- **Brukner, "A no-go theorem for observer-independent facts", arXiv:1804.00749, Entropy 20, 350 (2018); Frauchiger
  and Renner, "Quantum theory cannot consistently describe the use of itself", arXiv:1604.07422, Nat. Commun. 9, 3711
  (2018); Bong et al., "A strong no-go theorem on the Wigner's friend paradox", arXiv:1907.05607, Nat. Phys. 16, 1199
  (2020).** *Abstracts only.* These are about exactly the question of Claim B: whether one joint distribution over all
  observers' recorded facts exists. Bong et al. name the assumption "Absoluteness of Observed Events" and show that it,
  Locality and No-Superdeterminism cannot all hold if an observer can be coherently manipulated. **Consequence for the
  handoff** (*ours, unverified*): "model observers jointly within a history" is the Everettian reading these papers
  leave open (observed events are relative to a branch), but the joint distribution exists only within a decoherent
  family; where a friend is coherently reversed, no family contains all the records at once. Claim B therefore needs
  the qualification "within one decoherent family", which the handoff's Sec. 3 already supplies in general terms.
- **Losada, Laura, Lombardi, "Frauchiger–Renner argument and quantum histories", arXiv:1907.10095, Phys. Rev. A 100,
  052114 (2019).** *Abstract only.* In consistent histories the Frauchiger–Renner contradiction needs a family that
  violates the consistency condition; the records of the four agents cannot all be assigned in one valid family. The
  histories-language form of the previous bullet.
- **Waaijer and van Neerven, "Relational analysis of the Frauchiger–Renner paradox and interaction-free detection of
  records from the past", arXiv:1902.07139, Found. Phys. (2021; volume to verify).** *Search summary only.* The paradox
  disappears if one agent's certainty is not promoted to another's unless records from the past validate it.
- **Steane, "The extended Wigner's friend, many- and single-worlds and reasoning from observation", arXiv:2605.08375
  (May 2026).** *Abstract only.* Reasoning from observations must allow for their possible quantum erasure; permanent
  records are what make a record-based inference valid. The handoff's "decoherence is not a literal absolute ban on
  recombination" caveat, in print this year.
- **Fields, "Quantum Darwinism requires an extra-theoretical assumption of encoding redundancy", arXiv:1003.5136, Int.
  J. Theor. Phys. 49, 2523 (2010).** *Abstract only.* Observers cannot verify the redundancy without disturbing it; a
  limit on what quantum Darwinism can deliver to Claim B.

### Claim C: observer-moments over cosmic time and the cumulative fraction by today

- **Lineweaver and Egan, "The Cosmic Coincidence as a Temporal Selection Effect Produced by the Age Distribution of
  Terrestrial Planets in the Universe", arXiv:astro-ph/0703429, ApJ (2007; DOI 10.1086/522197; volume and page to
  verify).** *Full text read in part by the page reader.* The observer distribution is the terrestrial planet
  formation rate shifted by an evolution delay, P_obs(t) = PFR(t − Δt_obs), Δt_obs = 4 Gyr nominal, normalized from 0
  to ∞ with the formation rate "smoothly extrapolated" into the future; no observer lifetime term; per unit comoving
  volume. **It computes the handoff's F(t₀): "68% emerge earlier while 32% emerge later", 68 (+14/−10) %**, and
  concludes "most terrestrial-planet-bound observers will emerge earlier than we have." Its headline (about 68 % of
  observers find Ω_m at least as close to Ω_Λ as we do) is built on this distribution. The handoff's W(t) adds
  observer lifetime, interactions, a finite comoving region and a sterility cutoff; the cumulative fraction under a
  declared rule is already here, with its error bar.
- **Loeb, Batista, Sloan, "Relative Likelihood for Life as a Function of Cosmic Time", arXiv:1606.08448, JCAP 08
  (2016) 040 (item 7 of the handoff's list).** *Full text read in part by the page reader.* dP/dt is a normalized double
  integral over formation time and stellar mass of the IMF × star formation rate × η_Earth × a constant probability of
  life × a window equal to 1 while the star lives, in a fixed comoving volume with a fixed number of baryons, from the
  first stars (about 30 Myr) to about 10 Tyr; metallicity checked and dropped; several reference classes compared
  (minimum stellar mass from 0.08 to 3 M☉; two truncation times). **It gives a cumulative number: "the most conservative
  estimate put the probability of our existence before the current cosmic time at 0.1% at most"**, and "puts the
  probability of finding ourselves at the current cosmic time within the 0.1% level" when stars down to 0.08 M☉ count;
  with narrow solar-mass ranges "the current time indeed represents the peak". Weighting by number of observers is
  discussed as a refinement that would push the peak later, and not computed.
- **Behroozi and Peeples, "On the History and Future of Cosmic Planet Formation", arXiv:1508.01202, MNRAS (2015; DOI
  10.1093/mnras/stv1817; volume to verify).** *Full text read in part by the page reader.* Earth "formed earlier than
  ∼61% of all planets that will ever form" in the Local Group and "earlier than at least 92% of other similar planets"
  in the Universe; f = 0.92 is "the fraction of planets which have yet to form". A cumulative fraction by Earth's
  formation under the planet reference class, with no delay or lifetime.
- **Hanson, Martin, McCarter, Paulson, "If Loud Aliens Explain Human Earliness, Quiet Aliens Are Also Rare",
  arXiv:2102.01522, ApJ (2021; DOI 10.3847/1538-4357/ac2369; volume to verify).** *Full text read in part by the page
  reader (first 100,000 characters).* Origin-date density α(t) = q ∫ (t − b)^{n−1} ϱ(b) [H(L̄) − H(t − b)] db over
  star birth dates b, with n hard steps, a habitable star formation rate peaking near 12 Gyr and a planet-lifetime
  distribution H. The percentile of today "is always below 1%" for maximum lifetimes beyond a trillion years; the
  abstract has >99.99 % of advanced life appearing after today unless n < 3 and L̄ < 50 Gyr; "we seem early." The
  "loud" civilizations preempt later life, a within-history interaction, but as a rule of the grabby model rather than
  a term in the appearance integral; origin dates only, no observer lifetime or observer-moment weighting.
- **Haqq-Misra, Kopparapu, Wolf, "Why do we find ourselves around a yellow star instead of a red star?",
  arXiv:1705.07813, Int. J. Astrobiology (2018; DOI 10.1017/S1473550417000118; volume to verify).** *Full text read by
  sentence search.* Reference class "all observers that actually exist in the past, present, or future"; Sec. 6.1
  weights by main-sequence lifetime (10¹⁰, 10¹¹, 10¹³ yr for G, K, M); Conclusion C3: "over a hundred times greater
  likelihood of existing around an M-dwarf star in the future" if all three host observers alike. Likelihood ratios
  across star types and eras, not F(t₀); it names the self-sampling assumption over "the entire past, present, and
  future of the universe".
- **Kipping, "Formulation and Resolutions of the Red Sky Paradox", arXiv:2106.11207, PNAS 118, e2026808118 (2021);
  "Solar Hegemony", arXiv:2510.01215 (2025).** *Abstracts only.* Bayesian odds of finding oneself around an FGK star
  with a truncated observer window T_win and a critical stellar mass; "the first 0.1%" of the roughly 10 Tyr
  stelliferous period is elapsed time, not an observer fraction.
- **Bousso, Hall, Nomura, "Multiverse Understanding of Cosmological Coincidences", arXiv:0902.2263, Phys. Rev. D 80,
  063510 (2009).** *Full text read in part by the page reader (first 100,000 characters).* The time of observation
  t_obs is a scanned parameter with a prior f ∝ t_obs^p and the suppression exp(−3t/t_Λ) after vacuum domination;
  predicts t_obs near 11.0 Gyr against the observed 10.1 Gyr. A distribution over t_obs across a multiverse, not a
  within-universe W(t). The causal entropic principle of [BHKP07] (abstract only, in the bib) weights by entropy
  production over a causal diamond's history, which is a time-weighting of observers by proxy.
- **Ćirković and Balbi, "Copernicanism and the Typicality in Time", arXiv:1907.08947, Int. J. Astrobiology 19, 101
  (2020).** *Full text read in part by the page reader.* "Typicality in time is not – and cannot ever be –
  well-defined": the time average needs a limit t → t_max that may not exist, the future is not like the past, and no
  cosmological principle grounds it; Gott's and the Doomsday arguments are its prototypes. Advice: "refrain from
  assuming our typicality in this respect", or restrict the context (the Solar lifetime; the stelliferous era). This is
  the published objection the handoff's F(t₀) has to answer; the handoff's own caveat (a uniformly sampled
  observer-moment is a proposed distribution, not a consequence) is the same point in its words.
- **Olson, "Homogeneous cosmology with aggressively expanding civilizations", arXiv:1411.4359, Class. Quantum Grav.
  (2015; volume to verify); "On the Likelihood of Observing Extragalactic Civilizations: Predictions from the
  Self-Indication Assumption", arXiv:2002.08194 (2020).** *Search summaries and abstract.* An appearance rate f(t) per
  comoving volume per Gyr from a fitted star formation history, cumulative metallicity, a 4.5 Gyr delay and a 6 Gyr
  habitable window: the inputs of the handoff's W(t) for civilizations rather than observer-moments, used for expansion
  and visibility rather than for F(t₀).
- **Balbi, "The Impact of the Temporal Distribution of Communicating Civilizations on their Detectability",
  arXiv:1708.07433, Astrobiology (2018).** *Abstract only.* Appearance epochs and lifespans of civilizations as a
  statistical model within the Galaxy.
- **Dayal, Ward, Cockell, "The habitability of the Universe through 13 billion years of cosmic time",
  arXiv:1606.09224 (2016).** *Abstract only.* Habitability against cosmic time from supernovae, GRBs and AGN; "2.5 to
  20 times more habitable today" than 4 Gyr ago; no observer count and no cumulative fraction. Dayal et al. 2015 on
  galaxy habitability not read.
- **Zackrisson et al., "Terrestrial planets across space and time", arXiv:1602.00690, ApJ 833, 214 (2016).**
  *Abstract only.* Mean ages of terrestrial planets 7 ± 1 Gyr (FGK) and 8 ± 1 Gyr (M dwarfs) in the local Universe; no
  observer fraction.
- **Sorini, Peacock, Lombriser, "The impact of the cosmological constant on past and future star formation",
  arXiv:2411.07301, MNRAS (2024).** *Abstract only.* Observers proportional to the asymptotic star formation
  efficiency; P(Λ ≤ Λ_obs) = 0.5 %. Whole-history weighting, not a time distribution within our universe.
- **The anchors the brief asked for.** Olum, "Conflict between anthropic reasoning and observation", arXiv:gr-qc/0303070,
  Analysis 64, 1 (2004): typicality among all observers predicts large civilizations, not a time distribution (abstract
  only). Neal, "Puzzles of Anthropic Reasoning Resolved Using Full Non-indexical Conditioning", arXiv:math/0608592
  (2006): condition on everything, memories included; no cosmic-time distribution (abstract only). Garriga and
  Vilenkin, "Prediction and explanation in the multiverse", arXiv:0711.2559, Phys. Rev. D 77, 043526 (2008): the
  reference class as all observers with identical information; no time weighting (abstract only). Gott, "Implications
  of the Copernican principle for our future prospects", Nature 363, 315 (1993): the observation moment as a uniform
  random point in a process's duration (Nature page read; the 95 % rule t/39 to 39t is general knowledge, to verify).
  Bostrom, *Anthropic Bias* (Routledge 2002): the strong self-sampling assumption with observer-moments as the unit
  (secondary sources only; the handoff's unit is his). **Hartle and Hertog: the id given in the brief, arXiv:1309.0498,
  resolves to an unrelated operator-algebra paper; the correct id is to verify and the paper was not read.**

## Verdict

**Claim A: FOUND.** The quantity I(R_n) = −log₂ μ(C(R_n)) is Martellini's accumulated clock τ_A(h_n) = −σ ln P(h_n)
(July 2026) up to base and constant, defined on nested record algebras; the normalized conditional measure is Hartle's
Eq. 7 (1998) and the IGUS program of Gell-Mann and Hartle; the measure of the record-compatible set is Vaidman's
measure of existence of an observer; the nesting is Everett's branching memory tree, and "nonincreasing" is the
additivity of a measure, not a result. What is not found stated anywhere is the combination of the four sentences
inside a decoherent-histories family with the surprisal read as record specificity; that is a framing, and no sentence
of the form "we have not found" should be written about the quantity. Before anything cites Martellini, read it in
full (only the first 100,000 characters were read, by a page reader) and check that his record filtration is the
handoff's C(R_n) when the records are coarse-grained alternatives of one decoherent family.

**Claim B: FOUND.** Everett 1957, Sec. 5, derives the perfect correlation of several observers' records of one system
and their agreement on communication, from the joint state and with no independence assumed; quantum Darwinism and
Riedel–Zurek–Zwolak 2016 supply the redundant record; the Wigner's-friend no-go theorems (Brukner 2018; Frauchiger and
Renner 2018; Bong et al. 2020) and Losada et al. 2019 are the published statement of when a joint distribution over
observers' records exists (within one consistent family) and when it does not. The handoff's Stage D case is Everett's
calculation.

**Claim C: FOUND.** A cumulative fraction of observers or life by today under a declared sampling rule has been
computed at least four times, with different rules and very different numbers: **68 (+14/−10) %** of
terrestrial-planet-bound observers have already emerged (Lineweaver and Egan 2007; planet formation rate shifted by
4 Gyr, no lifetime weighting, integrated to infinity); **0.1 % at most** for life before the current time when stars
down to 0.08 M☉ count (Loeb, Batista and Sloan 2016; fixed comoving volume, 30 Myr to 10 Tyr, several mass cutoffs
compared, and at the peak for solar-mass-only classes); Earth earlier than **at least 92 %** of Earth-like planets ever
to form (Behroozi and Peeples 2015); today's percentile among advanced-life origin dates **below 1 %** for maximum
planet lifetimes beyond a trillion years (Hanson et al. 2021, with a preemption interaction). The spread, 0.1 % to
68 % from the choice of reference class and lifetime assumptions, is already the handoff's planned "sensitivity to
assumptions" result. Ćirković and Balbi 2020 argue that no such fraction can be well-defined. What the handoff would
add is a single model with observer-moments as the unit (Bostrom's), an observer lifetime r_i (Haqq-Misra et al. and
Kipping weight by stellar lifetime and a truncated window, not by observer duration), explicit interactions as a term
rather than a rule, a finite comoving region and a sterility time t_99.99, with several reference classes side by
side. If a narrower sentence is ever wanted ("we have not found a single model that ... under several reference
classes in one place"), it needs its own search note; this one does not back it.

**What would change the verdicts.** None of the three can return to NOT FOUND: the near misses are published and
several were read in full text. Reading Martellini 2026, Vaidman 1998 and 2012, and Page 1995 in full could sharpen
Claim A's differences (instruments against decoherent families; present worlds against histories) without restoring
novelty to the quantity. For Claim C, walking Lineweaver and Egan's and Hanson et al.'s reference lists, and reading
Bostrom 2002 for any cosmic-time application of the strong self-sampling assumption, would show whether the
observer-moment refinement has also been done; that search was not run and no sentence about it should be written
until it is.
