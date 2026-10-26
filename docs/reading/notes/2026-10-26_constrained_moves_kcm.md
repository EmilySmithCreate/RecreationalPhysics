# Kinetically constrained models against the owner's "hard rule": reading notes (26 October 2026)

**Why this note.** The owner adopted a "hard rule" for the six-link toy: the total square count S must stay exactly at
3N, the flat-space value, so only switches (or groups of switches) that keep S fixed are allowed; the soft alternative
adds an energy μ(S − 3N)². Exact checks (VISION Update 128) found that from the perfectly flat 6 × 6 × 8 torus no single
switch keeps S (every one loses 4 to 8 squares) and no pair of switches within two links restores S except undoing the
first, while damaged states after a big push have a few count-keeping switches (about 42 in 274,000). So under the
hard rule clean ordered space is frozen and only damaged regions move. The owner must choose among (a) the soft form,
(b) the hard rule with longer compound moves (a search for three-switch moves), and (c) the hard rule started from
damaged states. This is the situation studied for forty years under the name "kinetically constrained models" (KCMs),
and, for graphs, under "edge-swap irreducibility". This note reads that literature for what it says about the three
options. It is reading, not a decision; nothing here has been run.

**How it was read, and the caveat.** Read by an assistant agent on 26 October 2026. The main source, [RS03], was
downloaded from arXiv as a PDF and converted to text locally, so its quotations below are from the authors' text
directly, not from a summarizer; symbols (c, f, d, m, τ0) are retyped from that conversion and should be checked
against the PDF before they reach a paper. [Nis17] was read the same way. Everything else is abstract-only or
reported through [RS03], as the table says. The owner has not read any of these passages.

## Sources and how each was read

| Key | Source | How read, 26 October 2026 |
|---|---|---|
| [RS03] | F. Ritort, P. Sollich, "Glassy dynamics of kinetically constrained models", *Adv. Phys.* **52**(4), 219–342 (2003), arXiv:cond-mat/0210382, DOI 10.1080/0001873031000093582 (Crossref checked) | **Read in part**, arXiv v2 PDF (137 pp.): abstract; Sec. 1 (pp. 3–4); a passage of Sec. 2.4 (pp. 16–17); Sec. 3 introduction; Secs. 3.1, 3.1.1, the opening of 3.1.2 (pp. 20–28); the end of 3.2 and Sec. 3.3 with the opening of 3.3.1 (pp. 32–37); the end of 3.5, Secs. 3.6, 3.7 introduction, 3.7.1, the opening of 3.7.2, 3.7.4 (pp. 43–45, 49); Sec. 4 introduction, Sec. 4.1, the opening of 4.2 (pp. 52–56); Sec. 5 introduction and Sec. 5.1 (pp. 75–78). **Not read:** Secs. 2.1–2.3, 2.5–2.6, 3.4, most of 3.5 and 3.7, 4.3–4.10, 5.2–5.7, 6 |
| [FA84] | G. H. Fredrickson, H. C. Andersen, "Kinetic Ising model of the glass transition", *Phys. Rev. Lett.* **53**(13), 1244–1247 (1984), DOI 10.1103/PhysRevLett.53.1244 (Crossref checked) | **Not reached** (APS returned 403; Crossref has no abstract). What is said of it here is what [RS03] says |
| [Kaw66] | K. Kawasaki, "Diffusion constants near the critical point for time-dependent Ising models. I", *Phys. Rev.* **145**(1), 224–230 (1966), DOI 10.1103/PhysRev.145.224 (Crossref checked) | **Not reached** (paywalled; Crossref has no abstract). What is said of Kawasaki dynamics here is what [RS03] Sec. 3.2 says |
| [KA93] | W. Kob, H. C. Andersen, "Kinetic lattice-gas model of cage effects in high-density liquids and a test of mode-coupling theory of the ideal-glass transition", *Phys. Rev. E* **48**(6), 4364–4377 (1993), DOI 10.1103/PhysRevE.48.4364 (Crossref checked) | **Not reached**; reported through [RS03] Secs. 3.3, 5.1 (its ref. [88]) |
| [TBF04] | C. Toninelli, G. Biroli, D. S. Fisher, "Spatial structures and dynamics of kinetically constrained models of glasses", *Phys. Rev. Lett.* **92**(18), 185504 (2004), arXiv:cond-mat/0306746, DOI 10.1103/PhysRevLett.92.185504 (Crossref checked; Crossref gives no page range beyond the article number) | **Abstract only** (arXiv) |
| [TBF05] | C. Toninelli, G. Biroli, D. S. Fisher, "Cooperative behavior of kinetically constrained lattice gas models of glassy dynamics", *J. Stat. Phys.* **120**(1–2), 167–238 (2005), arXiv:cond-mat/0410647, DOI 10.1007/s10955-005-5250-z (Crossref checked) | **Abstract only** (arXiv) |
| [DS98] | P. Diaconis, B. Sturmfels, "Algebraic algorithms for sampling from conditional distributions", *Ann. Statist.* **26**(1), 363–397 (1998), DOI 10.1214/aos/1030563990 (Crossref checked) | **Abstract only** (from Crossref). Project Euclid returned an empty page; the 1993 ZIB preprint (SC-93-17) sits behind a bot challenge, which was not bypassed |
| [Nis17] | J. Nishimura, "Swap connectivity for two graph spaces between simple and pseudo graphs and disconnectivity for triangle constraints", arXiv:1704.01951 (2017), 7-page note. This is the repo's `[Swap17]` | **Read in full** (arXiv v1 PDF). No journal version found at Crossref (one query, 26 October) |
| [TRC11] | L. Tabourier, C. Roth, J.-P. Cointet, "Generating constrained random graphs using multiple edge switches", *ACM J. Exp. Algorithmics* **16** (2011), DOI 10.1145/1963190.2063515 (Crossref checked; no page range given) | **Abstract only** (from Crossref) |

