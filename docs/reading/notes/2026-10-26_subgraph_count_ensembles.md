# Fixing or rewarding a subgraph count: degeneracy, ensemble equivalence and what they say about the square rule (26 October 2026)

**Why this note.** The owner proposes that the six-link toy keep its square count at the flat-space value S = 3N,
either hard (only moves that keep S) or soft (an extra energy μ(S − 3N)², μ scanned). The exact check of VISION
Update 128 found that the perfect flat torus has no single switch keeping S, while damaged states have a few. A
reviewer (Codex) warned that fixing or rewarding the count of a small subgraph is known to make random-graph ensembles
"degenerate": they condense into very ordered or very disordered graphs. This note reads the papers behind that
warning and asks how far they reach a graph like ours: sparse (degree 6, N of about 300), bipartite, every degree fixed,
moves that are degree-preserving switches, and a hard-core rule. It answers four questions: what the degeneracy result
is and its scope; hard against soft (ensemble equivalence); what typical graphs with fixed subgraph densities look like;
and what all this predicts for the soft form at large μ.

**How it was read, and the caveat on every quotation.** Read by an assistant agent on 26 October 2026. Unlike the
timescape note, the papers were downloaded as PDFs from arXiv (or the journal, for [MWW04]) and converted to text with
PyMuPDF; the quotations below were copied from that text, not from a summarizer. Text extraction can drop symbols
(primes, subscripts, ligatures), so formulas are rebuilt by hand and **each quotation should be checked against the
PDF before it reaches a paper or a public page.** Bibliographic details were checked against Crossref
(api.crossref.org) on the same day. The owner has not read any of these passages.

## Sources and how each was read

