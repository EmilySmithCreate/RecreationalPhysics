# Reading note: the Causal Entropic Principle and the cosmological constant

Written 19 October 2026 by a fresh assistant reader (Claude), for the owner. Every statement below is marked either
**the paper says** (with a section, equation or figure number) or **ours**. Where a detail could not be found in the
text it says "to verify". Nothing here has been checked by a physicist.

## 1. Bibliography and read status

- **[BHKP07]** R. Bousso, R. Harnik, G. D. Kribs and G. Perez, "Predicting the Cosmological Constant from the Causal
  Entropic Principle", Phys. Rev. D 76, 043513 (2007); arXiv:hep-th/0702115. Versions on arXiv: v1 15 Feb 2007, v2
  16 Apr 2007, v3 15 Sep 2007 (the current one). **Read in full on 19 October 2026** from the ar5iv HTML rendering
  (https://ar5iv.labs.arxiv.org/html/hep-th/0702115), downloaded and converted to text, then read section by section
  from the abstract through Appendix A; the reference list was read as far as it bears on this note. ar5iv renders the
  latest arXiv version, so this should be v3 (to verify: the rendering does not print its version number). The PDF was
  not separately read. Figures were read through their captions only; the curves themselves were not seen.
- **[Bousso06]** R. Bousso, "Holographic probabilities in eternal inflation", Phys. Rev. Lett. 97, 191302 (2006);
  arXiv:hep-th/0605263 (v4, 21 Feb 2007). **Abstract only**, read from the arXiv abstract page. The abstract says that
  probabilities for vacua are "notoriously ambiguous" in the global description of eternal inflation, that the local
  point of view "is preferred by holography and naturally picks out a simple probability measure", and that "in lieu
  of anthropic criteria, I propose to estimate [the probability for observers] by the entropy that can be produced in
  a local patch." This is the measure [BHKP07] cites as its reference [21] and builds on.
- **[HS07]** J. B. Hartle and M. Srednicki, "Are We Typical?", Phys. Rev. D 75, 123523 (2007); arXiv:0704.2630 (v3,
  17 May 2007). **Abstract only.** The abstract says that some calculations commit a "selection fallacy": they treat
  us as "randomly chosen from a class of objects by some physical process, despite the absence of any evidence for
  such a process, or any observational evidence favoring our typicality", and that assuming typicality amounts to a
  choice of prior that "should be made explicit". *Ours:* [BHKP07] does assume typicality (its Fig. 1 caption speaks
  of "the vacuum energy measured by typical observers", and Sec. 4.3 reasons from "we get to make only one
  measurement" to "we can expect that it will not be a very unlikely value"); [HS07] appeared two months later and is
  the standard objection to that step. [BHKP07] does not discuss the objection, which is unsurprising given the dates.

Today's date: 19 October 2026.

## 2. What the Causal Entropic Principle says (one paragraph)

**The paper says** (Sec. 2.3, the two numbered conjectures; Eq. (9)) the principle is two conjectures. First, "the
universe consists of one causally connected region, or 'causal diamond'. Larger regions cannot be probed and should
not be considered part of the semi-classical geometry." Second, "the number of observations is proportional to ΔS, the
total entropy production in the causal diamond." A vacuum (a possible setting of the constants, here a value of the
cosmological constant Λ) is therefore weighted by w = ΔS (Eq. (9)), the increase in the entropy of ordinary matter
inside the diamond, with the entropy of horizons (de Sitter or black hole) deliberately left out (Sec. 2.3, paragraph
on Bekenstein-Hawking entropy and footnote 6). Why entropy stands in for observers: "observers, whatever their form,
have to obey the laws of thermodynamics. Observation requires free energy and is clearly incompatible with thermal
equilibrium or an empty universe. The free energy, divided by the temperature at which it is radiated, can be regarded
as a measure of the potential complexity arising in a spacetime region. This is equal to the number of quanta
produced, or more fundamentally, the entropy increase ΔS" (Sec. 2.3, "Motivation"). The result for Λ: with a prior
that is flat in ρ_Λ (Eqs. (6), (7)), the probability per unit log ρ_Λ is dP/dlog ρ_Λ ∝ ρ_Λ ΔS(ρ_Λ) (Eqs. (8), (34),
(35)); because the diamond's spacetime volume goes as 1/ρ_Λ (Eq. (21) and the text after it), a constant entropy
production rate would make this flat in log ρ_Λ (Eq. (36)), and the actual time dependence of entropy production then
picks out a peak (Sec. 4.2; Eq. (37)). In plain words: more vacua have a large Λ, but a small Λ buys a bigger
causal region and so more entropy production; the two cancel, and what is left over decides where the probability
peaks.

## 3. The mechanism of the peak

- **What produces the entropy.** The paper says (Sec. 3.2, "Stars"; Sec. 4.1, first paragraph) the dominant source is
  "the infrared glow of dust heated by starlight": about a tenth of baryons end up in stars, about a tenth of those
  burn, releasing about 7 MeV per baryon, and "more than half of this radiation is reprocessed by dust" and re-emitted
  at about 20 meV, so "there will be more than 100 infrared photons per optical photon" and stellar burning gives "an
  entropy of order 10^6 per baryon, after reprocessing by dust". Active galactic nuclei, supernovae and galaxy cooling
  are each estimated and found smaller (Sec. 3.2, the subsections with those names).
- **Why the rate is peaked in time, and when.** The paper says (Sec. 3.3, "Time dependence") the star formation rate
  "may be grossly described as a smooth function that peaks at around 2.5 Gyr and subsequently decreases
  exponentially with time", with different fits giving t_⋆ ∼ 1.5–3 Gyr; two fits are used, "N" (Nagamine et al.,
  peak 1.7 Gyr) and "H" (Hopkins and Beacom, peak 2.8 Gyr) (Fig. 5). Convolving the star formation rate with the
  entropy output of a stellar population as it ages (Eqs. (23)–(31)) gives an entropy production rate per comoving
  volume that "peaks when the universe is about 2.3 Gyr old and 3.3 Gyr old for the two curves" (text after Eq. (31);
  Fig. 6). The Introduction states the range as "approximately 2 to 3.5 billion years after the big bang", and Sec. 4.2
  writes t_peak ∼ 2 to 3.5 Gyr. "At earlier times, it is lower because fewer stars have formed; at late times, it is
  lower because few new stars form while older ones have burned out" (Sec. 4.2). The rate does not fall to zero: "due
  to the high abundance of long-lived low mass stars" it "maintains a finite value long after star formation has
  ceased" (after Eq. (31)), the smallest stars burning for about 5000 Gyr (after Eq. (30)).
