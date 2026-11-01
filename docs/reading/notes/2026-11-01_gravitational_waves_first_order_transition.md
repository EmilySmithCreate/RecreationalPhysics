# Gravitational waves from a first-order phase transition: the standard formulas, and which of their inputs the toy could stand in for (1 November 2026)

**Written 2026-11-01 by an assistant agent (Claude Fable 5.1). The owner has not read these passages.** Every quotation
below was taken from an HTML-to-text rendering (ar5iv) or from a PDF converted with PyMuPDF; equation numbers are as
the renderings showed them and should be checked against the published PDFs before any is cited in a paper. Nothing
here is a result of the programme; it is a reading. Everything in the two closing sections marked "ours" is ours and
unverified.

**Why this note.** `docs/papers/programme_draft.md` (piece 15) owes a target sheet on "the birth and the gravitational
waves it could leave", and the routes note of 1 November (`docs/design/routes_to_attention_2026-11-01.md`) said that the
step on this topic is a reading, not a run: the standard gravitational-wave (GW) formulas for a first-order transition,
to see which of their inputs the toy's measurements stand in for and which it cannot supply. The owner asked for the
reading to proceed, saying paper 2 (the scrap) needs something from this area.

## Sources and how each was read

Verified against the sources by a second agent on 2026-11-01; its corrections applied the same day.

| Key (not yet in `REFERENCES.bib`) | Paper | How read |
|---|---|---|
| [CapriniEtAl16] | C. Caprini, M. Hindmarsh, S. Huber et al., "Science with the space-based interferometer eLISA. II: Gravitational waves from cosmological phase transitions", JCAP 04 (2016) 001, arXiv:1512.06239 | In part, through an ar5iv rendering: Sec. 1.1 (parameters), Sec. 2.1 (the three contributions, Eqs. 6 to 18), Sec. 2.2 (efficiency factors, Eqs. 20 to 28). The last quarter of the page (the model survey) not read. |
| [CapriniEtAl20] | C. Caprini, M. Chala, G. Dorsch et al., "Detecting gravitational waves from cosmological phase transitions with LISA: an update", JCAP 03 (2020) 024, arXiv:1910.13125 | In part, through an ar5iv rendering: Secs. 2.1 to 2.3 (parameters, Eqs. 2 to 15) and Sec. 3 (GW spectra, Eqs. 27 to 32). Model sections (Sec. 4 onward) not read. |
| [HHRW14] | M. Hindmarsh, S. J. Huber, K. Rummukainen, D. J. Weir, "Gravitational waves from the sound of a first order phase transition", Phys. Rev. Lett. 112 (2014) 041301, arXiv:1304.2433 | In full through an ar5iv rendering (a four-page letter; Eqs. 6, 9, 12 to 14 quoted). |
| [HHRW17] | M. Hindmarsh, S. J. Huber, K. Rummukainen, D. J. Weir, "Shape of the acoustic gravitational wave power spectrum from a first order phase transition", Phys. Rev. D 96 (2017) 103520, arXiv:1704.05871 | In part through an ar5iv rendering: the abstract, Sec. II (definitions, Eq. 2), Sec. IV (Eqs. 23, 24, 31), Sec. V (the fit, Eqs. 35 to 45). The paper's own footnotes 5, 6 and 9 say that two of its numerical prefactors were corrected by an erratum; the corrected values are taken from [Athron23] below. |
| [HLLP21] | M. Hindmarsh, M. Lüben, J. Lumma, M. Pauly, "Phase transitions in the early universe", SciPost Phys. Lect. Notes 24 (2021), arXiv:2008.09136 | In part through an ar5iv rendering: Sec. 7 (bubble nucleation and growth, Eqs. 7.12, 7.21, 7.24, 7.25, 7.40 to 7.44) and Sec. 8.2 (GWs, Eqs. 8.17 to 8.25). Sec. 7.1 was already read from the PDF on 25 September (`relics_black_holes_2026-09-25.md`, source [7]); this note extends that reading and does not repeat it. Secs. 1 to 6 not read. |
| [Athron23] | P. Athron, C. Balázs, A. Fowlie, L. Morris, L. Wu, "Cosmological phase transitions: from perturbative particle physics to gravitational waves", Prog. Part. Nucl. Phys. 135 (2024) 104094, arXiv:2305.02357 (v3) | In part from the PDF (163 pages), converted with PyMuPDF: Sec. 5.1 (the transition temperature), 5.3 (kinetic energy fraction, Eqs. 5.19 to 5.25), 5.4 (length and time scales, Eqs. 5.36 to 5.38, 5.49, 5.50), Sec. 6.2 (redshift, Eqs. 6.27, 6.28), Sec. 6.3 to 6.5 (collisions, sound waves, turbulence, Eqs. 6.32 to 6.46). Secs. 1 to 4 and the model survey not read. This is the "recent review" the task asked for; it was found by its arXiv number from the task, not by a fresh search. |