| Key | Source | How read, 26 October 2026 |
|---|---|---|
| [CD13] | S. Chatterjee, P. Diaconis, "Estimating and understanding exponential random graph models", *Ann. Statist.* **41**(5), 2428–2461 (2013), arXiv:1102.2650, DOI 10.1214/13-AOS1155 | **Read in part**: abstract and Secs. 1 to 7 in full (all theorem statements); Sec. 8 (proofs) not read |
| [PN04a] | J. Park, M. E. J. Newman, "Solution of the two-star model of a network", *Phys. Rev. E* **70**, 066146 (2004), arXiv:cond-mat/0405457, DOI 10.1103/PhysRevE.70.066146 | **Read in full** (five pages). **Correction to the brief:** 066146 is the two-star paper; 066117 is a different paper (next row) |
| [PN04b] | J. Park, M. E. J. Newman, "Statistical mechanics of networks", *Phys. Rev. E* **70**, 066117 (2004), arXiv:cond-mat/0405566, DOI 10.1103/PhysRevE.70.066117 | **Abstract only** (general maximum-entropy framework; nothing specific to the question) |
| [PN05] | J. Park, M. E. J. Newman, "Solution for the properties of a clustered network", *Phys. Rev. E* **72**, 026136 (2005), arXiv:cond-mat/0412579, DOI 10.1103/PhysRevE.72.026136 | **Read in full**. This, not [PN04a], is their paper on the triangle (Strauss) model |
| [Str86] | D. Strauss, "On a general class of models for interaction", *SIAM Rev.* **28**(4), 513–527 (1986), DOI 10.1137/1028156 | **Not reached** (publisher page refused the request). Known here only through [PN05] and [FFPG10] |
| [FFPG10] | D. V. Foster, J. G. Foster, M. Paczuski, P. Grassberger, "Communities, clustering phase transitions, and hysteresis: pitfalls in constructing network ensembles", *Phys. Rev. E* **81**, 046115 (2010), arXiv:0911.2055, DOI 10.1103/PhysRevE.81.046115 | **Read in part**: arXiv v1 (titled "Clustering phase transitions and hysteresis: pitfalls in constructing network ensembles"), Secs. I, II, III.A, III.D, IV; Secs. III.B to III.C (non-regular networks) skimmed. **The closest source to our setting**: fixed degree sequence, switch moves, a reward on a cycle count |
| [SMHG15] | T. Squartini, J. de Mol, F. den Hollander, D. Garlaschelli, "Breaking of ensemble equivalence in networks", *Phys. Rev. Lett.* **115**, 268701 (2015), arXiv:1501.00388, DOI 10.1103/PhysRevLett.115.268701 | **Read in part** (abstract, the unipartite section through Eq. (20)) |
| [dHMRS18] | F. den Hollander, M. Mandjes, A. Roccaverde, N. J. Starreveld, "Ensemble equivalence for dense graphs", *Electron. J. Probab.* **23**, 1–26 (2018), arXiv:1703.08058, DOI 10.1214/18-EJP135 | **Read in part** (abstract, Secs. 1, 2.1, 4 with Theorem 4.1 and its discussion; proofs not read) |
| [RS13] | C. Radin, L. Sadun, "Phase transitions in a complex network", *J. Phys. A* **46**, 305002 (2013), arXiv:1301.1256, DOI 10.1088/1751-8113/46/30/305002 | **Read in part** (abstract, Sec. 1, Theorem 5.1 statement, Sec. 6 Conclusion) |
| [KRRS17] | R. Kenyon, C. Radin, K. Ren, L. Sadun, "Multipodal structure and phase transitions in large constrained graphs", *J. Stat. Phys.* **168**, 233–258 (2017), arXiv:1405.0599, DOI 10.1007/s10955-017-1804-0 | **Read in part** (abstract and introduction) |
| [HCT15] | S. Horvát, É. Czabarka, Z. Toroczkai, "Reducing degeneracy in maximum entropy models of networks", *Phys. Rev. Lett.* **114**, 158701 (2015), arXiv:1407.0991, DOI 10.1103/PhysRevLett.114.158701 | **Read in part** (abstract, first two pages to "The degeneracy problem") |
| [CETT06] | M. Costeniuc, R. S. Ellis, H. Touchette, B. Turkington, "Generalized canonical ensembles and ensemble equivalence", *Phys. Rev. E* **73**, 026105 (2006), arXiv:cond-mat/0505218, DOI 10.1103/PhysRevE.73.026105 | **Read in part** (abstract, Sec. I opening, Sec. V "Gaussian ensemble", Sec. VI). Added because it answers question 4 directly: the soft quadratic form is the "Gaussian ensemble" |
| [MWW04] | B. D. McKay, N. C. Wormald, B. Wysocka, "Short cycles in random regular graphs", *Electron. J. Combin.* **11**, R66 (2004), DOI 10.37236/1819 | **Read in part** (abstract, Sec. 1, Sec. 4 "Bipartite regular graphs"). Added because it says how many squares a random sparse regular bipartite graph has |

## (1) What the degeneracy result is, and its scope

**The theorem.** [CD13] Theorem 5.1 is "the first rigorous proof of the degeneracy observed in exponential graph models"
(Sec. 5). It is about the edge-triangle model on all simple graphs, with weight exp(n²[2β₁·edges/n² + 6β₂·triangles/n³])
(Eq. (5.1)). For β₁ < 0 with |β₁| large enough that c₁ = e^β₁/(1 + e^β₁) < c₂ = 1 + 1/(2β₁), there is a threshold q(β₁)
such that below it the edge density stays under c₁ and above it over c₂: "if β1 is a large negative number, then Gn is
either sparse (if β2 < q) or nearly complete (if β2 > q)". Example: "β1 = −5 gives c1 ≃ 0.007 and c2 = 0.9". The
abstract: "almost all graphs have essentially no edges or are essentially complete." Sec. 5 calls the jump in u* "a
first order phase transition".

**The other regimes, for the record.** With the subgraph parameters nonnegative (reward), the model is "essentially the
same as an Erdős–Rényi graph" with edge probability u*, or a finite mixture of such (Theorem 4.2); the same holds for
small negative parameters (Theorem 6.2: Σ|βᵢ|e(Hᵢ)(e(Hᵢ) − 1) < 2). For a large negative triangle parameter (penalty),
the graph "does not look like an Erdős–Rényi graph" (Theorem 6.3) and tends to a complete (χ(H) − 1)-partite graph with
edges randomly deleted (Theorem 7.1); for triangles that is "a random bipartite graph" (Sec. 1). Note what Theorem 7.1
says for a *bipartite* subgraph H, such as a square: "if H is bipartite, then Gn must be very sparse".

