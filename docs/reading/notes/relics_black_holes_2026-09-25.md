# Reading notes: relics, defect counting, and black-hole interiors (2026-09-25)

> **Status of these notes:** written by an assistant agent on 2026-09-25 from fetched copies of the papers. Some passages
> were read through a tool that summarizes a page, so every quotation must be checked against the paper itself before it is
> used in a paper or a letter. Inferences marked *ours* are unreviewed.


Literature review for series papers 2 (the leftover) and 4 (closed regions), written by an assistant agent
(Claude) on 25 September 2026. Context read first: CLAUDE.md, `docs/papers/series_plan.md` papers 2 and 4,
ASSUMPTIONS O33, O35, O36, O47.

**How each paper was read, so the reader can weigh each entry.** Two methods were used.
- *Text read directly*: the arXiv PDF was downloaded, its text extracted, and the passages searched and read
  by the agent. Quotations from these are exact up to PDF-extraction spacing.
- *Fetched and queried*: the arXiv HTML or abstract page was fetched and a summarizing tool was asked for
  specific passages and equation numbers. Quotations from these came back through that tool and **must be
  checked against the paper before they are quoted in a tracked document** (CLAUDE.md: search the text, do
  not rely on a summary).
- *Abstract only*: says so.

Nothing below was taken from memory without a fetch. Where a formula is our own derivation from a paper's
equations, it is marked **ours, unverified**.

---

## (a) The answer in one paragraph

If the project's leftovers behave like the defects of the published pictures, these are the laws to test.
(1) **Kibble-Zurek does not apply as a power law.** Its prediction, a defect density falling as
(quench time)^-(nu/(1+z nu)) for kinks in one dimension (del Campo and Zurek 2014, Eq. 10), is derived for
continuous transitions. For first-order ones Zhong (2025) argues that no Kibble-Zurek scaling of defects is
expected, and Suzuki and Zurek (2023/2025, Eq. 10) show that when nucleation dominates, the defect count is
the nucleation-and-growth count instead. The tube-to-sheet change is a decay over a fixed wall, so the
nucleation-and-growth (KJMA) picture is the one that should govern the leftovers. (2) **In one dimension,
KJMA gives exact counts.** With a constant nucleation rate I per column and front speed v, the untransformed
fraction is exp(-I v t^2) (Jun, Zhang and Bechhoefer 2004, Eq. 1), and the total number of seeds per column
is (1/2) sqrt(pi I / v) (ours, from that equation). With a nucleation rate that rises in time as
exp(beta t), the seed density is beta/(2v), the one-dimensional form of the cosmological bubble density
beta^3/(8 pi v_w^3) (Hindmarsh et al. 2021, Eq. 7.21; the 1D form is ours). With k planted seeds and no
spontaneous nucleation, a ring has exactly k meeting points, independent of the tube length, which is
consistent with T10's "one ring however large". (3) **If a leftover forms at a meeting point with
probability p, the count is binomial** (Gomez-Ruiz, Mayo and del Campo 2020): variance/mean = 1 - p, about
0.71 for O33's slope of 0.29. A random-walk mismatch picture (del Campo and Zurek, Eq. 26) instead gives a
mean growing as sqrt(k) and variance/mean^2 near pi/2 - 1 = 0.57. The existing T17 files can tell these
apart without a new run. (4) **Survival under cooling is a freeze-out integral**, not a formation law. For
Arrhenius healing and T25's geometric cooling, -ln(survival) should grow linearly with the cooling time
(ours), and O47's numbers are consistent with that, with a characteristic time near 10^5 sweeps. (5) The
published relative of the project's leftover is not a topological defect but a **trapped pocket of the old
phase** (a "false-vacuum remnant": Hong, Jung and Xie 2020, Eqs. 16-17), which is what a leftover curled
column is. On black holes, the published interiors divide into ordered, low-entropy condensates (the
gravastar of Mazur and Mottola; the graviton condensate of Dvali and Gomez, which keeps a large entropy by
sitting at a critical point) and maximal-entropy states (fuzzballs; Brustein and Medved's collapsed polymer
or frozen star). The owner's picture, an ordered, symmetric, re-curled interior reached by paying an
activation cost, sits with the first group, and **three things would distinguish it**. The first is where
the Bekenstein-Hawking entropy lives, since an ordered interior has few arrangements. The second is how it
forms: a sharp activation threshold, against formation driven by the sheer number of target states, which
is how Mathur and Brustein argue fuzzballs and frozen stars form. The third is what it predicts outside: a
horizon-scale surface gives non-zero tidal Love numbers and echoes, and GW250114 bounds the effective tidal
deformability below 34.8 at 90 %, consistent with zero. The closest published analog to "a black hole that
can burp a new space" runs the other way round: pockets of the *old* phase left behind by a delayed
first-order transition collapse into black holes, some with a baby universe inside (Hashino et al. 2025;
Ning et al. 2026). In the model so far, concentrated energy melts space (O20, O36, T26), which sides with
Trugenberger's disordered-bubble reading (VISION Update 2), not with the ordered picture.

---

## (b) Papers

### 1. Defect formation and counting

