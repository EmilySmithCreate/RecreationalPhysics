# Twist and curl: the relations as equations and inequalities, the observed table in her counts, and the 2D phase

*Written 2026-10-30 at the owner's request of 29/30 October ("read the papers that you listed and take math that they
brought that doesn't contradict our theory ... build out the table and the fully simplified equations and inequalities
representing the relationships between twist and curl observed in 3d and what it means for the 2d phase"). Every line
says whose it is: **hers** (her rule, `docs/design/twist_curl_rules_current.md`), **published** (a source, with how much
was read: `docs/reading/notes/2026-10-30_braid_lineage_reads.md` and `2026-10-30_helon_model_full_read.md`),
**exact** (arithmetic or geometry, checked), **measured** (a PDG value, from memory, to verify), **ours, unverified**.
Nothing here is a result about reality. The sandbox lane applies: the table and the integer test kill but never crown
(`sandbox/observed_particle_table.py`).*

## 1. The quantities

| Symbol | Meaning | Values | Whose |
|---|---|---|---|
| D | number of directions of the lattice | 2 (the paper 1 toy, four links a point) or 3 (six links) | exact |
| S_e | squares on link e | 0 ≤ S_e ≤ 2D − 1 (the hard-core rule caps it; flat is 2D − 2) | published [T25], exact |
| c_e | curl on link e, c_e = S_e − (2D − 2) | −(2D − 2) ≤ c_e ≤ +1; in 3D −4 to +1, in 2D −2 to +1 | hers (name), exact (range) |
| C(ℓ) | curl of a closed loop ℓ, the sum of c_e over the links its diagonals span | whole numbers; "what is real is the total round a closed loop" | hers |
| τ_d | twist on diagonal d | matter: 0 or ±⅓ on box diagonals (1,1,2); dark: 0 or ±½ on face diagonals (1,1,0); sign by colour | hers |
| T(ℓ) | net twist of a loop, Σ τ_d round it | a whole number of thirds (matter) | hers |
| Q | electric charge | Q = T(ℓ) for a free loop (in units of e) | hers |
| s | spin | ½ or 1 (and 0 for opposed pairs) | hers |
| n | mass count: looped diagonals, a long diagonal counting one | whole numbers | hers (Update 148) |
| m | mass | m = u n, u = m_e / n_e | hers; u exact given n_e |
| Wr | the coil (writhe of the loop as a curve) | real; 0 for every planar loop | exact |

## 2. The relations, 3D, as they stand

**Her rules written as constraints** (hers unless marked):

    (R1)  twist only where curl:            τ_d ≠ 0  ⇒  c_e ≠ 0 on the links of d's box
    (R2)  thirds on box diagonals:           τ_d ∈ {0, +⅓, −⅓} for matter;  sign(τ_d) = colour of d's end points
    (R3)  halves on face diagonals:          τ_f ∈ {0, +½, −½} for dark twist
    (R4)  charge is net twist:               Q = Σ_{d∈ℓ} τ_d  ∈ ℤ for a free particle        (confinement: Q ∉ ℤ only stacked)
    (R5)  spin × curl = ½:                   s · C = ½  ⇒  (C, s) ∈ {(½, 1) photon, (1, ½) matter};  s = 0 for two loops spinning against each other
    (R6)  mass is a count:                   m = u · n,   n = number of looped diagonals (a long diagonal counts one)
    (R7)  the unit:                           n_e = 3 as it stands (open: n_e > 3 if a 3-loop cannot hold its twist)
    (R8)  equal spacing (stability):         like twists sit at equal spacing round the loop  ⇒  a charge-±1 loop of three thirds is (S L^k)^3, n = 3(k + 1)
    (R9)  no uncharged spin:                 T(ℓ) = 0 and s ≠ 0 does not occur for a matter loop  (the neutrino must live elsewhere: see §5)
    (R10) pairs:                              curl is made with anticurl, +θ with −θ;  Σ_all τ_d = T_total is fixed after the burp

