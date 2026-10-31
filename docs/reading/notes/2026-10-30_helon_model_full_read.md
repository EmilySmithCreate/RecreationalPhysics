# Reading: the helon braid model (Bilson-Thompson 2005), read in full against the twist-and-curl rules of 29 October

A reading note, not a prior-work search. The owner asked on 29 October (23:50 UTC, verbatim in `sandbox/NOTEBOOK.md`):
"The helon braid model. Bilson-Thompson's picture of particles as braids of ribbons with twists in thirds, the closest
published relative of your loops. Already owed as a reading please read it." This note records what the paper says,
section by section with short quotations, and then sets each of her standing rules
(`docs/design/twist_curl_rules_current.md`) beside it. Where the two differ, the difference is given its kind under
rule 23 (convention / measurement / theory structure). **No tracked file other than this note, `REFERENCES.bib`,
`sandbox/NOTEBOOK.md` and VISION (one addendum) is changed.**

Kinds of statement (rule 10): **published** (what the paper says, with the section); **exact** (arithmetic on what it
says); **hers** (her rule); **ours, unverified** (our comparison). "General knowledge, to verify" marks a statement from
memory, not checked at a source here.

**Date:** 2026-10-30, 01:16 UTC by the clock (the evening of 29 October in the owner's time zone). **Who read:** the
assistant session (Claude Fable 5.1), in the worktree `particle-sector`. The owner has not read the paper.

## 1. Source and read status

**[BT05]** S. O. Bilson-Thompson, "A topological model of composite preons", arXiv:hep-ph/0503213v2 (v1 22 March 2005;
v2 27 October 2006, "added info about hypercharge, lepton number"); report ADP-05-05/T615; no journal reference on
the arXiv page. **Read in full:** all six pages, from the arXiv v2 PDF converted to text with PyMuPDF, and the four
figures seen as rendered pages (Figs. 1 and 2 on page 3, Figs. 3 and 4 on page 4). The reading of 21 October
(`2026-10-21_matter_as_loops.md`, Sec. 3) had the text but not the figures; it is not changed, and nothing below
contradicts it.

**[BTMS07]** Bilson-Thompson, Markopoulou and Smolin, Class. Quantum Grav. 24, 3975 (2007), arXiv:hep-th/0603022: its
arXiv abstract page was re-read today (abstract only this time; Secs. I to IV and V.A were read on 23 October). Not
re-read beyond that; what is said about it below is from the earlier notes.

**Not read:** the rishon papers it builds on, Harari, Phys. Lett. B86, 83 (1979) and Shupe, Phys. Lett. B86, 87 (1979)
(its refs. [3], [4]); Harari and Seiberg (1981) on hypercolour (ref. [5]); the later braid papers by Bilson-Thompson,
Hackett, Kauffman and Smolin (general knowledge, to verify). Robson (2002, 2004), its ref. [10], not read.

## 2. What the paper says

**The objects (Sec. II).** The fundamental thing is a half-twist in a ribbon: "twists through ±π in a ribbon", called a
dum (+π) and a dee (−π), together "tweedles". Assumption 1, "unique to the helon model": "Tweedles combine in pairs, so
that their total twist is 0 modulo 2π, and the ordering of tweedles within a pair is unimportant." The three pairs UU,
EE, UE are ribbons with twist +2π, −2π, 0, called helons H+, H−, H0, and "A twist through ±2π is interpreted as an
electric charge of ±e/3." Assumption 2: helons "bind into triplets", drawn as three strands joined at the top and at the
bottom (two disks joined by three strands); a triplet may split in half or two may merge. Assumption 3, "No charge
mixing": "we will not allow H+ and H− helons in the same triplet"; H+ with H0 and H− with H0 are allowed. Assumption 4:
"All unbraided triplets must carry integer electric charge." A fifth assumption comes later (below). He states that
assumptions 2 to 4 "are merely restatements in a different context of assumptions that Shupe and Harari made."

**Why three (Sec. II).** "three helons seems to be the minimum number from which a stable, non-trivial structure can be
formed. By stable, we mean that a physical representation of a braid on three strands (e.g. made from strips of fabric)
cannot in general be smoothly deformed into a simpler structure. By contrast, such a physical model with only two
strands can always be untwisted."

**Colour as ordering (Sec. II).** An unbraided triplet is symmetric under rotation by 2π/3, so the three strands cannot
be told apart; braiding makes them distinct, and the three positions of the odd helon out are the three colours:
H+H+H0, H+H0H+, H0H+H+ are the up quark in three colours; H0H0H+ and permutations the anti-down; H+H+H+ the positron,
H0H0H0 the neutrino, H−H−H− the electron; the H− triplets give the anti-up and the down. "we have created neutrinos,
but not anti-neutrinos ... because the H0 helon is its own anti-particle." Mass and spin are not assigned to helons:
"It is our expectation that spin, mass, hypercharge and other quantities emerge dynamically, just like electric charge,
as we arrange helons into more complex patterns." Footnote 13: the twist "may be viewed as a spin in some abstract space,
akin to isospin. We will not assume that this is the same as intrinsic angular momentum."

**Antiparticles, handedness, C, P, T (Sec. III).** The anti-braid is "the top-to-bottom mirror image"; braid times
anti-braid "can be deformed into the trivial braid"; a quantity β = ±1 for braid or anti-braid, summed, is conserved in
splitting and joining. Left and right forms are the left-to-right mirror images, "equate[d] with particles and
anti-particles having positive and negative helicity." Fig. 1 builds the first generation by adding zero, one, two or
three charges to a neutral braid. Charged fermions come in two handedness states; the neutrino and anti-neutrino in one
each, because building the second would duplicate the first rotated by π: "This pleasing result is a direct consequence
of the fact that we construct the neutrino and anti-neutrino from the same sub-components." T is a rotation by π with
all charges reversed; C, P, T together leave a braid unchanged.

**Bosons (Sec. III, Fig. 3).** W+ and W− are triplets of three H+ or three H−. Two neutral triplets: "a triplet of
untwisted helons" (the photon) and "a triplet of 'counter-twisted' helons (that is, each helon carries explicit
left-handed and right-handed twists)" (the Z0), which "can deform into each other" (a guess at Weinberg mixing). "What
sets bosons apart from fermions ... is that the strand permutation induced by the braid that forms a boson is the
identity permutation. The simplest braid that fulfills this criterion is the trivial braid." Interactions are "cutting
or joining operations, in which twists (tweedles) may be exchanged between helons" (Fig. 4: a charge-transferring vertex
and a polarising vertex).

