# Reading: the Koide relation on quark triplets, the phase 2/9, and the PDG 2025 masses

*Date of the reading: 2026-10-30. Who read: a fresh assistant agent (Fable 5.1), from the arXiv PDFs with the text extracted,
on the owner's instruction of this morning ("Verify." on the sentence "the form holds only roughly for some quark triplets";
"complete the listed readings"). Ordered by this session; reviewed and condensed by it. Everything below is published or PDG
unless marked inference (the agent's or ours). The arithmetic was rerun here in `sandbox/quark_koide_look.py`. Bears on
`docs/design/koide_gaps_2026-10-30.md`, gaps G2 and G6.*

**Conventions.** This project writes K = (m₁ + m₂ + m₃) / ((2/3)(√m₁ + √m₂ + √m₃)²), so Koide is K = 1. Rodejohann–Zhang and
Kartavtsev leave out the 2/3, so their Koide value is 2/3; Żenczykowski writes (1 + k²)/3 with Koide at k = 1. Numbers
below are converted to this project's K where they are quoted as ours.

## What was read, in full

| Source | Status | What it tests | What it finds (their numbers, their mass choices) |
|---|---|---|---|
| Rodejohann and Zhang, arXiv:1101.5525, Phys. Lett. B 698 (2011) 152 ("Extended Empirical Fermion Mass Relation") | FULL TEXT | (u,c,t), (d,s,b) running at M_Z; (c,b,t) pole; (u,d,s) running at M_Z | up- and down-families fail (our K ≈ 1.33 and 1.12); (c,b,t) with pole masses: their Eq. (5) "0.66 < K_heavy < 0.68 ... amazing agreement" (our K 0.99 to 1.02 at 1σ, 2010 errors); (u,d,s) at M_Z "0.49 < K_light < 0.65" (ours 0.74 to 0.98), "a small deviation ... at about 1σ". Neutrinos: light neutrinos cannot satisfy it (their K between 1/3 and 3/5); a seesaw or Majorana-phase version can, and in the inverted order predicts m_ee ≈ 0.025 eV (their Eq. 16) |
| Kartavtsev, arXiv:1111.0480 (journal not found, to verify) | FULL TEXT | the same triplets with PDG 2010 masses and with running masses at M_Z; a six-quark ratio | up and down families off by 27 % and 8 %; running makes it worse; running *leptons* at M_Z break Koide at 2 × 10⁻³ ("somewhat counterintuitive"); heavy triplet within 1 %, light off by 6 to 20 %; his remark: the six-quark ratio Σm/(Σ√m)² is 4 to 5 % below Koide at 2 GeV and 2 to 5 % above at M_Z, so "at some scale 2 GeV < μ < M_Z the quark masses satisfy (within the uncertainties) the Koide relation" |
| Żenczykowski, arXiv:1210.4125, Phys. Rev. D 86, 117303 (2012) | FULL TEXT | the Z3 parametrization √m_j = √M (1 + √2 k cos(2πj/3 + δ)); the phase alone, Eq. (8): tan δ = √3(√m_μ − √m_e)/(2√m_τ − √m_μ − √m_e) | δ_L = 0.2222324 "extremely close to 2/9" (Brannen 2006, Rosen 2007); k_L = 1 and δ_L = 2/9 give m_τ = 1776.9689 and 1776.9664 MeV, "mutually incompatible, but either ... excellent"; quarks: δ_U ≈ 2/27 = δ_L/3 from 2-GeV masses; δ_D ≈ 4/27 only "at the expected low-energy-scale value of the strange quark mass (i.e. for m_s around 160 MeV)"; proposed pattern δ_L = 2/9, δ_D = 4/27, δ_U = 2/27, δ_ν = 0; at M_Z both k_L and δ_L drift by 0.2 and 0.5 % |
| Żenczykowski, arXiv:1301.4143 (2013) | FULL TEXT | the same, "doubly special" | "possibly exact values of δ_L = 3δ_D/2 = 3δ_U = 2/9"; assumed, not derived ("we may expect that they are nearly exact. Therefore, we will assume this"); with k_U = k_D = 1 the Cabibbo-type angle comes out 2.98° against 2.37° |
| Rivero and Gsponer, hep-ph/0505220 | FULL TEXT | history; Foot's π/4 reading; Barut's ladder m(N) = m_e(1 + (3/2)α⁻¹ Σn⁴); a six-quark vector | the 1981 prediction 1.777 GeV was two standard deviations from the then-measured tau and was right; six quarks: "precision of about 5 %"; their footnote: "The ratio 283/180 being quite precisely equal to π/2 illustrates how easily one can get a good agreement with a beautiful number" (rule 13 in their words); no value of δ |
| Rosen, Mod. Phys. Lett. A 22 (2007) 283 | ABSTRACT ONLY | the 2/9 phase, extended to quarks and neutrinos with all δ = 2/9 | predicts m_t = 177.698 GeV, now excluded (PDG 172.56 ± 0.31; inference) |
| Foot, hep-ph/9402242; Koide, hep-ph/0005137; Sumino, arXiv:0812.2090 | ABSTRACT ONLY | the π/4 geometry; the cyclic matrix; a family gauge symmetry cancelling the QED correction so that Koide holds for pole masses | Sumino's is about why k = 1 survives to low energy, not about δ |
| Shulga, arXiv:2605.10245 (2026; journal to verify) | ABSTRACT ONLY | a model in which the phase is −2λ_B/9 | λ_B = 1 gives 2/9 and the author calls it "not an exact first-principles prediction" |

Search terms (WebSearch, 30 October 2026): "Zenczykowski Koide Z3 phases 2/9 2/27 quark arXiv"; "Koide relation phase 2/9
radian derivation explanation arXiv"; "Rosen Mod. Phys. Lett. A 2007 283 Koide 2/9"; "Koide 2/9 phase Brannen Koide 2007 J.
Phys. G cyclic"; "Koide charged lepton mass phase 2/9 derivation arXiv Koide Nishiura OR Sumino". INSPIRE not queried
directly. Three self-published notes claiming to derive 2/9 were seen only as snippets and are not cited.

## PDG 2025 values (Review of Particle Physics 2024 with the 2025 update; `pdg.lbl.gov/2025/tables/`)

| quantity | value | definition |
|---|---|---|
| m_e | 0.51099895000 ± 0.00000000015 MeV | pole |
| m_μ | 105.6583755 ± 0.0000023 MeV | pole |
| m_τ | **1776.93 ± 0.09 MeV** | pole; the record's 1776.86 ± 0.12 (from memory) was the older value |
| m_u, m_d, m_s | 2.16 ± 0.07, 4.70 ± 0.07, 93.5 ± 0.8 MeV | MS-bar at 2 GeV, 90 % CL |
| m_c, m_b | 1.2730 ± 0.0046, 4.183 ± 0.007 GeV | MS-bar at their own mass |
| m_t | 172.56 ± 0.31 GeV direct; 172.4 ± 0.7 pole from cross-sections; 162.5 +2.1 −1.5 MS-bar | three definitions, about 10 GeV apart |
| m_p, m_n | 938.27208816 ± 0.00000029, 939.5654205 ± 0.0000005 MeV | |
| m_π±, m_π⁰ | 139.57039 ± 0.00018, 134.9768 ± 0.0005 MeV | |
| Δm²₂₁, Δm²₃₂ | (7.50 ± 0.19) × 10⁻⁵ eV²; (2.451 ± 0.026) × 10⁻³ eV² normal, (−2.527 ± 0.034) × 10⁻³ inverted | |
| Σm_ν | no single PDG bound; listed cosmological limits 0.08 to 0.14 eV at 95 % | |

## The arithmetic (the agent's, rerun here; PDG 2025 central values, masses as PDG quotes them)

| triplet | K | distance from 1 | verdict |
|---|---|---|---|
| e, μ, τ | 0.9999967 ± 0.0000085 | −0.4σ | holds; K = 1 predicts m_τ = 1776.969 (0.4σ from 1776.93) |
| u, c, t | 1.2732 ± 0.0004 (1.2674 with t MS-bar) | 27 % | fails |
| d, s, b | 1.0969 ± 0.0011 | 10 % | fails |
| s, c, b | 0.6876 ± 0.0005 | −31 % | fails |
| c, b, t | 1.0038 ± 0.0004 (t direct); 1.0037 (t pole); 0.9939 ± 0.0019 (t MS-bar) | +0.4 % / −0.6 % | **not at 1 within any one definition's error; 1 lies between the definitions** |
| u, d, s | 0.8501 ± 0.0032 | −15 % | fails at 2 GeV |

Phases by Żenczykowski's Eq. (8) and (12) with the same inputs: δ_L = 0.2222248 (2/9 = 0.2222222; the τ error moves δ_L by
±6 × 10⁻⁶, so 2/9 is inside 1σ); δ_U = 0.0745 (2/27 = 0.0741); δ_D = 0.110 at 2 GeV (near 3/27 = 1/9, not his 4/27, which
needs m_s ≈ 160 MeV).