**[1] A. del Campo and W. H. Zurek, "Universality of phase transition dynamics: topological defects from
symmetry breaking", Int. J. Mod. Phys. A 29, 1430018 (2014); arXiv:1310.1600.**
- *Read:* fetched and queried (HTML v3), Secs. 2, 7, 9.
- *Establishes:* freeze-out time t_hat ~ (tau_0 tau_Q^(z nu))^(1/(1+z nu)) (Eq. 7); freeze-out length
  xi_hat = xi_0 (tau_Q/tau_0)^(nu/(1+z nu)) (Eq. 9); defect density n ~ xi_hat^d / xi_hat^D, i.e. exponent
  (D - d) nu/(1+z nu), which for kinks in one dimension is nu/(1+z nu) (Eq. 10). The estimate overcounts;
  in practice a factor f of about 5 to 10 multiplies xi_hat (Sec. 2). On a ring of circumference C much
  larger than xi_hat, independent domains choose phases at random, so the net winding is a random walk,
  Delta Theta ~ sqrt(C / xi_hat) (Eq. 26). An inhomogeneous transition makes defects only where the front
  moves faster than the relevant sound speed xi_hat/tau_hat (Eq. 55).
- *Bearing (ours, unverified):* KZ is derived for continuous transitions with degenerate broken-symmetry
  choices. The tube-to-sheet change is first order over a fixed wall, and it is not known whether each
  seed's sheet can come in several registrations that cannot join without a seam (T11 found the leftover is
  NEITHER at the seed nor where fronts meet). Eq. 26 is still useful as a rival counting law: if seeds
  choose registrations at random, the leftover count should grow as sqrt(k), not k.

**[2] F. J. Gomez-Ruiz, J. J. Mayo and A. del Campo, "Full counting statistics of topological defects after
crossing a phase transition", Phys. Rev. Lett. 124, 240602 (2020); arXiv:1912.04679.**
- *Read:* fetched and queried (HTML v2).
- *Establishes:* the defect number is binomial, P(n) = B(n, N, p), with N "the number of locations where a
  topological defect may be formed" (domain merges) and p the probability of a defect at a merge. All
  cumulants are proportional to the mean, with kappa_2/kappa_1 = 1 - p and kappa_3/kappa_1 = (1-p)(1-2p).
  Their 1D numerics give p = 0.422 +/- 0.014.
- *Bearing (ours, unverified):* the cleanest diagnostic for T17. With k evenly planted seeds there are
  exactly k merges; if leftovers form independently at merges, the spread across the twenty runs per k
  should be sub-Poissonian, with variance/mean near 0.71 (p = 0.29). Prediction C2 below.

**[3] F. Suzuki and W. H. Zurek, "Topological defect formation in a phase transition with tunable order",
arXiv:2312.01259 (v3, 25 April 2025; Los Alamos).**
- *Read:* fetched and queried (HTML v3), main text and the supplement's description.
- *Establishes:* a 1D Langevin field with a cubic term that makes the transition first order; defect
  density n = f n_nuc + (1 - f) n_KZM (Eq. 10), where f is the fraction converted by nucleation, from the
  Avrami form f = 1 - exp(-Omega) (Eq. 7), nucleation rate Gamma = A exp[-B(eps(t))/theta] (Eq. 5) and bubble
  size V(t, t_2) = integral of v (Eq. 8). At c = 0 they recover the KZ exponent (fit 0.267 +/- 0.029 against
  1/4). n_nuc is fitted numerically (a linear fit in eps, their Fig. S2), not given in closed form; in the
  nucleation-dominated regime the count departs from the KZ power law.
- *Bearing (ours, unverified):* in the model the leftover count should be the nucleation count, not a KZ
  power law. Since their n_nuc is empirical, the per-merge probability (our p) is also an empirical
  number; nothing here contradicts 0.29.

**[4] F. Zhong, "Is there Kibble-Zurek scaling of topological defects in first-order phase transitions?",
arXiv:2501.01064 (January 2025); Chin. Phys. Lett. 42, 030203 per the search listing (not checked).**
- *Read:* text read directly (PDF): abstract, introduction, conclusion.
- *Establishes:* for a cooled Landau-Devonshire model the order parameter shows complete universal scaling
  with the rate, but "as the system completely transforms from a polarized disordered phase to an ordered
  phase owing to an intrinsic symmetry-broken field responsible for the scaling, no topological defects of
  the KZ mechanism are generated and thus any KZ scaling for the topological defects can only be a rough
  approximation" (Conclusion). Its reference list gives Kibble, J. Phys. A 9, 1387 (1976) and Zurek, Nature
  317, 505 (1985) as the originals (neither read by us).
- *Bearing:* do not pre-register a KZ exponent for the leftovers. If a power law in the rate appears, treat
  it as effective and non-universal.

**[5] S. Jun, H. Zhang and J. Bechhoefer, "Nucleation and growth in one dimension, part I: The generalized
Kolmogorov-Johnson-Mehl-Avrami model", arXiv:cond-mat/0408260 (v2, 2004).**
- *Read:* text read directly (PDF), Secs. I and II.
- *Establishes:* with nucleation rate I per unit length per unit time and each island edge moving at v,
  the hole fraction is S(t) = exp(-I_0 v t^2) (Eq. 1) and f = 1 - S (Eq. 2) for constant I_0. For any I(t),
  with g(t) = the integral of I, the island (domain) density is n(t) = g(t) exp(-2v integral of g) (Eq. 8)
  and the hole-size distribution is rho_h(x, t) = g(t)^2 exp(-g x - 2v integral of g) (Eq. 9). Cites
  Kolmogorov, Johnson and Mehl, Avrami (J. Chem. Phys. 7, 1103 (1939)) and Sekimoto (Physica 125A, 261
  (1984)) as the originals (not read by us).