**Exact consequences** (ours, from R1 to R8; each checked in the sandbox or by arithmetic):

    (E1)  n ≥ 3 for any loop in 3D (three box-diagonal steps close; `proton_loop_fold.py`), and every closed loop of box diagonals is one colour (parity)
    (E2)  a charged lepton has n ≡ 0 (mod 3) under R8;  charged objects at n = 3, 6, 9, ...;  the gap below the muon is not made by R8
    (E3)  a loop of three box diagonals is planar, Wr = 0 (all 16 triangles);  4-loops Wr = 0;  |Wr| up to 1.000 at 5, 1.564 at 6
    (E4)  the four test particles pass R4 and R5: e (−1, ½), n (0, ½), γ (0, 1), π± (±1, 0)
    (E5)  the integer test: if R6 holds, n_X = n_e · (m_X / m_e) is a whole number for every particle X

**The published relations taken, that do not contradict R1 to R10** (published; sources in the reading note):

    (P1)  Lk = Tw + Wr                                   Călugăreanu, White, Fuller: linking of a ribbon's edges = its twist + its writhe
          — the one published relation between a twist and a coil; it needs a ribbon (a framing), which a loop of diagonals does not yet carry
    (P2)  Q = ⅓ (N_+ − N_−)                              rishon counting (Harari, Shupe 1979): charge = net count of charged constituents in thirds
          = ⅓ (a + b + c)                                 BHKS 2008, Eq. 3: charge = sum of the three strands' twists over three
    (P3)  three per particle                             rishons, helons, braids: "three helons seems to be the minimum ... stable, non-trivial structure" (BT05 §II)
    (P4)  Ω = β (N_+ + N_− − N_0)/3,  Q = (β + Ω)/2      BT05 Eqs. 3–5: hypercharge and the Gell-Mann–Nishijima relation from counting alone
    (P5)  C: flip every twist's sign;  P: reverse the order round the triplet;  T: both;  CPT = 1     BHKS 2008 Eqs. 5–7
    (P6)  interactions add twist strand by strand:  [a,b,c] + [d,e,f] = [a+d, b+e, c+f]              BHKS 2008 Eqs. 8–10
    (P7)  N_B = Σ β conserved: braids and anti-braids are made and destroyed together                 BT05 §III, Eq. 6 (lepton number)
    (P9)  a crossing is a twist:  σ₁ → [½, ½, −½],  σ₁⁻¹ → [−½, −½, ½],  σ₂ → [−½, ½, ½]     BHKW 2012 Eq. 2.1: a crossing of two strands under a cap equals half twists on the strands,
          so every braid reduces to twists only ("twisting (electric charge) and braiding are fundamentally the same process", BT05 §IV)
    (P10) twist is quantized by the node's symmetry:  the smallest distinguishable twist is π/3 on a four-valent node  BHKW 2012 §3.1: thirds from a three-fold symmetry, not put in by hand
    (P11) a conserved sum under the moves:  Θ = T_l + T_r + Σ T_i − 2 Σ x_i  (twists minus twice the signed crossings)    BHKW 2012 Eq. 3.4, additive under interaction and decay (Thms 3.1, 3.3)
    (P12) stability:  "any nontrivial braid with internal twists is stable under single evolution moves"                 BHKW 2012 §3.4; a trivial braid is unstable ("dual to a 3-ball")
    (P13) mass as a count of crossings:  conjectured, not computed; makes the interacting (boson-like) braids massless   BHKW 2012 §3.7, citing BT05 and BTMS07
    (P8)  Koide: (m_e + m_μ + m_τ) / (√m_e + √m_μ + √m_τ)² = 0.666661 against 2/3                     measured relation, no accepted derivation (Koide 1983, 1990); unit-free, so it holds for counts n as for masses