## Verdicts for the gaps

- **G6 (the quarks): VERIFIED as "roughly", with the number.** No quark triplet satisfies Koide within its errors. The
  nearest is (c, b, t), half a per cent off, and whether it passes depends on which of the top mass's three definitions is
  used, a spread larger than the distance to Koide. (s, c, b), which this session's expectation named as the nearest, is
  the farthest of the natural triplets. The published near-pass of 2011 was at 2010 precision with pole masses. The
  six-quark ratio crosses Koide at some scale between 2 GeV and M_Z, which is a statement about running, not a fixed law.
- **G2 (the phase): NOT DERIVED in the refereed literature.** δ_L is 2/9 within 1σ with 2025 masses; every author calls it
  "experimentally indistinguishable from 2/9" or "possibly exact"; the one model reaching it sets a free coefficient to 1.
  The quark phases sit near 2/27 (up) and near 1/9 (down, at 2 GeV), so a pattern in ninths and twenty-sevenths exists in
  the data but with one of its three entries depending on an assumed strange mass.
- **A fact the owner's parts have to carry (published, Kartavtsev; Żenczykowski):** both Koide's 2/3 and the phase 2/9 hold
  for the *pole* masses at low energy and drift by 0.2 to 0.5 % at the Z scale. A rule that fixes them at the deepest level
  would have to explain why they survive down to the measured masses and not up; Sumino's family gauge symmetry is the one
  published attempt for the 2/3.

## What would change the verdicts

A common-scale running of all six quark masses with current inputs (not done here); INSPIRE forward citations of
Żenczykowski 2012 for later phase work; Rosen 2007 in full.
