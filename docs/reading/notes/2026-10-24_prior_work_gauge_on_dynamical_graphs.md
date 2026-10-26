# Prior-work search: a gauge field on a graph that rewires, integrated out, rewards squares and shifts the graph's curled-to-flat change

*Written on `docs/reading/notes/prior_work_template.md`. Kinds of statement as in CLAUDE.md rule 10. This note does
not repeat the searches of `2026-10-24_prior_work_u1_curl_mass.md` (the side-4 ring as a plaquette, the Wilson-line
mass, Filk, quantum graphity's loop operators, the combinatorial-quantum-gravity papers). It backs step 3 of
`docs/design/u1_rewiring_graph_brief_2026-10-24.md`.*

**The sentence it backs** (proposed for the pre-registration of the brief's test (a) or (d), and any later write-up):
"Integrating out a gauge field on a dynamical lattice is known to shift the lattice's own couplings: on dynamical
triangulations it gives a weight per face that renormalizes the cosmological constant and moves its critical value
(Candido et al. 2021; Clemente and D'Elia 2023), and several gauge fields change the phase of 4D dynamical
triangulations (Bilke et al. 1998). We have not found this applied to a graph of fixed size whose square count varies,
where the same weight per square shifts the curling cost and so the curled-to-flat change."

**Date of the search:** 24 October 2026 (`date`: Sat Oct 24 16:42 EDT 2026).

**Who searched:** one assistant agent, in a workflow of the assistant session; no checking agent.

## Where was searched

Web search (US index, which covers arXiv, ar5iv, INSPIRE and journal pages) and WebFetch of arXiv abstract pages, ar5iv
HTML and one PDF (text extracted locally). Every search, with its terms, all on 2026-10-24:

| Source | Terms used | Results looked at | Nearest hit |
|---|---|---|---|
| Web search | 'gauge field on dynamical triangulations backreaction favours geometry phase U(1) coupled 2D quantum gravity' | 10 | arXiv:2307.04547 (2D: the gauge field only renormalizes the cosmological constant); hep-lat/9710077; hep-lat/9304016 |
| Web search | 'Candido Clemente D'Elia Rottoli compact U(1) gauge theory causal dynamical triangulations arXiv 2010.15714' | 9 | arXiv:2010.15714 (JHEP04(2021)184); 2112.03157 |
| WebFetch | arxiv.org/abs/2010.15714 (abstract) | 1 | critical indices independent of the bare gauge coupling |
| WebFetch | arxiv.org/abs/2307.04547, then the PDF, text extracted with PyMuPDF and searched (cosmological, renormali, integrate out, back-reaction, heat kernel, character, shift); Sec. 3.3 read | 1 | the passage quoted below |
| WebFetch | ar5iv.arxiv.org/html/2010.15714 (strong-coupling formula; whether torelons enter the action) | 1 | Sec. IV.2: λ_c(β) = log 2 − β/12 |
| Web search | 'quantum graphity matter coupling Hubbard model emergent geometry trapped surfaces gauge field graph dynamics' | 9 | arXiv:0911.5075, 1108.2013 (matter on an evolving graph, no back-reaction in 1108.2013), 1201.3206 |
| WebFetch | arxiv.org/abs/hep-lat/9710077 (twice: findings; title and authors) | 1 | Bilke et al., Phys. Lett. B418 (1998) 266 |
| WebFetch | arxiv.org/abs/hep-lat/9304016 | 1 | Renken, Catterall, Kogut, Nucl. Phys. B422 (1994) 677 |
| Web search | 'c=1 barrier branched polymers matter coupled to 2D quantum gravity changes geometry phase multiple Ising Potts random surfaces' | 9 | hep-th/9502036, hep-th/9404174, hep-th/9610037, 0806.3506 |
| Web search | 'gauge field on evolving random graph rewiring Monte Carlo joint graph and gauge field plaquettes number of cycles favoured' | 9 | none on point (1212.2875 is gauge theory as random surfaces on a fixed lattice) |
| Web search | 'Christ Friedberg Lee random lattice gauge theory 1982 Nuclear Physics weights random lattice dynamical' | 9 | Nucl. Phys. B202 (1982) 89, seen only as a citation; hep-lat/0602021 describes its action |
| Web search | 'Kazakov 1986 Ising model on random planar lattice exact solution third order transition Boulatov Kazakov' | 10 | secondary sources only (cond-mat/0207573, 1108.6269, 2511.03688) |
| Web search | 'two-dimensional Yang-Mills on random triangulation integrated out heat kernel weight per face area dependence dynamical triangulation strong coupling cosmological constant' | 9 | none on point |
| Web search | 'Trugenberger 2025 2026 arXiv combinatorial quantum gravity matter fields coupled network Ollivier curvature emergent particles' | 9 | arXiv:2409.09385 (dark sector, no gauge field); nothing newer found |
| WebFetch | arxiv.org/a/trugenberger_c_1 (author listing) | 0 | HTTP 404; the listing was not seen |
| Web search | '"dynamical lattice" OR "dynamical graph" lattice gauge theory backreaction graph connectivity emergent geometry Z2 gauge rewiring edges simulation' | 10 | arXiv:2605.16316 (Z2 on spin networks; abstract does not mention rewiring); 2512.22072; two unrefereed Research Square preprints, not used |
| WebFetch | arxiv.org/abs/2605.16316 | 1 | as above |
| Web search | 'Bianconi topological Dirac Maxwell field on network geometry coupled dynamics emergent geometry gauge field simplicial complex 2024' | 9 | arXiv:2106.02929 (Dirac operator on fixed networks; no gauge field, no rewiring) |
| Web search | 'quantum graphity gauge field emergent U(1) plaquette energy favours loops lattice formation Konopka Markopoulou Severini string-net dynamical graph backreaction' | 10 | hep-th/0611197, 0801.0861 (already in the earlier note) |
| Web search | 'Ising model coupled to exponential random graph annealed network joint Hamiltonian spins and edges phase transition network structure changes' | 9 | 1406.7031, 1509.07327 (annealed Ising on random graphs; the graph's own phase is not the question) |
| Web search | 'c=-2 matter spanning trees random planar lattice Gaussian field integrated out determinant Laplacian weight on dynamical graphs Kazakov Kostov' | 9 | 0903.4432, 1608.02916 |

Not searched: Google Scholar, INSPIRE's own search interface, and forward citations of 2010.15714 and hep-lat/9710077
(the obvious next step). arXiv full-text search was not used directly.

## What came closest

1. **Candido, Clemente, D'Elia and Rottoli, "Compact Gauge Fields on Causal Dynamical Triangulations: a 2D case study",
   arXiv:2010.15714, JHEP04(2021)184.** Read: abstract, and Sec. IV.2 and IV.3 through an ar5iv summary (not the PDF).
   Published, as summarised: U(1) and SU(2) on the dual links of 2D CDT on a torus; the critical cosmological constant
   moves with the gauge coupling, estimated at strong coupling as λ_c(β) = log 2 − β/12, which fits their data for
   β ≲ 1; the critical index ν = 0.496(7) does not move. Torelons are observables only and are not in the action.
   *Why it does not already do it:* in a triangulation the number of plaquettes is the volume, so a weight per plaquette
   can only renormalize the cosmological constant. In the toy, N is fixed and the number of squares changes with the
   arrangement, so the same kind of weight moves the curvature term and the curling cost instead. No decompactification
   is studied there.
2. **Clemente and D'Elia, "Spectral Observables and Gauge Field Couplings in Causal Dynamical Triangulations",
   arXiv:2307.04547.** Read: Sec. 3.3 in full from the PDF (text extracted locally). Quoted exactly: "the coupling to
   gauge fields just renormalizes the cosmological constant and shifts its critical value, leaving critical indices
   unchanged"; "it is known that two-dimensional gauge fields can be easily integrated away [43, 44, 45]. Nevertheless,
   on a curved geometry one is left with a non-trivial contribution, depending on the coordination numbers"; and "the
   presence of gauge fields modifies gravity just by an additive renormalization of the cosmological constant ... the
   situation could be quite different in higher dimensions." Their Fig. 15 sets the measured λ_c(β) for U(1) and SU(2)
   against the strong-coupling prediction. *This is the published form of the brief's leading order:* integrate out the
   field, get a weight per face, read it as a shift of a coupling of the geometry. It is the same mechanism, on a
   different object.
3. **Bilke, Burda, Krzywicki, Petersson, Tabaczek and Thorleifsson, "4d Simplicial Quantum Gravity Interacting with
   Gauge Matter Fields", hep-lat/9710077, Phys. Lett. B418 (1998) 266.** Read: abstract only (through WebFetch).
   Published, as summarised: one non-compact U(1) field back-reacts weakly on the geometry; with more than two fields the
   branched-polymer phase gives way to a new phase with negative string susceptibility exponent and fractal dimension
   near 4. A search summary (not read by us) reports a later suggestion that this depends on putting the field on links
   or dual links. *Why it does not already do it:* 4D triangulations, non-compact fields, and no curled direction or
   square count.
4. **Renken, Catterall and Kogut, "Three-Dimensional Quantum Gravity Coupled to Gauge Fields", hep-lat/9304016,
   Nucl. Phys. B422 (1994) 677.** Abstract only. U(1) on 3D dynamical triangulations; mean-field theory predicts a
   confinement transition in both curvature phases, simulations find none. A case where the field did not change the
   phase picture.
5. **Matter changing the geometry's phase: the c = 1 barrier.** Kazakov's Ising model on random planar lattices (1986)
   and its Boulatov–Kazakov extension (seen only through secondary sources: cond-mat/0207573, 1108.6269, 2511.03688;
   the original papers not seen, references to verify). Multiple Ising copies on dynamical φ³ graphs, where enough
   matter drives the surfaces into a branched-polymer phase (Harris and Wheater, hep-th/9404174; Harris,
   hep-th/9502036 and hep-th/9610037; search summaries only). Ising and Potts on CDT keep flat-space exponents
   (arXiv:0806.3506, summary only). And c = −2 matter, whose integrated-out Gaussian weight is the spanning-tree count
   (Caracciolo and Sportiello 0903.4432, Caracciolo, Sokal and Sportiello 1608.02916; summaries only; the
   determinant–spanning-tree link is general knowledge, to verify). These are the published examples of "integrating out
   the matter weights each graph by a graph quantity and can move the geometry's phase". None uses a gauge field on a
   graph whose square count varies.
6. **Quantum graphity with matter.** Hamma et al., arXiv:0911.5075 (Bose–Hubbard on an evolving graph) and 1108.2013
   (trapped surfaces, solved explicitly without back-reaction of matter on the lattice; summaries only). Konopka,
   Markopoulou and Severini 0801.0861 (an emergent U(1) as a property of the graph's ground state, not a field coupled
   to it; covered in the earlier note). Not a gauge field integrated out to change the graph's phase.
7. **Not on point.** Christ, Friedberg and Lee, Nucl. Phys. B202 (1982) 89 (random lattices with a triangle action
   weighted by areas; a fixed random lattice in its usual use; seen only as a citation, through hep-lat/0602021). Vaid,
   arXiv:2605.16316 (Z2 on spin networks; the abstract says nothing about rewiring). Bianconi, arXiv:2106.02929 (Dirac
   operator on fixed networks). Annealed Ising on random graphs (1406.7031, 1509.07327), where the question is the
   spins, not the graph. Trugenberger's papers to 2409.09385 contain no gauge field as far as these abstracts show;
   his arXiv listing was not reachable.

**A point the reading raises for the brief (ours, exact).** In 2D CDT the shift comes from the constant part of the
plaquette action (Candido et al.'s β N₂/12). The same is true in the toy: the brief writes the field's energy two ways,
κ Σ (1 − cos φ) or the weight exp(β Σ cos φ), and when the number of squares P changes with the wiring these differ by
the factor exp(−βP). With the weight exp(β Σ cos φ), integrating out gives I₀(β) per square, a reward. With the energy
(1 − cos φ), it gives e^(−β) I₀(β) per square, and since I₀(β) < e^β for every β > 0 this is a penalty: the field then
favours fewer squares, the flat sheet over the tube, and raises the curling cost. So the sign of the brief's effect is
set by where the zero of the plaquette energy sits, which is a choice to be made and recorded under S1 before the
prediction is registered. It is the toy's version of "renormalizes the cosmological constant".

## Verdict

**PARTLY FOUND.** The mechanism is published: integrating out a gauge field on a dynamical lattice gives a weight per
plaquette that shifts the lattice's own couplings and moves a critical value, measured against a strong-coupling
prediction in 2D CDT (2010.15714; 2307.04547, read in part), and matter fields that move a random geometry's phase are
textbook (the c = 1 barrier; 4D DT with several gauge fields). What we have not found: a gauge field on a graph of fixed
size whose number of plaquettes changes with the wiring, so that the integrated-out weight acts on the curvature term,
and its effect on a curled-to-flat (decompactification) change. The pre-registration may say: "This is the known
effect of integrating out a gauge field on a dynamical lattice (Candido et al. 2021; Clemente and D'Elia 2023), applied
to a graph whose square count varies; we have not found it applied to such a graph, nor to a curled-to-flat change." It
must not say the reward for squares is new.

Caveats. One agent searched; no checking agent was run (rule 15 asks for the search, not a second agent, but the
earlier note's checker found real misses). Only 2307.04547 Sec. 3.3 was read from the PDF; everything else is abstract or
summary level, and the ar5iv summary of 2010.15714 must be checked against the PDF before its formula is quoted.

What would change the verdict: forward citations of 2010.15714, 2307.04547 and hep-lat/9710077 (a later paper may put
a gauge field on CDT with a compact direction, or on a graph model); an INSPIRE search for gauge or matter fields on
"random regular graphs" with switch moves; the full text of Trugenberger's recent papers and his arXiv listing; and
the three references [43, 44, 45] of 2307.04547 on integrating out 2D gauge fields, which may already state the
curved-geometry correction in the form the brief's surface terms need.