The ar5iv rendering of [Athron23] stopped inside its Sec. 4, so its Secs. 5 and 6 were read from the PDF. The 2016
paper's own abstract page was fetched for the title and journal.

## 1. The four inputs

Every fit in this literature is a function of four numbers evaluated at the transition, plus the number of relativistic
degrees of freedom g* (about 100 at the electroweak scale, which only enters as weak powers).

**T\*, the transition temperature.** [CapriniEtAl16] Sec. 1.1: "T* denotes the temperature of the thermal bath at the
time t* when GWs are produced", and for transitions without strong reheating T* is close to the nucleation temperature
T_n. [Athron23] Sec. 5.1 is franker about which moment that is: "The correct transition temperature is not known in
general; perhaps there is no single milestone that works in all cases. Typical choices for T* are the nucleation
temperature, the percolation temperature, the completion temperature, and the reheating temperature", and "The common
approach in recent careful studies is to choose T* = T_p throughout" (the percolation temperature). T* enters the GW
formulas only through the redshift from then to now: the peak frequency today scales as T*/(100 GeV), and the amplitude
today does not depend on it explicitly (Eqs. 6.27 and 6.28 of [Athron23], quoted in Sec. 3 below).

**alpha, the strength.** Three definitions are in use, and they agree only in the "bag" model where the energy density
splits into a constant vacuum part and a T^4 radiation part.

- [CapriniEtAl16] Sec. 1.1, Eq. (4): alpha is "the ratio of the vacuum energy density released in the transition to that
  of the radiation bath", alpha = rho_vac / rho_rad*, with rho_rad* = g* pi^2 T*^4 / 30. This is the latent-heat-over-
  radiation form the task named.
- [CapriniEtAl20] Sec. 2.2 moves to the trace anomaly: Eq. (12), alpha_theta = (4/3) Delta theta(T_n) / w_+(T_n), with
  theta = (e - 3p)/4 and w_+ the enthalpy of the old phase just ahead of the wall; the paper calls the bag form Eq. (9)
  "the definition of alpha which is being used in most of the literature" and adopts the trace-anomaly form, dropping the
  subscript. An energy-based form, Eq. (13), is noted to "overestimate kinetic energy for weak transitions" (paraphrase
  of the rendering).
- [HLLP21] Eq. (7.40): alpha_n = (4/3) Delta theta / w_s at T = T_n, with Delta theta = theta_s - theta_b. [Athron23]
  Eq. (5.23): "alpha = 4(theta_f(T*) - theta_t(T*)) / (3 w_f(T*)), where theta is the trace anomaly defined in
  Eq. (5.10) and w_f is the enthalpy density of the false vacuum. The latter generalizes the radiation energy density,
  with the relation w_f = (4/3) rho_R holding in the bag model."

What alpha measures, in words: how much energy the change frees, as a fraction of the thermal energy already there. In
the bag model alpha = epsilon / rho_R, where "epsilon is the energy liberated by the phase transition" ([Athron23]
Sec. 5.3, text after Eq. 5.21).