**How each maps onto her rules** (ours, unverified): P2 is R4 with "twisted strand" for "twisted diagonal"; P3 is
E1 with a reason (two strands untwist, three cannot) that is about braids and transfers to loops as an analogy only;
P5 is R10's pairs made exact (her antiparticle is the colour-flipped loop; "reverse the order" is the loop run the other
way); P6 is what R10 needs as a rule in the toy, net twist conserved diagonal by diagonal under the moves; P7 is her
"net matter stays the same"; P1 is the relation she called "the self-referential loop of the twist curl relationship",
in its published form, and it says a coil can trade for twist only when the loop is a ribbon with two edges. P9 is the published form of her 'the twists repel somewhat' turned the other way: a coil (crossing) and a twist are
exchangeable, half a twist per strand per crossing, so a loop can hold its twist as shape or as twist, which is what her
'a tight loop needs a gluon to hold its twist' needs as a rule. P10 is the one place in the lineage where thirds are
derived rather than named, and it comes from a three-fold symmetry at a point, which the cubic lattice has along its body
diagonals. P11 is the exact shape a conserved net twist in the toy would take if the coil counts against it. P12 is R1
and R9 in their words: no twist, no stability. P13 is the published cousin of R6, with crossings for diagonals. P4 and P8
have no counterpart in her rules yet; P4 is the kind of count-to-rule result she asked for on 29 October, and P8 is the
sharpest known constraint on any mass rule for the charged leptons.

**What is not taken, with its kind (rule 23):** BT05's "no H+ with H− in one triplet" (theory structure, inherited
from Harari and Shupe; her proton holds both); BHKS's unbounded generations from a neutrino series [a, 2 − 2a, a − 2],
a even (theory structure; nothing measured supports a fourth generation); BHKS's half-integer twists on non-orientable
ribbons (allowed there, unused; her halves are the dark twist, a different thing); the rishon hypercolour force
(theory structure, added to fix problems the braid picture claims to avoid).

## 3. The observed table in her counts (step 1 of the path; `sandbox/observed_particle_table.py`)

Masses are PDG values from memory, **to verify** before any number leaves the sandbox. n is for n_e = 3; k = (n − 3)/3
is the gluons per run under R8 if the object were three thirds equally spaced.

| particle | mass MeV | Q (thirds) | spin | n (n_e = 3) | n mod 3 | content |
|---|---|---|---|---|---|---|
| electron | 0.510999 | −3 | ½ | 3.00 | 0 | lepton |
| muon | 105.658 | −3 | ½ | 620.30 | — | lepton |
| tau | 1776.86 | −3 | ½ | 10,431.7 | — | lepton |
| neutrino | < 8 × 10⁻⁷ | 0 | ½ | < 0.005 | — | lepton |
| photon | 0 | 0 | 1 | 0 | 0 | boson |
| π⁺ | 139.570 | +3 | 0 | 819.40 | — | u anti-d |
| π⁰ | 134.977 | 0 | 0 | 792.43 | — | u anti-u, d anti-d |
| K⁺ | 493.677 | +3 | 0 | 2,898.3 | — | u anti-s |
| ρ(770) | 775.26 | +3 | 1 | 4,551.4 | — | u anti-d, spins parallel |
| proton | 938.272 | +3 | ½ | 5,508.46 | — | uud |
| neutron | 939.565 | 0 | ½ | 5,516.05 | — | udd |
| Λ | 1115.68 | 0 | ½ | 6,550.0 | — | uds |
| Δ⁺⁺ | 1232 | +6 | 3/2 | 7,233 | — | uuu |
| Ω⁻ | 1672.45 | −3 | 3/2 | 9,818.7 | — | sss |
| W | 80,369 | +3 | 1 | 471,836 | — | boson |
| Z | 91,188 | 0 | 1 | 535,349 | — | boson |
| Higgs | 125,200 | 0 | 0 | 735,031 | — | boson |

(The script prints 37 rows, the quark masses among them with their scheme dependence noted.)

**The integer test, E5, run** (exact arithmetic on measured ratios; ours):