## 1. How a local constraint freezes order and leaves defects mobile ("facilitation")

**The mechanism, in the founding model.** [RS03] Sec. 3.1 describes the Fredrickson–Andersen spin-facilitated models
(the "f, d-SFM"): two-state variables nᵢ = 0, 1 on a d-dimensional lattice, where "an up-spin nᵢ = 1 represents a
mobile, low-density region", and "the facilitation constraint is formalized by requiring that a spin can flip only if
at least f ≥ 1 of its n.n.s are in the mobile state nᵢ = 1" (Eq. (26)). With the trivial energy E = Σᵢ nᵢ (Eq. (28)),
"at low temperatures the equilibrium concentration ceq = ⟨nᵢ⟩ of up-spins, i.e. mobile regions, becomes small ... Only
a very small number of spins will then have f or more up-spin neighbours, while all other spins will be effectively
frozen until enough of their neighbours flip up. The kinetic constraint thus creates a dynamical bottleneck" (pp.
21–22).

**Two families.** [RS03] Sec. 3.1.2: "In models with undirected constraints and f = 1 (one-spin facilitated models),
relaxation occurs primarily by the diffusion of defects ... All other models—i.e. the f, d-SFMs with f > 1 and the
models with directed constraints—require cooperative processes for relaxation to occur." The first give Arrhenius
("strong glass") timescales, τ ∼ c^(−1−2/d) (Eq. (34)); the second much steeper growth ("fragile glasses"). The same
split appears in the lattice versions of cellular structures (Sec. 3.5, p. 43): a "+1-spin and a −1-spin" dimer
"can diffuse ... across a background of largely 0-spins"; "isolated defects themselves can diffuse by creating freely
diffusing dimers at an energy cost of ∆E = 2."