**beta/H\*, the inverse duration.** [CapriniEtAl16] Sec. 1.1, Eqs. (1) to (3): the nucleation rate is Gamma(t) =
A(t) exp(-S(t)); beta is defined by beta = -(dS/dt) at t* and is approximately the logarithmic rate of change of
Gamma; and beta/H* = T* (dS/dT) at T*. The paper calls beta the "(approximate) inverse time duration of the PT" and
says "The smaller beta/H* is, the stronger the phase transition and consequently the GW signal." [HLLP21] Eq. (7.12) defines it directly from the
rate per volume: beta = d/dt log(Gamma/V) at the time t_f when bubbles collide. Footnote 8 of [HLLP21] Sec. 8.2 notes
that alpha and beta are not independent: stronger transitions take longer and so have smaller beta (paraphrase).

**R\*, the mean bubble separation (the length scale beta sets).** [HLLP21] Eq. (7.21): the final bubble density is
n_bubble = beta^3 / (8 pi v_w^3) = 1/R*^3, so R* = (8 pi)^{1/3} v_w / beta. [CapriniEtAl20] Eq. (6) and [Athron23]
Eq. (5.50) replace v_w by max(v_w, c_s) for subsonic walls, because then the shock ahead of the wall, moving at the
sound speed, is what meets its neighbor. [Athron23] text after Eq. (5.49): "Strictly speaking, this relation is
obtained at the so-called e-folding time/temperature, where the false vacuum fraction P_f = 1/e, but it is often
applied at the percolation or nucleation temperature."

**v_w, the wall speed.** [CapriniEtAl16] Sec. 1.1: v_w "denotes the bubble wall velocity in the rest frame of the fluid
far away from the bubble". [CapriniEtAl20] Sec. 2.3: v_w is close to 1 for a large class of strong transitions
(paraphrase; their Eq. 15 is the transition-radiation friction result). In every amplitude formula v_w enters linearly
or through the (8 pi)^{1/3} v_w / beta length, and in the efficiency factor kappa.

[HLLP21] Sec. 8.2 states the count: four parameters determine the spectrum, T_n, alpha_n, beta and v_w, with footnote 7
adding that the sound speed is a fifth that recent work includes (paraphrase).

## 2. The three contributions, and how the energy is split among them

The total is a sum, [CapriniEtAl16] Eq. (6): h^2 Omega_GW = h^2 Omega_phi + h^2 Omega_sw + h^2 Omega_turb, and
[HLLP21] Eq. (8.17): Omega_gw = Omega_bc + Omega_sw + Omega_tu. Each takes a share of the released energy through its
own efficiency factor.