- *Bearing (ours, unverified):* the exact 1D law for a tube. Integrating nucleation over the untransformed
  length gives total seeds per column (1/2) sqrt(pi I / v). In quantities the project can measure
  (Prediction C1): seeds per tube = sqrt(pi r / 2) for large r = tau_sweep / tau_wait, and about 1 + r/2
  for small r. "One ring however large" (T10) and "one sheet patch in 78 of 80 boxes" say the runs so far
  sit at small r.

**[6] E. Ben-Naim and P. L. Krapivsky, "Nucleation-and-growth in one dimension" (arXiv:cond-mat/9603036;
Phys. Rev. E 54, 3562 (1996) per the reference list of [5]).**
- *Read:* fetched and queried (HTML), Secs. II.1, II.2.
- *Establishes:* in units where each island edge moves at 1/2 and the rate is 1: simultaneous nucleation
  gives gap density f(x, t) = exp(-x - t) and N(t) = S(t) = exp(-t) (Eq. 7); continuous nucleation gives
  f(x, t) = t^2 exp(-x t - t^2/2) and S(t) = exp(-t^2/2) (Eqs. 19-20). The fraction of one-seed islands
  decays as t^-2 under continuous nucleation.
- *Bearing:* confirms [5] independently. The "simultaneous nucleation" case is the planted-seed experiment
  (T17): the coverage is deterministic, and all the randomness is in what happens at the merges.

**[7] M. B. Hindmarsh, M. Luben, J. Lumma and M. Pauly, "Phase transitions in the early universe", SciPost
Phys. Lect. Notes 24 (2021); arXiv:2008.09136.**
- *Read:* text read directly (PDF), Sec. 7.1.
- *Establishes:* transition rate parameter beta = d/dt log(Gamma/V) at t_f (Eq. 7.12);
  Gamma/V = Gamma_f exp(beta (t - t_f)) (Eq. 7.13); t_f defined by 8 pi v_w^3 Gamma_f / (beta^4 V) = 1
  (Eq. 7.16); false-vacuum fraction h(t) = exp[-exp(beta (t - t_f))] (Eq. 7.17); final bubble density
  n_bubble = Gamma_f/(V beta) = beta^3/(8 pi v_w^3) = 1/R_*^3 (Eq. 7.21). Also: "In the extreme case of a
  slow wall and large latent heat, nucleation can stop altogether, and the interior of the bubbles can
  reheat to the critical temperature. In this case, the universe is in a mixed phase" (after Eq. 7.21).
