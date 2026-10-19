# Reading notes: dynamical triangulations, as a published model with a varying count of building blocks (2026-10-18)

> **Status of these notes: nothing new below was read.** Written 18 October 2026 at the owner's request ("Let's learn a
> little bit more about dynamical triangulation"). This session's network proxy refused every paper host tried (arxiv.org,
> export.arxiv.org, ar5iv, inspirehep, scholarpedia, wikipedia: all 403 or unreachable). The one tool that worked was a
> web search, which returns a search engine's summary of a page, not the page. So every statement is one of:
>
> - **[already in the record]**: from entries read in part by an assistant agent on 2026-10-05 (REFERENCES.bib [AGGN22],
>   [AL26]), with their own status lines.
> - **[search summary]**: what the search engine said a page says. Not read. No section or equation numbers, because
>   none were seen. To be checked against the paper before it is quoted or cited anywhere.
> - **[general knowledge, to verify]**: the assistant's memory, not any page in this session.
> - **[ours]**: a comparison with the toy, made here.
>
> The reading asked for (the review in full, searched, with section numbers) still has to be done on a machine that can
> reach arXiv. The owner has not read any of these.

## Why this model, in one paragraph

Dynamical triangulations build spacetime out of identical building blocks (simplices: triangles in two dimensions,
tetrahedra in three, their four-dimensional cousins in four) glued along their faces. The geometry is in how they are
glued, not in any coordinates. **The number of blocks is not fixed**: the moves add and remove blocks, and the energy
(the Regge action) charges a price per block. That price is the model's bare cosmological constant. It is the published
precedent VISION claim 3 names for "one energy function covers configurations with different counts", and it is the
nearest published relative of the contraction model's varying count of points (VISION Update 63; the brief, section 2.2).

## What the sources say

**The energy and the count** [search summary; the source is a 1998 review of discrete approaches, gr-qc/9805049, not
read]. In four-dimensional dynamical triangulations every block is equilateral, so the Regge action reduces to a count of
triangles and of four-dimensional blocks, with two bare couplings, one tied to Newton's constant and one to the
cosmological constant. The cosmological constant has to be tuned to a critical value for a continuum limit; below it the
sum over geometries diverges (too many geometries, each cheap). *Ours:* this is what a cost per point does in a model
whose count varies: with the cost too low the count runs away; with it right the count is set by the balance of the cost
against how many arrangements each count allows. The contraction model's mu_N is this constant, set to zero in the brief
pending the owner's decision; at zero the toy's count is set by the moves and the stores alone, which is the "diverges"
side of the published balance and should be said plainly if mu_N stays at zero.

**Fixed count or free count** [search summary; general knowledge, to verify]. Most simulations hold the count fixed
(a fixed-volume ensemble) and let it fluctuate only a little about a target, so the cosmological constant does not appear
as a free knob; it is conjugate to the volume and appears only when the volume is free. *Ours:* the toy so far is the
fixed-count case; the contraction model is the free-count case, and the published practice is to run it fixed and read
the constant off the fluctuations.

**The moves** [search summary; gr-qc/9805049 and 1404.5288, not read]. The local moves are Pachner moves, which change the
count of blocks (in four dimensions the 1-5 move adds four blocks and its inverse removes them; the 2-4 move adds two;
the 3-3 move keeps the count). They are ergodic: any two triangulations of the same topology are joined by a sequence of
them. The Regge action is invariant under some of them. *Ours:* the toy's compaction and splitting (a pair removed or
inserted, the count changing by two) are the counterpart of a Pachner move that changes the count, and the switch is the
counterpart of one that does not. The published model's ergodicity is a theorem; the toy's reach under the new moves is
owed (the brief, test E4).

**The phases, Euclidean version** [search summary; several sources, among them 1304.6339 and 2207.12642, not read]. At
fixed volume the plain (Euclidean) model has two phases, neither a space: a **crumpled** phase at low coupling, where a
few vertices touch almost every block (very high dimension), and a **branched-polymer** phase at high coupling, a tree
of thin tubes with dimension about 2. The transition between them was first thought continuous and is now reported as
**first order** in three and four dimensions at larger volumes; a 2022 study with a second (measure) coupling finds a
line of first-order transitions whose latent heat falls along the line. [already in the record: AGGN22, read in part on
5 October] a transition involving a change of topology is first order, with pronounced hysteresis.

**The causal version** [search summary; Loll's review 1905.08669, abstract only; already in the record: AL26, Secs. 5, 7
and 10 read in part on 5 October]. Causal dynamical triangulations add a time direction: blocks carry a time arrow, and the
arrows must agree where blocks meet, which forbids the branching and crumpling. The extended phase is then a
four-dimensional de Sitter-like universe emerging from the sum over geometries; the other phases "appear to be lattice
artefacts" [AL26]. Simulations reach "linear size of the order of 12-20 Planck lengths" [AL26]. The four-block coupling
there "plays a similar role to a cosmological constant, since it controls the total volume" [search summary].

## How it lines up with the hypothesis, and where it does not [ours]

| Question | Dynamical triangulations | The toy (contraction model) |
|---|---|---|
| What varies | the count of blocks, by Pachner moves | the count of points, by compaction and splitting |
| The price of a block | the bare cosmological constant, tuned | mu_N, set to zero pending her decision |
| Random phase | crumpled (high dimension) and branched (dimension 2), both unphysical | the melt (broken points) |
| The ordered phase | a de Sitter-like extended universe, in the causal version only | flat space (every width >= 6, H = 0) |
| Order of the transition | first order between the two unphysical phases (Euclidean); the causal version's transitions are their own question | T6: first order at lambda = 0, inconclusive at lambda >= 1 |
| Time | put in by hand as a foliation (causal version) | none |
| What it has that the toy lacks | a proven ergodic move set at varying count; a continuum-limit argument; a dimension measurement (spectral dimension running from about 4 to about 2) | nothing comparable |
| What the toy has that it lacks | a specific stable-for-now arrangement (the slab) that converts with an exact release; sealed energy bookkeeping | not asked there, as far as these summaries reach |

**What is worth aligning with**, in order: (1) the cost per block as the way a varying count is priced, which is the
decision the brief leaves to her (mu_N); (2) the practice of running at fixed count and reading the constant off the
fluctuations, which the toy could copy; (3) the spectral dimension as the observable of "is it a space", already on this
project's ladder (TASKS T13 rung 1) and never run. **What does not carry over:** the causal foliation (the toy has no
time) and the claim that a continuum limit exists (not something the toy aims at).

**Rule 15 note.** Nothing here is a "we have not found"; the opposite: a published model with a varying count exists and
is mature. Any sentence in the brief about the varying count should cite it as a precedent and not as a result.

## Sources (as given by the search engine; none read)

- Loll, "Quantum Gravity from Causal Dynamical Triangulations: A Review", arXiv:1905.08669, Class. Quantum Grav. 37
  (2020) 013002.
- Loll, "Discrete approaches to quantum gravity in four dimensions", arXiv:gr-qc/9805049.
- Ambjorn, Jurkiewicz, Loll, "Dynamically triangulating Lorentzian quantum gravity", arXiv:hep-th/0105267 (VISION claim 3;
  unread).
- Smit, "Continuum interpretation of the dynamical-triangulation formulation of quantum Einstein gravity", arXiv:1304.6339.
- "Discretization independence implies non-locality in 4D discrete quantum gravity", arXiv:1404.5288.
- arXiv:2207.12642 (a 2022 fixed-volume Euclidean study with a measure coupling; title not seen).
- Already in the record: [AGGN22] (arXiv:2202.07392), [AL26] (arXiv:2604.05641).