**Generations (Sec. III).** Higher generations are "more complicated patterns" of crossing of the same three helons:
"all fermions may be viewed as a basic neutrino 'framework' to which electric charges are added, and the structure of
this framework determines to which generation a given fermion belongs." Emitting a W does not change the braiding, so a
muon must become a muon-neutrino (Fig. 2).

**Colour interaction and hadrons (Sec. III).** Braids stack like pancakes; strands lying one above another form a
"super-strand" whose charge is the sum; braids written as permutation matrices with helons as entries add (Eq. (1),
the neutral pion u_R + anti-u_R; Eq. (2), the proton d_B + u_R + u_G). Assumption 5, "Charge equality": "When two or
more braids are stacked, they must combine to produce the same total charge on all three super-strands." Leptons meet it
trivially and so do not feel colour; quarks must group into colour-neutral sets of integer charge. Gluons: two as
triplets mixing untwisted and counter-twisted strands, six as "the six permutations of one H+, one H0, and one H−".

**Hypercharge from counting (Sec. III, Eqs. (3) to (5)).** Ω = β(N(H+)/3 + N(H−)/3 − N(H0)/3); Q = β(N(H+) + N(H−))/3;
hence Q = (β + Ω)/2. For quarks Ω is strong hypercharge and β/2 the third component of isospin; for leptons the roles
swap. The Gell-Mann–Nishijima relation "may trivially be derived" from the count. Consequence he accepts: strangeness,
charm, bottomness and topness are not quantum numbers here, and the c–s and t–b pairs are isospin doublets, against
the Standard Model's assignment. Lepton number is the braid count (Eq. (6)); baryon number likewise.