**Scope: dense graphs only, edges free.** The abstract: "A limitation of our approach, inherited from the limitation of
graph limit theory, is that it works only for dense graphs." Dense means edge count of order n² (Sec. 2.2: the graphon
framework "is therefore useful only when p does not tend to zero"). The degeneracy is in the *edge density*, which is
free to move. **Neither condition holds in the toy:** degree 6 is sparse (edge density 6/(N − 1), about 0.02 at N = 300),
and every degree is fixed, so "empty" and "complete" are not available. [CD13]'s theorems do not apply to the toy as
stated.

**What does reach a fixed-degree sparse graph: [FFPG10].** This paper takes exactly the step the reviewer's warning
needs. It fixes the degree sequence ("we fix the exact degree sequence"), samples by degree-preserving rewiring with
Metropolis acceptance (Sec. II.F), and rewards triangles with H = −βn_Δ (Eq. (8)). It had hoped that fixing degrees
would "prevent the extreme condensation of edges typical of the Strauss model". It does not: "For regular graphs
(identical degrees for all nodes) with degree k > 2 we find a single first order transition" (abstract). The
high-reward state is "a disjoint set of (k+1)-cliques" (Sec. III.A.1); n_Δ "first increases proportional to exp(β), but
then the increase accelerates and finally it jumps in a discrete step to a value very close to" that maximum; jumps and
hysteresis appear only "above a k-dependent value of N" (for k = 3, hysteresis for N ≥ 200, not for N ≤ 100; Fig. 1).
And because the graphs are sparse, "The critical values of β increase logarithmically with N": the reason given is that
moves destroying triangles outnumber moves creating them, so "exp(βc) has to increase ∝ N" (Sec. III.A.1). Conclusion
(Sec. IV): "Yet there is still a first order transition for homogeneous networks, i.e. those with fixed degree. In the
phase with strong clustering ... the configuration is basically a collection of disjoint k-cliques."

**[PN05] on the Strauss model, edges free:** the degenerate region "corresponds to a first-order phase transition in
the density of the network" (abstract); it "is a high-density phase ... almost a complete graph" (Sec. IV); and "there
is no intermediate set of parameter values that will give the graph a moderate density of triangles" (Sec. IV). Their
footnote [23] says the solution "should work in the sparse regime also", but the model there still has free edges.
**[PN04a]** (two-star model) is moot for the toy: at fixed degree the number of two-stars is fixed, so a two-star term
is a constant. Its one relevant sentence is about a conserved order parameter, quoted under (3).

**[HCT15] states the general mechanism:** "degeneracy appears when the corresponding density of states function is not
log-concave, which is typically the consequence of nonlinear relationships between the constraining observables"
(abstract).

**Answer.** The rigorous result ([CD13]) is for dense graphs with free edges, and in that form it does not cover the toy.
The warning nevertheless holds in the toy's own setting: [FFPG10] shows, numerically, that a *reward* on a cycle count
with every degree fixed and switch moves gives one first-order jump into disjoint maximally clustered pieces, with
hysteresis, and with a threshold that grows like ln N because the graph is sparse. *(Ours, unverified:* the toy's
squares are the bipartite analogue of [FFPG10]'s triangles, and the toy already shows this behavior. Its λ = 0 end is a
reward on squares alone, and it shatters into hypercube knots with hysteresis, as Gate A, [GV21] and T6's FIRST ORDER
verdict record. So the reviewer's warning describes something the project has already measured in its own model, not a
new risk peculiar to the owner's rule.)* What none of these papers treats is a **target** on the count (penalizing
departures in both directions), which is the owner's rule; see (2) and (4).

## (2) Hard against soft: are the two ensembles equivalent?