- *Bearing (ours, unverified):* the same steps in one dimension (bubble length 2v(t - t') in place of the
  sphere) give -log h = (2 v Gamma_f / beta^2) exp(beta (t - t_f)) and a seed density per column of
  beta/(2v); seeds per tube = beta L/(2v) = beta tau_sweep. For the tube, nucleation is Arrhenius over a
  fixed wall (12 units, VISION Update 9), so beta = (12/g^2) dg/dt: the rate grows on **heating**, not on
  cooling, and a sealed box, where the released lump warms the bath, should speed nucleation up. That is
  the opposite of the cosmological case quoted above, where reheating stops nucleation, and it is worth a
  sentence in paper 2 (Prediction C4).

**[8] H. Jang and G.-W. Chern, "Suppressed coarsening after an interaction quench in the Holstein chain",
arXiv:2602.05815 (February 2026; University of Virginia).**
- *Read:* text read directly (PDF), abstract and introduction. The abstract of the companion paper
  arXiv:2512.07744 (1D kink coarsening) was read from the arXiv listing.
- *Establishes:* an isolated, strictly energy-conserving 1D system shows three post-quench regimes: a
  disordered state, "slow scale-invariant ordering dynamics", and "a frozen CDW state with arrested
  coarsening and immobile kinks". In the middle regime the kink density falls as n ~ t^(-1/3). The
  introduction summarizes that in Hamiltonian 1D quenches kinks move ballistically and rarely annihilate,
  giving n ~ 1/t at long times, and that energy conservation couples kink motion to a slowly evolving
  local temperature.
- *Bearing (ours, unverified):* the closest published setting to the sealed tube: energy conserved,
  defects in 1D, and the same three outcomes the project sees (melt, convert, freeze). The kink-decay laws
  (t^-1, t^-1/2, t^-1/3) are what to fit if the leftover count in a sealed box is followed in time.

### 2. Relics and remnants as dark matter; Trugenberger's allotropes

**[9] C. A. Trugenberger, "Dark matter and dark energy in combinatorial quantum gravity", Class. Quantum
Grav. 41 (2024), DOI 10.1088/1361-6382/ad7acf; arXiv:2409.09385 (the project's [T24]).**
- *Read:* fetched and queried (HTML v1), Sec. V "Dark matter". One web search for newer Trugenberger papers
  on dark matter (2025-2026) found only the review [T25] and arXiv:2311.17526 (on 3D quantum behavior, not
  read); a search of his full arXiv listing was not made in this session.
- *Establishes (as extracted; check the wording before quoting):* "At each coupling, one of the four
  possible vertex types of the semi-regular tiling, with one, two, three of four squares will constitute the
  minimum of the free energy"; "When the coupling is decreased from the critical value, the number of
  squares corresponding to the free-energy minimum will increase"; "If, at this new value, the free-energy
  difference between the actual minimum and the previous minimum at higher couplings is sufficently small,
  very long-lived metastable domains of a different tiling can survive". Such domains, "characterized by
  0 < s_i < s-bar are neither baryonic matter nor space but, rather, represent natural candidates for dark
  matter". They have higher curvature and so gravitate. No simulations, no abundance, no statement on the
  order of the steps, and nothing on black holes.
- *What he predicts, plainly:* allotropes form on cooling, survive when the free-energy gap to the new
  minimum is small, carry excess curvature (mass), and are otherwise inert. He gives no number.
- *Bearing (ours, unverified):* two differences from the project's leftover. His survive because the
  free-energy gap is small (thermodynamics); the project's survive because of a healing wall and fast
  cooling (kinetics, O35 and O47). And his have *fewer* squares than the new minimum (left over from the
  higher-coupling side), while the project's curled column has *more* (left over from the more curled
  side). Both are pockets of the previous minimum. The project's result that the cooling rate decides
  survival is a measurement his paper does not contain.

**[10] J.-P. Hong, S. Jung and K.-P. Xie, "Fermi-ball dark matter from a first-order phase transition",
Phys. Rev. D 102, 075028 (2020); arXiv:2008.04430.**
- *Read:* fetched and queried (HTML v2), Secs. II-IV.
- *Establishes:* dark fermions too heavy to enter the new phase are trapped in shrinking pockets of the old
  phase and form "Fermi-balls". False-vacuum fraction p(T) = exp(-I(T)) (Eqs. 14-15), with percolation at
  p = 0.71. A pocket stops splitting when no further bubble nucleates inside it while it shrinks:
  Gamma(T_*) V_* (R_*/v_b) ~ 1 with V_* = (4 pi/3) R_*^3 (Eq. 16). Remnant density
  n_* = (3/(4 pi))^(1/4) (Gamma(T_*)/v_b)^(3/4) p(T_*) (Eq. 17); nucleation rate Gamma ~ T^4 exp(-S_3/T)
  (Eq. 10). The final abundance (Eq. 29) has no exponential dependence on beta/H.
- *Bearing (ours, unverified):* the published concept that fits the project's leftover: a pocket of the
  old phase held by something that stops it shrinking (for them, fermion pressure; in the model, the wall
  against removing the last curled column). The 1D form of Eq. 16 is L_* = sqrt(v/Gamma), so the pocket
  count per length goes as sqrt(Gamma/v), matching the KJMA count of [5].

**[11] K. Kawana and K.-P. Xie, "Primordial black holes from a cosmic phase transition: The collapse of
Fermi-balls", Phys. Lett. B (2021), DOI 10.1016/j.physletb.2021.136791; arXiv:2106.00111.**
- *Read:* fetched and queried (HTML v3).
- *Establishes:* the same remnant count, n_FB = V_*^-1 p(T_*), and a chain: "The FOPT forms Fermi-balls,
  which in turn collapse into PBHs when the internal Yukawa force becomes dominant." The collapse is a
  mechanical instability, not a phase change.
- *Bearing (ours, unverified):* in the published literature the relic of a first-order change and a black
  hole can be the same object at two stages. That links papers 2 and 4 of the series in a way the project
  has not drawn.

**[12] H. Murayama and J. Shu, "Topological dark matter", Phys. Lett. B (2010), DOI
10.1016/j.physletb.2010.02.037; arXiv:0905.1720.**
- *Read:* fetched and queried (HTML v1).
- *Establishes:* uses the KZ freeze-out length, xi ~ xi_0 (tau_Q/tau_0)^(nu/(1+mu)), in cosmological terms
  xi ~ H^-1 (H^2/(lambda T_c^2))^(1/3), to argue that "the Kibble-Zurek mechanism provides a substantially
  larger abundance of topological defects from phase transitions in early universe than the original
  estimate by Kibble". Point defects then give n/s ~ 0.006 (30 T_c/M_pl)^(3 nu/(1+nu)) and a relic
  abundance formula. Stability comes from a conserved topological charge.
- *Bearing:* the textbook route from "defects per correlation volume" to a dark-matter abundance. It needs
  a conserved charge for stability, which the project's leftover does not have (it anneals, O35).

**[13] C. Rovelli and F. Vidotto, "Small black/white hole stability and dark matter", arXiv:1805.03872
(Universe, 2018, per the search listing).**
- *Read:* abstract only.
- *Establishes (abstract):* remnants of evaporated black holes, stabilized by a minimal area eigenvalue of
  loop quantum gravity, could be a component of dark matter.
- *Bearing:* a published line in which the dark-matter relic is a black-hole remnant, which joins the
  owner's two pieces (leftover, black hole) from the other end. Not read further.

### 3. Black-hole interiors as a different phase

**[14] P. O. Mazur and E. Mottola, "Gravitational condensate stars: an alternative to black holes",
arXiv:gr-qc/0109035 (v6; journal reference on arXiv: Universe 9 (2023) 88).**
- *Read:* fetched and queried (HTML v6).
- *Establishes:* three regions (Eq. 6): a de Sitter interior with rho = -p, a thin shell with rho = +p, and
  a Schwarzschild exterior. The interior is a "gravitational vacuum condensate" reached through "a vacuum
  rearrangement phase transition in the vicinity of" the would-be horizon. Entropy of order k_B M l/hbar
  (Eq. 18), far below Bekenstein-Hawking. The dynamical formation mechanism is stated to be incomplete
  (Appendix A.7).
- *Bearing (ours, unverified):* the published interior most like the owner's: ordered, symmetric, a
  distinct phase, with a surface. It pays for order with low entropy. If the owner's re-curled interior is
  like this, the pages should say where the black-hole entropy lives.

**[15] G. Dvali and C. Gomez, "Black holes as critical point of quantum phase transition", arXiv:1207.4059
(2012; no journal reference on arXiv).**
- *Read:* text read directly (PDF), pp. 1-4.
- *Establishes:* a black hole as a self-sustained Bose-Einstein condensate of gravitons at "maximal
  packing": L = sqrt(N) L_P and alpha = 1/N, "with the critical value of the coupling, alpha N = 1"
  (Eqs. 3-5); self-sustainability condition E_k + V = (1 - alpha N) hbar/L = 0 (Eq. 4). Nearly gapless
  Bogoliubov modes at the critical point carry the entropy.
- *Bearing (ours, unverified):* the one published proposal we found in which the interior is an ordered
  condensate *and* keeps a large entropy, by sitting at a critical point. If the owner wants order without
  losing the Bekenstein-Hawking entropy, this is the precedent to read in full.

**[16] R. Brustein and A. J. M. Medved, "Black holes as collapsed polymers", Fortsch. Phys. 65, 1600114
(2017); arXiv:1602.07706.**
- *Read:* fetched and queried (HTML v1).
- *Establishes:* the interior as a bound state of highly excited closed strings at the Hagedorn
  temperature, modeled on the collapsed phase of a polymer (the coil-globule analogy, Sec. 3). Free energy
  -(F/V T)_CP = c - (1/2) upsilon c + ... (Eq. 3) and its string form (Eq. 6); minimizing gives N = R/g_s
  and an area-law entropy. No transition from ordinary matter is described.
- *Bearing:* a black hole as a distinct phase of the underlying degrees of freedom, as in the owner's
  picture, but the phase has maximal entropy, not order.

**[17] R. Brustein, A. J. M. Medved and K. Yagi, "When black holes collide: probing the interior
composition by the spectrum of ringdown modes and emitted gravitational waves", Phys. Rev. D 96, 064033
(2017); arXiv:1704.05789.**
- *Read:* fetched and queried (HTML v2).
- *Establishes:* the collapsed-polymer interior adds a class of ringdown modes with omega ~ g_s c/R_S and
  damping time ~ (1/g_s)(R_S/c), "parametrically lower" in frequency and longer lived than a classical
  black hole's; from GW150914, g_s <~ 0.65 (as extracted; equation numbers to verify).
- *Bearing:* the observable that separates an interior phase with its own internal modes from a vacuum
  interior: a second, slower ringdown branch.

**[18] R. Brustein, A. J. M. Medved and T. Simhon, "Black holes as frozen stars", Phys. Rev. D 105, 024019
(2022); arXiv:2109.10017.**
- *Read:* abstract only.
- *Establishes (abstract):* "maximally negative radial pressure throughout the entirety of the object's
  interior"; the transitional outer layer is stable, and fluctuations there are "perfectly frozen".

**[19] C. Bambi, R. Brustein, V. Cardoso, ..., S. Mathur, ..., P. Pani et al., "Black hole mimickers: from
theory to observation" (proceedings of the Princeton workshop, 3-5 March 2025), arXiv:2505.09014.**
- *Read:* text read directly (PDF): Brustein's section "Frozen Stars as Black Hole Mimickers" (pp. 35-37),
  the opening of Mathur's section, and Gupta's section on spin-induced quadrupoles.
- *Establishes:* the frozen-star metric ds^2 = -eps^2 dt^2 + dr^2/eps^2 + r^2 dOmega^2, with radius
  R ~ 2GM(1 + eps^2), sourced by p_r = -rho with zero transverse pressure. Predictions: "an additional
  branch of ringdown modes, with a longer decay time and lower amplitude than the primary signal" and "a
  large, negative Love number". On formation: "Inspite of having an exponentially small transition
  probability amplitude to any of the microstates of the BHs Gamma ~ e^-S_BH, having an exponentially large
  phase space e^+S_BH leads to a total transition probability ~ 1." Gupta's section: the spin-induced
  quadrupole parameter kappa is 1 for Kerr, about 2 to 14 for neutron stars and 10 to 150 for boson stars,
  and "for gravastars it could be negative"; binaries through the third observing run show no significant
  evidence for a mimicker.
- *Bearing (ours, unverified):* formation "by counting" is exactly the interchangeable-points drive of
  VISION Update 27 (the fully curled state wins by its symmetry count only below lambda near 1.02). The
  published black-hole mimickers that keep the full entropy form this way; an ordered interior with few
  arrangements cannot, and must form by activation. That is a clean line between the owner's picture and
  these alternatives.

**[20] S. D. Mathur, "The fuzzball proposal for black holes: an elementary review", Fortsch. Phys. 53,
793 (2005); arXiv:hep-th/0502050,** and **[21] S. D. Mathur, "Tunneling into fuzzball states", Gen. Rel.
Grav. 42, 113 (2010); arXiv:0805.3716.**
- *Read:* both fetched and queried (HTML).
- *Establish:* the 2-charge microstate count S_micro = 2 sqrt(2) pi sqrt(n_1 n_p) ([20], Eq. 3.32); each
  microstate is a horizonless geometry capped near the horizon; the fuzzball radius grows with the charges
  until it reaches horizon size ([20], Eq. 7.166); the generic state is a random, high-entropy one, not a
  condensate. [21]: the tunneling amplitude into one fuzzball state is A ~ exp(-alpha G M^2), the number of
  states is exp(S_bek) ~ exp(G M^2), and "these small and large numbers compensate each other". No
  phase-transition language.
- *Bearing:* the maximal-entropy end of the spectrum; formation by counting, as in [19].

**[22] V. Cardoso and P. Pani, "Testing the nature of dark compact objects: a status report", Living Rev.
Relativ. 22, 4 (2019); arXiv:1904.05363.**
- *Read:* text read directly (PDF), Secs. 2, 3.9, 4.2, 4.5.3, 5.8 and Table 1.
- *Establishes:* closeness parameter r_0 = 2M(1 + eps) (Eq. 3); echo delay tau_echo ~ 4M |log eps|
  (Eq. 37). Tidal Love numbers of black holes are zero, while those of ultracompact objects vanish only
  logarithmically, k ~ 1/|log eps|; for Robin-type boundary conditions k ~ 2(4a - 3c)/(15 a log eps)
  (Eq. 95), "a magnifying glass to probe near-horizon quantum structures". For eps ~ l_P/M, k is of order
  10^-3 to 10^-2, "probably out of reach even with 3G", needing LISA golden binaries. Table 1 does not mark
  formation as addressed for gravastars, fuzzballs or collapsed polymers (our reading of the extracted
  table).
- *Bearing:* the standard list of what would distinguish any interior phase with a surface: echoes, Love
  numbers, spin-induced multipoles, ringdown. None of them is specific to "ordered" as against
  "disordered".

**[23] M. Andres-Carcasona and G. Caneva Santoro, "No Love for black holes: tightest constraints on tidal
Love numbers of black holes from GW250114", arXiv:2512.01918 (December 2025).**
- *Read:* abstract only.
- *Establishes (abstract):* a 90 % upper limit on the effective tidal deformability, Lambda-tilde < 34.8;
  the data are consistent with vanishing Love numbers; some boson-star models are ruled out.
- *Bearing:* the current bound any horizon-scale surface must respect.

**[24] J. Liu, L. Bian, R.-G. Cai, Z.-K. Guo and S.-J. Wang, "Primordial black hole production during
first-order phase transitions", Phys. Rev. D 105, L021303 (2022); arXiv:2106.05637** (abstract only);
**[25] K. Hashino, S. Kanemura, T. Takahashi, M. Tanaka and C.-M. Yoo, "Super-critical primordial black hole
formation via delayed first-order electroweak phase transition", arXiv:2501.11040 (January 2025)** (fetched
and queried, HTML v1); **[26] Z. Ning, X.-X. Zeng, R.-G. Cai and S.-J. Wang, "Numerical simulations of
primordial black hole formation via delayed first-order phase transitions", JCAP 07 (2026) 073;
arXiv:2601.21878** (text read directly: abstract and contents).
- *Establish:* regions where the vacuum decay is postponed stay in the old phase while the radiation
  outside redshifts; they become overdense and collapse ([24], abstract). In the "super-critical" case "a
  baby universe is realized in the local region inside the wall", and outside observers see a black hole;
  the criterion is t_V <~ t_H, with t_H = 1/(2 H) and t_V = (1/2) sqrt(3 M_pl^2/rho_V) ([25], Eqs. 20, 21,
  24). Full simulations ([26]) find three outcomes: "type B (supercritical) PBHs with an interior baby
  universe", "type A (subcritical) PBHs ... formed by direct wall collapse", and dispersal. Type B needs
  t_H/t_V >~ 1 (critical range about 1.1 to 1.6); type A occurs down to about 0.35 to 0.7.
