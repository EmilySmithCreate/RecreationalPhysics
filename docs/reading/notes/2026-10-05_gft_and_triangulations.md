# Group field theory condensates and dynamical triangulations: reading notes (5 October 2026)

The owner asked how the most developed "space is a phase" programmes stand and how they meet her hypothesis. **Read
by an assistant agent on 5 October 2026 from the arXiv HTML texts, searched locally; the owner has not read these
passages.** Read status is given per paper. Keys refer to `REFERENCES.bib`; papers without a key are cited by arXiv
number and were read only as stated.

## In one paragraph

Neither programme contains a change between two ordered geometric phases with different numbers of large dimensions.
Group field theory has one non-geometric and one geometric phase, joined by a transition its own methods treat as
continuous, and its Big Bang is a bounce inside the geometric phase with no energy released. Causal dynamical
triangulations have first-order transitions with barriers and hysteresis, but as features of a phase diagram, never
as an event in time. Their history is a direct caution for this project's "one hump" result at small sizes.

## Group field theory (GFT) condensate cosmology

- **[MOPT23] Marchetti, Oriti, Pithis, Thürigen, "Mean-field phase transitions in TGFT quantum gravity"**, Phys. Rev.
  Lett. 130, 141501 (2023); arXiv:2211.12768. *Full text read.* The condensate picture "relies on the assumption of a
  phase transition to a nontrivial vacuum (condensate) state describable by mean-field theory". Mean field is argued
  valid because "the theory's effective dimension blows up towards the IR". "The full theory space is very involved
  and largely out of reach for explicit control".
- **Ben Geloun, Pithis, Thürigen**, arXiv:2305.06136. *Abstract and Secs. 4.3, 5.* "The two phases are connected via a
  continuous phase transition at a critical surface", in one approximation.
- **[Ori21] Oriti, "Tensorial group field theory condensate cosmology as an example of spacetime emergence in quantum
  gravity"**, arXiv:2112.02585. *Secs. 5.3 and 6 in full; 4 to 5.2 in part.* "we find a quantum bounce instead of the
  big bang". As a conditional alternative: "Geometrogenesis replaces the big bang in quantum gravity." And: "there is
  no notion of time that could be applied to the whole set of continuum phases"; "All the above reasoning is tentative
  as much as it is sketchy".
- **A 2024 collection of perspectives**, arXiv:2411.12628. *Two sections read.* Computing the full effective action "is
  currently out of reach"; the bounce "may however be spoiled by quantum effects".
- **Abstracts only:** Oriti, Sindoni, Wilson-Ewing (arXiv:1602.05881, the bounce); Oriti and Pang (arXiv:2105.03751:
  it "fails to give a compelling inflationary scenario in the early universe" and gives "phantom-like dark energy" at
  late times); a critique of geometrogenesis by Mozota Frauca (arXiv:2307.11805).

**Answers.** The order of the transition: continuous, by the method chosen (mean field with a diverging correlation
length; one renormalization-group approximation). No simulations, no finite-size analysis, and no first-order analysis
was found in the texts searched. The Big Bang: a bounce inside the geometric phase is the working result; the
transition itself replacing the Big Bang is a conditional alternative. Energy released at the transition: nothing
found. Two geometric phases, or a change in the number of dimensions: no.

## Causal and Euclidean dynamical triangulations (CDT, EDT)

- **[AL26] Ambjørn and Loll, "Causal Dynamical Triangulations: New Lattice Theory of Quantum Gravity"**,
  arXiv:2604.05641 (April 2026). *Secs. 5, 7, 10 in full.* Of the phases other than the extended one: "The other
  phases appear to be lattice artefacts, which lack any discernible relation with a continuum theory of gravity."
  Simulations reach "quantum spacetimes of linear size of the order of 12-20 Planck lengths".
- **[AGGN22] Ambjørn, Gizbert-Studnicki, Görlich, Németh, "Topology induced first-order phase transitions in lattice
  quantum gravity"**, JHEP 04 (2022) 103; arXiv:2202.07392. *Full text read.* "phase transitions which involve a change
  in topology will be first-order transitions"; "a barrier for such a change can be created and lead to pronounced
  hysteresis". A transition first reported as possibly higher order was revised to first order with larger volumes.
- **Loll's review**, arXiv:1905.08669. *Two sections searched.* For one transition "the two peaks showed a tendency to
  approach each other for growing four-volume", and a "(potentially misleading) double peak in histograms simply
  disappears" when a different quantity is held fixed.
- **Ambjørn, Jordan, Jurkiewicz, Loll**, arXiv:1205.1229. *Abstract and Sec. 4.* At a first-order transition: "The
  histogram at N4=40k assumes an approximate Gaussian shape, which gets distorted at N4=80k, with a double peak
  starting to emerge at N4=100k".
- **Coumbe and co-authors**, arXiv:1904.05755. *Parts.* On a torus: "We were not able to observe double peaks in
  histograms of the order parameter", and the transition was still classed as (weakly) first order from how the
  transition point shifts with size. Their code uses "parallel tempering/replica exchange".
- **[RdF15]** (already in the bibliography; re-read in part): the Euclidean transition was "long believed to be of
  second order until in 1996 first order behavior was found for sufficiently large systems"; "for N4 ≥ 32k a clear
  double peak".
- **A 2026 machine-learning study**, arXiv:2510.02159. *Parts.* These transitions are "somewhat atypical, sharing
  certain features of both first- and higher-order transitions".

**Answers.** Which transitions are first order: several, each established only at large sizes, with two revised after
first being read as higher order. Do the phases differ in dimension: one is extended and four-dimensional, one is
branched and one collapsed; the one transition between two extended phases keeps four dimensions. Latent heat,
nucleation, fronts: the word "latent" was not found in seven of the texts; barriers and hysteresis are described as
features of the simulation history, not of a process in physical time. Methods against slow dynamics: replica
exchange; how the transition point shifts with size (an exponent of 1 means first order); the trend of the Binder
cumulant with size; measuring on both sides of a hysteresis loop.

## How they meet this project (*ours, from the agent's reading*)

- **Not found in either:** an order → order change with a change in the number of large dimensions and an energy
  release. "The Big Bang is a transition into a geometric phase" is in print (geometrogenesis); this is not.
- **GFT runs the other way on three counts**: non-geometric to geometric, treated as continuous, a bounce with nothing
  released. A reader from that programme will ask what clock the tube opens against, because in their framework the
  phases are not connected by a process in time.
- **CDT's topology conjecture is the nearest published support**: changes that need a rearrangement of the whole
  configuration are first order, with a barrier and hysteresis. The tube opening into a sheet is that kind of change.
  It is a conjecture about equilibrium ensembles, and its authors call the other phases lattice artefacts.
- **A caution for T6's "one hump"**: three first-order transitions in these programmes showed a single hump at small
  sizes, and one higher-order transition showed a misleading double hump. INCONCLUSIVE was the right verdict at a
  hundred points. The discriminators those groups rely on are how the transition point shifts with size and the trend
  of the Binder cumulant, at sizes in the tens of thousands and up.
- **Tori.** In CDT the order of one transition differs between a sphere and a torus. Every run in this project is on
  a torus.

## One narrow question each

- GFT (Thürigen): in the mean-field analysis of [MOPT23], if two interactions of different order with couplings of
  opposite sign are kept, does the potential give a first-order transition into the condensate?
- CDT (Gizbert-Studnicki): at the toroidal transition classed as first order, is there a measured jump per building
  block that stays finite as the volume grows, and what is its value?