**The general criterion.** Equivalence of the microcanonical (hard) and canonical (soft, linear in the count) ensembles
follows from concavity of the microcanonical entropy s(u) in the constrained quantity. [CETT06] Sec. I: "microcanonical
nonequivalent states ... directly arise as a result of the nonconcavity of the entropy function". [RS13] Sec. 6: in
exponential random graph models "the entropy need not be concave" and "Inequivalence can result from the existence of
graphons maximizing se,t for some (e, t) which are not maximizers of ψβ1,β2 for any (β1, β2)". [KRRS17] Sec. 1: "the
microcanonical and grand canonical ensembles are inequivalent ... because the relevant entropy function is not concave
on the phase space, there are large portions of the phase space where the ERGM model gives no information about the
constrained optimal graphons."

**Dense graphs with subgraph constraints ([dHMRS18] Theorem 4.1).** A triangle-density constraint alone: equivalent if
T₂* ≥ 1/8 or T₂* = 0 (case I). Edges and triangles together: equivalent on the Erdős–Rényi curve T₂* = T₁*³ (case
II(a)), but "breaking of ensemble equivalence occurs when the constraints are frustrated" (abstract), i.e. off that
curve (cases II(b) to II(d)). Their open question: "Is s∞ = 0 as soon as the constraint involves a single subgraph count
only?" (Sec. 4).

**Sparse graphs ([SMHG15]).** A fixed number of links: equivalent (Eq. (10)). A fixed degree sequence: not equivalent,
s = ln q(k*) ≥ ln √(2πk*) > 0 (Eq. (18)), so "graphs with a given degree sequence are not" equivalent (abstract);
"ensemble equivalence holds when there is a single global constraint, while it is broken when there is an extensive
number of local constraints." In the toy the degrees are already fixed hard (the switch keeps them), so that particular
nonequivalence is built in and is not what the owner is choosing. Her choice is about one more, global, constraint: S.

**What [FFPG10] found for a target on the count (Sec. III.D).** They tested the model of Milo et al. with
H = β|n_Δ − n_Δ,0| (Eq. (7)), a two-sided penalty around a target, which is the owner's soft form with an absolute
value in place of the square. With it "one neither encounters any of the jumps discussed above nor any hysteresis. But
that does not mean that the method is not plagued by the same basic problem, i.e. extreme sluggish dynamics and
effectively broken ergodicity." After more than 10⁹ attempted swaps, "few changes from the initial configurations are
seen", especially in the strongest clusters. Sec. I: "statistical models with hard constraints show slower relaxation and
worse ergodic behavior than models with soft constraints", and the large-penalty limit "is similar to a model with a
hard constraint". Their workaround was to alternate the constrained moves with unconstrained "annealing periods".

**Answer.** For a single global count, hard and soft (linear) ensembles agree exactly where the entropy curve s(S) is
concave and disagree where it has a dent; graphs make dents common ([RS13], [KRRS17], [HCT15]). The owner's soft form is
not the linear canonical ensemble, though: it is a quadratic penalty, which [CETT06] treats under the name "Gaussian
ensemble" (see (4)), and that ensemble *can* be made equivalent to the hard one even across a dent. *(Ours, unverified,
on the choice:* the papers point to the soft form as the safer one to sample and the hard form as the cleaner one to
define. The hard rule makes "S = 3N" exact, but [FFPG10] III.D and the toy's own exact check (no single S-keeping switch
out of the flat torus) both say it will barely move from where it starts; any verdict from a hard-rule run would be a
verdict about the starting state. The soft form with μ scanned lets S wander by a few squares, which is what lets the
chain move at all, and at large μ it approaches the hard ensemble (see (4)). If the owner wants the hard rule's
definition, the papers' practical route is to run the soft form and keep only the configurations with S = 3N exactly,
as [FFPG10] did when it averaged "only over configurations with exactly n∆,0 triangles".)*

## (3) What do typical graphs with fixed densities look like?

