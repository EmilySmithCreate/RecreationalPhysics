# Reading note: the cosmic-time observer measure (Loeb, Batista & Sloan 2016; Bousso, Freivogel & Yang 2008) and the published inputs a Stage E model can import

**Date:** 2026-10-12. **Written against:** `docs/theory/observer_relative_histories_research_handoff.md`, section 5 ("Cosmic-time measure of observer experiences") and Stage E (the cosmological toy population model).
**Who read what:** an AI assistant, from the arXiv PDFs converted to text with `pdftotext`. Equations were transcribed from the text layer and, where a number could be checked by arithmetic, checked (marked *exact*). Nothing here has been reviewed by a physicist. Statement kinds (CLAUDE.md rule 10): **published** = what the paper says; **exact** = arithmetic we did; **ours, unverified** = our reading.

## 0. Reading status

| Source | Status | What was read (URL actually used) |
|---|---|---|
| Loeb, Batista & Sloan 2016 | **Read in full** | arXiv:1606.08448v2 PDF (`https://arxiv.org/pdf/1606.08448v2`), 11 pp, all sections and references |
| Bousso, Freivogel & Yang 2008 | **Read in full** | arXiv:0712.3324v3 PDF (`https://arxiv.org/pdf/0712.3324v3`), 15 pp, all sections and references |
| Madau & Dickinson 2014 | **Read in part** | arXiv:1403.0007 PDF: abstract; Sec. 2 (the cosmology line); Sec. 5, the passage around Eq. (15) and the Fig. 9 caption; the closing summary |
| Planck 2018 results VI | **Read in part** | arXiv:1807.06209 PDF: abstract; Table 2 (p. 16 of the PDF); Sec. 3.2, Eqs. (13) to (15) |
| Haqq-Misra, Kopparapu & Wolf 2018 | **Read in part** | arXiv:1705.07813 PDF: abstract, Sec. 1, Secs. 4 to 6 (conclusions C1 to C5) |
| Lingam & Loeb 2018; Behroozi & Peeples 2015; Zackrisson et al. 2016; Dayal, Ward & Cockell 2016; Kipping 2025; Ćirković & Balbi 2020; Lapi et al. 2024 | **Abstract only** | arXiv abstract pages (ids in Sec. 1.6) |

`REFERENCES.bib` is not edited by this note; entries for these papers are owed when any of them is cited in a tracked page.

## 1. Loeb, Batista & Sloan (2016), "Relative Likelihood for Life as a Function of Cosmic Time"

**1.1 Bibliography.** A. Loeb (Harvard), R. A. Batista and D. Sloan (Oxford). arXiv:1606.08448, v1 27 June 2016, v2 26 July 2016. *Journal of Cosmology and Astroparticle Physics* 2016(08), 040. DOI 10.1088/1475-7516/2016/08/040. Read from the v2 PDF.

**1.2 What they compute, in their words.** "the relative formation probability per unit time of habitable Earth-like planets within a fixed comoving volume of the Universe, $dP(t)/dt$, starting from the first stars and continuing to the distant cosmic future" (abstract), restricted to "life as we know it" and ΛCDM. The distribution is normalized to unit integral, so "it only compares the relative importance of different epochs for the emergence of life but does not calibrate the overall likelihood for life in the Universe" (Sec. 1). Footnote 1: "We address this question from the perspective of an observer in a single comoving Hubble volume formed after the end of inflation. As such we do not consider issues of self-location in the multiverse, nor of the measure on eternally inflating regions of space-time." **What they do not compute:** the number or duration of observers or observer-moments; a per-planet delay from habitability to life; any dependence of life's probability on time already elapsed. They say so (Sec. 4, below).

**1.3 The equations, numbered as in the paper.**

*Master equation* (Eq. 2.1):

$$\frac{dP}{dt}(t)=\frac{1}{N}\int_0^{t}dt'\int_{m_{\min}}^{m_{\max}}dm'\;\xi(m')\,\psi(t',m')\,\eta_{\rm Earth}(m')\,p({\rm life}|{\rm HZ})\,g(t-t',m'),$$

with $1/N$ fixing $\int dP = 1$. Window function: $g(t-t',m)=1$ if $0<(t-t')<\tau(m)$, else 0 (Sec. 2.1). (Ours, unverified: the paper writes $\psi(t',m')$ but Sec. 2.6 gives a $\psi$ that depends on time only, with the mass dependence carried entirely by $\xi(m)$.)

*Stellar mass range* (Sec. 2.2). $m_{\min}=0.08\,M_\odot$ (hydrogen-burning threshold). $m_{\max}$ from the minimum time life needs: planet formation took about 40 Myr [11]; the oldest zircons formed about 160 Myr after that [12]; so a conservative minimum of 200 Myr; the earliest evidence for life is about 800 Myr after Earth formed [11]. With $\tau\propto m^{-2.5}$ this gives $m_{\max}=2.8$ to $4.7\,M_\odot$ (*exact*: $(10^{10}/8\times10^8)^{1/2.5}=2.75$, $(10^{10}/2\times10^8)^{1/2.5}=4.78$). Stated as unimportant: massive stars are rare and short-lived.

*Time range* (Sec. 2.3). First stars at $z\approx70$, about 30 Myr after the Big Bang [2, 4 to 6]; the longest-lived stars last about 10 trillion years [9]; $dP/dt$ "is expected to vanish beyond that time".

*Initial mass function* (Eq. 2.2), Chabrier [14], per unit linear mass:

$$\xi(m)\propto\begin{cases}\left(\dfrac{m}{M_\odot}\right)^{-2.3} & m>1\,M_\odot\\[6pt] a\,\exp\!\left[-\dfrac{\ln^2(m/m_c)}{2\sigma^2}\right]\dfrac{M_\odot}{m} & m\le1\,M_\odot\end{cases}\qquad a=790,\ \sigma=0.69,\ m_c=0.08\,M_\odot.$$

(*Exact*: with these constants the two pieces match at $m=1\,M_\odot$ to 3 %: the lognormal piece evaluates to 0.973 against 1 for the power law, so $a=790$ is the continuity constant when the power law has unit coefficient at $1\,M_\odot$. The placement of the factor $M_\odot/m$ was read from the text layer and should be checked against the typeset PDF: *to verify*. General knowledge, to verify: Chabrier 2003, Table 1, gives $m_c=0.079\,M_\odot$, $\sigma=0.69$ for the individual-star IMF; Loeb et al. round $m_c$ to 0.08.) They "ignore the evolution of the IMF with cosmic time and its dependence on galactic environment" and "the uncertain dependence of the likelihood for habitable planets around these stars on metallicity [7]".

*Stellar lifetime* (Eq. 2.3), piecewise:

$$\tau(m)=\begin{cases}1.0\times10^{10}\,{\rm yr}\,(m/M_\odot)^{-2.5} & 0.75\,M_\odot<m<3\,M_\odot\\ 7.6\times10^{9}\,{\rm yr}\,(m/M_\odot)^{-3.5} & 0.25\,M_\odot<m\le0.75\,M_\odot\\ 5.3\times10^{10}\,{\rm yr}\,(m/M_\odot)^{-2.1} & 0.08\,M_\odot\le m\le0.25\,M_\odot\end{cases}$$

Sources: $m<0.25$ from Laughlin, Bodenheimer & Adams 1997 [9]; $0.75<m<3$ an average index $-2.5$ normalized to the Sun [16]; the middle range an interpolation enforcing continuity. (*Exact*: continuous to 1.5 % at $0.75\,M_\odot$ and 0.1 % at $0.25\,M_\odot$; $\tau(0.08)=1.07\times10^{13}$ yr, $\tau(0.15)=2.9\times10^{12}$, $\tau(0.27)=7.4\times10^{11}$, $\tau(0.49)=9.2\times10^{10}$, $\tau(0.90)=1.3\times10^{10}$ yr.) Metallicity: $Z\approx0.04$ maximizes lifetime [17]; the effect on results was "small compared to other uncertainties" and is ignored.

*Star formation rate* (Eq. 2.4), the Madau & Dickinson [18] fit (identical to MD14 Eq. 15, verified at source, Sec. 3 below):

$$\psi(z)=0.015\,\frac{(1+z)^{2.7}}{1+[(1+z)/2.9]^{5.6}}\ M_\odot\,{\rm yr}^{-1}\,{\rm Mpc}^{-3}.$$

Truncated at early times at the first stars [2]. Extrapolated into the future, "or equivalently negative redshifts $-1\le z<0$" [19]; they find the comoving rate "drops to less than $10^{-5}$ of the current rate at 56 Gyr into the future". (*Ours, unverified*: redoing that with Planck 2018 parameters and matter + Λ only gives about 74 Gyr, not 56; the difference is immaterial because they then impose the cutoff below, but the 56 is *to verify*.) To avoid an abrupt cutoff they multiply by $\exp(-t/t_1)$ with $t_1\approx50$ Gyr, the ratio of the present cold-gas reservoir [13] to the present star formation rate (a closed-box model; infall suppressed by accelerated expansion [20, 21]). A sharper $\exp(-t/t_2)$, $t_2\approx20$ Gyr, gave results "indistinguishable within the overall uncertainties".

*Probability of life on a habitable planet* (Sec. 2.7): $P({\rm life}|m)=P({\rm HZ}|m)\,P({\rm life}|{\rm HZ})$. $P({\rm HZ}|m)=\eta_{\rm Earth}$ [22]; Kepler gives $6.4^{+3.4}_{-1.1}\,\%$ for roughly solar-mass stars [23 to 25] and $24^{+18}_{-8}\,\%$ for M dwarfs [26]; because of the large uncertainties they take $\eta_{\rm Earth}$ **constant in $m$**, and it cancels in $N$. $p({\rm life}|{\rm HZ})$ is also taken **constant**: "One could suppose that the probability of life evolving on a planet increases with the amount of time that the planet exists, or that increasing the surface area of the planet should increase the likelihood of life beginning. However, given our ignorance we will set this probability factor to a constant". It too cancels.

**1.4 Results** (Sec. 3, Fig. 4; the figure's two panels are $t\,dP/dt=dP/d\ln t$ and the cumulative $P(<t)=\int_0^t(dP/dt')\,dt'$, for $m_{\min}=0.08,0.15,0.27,0.49,0.90,1.64\,M_\odot$ with $m_{\max}=3\,M_\odot$, equally spaced in $\ln m$).
- For the full range $0.08$ to $3\,M_\odot$, $dP/d\ln t$ "peaks around the lifetime of the lowest mass stars $t\sim10^{13}$ yr with a probability value that is a thousand times larger than for the Sun".
- "For mass ranges centered narrowly around a solar mass, we find that the current time indeed represents the peak."
- "a rather small extension of the mass range down to a quarter of a solar mass shifts the peak by two orders of magnitude in time into the future."
- "Evidence of life around the nearest star, Proxima Centauri ($m=0.12\,M_\odot$), for example, would indicate that our existence at or before the current cosmic time would be at the 0.1% level."
- Sec. 4: "Although our result puts the probability of finding ourselves at the current cosmic time within the 0.1% level, rare events do happen." And: "the most conservative estimate put the probability of our existence before the current cosmic time at 0.1% at most. It is likely that with more refined models this number will be reduced".