**Unresolved (Sec. IV), in his words:** "the origin of spin, the origin of mass, and the nature of Cabbibo-mixing." On
spin: helicity is found, "but not spin itself"; assuming spin-½ helons "would not explain what spin is" and would need
a rule against spin-3/2 composites. On mass: twisting a ribbon crosses its own edges (a generator of B2), so "twisting
(electric charge) and braiding are fundamentally the same process", and "we propose that, roughly speaking, the more
non-trivial the crossings in a fermion's substructure, the greater its mass. Much work will be needed to develop and
test this idea quantitatively." No graviton, no Higgs. Sec. V: "just what physical process (if any) the twisting and
braiding of helons represents" is the foremost open question; the loop-quantum-gravity reading is [BTMS07].

## 3. Her rules beside it, one by one

Each line: her rule (hers), what the paper has (published), the kind of any difference (rule 23), and what follows
(ours, unverified).

1. **Charge in thirds as twist.** Hers: matter twist in thirds on the box diagonals, sign by colour. His: a full twist
   of a ribbon (2π) is ±e/3, built from two half twists that must pair to a whole. *Same claim in two carriers.* His
   unit is finer than hers: the half twist (±π) exists as a part but never alone; her smallest matter twist is ⅓ with
   no half beneath it, and her halves are the dark twist on the face diagonals, which he has no counterpart for.
   Difference of kind: **theory structure** (what carries the twist), stops nothing.
2. **Three is the smallest stable unit.** Hers: the electron is three white thirds, the smallest charged mass. His:
   three strands is the minimum that "cannot in general be smoothly deformed into a simpler structure"; two strands
   "can always be untwisted." *Agreement*, and his reason (the braid group B3 against B2) is one she could use for
   "a loop of fewer than three diagonals holds no twist". Exact, hers, from 29 October: three box-diagonal steps do
   close on the lattice. His argument is about braids, not loops, so it transfers as an analogy, not a proof.
3. **No charge mixing (his assumption 3) against her proton.** Hers: the proton is one long ring holding ⅔, ⅔ and
   −⅓, "twist and anti-twist" in one loop, which "fights itself", with gluon folds keeping them apart. His: H+ and H−
   are never in one triplet, and the proton is three separate quark braids stacked (Eq. (2)); the up quark is H+H+H0,
   with no H− in it. *The direct disagreement.* Kind: **theory structure** (his assumption, stated as inherited from
   Shupe and Harari; not a measurement). It stops nothing of hers, and it names a test: in his model a single
   triplet with +⅔ and −⅓ is forbidden by rule; in hers it is allowed and unstable. The observed proton does not
   decide between "three quarks stacked" and "one ring" at this level.
4. **Uncharged objects.** Hers: an uncharged coil takes no spin, so there is no uncharged electron, and "spin with no
   twist is a second kind of force" that binds nucleons. His: the neutrino is exactly an uncharged braided fermion,
   H0H0H0 with crossings, and it has mass (small) and spin ½ in the world. *Disagreement in words.* Kind: **theory
   structure** at the level of the models, but behind it a **measurement**: neutrinos exist, are neutral, carry spin ½
   and have mass. Her rule as written ("an uncharged coil takes no spin") must either place the neutrino elsewhere (a
   dark-twist object on the face diagonals, halves cancelling to zero, is the obvious candidate in her own scheme) or
   be narrowed to "no uncharged *matter-twist* loop with spin". This is the one line in the comparison where a
   measurement bears, and it is hers to answer.
5. **Antiparticle as the mirror; pairs made and cancelled.** Hers: twist +θ is made with −θ, a black and a white twist
   meeting cancel, and spacetime keeps only the net matter the burp left. His: the anti-braid is the top-to-bottom
   mirror, braid plus anti-braid is trivial, braids "are created and destroyed together, from trivial braids (i.e.
   bosons)", and the conserved β sum is lepton number. *Agreement in form.* His Eq. (6) is the exact version of her "net
   matter stays the same": lepton number = braids minus anti-braids. For her toy the counterpart is the net twist, not
   yet defined (standing rules, Sec. 5, item 6). Good news in the sense she asked for: the conservation she wants has a
   published counting form to copy.
6. **The photon.** Hers: half a curl with one unit of spin, running along the body diagonals as a spiral; beside it a
   quarter twist and anti-twist, gone two links on. His: the photon is the trivial, untwisted triplet; the Z0 is the
   "counter-twisted" triplet, each strand carrying a twist and an anti-twist. *Different objects.* Her "quarter twist and
   anti-twist beside the photon" is in form his counter-twisted strand, which he uses for the Z0, not the photon. Kind:
   **theory structure**. No measurement here; both are pictures.