**Where the released energy goes.** [CapriniEtAl16] Sec. 2.2 splits alpha into a part that stays in the moving wall
(the scalar field's gradient energy) and a part handed to the plasma. Eq. (23): kappa_phi = (alpha - alpha_infinity) /
alpha, the "surplus energy" that keeps accelerating the wall when the wall runs away; Eq. (24): kappa_v =
(alpha_infinity / alpha) kappa_infinity for the bulk motion of the fluid, with kappa_infinity = alpha_infinity /
(0.73 + 0.083 sqrt(alpha_infinity) + alpha_infinity); and the rest, kappa_therm = (1 - kappa_infinity)
alpha_infinity / alpha, is heat. In the runaway case "Only the fraction alpha_infinity / alpha of the total energy
budget is then transformed into bulk motion and thermal energy" (Sec. 2.2.2). When the wall reaches a terminal speed
(the usual thermal case), Eq. (20) gives kappa_v = alpha / (0.73 + 0.083 sqrt(alpha) + alpha) for v_w near 1, the
same fit as [HLLP21] Eq. (7.44).

[Athron23] Sec. 6.3 states the modern consensus on the wall's share: "because kappa_coll << 1 in the non-runaway case,
the collision component of the GW spectrum is typically subdominant across the whole frequency spectrum and it may be
neglected entirely", and "The fraction of energy released during the phase transition into the kinetic and gradient
energy of the bubble wall reduces as the bubble wall approaches its terminal velocity (in the non-runaway case), while
most of the energy is transferred to the surrounding plasma before collision." The exception: "when the bubble wall
runs away ... kappa_coll is close to unity and the collision contribution would be effectively the only source of
GWs". [HHRW14] gives the physical reason: the compression-wave energy grows as R^3 and "quickly outstrips the energy in
the scalar field, which grows only as R^2".

**The kinetic energy fraction K.** [Athron23] Eq. (5.19): K = rho_kin(T*) / rho_tot(T*); Eq. (5.21): K = kappa alpha /
(1 + alpha) in the bag model, with kappa = rho_kin / epsilon; Eq. (5.24): K = kappa alpha / (1 + alpha + delta) with the
trace-anomaly alpha, delta = 4 theta_t / (3 w_f) usually neglected. Also K = Gamma Ubar_f^2 (Eq. 5.35, Sec. 5.4;
repeated after Eq. 6.34), where Ubar_f is the root-mean-square fluid velocity and Gamma the adiabatic index (about 4/3). [HHRW17]
Sec. IV gives the Espinosa et al. estimate Ubar_f = sqrt((3/4) kappa_v alpha), which it says "gives a good estimate of
the 3D mean-square velocity" (paraphrase). [Athron23] Sec. 5.3 adds a caution worth keeping: "Even if this is close to
one most of the energy will be transferred to heat during the progress of the phase transition".

**The turbulence share.** [CapriniEtAl16] Eq. (21): kappa_turb = epsilon kappa_v; Sec. 2.2.1 (the non-runaway
case) sets the value: "to allow for the uncertainty in what follows we conservatively set ϵ=0.05". [Athron23] Sec. 6.5: kappa_turb "remains poorly understood and is arguably the greatest source of
uncertainty in predictions for turbulence"; the literature uses epsilon = 5 to 10 %, and "ref. [645] uses epsilon = 1
for strong transitions". [CapriniEtAl20] Sec. 3.3 neglects turbulence in its numerical analysis.

## 3. The formulas, with their numbers

Frequencies today in Hz; amplitudes as h^2 Omega today. Two versions are given where the 2016 and the 2023 prefactors
differ, since both circulate.

**Redshift factors** ([Athron23] Eqs. 6.27 and 6.28, from a transition at temperature T_1 with g_eff degrees of
freedom): f_0 = 1.65 x 10^-5 Hz (g_eff/100)^{1/6} (T_1 / 100 GeV) (f_1 / H_1), and Omega_0 h^2 = 1.67 x 10^-5
(100/g_eff)^{1/3} Omega_1. "We recommend using T_1 = T_reh because redshifting should be taken from after reheating."

**Bubble collisions (envelope approximation).** [CapriniEtAl16] Sec. 2.1.1:
- Eq. (7): h^2 Omega_env(f) = 1.67 x 10^-5 (H*/beta)^2 (kappa alpha / (1 + alpha))^2 (100/g*)^{1/3}
  (0.11 v_w^3 / (0.42 + v_w^2)) S_env(f), with kappa = kappa_phi (Eq. 12).
- Eq. (8): S_env(f) = 3.8 (f/f_env)^{2.8} / (1 + 2.8 (f/f_env)^{3.8}).
- Eq. (9): f*/beta = 0.62 / (1.8 - 0.1 v_w + v_w^2); Eq. (10): f_env = 16.5 x 10^-3 mHz (f*/beta) (beta/H*)
  (T*/100 GeV) (g*/100)^{1/6}.
[Athron23] Eq. (6.32) writes the same thing as 1.67 x 10^-5 (g*/100)^{-1/3} (kappa_coll alpha / (1 + alpha))^2
(beta/H*)^{-2} Delta(f_coll, v_w) S_coll(f, v_w), and notes that a later calculation that keeps the finite duration
of the transition "can reduce the signal by an order of magnitude" (Sec. 6.3).

**Sound waves.** The 2014 result that made this the dominant source: [HHRW14] Eq. (12), Omega_GW is approximately
(3 Pi-bar^2 / 4 pi^2) (H* tau_s) (H* R*) (1 + w)^2 Ubar_f^4, where tau_s is the lifetime of the source and R* the mean
bubble separation at collision; "Compared with the envelope approximation ... sound waves are parametrically larger by
the factor tau_s / (R* v_w)" (paraphrase of the text around Eq. 14), which with tau_s of a Hubble time is of order
beta/H*. The abstract: "We find that the compression waves in the fluid continue to be a source of GWs long after the
bubbles have merged" and "For a wide range of models the main source of the GWs produced by a phase transition is
therefore the sound the bubbles make."

The fits:
- [CapriniEtAl16] Eq. (13): h^2 Omega_sw(f) = 2.65 x 10^-6 (H*/beta) (kappa_v alpha / (1 + alpha))^2 (100/g*)^{1/3}
  v_w S_sw(f); Eq. (14): S_sw(f) = (f/f_sw)^3 [7 / (4 + 3 (f/f_sw)^2)]^{7/2}; Eq. (15): f_sw = 1.9 x 10^-2 mHz (1/v_w)
  (beta/H*) (T*/100 GeV) (g*/100)^{1/6}, "A conservative estimate" from f_sw = (2/sqrt 3) (beta / v_w) at production.
- [HHRW17] Eqs. (35) to (37): d Omega_gw / d ln k = (H_n R*) A C(s), C(s) = s^3 (7 / (4 + 3 s^2))^{7/2}, s = k R* /
  (k R*)_max; Eq. (39): A is about 0.687 Gamma^2 Ubar_f^4 Omega-tilde_gw; Eq. (24) defines Omega-tilde_gw, found to be
  "of order 10^-2", with footnote 9 giving the corrected value 1.2 x 10^-2; Eq. (43): f_p,0 is about 26 (1/(H_n R*))
  (z_p/10) (T_n / 100 GeV) (h*/100)^{1/6} micro-Hz, with z_p = (k R*)_max about 10. The abstract: "It is the sound shell
  thickness which sets the position of the peak of the power spectrum." Footnotes 5 and 6 of the paper say its Eq. (39)
  is missing a factor of 3 and its Eq. (45) prefactor contains errors; the erratum replaces the prefactor 0.687 by
  2.061 (the value [HLLP21] Eq. (8.24) and [Athron23] Eq. (6.39) carry below); use the corrected forms below.
- [CapriniEtAl20] Eq. (29): d Omega_gw,0 / d ln f = 0.687 F_gw,0 K^2 (H* R* / c_s) Omega-tilde_gw C(f / f_p,0), with
  Omega-tilde_gw about 10^-2 from simulations, F_gw,0 the redshift factor, C(s) as above (Eq. 30), and Eq. (31):
  f_p,0 about 26 (1/(H* R*)) (z_p/10) (T*/100 GeV) (g*/100)^{1/6} micro-Hz. When the source lives less than a Hubble
  time (H* tau_sh < 1, with tau_sh = R* / sqrt K the shock-formation time), Eq. (32) replaces K^2 (H* R*) by K^{3/2}
  (H* R*)^2 / c_s, that is 0.687 F_gw,0 K^{3/2} (H* R* / sqrt(c_s))^2 Omega-tilde_gw C (checked against the ar5iv
  text; the PDF is still to be checked): the signal is cut by the factor H* tau_sh.
- [HLLP21] Eq. (8.24), the "simple model": d Omega_gw,0 / d ln f = 2.061 F_gw,0 Omega-tilde_gw [(H* R*)^2 / (sqrt K +
  H* R*)] K^2 C(f / f_p,0), with Omega-tilde_gw = 0.012, F_gw,0 = (3.57 +- 0.05) x 10^-5 (100/g_eff)^{1/3} (Eq. 8.23),
  f_p,0 = 10 f_*,0 and f_*,0 about 2.62 (1/(H_n R*)) (T_n / 100 GeV) (g_eff/100)^{1/6} micro-Hz (Eq. 8.22). The 2.061
  "approximates 3 / integral d ln s C(s)". Stated validity: alpha_n below about 0.1, v_w between about 0.4 and 0.5 or
  above the Chapman-Jouguet speed, below 0.9.
- [Athron23] Eq. (6.39), the current form with the corrected prefactor: h^2 Omega_sw(f) = 2.59 x 10^-6 (g*/100)^{-1/3}
  (kappa_sw alpha / (1 + alpha))^2 (max(v_w, c_s,f) / c) (beta/H*)^{-1} Upsilon(tau_sw) S_sw(f); Eq. (6.40): f_sw =
  8.9 x 10^-6 Hz (g*/100)^{1/6} (T*/100 GeV) (c / max(v_w, c_s,f)) (beta/H*) (z_p/10). "We have included corrections to
  the numerical prefactor based on the erratum of ref. [475]. This disagrees with the numerical prefactor given in
  ref. [457] prior to the publication of the erratum and these numerical errors have also propagated into some
  literature after the erratum was published." The lifetime factor, Eq. (5.38): Upsilon = 1 - 1 / sqrt(1 + 2 H* tau_sw),
  which the review says replaces the earlier approximation Upsilon = min(1, H* tau_sw) (Eq. 5.37); and Eq. (6.36):
  tau_sw is about L* / Ubar_f = L* sqrt(Gamma / K), the time for shocks to form. Refs. [307, 374] of the review
  "include an additional efficiency factor 1 - kappa_coll to account for energy used in collisions."

**Turbulence.** [CapriniEtAl16] Eq. (16): h^2 Omega_turb(f) = 3.35 x 10^-4 (H*/beta) (kappa_turb alpha / (1 + alpha))^{3/2}
(100/g*)^{1/3} v_w S_turb(f); Eq. (17): S_turb(f) = (f/f_turb)^3 / {[1 + (f/f_turb)]^{11/3} (1 + 8 pi f / h*)}; Eq. (18):
f_turb = 2.7 x 10^-2 mHz (1/v_w) (beta/H*) (T*/100 GeV) (g*/100)^{1/6}. [Athron23] Eqs. (6.42) to (6.46) carry the
same fit with max(v_w, c_s,f) in place of v_w, f_turb = 2.7 x 10^-5 Hz (g*/100)^{1/6} (T*/100 GeV) (...) and h* =
1.65 x 10^-5 Hz (g*/100)^{1/6} (T*/100 GeV), noting the K^{3/2} dependence comes from taking the autocorrelation time to
be "the eddy circulation time for the largest scales (see Eq. (5.40))", the tau_c relation that follows being
Eq. (6.44). The review's caution on kappa_turb is quoted in Sec. 2.

**What the shapes have in common** (reading the formulas, ours). Every amplitude is (an efficiency times alpha / (1 +
alpha)) to a power, times the dimensionless length of the transition (H* R*, or (beta/H*)^{-1} or ^{-2}), times a
number of order 10^-5 to 10^-4 from the redshift and from the simulations; every peak frequency is (a number of order
1 to 10) times 1/R* at the transition, redshifted by T*. So the four inputs do two different jobs: alpha, kappa and
v_w set how much of the energy moves and how fast; beta/H* (through R*) sets the size of the moving regions, which
fixes both the frequency and, through the lifetime, the amplitude; T* only moves the whole spectrum along the
frequency axis.

## 4. What the toy measures that these formulas take as input (ours, unverified)

The toy is the four-, six- and eight-link curled-torus model of this repository (λ > 1, our family around the published
model, never CQG). The facts below are from the record; the mapping to the GW inputs is ours and has not been checked
by anyone.

**What the toy has no version of.** It has no temperature in kelvin and no clock in seconds: its coupling g plays the
part of a temperature, and its sweep is the sampler's clock, which the fair clock of ASSUMPTIONS O90 (one fair sweep =
N/96 chain sweeps) corrects only for size, not into any unit. It has no Hubble rate, no expansion, no speed of light,
no energy in GeV. **So T\*, beta/H\*, R\* in meters, the lifetime H\* tau_sw, and every number with units are out of
reach**, and with them the peak frequency today and the absolute amplitude h^2 Omega. No dimensionless ratio of the
toy's clock to a Hubble time exists to form beta/H*. (The owner's question of this morning, a translation between the
sweep clock and physical units, is a separate design question; this note only records that the GW formulas need one.)

