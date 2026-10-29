# Twist and curl: the rules as equalities and inequalities (draft, 27 October 2026)

*Written at the owner's request of 19:39 UTC ("I want us to write the math of this relationship in a simple
equality/inequalities"), from her answers of 16:42 to 19:39 UTC (verbatim in `sandbox/NOTEBOOK.md`; VISION Updates 133
and 134). Each line says whose it is: **hers** (her rule, her words put in order), **exact** (arithmetic), **ours** (our
translation or reasoning, unverified), **open** (a choice still hers). Nothing here has been run. A rule is put in, so
whatever it says is not a result; the results are what follows from the rules together.*

## The two quantities

- **Curl** on a link e: c_e = S_e − 4 (six links; flat space has 4 squares on every link). c_e > 0 is curl, c_e < 0 is
  anticurl. *Exact:* the hard-core rule bounds it, −4 ≤ c_e ≤ +1, so the toy's curl is lopsided (O164; Update 134).
- **Twist** on a square p: τ_p, measured in turns. Her values (19:50 UTC): −⅔, −⅓, 0 (gluons), ⅓, ⅔ for matter, ±½ for
  dark. **Open, phase or count:** as a phase (the light field, `graphity.u1`, defined mod 1) the five matter values are
  three, 0, ⅓ and ⅔, since +⅔ and −⅓ are the same turn; that is the published triality (quarks 1, antiquarks 2, gluons
  0, the ℤ₃ centre of colour), and a half turn is its own mirror (+½ is −½), which matches dark twist being one-sided.
  As a count (whole thirds, not mod 1) all five are distinct and carry electric charge. Physics uses both: charge as a
  count, triality as a phase.

## The rules

1. **Balance** (hers, 25 October; soft form 27 October): Σ_e c_e = 4(S − 3N), held near zero by the penalty
   (μ₀/N)(S − 3N)².
2. **Prices** (hers; **version B chosen**, 20:04 UTC: "this is fine"; two versions on the record). A pair is always made together and costs the sum of its two
   prices (19:50 UTC: "curl costs double, but you always get both"). Version A (17:41 UTC): curl 4(λ − 1), anticurl 4λ;
   *exact:* λ·H(λ′) with λ′ = 2 − 1/λ, a pair costs 8λ − 4. Version B (19:50 UTC, "I may not be thinking of this
   right"): both 4(λ − 1); *exact:* (λ − 1)·H(2), the toy at λ′ = 2 and coupling g/(λ − 1), a pair costs 8(λ − 1). Under
   B, λ sets only the energy unit, and at λ′ = 2 no curled X of the toy is stuck for now (2D dips end near 1.6, the
   rod's window at 1.5, the slab's at 2: O13, O41, O49), so B leaves the toy no X to hold.
3. **Twist makes curling dearer** (hers, T1; the form ours, open): each unit of curl on a link costs κ·T_e more, with
   T_e = Σ over the link's squares of (1 − cos 2πτ_p): 0 with no twist, 2 at a half turn, the same for ±τ.
   Acts on anticurl too (hers, 19:50 UTC): the extra cost is κ·T_e·|c_e|.
4. **Pairs** (hers, T3, imposed on the moves; reading (a) chosen 19:39 UTC): a move may make curl only together with an
   equal amount of anticurl, the curl carrying twist +θ and the anticurl −θ:
   Δ(curl) = Δ(anticurl) and τ(curl) + τ(anticurl) = 0.
5. **Charge** (hers, T2, confirmed): where a full turn of twist closes round a loop there is one charge,
   Q = Σ_loop τ_p ∈ ℤ, and each charge costs half a unit of curling energy: E_Q = 2(λ − 1)|Q|.
6. **Twist comes in fixed pieces** (hers, Update 97 and 19:39 UTC): matter twist in thirds, τ ∈ {±⅓, ±⅔}, on body
   diagonals, two-sided; dark twist in halves, τ = ±½, on face diagonals, one-sided. A matter strand closes on a whole
   number: Σ thirds ∈ ℤ.
7. **Spin** (hers, 19:39 UTC; **open**, see below): one whole set of quarks plus one half curl is a particle of spin 1.

## What follows exactly

- **Thirds never make a half** (exact): k/3 = m + ½ would need 2k = 6m + 3, an even number equal to an odd one. So no
  sum of matter twists gives a dark twist, and a single half never closes with thirds; k/3 + j/2 is whole only when j is
  even and k is a multiple of 3. The two sectors stay separate under rule 6 by arithmetic, which is her "combined
  twists of ⅓ can't get you there".
- **Charge and quark count** (exact, Update 97): with Q the charge in whole units and t = quarks minus antiquarks,
  3Q + t ≡ 0 (mod 3) for every observed particle (published form: Tong 2017, abstract read).
- **Spin one half is not in the toy as it stands** (exact, Update 97): any state built from link labels comes back with
  sign +1 after a full turn, so a half-integer spin has to be put in. **Open:** in rule 7, is it "a quark set gives ½
  and the half curl gives ½, total 1", or something else? (A photon has spin 1; one electron-positron pair is the
  usual "whole set plus...", general knowledge, to verify.)