**So Loeb et al. do compute the equivalent of the handoff's $F(t_0)$**, as $P(<t_0)$ in Fig. 4 (bottom), and the number they give for the full stellar range is **about $10^{-3}$** (stated in the text as "0.1%" and "0.1% at most"; the curves for narrower ranges rise toward order unity as $m_{\min}$ approaches a solar mass, but those values are read from a log-scale plot and are *to verify*). It is the cumulative fraction of *habitable-planet-weighted life-emergence probability*, not of observer-moments.

**1.5 Stated assumptions and caveats** (their words where short). Fixed comoving volume with a fixed number of baryons; one post-inflation Hubble volume, no multiverse measure (footnote 1); IMF fixed in time; metallicity ignored; $\eta_{\rm Earth}$ and $p({\rm life}|{\rm HZ})$ constant; the future SFR an extrapolation plus an exponential cutoff. On M dwarfs (Sec. 4): if one insists life near the Sun is typical, "then we must conclude that the physical environments of low-mass stars are hazardous to life [32]. This could result, for example, from the enhanced UV emission and flaring activity of young low-mass stars, which is capable of stripping rocky planets of their atmospheres [33]." Tidal locking is **not** mentioned in the paper (it appears in the later Haqq-Misra et al. and Lingam & Loeb). The lower mass cutoff is parameterized simply as $m_{\min}$, scanned over the six values above; there is no habitability weight that varies smoothly with mass. Two refinements they name and do not do, both of which "push the peak to the future": (i) life starting as a Poisson process rather than immediately on habitability; (ii) "re-weighting by the number observers on a planet. Although this may reach some theoretical peak, populations are at best exponentially suppressed to the past, and so a given observer (as opposed to inhabited planet) would be more likely to exist later on in a planet's existence." Also unmodeled: moons [40], asteroid belts [41], system architecture, binaries [42], galactic location [43], galaxy type and metallicity [15, 44], quasars, gamma-ray bursts [45], cluster gas.