**What the toy could stand in for, as pure numbers.**

1. **alpha, the strength.** The release per point is exact: 4(λ − 1) per curled direction with every direction costing
   the same (VISION Update 5; `test_sheet_tube_cube_ladder`), and 3a per point, a = 4(λ − 1), released all at the last
   opening under the owner's "all at the last" tie (O89, O106; VISION Update 47). The bag-model alpha is "the energy
   liberated by the phase transition" over the thermal energy already present ([Athron23] Sec. 5.3), so the toy's
   analogue would be (release per point) divided by (thermal energy per point of the old phase at the coupling g
   where the opening happens). Both numbers exist in the toy in its own units, and their ratio is dimensionless. Two
   cautions, ours. (a) The toy's "thermal energy per point" of a slab at coupling g is the equilibrium excess energy
   of the curled state at that g, which has been measured along the λ map (T8, T23, T24) only at the couplings where the
   tube was run; it is a defect energy, not a radiation bath with g* degrees of freedom, so the correspondence is a
   stand-in and no more. (b) In the formulas alpha enters only as kappa alpha / (1 + alpha), the fraction that ends in
   bulk motion; the toy has no fluid, so no kappa.

2. **The completion mode (one front or several seeds), which is what beta/H\* describes.** The formulas encode the
   duration of the transition only through the bubble separation R* = (8 pi)^{1/3} v_w / beta: a fast transition
   (large beta/H*) means many small bubbles close together; a slow one means few large bubbles. The toy measures
   exactly this distinction in its own terms: T37 saw nucleation and growth of the opening in long tubes, with relics
   growing in proportion to length where the sheet stayed clean (O88); T53 saw the "spaghetti" X open from several
   places in the long torus (SEVERAL, O105); T88 saw ONE FRONT from the fed end at 30 units a store and SEVERAL (a
   second open region ahead of the front) at 60 a store on the longer rods (O171). The dimensionless quantity the toy
   could supply is **the number of seeds per unit length of X at a given coupling and feed**, which is the toy's n_bubble
   of [HLLP21] Eq. (7.21). The earlier note (`relics_black_holes_2026-09-25.md`, item 2) already wrote the
   one-dimensional form, seed density = beta/(2v) for a rate rising as exp(beta t), and the T17 planted-seed files
   can test the binomial form of the leftover count. **What it cannot do** is turn seeds per column into beta/H*: that
   needs the length of a column in meters and the Hubble time, neither of which the toy has. And the toy's seeds so far
   appear in a tube or rod fed from a bath, not in a medium whose own temperature falls as it expands; the cosmological
   case has the nucleation rate rising as the universe cools, which is where the exp(beta t) form comes from, and the
   toy at fixed g has a constant rate instead (the KJMA case of the 25 September note).

