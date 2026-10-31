# Reading: the braid-and-rishon lineage behind the helon model, and the pattern-to-rule sources named on 29 October

A reading note, not a prior-work search. The owner asked (29/30 October, verbatim in `sandbox/NOTEBOOK.md`): "Please
read the papers that you listed and take math that they brought that doesn't contradict our theory. Read additional
abstracts of key sources for those papers." The mathematics taken is in `docs/design/twist_curl_relations_2026-10-30.md`
(P1 to P13); this note records what was read, how much, and what each source says, so the taking can be checked.
**Tracked files changed with it:** that design document, `REFERENCES.bib` (fifteen entries), `sandbox/NOTEBOOK.md`,
`sandbox/LOG.md`, VISION (one addendum).

Kinds of statement (rule 10): **published** (with how much was read); **exact** (arithmetic, ours); **ours, unverified**.
"General knowledge, to verify" marks a statement from memory.

**Date:** 2026-10-30, 01:16 to 02:10 UTC by the clock. **Who read:** two assistant agents (Claude Fable 5.1) read the two
long papers in full from the arXiv PDFs (text; the 2008 paper's seven figures from page renders, the 2012 review's
figures not viewable) and reported with verbatim quotations; the session read the abstracts itself from INSPIRE and
arXiv. The owner has read none of them.

## 1. Sources and read status

| Key | Source | Read status |
|---|---|---|
| [BHKS08] | Bilson-Thompson, Hackett, Kauffman, Smolin, "Particle identifications from symmetries of braided ribbon network invariants", arXiv:0804.0037 (v1 only, 2008; no journal reference) | **Read in full** by an agent (text and figures) |
| [BHKW12] | Bilson-Thompson, Hackett, Kauffman, Wan, "Emergent braided matter of quantum geometry", SIGMA 8 (2012) 014, 43 pages, doi:10.3842/SIGMA.2012.014, arXiv:1109.0080v2 | **Read in full** by an agent (text; figures not seen) |
| [Harari79] | Harari, Phys. Lett. B 86, 83 (1979) | Abstract only (INSPIRE) |
| [Shupe79] | Shupe, Phys. Lett. B 86, 87 (1979) | Abstract only (INSPIRE) |
| [HS81] | Harari and Seiberg, Phys. Lett. B 98, 269 (1981) | Abstract only (INSPIRE) |
| [HS82] | Harari and Seiberg, Nucl. Phys. B 204, 141 (1982) | Abstract only (INSPIRE) |
| [BHK09] | Bilson-Thompson, Hackett, Kauffman, J. Math. Phys. 50, 113505 (2009), arXiv:0903.1376 | Abstract only (arXiv) |
| [Hackett07] | Hackett, Class. Quantum Grav. 24, 5757 (2007), arXiv:hep-th/0702198 | Abstract only (arXiv) |
| [Wan07] | Wan, arXiv:0710.1312 | Abstract only (arXiv) |
| [HW09] | Hackett and Wan, Class. Quantum Grav. 26, 125008 (2009), arXiv:0803.3203 | Abstract only (arXiv) |
| [Koide83], [Koide90] | Koide, Phys. Lett. B 120, 161 (1983); Mod. Phys. Lett. A 5, 2319 (1990) | Abstracts only (INSPIRE); the sum rule is stated in the 1990 abstract |
| [GellMann61] | Gell-Mann, CTSL-20 (1961) | Abstract only (INSPIRE) |
| [GellMann64] | Gell-Mann, Phys. Lett. 8, 214 (1964) | Not read (no abstract available) |
| [Neeman61] | Ne'eman, Nucl. Phys. 26, 222 (1961) | Abstract only (INSPIRE) |
| not reached | Smolin and Wan, arXiv:0710.1548; He and Wan 2008 (C, P, T of braid excitations; conserved quantities); Hackett's 2011 invariants papers; Wan's thesis; Koide's 1982 Lett. Nuovo Cim. paper | Not read; named from the reviews' reference lists |

## 2. What each says (published; quotations are the agents' or the abstracts')

**[Harari79], [Shupe79], [HS81], [HS82], the rishon model.** Two spin-½ constituents, one of charge ⅓ (T) and one
neutral (V); quarks and leptons as triplets; "A distinguishability assumption leads to the emergence of three quark
colors" (Shupe); Harari's abstract says the scheme "offers no convincing dynamics". The 1981 paper supplies the dynamics
as a gauge theory with a second confining force, hypercolour, and finds at least three generations; the 1982 analysis
names its own difficulties (the symmetry-breaking pattern; light composite vector bosons). The helon model of [BT05]
keeps the triplets and the thirds and drops hypercolour (`2026-10-30_helon_model_full_read.md`).