- **What cuts the count off: the diamond, not the stars.** The paper says the comoving volume inside the diamond,
  V_c(t) (Eqs. (18), (19); Fig. 4), is small at early times, largest at the diamond's "edge" where the two cones meet,
  at t_edge ≈ 0.23 t_Λ (Eq. (20); 3.9 Gyr in our universe), and then goes to zero: "this reflects the exponential
  dilution of all matter, which is expelled from the diamond by the accelerated expansion" (after Eq. (20)). Here t_Λ =
  (3/8πρ_Λ)^{1/2} (Eq. (11); 16.7 Gyr for the observed value). So a larger Λ means a smaller t_Λ and an earlier,
  smaller diamond.
- **How this makes the probability peak near the observed Λ.** The paper says (Sec. 4.2) that for large ρ_Λ "the
  causal diamond is small, and it will contain only a small comoving volume by the time the entropy production peaks",
  so the probability falls with ρ_Λ; for small ρ_Λ "the causal diamond is very large, but the entropy production rate
  peaks early, when the comoving volume is still relatively small", so the probability rises with ρ_Λ. The maximum is
  where the two timescales agree: **t_edge(ρ_Λ) = t_peak** (Eq. (37)), which by Eqs. (11) and (20) gives
  log ρ_Λ,peak ≈ log(0.006/t_peak²) ≈ −123 (Eq. (38)). Fig. 9 is a cartoon of this. The dependence of the star
  formation rate itself on Λ (Eq. (32), via the Press–Schechter fraction of matter in halos above 10^7 solar masses) is
  "only a tiny correction" (after Eq. (32); Fig. 7); the Λ-dependence "enters mainly through V_c" (after Eq. (33)).
