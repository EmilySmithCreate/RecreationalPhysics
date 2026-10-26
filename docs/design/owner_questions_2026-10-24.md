# Questions waiting on the owner (kept current; updated 26 October 2026)

*One list of everything that needs her answer before the work can move. Each item says what it decides and where the
full text is. Answer in any order; items marked ★ unblock the most. Answered items are moved to the end with the date.
Her words of 25 October are in `sandbox/NOTEBOOK.md` under that date (her two passes of `#` notes on this file kept
verbatim there); the record is VISION Updates 104 to 112.*

## Open, 26 October: the hard rule and the twin X (start here)

*After the fourth Codex audit (ASSUMPTIONS O159, VISION Update 129) and three readings of the same day
(`docs/reading/notes/2026-10-26_constrained_moves_kcm.md`, `2026-10-26_subgraph_count_ensembles.md`,
`2026-10-26_paired_defects_gauss_bonnet.md`; read by assistant agents, quotations to check against the PDFs). For each
question: what the runs and the reading say, the assistant's recommendation, and what your answer lets us test. Labels:
exact (arithmetic or complete enumeration), look (a sandbox look: can kill, never crown), published (read, with the
note), ours (an interpretation, unverified).*

**Q1 ★ Your hard rule freezes clean space. Keep it as is, extend the moves, or soften it?**
You confirmed the hard form on 25 October (squares held at exactly 3N; a move allowed only if it keeps the count).

- *Exact (Update 128, as corrected by O159).* Out of flat six-link space (the 6 × 6 × 8 torus) no single switch keeps
  the count, and no pair of switches within two links of each other does, except undoing the first. In damaged states a
  few switches keep it (42 in 274,248; 57 in 272,560; 14 in 282,861). So under the rule clean space cannot move at all
  and damaged space moves rarely.
- *Published.* This is the known behavior of systems where only moves that keep a total are allowed (kinetically
  constrained models, Ritort and Sollich 2003): order freezes and only defects move, and an ordered state can sit in a
  sealed-off compartment of its own that no allowed move enters or leaves. Closest to the toy: Nishimura 2017 (already in
  our bibliography as [Swap17]) shows that graphs with fixed degrees *and* a fixed triangle count can be cut into
  separate compartments unless a move rewires 8 or more links at once, which is four switches. A soft penalty restores
  the connections, and at a large enough strength it gives the same results as the hard rule (Costeniuc et al. 2006,
  provided the entropy curve has no corner there).
- *Ours, from the reading.* The soft form μ(S − 3N)² grows with the square of the system's size, so the scan has to fix
  in advance whether μ stays fixed or shrinks with size. At large μ a flat start stays frozen for the same reason as
  under the hard rule, so every soft run must start from both sides (flat, and damaged) and show that the two meet.
- **The options.** (a) The soft form, μ scanned, runs from both sides. (b) The hard rule with compound moves: first an
  exact count of three- and four-switch moves out of flat space (cheap, no decision of physics). (c) The hard rule, X
  built from damaged states: results may depend on where they start.
- **Recommended:** (b)'s exact count first, because it costs nothing and decides whether the hard rule can work at all;
  then (a) if it finds nothing.
- **What your answer lets us test.** Whether any X that obeys your rule can open into space at all. If four-switch moves
  out of flat space also find nothing and the soft form only ever leaves flat space by damage, the rule as stated
  forbids the clean opening, and that is a result about the rule. If either finds a clean path, the push look can be run
  on the right family for the first time.

**Q2 ★ What does a curled X that obeys your rule look like: where does its anticurl sit?**
Your "proceed" of 26 October answered a suggestion that ended "the shape of that starting X would be yours to
describe". Nothing can be built until you describe it.