**[BHKS08].** Nine pages. Every capped three-strand braid reduces to a trivial braid with a twist on each strand (Fig.
6: one crossing under a cap deforms into a twist on each strand), so a particle is "an invariant triplet of half-integers
(a, b, c)"; orientable braids have whole-number triplets. The symmetry group acting on the triplet is S₃ × Z₂; charge
must be a function of a + b + c, "The simplest choice is then that charge is 1/3(a + b + c)" (Eq. 3). C = flip every
sign (Eq. 5), P = reverse the order (Eq. 6), T = both (Eq. 7), CPT = 1. Interactions are assumed to add twists strand by
strand (Eqs. 8 to 10). The neutrino is the twist-free, chargeless series [a, 2 − 2a, a − 2] with a even (Eq. 11), the
first [2, −2, 0], so there are "infinitely many higher generations". Table 2 lists two generations; the electron is
[1, −3, −1], the muon [3, −7, 1], the up quark [2, −1, 1] and permutations for colour. Mass: none ("the dynamical
breaking of the chiral symmetry leading to a spectrum of fermion masses needs to be studied"). Spin: "the states we
have identified as fermions have not been shown to be either spinorial or fermionic". No reference to Călugăreanu,
White or Fuller; no knot-theory reference. *Exact, the agent's check:* charge = (a + b + c)/3 gives the right charge
for every entry of Table 2 but one, s_L,r = [5, −6, 2], which sums to +1 and is a typo for [3, −6, 2] by the pattern
d = ν + [−1, 0, 0].

**[BHKW12].** Forty-three pages reviewing two schemes. Three-valent (the helon model embedded in ribbon networks): a
twist of ±2π on a strand is ±e/3; twists of ±4π and more "can be regarded as equivalent to crossings"; the exchange is
exact, σ₁ → [½, ½, −½], σ₁⁻¹ → [−½, −½, ½], σ₂ → [−½, ½, ½] (Eq. 2.1), iterated until the braid word is the identity
(Eq. 2.2); the "reduced link" of the strands' edges is unchanged by the network's 1→3 and 2→2 moves, so the braids
"will not decay", which also "appears to prohibit any non-trivial particle interactions": the trivalent scheme is
"too stable". Four-valent (Wan's braids): nodes are spheres with four tubes; a node's three-fold symmetry makes "the
smallest distinguishable twist π/3" and "All twists are valued in Z in units of π/3"; a braid is an 8-tuple of
end-node states, external twists, internal twists and a crossing word; two invariants, Θ = T_l + T_r + Σ T_i − 2 Σ x_i
(twists minus twice the signed crossing count) and χ = (−1)^|X| S_l S_r (Eq. 3.4), additive and multiplicative under
direct interaction, decay and exchange (Thms 3.1, 3.3); "any nontrivial braid with internal twists is stable under
single evolution moves"; the trivial braids are unstable and "plausible ... analogous to gravitons"; Θ "or an
appropriate function of it" is the candidate electric charge, which "naturally, rather than by hand, gives rise to
charge quantization and fractional charges"; mass: "the number of crossings in a braid can be a candidate for its
mass", conjectured, with the interacting braids then massless; spin: "we do not know yet what features of a braid
correspond to" it; generations, mixing, CP violation: not reproduced ("the absence of CP-violation in our theory does
not comply with the SM"). Open, in their words: "the lack of sufficient super-selection rules over an enormous zoo of
3-strand braids"; "Both trivalent and 4-valent schemes need a mechanism to create nontrivial braids on unbraided
networks". Neither scheme cites a twist-writhe-linking paper; the crossing-twist exchange is referred to [BHK09].

**[Koide90] (abstract).** m_e + m_μ + m_τ = (2/3)(√m_e + √m_μ + √m_τ)². *Exact, ours, PDG values from memory:* the left
over the right is 0.666661. [Koide83]'s abstract gives no formula; the relation is usually cited to it and to the 1982
letter (general knowledge, to verify).

**[GellMann61], [Neeman61], [GellMann64] (abstracts; the 1964 paper has none).** The eight baryons as one multiplet of
a unitary symmetry split by a mass term, the pseudoscalar octet with a predicted ninth meson, eight vector bosons; the
1964 paper is the quark paper with charges in thirds (general knowledge). Taken as the worked precedent for "a pattern
in the table forces constituents in thirds", not for any formula.

## 3. What was taken and what was not

Taken (P1 to P13 of the design document): charge as a signed count in thirds; three per particle as the minimum; the
antiparticle as the sign flip and the reversed order; twist conserved strand by strand under interaction; lepton number
as a signed count; hypercharge and the Gell-Mann–Nishijima relation from counts; the exchange of a crossing for half
twists; thirds from a three-fold symmetry at a point; a conserved twist-minus-crossings sum; "no twist, no stability";
mass as a count of crossings (as their conjecture); Koide's relation as a unit-free constraint.

Not taken, each with its kind (rule 23): no charge mixing inside one object (theory structure, inherited); unbounded
generations (theory structure); half-integer twists on non-orientable ribbons (unused by them; her halves are dark
twist); hypercolour (theory structure); the four-valent scheme's deterministic interactions and its absence of CP
violation (its own stated failures).

What would change this reading: Smolin and Wan 2008 and He and Wan 2008, which give the four-valent braids their
propagation and their C, P, T; [BHK09], where the crossing-twist exchange is proved; Hackett's 2011 invariants papers.