**Conserved versions.** In the Kob–Andersen lattice gas ([RS03] Sec. 3.3), particles hop to empty neighbouring sites
"subject to the condition that the particle has fewer than m occupied neighbour sites both before and after the move";
there "all allowed configurations have the same energy and the same Boltzmann weight so the energy landscape is
trivial", and the slowness comes entirely from the constraint. Mobility is carried by vacancies: the triangular
lattice gas with one-vacancy assistance loses its glassy features because "pairs of vacancies can then diffuse freely
even in an otherwise fully occupied lattice" (p. 35). [TBF04] abstract: "In finite dimensions there exist rare mobile
elements that destroy the transition. At low vacancy density, v, the spacing, Ξ, between mobile elements diverges
exponentially or faster in 1/v."

**Does it match "clean space frozen, damaged space moves rarely"?** *Ours, unverified.* In shape, yes: the flat torus
plays the part of the all-down state of the FA model or the fully packed lattice of Kob–Andersen, and defects
(damaged points) play the facilitators. Two differences matter. (i) In KCMs the constraint is imposed and the energy
is trivial; in the toy the "constraint" (keep S) is a conserved quantity, so the closer KCM analogues are the
conserved ones (Kob–Andersen; Kawasaki dynamics; Skinner's constant-energy chain, below), not the FA model. (ii)
Whether the toy is in the "defects diffuse" family (f = 1-like: a damaged region can move as a unit, Arrhenius,
effectively irreducible) or the "cooperative" family (several defects must meet; super-Arrhenius, strong finite-size
reducibility) is not known; 42 count-keeping switches in 274,000 says moves exist near damage, not whether a defect
can carry itself across clean space. That is the measurement that tells the families apart (Sec. 4 below).

## 2. Ergodicity and irreducibility: when a constrained move set splits the state space

**Definitions.** [RS03] Sec. 3.1.1: the Boltzmann distribution "is guaranteed to describe the unique equilibrium
state ... under two conditions: that the dynamics obeys detailed balance w.r.t. the energy function E, and that the
dynamics is irreducible. Irreducibility means that the system can pass from any configuration to any other by some
finite number of 'allowed' transitions". With constraints, "configuration space split[s] into mutually inaccessible
partitions"; "if the system is started off in a configuration in a given partition, it will equilibrate to the
Boltzmann distribution in that partition only". Irreducibility is a static, temperature-independent notion: "the
value of T never changes an allowed transition into a forbidden one, as long as T > 0—and ... the different mutually
inaccessible partitions of configuration space have no interpretation as thermodynamic phases" (p. 26). Ergodicity is
the stronger, timescale notion (paths that keep "sufficient statistical weight in the thermodynamic limit").

**Isolated ordered states are normal, and not fatal by themselves.** [RS03] p. 24, for the 1, d-SFM: "the
configuration with all spins down ... allows no transitions at all to other configurations since no facilitating
up-spins exist; it forms a partition on its own." This is called "rather trivial" reducibility because that partition
is a vanishing fraction (2^(−N)) of states, and the model is "effectively irreducible": the fraction p(c, N) of
configurations at concentration c in the dominant partition tends to 1 as N → ∞ at every c > 0 (Eq. (33) and the
definition after it). Strong reducibility also exists: "for f > d ... p(c, L → ∞) = 0 for any c < 1"; e.g. in the
3, 2-SFM "any 2 × 2 square of down-spins can never be flipped up whatever the state of the neighbouring spins" (Sec.
4.1, p. 54); and Kob–Andersen with m = 3 is "strongly reducible: any set of eight particles occupying the sites of a
2 × 2 × 2 cube could never move" (p. 34).

**How it is shown.** [RS03] Sec. 4.1: (i) a cellular-automaton test — flip every mobile spin, iterate, and ask whether
the end state is the fully mobile one; this maps exactly onto bootstrap percolation; (ii) "large void instabilities"
or "critical droplets": a mobile region large enough grows to fill the system with probability near one, so one such
nucleus somewhere suffices (Eqs. (54)–(56)); (iii) for lattice gases, the "backbone": iteratively remove every mobile
particle; whatever remains is permanently frozen (pp. 55–56; simulations "suggest that ... the number of particles in
the backbone was found to be a very good approximation to the number of particles that remained blocked"). Rigorous
results: Schonmann proved effective irreducibility for 2 ≤ f ≤ d (Sec. 5.1). [TBF05] abstract: for Kob–Andersen on
hypercubic lattices "only two behaviors are possible ...: either ergodicity at all densities or trivial
non-ergodicity, depending on the constraint parameter and the dimensionality."

**Finite size is the trap.** [RS03] p. 26: the threshold c*(N) above which a finite system is effectively irreducible
"will often converge to zero only very slowly, e.g. logarithmically in N"; for the 3, 3-SFM c*(L) ∼ 1/ln(ln L), so
"even for a macroscopic L = 10^10 (say) the thermodynamic limit is not yet reached and the system will show strong
reducibility effects below some nonzero c*(L)" (p. 55). For Kob–Andersen the size needed "diverges as a double
exponential of 1/(1 − c)" (p. 37).

**Conserved dynamics and move size.** The review does **not** state a general theorem that conserved (Kawasaki-type)
dynamics needs moves of a given size. What it says of Kawasaki dynamics ([RS03] Sec. 3.2, p. 33): it "can be thought
of as a kind of kinetic constraint. It does give rise to some glassy features, e.g. freezing into non-equilibrium
domain structures when the system is cooled sufficiently rapidly"; and the Kob–Andersen model "is actually very
similar to a 3,3-SFM with Kawasaki dynamics" (p. 34). Two passages bear directly on a fixed-count rule:
- **Skinner's constant-energy chain** (p. 33): spins "can flip only if they have exactly one up and one down
  neighbour. This is equivalent to evolution at constant energy, leading to a random walk of a fixed number of domain
  walls that can neither cross nor annihilate. Because of the fixed energy restriction, the model cannot be used to
  study out-of-equilibrium relaxation". This is the review's nearest case to "S must stay fixed".
- **The opposite rule is also reducible** (p. 33): forbidding energy-conserving flips, "Even at T > 0, the constraint
  that the energy must change in a move is strong enough to make the dynamics reducible; a domain of an even number of
  up-spins surrounded by all down-spins, for example, can never be eliminated."
- **A reservoir cures much of it** (pp. 35, 77): letting particles exchange with a reservoir in one plane means
  "many more configurations become mutually accessible, if necessary by first removing particles one by one and then
  reinserting them; this significantly weakens reducibility effects", and "In some cases this makes the dynamics fully
  irreducible."

**For graphs with a fixed count, the direct result is [Nis17].** Degree-preserving double edge swaps connect all
simple graphs of a degree sequence (its refs. [14] = Taylor 1981 and others). Adding a fixed triangle count breaks
this: [Nis17] Sec. 4, for degree sequence {3, 3, 3, 3, 2, 2, 2, 2} with 4 triangles, "this degree sequence has exactly
2 isomorphism classes with 4 triangles and thus it then immediately follows that the associated graph of graphs is
disconnected for k edge-swaps for k < 8 since there are 8 different edges between the two isomorphism classes"
(Fig. 1; Figs. 2 and 3 give two more examples, for fixed triangle *sequences*). Its conclusion: these examples "are
more worrying from a practical standpoint", and "whether the demonstrated problems with k edge-swaps pose a fundamental
limitation not only to sampling with strict constraints, but also to importance weighted or biased samplers is worth
considering." It cites [TRC11] for k-edge swaps ("selecting k edges and cyclically permuting one endpoint in each
edge") with numerical evidence that "3 edge-swaps and 4 edge-swaps are effective at sampling simple graphs with a
constrained number of triangles" for some degree sequences. [TRC11] abstract: "in general, it is not necessarily
possible to access all graphs obeying some given constraints through a classical switching procedure calling on pairs
of edges", and k-edge switching "makes it possible to progressively improve the covered portion of a set of
constrained graphs".

**Markov bases.** [DS98] abstract: "We construct Markov chain algorithms for sampling from discrete exponential
families conditional on a sufficient statistic ... The algorithms involve computations in polynomial rings using
Gröbner bases." *General knowledge, not read by us, to verify against the paper:* a "Markov basis" is a finite set of
moves that connects every fiber {x : T(x) = t}, and the theory guarantees one exists and computes it when T is linear
in the cell counts (a toric ideal); its moves can be large. *Ours, unverified:* the square count S is a quartic
function of the edge indicators, not a linear statistic, so the toric-ideal guarantee would not apply as stated; and
on a finite space some finite connecting move set trivially exists, the question being only whether it is local. That
is exactly the question [Nis17] answers in the negative for triangles.

## 3. Hard constraint against soft penalty; kinetic constraint against state-space restriction

**A pure kinetic constraint leaves equilibrium alone.** [RS03] abstract: KCMs "have trivial, often non-interacting,
equilibrium behaviour but interesting slow dynamics due to restrictions on the allowed transitions between
configurations." Sec. 3.1, p. 21: "the fact that some rates are zero due to the kinetic constraint does not break
detailed balance, since a transition and its reverse transition are always forbidden together." With irreducibility
(effective, in the large-N sense), the Boltzmann distribution over **all** configurations is the equilibrium (Sec.
3.1.1); without it, Boltzmann within one partition.

**The hard S rule is not a pure kinetic constraint.** *Ours, unverified, but it follows from the definitions just
quoted.* A KCM forbids transitions and leaves the set of states and their weights alone. "S must stay at 3N" forbids
*states*: it changes the ensemble from all valid graphs to the fiber S = 3N, as fixed particle number does in
Kob–Andersen and fixed energy does in Skinner's chain. Within that fiber, H = 16(3N − S) + 4λX reduces to 4λX + const,
so the hard-rule chain samples exp(−4λX/g) restricted to the reachable part of the fiber. Two separate questions
therefore have to be answered for option (c), not one: which ensemble (the fiber), and which partition of it the moves
reach.

**Soft penalty against hard rule.** [RS03] p. 26, citing [KA93]: "one could consider a weaker form of kinetic
constraints where the notionally forbidden transitions take place with a very small rate 1/τ0. As long as τ0 is
finite, the connectivity of configuration space is the same as that for an unconstrained model and so the dynamics is
trivially irreducible. On the other hand, the dynamical evolution of the system should be independent of τ0 for times
t ≪ τ0". And the converse direction, energy producing constraints: Sec. 3.6, "a class of models which are
conventionally formulated in terms of nontrivial energy functions and unconstrained dynamics ... can be mapped to
noninteracting defects with constrained dynamics"; in the triangle model "flipping any triangle of defect variables
then leads to a state with an additional defect, and requires an activation over the energy barrier 2J", and "these
kinetic constraints are not imposed ad hoc, but result naturally from the dynamics of the underlying spin system"
(pp. 44–45). Sec. 1, p. 4: "a change in the dynamical rules corresponds to a nontrivial modification of the underlying
microscopic model, e.g. by adding new interaction terms to the energy function", and "a relatively minor change in
these rules can alter the resulting behaviour quite dramatically" (directed against undirected constraints).

*Ours, unverified.* So the literature treats a hard constraint and a steep energy barrier as the same dynamics on
times short compared with the barrier-crossing time, and different in connectivity. The soft form μ(S − 3N)² differs
from [KA93]'s weak constraint in one respect: it is an energy, so it also changes the equilibrium weights (S
fluctuates about 3N with a spread set by g/μ), whereas the weak kinetic constraint keeps the same energy. As μ → ∞ the
soft form's equilibrium tends to the hard fiber; whether the two ensembles agree on the observables of interest at
finite μ is the standard question of ensemble equivalence (general knowledge, to verify), which can fail near a
first-order change.

## 4. What this literature predicts for options (a), (b), (c), and what would tell them apart

*Everything in this section is ours, unverified: an application of the passages above to the toy.*

**(a) The soft form.** Predicted: irreducible (the [KA93] weak-constraint argument), equilibrium = Boltzmann in
H + μ(S − 3N)² over all valid graphs. Clean space is no longer frozen but is activated: the cheapest exit from flat
space loses 4 squares, so it costs at least 16μ (plus the existing 16 per square), and the rate of leaving clean space
falls as exp(−16μ/g) or faster. For times short compared with that, the soft chain should look like the hard one;
after it, like a chain with a stiff spring on S. **Measurement:** run the soft chain at several μ and fit the waiting
time to the first move out of a clean torus against μ/g (an Arrhenius line in μ predicts the barrier-crossing picture);
and compare averages of X and of local dimension between soft runs restricted to S = 3N and hard-rule runs on the same
fiber.

**(b) The hard rule with three-switch (or longer) moves.** Predicted: possibly still no local count-keeping move out
of the flat torus. [Nis17] shows fixed-cycle-count spaces needing swaps on 8 or more edges; [TRC11] shows k-switches
improving coverage gradually, without a guarantee. If the flat torus remains a partition on its own under k-switches,
it is the review's "all-down" state: harmless for equilibrium if it is a vanishing fraction of the fiber, but then the
hard rule can never start from clean space. **Measurement:** exhaustive count of count-keeping k-switches out of the
flat 6 × 6 × 8 torus for k = 3 (and 4 if affordable), by locality radius, with the "undo" moves excluded; zero at every
radius is the isolated-partition outcome. At sizes small enough to enumerate (the T4 machinery, `small_graphs.explore`),
count the partitions of the S = 3N fiber under each move set, as [Nis17] did for triangles.

**(c) The hard rule from damaged states.** Predicted: the chain equilibrates within whatever partition the damaged
start lies in, and results can depend on the start; reducibility can be strong at low defect density and converge
slowly with size (c*(N) ∼ 1/ln N or slower in the KCM examples). If damage can travel as a unit (the f = 1, "diffusing
defect" family), clean regions are eventually visited and timescales are Arrhenius; if several damaged regions must
meet (the cooperative family), clean regions stay frozen for super-Arrhenius times and finite-size effects are severe.
A further question the review raises in its own terms: whether the push-damaged states even have S = 3N; if not, the
hard rule fixes them on a different fiber. **Measurements:** (1) a "backbone" in the review's sense: repeatedly apply
every count-keeping move available and record which points or links are never touched; the fraction never touched,
against defect density and N, is p(c, N); (2) the mean-squared displacement of a damaged region's centre against time
(diffusing: linear in time; cooperative: stuck until another defect arrives); (3) the persistence function, the share
of points that have not changed by time t, from several damaged starts with the same S, to see whether they reach the
same averages (one partition) or not (several).

**What tells (a), (b), (c) apart at once:** whether the flat torus belongs to the same partition as the damaged states
under the chosen move set. Under (a) it does by construction; under (b) only if some k-switch connects them; under (c)
not under single switches and local pairs, by the exact checks of Update 128.

## What the sources do not say

- None of them treats a graph with a fixed **square** (4-cycle) count, or a hard-core rule on shared neighbours; [Nis17]
  treats triangles. The step from triangles to squares is ours.
- [RS03] gives no general theorem on the move size needed for conserved dynamics; its conserved examples are lattice
  gases and Ising chains with particle or energy conservation.
- [RS03] does not compare a hard constraint with a soft *energy* penalty on a conserved quantity; it compares a hard
  kinetic constraint with a small finite rate for the forbidden moves, and energy barriers with effective constraints.
- [DS98] was not read; nothing here establishes what it says about non-linear statistics.
- [FA84] and [Kaw66] were not reached; everything said of them is [RS03]'s account.
- The sections of [RS03] on relaxation times, dynamical heterogeneity and aging (Secs. 5.2–5.6) were not read; they are
  where the predictions for (c)'s timescales would be found in detail.
- Nothing here bears on the physics of reality; it bears on whether a chosen move set can sample the toy's chosen
  ensemble, and how fast.