3. **The wall speed v_w, as a shape only.** T47 part A found the front's pace steady in both baths (pace ratio inside
   the steady band at every size, O76), and the speed per sweep falls as 1/L for a reason in the clock, not the front
   (O90: 0.75 to 0.81 columns per sweep once multiplied by L). T50 found the front speeds up where energy sits (SPEEDS at
   6 and 10 units per point, no effect at 1 and 3, O93). So the toy has a front with a fixed speed in its own units, and
   a measured dependence of that speed on the energy stored ahead of it. The formulas take v_w as a fraction of the
   speed of light; the toy has no speed of light to divide by, so v_w is not supplied. The one dimensionless thing the
   toy could say is whether its front is faster or slower than the toy's own sound speed, if a sound speed were ever
   defined for it (the speed at which a small disturbance spreads through the open phase); it has not been.

4. **The fraction of the release left in walls or defects, which is what kappa_phi and (1 − kappa) describe.** In the
   formulas the energy that stays in the wall sources the collision term with efficiency kappa_phi, and the energy that
   becomes heat rather than bulk motion is lost to the GW signal ([CapriniEtAl16] Sec. 2.2; [Athron23] Sec. 5.3 and
   6.3). The toy measures a fraction of the release that is **not** returned as free energy but stays locked in
   structure: the knots. Paper 2's scrap is knots of fixed energy (the column, 14; the knot of two kinds of point, 20
   to 30; the double column, 8) whose number is set at the opening and not by the cooling (O104, O107); at the slowest
   cooling about one knot of each kind survives per three to five sheets of 1,024 points, and the energy left falls
   as (cooling time)^{-0.34} from 4 % to 1.3 % of the release (O104). So the toy can supply a dimensionless
   **defect-energy fraction of the release**, about 1 % at its slowest cooling and settable by the seed count. The
   nearest GW quantity is kappa_phi, the wall's share; but the match is loose, ours, and should not be pressed: kappa_phi
   is energy in moving walls that radiates during collisions, whereas the knots are stuck and cold and radiate nothing.
   What the toy's number more nearly resembles is the energy budget's heat term, the part that never becomes bulk
   motion, except that heat thins with expansion and knots, being a fixed number of things, would thin as matter
   does ([PWS09] by O100's reading). The toy has no fluid, so there is no kappa_v, no K, no Ubar_f, and nothing to
   put into the K^2 or K^{3/2} that every amplitude carries.

5. **Nothing for turbulence.** The toy has no fluid motion, no vorticity, and no cascade; kappa_turb has no analogue.

**Said plainly.** Of the four inputs, the toy can offer a stand-in for one (alpha, as release over the old phase's
thermal excess, in its own units), a qualitative version of a second (the completion mode behind beta/H*, as seeds
per length, without the conversion to a Hubble time), a shape without a scale for the third (a steady front that speeds
up where energy sits, without a speed of light), and nothing for the fourth beyond a fixed speed. Of the three
contributions, it bears on none directly, since all three are sourced by a fluid or by moving walls, which it does not
have; what it can supply is a dimensionless defect fraction of the release, which the formulas treat as lost energy.
Every amplitude in the literature needs K, the kinetic energy fraction of a plasma, and the toy has no plasma.

**What this reading does not change.** The toy's opening is a decay with an activation cost, not a thermal first-order
transition in a cooling bath (VISION S2′; Update 44, open item (a)); the formulas above are written for the second, and
even a complete set of the four inputs would be an analogy, not a prediction of a signal.

## 5. What paper 2 would need from this area to matter to these groups (ours)

1. A dimensionless alpha for the toy (release per point over the curled phase's thermal excess at the opening
   coupling), computed from numbers already on the record, with its definition fixed before it is read.
2. The seed count per length against coupling and feed (T17, T37, T53, T88), reported as the toy's bubble density, and
   whether its leftover count is binomial in the seeds, the test the 25 September note named and no run has yet made.
3. A statement, in one line, that the knots are a defect-energy fraction of the release of about 1 % at the slowest
   cooling, set by the seeds and not the cooling, and that this fraction has no counterpart in the GW energy budget
   because it neither moves nor radiates.
4. An explicit list of what the toy cannot supply (T*, beta/H*, v_w/c, K, any unit), so that no reader takes the
   analogy for a spectrum.
5. A map from the sweep clock to a unit of time, if one is ever decided, since without it none of the three
   dimensionless numbers above becomes a frequency or an amplitude.
