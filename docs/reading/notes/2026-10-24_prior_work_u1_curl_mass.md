# Prior-work search: a compact direction of length four, counted as a plaquette, gives the field component along it a mass (O151)

*Written on `docs/reading/notes/prior_work_template.md`. Kinds as in CLAUDE.md rule 10.*

**The sentence it backs** (ASSUMPTIONS O151; any later write-up): "This is the known Wilson-line (A5) mass mechanism, by
which a face filling a non-contractible cycle gaps the corresponding link mode, as in Gregoire and Wacker's theory-space
counting. Here the toy's own rule puts it in at tree level. We have not found it stated for a compact direction of
length four on a graph."

**Date of the search:** 24 October 2026.

**Who searched:** two assistant agents with different starting angles (the emergent-geometry side; the lattice-gauge
side) and one checking agent told to refute their verdicts, in a workflow of the assistant session.

## Where was searched

arXiv, ar5iv HTML, the arXiv listing pages and web search. Every search, with its terms:

First agent (emergent-geometry side):
- WebSearch 2026-10-24: 'Trugenberger combinatorial quantum gravity matter fields photons gauge field graph'
- WebSearch 2026-10-24: 'quantum graphity emergent U(1) gauge field string-net Hamma Markopoulou light'
- WebSearch 2026-10-24: 'lattice gauge theory compact dimension size four plaquette Polyakov loop photon mass Kaluza-Klein lattice'
- WebSearch 2026-10-24: 'Caravelli Markopoulou disordered locality Lorentz dispersion relations graph defects photon' (found arXiv:1201.3206, 1309.0311, gr-qc/0702044: dispersion corrections from nonlocal links, no compact direction)
- WebSearch 2026-10-24: 'lattice gauge theory on arbitrary graphs plaquettes defined as all 4-cycles Wilson action cycle basis random graph'
- WebSearch 2026-10-24: 'causal dynamical triangulations coupled to gauge field U(1) Maxwell lattice gauge on dynamical triangulation'
- WebFetch arxiv.org/html/2512.17676 (both parts, offsets 0 and 100000): full-text search for photon/gauge/U(1)/Maxwell/electromagnet/light: none
- WebFetch arxiv.org/abs/2311.17526: abstract, no gauge fields
- WebSearch 2026-10-24: 'Kelly Trugenberger Biancalana emergent electromagnetism photons random graphs Ollivier curvature'
- WebSearch 2026-10-24: 'Maxwell field on causal sets discrete electromagnetism causal set' (Johnston arXiv:1010.5514; Sverdlov causal-set gauge Lagrangians seen only as a listing, no arXiv number seen; hep-th/9712069)
- WebSearch 2026-10-24: 'gauge theory on complex networks random regular graph plaquettes cycles Z2 U(1) gauge random graphs loops of length four'
- WebSearch 2026-10-24: 'lattice action with Polyakov loop term tree-level mass for Wilson line scalar A5 zero mode compact dimension deformation'
- WebSearch 2026-10-24: 'emergent photon polarization along compact direction mass small torus lattice Kaluza-Klein U(1) graph emergent spacetime'
- WebSearch 2026-10-24: 'Myers Ogilvie deformed Yang-Mills lattice Polyakov loop terms added to action center symmetry arXiv'
- WebSearch 2026-10-24: 'Trugenberger 2024 2025 arXiv gauge fields electromagnetism emergent network combinatorial quantum gravity'
- WebSearch 2026-10-24: 'Hamma Markopoulou Lloyd Caravelli Severini Bose-Hubbard evolving graph emergent spacetime arXiv' (arXiv:0911.5075: a matter Hubbard model on an evolving graph, no gauge field)
- WebFetch ar5iv 0801.0861: definition of the emergent U(1) loop operators (even cycles of length L, hexagonal plaquettes; no photon mass, compact direction or Kaluza-Klein)
- WebFetch ar5iv hep-th/0611197 (twice) plus arxiv abs: four-edge loop operators as plaquettes in the low-temperature phase; no wrapping loops, no photon mass