**Dense, edge and triangle densities fixed ([RS13], [KRRS17]).** Entropy maximizers are "multipodal": "a partition of
the vertices into M < ∞ subsets V1, V2, ..., VM, and a set of well-defined probabilities gij of an edge between any
vi ∈ Vi and vj ∈ Vj" ([KRRS17] abstract, proved for edge and k-star constraints; for edges and triangles "evidence, but
not proof"). Near the lowest triangle densities, [RS13] Theorem 5.1 gives a two-part (bipodal) graphon: dense between
the halves, sparse inside them; [RS13] finds "a phase transition between distinct heterogeneous multipartite phases at
low triangle density, and a phase transition between these phases and the disordered phase at high triangle density"
(abstract). [dHMRS18] Sec. 4: in the frustrated region "Graphs drawn from the microcanonical ensemble do not look like
Erdős–Rényi random graphs"; on the scalloped boundary a typical graph is a complete ℓ-partite graph "plus some
additional edges in the last piece that create no additional triangles".

**A conserved count means real coexistence ([PN04a] Sec. III).** With "the number of edges in the graph ... fixed, a
'conserved-order-parameter' version", "the phase coexistence region will correspond to true coexistence": the system
"prefers simultaneously to have some high-degree 'hub' vertices ... and some of lower degree, rather than being uniform
everywhere", which they call "the precise network analog of the phase separation phenomenon". [FFPG10] Sec. IV, with
degrees fixed: "clustering tends to be cooperative. Once many triangles are formed in a certain part of the network,
they help in forming even more."

**The analogue of "paired excess and deficit."** No paper here says it in those words. *(Ours, unverified:* the nearest
published form is the phase separation above. When a global count is pinned at a value inside a dent of s(S), the most
numerous graphs do not hold the count uniformly; they split into regions above the average and regions below it, in the
proportion that makes the total come out right, as a fixed amount of water at the boiling point splits into liquid and
steam. Multipodality is the dense-graph version: a few vertex classes, each with its own density. For the toy, the
regions above the average would be square-rich knots (curled cells, the 6-cube at most) and the regions below would be
square-poor, damaged or random-like wiring. That is excess and deficit in the sense of different places carrying
different counts, not in the sense of a local one-for-one pairing; whether the toy's damaged states show the second
kind as well is the measurement of Update 127, and these papers do not speak to it.)*

## (4) What this predicts for the soft form at large μ

**[CETT06] Sec. V.** A quadratic term γu² in the exponent is Hetherington's "Gaussian ensemble". It satisfies a
"supporting parabola" condition where the ordinary canonical ensemble needs a supporting line, so it reaches states the
canonical ensemble cannot (Fig. 4), and "a single (finite) value of γ can in fact be used to achieve equivalence between
the Gaussian and microcanonical ensembles for all value u in the range of h, provided that (i) γ assumes a large enough
value, basically greater that the largest second derivative of s(u); (ii) that the graph of s(u) contains no corners".
At a corner (a first-order point of the hard ensemble itself), "the Gaussian ensemble with γ < ∞ cannot be applied ...
Such points, however, can be dealt with ... by letting γ → ∞". Their conclusion: "the Gaussian ensemble is a universal
ensemble".

**How many squares a disordered six-link graph has ([MWW04]).** For random d-regular bipartite graphs the cycle counts
are asymptotically independent Poisson with means (d − 1)^c/c for even c (Sec. 4, with μ′ᵢ = (d − 1)^{cᵢ}/cᵢ),
**independent of n**. For squares (c = 4) and d = 6 that is 5⁴/4 ≈ 156 squares in the whole graph, against 3N = 900 at
N = 300. *(Ours, a consistency check: the same formula at d = 4 gives 3⁴/4 = 20.25, which is the "(3⁴/4)/160" random-phase
floor of [T25] recorded in ASSUMPTIONS O5. The published floor is this count.)*

*All of the following is ours, unverified.*

1. **Scaling.** Written per point, μ(S − 3N)² = μN²(φ − 3)², with φ = S/N. The Gaussian ensemble of [CETT06] uses a term
   of order N (γ times an intensive quantity squared, times N); the owner's term is of order N². So at fixed μ the soft
   rule gets stronger, per point, as N grows, and in the large-N limit it behaves as the hard rule with fluctuations of S
   of order 1/√μ squares about the target, not of order √N. A μ that looks "soft" at N = 100 is much harder at N = 300.
   Any μ scan has to say whether μ is held fixed or scaled as 1/N, and the pre-registration should fix that before a run.
