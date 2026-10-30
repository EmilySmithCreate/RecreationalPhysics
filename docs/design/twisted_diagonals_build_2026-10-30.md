# The twisted-diagonal state: the form fixed before it is coded (30 October 2026)

*Written on the owner's decision of this afternoon ("item 3 of the diagonals brief and is not built -> proceed w build").
Under S1 the form is fixed here, in writing, before any run; every line says whose it is. The rules it encodes are the
standing sheet `twist_curl_rules_current.md` (hers), read in full before this was written; where the sheet leaves a
choice, the choice is marked **ours** and is hers to change. Module: `src/graphity/twist.py`; tests:
`tests/test_twist.py`. This is her Option B (the diagonals brief, decision 5): particles are loops of twisted diagonals
built as variables, and the wiring's knots are the scrap. Nothing here derives anything; a rule is put in, and the
results are what follows from the rules together.*

## 1. The lattice (exact, from the sheet)

An L × L × L torus of points coloured by the parity of x + y + z (black even, white odd; a convention, ours). A **box
diagonal** is a step whose displacement is a signed permutation of (1, 1, 2): 24 of them, length √6, same colour to
same colour. A **long diagonal** is (1, 1, 2m) in any signed permutation with m ≥ 2 (her 1 × 1 × 4, √18). A **face
diagonal** is a signed permutation of (1, 1, 0): 12, length √2, same colour. Body diagonals (1, 1, 1) change colour and
carry light, not twist; they are not part of this state.

## 2. The state

A **loop** is a closed sequence of points on the torus whose consecutive steps are box diagonals, long diagonals or face
diagonals (one kind per loop; a loop of box diagonals is matter, of face diagonals dark, by the sheet), all of one colour
(automatic for these steps). Each loop carries:

| quantity | values | rule it encodes | whose |
|---|---|---|---|
| twist τ_i on each diagonal i | multiples of ⅓ on box diagonals; multiples of ½ on face diagonals; **0 on a long diagonal** | twist in thirds (matter) and halves (dark); the long diagonal holds curl with no twist | hers |
| sign of τ_i | either sign on any diagonal | a positive particle goes over 1 (⅔, ⅔) and twists back (−⅓); the neutrino holds +θ and −θ; so the colour sets which sign is "matter" and does not forbid the other | hers (the sheet); the reading that colour does not constrain the sign was ours and is **hers from 2026-10-30** ("agree") |
| curl per loop | an integer ≥ 1 | one curl of energy per loop | hers |
| spin s per loop | −½, 0, +½; **non-zero only if some τ_i ≠ 0** | half spin on a full curl; spin needs twist present, not net twist (30 October) | hers |

A **particle** is a named set of loops. Its readers (exact, from the sheet's section 2):

- **charge** = Σ τ_i over all its diagonals; a particle on its own must have whole charge (a loop alone may carry a third);
- **spin** = |Σ s_ℓ| over its loops (spins can cancel while twists add: the pion);
- **mass as a count** = the number of looped diagonals, a long diagonal counting one (Update 148);
- **the parts, each its own quantity** (30 October, §5 of the relations document): L = loops, n = diagonals, τ⁺ = Σ|τ_i|,
  T = Σ τ_i, s = Σ s_ℓ, C = Σ curl. No rule combines them into MeV here; MeV is the measured total only.
- **net twist** of a set of particles = Σ T, the quantity pair creation conserves (the sheet, "Pairs and annihilation";
  the sheet's open item 6, defined here for the first time).

## 3. What is checked, and what is not

Checked by the module (and raised as an error): a step that is not an allowed diagonal; a loop that does not close on
the torus; a twist not a multiple of its kind's increment; twist on a long diagonal; spin without twist present; mixed
step kinds in one loop. **Not checked, open:** the stability rule (sheet, open item 1); whether a loop of three can hold
its twist (the electron's size n, item 3); whether twisted diagonals may cross or share points (allowed for now; ours, and hers from 2026-10-30, "agree"); the photon (not a loop of box diagonals; it stays unbuilt).

## 4. The energy

*Revised 2026-10-30 on her decisions of that afternoon.* The twist term adopted as the working form (hers: "it's okay to work with
this, just carry the note. we'll see if we can derive later"), with the writhe term she asked for ("writhe seems like a
great idea and already has available math"):

    E_twist(loop) = ε [ Σ_i τ_i² + Σ_i (τ_{i+1} − τ_i)² ]  +  ε_w Wr²

elastic plus mismatch on the diagonals (E4 of `sandbox/twist_energy_options.py`), and the coil's own cost through the
writhe Wr of the loop as a closed polygon (the Gauss double integral; the Călugăreanu–White–Fuller theorem Lk = Tw + Wr
and the elastic-rod and DNA models are the published math, general knowledge, to verify). Two constants, ε and ε_w;
neither pinned yet. **Rule-13 note, carried:** E4 was chosen because its rankings of her test particles were the ones
she wanted; it is not derived. **Her requirement on the term (hers, this day):** a charge of 2 or more on one loop must
cost more than two separate particles, since like twists repel and a free particle carries a whole twist; under E4 alone
charge 2 on six diagonals costs exactly two electrons, so a repulsion piece is still owed (the simplest, ours, in the
look: a per-loop cost in the net twist squared). **Her correction on the periodic form:** periodic in a loop's net
twist (whole charge free, fractions costing) is her "a full twist is a requirement" as an energy, the confinement of
thirds, and is not what was decisive against; the per-diagonal form was. Proposed for her, not adopted: that term
beside E4. **The question the writhe term raises (ours):** the conserved quantity of a closed ribbon is Lk = Tw + Wr,
so twist can turn into coil; if charge is the net twist it is not conserved under coiling; the published reading would
make charge the linking number, twist held plus coil. Hers to decide. *Checked 2026-10-30 on her question (exact; `sandbox/linking_number_check.py`): charge as Lk is not consistent with the state as built, since a closed ribbon's Lk is a whole number, so a loop alone could not carry a third, and the writhe of a closed pentagon of box diagonals is a generic real, so the twist held could not stay in thirds; it would give her the whole-twist requirement for free on planar loops. Charge as net twist, with writhe a shape cost outside charge, is consistent; the theorem's conservation law is then not used, and that note is carried. Hers.* Previously here: "None is added." (the sheet's
section 4 stood until this afternoon). The sheet's section 4 stands: the state carries curl as a count per loop (one curl of energy each) and no
twist term (the κ form was ours and is not adopted). So the first thing the state can do is score the sheet's own
particles exactly, and conserve net twist; what it cannot yet do is move.

## 5. The first exact check (run with the tests, nothing registered)

The sheet's four test particles, built by hand and read by the module: electron (one loop of three box diagonals, twists
−⅓, −⅓, −⅓, spin ½): charge −1, spin ½, mass 3. Positive pion (two loops: ⅔ + ⅓ on one, their spins opposed ... as the
sheet reads it, "twists ⅔ + ⅓, spins opposed"): charge +1, spin 0. Neutron (three loops, −⅓, −⅓, +⅔ net, spins netting
½): charge 0, spin ½. Neutrino (one loop, +⅓ and −⅓, spin ½): charge 0, spin ½, twist present ⅔. A pair (loop with T and
its mirror with −T): net twist 0. The photon is excluded (not a loop of box diagonals).

## 6. What this build does not claim

That any of these loops is stable, that the counts are masses in MeV, or that the lattice is space. It is the first
object in the toy that is her particle by her rules, and its only immediate use is that the rules can now be checked
against each other exactly, and that a wave or a chain can later act on it.