- *Exact (ours, arithmetic from the defects note; the check on the toy's states is not yet run).* If every square in the
  six-link toy is a face of a little cube and the cubes close up into a space with no edges, the square count is exactly
  3N automatically: your rule says space is made of whole cubes. The rod breaks it because its tight curl adds squares
  that wrap around the short direction (curl 576). So a curled X that obeys the rule must be *missing* squares somewhere
  to balance those: links where the cubes do not close up.
- *Published.* On a closed surface curvature defects must balance (Gauss-Bonnet; Bowick and Giomi 2009): a curved-in cap
  is carried by a curved-out skirt around it, and on their example surface "disclinations must appear in pairs". That is
  your "curl inside a larger uncurl" (Updates 83, 92) with a picture. *Caution:* in the literature unpaired defects are
  expensive because of long-range strain; the toy's energy is a sum over links with no long-range strain, so that reason
  does not carry over; and the theorems apply only once the toy's squares are read as faces.
- *Look (Update 127, corrected).* In the push runs the anticurl appeared as damage, mostly at broken points (79 states of
  100), on an X that did not obey the rule.
- **The choices, for you to pick or replace.** (i) A collar: the anticurl in a ring around the curled rod, in the space
  around it. (ii) Spread thinly through the surrounding space. (iii) Inside: a hollow or broken core in the rod. (iv)
  In the two slabs, balancing the rod between them (your twin X).
- **What your answer lets us test.** We build that X exactly, check that it is stuck for now (every single move out
  costs), then give it the push. That tests your "they always come in pairs": does opening cancel curl and anticurl
  together, leaving clean space, or does it leave breakage? And it settles whether breakage is damage or your pair, which
  the rod runs could not (Update 127).

**Q3 The pair tie f = (0, 0, a, 0), still marked "to confirm", with three things the audit found.**

- *Exact.* Under it the first opening releases nothing and the second releases 2a per point, so it gives your total and
  your order (first nothing, second everything) but not half to each twin: "half each" would split the second release
  by our choice. The gas of 6-cubes (three directions curled) costs 3a under it, so "curling two costs the same as one"
  holds for one and two only. A slab that was never a rod costs 2a where it cost a.
- *Your words.* Your answer was a conditional, "If each curled direction carries its own curling cost yes…"; we had
  recorded it as a plain yes (corrected, O159).
- *Look.* In the push runs the tie made the second direction follow the first more often, but every opening broke a
  fifth to a third of the points; those runs were on the rule-breaking rod, and under your rule the curling energy is 4λ
  a unit, not 4(λ − 1), so their numbers do not carry over.
- **Asked.** Confirm the tie as written; or say what "half each" should mean in the toy (for instance, each twin's slab
  releasing its own curling cost as it opens, which needs the two slabs to open separately).
- **What your answer lets us test.** Fixes the energy of the rule-obeying X before its push (Q2), so that "the second
  direction follows the first" and "each twin gets half" are tested as written instead of read off afterwards.

**Q4 Pricing broken points (option 2 of Update 125, held).** *Ours:* under your rule the anticurl belongs in X, so
pricing broken points would penalize the very thing your rule requires. **Recommended:** keep it held until a
rule-obeying X has been pushed (Q2). Say if you disagree.

**Older items still open** (full text further down): H3, H4 and H8 of the hypothesis below, not yet confirmed; items 17 to 25.

## Your hypothesis as it stands (25 October): confirm, correct or strike each line

*The assistant's assembly of your answers of 24 and 25 October, so that you can state it in your own words. Each line
says what kind of statement it is. Lines you have confirmed say so.*

H1. **The base** *(confirmed, 25 October)*. The base is two degrees of freedom, twist and curl. Points and links are not
    part of it: they describe the three-dimensional spacetime that emerges, and the toy is built from them for that
    reason. The total of curl and uncurl stays zero, so they appear and disappear in pairs; in the toy, curl is extra
    squares and uncurl missing squares, and the rule is squares = points (hard form, confirmed). *(Published counterpart:
    Gauss–Bonnet.)*
H2. **Light** is the links' collective wave; it keeps its speed in open directions, and the part of it along a tight curl
    gets mass. *(Exact in the toy, O151; published counterpart Levin and Wen 2006.)*
H3. **Matter, as you now state it** *(25 October, second pass; the 120°/60° split is yours, the cube facts exact)*. Every
    strand, matter and dark, is built of three thirds, tying the 12 right angles of three intersecting planes. Each third
    carries 120° of charge-twist, a turn of the grid, and 60° of spin-twist, the strand's own twist angle (your decision,
    Update 109; see S1′). The three together are what can be written
    as three-dimensional space and move; looking at one apart loses degrees of freedom (to see which quark, we give up
    the information of three-dimensional movement). Electric charge is the count of signed thirds and needs mass present,
    not an amount. Handedness marks matter against antimatter and carries its own charge, separate from electric charge
    (the weak force's shape); an antiparticle is the mirror image of its strand. Dark strands are one-sided (Möbius) and
    carry no charge; the whole-twist rule is for matter strands. *(See S1 for what the cube says about a 60° grid turn.)*
H4. **The burp splits matter from antimatter.** When two black holes merge and burp, the spinning hole sorts handed
    strands (through the weak force), the parent keeps a surplus of antimatter and the daughter a surplus of matter, and
    the total over the pair is zero. *(Yours; sorter as the weak force, the assistant's correction; published relatives
    Vilenkin 1978, leptogenesis, Boyle–Finn–Turok 2018, to read.)*
H5. **The pair's curvatures balance** *(confirmed)*: each universe slightly curved, opposite in sign, net flat over the loop
    with every version stacked, because the total over twist and curl stays zero. Your sign: **ours slightly negative,
    the parent slightly positive** (you agreed, and asked for the sandbox look, which follows in C1).
H6. **Expansion** *(confirmed)*: empty space grows at no cost, at a front moving at light's speed, only where space is
    empty; atoms, planets and galaxies count as curved and do not grow; matter clumping slows the overall rate and voids
    taking over speed it up. *(Published shape: Wiltshire's timescape, read.)*
H7. **Why now**: observers are most likely where entropy production peaks, when the slowing and speeding eras balance.
    *(Published: the causal entropic principle, read in full.)*
H8. **Your mechanism for the burp's matter** *(new, 25 October; your words in the notebook)*: the positive background
    (the parent) pulls away our surplus antimatter. Without it, curl costs more than uncurl (λ > 1). When the space snaps
    fully open, it releases the energy in that store as matter and antimatter that cancel perfectly (λ = 1), except for a
    single burp of surplus matter, which then behaves as matter does while space cools and expands; without the missing
    antimatter it would all be light.

## Open, after your second pass

S1. ~~**The 60° spin-twist as a turn of the grid.**~~ *Answered 25 October: "okay, proceed" with (b): the 60°
    spin-twist is the strand's own twist angle, the 120° charge-twist a turn of the grid (VISION Update 109). A twist
    angle on strands is a new ingredient; its form is written before anything is built.*
L1. ~~**Light backed up at the front: which side?**~~ *Answered 25 October: from the curled side (the black hole, in
    the mother's space). Computed (Update 110, exploratory): in the toy's field that light pushes the front toward the
    curl, helping it open, at every frequency; it does not pull curl back.*
L2. ~~**The shell's charge.**~~ *Answered 25 October: confirmed, pairs sorted by the hole's spin.*
L3. ~~**The hold-back as charge, not light.**~~ *Answered 25 October: "Adopt" (VISION Update 111).*
S2. **Pair creation, as you now have it** *(you agreed one photon gives the electron and the positron; and "2 photons
    carry 360, but it is split against the 3 1/3 twists and the 3 -1/3 antitwists")*. On your question "why not? 1
    photon is a half curl / 180 degrees": a photon carries one whole unit of spin, whatever picture we draw it with, and
    spin adds: one whole unit plus whole units stays whole, so one photon cannot leave a single spin-one-half object
    behind; it can leave a pair. Your two-photon picture is observed: an electron and a positron at rest annihilate into
    two photons (general knowledge, to verify). **To confirm:** one photon's half curl means "half a turn of curl in your
    base picture", which in spin units is one whole unit. Agree?
Z2. **Your prediction under the hard rule** *(H8 is your mechanism; the prediction read from it is inferred until you
    confirm)*: a balanced curled X opens with a single sharp, bounded burp, curl and uncurl vanishing in pairs, and the
    release is all light except for a surplus set by the store's imbalance. Confirm this as your prediction, or restate.
    *The toy has no matter or antimatter yet, so what a run could test now is the first half: does a balanced X open
    sharply, with curl and uncurl vanishing in pairs?*
0. **Light and the curling cost under your hard rule** *(you think light lowers it, so a lower g can pay it, and asked
   whether that is consistent with your hard answer)*. *Ours, exact at leading order:* the light field's reward is the
   same amount per square (ln I₀(β) at leading order), and under the hard rule every allowed arrangement has the same
   number of squares (squares = points). So **at leading order, in the strong-coupling (small β) expansion where the
   field is not yet free light, light neither lowers nor raises the curling cost under
   your rule**; both zero choices agree, and item 0's fork disappears. Any effect comes from higher-order terms that
   depend on how the squares are arranged, which can be computed exactly (the method of Update 102). Your "lowered by
   the missing antimatter" is a separate route (H8) that the light field does not supply. **To decide:** compute the
   higher-order terms (cheap, exact), before you settle the sign.
0b. **The electron against three down quarks** *(you asked what follows from the logic: no colour, no twist, unstable
    forms held precariously)*. What it touches (general knowledge, to verify): three down quarks do exist together, as the
    Δ⁻ particle, charge −1, spin three halves, and it lives about 10⁻²³ seconds before falling apart. The electron, same
    count of thirds, lasts forever. So your "unstable forms held precariously" matches what is seen: same count, very
    different binding and lifetime. In your terms the difference would be colour: the electron's three thirds carry no
    colour and close into a stable band; the Δ⁻'s are three colours bound by gluons and fall apart. **To confirm:** is the
    electron's band colourless because its three thirds share one handedness and close flat, while quarks' thirds are
    open ends that must be bound?
0d. **The photon flipping a third** *(you said the flip must happen on a group of twists summing to a whole number)*. A
    group summing to −1 flipping to +1 still changes the charge by 2, which a neutral photon cannot do. Charge stays
    conserved only if flips come in compensating pairs (one +1/3 → −1/3 and one −1/3 → +1/3 together). **To confirm:**
    flips in compensating pairs, or a charged partner (the W of the weak force does exactly this job in standard physics,
    changing a down quark into an up quark with an electron and an antineutrino; general knowledge, to verify).
5. ★ **How a phase rides a switch** *(you found it hard to picture)*. In plain words: when the toy rewires a link, the
   light field had a phase (a small arrow) on the old link. Four ways to handle the new link:
   - (a) **fresh:** the new link gets a random arrow;
   - (b) **carried:** the arrow moves with the link to its new place;
   - (c) **averaged out:** we never track arrows; we add their average effect as a small reward per square (no arrows in
     the run at all; this is "integrated out");
   - (d) **heat bath:** the new link's arrow is drawn to suit its neighbours' arrows, the way a new person in a room
     tends to match the room's mood (the published way).
   *Assistant's recommendation: (c) first, because it is cheap and, under your hard rule, gives an exact statement at
   leading order (item 0); then (d), the published way, to check it.*
11. **Q7, the survival rule:** only which objects last, or also the matter excess; and do the routes to the excess she
    named on 21 October still stand? Your merger split (H4) and store mechanism (H8) are new routes; replace the others
    or join them?
10, 12, 13, 15. **Worksheet items unchanged:** Q6 the mass rule (twist count alone, or plus binding energy; the
    proton is about 1,836 electrons); Q11 three generations; X3 colour; X2 "twist is always the same".
14. **X1** "touches 12 cubes": your H3 now ties the three thirds to the 12 right angles of three planes. Is that the 12
    of X1? If yes, it closes.
C1′. **The sandbox look you asked for came back against the toy reading of "ours negative"** (exploratory;
    `sandbox/opened_space_curvature_sign.py`). In 600 saved four-link sheets that opened by themselves from a curled
    tube while cooling (T51), curl minus uncurl is net **positive** (curl left over) in 519, zero in 80, negative in 1;
    mean +9.2 links' worth; at one tube size (L = 256) smaller the slower the cooling (+10.0, +4.3, +2.3; the +21 earlier
    quoted is a larger tube, corrected after the audit). So in the toy without your rule, a
    space that opened from a curl keeps leftover curl that heals toward flat; it does not end net uncurled. That kills
    the toy reason for "ours negative" (the other three reasons, your own words, Update 83 and timescape, stand, and none
    of them is the toy). It does not crown "ours positive" either: the leftover is unhealed curl from the curled start,
    and the toy has no matter, so it says nothing about uncurl made by matter; under your hard rule the net is zero by
    construction. **You agreed: ours slightly negative, the parent positive (H5).** Your first words (Update 104) gave
    negative for both the hole around us and our universe; the agreement is your later answer. Nothing more to decide
    unless you want the sign open.
C1″. **"Matter as uncurl?"** *(your question)*. In your own picture (Update 83: the uncurl left when matter formed adds
    negative curvature), matter goes with uncurl around it: the matter is the curled strand, the uncurl the space it was
    taken from. *Ours, unverified.* Under your hard rule each curl must come with equal uncurl, so "matter is curl, its
    surroundings uncurl, net zero" is the form that fits. In standard physics matter curves space positively near it (it
    pulls); a void with no matter is negatively curved. **To confirm:** matter = curl, with an equal uncurl around it.
Z1′. **The hard rule and warm spaces** *(you asked whether hard means no variability in higher g)*. Under the hard rule the
    total number of squares cannot change, so a warm space cannot melt into the random tangle (which has far fewer
    squares): the published model's hot phase is forbidden. What still varies with warmth is where curl and uncurl sit
    and how many pairs there are (the surplus X). So: no variability in the total; plenty in the arrangement.
    **Exact, 25 October** (`sandbox/zero_total_rule_reach_n18.py`): at 18 points the moves under the hard rule reach all 9
    allowed arrangements (one piece; three perfectly flat, six with curl and uncurl paired, surplus 2 to 9). At 16
    points no arrangement keeps the rule. So the hard rule does not trap the toy at the smallest size where it can be
    tested.
E1′. **When to update the toy** *(you agreed to adding points; asked when to make each change)*. *Assistant's proposed
    order, one component at a time, each with its own prediction:* (1) the hard rule alone at fixed size (four links):
    does a balanced X open, and do curl and uncurl vanish in pairs (Z2)? (2) the light field averaged out under the rule
    (item 0's higher-order terms, exact, no run). (3) adding points (E1) under the rule: do empty regions grow while
    curled ones keep their size (your E2: yes to both)? (4) matter labels (thirds and handedness) last. **To decide:**
    this order, or another.
S1′. **Your Update 109 decision, with a corrected premise** *(rule-22 audit, Update 112)*. The cube look turned about a
    cube's centre, where a 60° turn with a mirror swaps the kinds. About a lattice point, your picture, it keeps every
    kind. So three 60s give the mirror image (a point flip) but no swap of kinds, and the link to matter and antimatter
    through the kinds is withdrawn. Your decision (the 60° spin-twist as the strand's own twist angle) was recommended
    because a 60° grid step carries a mirror about any centre, which still holds. **Keep the decision?**
L4. ~~**Which charge, or a neutral layer?**~~ *Answered 25 October: "I agree with l4": the hold-back is the
    tension of a neutral layer of paired curl and uncurl at the front (Update 113); the handed charge's reach
    today is tiny, agreed.*
R1, R2. **Reading owed by the assistant** (no answer needed): holography and the area law, dimensional reduction,
    worldsheets, tensor networks (bears on H1); Boyle–Finn–Turok, Popławski, Vilenkin, Fukugita–Yanagida; Bödeker and
    Moore (2009, 2017); Coleman (1977, [C77]); Narayan, Ramaswamy and Menon (2007); Cohen, Kaplan and Nelson; Wald and Blandford–Znajek; Cohen, De Rújula and Glashow; Melia and
    Shevchuk; ALPHA-g (2023); Hofstadter (2007); the timescape quotes against their PDFs.

## Older items (handoffs of 22 and 23 October), unchanged

16. ~~**Her word on the held-out runs** of T71 and T74 at L = 16 (`sandbox/heldout_2026-10-23/`).~~ *Answered 25 October
    (VISION Updates 114 and 115): both go ahead on her registered predictions. Listed here as open by mistake until 26
    October. What remains is ours: T71's L = 16 jobs were queued on 25 October and their results are not yet fetched;
    T74's L = 16 amendment and jobs had not been written or queued; written and launched 26 October on her "Yes please"
    (PREREGISTRATION T74, Amendment 6).*
17. **The runaway remedy for soft space** (`docs/design/regge_stage_b_brief.md`, question 5).
18. **Her prediction for the λ-from-curvature test** (Update 89).
19. **Her predictions for the first soft-space runs** (a disturbance's speed; two knots' pull).
20. **The Eq. (45) ratio test:** continue or drop, and her prediction (`docs/design/eq45_ratio_brief.md`).
21. **T80:** the decisions in its design amendment; the inferred predictions confirmed.
22. **The drift of the background curvature:** settling from above (Update 83), growing (the antimatter shell), or
    replaced by the merger split (H4, H5, H8)?
23. **The twisted-diagonal look on saved end states:** her prediction before any saved state is opened.
24. **Whether the reply drafted for the model's author goes** (`docs/outreach/`, local only).
25. **Whether the ten-step claim on the programme page reads as hers.**

## Answered on 25 October, second pass (her words in the notebook)

- 0a, keep the charge rule: confirmed. 0c, the whole-twist rule is for matter strands; dark matter may be all one-sided
  Möbius strips with no charge. 2, dark strands' colour and sign agree: confirmed. 4, the boundary prediction as read:
  confirmed. C2, the surface is twist and curl: confirmed. Z1, the hard rule: confirmed. E1, adding points to empty space:
  agreed in principle (a dated decision, VISION Update 108; built only when its turn comes, E1′). E2, her prediction:
  curled and matter-holding regions keep their size while empty regions grow, and matter gathers where empty regions
  meet ("yes to both"). 6, the field's coupling tied to the graph's temperature (β = κ/g). 7, the first observable is the
  tube's waiting time; the λ window and the surcharge on curl would depend on the outside's charge, which can vary, so
  daughter universes start with different matter, with similar behaviour, and from inside we may not know the λ we
  started with. 8, four links first (the accepted math the published model and its author use), then six. 9, her
  prediction for the field test still owed. H5's sign: ours negative, agreed.

## Answered on 25 October, first pass

her idea moved from LIGO's burps to the merger split (Update 104; that LIGO's signals are not burps was the
assistant's conclusion, not her answer); the sorter is the hole's spin through a handedness with its own charge; net
flat is over the loop's stacked versions; the partner's sign is opposite because the total stays zero; charge depends on
having mass, not how much; three halves can release a photon when spins realign; the zero-total rule agreed (Update
105); expansion in empty space at light's speed with the eras from the empty share (Update 106); three 60s make the half
(her idea); her first notes on this file (H1, S1, C1, C2, C3, Z1).

## Answered on 24 October

The handoff refines the ring picture; the electron is three thirds closed into a 360° two-sided band; signed thirds on
body diagonals (matter), signed halves on face diagonals (dark); handedness marks matter against antimatter; an
antiparticle is the mirror image of its strand; light on the edges, the twist on the diagonals; pairs close; a lone
third is confined; gluons, her prediction "none"; the proton +2/3, +2/3, −1/3; the photon field built and gated; her
light prediction holds (O151); the design brief for the field on the rewiring graph; charge one rule for all; the neutron
+2/3, −1/3, −1/3, twists cancel to flat, "spin with no twist can be mildly magnetic but no charge"; dark matter as a
one-sided strip, both occur. (VISION Updates 96 to 102.)

## Read-backs after the Codex audit (25 October; VISION Update 117, ASSUMPTIONS O156)

- **RB1. The parent's sign.** Your first words: "the black hole that is technically around us has slight negative
  curvature and long lived matter universes like ours are in a slight negative curvature space, but when the 2 are
  viewed together it is net flat." The record later wrote ours negative and the parent positive. Which do you mean? # #
- **RB2. Net flat over what.** Over the loop's stacked versions (your answer), or over one joined surface (the
  Gauss-Bonnet reading, which needs a surface the toy does not supply)? # #
- **RB3. The sorter's ledger.** Electric charge, baryon number (protons against antiprotons), lepton number (electrons
  and neutrinos against their opposites) and the strands' handedness are four separate counts. Which does the hole's
  spin move? Moving only positrons would leave our side charged. # #
- **RB4. The layer.** The zero total fixes only the overall balance; the neutral layer at the front (L4) is an added
  rule about where the uncurl sits. Ours: keep it as your added rule. # #
- **RB5. Growth.** Points come in pairs (exact). Is space growing by pairs, or by whole rows, all right with you? # #

### Answers on the read-backs (25 October; VISION Update 118)

- RB1: what alternates is matter against antimatter, set by the black hole's spin; all daughters of one mother share it,
  granddaughters take the grandmother's; neutral over versions, over each front, and combining amplitudes. The parent's
  curvature sign is not restated. RB2: one joined surface; the surface is the relation between two degrees of freedom.
  RB5: whole rows, no local pair (a look agrees). RB3 and RB4 still open.

## G1. Growth's rule (asked for help, 25 October)

Growth adds whole double rows where a ring of space is empty. Three ways to decide when a row is added:

- **(a) A clock (recommended).** Each fair sweep, every empty ring gains a double row with a fixed chance p: the speed
  knob, your front at c. Rows are never removed. It breaks equilibrium on purpose: expansion runs one way, like time.
  The rate is put in by hand, so the test is not whether space grows but what growth does to matter: do curled and
  matter-holding regions keep their size, and does matter gather where empty regions meet (your E2)?
- **(b) A price.** Rows are added and removed with a price per point (term 6's μ), accepted by the toy's usual rule, with
  the count of places a row can go in the weight. This is equilibrium: space settles at a size, or grows without end if
  the price is zero, at a pace set by counting, not by a speed.
- **(c) A trigger.** A row is added only when something pays for it, for example energy reaching an empty ring from a
  burp. Growth then follows energy, not a clock.

Ours: (a), because it is your picture (growth at a fixed speed wherever space is empty) and the only one with a speed
in it; (b) answers the audit's point about counting but gives a size, not an expansion; (c) ties growth to energy, which
your "no cost" rules out. # #

G1 answered 25 October: (a), the clock (VISION Update 119). Her pair of degrees of freedom: curl and twist.

Twins confirmed 25 October (Update 120): they replace H4 and H8; each burp gives a pair; each twin carries the full curling cost. **Asked:** one Big Bang then carries two curling costs. Does the parent's gate wait for twice the cost, or is each twin its own layer opening, paid separately? # #
Answered 25 October: one gate, double the bill; both twins released at once (Update 120).

### After the audit of the later record (25 October; VISION Update 121, ASSUMPTIONS O157)

- RB1's "all daughters of one mother share a direction" was our fill-in of an unfinished sentence; superseded by the
  twins (one of each per burp).
- **T1. The twin mechanism as built.** The slab's curl releases one curling cost per opening. So in the toy one opening's
  release goes to one twin, and the second twin's equal share is drawn from the parent's stores at the same moment (the
  double bill paid from what was fed). Is that your picture, or must each twin be its own opening of space (then the
  parent refolds and opens again within the same instant, paid the same way, and the toy needs that built)? # #
- **RB3 reopened by the twins.** If what the spin sorts is electric charge, each twin would be charged. Which count is it? # #

### Read-back of her answer to T1 (25 October; VISION Update 122)

- **T1a. The twins' X.** Each twin comes from its own curled direction, so the twin X has two curled directions (in the
  toy, the rod 4 x 4 x L, one direction open), not the slab (one curled). Right? # #
- **T1b. The cascade.** Both wait for the stores to exceed the barrier; the first opens, the hold-back drops, and the
  second opens at once. In the toy that means the first opening must lower the second's barrier. Right? # #
- **T1c. Energy.** "Each side gets half the curl energy" against "each twin carries the full curling cost" (earlier
  today). Which? # #
- **T1d. T82.** It tests the second twin drawn from the stores, which is not your mechanism. Withdraw it (kept on the
  record, never run) and design the cascade test instead? Ours: yes. # #
- **RB3, via poles.** Is what the spin sorts the direction of a dipole (north up or down), each twin neutral? # #

Answered 25 October (Update 123): T1d withdraw T82; RB3 the dipole's direction, each twin neutral; T1c half each.
- **T1a′. The twin X.** "A rod between 2 curled slabs, a right hand and left hand whirlpool": two curled slabs of opposite
  handedness joined by a rod, each slab opening into one twin. Right? # #
- **T1e. A tie for the pair.** Half each needs curling two directions to cost the same as curling one, which is the
  direction tie withdrawn on 16 October ("all at the last"), now between the twin pair's two directions. Bring it back
  for the pair? # #

Answered 25 October (Update 124): T1a′ yes; T1e yes, the tie for the pair, its form f = (0, 0, a, 0) as read (to confirm); proceed toward a signed twist.