2. **Where it collapses.** At large μ the ensemble does **not** collapse onto disordered graphs: disordered six-link
   graphs carry about 156 squares in total, so S = 3N is an extensive distance from them, and the penalty excludes them
   outright. It collapses onto the slice S ≈ 3N, and within that slice the weights are set by the toy's other energy
   terms (λX, and anything else in H) and by how many arrangements each kind of state has. The papers then say two
   things: if s(S) is concave at 3N in the relevant ensemble, the slice is dominated by one homogeneous kind of state;
   if 3N sits inside a dent (T6 found two humps, the signature of a dent, at λ = 0 in four links), the slice is dominated by phase-separated
   graphs (knots plus a square-poor remainder, (3) above). Whether the flat torus wins inside the slice is not decided
   by any of these papers. A perfect torus is a single rigid arrangement up to renaming, and at λ > 1 it is the lowest
   energy, so at low coupling it should dominate; at higher coupling, mixtures with defects have far more arrangements.
   Which wins is a question the toy can answer exactly at small sizes (an enumeration restricted to S = 3N, as in T4)
   before any run.
3. **Dynamics.** [FFPG10] III.D says a two-sided target removes the jumps and hysteresis but leaves "extreme sluggish
   dynamics". With the toy's exact result that the flat torus has no single S-keeping switch, large μ makes the flat
   torus a trap: every move out costs at least μ (one square changes) on top of the usual energy. So at large μ a run
   started flat will stay flat for the same reason a hard-rule run will, and staying flat would not show that the flat
   torus is favored. A run at large μ has to start from both sides (flat, and a damaged or random start) and report
   whether the two meet, as T5 and T6 did.
4. **On the reviewer's warning, restated.** The degeneracy in the literature is the reward case (a linear term
   favoring more of the subgraph), which condenses into knots; the toy has already measured that at λ = 0. The owner's
   rule is a target, not a reward. The literature's warning that carries over to a target is the ergodicity one
   ([FFPG10] III.D) and the phase-separation one ((3) above), not the "empty or complete" one.

## What it does not say

- **No theorem covers our case.** The rigorous results ([CD13], [dHMRS18], [RS13], [KRRS17]) are for dense graphs with
  free edges. [SMHG15] is sparse but constrains degrees or links, not a cycle count. [FFPG10] is the right setting
  (sparse, fixed degree, switch moves, a cycle-count term) but is numerical, uses triangles in non-bipartite graphs, and
  has no hard-core rule. No paper read here treats a 4-cycle count in sparse bipartite regular graphs, a quadratic
  target on any subgraph count in graphs, or the toy's hard-core rule.
- **Nothing here says whether 3N lies inside a dent of the toy's s(S)** at six links. That is a property of the toy and
  has to be computed (the six-link analogue of T6's entropy curve).
- **Nothing here says whether the flat torus or a defected mixture dominates the S = 3N slice**, nor anything about a
  local, one-for-one pairing of excess and deficit.
- [CD13]'s Sec. 8 (proofs), [dHMRS18]'s proofs, [Str86] and [PN04b] beyond its abstract were not read.
- **A prior-work search for rule 15** was not done: this note does not support a sentence saying a square-count target
  "has not been studied".

## Corrections to the brief

- [PN04a] "Solution of the two-star model of a network" is *Phys. Rev. E* **70**, 066146; "Statistical mechanics of
  networks" is **70**, 066117 (Crossref). Their paper on the triangle (Strauss) model, the one that bears on the
  question, is [PN05], *Phys. Rev. E* **72**, 026136 (2005). The two-star model is a constant at fixed degree.
- [FFPG10]'s published title is "Communities, clustering phase transitions, and hysteresis: pitfalls in constructing
  network ensembles" (Crossref); the arXiv v1 read here is titled "Clustering phase transitions and hysteresis: pitfalls
  in constructing network ensembles".