- **The quantitative result.** The paper says (Sec. 3.4, after Fig. 8): for the N star formation rate "the median
  value is ρ_Λ = 5.6 × 10^−123 with the 1σ error band between 4.2 × 10^−124 to 5.8 × 10^−122"; for the H rate "the
  median value ρ_Λ = 2.1 × 10^−123 with the 1σ error band between 2.4 × 10^−124 to 1.4 × 10^−122". The observed value
  is (1.25 ± 0.25) × 10^−123 (Eq. (1)). "With either choice, the observed value is well within the 1σ region, and
  hence, not unlikely" (Sec. 3.4). The width of the distribution is set by the times t_on and t_off at which the rate
  is half its peak, put through Eq. (37) (Sec. 4.2). **The paper gives no percentile.** *Ours, arithmetic on their
  numbers:* the observed value sits a factor 4.5 (N) or 1.7 (H) below the median; measured in log ρ_Λ against the
  lower 1σ edge, that is roughly 0.6σ (N) and 0.25σ (H) below the median. Sec. 4.3 says that exactly this kind of
  number is "entirely irrelevant": "we get to make only one measurement", and the claim is only that the observed
  value "was not unlikely to have been observed". For comparison, the paper says the observers-per-baryon weighting
  puts the observed value 3.5σ below its median if dwarf galaxies of 10^7 solar masses can host observers, 2.9σ at
  10^9, and 1.8σ (a factor of 22) only if one assumes galaxies of 10^12 solar masses are needed (Sec. 2.2; Fig. 2).

## 4. Observers against entropy: a count, or a proxy?

**The paper says** the count is of entropy, used as a stand-in for observations, and the two are declared
proportional on average, not equal. The second conjecture is "the number of observations is proportional to ΔS"
(Sec. 2.3), and the Introduction says the principle "assumes that on average, the number of observations will be
proportional to the amount of matter entropy produced in a causally connected region". The justifying sentence is in
Sec. 2.3, "Motivation": "The basic idea is that observers, whatever their form, have to obey the laws of
thermodynamics. Observation requires free energy and is clearly incompatible with thermal equilibrium or an empty
universe." And in the Introduction's outline: "Since observation requires free energy, it is natural to expect that
the number of observers will scale, on average, with ΔS. In other words, we demand nothing more than that observers
obey the laws of thermodynamics."

The paper does not say the two are equivalent. It allows that "there might be an absolute minimum complexity necessary
for observers, so that subcritical weights ΔS < ΔS_crit should be replaced by zero", and chooses "simply ΔS, with no
cutoff" because a cutoff "does not appear to play an important role for the questions studied here" (Sec. 2.3). It
also says that keeping conjecture 1 and using explicit anthropic criteria for observers instead of ΔS "would not have
changed our final result significantly" (Sec. 2.3, last paragraphs): the improvement over earlier work comes from the
causal-diamond cutoff, not from the entropy proxy. It offers evidence that the proxy is a good one after the fact: ΔS
"would drop sharply if galaxies, stars, or heavy elements were absent" (Sec. 4.1), and a universe without heavy
elements, hence without dust, would get a weight 100 times smaller (Sec. 4.1). Footnote 10 notes, half in jest, that
the Earth and the authors themselves are entropy producers of the counted kind. The paper stresses the weight is an
entropy *difference*, "not to an absolute entropy or the exponential of an entropy" (Sec. 2.3, paragraph on the
Hartle-Hawking amplitude).

*Ours:* so "observers" never enter the calculation as a number; the whole physical content is a thermodynamic
proportionality, which [HS07] would call a typicality prior made explicit.

## 5. How the causal diamond bounds what is counted; pasts times futures

