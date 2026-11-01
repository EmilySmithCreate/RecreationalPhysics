# Prior-work search: the 14-point baby universe (the biplane graph) at λ = 0

CLAUDE.md rule 15. Filled in on 2026-11-01 (clock run before writing).

**The sentence it backs** (ASSUMPTIONS Q8 and section D; the note to the model's authors; any paper that mentions it):
"The 4-cube is not the only baby universe at λ = 0: the incidence graph of the 7-point biplane (14 points, three
squares on every link) ties with it in energy per point at every λ and forms by itself in about one finished piece in
seven. We have not found it named as a ground-state piece in the published work on this model or its relatives."

**Date of the search:** 2026-11-01.

**Who searched:** an assistant session (Claude Fable 5.1), with web search, the arXiv API, the OpenAlex API, local text
extraction of three PDFs, and the full text of [Kelly22]'s thesis (PDF supplied by the owner on 21 September). The owner
has not read these passages.

## Where was searched

| Source | Terms used | Results looked at | Nearest hit |
|---|---|---|---|
| arXiv API, full record search | "combinatorial quantum gravity" AND (hypercube OR biplane OR "baby universe") | 1 entry returned: [GV21] (2101.04072); its abstract names hypercubes and a ribbon only | [GV21] |
| Web search (general) | "combinatorial quantum gravity" biplane / "14 vertices" / "(0,2)-graph" baby universe hypercube | 10 results, all dynamical-triangulation "baby universes" (Ambjørn and others, 1993 onward); none about graph models | none |
| Web search (graph theory) | Brouwer (0,2)-graphs valency 4 classification 14 vertices biplane Mulder | MathWorld "(0,2)-Graph"; OEIS A282741; Li and Sun, arXiv:2512.15046 (full text extracted and searched) | FOUND in graph theory, see below |
| [GV21] full text (PDF extracted, searched for hypercub / biplane / (0,2) / ribbon / isomorph / "other bipartite") | as listed | Sec. 2 (its Eq. (2.11), Figs. 3, 4, 6, 7), Sec. 3.1 | "isolated or weakly connected d-dimensional hypercubes", "all 4-cycles belong to hypercubes" (connected case) |
| [KKVG23] Kochergin, Khaymovich, Valba, Gorsky, arXiv:2305.14416, full text extracted | hypercub / ideal cluster / biplane / (0,2) | "Structure of ideal cluster of k-cycles" | "for k = 4 the ideal cluster is a complete bipartite graph of 2d vertices" (a different model: no hard-core rule) |
| [Kelly22] thesis, full text (347 pages) | biplane / (0,2) / Heawood / Fano / hypercub | pp. 151 to 152 (Sec. 4.2.x, Eq. (4.96)); Fig. 4.10 | "multiple disconnected copies of the d-dimensional hypercube"; "Heawood" occurs once, on graph minors, unrelated |
| Forward citations of [GV21] (OpenAlex, W3119829593: 15 works) | titles scanned | 15 titles: Anderson-model and scar papers by the same group, [T22], [T23a], [T25b], [Kelly22a], [KKVG23], four referee reports | none names a second ground-state piece |
| Forward citations of [KTB19] (OpenAlex, W2911355343: 32 works) | titles scanned | 32 titles: reviews (Loll, Boguñá, Nokkala), Brunekreef and Loll, Tee, Akara-pipattana, Trugenberger's later papers, [GV21] | none names a second ground-state piece |
| [KTB19] and [T25] texts | read directly on 2026-09-20 (Q8) | Sec. 3.3.1 of [KTB19]; "Cycle condensation" of [T25] | "situations where more than one baby universe exists" (general words, no example) |
| Google Scholar; INSPIRE-HEP | not searchable by this session's tools | Semantic Scholar's API returned errors twice | not done |
| `REFERENCES.bib` and earlier notes | biplane, Q8, Mul79 | Q8, Q9, O85 ([Mul79] used for the 4^D bound) | this repository's own record only |

## What came closest

- **In graph theory the object is known and named.** A graph in which any two points have 0 or 2 common neighbours is a
  (0,2)-graph ([Mul79], which proves they are regular and that a (0,2)-graph of valency k has at most 2^k points, with
  equality only for the k-cube). Brouwer classified the small ones (A. E. Brouwer, "Classification of small (0,2)-graphs",
  J. Combin. Theory A 113 (2006) 1636; **not read**, cited from Li and Sun and MathWorld). Li and Sun (arXiv:2512.15046,
  Sec. on (0,2)-graphs, **read in the relevant passage**) state: "at k = 4, there is a single graph except Q4 with
  N = 14", which they call "the 1463 graph" from its layer counts, and they add that in such a graph "the three bottom
  layers are the same as that of the 4-dimensional hypercube". OEIS A282741 gives the counts of bipartite (0,2)-graphs by
  valency as 1, 1, 1, 2, 4, 13, 40, 104. Every valid piece of this model with three squares on every link is a bipartite
  (0,2)-graph of valency 4 (the hard-core rule caps common neighbours at 2, and three squares on every link means every
  pair at distance 2 has exactly 2), so **Brouwer's classification says the 4-cube and the 14-point graph are the only
  two baby universes possible at D = 2**, which closes Q8's "we have not shown that these two are the only ones". That
  the 14-point bipartite (0,2)-graph of valency 4 is the biplane's incidence graph is our identification (Q8, checked by
  computer); Brouwer's uniqueness makes it the same graph as the "1463 graph". *Exact once Brouwer's theorem is read in
  the original; until then it rests on two secondary statements of it.*
- **In the physics literature the cold phase is described as hypercubes.** [GV21] (read in full in the relevant
  passages): "a set of isolated or weakly connected d-dimensional hypercubes", the count N / 2^d, the rest in one
  "closed bipartite ribbon"; in the connected case "all 4-cycles belong to hypercubes". Their model differs from ours
  in two ways that matter here: it imposes neither bipartiteness nor the hard-core rule (bipartiteness emerges), and its
  census is by 4-cycle counts and pictures, not by an isomorphism test, so a 14-point piece would have been counted among
  the leftover "ribbon" nodes if it formed. [Kelly22] (pp. 151 to 152): "multiple disconnected copies of the
  d-dimensional hypercube". [KTB19] Sec. 3.3.1 allows "situations where more than one baby universe exists" without
  naming one. [KKVG23] is a different model (chemical potentials for k-cycles on random regular graphs with no hard-core
  rule) and its k = 4 "ideal cluster" is K_{d,d}, which the hard-core rule forbids here; it does not bear on this model.
- **Not found anywhere searched:** a statement that the biplane graph (or any non-hypercube piece) is a ground state
  of the square-counting action, or a census of the λ = 0 cold phase by isomorphism type.

## Verdict

**NOT FOUND** for the physics claim: the sentence may be written as "we have not found it named as a ground-state piece
in the published work on this model or its relatives", linking this note. **FOUND** for the graph theory: the sentence
must also say that the graph is a known object, the unique bipartite (0,2)-graph of valency 4 besides the 4-cube
(Brouwer 2006, via Li and Sun 2025), so what is ours is only its appearance as a tie in this energy and its formation by
itself in about one piece in seven.

What would change the verdict: a full-text search of Google Scholar or INSPIRE (not reachable here); reading Brouwer
(2006) in the original; the text of [GV21]'s Fig. 4 configurations re-read by isomorphism type, which their published
figures do not allow; unpublished work of the model's authors, which no search reaches.
