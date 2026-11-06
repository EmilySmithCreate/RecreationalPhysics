# Reading: Brannen (2006), "The Lepton Masses", and his neutrino prediction

*Date of the reading: 2026-10-30. Who read: a fresh assistant agent (Fable 5.1), from the preprint's own PDF
(http://brannenworks.com/MASSES2.pdf, 7 pages, FULL TEXT) and the papers that take it up, on the owner's instruction
("Read." on gap G5 of `docs/design/koide_gaps_2026-10-30.md`). Ordered by this session; reviewed and condensed by it.
Published unless marked inference (the agent's) or ours.*

## The form and the fit (Brannen 2006, Sec. I)

The circulant matrix Γ(μ, η, δ) with eigenvalues λ_n = μ(1 + 2η cos(δ + 2nπ/3)) (his Eq. 4); with η² = 1/2 the eigenvalues
taken as √m give Koide's relation (Eqs. 8 and 9). Fitted on all three charged leptons (Eq. 14): μ₁ = 17716.13(109) eV^½,
η₁² = 0.500003(23), δ₁ = 0.2222220(19) rad. Assuming Koide exact and fitting electron and muon only (Eqs. 17, 18):
μ₁ = 17715.99225(79) eV^½, δ₁ = 0.22222204715(312); predicted m_τ = 1776.968921(158) MeV (Eq. 12). These are the numbers
`sandbox/koide_brannen_look.py` reproduces.

**On 2/9.** Not claimed exact and not derived: "a new coincidence is that δ₁ is close to 2/9, a fact that went unnoticed
until this author discovered it in 2005"; "The near compatibility of the charged lepton masses with respect to η² = 1/2 and
δ₁ = 2/9 is difficult to explain. The values seem too close to be accidental. Perhaps these are the first order values and
there are second order corrections". He shows that η² = 1/2 and δ = 2/9 cannot both be exact given m_e and m_μ (the
difference is at the 10⁻⁶ level in δ). "δ₁ is close to a rational number, while the other terms that are added to it inside
the cosine of Eq. (4) are rational multiples of pi."

## The neutrino prediction (Secs. II, V, VI)

Two stages, and the count of constants matters (rule 13):

1. **Stage 1, a fit.** Earlier attempts to put neutrinos into Koide failed because every square root was taken positive;
   Brannen lets the lightest neutrino's root be negative, imposes η₀² = 1/2 and fits μ₀ and δ₀ to the two 2005 oscillation
   splittings (7.92 × 10⁻⁵ and 2.4 × 10⁻³ eV²). Two constants, two data points: "It is not a surprise that adding the
   freedom of negative square roots to the Koide relation allows the oscillation data to be fitted". Output: the absolute
   masses, m₁ = 0.000388(46), m₂ = 0.00895(17), m₃ = 0.0507(30) eV; μ₀ = 0.1000(26) eV^½, δ₀ = 0.486(21).
2. **Stage 2, two integers read off the fit.** (μ₁/μ₀)² = 3.14(16) × 10¹⁰ = (2.9999(71))²², and δ₁ − δ₀ = −0.264(21) =
   −π/12 × 1.008(80) (Eqs. 59, 60). He then sets μ₀ = μ₁/3¹¹ and δ₀ = δ₁ + π/12 exactly, with a reason offered for the
   24 (the tribimaximal mixing matrix in his basis "is a 24th root of unity", Eq. 53) and none for the 3. The masses become
   m₁ = 0.000383462, m₂ = 0.00891349, m₃ = 0.0507118 eV (Eqs. 61 to 63), Σ = 0.0600 eV, splittings 7.9303 × 10⁻⁵ and
   2.49224 × 10⁻³ eV² (Eqs. 64, 65), "dead in the center of the error bars". *Inference (the agent's, and ours):* the two
   integers were chosen after the stage-1 numbers were seen, so stage 2 is a sharpened postdiction of the same two
   splittings; what it genuinely predicts is the absolute masses, their sum, the normal ordering and one negative root.

**The phase shift, precisely:** δ_ν = δ_e + π/12, i.e. 2/9 + 1/24 turn ≈ 0.4840 rad, stated in 2006 as a difference of two
fitted phases and in 2010 (arXiv:1006.3114, Eq. 69) as √m_νg = 0.1000(26) √eV [1 + √2 cos(2gπ/3 + π/12 + 2/9)].

## Against today's data (the agent's arithmetic; inputs NuFIT 6.0, arXiv:2410.05380, Table 1, and PDG 2024 Table 14.7)

| quantity | Brannen 2006 | today | distance |
|---|---|---|---|
| Δm²₂₁ | 7.930 × 10⁻⁵ eV² | 7.49 ± 0.19 (NuFIT); 7.41 +0.21 (PDG) | +2.3σ to +2.5σ, inside 3σ |
| Δm²₃₂ (normal) | 2.492 × 10⁻³ eV² | 2.437 +0.028 (PDG, no SK); 2.433 +0.026 (with SK) | +2.0σ to +2.3σ, inside 3σ by 0.03 |
| Δm²₃₁ (normal) | 2.572 × 10⁻³ eV² | 2.513 +0.021 (NuFIT, with SK); 2.534 +0.025 (without) | +2.8σ / +1.5σ |
| Σm_ν | 0.0600 eV | < 0.12 (Planck 2018 + BAO); < 0.072 (DESI 2024 + CMB, abstract) | allowed |

**Verdict: not excluded, not "dead center" any more.** Both splittings sit 2 to 3σ above the present values. Brannen himself
(2010, Eqs. 71, 72) moved the scale from 0.1000 to 0.0990 √eV "to match the new experimental data", which silently drops
the exact 3¹¹ (17716/3¹¹ = 0.10001).

## Later tests

- Koide, hep-ph/0605074 (J. Phys. G 34 (2007) 1653), FULL TEXT: takes the sign flip and the π/12 seriously as "Brannen's
  speculation", notes the oscillation data alone cannot judge it, finds the predicted ratio of splittings (0.0318) against
  the observed 0.029 ± 0.005 "favorable", and builds an S3 model that reproduces θ_ν = θ_e + π/12 under one convention
  ("If we took another conventions of the S3 representation, we would not obtain the Brannen's relation"). "It is an open
  question that the relation (3.5) is accidental or not" (0706.2534).
- Rodejohann and Zhang, arXiv:1101.5525, FULL TEXT: do not cite Brannen; show the all-positive relation fails for light
  neutrinos (their K between 1/3 and 3/5) and that one Majorana phase near π on one root restores it, which is Brannen's
  sign flip in another language; nothing on 3¹¹ or π/12. Compatible, not a refutation.
- No refereed paper found that tests or refutes the 3¹¹ and π/12 prediction as such.

## What it does for the owner's gaps

- **G5 (the neutrinos):** in the Koide form a massless loop sits at 3/8 turn; Brannen's neutrinos are not that. They are
  the same three-spoke form with one spoke's root *negative*, a scale 3¹¹ smaller and a phase 1/24 turn further round. In
  her parts, a negative root is a signed part that overwhelms the constant part, which the form allows and the charged
  leptons never use. Whether a loop can carry a negative root is hers to say (G8, what √m is). The two integers 11 and 12
  are the kind of thing rule 13 counts.
- The sum 0.060 eV is a number the first cosmology bound to reach it would decide (DESI's 0.072 is already close).

## Sources fetched

MASSES2.pdf (full); arXiv:1006.3114 (full); hep-ph/0605074 (full, via ar5iv); arXiv:1101.5525 v1 (full); viXra:0702.0052
(abstract); hep-ph/0505220 (abstract here; full in the companion note); arXiv:2410.05380 Table 1; PDG 2024 neutrino review
Table 14.7; arXiv:1807.06209 and 2404.03002 (abstracts); Wikipedia "Koide formula". nu-fit.org refused the connection.