**The paper says** yes to the geometric question. "The causal diamond [29] is the largest region of spacetime
causally accessible to a single observer. It is defined by the intersection of the past light-cone of a late-time
point on the worldline with a future light-cone of an early-time point, shown in Fig. 3." The early point is placed
at reheating, "since no matter existed before then", and more carefully a diamond is "triggered (that is, a bottom
cone drawn) as soon as there is entropy in the matter sector" (Sec. 2.3). The late point, for a positive Λ, is on the
de Sitter event horizon; for a negative Λ it would be on the big crunch (Sec. 2.3). The paper gives the diamond in
conformal time as r = Δτ/2 − |Δτ/2 + τ| (Eq. (18)), with Δτ the finite total conformal lifetime 2.804 t_Λ^{1/3}
(Eq. (17) and the sentence after it); the comoving volume is V_c = (4π/3) r³ (Eq. (19)).

**On pasts times futures.** *Ours, unverified, and the honest answer is: the paper's structure resembles the owner's
reading in one specific sense and does not support it in the sense she means.*

- What resembles it. The diamond's radius at a given time is the smaller of two light-travel distances: how far light
  has come since the bottom tip, and how far it can still go before the top tip (that is what Eq. (18) says: the
  comoving radius grows linearly in conformal time up to the midpoint and shrinks linearly after). So the *size* of
  the region whose contents count at time t is bounded by both "what came before" (the bottom cone) and "what can come
  after" (the top cone), and it peaks exactly at the middle of the conformal lifetime, τ(0)/2 (Eq. (20)). The paper
  says the probability peaks when this geometric middle coincides with the peak of the entropy production rate
  (Eq. (37)). That is a middle-of-the-history peak with a past constraint and a future constraint, which is the shape
  of the owner's conjecture.