7. **Spin.** Hers: spin × curl = ½, "precise"; charge is twist carried by spin. His: unresolved; helicity is found as
   handedness of the braid, spin is not, and he refuses to assume it. *Hers goes further.* This is where her rules can
   fail and his cannot: his makes no spin claim. Note his footnote 13: the twist "may be viewed as a spin in some
   abstract space, akin to isospin", explicitly not angular momentum, which is the opposite of her identification.
   Kind: **theory structure**.
8. **Mass.** Hers: mass counts looped diagonals, a long diagonal counting one; the electron's unit 0.1703 MeV. His:
   unresolved; a guess that more crossings mean more mass, with generations as more crossing, "roughly speaking". *Hers
   is a definite count where his is a direction.* His guess and her count agree in sign only if her higher-generation
   loops hold more diagonals, which they do (muon 621). Neither has produced a mass number; his says so.
9. **Generations.** His: same three helons, more complicated crossing; a neutral "framework" fixes the generation and
   charges are added to it. Hers: the muon is three thirds with 206 gluons in each run (exact under equal spacing and
   the count rule). *Same shape:* the charge sits on the same three carriers and the rest of the object sets the
   generation. His framework is braiding; hers is the untwisted length between twists. His model, like hers, has
   no rule that picks out why the second generation is where it is: the gap problem (1 to 205 gluons per run) has no
   counterpart he solves.
10. **Colour.** His: the position of the odd helon in the ordered triplet, made distinct by braiding. Hers: not a
    standing rule; the three directions of 29 September (the quark-colour image, Update 30) were set aside in Update 50.
    *Something his has that hers lacks*, and it is cheap: on a loop of three twisted diagonals with gluon runs between,
    the position of the odd twist is only distinct if the loop has an orientation or a marked point. Whether her loops
    carry colour is open and was not asked.
11. **Gluons.** Hers: a long untwisted diagonal holding curl, no twist, no charge. His: six gluons are the permutations
    of H+, H0, H−, triplets with mixed charges, and two mix untwisted and counter-twisted strands. *Different objects,*
    and his gluons carry twist (charge ±⅓ on strands) where hers carry none. Kind: **theory structure**. His assumption
    3 does not apply to gluons (they are unbraided), which is why they may mix H+ and H−.
12. **Hypercharge and the Gell-Mann–Nishijima relation from counting.** His Eqs. (3) to (5). Hers: nothing yet. *This is
    the paper's one derived relation*, and it is the kind of result her question of 29 October asks for: a quantum
    number that is a count on the object, and a textbook relation that falls out of two such counts. The price he pays
    is stated: strangeness, charm, bottomness, topness are not quantum numbers, and the second and third generation
    quarks become isospin doublets. (General knowledge, to verify: the Standard Model's assignments are the measured
    ones; his is a reinterpretation of the same data, so this is a **convention** difference as he frames it, and he
    says so.)

## 4. What the reading does for her programme (ours, unverified)

- **Confirmed as the nearest relative.** Charges in thirds as twists on three strands, three as the minimum, the
  antiparticle as a mirror, pairs from and to a trivial object, the photon as the twist-free object, lepton number as a
  signed count, generations as more structure on the same three carriers: all of these are her rules in his carrier.
  Nothing in it is a lattice, a loop, a curl of space or a count of mass, and it has no dark sector.
- **Where hers is ahead and therefore exposed.** Mass as a count and spin × curl = ½ are definite where he stops. That is
  the right place to be for a theory that wants to fail: his model cannot be wrong about a mass because it gives none.
- **Where his is ahead.** A derived relation (Q = (β + Ω)/2) from counting alone; colour as a derived ordering; a
  neutral fermion with spin. The first two are things her loops could be asked to give; the third is the one
  measurement-backed objection found today (item 4), and the question for her is where the neutrino lives in her
  scheme.
- **The two assumptions that clash with her proton** (no charge mixing in one triplet; the proton as three stacked
  braids) are inherited rules, not measurements, and they stop nothing.
- **What would change this reading:** the later braid papers (Bilson-Thompson, Hackett, Kauffman, Smolin), which are
  said to give the braids dynamics and may address spin or mass; the rishon originals, for whether "no charge mixing"
  was ever argued from data. Neither is read.