Second agent (lattice-gauge side):
- WebSearch 2026-10-24: 'lattice gauge theory compact dimension length four Polyakov loop plaquette mass photon Kaluza-Klein lattice'
- WebSearch: 'U(1) gauge field on combinatorial quantum gravity graph Trugenberger photon emergent'
- WebSearch: 'lattice gauge theory on arbitrary graphs plaquettes all 4-cycles cycle space formulation'
- WebFetch arxiv.org/abs/hep-th/0010126, then full PDF extracted locally with pypdf and keyword-searched (plaquette, cycle, torus, mass, Wilson, compact, winding, Kaluza, photon, massless, periodic)
- WebSearch: 'quantum graphity emergent U(1) gauge field string-net condensation dynamical graph Hamma Markopoulou'
- WebFetch ar5iv 0801.0861 (which cycles enter, photon mass, compact directions, winding)
- WebSearch: 'lattice action with Polyakov loop term added center symmetry breaking mass for A_4 zero mode deformed Yang-Mills Myers Ogilvie'
- WebSearch: 'Kaluza-Klein on the lattice dimensional reduction gauge field component along compact direction scalar adjoint Higgs zero mode lattice Nt small'
- WebSearch: 'deconstruction moose Wilson line around circle operator Tr(U1 U2 ... UN) potential gives mass pseudo-Goldstone A5 zero mode tree level'
- WebFetch arxiv.org/abs/hep-th/0104005 (abstract only)
- WebFetch ar5iv hep-ph/0202093 (Wilson-loop mass passage; radiative or tree level)
- WebSearch: 'Trugenberger Biancalana Kelly gauge field matter fields on random graphs Ollivier curvature electromagnetism'
- WebSearch: 'Maxwell field on causal set OR emergent network lattice gauge theory on dynamical graph photon propagation emergent spacetime graph'
- WebFetch arxiv.org/abs/2010.15714
- WebSearch: 'lattice torus extent L=2 or L=4 periodic direction trivial plaquette wraps around lattice gauge theory small lattice artifacts Polyakov loop coincides plaquette'
- WebSearch: 'Arkani-Hamed Cohen Georgi electroweak symmetry breaking from dimensional deconstruction plaquette operator mass Wilson line pseudo-Goldstone hep-ph/0105239'
- WebSearch: 'Hodge Laplacian cell complex harmonic 1-forms first homology attaching 2-cell to non-contractible cycle spectral gap lattice Maxwell discrete exterior calculus'

Checking agent: minimal moose plaquette Wilson loop pseudo-Goldstone; lattice small extent Polyakov loop as plaquette, all 4-cycles; Maxwell on graphs (Majid); Hodge Laplacian cell complex torus harmonic mode; Trugenberger gauge photon 2026; U(1) on random regular graph with 4-cycles as plaquettes.

## What came closest

(1) The rule. Filk (arXiv:hep-th/0010126, full text read) defines a gauge theory on an arbitrary graph as S = sum_L h_L Tr tr(A_G)^L, a sum over closed walks of length L, and says graphs have 'no natural analogues for plaquettes'. On a triangle-free graph such as the toy's bipartite ones, keeping only h_4 equals 'every 4-cycle is a square' up to a constant. Filk does not work out what this does on a lattice with a direction of length 4.

(2) The mechanism. Ours, unverified: counting the side-4 ring as a square adds a cos(Polyakov loop) term with the plaquette's own coupling. To second order this is a tree-level mass for the field component along the curl. In Kaluza–Klein language that component is the Wilson-line (A5) scalar, not the photon of the open directions, which stays massless. In ordinary lattice gauge theory, where only elementary plaquettes enter the action, that scalar is massless at tree level and gets a mass only radiatively. Hill and Leibovich (hep-ph/0205057) show this for latticized 5D U(1); Maru and Yamashita (hep-ph/0603237) at two loops; de Forcrand and Kurkela (1003.4643) and Del Debbio and Rinaldi (1203.5627) on the lattice. In deconstruction, the loop round the circle is 'what provides the mass' for that mode (Lane, hep-ph/0202093, reviewing Arkani-Hamed, Cohen and Georgi, hep-th/0104005 and hep-ph/0105239). There it enters as |Tr(U1...UN)|^2 with a radiative coefficient, which is trivial for U(1). The closest published statement of the general principle is Gregoire and Wacker (hep-ph/0206023): light link scalars are the non-contractible cycles of theory space, plaquettes are tree-level potential terms that give mass to the cycles they fill, and a circle with no plaquette keeps a massless scalar. The minimal moose (hep-ph/0206020) uses tree-level four-link plaquettes. Polyakov-loop terms are also put into actions on purpose in centre-stabilized and trace-deformed Yang–Mills (Unsal and Yaffe 0803.0344; Myers and Ogilvie 0707.1869; lattice: Vairinhos 1111.0303, Bonati et al. 1807.06558 and 1912.12028). Those are double-trace or adjoint terms meant to protect centre symmetry, and they are trivial for U(1). In continuum QED on S^1 x R^3, massive polarisation-dependent photon modes appear at one loop (Ferrer and de la Incera, hep-ph/0107229, hep-ph/0408229).