- *Bearing (ours, unverified):* the published mechanism closest to "a black hole that holds, or burps, a
  new space", with a threshold and three outcomes as in T9. But the direction is reversed: the black hole
  is a trapped pocket of the *old* phase (the project's leftover, grown large), not space re-curled. It
  deserves one paragraph in paper 4 as the nearest relative, stated as a different mechanism.

### 4. Concentrated energy in discrete geometry

**[27] A. Hamma, F. Markopoulou, S. Lloyd, F. Caravelli, S. Severini and K. Markstrom, "A quantum
Bose-Hubbard model with evolving graph as toy model for emergent spacetime", Phys. Rev. D 81, 104032
(2010); arXiv:0911.5075.**
- *Read:* fetched and queried (HTML v3), Sec. II.
- *Establishes:* an exchange term converts matter quanta at two vertices into an edge between them (the
  H_ex term), so a highly connected region "S" can trap particles, and "other particles coming from
  outside, will get trapped inside S too, therefore increasing the number of edges and particles within
  it" (as extracted). The classical model's long-time state is a random graph (Poisson degrees), not an
  ordered one.
- *Bearing (ours, unverified):* a published discrete model in which concentrated matter makes a denser,
  more connected region instead of melting. The mechanism is a matter-to-edge coupling that CQG does not
  have. The project's graphs have fixed degree, so there is no analog without a new rule (S1).

**[28] F. Caravelli, A. Hamma, F. Markopoulou and A. Riera, "Trapped surfaces and emergent curved space in
the Bose-Hubbard model", Phys. Rev. D 85, 044046 (2012); arXiv:1108.2013.**
- *Read:* fetched and queried (HTML v3).
- *Establishes:* highly connected subgraphs (a complete core K_N) trap matter; the ground state is
  protected by a gap that grows linearly with N; the vertex degree sets a local propagation speed (Eq. 60).
  The trapping regions are put in by hand, and back-reaction is ignored (Secs. II, VII).
- *Bearing:* a "trapped surface" in a graph means a dense core. It is not shown to form from concentrated
  energy.

**[29] J. Smit, "Using massless fields for observing black hole features in the collapsed phase of
Euclidean dynamical triangulations", arXiv:2301.07081 (v4, 17 December 2024).**
- *Read:* fetched and queried (HTML v4).
- *Establishes:* the collapsed (crumpled) phase of 4D Euclidean dynamical triangulations contains "a
  'singular structure' consisting of two adjacent 'singular vertices'" belonging to a macroscopic number of
  simplices. There, ensemble-averaged scalar propagators give a metric with a horizon, a de Sitter-like
  interior and an exterior with g_tt = 1/g_rr. The collapsed and elongated phases are "separated by a
  first-order transition line in the kappa_2-beta phase diagram". The author stresses that the results
  are volume-averaged over the ensemble, not a localized collapse of concentrated matter.
- *Bearing (ours, unverified):* a discrete-geometry precedent for a collapsed, highly connected phase with
  black-hole features, reached through a first-order line. It is a phase of the whole ensemble, not a local
  re-curling. We have not found a discrete-geometry model in which a local injection of energy produces an
  ordered, re-curled region rather than disorder.

**Not read (seen only as references or titles):** Kibble, J. Phys. A 9, 1387 (1976); Zurek, Nature 317,
505 (1985) and Phys. Rep. 276, 177 (1996); Avrami (1939); Sekimoto (1984); Preskill's monopole-relic
calculation (not seen anywhere in this session; general knowledge only). Suzuki's 2025 papers "Machine
learning topological defect formation: When are the defects made?" and "Deconstructing symmetry breaking
dynamics" (titles from the arXiv listing). Lewicki and Vaskonen, arXiv:2305.04924 and 2402.04158 (titles
from search only).