- **The halves of the burp** (exact, O164): under the soft penalty with μ₀/N an unbalanced rod's two openings release
  aN + 3μ₀N/16 and aN + μ₀N/16, a = 4(λ − 1); they are equal only if μ₀ = 0 or the rod is balanced (rule 1).

## What could follow, to be tested (ours)

- **Slower curl near twist (T4) can follow from rule 3 without being written in.** In the chain a move that raises the
  energy by κT is accepted with probability e^(−κT/g), so a front crossing twisted squares advances less often, by that
  factor. Testable: measure the front's pace against the twist it crosses, with nothing about speed written in.
  (Caution: the chain's clock is a count of attempts, not physical time.)
- **Which twin we are in.** See "Unequal twins" below.

## κ, in plain terms (ours; general knowledge, to verify)

κ is a **coupling constant**: how strongly one quantity feels another. Physics has a few, and each gives a way to read κ:
- **The electric charge** (the fine-structure constant α ≈ 1/137) says how strongly light and matter feel each other.
  κ plays that part between twist and curl. Only the ratio κ/4(λ − 1) matters, the way only α matters, not e alone.
- **Couplings change with scale.** α is about 1/137 at everyday energies and about 1/128 at the energies of the Z
  boson, because the vacuum screens charge at long range (the "running" of couplings, renormalization). So κ need not be
  one number at every scale: the κ put into the toy is the bare value, and the κ seen at large scale could come out
  different. Whether it does is a result the toy could give, not something we set.
- **Kaluza–Klein:** a curled direction seen from the large ones looks like a charge, and the charge's strength is set by
  the curl's size (smaller curl, stronger charge). That is the published case nearest to "twist and curl affect each
  other": the coupling is not free there but fixed by the curl. If the toy showed κ's effective value set by curl size,
  that would be a real link to the published physics.

## Unequal twins: why only they change the answer (ours, unverified)

Her measure counts observers who evolved. The chance of finding ourselves in a twin is its share of all observers, and
the time we most likely see is when that twin's entropy production peaks (H7).
- **Equal twins** (mirror images: the same energy, the same history): each holds half the observers, and their peaks
  fall at the same time after the shared birth. Adding the second twin doubles the count and moves nothing: the most
  likely time is the same as with one universe. A twin of antimatter is still equal in this sense, since its observers
  are made of antimatter and call it matter.
- **Unequal twins** (one gets more of the release, or more matter that can build stars): the richer twin holds more
  observers, so we are more likely in it, and the most likely time is that twin's peak, not an average. That turns the
  twin picture into a prediction: we live in the twin that produced more entropy. The toy has a source of inequality
  already: the soft penalty's unequal halves above; and her surplus mechanism (H4) splits matter from antimatter,
  which by itself does not make the twins unequal.

## Published relatives (general knowledge, none read, to verify before citing)

Universes born in both time directions with the arrow pointing away from the middle: Carroll and Chen 2004. The
universe before the bang as our mirror image: Boyle, Finn and Turok 2018 ([BFT18]). Two arrows of time from one central
point: Barbour, Koslowski and Mercati 2014. Observers where entropy production peaks: the causal entropic principle
(Bousso, Harnik, Kribs, Perez 2007; [BHKP07], read).

## Still to decide before any build (hers)

1. ~~Rule 3: κ on curl only, or on anticurl too.~~ Both (19:50 UTC).
2. Rule 7: what the spin sum is. And the twist: phase, count, or both. (Rule 2: version B, chosen.)
3. ~~Question 5: how the twist moves when a link is rewired.~~ Falls away (00:14 UTC, 28 October): twist is what curl
   does to the diagonals, read from the wiring, not a separate field ("Without a curl there is no twist. They are
   defined by each other"). In discrete increments, so a count, not a free phase.
4. Rule 4 as written makes every move conserve twist and balance curl at once; whether the toy's single switch can ever
   satisfy it is an exact count to run first (ours: it may need two switches at once, as the hard rule did).
5. ~~Where the twist lives.~~ Answered (00:14 UTC, 28 October): dark, ±½ on the face diagonals of the squares;
   matter, in thirds on the centre diagonals of 1 × 1 × 2 boxes (replacing Update 97's cube body diagonals). Cost:
   "1 photon per spin unit on a net 1 twist particle"; what one photon is in energy units is open. *Exact:* the
   wiring alone has no handedness (a graph and its mirror image are the same graph), so a signed twist read from it
   needs an orientation from outside, such as the starting lattice's coordinates.
   Hers (00:19 UTC): clockwise from the starting lattice; black and white points never switch; a mirror world swaps
   left and right and matter and antimatter. *Exact:* every diagonal named above joins two points of one colour, so
   each carries a fixed colour; *proposed, hers to confirm:* twist on a black diagonal +, on a white one −. Swapping
   the colours everywhere is an exact symmetry of the energy.
   What breaks it (hers, 00:32 UTC): the shape, the sphere-shell form of the curled slab seen from the rod. *Exact:*
   a closed shell of squares has Σ(4 − squares at a point) = 8 (Euler), so it carries fixed poles whose cost does not
   grow with size; one rotation reads clockwise at one pole and anticlockwise at the other. *Ours:* the toy has no
   motion, so the whirlpool's sense must be in the starting arrangement.
   Conversion (hers, 00:48 UTC): a full turn is 3/3 along a box diagonal or 2/2 along a face diagonal; half a curl is
   180° in one direction. A square's two face diagonals are a left and a right half twist and cancel (net 0); a net-0
   pair takes a photon without charge or spin, or closes as a Möbius band, or loops on itself holding one twist, charged
   and spinning, another kind of quark. *Exact:* an open 2 × 2 × 2 block has 12 boxes of 1 × 1 × 2 and 48 centre
   diagonals; 36 squares (24 on its surface; her 24 counts these, each square one cancelling ±½ pair, confirmed 00:50 UTC), 72 face diagonals. On a Möbius band a diagonal's slant flips going once
   round and its colour does not. **DECISION (01:35 UTC): one extra square on a link is one whole curl,
   360°**; it gives a face diagonal two half twists and a box diagonal three third twists.
   **DECISION (02:05 UTC): a photon is half a curl on one diagonal**; a second gives the antimatter half curl. The dark
   photon is the full-curl unit of half twist on a face diagonal that joins two Möbius strips (hers). *Exact:* each square
   carries 2 face diagonals (one black, one white) and is pierced at its centre by 4 box centre diagonals (2 black,
   2 white); per point, 6 face and 12 box diagonals.
   **DECISION (2026-10-28, 06:12 UTC): what is whole is the total twist around a closed loop; links are not real (hers),
   the toy counts curl on them as bookkeeping. DECISION: twist can hold a photon's half curl, as charge.** Ours, the
   form: τ_d = s_d [round(n_d C_p)/n_d + h_d/2], h_d the photons diagonal d holds; energy term ε Σ|h_d|, ε open.
   **Requirement (hers, 2026-10-28, 07:12 UTC): the toy must allow electromagnetism in 3D spacetime.** Charge exists on the
   sheet (whole twist round a loop); a force between charges at a distance does not (O22). A new ingredient under S1;
   needs a dated VISION decision before it is built. Candidate, published: Wilson's lattice form (a phase per link,
   energy from the phases round each square; general knowledge, not read). Hers also, 2026-10-28: a gluon is untwisted curl,
   a loop folds when curl cannot pay a twist. *Ours:* loop total = twist + fold (Călugăreanu), charge from twist, mass
   from |twist| + |fold|; a neutral spin-½ loop only as a one-sided (Möbius) closure.
   **DECISIONS (2026-10-28, 07:26 UTC):** (1) one-sided loops use the published Möbius formula, linking = twist + 2 fold
   with linking odd (Denne–Larsen 2023, read in part, proof to verify); (2) the toy gets a carrier for electromagnetism;
   (3) it lives on links, which are scaffolding in 3D spacetime and absent in 2D, where only twist and curl exist; a
   link is the unit of movement and the link count is distance. Hers: in flat spacetime points and links are added
   freely, in rows, at the speed of light. *Ours:* that is a varying count (parked, VISION claim 3) and needs its own
   decision; the carrier is Wilson's form and needs a VISION update before it is built. Open: whether the slowed
   diagonal is the face (√2 in 3 ticks, 0.47) or the body diagonal (√3 in 3 ticks, 0.58).
   **DECISIONS (2026-10-28, 07:43 UTC): the carrier lives on the links; the count stays fixed** ("count is stable near
   mass"). *Exact (sandbox look, `sandbox/link_carrier_dirac_wilson.py`):* an angle per link gives a whole monopole
   number per cube; only whole charges couple to a closed loop, the proton's three thirds passing as one loop; a
   carrier with 180° steps cannot tell +1 from −1, so the carrier needs finer steps than a half curl (60° steps
   separate −2 to 2). Her "2-length diagonal": the body diagonal plus an edge is the (1,1,2) box diagonal, √6.
   **DECISIONS (2026-10-28, 13:03 UTC): gravity's carrier is on the links; gravity is 3D only and comes with moving matter; the diagonals making the lattice rigid is a feature; the wiring is not fixed; the point count is constant in curved space and grows where curl meets flat space; the body diagonal is the axis through the triangle of face diagonals, not a side of it.** *Exact (`sandbox/pyramid_check.py`):* in one cube the four black corners are a regular tetrahedron of face diagonals, each face with one edge per family, each body diagonal the axis of one face. *Exact (`sandbox/gravity_carrier_isotropy.py`):* with distance counted in links at her weights every diagonal ties with its edge path, so the pull of one source differs by direction, 1/√2 along a face diagonal and 1/√3 along a body diagonal at every range; with Regge's lengths the worst direction is 0.92 and does not shrink; a scalar on the points goes to 1. *Ours, general knowledge, to verify:* the measured pull is the same in every direction to far better than that, and measured clocks run slower near matter, not faster.
   **DECISIONS (2026-10-28, 13:18 UTC): the isotropy prediction DIRECTION-DEPENDENT is hers, confirmed; the links carry the lattice's lengths (Regge's √2, √3, √6); a link's value is set by its own energy, its curl.** *Exact (O22):* a relic's curl sits on its own links and the energy beyond them is additive, so a value set by a link's own curl reaches no further than the relic; a pull at a distance needs the curl to spread or the value to be solved from a spreading rule sourced by curl. The response rule (how a link's value moves twist and curl) is still owed. *Ours:* twist has two signs by colour, so the antimatter daughter is the colour-swapped daughter, and the toy's energy is colour-blind, so the two tie exactly.
   **DECISIONS (2026-10-28, 13:32 UTC): the two daughters are the colour-swap pair (a symmetry, not an ingredient); annihilation is a black and a white twist neutralizing, their curl leaving as two photons; surplus matter in a daughter is the twists whose partners are in the other daughter; what spreads at no energy cost is the links' length, twist counts and charges staying fixed; the response rule is that a loop shifts toward a shorter path.** *Ours:* that spread is the value spreading, not curl (curl is whole and costs 4(λ − 1) per unit); the carrier of Update 96 already spreads by its own action, and Regge's variation of a discrete curvature action with respect to link lengths is the published way for lengths to obey an equation rather than a hand-put rule (to verify; needs Ollivier curvature on weighted graphs). The constant α in length = lattice length × (1 + α|curl|) is not yet hers.
   **DECISIONS (2026-10-28, 13:42 UTC): one constant α, scanned and published; Regge's route first, the smoothing rule as the control; her predictions: the two-relic gap CLOSES, the warm sheet's correlation is SHORT (T83, pre-registered and running).**
   **KILLED (2026-10-28, 15:51 UTC; Codex audit O166 (2)): spin angle = ½ × net twist angle, with charge = net twist.** Spin would then be a function of charge; the neutron (charge 0, spin ½), the charged pion (1, 0) and the photon (0, 1) break it. Replacement hers to propose; those three particles are the first test of any replacement. The thirds, the colour sign, the loop total and the pyramid are untouched.
   **HER REPLACEMENT (2026-10-28, 15:59 UTC) for the killed spin rule: "the photon applies energy to the net twist which together gives charge."** *Ours, as read:* charge = net twist + photons held (the sheet's τ with h), spin = ½ × the twist angle without the photons. *Exact check on the three particles:* neutron, twist 1 with a photon of −1: spin ½, charge 0, passes; charged pion, twist 0 with one photon: spin 0, charge ±1, passes; the photon alone, no twist and one half curl: this rule gives charge 1 and the ribbon rule spin ½, against the measured 0 and 1: fails as read, so the photon as a free particle needs its own reading (hers). What the neutron then is: a proton's loop holding one photon of the opposite sign, which makes its mass the proton's plus a photon's and its charge zero; whether the toy can hold such a thing is untested.
   **DECISION (2026-10-28, 19:35 UTC): THE UNIT. The closed loop of three white thirds (−⅓, −⅓, −⅓), net twist −1, no fold, is the electron: mass 0.511 MeV, charge −1, spin ½.** One unit of twist-mass is therefore 0.511 MeV. *Exact, ours, under mass = |twist| + |fold| in one unit (that fold weighs as twist does is the sheet's reading, not yet hers):* the proton holds 1835.2 units of fold (1834.5 if |twist| counts the thirds, 5/3); the neutron, a proton holding one photon of −1 under her spin replacement, makes that photon 2.531 units (1.293 MeV); the charged pion, twist 0 with one photon, holds 270.6 units of fold. Not predictions: what the loops must hold. First exact check: whether a compact lattice loop can hold 1,835 units of writhe (at most 0.26 per diagonal so far, so some 7,000 diagonals).
   **DECISIONS (2026-10-28, 22:00 UTC): mass counts looped diagonals, twisted or not (fold is a shape, not the mass; mass = |twist| + |fold| was ours and is withdrawn); a particle is a closed loop or several, with one curl of energy (a fully curled diagonal) per loop or full coil; an extra half curl giving a net curl is held as spin and makes an ion; gluon folds are the glue that keeps the opposite-handed twists in the proton's long coil apart while they net to +1 or −1 (her corrections, 22:21 and 22:27 UTC: the coil, not the atom).** Her questions: longer diagonals such as (1,1,4) as flat loop segments (*exact:* even parity, length √18 = 4.24, so allowed by colour); untwisted loops joining long coils that take curl as heat. *Exact, with her unit:* one looped diagonal is 0.1703 MeV; proton 5,508 diagonals, neutron 5,516 (held photon 7.6 diagonal-masses), charged pion 819. *Ours, to verify:* mass proportional to length puts the proton-to-electron size ratio between 12 (packed) and 1,836 (straight); measured, above about 800 (0.84 fm against no electron structure below 1e-18 m), so the proton would be an extended loop. *Corrected 22:21 UTC:* not a needle; a large open ring (13,500 links of strand, 4,300 across as a circle, 2,800 crumpled a little) meets the scattering bound on the electron (about 1e-18 m) with a link near 3e-19 m, while a compact fold (18 links) or a random crumple (116) cannot; under the moment-based bound (near 1e-22 m) no shape can, so which bound applies to a twist loop decides the reading (general knowledge, to verify). *Annihilation under her rules (ours):* e⁺e⁻ cancel twists, the diagonals go flat, two held spins leave as two photons; p p̄ cancel twists but keep 11,000 looped diagonals of curl, which must break into smaller closed loops, her pions, as measured (about five pions on average).
   **HER READING OF THE FREE PHOTON AND OF PHOTON–MATTER RULES (2026-10-28, 22:55 UTC).** The free photon is half a curl moving along a body diagonal as a wave, spiralling forward at 45° round a four-cube loop at one link per tick (the speed of light and of flat space opening), at no energy cost because links are flexible in length; the link it is on lights up as the box diagonals round it twist and untwist for that moment (a quarter curl per two-cube, brief matter–antimatter pairs); the spiral is smooth. A closed surplus loop takes one photon as held spin, which gives it charge; two photons closing an open diagonal make a matter and an antimatter loop that cancel at once and return the photons; a surplus loop holds one photon, a twisted loop a second as spin, a further photon excites it. *Ours:* this closes Update 138's open item (the free photon is not held, so charge 0; its spin the spiral's full turn); her pair rule carries the measured pair threshold by the unit (two photons of 0.511 MeV); a passing wave leaves no heat in a lossless medium, the toy's light field conserving energy at fixed wiring with dispersion only; heat needs an absorber, as her excitation rule says.
   **DECISIONS (2026-10-28, 23:20 UTC): a photon's excitation is of the electron's orbit round the nucleus, the known science (her 'a further photon excites the loop' is replaced); gravity travels through the cube edges (the axis links) and light through the body-diagonal links.** *Ours:* light then reads the edges' halo only through the body diagonals; the next decision is how a body diagonal's length is set: derived from its cube's edges by geometry (√(ℓx² + ℓy² + ℓz²), no new constant) or its own variable. With the derived form light couples to the halo with coefficient 1 and matter with α, so γ = 1 pins α and the pull's strength becomes a prediction.
   **DECISIONS (2026-10-28, 23:29 UTC): a body diagonal's length is derived from its cube's edges by geometry; the proton is a large closed ring of about 5,500 diagonals; the scattering bound on the electron's size is the operative one; the diagonals are built as variables before any wiring-knot search (option B).** Brief: `diagonals_brief_2026-10-28.md`.
   **DECISION (2026-10-29, 00:35 UTC): a diagonal has twist only where it has curl; no curl, no twist, no degree of freedom.** Twist is read from the wiring's curl (the sheet's τ) and is not a state of its own. *Exact, the spectrum (ours):* every closed loop of box diagonals is one colour, so its charge is k/3 with k its twisted count, whole for k a multiple of 3; 'one curl per loop' gives charge 1 at every loop length, a charged particle at every n × 0.170 MeV from n = 3, and nothing charged is measured between the electron and the muon (621 diagonals). Her three stability candidates, checked: fold whole is killed (48 five-loops have |fold| = 1.000), a minimum coil gives about 3 MeV, the pyramid 0.68 MeV; none makes the gap. A stability rule is missing.

   **CORRECTIONS AND POSITIONS (2026-10-29, 10:46 UTC; VISION Update 145).** The pyramid has no 1 × 1 × 2 diagonals (its sides are face diagonals, its axes body diagonals), so it has no mass and was never a candidate: 'the pyramid 0.68 MeV' above was our miscount, withdrawn. A diagonal runs black to black, an anti-diagonal white to white (exact). A passing photon puts about a quarter twist and anti-twist on the diagonals beside it, uncharged and gone once it is two links on; a photon excites only a loop that already has mass, the first giving spin and more exciting it further; photons are caught by the electron field; the electron is the smallest charged mass; a coil can exist uncharged. *Ours:* the spectrum problem is therefore two-sided (uncharged loops at every length too); the free electron's spin ½ needs a holder under 'spin with the first photon'; and the toy gives a loop an energy of one curl whatever its length while its mass is its length, two numbers where E = mc² has one.
   **DECISIONS (2026-10-28, 08:02 UTC): the lattice's lengths are used (√6); the carrier has 60° steps; each ⅓ twist
   carries 60° of spin, three together 180° on the closed net-1 loop.** *Exact:* spin angle = ½ × net twist angle round
   the loop; net 1 gives 180°, an odd half turn, spin ½ and charge 1; net 2 gives spin whole; net 0 two-sided gives
   spin 0. *Ours:* "net", not "absolute", is the reading taken (with |twist| the proton's 5/3 would not give a half).
   **DECISION (01:28 UTC): the sign is the colour of the diagonal, black +, white −.** The photon is its own unit of
   energy, not tied to λ (hers: λ − 1 measures the daughter's surplus); one photon gives a loop of net twist 1 spin ½ and
   one charge; spin comes only in halves; a dark (face-diagonal) pair takes no charge or spin, holds a full or double
   curl, and is smaller. *Exact:* per point of a cubic lattice, 6 face diagonals and 12 box centre diagonals, so 3 and 4
   turns of twist at full size, 3 : 4. The rest of the original item: Rules 3 to 5 put it on squares (the light field's phase, built, a true mirror pair); rule 6
   follows Update 97, which put thirds on cube body diagonals and halves on face diagonals. A face diagonal crosses one
   square and a body diagonal crosses a cube, so the two can be joined (a square's twist read along its diagonal; a
   cube's from its six faces), but how is a choice: hers.