- What does not support it. The quantity the paper counts is not a product of a count of pasts and a count of futures.
  ΔS(ρ_Λ) = ∫ dt V_c(t) ∂_{V_c}Ṡ(t) (Eq. (33)) is an *integral over time* of (volume in the diamond) × (entropy
  production rate per volume); nothing in it is a number of histories leading to a state, nor a number of
  continuations from it. The radius r(τ) is a *minimum* of two distances, not a product of two counts. The paper never
  speaks of "versions", histories, or counting alternatives; its entropy is thermodynamic entropy of matter (photons
  produced), and it explicitly distinguishes this from counting quantum states ("has nothing to do with the
  Hartle-Hawking amplitude, exp(S_dS), which describes the number of quantum states", Sec. 2.3). The paper does not
  touch a pasts-times-futures reading at all.
- *Ours:* the one place a product does appear is the order-of-magnitude argument in Sec. 4.2, where for a constant rate
  the total ΔS is "the product of t_Λ M(t_Λ)" (time available × mass inside the horizon). That is a product of a
  duration and a volume, not of a past count and a future count, and the paper labels it a rough estimate.

## 6. The "why now" coincidence

**The paper says** it explains it, and the explanation is the peak of section 3. Introduction: "The same result also
explains the so-called coincidence problem or 'why now' problem. According to the Causal Entropic Principle, typical
observers will exist when most of the entropy production in the causal diamond occurs. Our result ensures that this
happens during the era when the matter and vacuum energy densities are comparable." The mechanism: the preferred Λ is
the one for which the diamond's edge time, t_edge = 0.23 t_Λ (Eq. (20)), equals the time of peak entropy production
(Eq. (37)); and t_Λ is also the time scale on which vacuum energy takes over, with equality ρ_Λ = ρ_m at 0.59 t_Λ
(after Eq. (13); 9.8 Gyr in our universe). Sec. 4.2 restates it: "vacua with smaller ρ_Λ give rise to a larger causal
diamond, i.e., to a bigger de Sitter horizon and a longer time until vacuum domination", and the Introduction: "ρ_Λ
prefers to take a value such that vacuum energy begins to dominate near the time of peak entropy production."

*Ours:* note what is and is not derived. The paper derives that Λ-domination and peak entropy production fall within a
factor of a few of each other in time (0.23 t_Λ against 0.59 t_Λ). It does not derive that an observer is at 13.7 Gyr
specifically, nor that ρ_Λ/ρ_m is 2.3 today (Eq. (4)) rather than, say, 0.5 or 10; "comparable" is the claim, and the
distribution's 1σ width is about two orders of magnitude in ρ_Λ (Sec. 3.4). The paper's observers are spread over the
entropy-production curve, which is why "now" is near equality rather than exactly at it.

## 7. Caveats the paper gives

- **Flat prior in Λ.** The paper assumes dN/dρ_Λ = const (Eq. (6)) because "ρ_Λ = 0 is not a special point", and
  dp/dN = const (Eq. (7)), with footnote 4: "Dynamical effects can modify this flat prior [27]. We shall assume that
  the resulting distribution remains effectively flat, at least for small |ρ_Λ|. Models violating this assumption are
  unlikely to solve the cosmological constant problem."
- **Only positive Λ, everything else held fixed.** "Our distribution is conditioned on the assumptions that ρ_Λ > 0,
  and that all low energy physics is the same as in our vacuum" (Introduction, "Extensions"). A "preliminary analysis
  indicates that negative values will be somewhat favored by the Causal Entropic Principle, though not by enough to
  render the observed value unlikely" (same place). Varying several parameters at once is named as "a much more
  stringent test" and left for future work.
- **Dependence on the star formation model.** Two star-formation histories are used precisely "to illustrate the
  systematic dependence of our calculation on the time dependence of star formation" (Sec. 3.3), and their differences
  "hint at the systematic uncertainties" (Fig. 8 caption). The result is "completely insensitive to this overall
  normalization; it depends only on the shape of the SFR" (Sec. 3.3). The stellar physics is admitted to be crude: "we
  assumed overly simplistic formulae for the luminosity and the lifetime of a star ... ignored the dependence on
  metallicity" (after Eq. (31)); the prediction "depends only on the roughest features: the width and position of the
  peak of the entropy production rate". The choice of 10^7 solar masses as the smallest star-forming halo is said to
  involve "no speculation about what observers need" and the result to be "quite insensitive to this choice"
  (Sec. 3.3, "Dependence on ρ_Λ").
- **Curvature.** The paper assumes a spatially flat FRW metric (Eq. (10)) and, more strongly, "that the cosmological
  constant dominates before curvature does, for all values of ρ_Λ considered here. Thus, we are assuming that the
  universe is flatter than necessarily required by current constraints" (Sec. 3.1). Spatial curvature k is listed
  among parameters whose distribution it would be "interesting" to compute (Introduction, "Extensions").
- **The radiation era is neglected**, justified in Appendix A: the correction to the diamond's size is below 1 % at the
  observed Λ and small wherever the distribution has support (Eq. (48) and the text after it).
- **Horizon entropy excluded.** Bekenstein-Hawking entropy of the de Sitter horizon and of black holes is left out
  because "it is difficult to see the relevance of horizon entropy to the existence of observers" (Sec. 2.3); footnote
  6 argues the exclusion is unlikely to matter qualitatively since supermassive black hole growth peaks at a similar
  time. Hawking radiation from black holes is neglected as too slow (Sec. 3.2).
- **Boltzmann brains.** The paper does not mention Boltzmann brains, freak observers or thermal fluctuations as
  observers anywhere in the text (searched for "Boltzmann" and "brain": no match). It does say that vacua with ρ_Λ of
  order one, "which can contain only a few bits, have strictly zero probability of hosting observers" (Sec. 2.3), and
  that a diamond in a metastable de Sitter vacuum "empties out at an exponential rate" after Λ-domination, so that
  enlarging it adds nothing (Sec. 2.3). *Ours:* this definition, by construction, stops counting once matter has left,
  which is the regime where Boltzmann-brain arguments live; but the paper does not say so, and it is not a treatment.
- **The statistical claim is deliberately weak.** "The success of the Causal Entropic Principle ... is not that it
  predicts the precise value of ρ_Λ, but that our distribution shows that the observed value was not unlikely to have
  been observed" (Sec. 4.3). *Ours:* the typicality assumption this rests on is what [HS07] objects to; the paper
  predates that objection and does not answer it.

## 8. What this supplies to the project (ours, unverified)

The owner's conjecture (VISION Updates 26, 33 position 4, 43; ASSUMPTIONS O101) is that a loop's turn is scored by
what it produces, that the reward is observers who evolved, and, in the form put to this reader, that the "number of
versions" at a time is the number of pasts leading to a state times the number of futures following it, peaking in
the middle. Set against this paper:

- **What corresponds.** The paper's ΔS is the one published quantity we know of that (a) stands in for "observers" by
  a stated rule, (b) is a finite number per causal region because the region is bounded at both ends in time, and (c)
  peaks in the middle of the history for a stated reason: the bottom cone starves it early, the top cone starves it
  late (Sec. 4.2; Eq. (20)). Its *rate*, dS/(dV_c dt) (Eq. (31); Fig. 6), is the paper's version of "how much
  observer-making is going on at time t", and the comoving volume in the diamond, V_c(t) (Eq. (19); Fig. 4), is its
  version of "how much of the world counts at time t". VISION Update 43 already notes that the paper counts something
  that goes with observers rather than observers; that reading is confirmed by the text (Sec. 2.3, 4.1).
- **What does not correspond.** ΔS is not a count of versions, histories or arrangements. It is thermodynamic entropy
  of matter (mostly a photon count), integrated over time; the paper separates it explicitly from a count of states
  (Sec. 2.3). The diamond's radius is a minimum of a past reach and a future reach, not a product of a past count and
  a future count, and the paper never multiplies pasts by futures. The owner's "pasts times futures" is therefore not
  supported by this paper; at most, the diamond offers an analogy for *why* a bounded-at-both-ends count peaks in the
  middle. The paper's bottom tip is also a physical event (reheating, the first matter entropy), not the start of a
  cycle, and its top tip is a horizon fixed by Λ, not the end of a turn; it has no cycle, no re-collapse (for Λ > 0),
  and no mechanism by which a turn ends, so it does not supply the "stated end" O101 asked for except in the form
  "matter leaves the horizon".
- **Where it bears on the measure question.** The paper's answer to "which region do we count over" is the single
  causal diamond of one observer (conjecture 1), motivated by black-hole complementarity (Sec. 2.3, "Motivation"), and
  [Bousso06]'s abstract says this local measure "is insensitive to large expansion factors or lifetimes". That is the
  published alternative to the owner's "per turn" unit (VISION Update 23): a region bounded causally rather than a
  cycle bounded in time. It is a target in rule 13's sense, not a confirmation.
- **What a toy-model version of the count would have to define.** (i) A clock and a causal structure: the toy has
  neither time nor a light cone (CLAUDE.md; VISION Update 36 on the speed limit), and the diamond is defined by light
  cones, so the first requirement is a front speed from the dynamics, which T47 part A measured only as "the steady
  fronts any uniform medium gives". (ii) A matter-sector entropy that increases: the toy's H is a count of squares and
  the toy conserves energy when sealed; what plays the part of free energy being radiated to a cold sink at a
  temperature is not defined. The sealed bath of C stores (ASSUMPTIONS Q12) has a temperature read off it, so an
  entropy change of the bath is computable in principle, and that is the nearest candidate. (iii) A region that
  empties: the paper's cutoff comes from matter leaving the horizon; the toy's new space does not expand, so nothing
  leaves, and some other stated end would be needed. (iv) A flat prior over the varied parameter, with the Jacobian
  handled as in Eqs. (6)–(8): if λ or D is the thing varied, the toy would have to say what "uniformly distributed in
  λ" means and why. None of these exists in the toy today, and this note recommends none be built without a dated
  decision under S1.
- **One number the paper hands over for rule 13's checklist.** Eq. (38): log ρ_Λ,peak ≈ log(0.006/t_peak²). It is a
  prediction from one input (the time of peak entropy production, 2 to 3.5 Gyr), with its uncertainty propagated
  through the width of the rate curve (Sec. 4.2), and the input does not contain the target (the star formation
  history is in the matter era and "the cosmological constant played no dynamical role and cannot have anything to do
  with this peak", Sec. 3.3). That is the shape of derivation rule 13 asks for; what the paper does not do, by its own
  account (Sec. 4.3), is count how many other arbitrary weightings would also land within a factor of a few.

*Prior-work status (rule 15):* this note records one paper read in full and two abstracts; it is not a search and
does not license any "we have not found" sentence.