---

## (c) Testable predictions for the project's simulations

All are **ours, unverified**, derived from the equations above under the stated assumptions. Each needs its
own pre-registration (rule 4) before a run. C2, C5 and part of C3 need no new run.

**C1. Spontaneous seeds against tube length (paper 2).** Assumptions: a constant nucleation rate per column
(Arrhenius over the 12-unit wall), fronts at constant speed, KJMA [5]. Measure tau_wait (the mean time to
the first nucleation, already known: 1/(3 exp(-12/g)) sweeps per tube, VISION Update 9) and tau_sweep (the
time for one seed's two fronts to convert the tube, from front position against time). With
r = tau_sweep/tau_wait:
- seeds per tube N_s ~ 1 + r/2 for r << 1, and N_s ~ sqrt(pi r / 2) for r >> 1;
- leftovers per tube n ~ 1.10 + s (N_s - 1), with s = 0.29 from O33, if spontaneous seeds behave like
  planted ones.

Vary: tube length L at fixed g and lambda, chosen so that r spans about 0.3 to 30. Falsifier: if "one ring
however large" (T10) persists at r >> 1, either nucleation stops once a front exists (fronts suppress
nucleation ahead of them) or leftovers are not tied to seeds.

**C2. Counting statistics of T17 (no new run).** From `results/t17_seeds_k{1,2,4,8}.csv`, take the variance
of the leftover count across the twenty runs at each k.
- Binomial at merges [2]: variance/mean = 1 - p, about 0.71 for p = 0.29; third cumulant/mean about 0.30.
- Random-walk mismatch [1, Eq. 26]: mean growing as sqrt(k), variance/mean^2 near pi/2 - 1 = 0.57.
- Poisson (independent scattering along fronts): variance/mean = 1.

