# Reading note: CP violation and the matter excess (baryogenesis), 19 October 2026

**Why this note exists.** The owner asked on 19 October whether we can start exploring CP violation, after proposing
that curling energy is matter, uncurling energy is antimatter, and the small excess of matter is "a little more curl"
held in the stores (`sandbox/NOTEBOOK.md`, 19 October). This note records what is settled physics, what is open, and
what the toy can and cannot hold, so that the words are used as physics uses them before any design is written.

**Status of the reading.** Search summaries only (the assistant's web search of 19 October); none of the papers below
has been read in full by us, and every number is "to verify" until one has. Nothing here is evidence for the hypothesis
(rule 13: a published result is a target). The bibliography keys are not yet in `REFERENCES.bib`; they are added when
a paper is read.

## 1. What is settled, in plain words

- **Pair production.** Light of enough energy (at least twice the rest energy of the particle) makes a particle and
  its antiparticle together, and the conserved quantities (charge, baryon number, lepton number) are conserved by the
  pair. The owner's sentence on this is standard physics as she wrote it.
- **Annihilation.** A particle meeting its antiparticle becomes light of the same total energy. Energy is not
  "cancelled"; what cancels is the count (the net number of particles of that kind). The record already says this
  (notebook, 18 October).
- **The hot early universe** held nearly equal numbers of particles and antiparticles in a plasma with the light. As it
  cooled they annihilated, and the light they became is part of the photon bath. The excess that survived is all the
  ordinary matter there is.
- **The size of the excess.** About one baryon per 10^9 to 10^10 photons: the baryon-to-photon ratio η is about
  6 × 10^-10 (the lecture notes found give n_B/s of about 10^-10 at temperatures far above the nucleon mass; the
  6 × 10^-10 is from general knowledge and is to be checked against [Planck18]). This is the number any account of
  "a little more matter" has to produce.
- **The microwave background** is not the annihilation flash itself. The annihilation light was thermalised long
  before; the background is the bath's light set free when atoms formed, about 380,000 years in, at about 3,000 K, now
  stretched to 2.7 K. The owner's "becomes the background radiation" is right in the sense that the bath carries the
  annihilation energy, and wrong if read as the flash reaching us directly.
- **CP violation exists.** Some weak-interaction processes treat matter and antimatter differently: seen in neutral
  kaons (Cronin and Fitch, 1964), in B mesons (BaBar and Belle, 2001), in D mesons (LHCb, 2019), and for the first
  time in a baryon in 2025: LHCb measured an asymmetry of (2.45 ± 0.46 ± 0.10) % between the decay of the Λb⁰ baryon
  to a proton, a kaon and two pions and the same decay of its antiparticle, at 5.2 standard deviations
  ([LHCb25], arXiv:2503.16954, reported as published in Nature; a commentary is arXiv:2504.15008). In the Standard
  Model all of it comes from one phase in the quark mixing matrix (Kobayashi and Maskawa, 1973).

## 2. What is open: the origin of the excess (baryogenesis)

Sakharov (1967) stated three conditions for a universe that starts balanced to end with an excess:

1. a process that changes the net count of baryons;
2. a process that treats matter and antimatter differently (C and CP violation);
3. a departure from thermal equilibrium, so that the excess made is not undone.

The search summaries agree on how the Standard Model fares: it meets (1) only through quantum effects that are fast
in the hot plasma and negligible now; its CP violation (2) is far too small, by about ten or more orders of magnitude
on the usual estimate, one summary says 10^-20 of what is needed; and its electroweak change is a smooth crossover,
not the strongly first-order transition that (3) needs in the best-studied mechanism, electroweak baryogenesis
(review: arXiv:2508.09989, "Bubble Trouble"). So the excess is an open problem, and proposals either add a source of
CP violation or a first-order transition, or both. One older proposal (Nasser and Turok, arXiv:hep-ph/9406270,
abstract only) keeps the Standard Model's CP violation and amplifies it.

## 3. Where the owner's picture meets this

- **Condition 3 is the burp.** A sharp change from a stable-for-now state with a moving front is a departure from
  equilibrium, and the record said on 5 October (VISION Update 42) that the walls of first-order bubbles are where the
  best-studied mechanism makes the excess. That is the one place her hypothesis touches the problem with something it
  already has.
- **Condition 2 is what "the stores hold a little more" supplies**, and it supplies it as an input: an asymmetry put
  into the ledger, not one the toy makes. A mechanism would have to say why curl and uncurl are not exact inverses.
- **Condition 1 has no counterpart in the toy** (it has no count of particles), unless the two kinds of point are read
  as the two kinds of matter, and then see section 4.

## 4. What the toy has, exactly

- **Curl and uncurl cancel to the unit.** Under the layer form a contraction costs exactly a N_slab and a split
  releases exactly a N_slab (`graphity.contraction`; VISION Update 65). The reference arm of T71 is this cancellation
  running: the lump pays the fold back.
- **The "little more" sits in the parent, not the daughter.** Under the one-way rule (Update 66) every daughter carries
  exactly a N_slab; the parent's stores hold the gate plus the feed since the last burp. In a sandbox look
  (`sandbox/LOG.md`, 19 October) that excess read 0.3 % of everything released at λ = 1.25 and 28 % at λ = 1.10, a number
  set by the gate, the rate and the moment of reading. It is not 6 × 10^-10 and is not to be tuned to it.
- **The two kinds of point are exactly equal in number, always.** Every link joins one point of each kind and every
  point has the same number of links, so in every valid state at every size the two kinds are equal. An excess of one
  kind cannot exist in the toy. The energy and every move are symmetric under swapping the kinds. So the toy has no C,
  no P and no CP as it stands; a CP-violating toy needs a new ingredient under S1 (a term or a move rule that tells the
  kinds apart, or a degree rule that lets their counts differ).
- **The one sign the toy's weights ever see** is the exchange sign of Update 29 (O57): an arrangement with an odd
  renaming gets zero weight. It is a selection rule, not an asymmetry between kinds.

## 5. What would be a next step, if the owner wants one (none is decided)

- Read in full before anything is designed: Sakharov 1967 (JETP Lett. 5, 24); the "Bubble Trouble" review
  (arXiv:2508.09989) for how an excess is made at a bubble wall, since the burp's front is the only point of contact;
  [LHCb25] for what a measured asymmetry looks like.
- The one exact question the toy can be asked without a knob: is there any move in the current sets whose reverse is
  not in the set, or costs a different amount? (The gate is such an asymmetry in timing: a split waits for a N_slab in
  the stores, a contraction does not. It does not change what is released.) A written answer, then her decision.
- Any ingredient that makes curl and uncurl unequal in energy, or lets the kinds differ in number, is a new knob and
  needs her dated VISION decision before it is run.

## Sources (search summaries, 19 October 2026; none read in full)

- LHCb, "Observation of charge-parity symmetry breaking in baryon decays", arXiv:2503.16954 (2025).
- "New horizon in particle physics: first observation of CP violation in baryon decays", arXiv:2504.15008 (commentary).
- "Bubble Trouble: a Review on Electroweak Baryogenesis", arXiv:2508.09989.
- Nasser and Turok, arXiv:hep-ph/9406270 (abstract).
- D. B. Kaplan, lecture 9 of a graduate course (baryon asymmetry; n_B/s about 10^-10), archive.int.washington.edu.
- "Weak Interactions in Atoms and Nuclei: The Standard Model and Beyond", arXiv:nucl-th/0305040 (Standard Model
  sources of CP violation and their size).