**1.6 Responses and related work found by search** (Semantic Scholar lists 69 citing papers; the ones below bear on the handoff; none is a formal rebuttal in JCAP).
- **Haqq-Misra, Kopparapu & Wolf 2018**, "Why do we find ourselves around a yellow star instead of a red star?", *Int. J. Astrobiology* 17, 77 to 86, arXiv:1705.07813 (read in part). Quotes Loeb et al.'s closing question and answers it with Bayesian posterior odds on the *hypothesis* (which star type hosts observers), not on time. With $N_G/N=0.07$, $N_K/N=0.12$, $N_M/N=0.77$ and habitable-zone widths, C1: at the present era a G dwarf is expected, "about a ninety percent lower likelihood" of an M dwarf today. Including time, with main-sequence fractions $f_G=10^{-3}$, $f_K=10^{-2}$, $f_M=1$ (Sec. 6, Eq. 14): $P(G|L)\approx5.6\times10^{-4}$, $P(M|L)\approx0.99$, and C3: "Our existence around a G-dwarf star is unlikely, with over a hundred times greater likelihood of existing around an M-dwarf star in the future." C4: with M dwarfs inhospitable, about four times more likely around a K dwarf in the future. C5: "If observers in our operational reference class do not exist in the future, then our existence around a G-dwarf star at the present era is to be expected." *Ours*: C3 is Loeb et al.'s result restated in Bayesian form; the paper's resolution is to change the reference class, which is the handoff's own point about reference classes.
- **Lingam & Loeb 2018**, "Is Life Most Likely Around Sun-like Stars?", *JCAP* 05, 020, arXiv:1710.11134 (abstract only). Adds atmospheric erosion by stellar winds and biologically active UV: "planets orbiting most M-dwarfs are not likely to host life"; highest probability of complex biospheres around K and G stars; "the current existence of life near the Sun is slightly unusual, but not significantly anomalous." *Ours*: the first author of the 2016 paper reversing its headline under the red-dwarf-suppressed scenario.
- **Kipping 2025**, "Solar Hegemony: M-Dwarfs Are Unlikely to Host Observers Such as Ourselves", arXiv:2510.01215, submitted to AAS Journals (abstract only). Bayesian model with two explanations (a critical stellar mass below which no observers arise; a shorter observer window); chance disfavored with a Bayes factor of about 1600; needs $M_{\rm crit}>0.34\,M_\odot$ (2σ) when the window is fixed at 10 Gyr. Does not cite Loeb et al. in the abstract.
- **Ćirković & Balbi 2020**, "Copernicanism and the typicality in time", *Int. J. Astrobiology* 19, 101 to 109, arXiv:1907.08947 (abstract only). Argues "typicality in time" is "not, and cannot ever be, well-defined" without a restricting context (e.g. within the Sun's lifetime); does not conclude we are atypical. Bears directly on $p(t\mid\text{sampled observer-moment})$.
- **Behroozi & Peeples 2015**, "On the history and future of cosmic planet formation", *MNRAS* 454, 1811, arXiv:1508.01202 (abstract only). The Solar System formed after 80 % of existing Earth-like planets; the Universe "will form over 10 times more planets than currently exist"; "at least a 92% chance that we are not the only civilisation the Universe will ever have." *Ours, exact from those two abstract numbers*: Earth formed before roughly $1-0.8/11\approx93\,\%$ of all Earth-like planets that will ever form; a planet-count cumulative fraction of order 0.07 at $t_0$, to compare with Loeb et al.'s habitable-planet-years $10^{-3}$. Both are inputs to, not values of, an observer-moment $F(t_0)$.
- **Zackrisson et al. 2016**, "Terrestrial planets across space and time", *ApJ* 833, 214, arXiv:1602.00690 (abstract only): about $1\times10^{19}$ terrestrial planets around FGK stars and $5\times10^{20}$ around M dwarfs in the observable Universe; mean ages $7\pm1$ and $8\pm1$ Gyr. **Dayal, Ward & Cockell 2016**, arXiv:1606.09224 (abstract only): weighting by harmful radiation from supernovae, GRBs and AGN, the Universe is "2.5 to 20 times more habitable today" than when life appeared on Earth. **Lapi et al. 2024**, "Semi-empirical estimates of the cosmic planet formation rate", *Galaxies*, arXiv:2408.08611 (abstract only): about $10^{20}$ Earth-like and $10^{18}$ habitable Earths in the past light cone.
- General knowledge, to verify: no published comment or erratum on the JCAP paper was found; the "0.1 %" figure propagated through press coverage (Harvard Gazette, CfA release, August 2016) which also recorded Loeb's own two readings ("we're premature" or "low-mass stars are hazardous").

## 2. Bousso, Freivogel & Yang (2008), "Boltzmann babies in the proper time measure"

**2.1 Bibliography.** R. Bousso, B. Freivogel, I-S. Yang (UC Berkeley and LBNL). arXiv:0712.3324, v1 20 Dec 2007, v3 2 Apr 2008. *Phys. Rev. D* 77, 103514 (2008). DOI 10.1103/PhysRevD.77.103514. Read from the v3 PDF.

**2.2 The proper time measure** (Sec. II). Choose a small spacelike patch $\Sigma_0$ orthogonal to at least one eternally inflating geodesic; build Gaussian normal coordinates along the orthogonal geodesic congruence so that an event has time $t$ if it occurs at proper time $t$ along its geodesic; count only observations between $\Sigma_0$ and $\Sigma_t$. With $N_i(t)$ the number of completed observations of type $O_i$ in that four-volume,

$$\frac{p(O_1)}{p(O_2)}=\lim_{t\to\infty}\frac{N_1(t)}{N_2(t)},\quad(1)\qquad \frac{dp/dT|_{T_1}}{dp/dT|_{T_2}}=\lim_{t\to\infty}\frac{dN/dT|_{T_1}(t)}{dN/dT|_{T_2}(t)}.\quad(2)$$

At late times $N_i(t)\propto\exp(3H_{\rm big}t)$ with $H_{\rm big}$ the largest Hubble rate in the landscape (Planckian, $H_{\rm big}\sim O(1)$), so $\lim N_1/N_2=\lim\dot N_1/\dot N_2$ (Eq. 3): counting totals, rates, or a recent fixed-width window gives the same answer. Caveats they state: Gaussian normal coordinates fail at caustics, so they consider "only expanding spacetime regions and ignoring clustering and inhomogeneities (and thus, strictly speaking, all known observers)"; "we will assume that the local counting of observations is unambiguous" (footnote 2); geodesics through the nucleation region are dropped.

**2.3 Geometry** (Sec. III). Outside: flat de Sitter slicing $ds^2=-dt^2+H_{\rm out}^{-2}e^{2H_{\rm out}t}d\mathbf x^2$ (Eq. 4). Inside a Coleman–De Luccia bubble: open FRW, $ds^2=-d\tau^2+a(\tau)^2(d\xi^2+\sinh^2\xi\,d\Omega_2^2)$ (Eq. 5), with the constant-$\tau$ (constant-density) slices the physically preferred ones. The "square bubble approximation" sets $\tau=t-t_{\rm nuc}$ (Eq. 6) and a flat finite patch (Eq. 7). Their exact treatment (Eqs. 8 to 33) gives

$$t-t_{\rm nuc}=\tau+H_{\rm out}^{-1}\left(\xi+e^{-\xi}-1+\dots\right)\quad(33)$$

and the geodesics become comoving in a time of order $H_{\rm out}^{-1}$ (Eq. 26). They set $H_{\rm out}=H_{\rm big}$ (Eq. 34) by assuming our vacuum is produced directly from the fastest-inflating one.

**2.4 The youngness paradox, with its numbers** (Sec. IV). Number of bubbles of our type produced before $t$: $n(t)=C\exp(3H_{\rm big}t)$ (Eq. 35). Observations in one bubble: $dN^{(1)}=f(\tau)\,d\tau\,dV_y$ (Eq. 36), $f(\tau)$ "can be thought of as an observer density" per comoving volume per FRW time. Then $dp/d\tau\equiv\lim_{t\to\infty}dN(t)/d\tau$ (Eq. 37), $dN(t)/d\tau=f(\tau)V_y\exp[3H_{\rm big}(t-\tau)]$ (Eq. 38), and

$$\frac{dp}{d\tau}\propto f(\tau)\,\exp(-3H_{\rm big}\tau).\quad(39)$$

"In our universe, it is reasonable to assume that $f(\tau)$ has a broad (at least Gyr-scale) peak at some $\tau_{\rm peak}\sim O(10\,{\rm Gyr})$, since at early times, there was no structure, and at late times, there will be no free energy. In any case, there will be no features in $f(\tau)$ that can possibly compete with the exponential factor." With Planckian $H_{\rm big}$:

$$\frac{f(13\,{\rm Gyr})}{f(13.7\,{\rm Gyr})}\,\exp(10^{60})\approx\exp(10^{60})\quad(40)$$

observers at 13 Gyr for every one like us (Sec. I.C states the same as $\exp(3\times0.7\,{\rm Gyr}/H_{\rm big}^{-1})$, and "the probability for an observer to live as late as we do is $\exp(-10^{60})$"; *exact*: $3\times0.7\,{\rm Gyr}/t_{\rm Planck}\approx1.2\times10^{60}$). The exact bubble geometry gives the same $\tau$-distribution, Eq. (53) $=$ Eq. (39), factorized from a spatial distribution $dp/d\xi\propto\sinh^2\xi\,\exp[-3(\xi+e^{-\xi}-1+\dots)]$ (Eq. 54) peaked at $\xi\sim1$, with an effective comoving volume $V_{\xi,{\rm eff}}=4\pi\int_0^\infty d\xi\,\sinh^2\xi\,e^{-3(\xi-1+e^{-\xi})}\approx15.75$ (Eq. 55).

*Observable form* (Sec. IV.B, following Tegmark [37]): $dp/dT=\int d\tau\,(dp/d\tau)\,g(T|\tau)$ (Eq. 41) with $g(T|\tau)\approx T_{\rm av}(\tau)^{-1}\exp[-10^{10}((T-T_{\rm av}(\tau))/T_{\rm av}(\tau))^2]$ (Eq. 42; the $10^{10}$ from the amplitude of density perturbations), $T_{\rm av}(\tau_1)/T_{\rm av}(\tau_2)=(\tau_2/\tau_1)^{2/3}$ (Eq. 44). Since $\exp(-3H_{\rm big}\tau)$ dominates, the integral sits at the earliest allowed time; ignoring observers before 10 Gyr, $dp/dT\propto g(T|\tau=10\,{\rm Gyr})\propto\exp[-10^{10}((T-3.3\,{\rm K})/3.3\,{\rm K})^2]$ (Eq. 46): a 3.3 K background, "ruled out at great confidence by our observation that $T=2.7$ K", and worse as the early cutoff is lowered.

**2.5 "Boltzmann babies"** (Sec. I.C): "even observers just one minute younger (relative to their big bang) are superexponentially more probable than we are. ... Because of the exponential pressure to be young, it pays to arise from a rare quantum fluctuation in the early universe. The most likely observers are such 'Boltzmann babies', and the most likely observations are the phenomena of the hot, dense, early universe they see."

**2.6 Modifications tried and why each fails** (Sec. V). (A) "Don't ask, don't tell" (Linde [16]): compute only reheating-surface rates; incomplete, forbids counting observers (and so the anthropic Λ argument), and still favors short inflation. The general fix proposed in Linde [38] is a correction factor $P(O_1)/P(O_2)=[p(O_1)/p(O_2)]\exp[3H_{\rm big}(\Delta t_1-\Delta t_2)]$ (Eq. 57) with $\Delta t_i$ the time to produce the observation; four definitions are tried. (B) Spatial averaging: $\Delta t(T)=(13.7\,{\rm Gyr})(2.7\,{\rm K}/T)^{3/2}$ (Eq. 59). Without fluctuations it gives the intuitive $dP/dT\propto f(T)$ (Eq. 63); with fluctuations $dP/dT\propto\exp[10^{61}((3.3\,{\rm K}/T)^{3/2}-1)-10^{10}((T-3.3\,{\rm K})/3.3\,{\rm K})^2]$ (Eq. 66), driving $T$ to the lowest value: "overcompensates", ruled out. (C) Waiting for the first time: probabilities stop adding, $P_1+P_2>P_{12}$ (Eq. 68); in a stationary start $P_i/P_j=(Vp_i+1)/(Vp_j+1)$ (Eq. 71), no correction at large $V$, all outcomes equal at $V\to0$. (D) "Growing together": the defined $\Delta t_i$ is independent of $T$ to accuracy $H_{\rm big}^{-1}$, so nothing changes. (E) Anticipation (project each observation back to the bubble wall): removes youngness but is not sharply defined and makes **Boltzmann brains** dominate "with probability 1" [19, 20, 44], because "Boltzmann brains arise at a fixed rate per unit time and unit physical volume, not per comoving volume. Thus, the comoving observer density $f(\tau)$ grows exponentially with the scale factor at extremely late times, so $f(T)$ diverges at the Hawking temperature of the de Sitter space." Eq. (63), they say, "is a poisoned chalice". **Conclusion** (abstract): "We consider a number of modifications of the proper time measure, but find none that would make it compatible with observation." Measures that fared well in their account: the causal diamond measure [9, 25, 26, 27].

**2.7 Typicality** (Sec. I.A). They argue for assuming typicality "on empirical grounds" and against Hartle & Srednicki [1], whose prescription (probability that some laboratory somewhere sees the outcome, $1-(1-\epsilon)^L$) "would put an end to experimental science" because $L$ is unknown. The handoff's reading list item 11 (Hartle & Srednicki 2007) is the other side of this argument; the handoff itself sides with caution ("a proposed xerographic/self-location distribution"). Both positions are on the record here.

## 3. Madau & Dickinson (2014), Eq. (15), verified at source

P. Madau and M. Dickinson, "Cosmic Star-Formation History", *Annu. Rev. Astron. Astrophys.* 52, 415 to 486 (2014), arXiv:1403.0007, DOI 10.1146/annurev-astro-081811-125615. Read in part. Sec. 5 ("From observations to general principles"), text after the Fig. 9 caption:

$$\psi(z)=0.015\,\frac{(1+z)^{2.7}}{1+[(1+z)/2.9]^{5.6}}\ M_\odot\,{\rm year}^{-1}\,{\rm Mpc}^{-3}.\quad(15)$$

Published context needed to use it: a **Salpeter (1955) IMF from 0.1 to 100 $M_\odot$** throughout (FUV and IR luminosities converted with $K_{\rm FUV}=1.15\times10^{-28}$, Eq. 10, and $K_{\rm IR}=4.5\times10^{-44}$, Eq. 11; Chabrier or Kroupa values are rescaled to Salpeter by dividing by 0.63 or 0.67); a flat cosmology with $(\Omega_M,\Omega_\Lambda,\Omega_b,h)=(0.3,0.7,0.045,0.7)$ (Sec. 2); the fit rises as $(1+z)^{-2.9}$ at $3<z<8$, peaks "at $z\approx1.85$" (summary; "between $z=2$ and 1.5, when the Universe was $\sim3.5$ Gyr old"), and the $z<1$ data are "also fit quite well by an exponential decline with cosmic time and an e-folding timescale of 3.9 Gyr"; it "produces 20% fewer stars by $z=0$" than the Behroozi et al. (2013) fit. (*Exact*: the formula peaks at $z=1.86$ with $\psi=0.133$, 8.9 times $\psi(0)=0.015$; the review's words are "a peak rate approximately nine times higher than is seen today".) *Ours, unverified*: Loeb et al. apply a Salpeter-calibrated SFRD with a Chabrier $\xi(m)$; since both are normalized away in $N$, only the shape in time matters, but a Stage E model that wants absolute planet counts must rescale (MD14's 0.63 factor) and should say so.

## 4. Planck 2018 results VI, Table 2, TT,TE,EE+lowE+lensing (the baseline column)

Planck Collaboration (N. Aghanim et al.), "Planck 2018 results. VI. Cosmological parameters", *A&A* 641, A6 (2020), arXiv:1807.06209, DOI 10.1051/0004-6361/201833910. Read in part. Table 2 (68 % intervals; verified by re-extracting the page without layout so that each column reads in order):

| Parameter | Value |
|---|---|
| $\Omega_b h^2$ | $0.02237\pm0.00015$ |
| $\Omega_c h^2$ | $0.1200\pm0.0012$ |
| $100\,\theta_{\rm MC}$ | $1.04092\pm0.00031$ |
| $\tau$ | $0.0544\pm0.0073$ |
| $\ln(10^{10}A_s)$ | $3.044\pm0.014$ |
| $n_s$ | $0.9649\pm0.0042$ |
| $H_0$ [km s$^{-1}$ Mpc$^{-1}$] | $67.36\pm0.54$ (also Eq. 14) |
| $\Omega_\Lambda$ | $0.6847\pm0.0073$ (also Eq. 15) |
| $\Omega_m$ | $0.3153\pm0.0073$ |
| $\Omega_m h^2$ | $0.1430\pm0.0011$ |
| $\sigma_8$ | $0.8111\pm0.0060$ |
| Age [Gyr] | $13.797\pm0.023$ |
| $z_{\rm re}$ | $7.67\pm0.73$ |
| $z_*$ | $1089.92\pm0.25$ |
| $z_{\rm eq}$ | $3402\pm26$ |

Eq. (13) gives the TT,TE,EE+lowE values without lensing: $H_0=67.27\pm0.60$, $\Omega_m=0.3166\pm0.0084$. The paper stresses these "assume the base-ΛCDM cosmology with minimal neutrino mass" and are "highly model dependent".

**Redshift to cosmic time** (standard; textbook, e.g. Hogg 1999, arXiv:astro-ph/9905116, lookback-time integral, to verify the equation number):

$$t(z)=\frac{1}{H_0}\int_z^\infty\frac{dz'}{(1+z')\,E(z')},\qquad E(z)=\sqrt{\Omega_r(1+z)^4+\Omega_m(1+z)^3+\Omega_\Lambda},$$

and, with matter and Λ only, the closed form $t(z)=\dfrac{2}{3H_0\sqrt{\Omega_\Lambda}}\,\operatorname{arsinh}\!\left[\sqrt{\Omega_\Lambda/\Omega_m}\,(1+z)^{-3/2}\right]$. (*Exact*, with the Table 2 values and $1/H_0=977.79/67.36$ Gyr: the integral with $\Omega_r h^2=4.15\times10^{-5}$ gives 13.795 Gyr; matter + Λ only gives 13.801 Gyr; the closed form agrees; Planck's own 13.797 is reproduced. MD14's peak $z=1.85$ falls at $t=3.52$ Gyr; $z=1.3$ at 4.80 Gyr; $z=0.7$ at 7.29 Gyr.) In the future ($a>1$, $-1<z<0$) the same formulas hold with $(1+z)=1/a$, and $a(t)=(\Omega_m/\Omega_\Lambda)^{1/3}\sinh^{2/3}\!\left(\tfrac32\sqrt{\Omega_\Lambda}H_0t\right)$ for matter + Λ.

## 5. Mapping against handoff Section 5 and Stage E

| Handoff construction | Verdict | Where, and what differs |
|---|---|---|
| Finite comoving reference region | **STANDARD** | Loeb et al. Secs. 1 and 2.1 ("a fixed comoving volume which contains a fixed number of baryons"); Bousso et al. $V_y$ per bubble, Eq. (36), which "will drop out of probabilities" |
| $n_{\rm obs}(\alpha,\mathbf x,t)$, a rate of observer-moments not defined solely as planets | **NOVEL CONJECTURE** as a definition; the published object is a *planet* rate | Loeb et al. define their integrand from habitable Earth-like planets with constant $\eta_{\rm Earth}$ and $p({\rm life}|{\rm HZ})$; Bousso et al. leave $f(\tau)$ ("an observer density") unspecified beyond "a broad Gyr-scale peak". No paper here models observer duration, number per planet, or interactions |
| $W(t)=\sum_\alpha p_\alpha\int n_{\rm obs}\,dV$ | **SIMPLIFYING ASSUMPTION** on top of a STANDARD object | Bousso et al. Eq. (36): $f(\tau)$ is exactly $W$ per comoving volume in one history. The sum over decoherent histories weighted by $p_\alpha$ is the handoff's addition; neither paper sums over branches (Loeb et al. footnote 1 explicitly declines any multiverse measure) |
| Loeb et al.'s $dP/dt$ as a baseline $W(t)$ | **STANDARD form, with one reading to state** | *Ours, unverified*: because $g$ is a top hat over the whole lifetime, Eq. (2.1) integrates to the number of habitable Earth-like planets *alive* at $t$ per comoving volume (not forming at $t$). Read as a life-emergence rate it assumes a constant hazard per habitable planet-year; read as an observer-moment rate it assumes constant observer-moments per habitable planet-year. The curve is the same; Stage E should name which reading it uses |
| $p(t\mid\text{sampled observer-moment})=W/\int W$ | **SIMPLIFYING ASSUMPTION** (self-sampling), contested in print | Loeb et al. normalize the same way (their $1/N$). Bousso et al. Sec. I.A defend typicality against Hartle & Srednicki; Ćirković & Balbi 2020 argue typicality in time is not well defined without a restricting context; Haqq-Misra et al. 2018 resolve the same question by choosing the reference class (C5). The handoff's "proposed xerographic distribution, not a theorem" matches Srednicki & Hartle's framing (reading list item 6, not read here) |
| $F(t_0)=\int_0^{t_0}W/\int_0^\infty W$ | **STANDARD** (computed by Loeb et al.) | Fig. 4 bottom panel, $P(<t)$; the published value for the full stellar range is about $10^{-3}$ (text: "0.1%", "0.1% at most"). For planets rather than planet-years, Behroozi & Peeples 2015 imply order 0.07 (ours, from their abstract). No published number exists for observer-moments |
| $T_{\rm support}(\alpha)$, last time of observer-supporting conditions | **SIMPLIFYING ASSUMPTION** with published anchors | Loeb et al. Sec. 2.3: $dP/dt$ "is expected to vanish" beyond the $\sim10^{13}$ yr lifetime of $0.08\,M_\odot$ stars [9]; their SFR cutoff $e^{-t/t_1}$, $t_1\approx50$ Gyr. Bousso et al. Sec. IV.A: "at late times, there will be no free energy". Neither defines a sterility time; the handoff's indicator $\mathbf 1[T_{\rm support}\le t]$ is new |
| $F_{\rm sterile}(t)$ and $t_{99.99}$ | **NOVEL CONJECTURE** (a definition, not in either paper) | Nothing published here. Bousso et al. Sec. V.E is the published reason it may not exist: Boltzmann brains at a fixed rate per physical volume make the comoving $f(\tau)$ grow as $a^3$ and $f(T)$ diverge at the de Sitter temperature. The handoff's own caveat ("a finite sterility cutoff need not exist") is this result, and should cite it |
| Baseline stellar-life scenario | **STANDARD ingredients** | Eqs. (2.1) to (2.4) of Loeb et al.; MD14 Eq. (15); Planck Table 2. Delays to biology (200 to 800 Myr) enter only through $m_{\max}$; evolutionary delay as a per-planet lag and observer duration are not in the paper |
| Red-dwarf-friendly scenario | **STANDARD** (it is Loeb et al.'s headline) | $m_{\min}=0.08\,M_\odot$: peak at $t\sim10^{13}$ yr, a thousand times the Sun's; the handoff's "order $10^{13}$ years for potential life emergence, not proven observer-moment dominance" is the right reading of Fig. 4 |
| Red-dwarf-suppressed scenario | **STANDARD** as a knob; the physics is in later papers | Loeb et al. implement it only as a larger $m_{\min}$ (0.15 to 1.64 $M_\odot$); the mechanisms (UV, flares, atmosphere loss [32, 33]; tidal locking and stellar winds in Lingam & Loeb 2018; Kipping 2025's $M_{\rm crit}>0.34\,M_\odot$) are published elsewhere |
| Interactions and civilizations sensitivity | **NOVEL CONJECTURE** (parameterized speculation, as the handoff says) | Not in either paper. Loeb et al. name "re-weighting by the number observers on a planet" as a refinement that would push the peak later; Haqq-Misra et al. define an "operational reference class" of SETI-communicable observers |
| Late-time stress test (normalizability; exotic or very late observers) | **STANDARD caution** | Bousso et al. Secs. I.B and V.E (Boltzmann brains, Refs. [19, 20, 44]); the proper-time result that no finite-time feature of $f(\tau)$ competes with an exponential. Loeb et al. assume normalizability by construction (vanishing after $10^{13}$ yr) |
| Observer worldline proper time in $r_i$ | **SIMPLIFYING ASSUMPTION**, flagged by Bousso et al. | Sec. III.A: the preferred constant-density FRW time $\tau$ is not the congruence's proper time $t$; observables correlate with $\tau$. In a homogeneous FLRW toy, comoving proper time $=\tau$, so the handoff's choice is the published one; it breaks only for non-comoving or clustered observers (which Bousso et al. drop, Sec. II) |

## 6. What contradicts or complicates the handoff

1. **$F(t_0)$ already exists in print, with a number, for the wrong reference class.** Loeb et al.'s $P(<t_0)\approx10^{-3}$ (full stellar range) is the cumulative share of habitable-planet-years, not of observer-moments. The handoff must not quote it as an observer-moment percentile; it is the natural **baseline** for Stage E, with the reading in Sec. 5 stated. Haqq-Misra et al.'s C3 (over a hundred to one for an M-dwarf future) is the same arithmetic in Bayesian dress.

2. **Bousso et al.'s youngness result does not transfer to the handoff's $F(t_0)$, and that is a point in the handoff's favor, with one caution.** The $\exp(-3H_{\rm big}\tau)$ in Eq. (39) comes entirely from the exponentially growing *number of bubbles* under a global proper-time cutoff (Eq. 35); within one bubble, with a finite comoving region and no bubble counting, their Eq. (36) reduces to the handoff's $W(t)$ and their $dp/d\tau$ to $W/\int W$. Loeb et al. footnote 1 makes the same restriction. **Caution:** Bousso et al. call exactly that intuitive object (Eq. 63) "a poisoned chalice" because late-time fluctuation observers make $\int W$ diverge. So the handoff's $F(t_0)$ is well defined only if the reference class excludes Boltzmann-brain-type observers or $T_{\rm support}$ is imposed by hand; the handoff's late-time stress test should say which, and cite Sec. V.E.

3. **Typicality in time is itself contested.** Bousso et al. (for) and Hartle & Srednicki, Ćirković & Balbi (against or "ill-defined") disagree in print. The handoff's phrasing ("a proposed self-location distribution") is consistent with the latter; a Stage E report should present $F(t_0)$ under at least two reference classes, as Haqq-Misra et al.'s C3 against C5 does.

4. **The red-dwarf question is where the published answer moved after 2016.** Lingam & Loeb 2018 (the same first author) and Kipping 2025 both land on the red-dwarf-suppressed side; Haqq-Misra et al. 2018 show the G-dwarf present is "expected" once M dwarfs are excluded. Stage E's two red-dwarf scenarios therefore bracket the live literature rather than a settled baseline.

5. **Small discrepancies to carry, none load-bearing.** Loeb et al.'s "56 Gyr" for $\psi$ to fall to $10^{-5}$ of today's is not reproduced by our Planck-parameter extrapolation (about 74 Gyr; different $a(t)$ or cosmology; to verify); their SFRD is Salpeter-calibrated while their IMF is Chabrier (shape-only use makes this harmless); Eq. (2.2)'s $1/m$ placement is read from a text layer (to verify against the typeset PDF); the plotted $P(<t_0)$ values for $m_{\min}>0.08\,M_\odot$ are not stated in the text and must be read off a log plot or recomputed.

## 7. Published equations and parameters a Stage E model can import (one line each)

- Loeb et al. Eq. (2.1): master convolution; window $g(t-t',m)=\mathbf 1[0<t-t'<\tau(m)]$.
- Loeb et al. Eq. (2.2): Chabrier IMF, $a=790$, $\sigma=0.69$, $m_c=0.08\,M_\odot$, slope $-2.3$ above $1\,M_\odot$.
- Loeb et al. Eq. (2.3): lifetimes $1.0\times10^{10}\,m^{-2.5}$ / $7.6\times10^{9}\,m^{-3.5}$ / $5.3\times10^{10}\,m^{-2.1}$ yr on $(0.75,3)$ / $(0.25,0.75]$ / $[0.08,0.25]\,M_\odot$.
- Loeb et al. Eq. (2.4) $=$ MD14 Eq. (15): $\psi(z)=0.015(1+z)^{2.7}/\{1+[(1+z)/2.9]^{5.6}\}\ M_\odot\,{\rm yr}^{-1}{\rm Mpc}^{-3}$, Salpeter 0.1 to 100 $M_\odot$; future cutoff $e^{-t/t_1}$, $t_1\approx50$ Gyr (alternative 20 Gyr).
- Loeb et al. Secs. 2.2, 2.3, 2.7: $m_{\min}=0.08\,M_\odot$ (scan 0.08, 0.15, 0.27, 0.49, 0.90, 1.64); $m_{\max}=3\,M_\odot$ (2.8 to 4.7 allowed); first stars 30 Myr; $\eta_{\rm Earth}$ 6.4 % (solar) and 24 % (M dwarf) from Kepler, used as a constant.
- Planck 2018 Table 2 (baseline column): $H_0=67.36\pm0.54$, $\Omega_m=0.3153\pm0.0073$, $\Omega_\Lambda=0.6847\pm0.0073$, age $13.797\pm0.023$ Gyr; $t(z)$ integral and closed form of Sec. 4.
- Bousso et al. Eqs. (36), (37), (39): $f(\tau)$ as the one-history observer density; the global measure multiplies it by $\exp(-3H_{\rm big}\tau)$; Eq. (40) and the $\exp(-10^{60})$ for an observer as late as us; Eq. (46), the 3.3 K prediction; Sec. V.E, the late-time divergence of $f$.
- Haqq-Misra et al. 2018: $N_G/N=0.07$, $N_K/N=0.12$, $N_M/N=0.77$; $f_G=10^{-3}$, $f_K=10^{-2}$, $f_M=1$; conclusions C1 to C5 as alternative reference-class readings.