Check the positions too: do leftovers sit at the midpoints between planted seeds (the merges)? T11 found
NEITHER for one seed; if that also holds for k seeds, the binomial-at-merges picture fails whatever the
variance says. By our arithmetic, the four means (1.10, 2.15, 2.50, 3.40) fit linear, square-root and
logarithmic forms about equally well, so the means alone cannot choose. Runs at k = 16 and 32 on a tube
long enough to keep the spacing would.

**C3. Survival under cooling as freeze-out (paper 2; O47).** Assumptions: each leftover heals independently
at an Arrhenius rate k_h(g) = nu exp(-E_h/g); geometric cooling from g0 to g1 over t_cool. Then
-ln P(survive) = the integral of k_h(g(t)) dt, which to leading order in E_h/g0 is

    -ln P ~ t_cool / t*,   with   t* = E_h ln(g0/g1) / (g0 k_h(g0)),

i.e. t* ~ 1.29 E_h tau_h(1.25) for T25's g0 = 1.25 and g1 = 0.25, where tau_h is the mean healing time.
Check against O47 (our arithmetic): 15 of 19, 14 of 18 and 7 of 19 surviving at t_cool = 10^4, 3 x 10^4 and
10^5 are consistent with a single exponential with t* near 10^5 sweeps, so half survive near 7 x 10^4.
Zero-parameter test: fit E_h and tau_h(1.25) from O35's healing times at g = 1.0, 1.25 and 1.5, then
predict t*. Vary next: the end coupling g1 (t* should grow as ln(g0/g1)) and the start g0.