- m_μ/m_e = 206.768 283 0 ± 4.5 × 10⁻⁶; m_p/m_e = 1836.152 673 4 ± 5.7 × 10⁻⁷; m_τ/m_e = 3477.23 ± 0.23 (to verify).
- **n_e = 3 fails:** the muon would be 620.30 diagonals, the proton 5,508.46, the tau 10,431.7. None is whole; the muon
  misses by 0.30 where the allowed error is 4 × 10⁻⁵. (The record's "621 = 3 + 3 × 206" rounded 206.77 to 206.)
- Over n_e = 1 to 5,000, the muon alone is whole within error at 343 values (the first: 82, 164, 246, ...); all three
  together at 3 values (3,871; 4,061; 4,264), against a chance expectation of 3.8. So no n_e is singled out: the passes
  are what three unrelated ratios produce by accident.
- **Kind: measurement** (rule 23), after the arithmetic. What it kills: *m = u · n with one unit u and n a whole
  count*, for the electron, muon, proton and tau together, at every n_e up to 5,000 beyond chance. What it does not
  kill: mass as a count plus something else (an energy of the coil, of the twist, or of the gluon runs, which the
  standing rules already say is a separate ledger, §4 of the rules sheet); or masses that are not simply additive over
  parts (binding). Under rule 11 the four answers: (i) it falsifies R6 in its one-unit form, not the count idea;
  (ii) the failure is in the mechanism as stated, not implementation, parameters or size; (iii) the test that tells
  the readings apart is whether a second term with no free constant (the coil's energy, say, at the loop's own Wr) makes
  620.30 − 3 × 206 = 0.30 for the muon and 0.46 for the proton out of the same rule; (iv) abandon "mass is only a
  count" if no such term without a fitted constant closes both gaps.
- P8 (Koide) survives the change of units unchanged, so any mass rule for the leptons has to reproduce 2/3 to six
  figures; a count rule does so only if the counts themselves do.

## 4. What the 3D relations mean for the 2D phase (the paper 1 toy, four links a point)

Exact, ours, from the lattice:

    (2D-1)  curl range:  c_e = S_e − 2 ∈ {−2, −1, 0, +1};  one extra square is still one whole curl
    (2D-2)  colour:  the (1,1) diagonal (length √2) joins like colours and is the only "box diagonal" the square sheet has;
            the (1,0) step is a link; there is no black-to-white diagonal at all, so light's body-diagonal path does not exist in 2D:
            in the 2D phase light would have to run on the links, at the link speed (one link a tick), which is what T47 measured for fronts
    (2D-3)  the smallest closed loop of (±1,±1) diagonals has 4 steps: three cannot close (their x-sum is odd).
            So the electron as a loop of three thirds does not exist in 2D; the smallest charged loop under R8 is 6 (three thirds, three gluon runs) or a 4-loop with one diagonal untwisted, which breaks R8.
    (2D-4)  every closed loop of (1,1) diagonals is planar:  Wr = 0 for all;  the coil does not exist in 2D (P1 collapses to Lk = Tw)
    (2D-5)  X in 2D (the tube) is c_e = +1 on every link along the curled direction: one whole curl on every link, so by R1 twist could sit anywhere on it;
            the burp (T7, T9) takes that curl away everywhere except in the scraps (the four-point column, the knots of O107), which is where R1 then allows twist

Ours, unverified, what follows: (a) the 2D phase holds no electron and no coil, so her particle rules are three-
dimensional rules, and the burp from two to three open directions is where particles become possible, which fits
her "everything but twist and curl emergent" and Update 19 (matter is the structured leftover). (b) The order of
events her rules then imply: curl everywhere in X (one per link) → the burp removes it → curl survives only in knots
→ R1 says twist, and so charge and matter, can sit only there → the amount of matter is set by the scrap count at the
opening, which O107 found fixed by the seeds and not by the cooling. That is claim 5 written in the particle rules.
(c) In 2D the dark twist (halves on face diagonals) has no carrier either, since (1,1) is the only diagonal and it is
already the matter carrier; a 2D phase would have one kind of twist at most.

## 5. Open after this document (hers to decide, in order)

1. R6 in its one-unit form fails the integer test (§3). Keep mass as a count plus a second ledger, or replace it.
2. R9 and the neutrino (`2026-10-30_helon_model_full_read.md`, item 4): where an uncharged spin-½ object lives.
3. Whether R10 is to be built as P6 (net twist conserved diagonal by diagonal under the toy's moves): the first exact
   piece of the diagonals build, no constant.
4. Whether a framing (a ribbon with two edges) is given to her loops so that P1 applies, or the coil stays a shape.
5. P4's counterpart: does any count on her loops give hypercharge and the Gell-Mann–Nishijima relation.