(3) The maths. Ours, an application of standard discrete Hodge theory (Eckmann 1944; Lim, arXiv:1507.05379): harmonic 1-forms count the cycles no 2-cell fills. Making the length-4 ring a face fills a non-contractible cycle and gaps that polarisation. At sides 6 and 8 the ring is not a face and nothing is gapped, which matches O151.

(4) Gauge fields on emergent-geometry graphs. These exist in print, but not on combinatorial-quantum-gravity graphs. Quantum graphity (Konopka, Markopoulou and Smolin, hep-th/0611197) keeps 'loop operators with exactly four edges' on a regular cubic pattern, with a three-valued quantum link and no wrapping loops. Konopka, Markopoulou and Severini (0801.0861) claim an emergent U(1) from an even-cycle loop operator. They note that cycles winding round a tube about 8 edges round lower the graph energy, but they never discuss the gauge spectrum. Compact U(1) and SU(2) on 2D causal dynamical triangulations measure torelons but keep wrapping loops out of the action (Candido et al., 2010.15714, 2112.03157). Trugenberger's 2025 review (2512.17676, full text searched) and the other combinatorial-quantum-gravity papers (1610.05934, 1901.09870, 2311.17526, abstracts only) contain no gauge field or photon.

## Added after the Codex audit (24 October, O154)

Two works the searches missed, bibliographic data checked at Crossref on 24 October, abstracts checked by the Codex
reviewer, not read by us:
- R. L. Renken, S. M. Catterall and J. B. Kogut, "U(1) lattice gauge theory coupled to quantum gravity", Nucl. Phys.
  B Proc. Suppl. 34, 730-732 (1994), doi:10.1016/0920-5632(94)90496-0: a U(1) field coupled to dynamical triangulations
  in three dimensions, the direct precedent for a gauge field on fluctuating geometry, decades before 2010.15714.
- M. Levin and X.-G. Wen, "Quantum ether: Photons and electrons from a rotor model", Phys. Rev. B 73, 035122 (2006),
  arXiv:hep-th/0507118: a bosonic model on a cubic lattice whose low-energy limit has massless U(1) gauge modes and
  Dirac fermions; the published model nearest the particle handoff's aim of photons and fermions from one lattice.

Corrections: A. Romeo is a listed author of hep-ph/0107229 (Ferrer, de la Incera and Romeo; marked unverified above);
arXiv:1003.4643 also lists M. Panero. The verdict stands; the sentence for a write-up should say only that these
searches, on 24 October, did not locate the exact side-four, all-four-cycles combination.

## Verdict

**PARTLY FOUND.** Every ingredient is published; the combination is not, as far as these searches reached.

What we have not found: a lattice or graph gauge theory in which the straight ring round a compact direction of length four enters the action as a plaquette, because it is a 4-cycle, at the plaquette's own coupling. Equivalently, the tree-level mass of 2 in lattice units, omega^2 = 4 + 4 sin^2(k/2), for the polarisation along such a curl as a consequence of the 'every 4-cycle is a square' rule on the toy's 4-regular bipartite graphs. A safe sentence for a write-up: 'This is the known Wilson-line (A5) mass mechanism, by which a face filling a non-contractible cycle gaps the corresponding link mode, as in Gregoire and Wacker's theory-space counting. Here the toy's own rule puts it in at tree level. We have not found it stated for a compact direction of length four on a graph.' Caveats: most items were read at abstract level. The quotations from Filk and Lane were checked against the PDFs. Those from hep-th/0611197, 0801.0861 and hep-ph/0206023 come from ar5iv HTML summaries and should be checked against the PDFs before citing. Romeo as a co-author of hep-ph/0107229 is unverified.

Corrections the checking agent made to the two searches (kept so the next reader does not repeat them): the first
search's NOT FOUND was too strong (it missed Gregoire and Wacker, hep-ph/0206023, and the minimal moose,
hep-ph/0206020); deconstruction does use tree-level plaquettes on theory-space loops; Lane's operator |Tr(U1...UN)|^2 is
trivial for U(1) and radiative, so he is "the same family of operator", not "the same mechanism"; Filk sums closed
walks, not cycles, which equals the 4-cycle rule only on triangle-free graphs such as the toy's; several arXiv numbers
were mislabelled by one search (1302.2196 is a continuum study; 0802.1232, 1406.2549, 2205.04854 and 2201.08993 do not
say what was attributed) and are not used above.