**C4. Seeds under a heating ramp, and in a sealed box (paper 2).** The 1D form of [7] Eq. 7.21 gives seeds
per tube N_s = beta tau_sweep, with beta = (12/g^2) dg/dt for the tube's Arrhenius nucleation. So the
leftover count should grow linearly with the heating rate, not as a KZ power law ([3, 4]). In a sealed box
the released lump warms the bath, so nucleation should speed up as conversion proceeds (the opposite of the
cosmological case in [7]). The prediction is more sheet patches per tube in a sealed conversion than in an
open one started at the same g, when the bath spreads heat faster than the front moves. Vary: ramp rate;
sealed against open.

**C5. The leftover as a trapped pocket (papers 2 and 4; no new run for the first half).** If the leftover is
a pocket of the old phase that cannot shrink ([10] Eq. 16), its survival is set by the wall against
removing the last curled column, and its count per length in a spontaneous conversion should go as
sqrt(I/v) ([10] Eq. 17 in 1D, matching C1). Read from the saved end states: is the leftover always the last
column of X (a pocket), or sometimes a seam between two sheet registrations (a topological defect)? The
answer decides whether [1]-[4] or [10]-[11] is the right literature for paper 2.

**C6. Activation against counting (paper 4).** The owner's black hole forms by paying an activation cost;
the maximal-entropy alternatives ([19], [21]) form because the number of target states makes up for a tiny
amplitude. In the model, with named points, re-curling (if it ever happens) should show a sharp threshold
in local energy that does not depend on size, as the 12-unit spark did for uncurling, with the successive
fold excesses of O55 (36, 16 and 0 in six links at lambda = 1.25). With interchangeable points near
lambda = 1.02 (the designed T34 follow-up), a fold driven by counting should show a rate that scales with
the symmetry count of the folded state and no sharp threshold. Seeing the first but not the second
supports the owner's activation picture over the counting one.

**C7. A pocket that holds energy (paper 4, speculative).** In [24]-[26], pockets of the old phase that decay
late become black holes, with three outcomes separated by a threshold. The model's analog would be a long
stretch of tube left unconverted in a sealed box while the rest converts. From the existing T9 and T18 end
states: does the largest unconverted stretch ever exceed the one-column leftover, and does its size depend
on bath size the way the three outcomes of [26] depend on t_H/t_V? If no large pocket ever survives, the
delayed-decay route has no analog in this model, and paper 4 should say so.

---

## (d) Whom to ask (one narrow question each)

Recent papers were checked on arXiv on 25 September 2026; affiliations are taken from the papers' own
headers.

1. **Gia-Wei Chern, University of Virginia (Physics).** Recent: Jang and Chern, arXiv:2602.05815 (2026:
   isolated, energy-conserving 1D chain; three regimes; kink density t^-1/3); arXiv:2512.07744 (2025, 1D
   kink coarsening; abstract read); arXiv:2609.28436 (September 2026, domain-wall dynamics; abstract read).
   *Question:* "In a closed, energy-conserving, effectively one-dimensional system that converts from k
   evenly spaced seeds, we count 1.10, 2.15, 2.50 and 3.40 leftover defects for k = 1, 2, 4 and 8 (twenty
   runs each). Is the variance of the count across runs the right way to tell 'a defect forms at some
   merges' (binomial, variance/mean = 1 - p) from 'a defect forms at every merge and neighbors then
   annihilate', or is there a better diagnostic?"

2. **Kent Yagi, University of Virginia (Physics).** Recent: arXiv:2404.11110 and arXiv:2601.13411
   (quasinormal modes and their excitation beyond general relativity, I and II); arXiv:2410.02531 (tidal
   response beyond vacuum GR; its header gives UVA). Earlier, co-author of arXiv:1704.05789 with Brustein
   and Medved on interior modes. *Question:* "If a black hole's interior were an ordered, low-entropy phase
   with a boundary just outside r = 2M, like a gravastar, which single observable gives the tightest
   current bound on it: the tidal Love number (Lambda-tilde < 34.8 from GW250114), the spin-induced
   quadrupole, or an extra ringdown branch?"

3. **Fumika Suzuki (with W. H. Zurek), Los Alamos (affiliation from arXiv:2312.01259v3, April 2025; to
   verify).** Recent: arXiv:2312.01259 v3 (2025, defects across a transition of tunable order); two 2025
   papers on when defects are made (titles only). *Question:* "When a first-order change has a unique
   product phase, so the leftover is a trapped pocket of the old phase rather than a topological defect,
   should the pocket count still follow your n_nuc, i.e. scale with the number of nucleated domains, or do
   you expect a different law?"

Per the outreach preferences in memory: one narrow question each, disclose that the work is AI-assisted,
and draft nothing from these notes into `docs/outreach/` without the owner's decision.
