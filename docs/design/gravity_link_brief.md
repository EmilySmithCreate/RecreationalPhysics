# Design brief: gravity carried on the links

**Confirmed by the author, 2026-10-28, 13:53 UTC by the clock** ("I confirm the brief. We can start with the simpler version as the brief suggests"): the response rule is the simpler one of section 3, and both arms, Regge and the smoothing control, are computed and set against Newton's shape. *Read by fetch the same hour ([T25] Sec. II.2):* the published measure is the uniform measure on the sphere of neighbours (non-lazy), W by Eq. (5), κ by Eq. (4); the hand check reproduces Eq. (8) at S = 0, 1, 2 in two dimensions, so section 4's H_curv is: that measure, with shortest-path distances taken over the link lengths.

Written 2026-10-28 at the author's decisions of that day (VISION Update 136 and its addenda; her words verbatim in
`sandbox/NOTEBOOK.md`, 13:03 to 13:40 UTC). It replaces, for the carrier, option A of `gravity_brief.md` section 6
(a quantity on the points, Update 40); the condition of Update 40 carries over: whatever carries the pull must match
curve-first gravity where Einstein's account has been measured. Everything not marked hers is *ours, unverified*; nothing
here has been run. The model with any of it is our family around the published model, never combinatorial quantum
gravity (Update 22's naming condition).

## 1. Her decisions, which fix the shape

1. **The carrier is on the links**, three-dimensional only; gravity "comes with moving matter, which is only a thing in
   3d". In 2D there are no links to carry it (Update 135).
2. **The links carry the lattice's lengths**: 1 on an axis, √2 on a face diagonal, √3 on a body diagonal, √6 on the
   box diagonal (Regge's lengths, the 0.92 row of `sandbox/gravity_carrier_isotropy.py`). The diagonals making the
   lattice rigid is "a feature".
3. **Source: a link's value is set by its own energy, its curl.**
4. **What spreads is the length**, at no energy cost, while twist counts and charges stay fixed ("the value spreads").
5. **Response: a loop shifts toward a shorter path.**
6. **One constant, α, scanned and published**, not tuned.
7. **Regge's route first**; the nearest-neighbour smoothing rule is the control arm only.
8. **The wiring is not fixed; the point count is constant in curved space** and grows only where curl meets flat space.
9. Her predictions, recorded before anything is built: two relics' gap **CLOSES**; the warm sheet's correlation is
   **SHORT** (PREREGISTRATION T83, running).

## 2. What is exact already, and what it forbids

- At fixed wiring the toy's energy is a sum of per-link terms, so two relics sharing no square are exactly additive and
  nothing pulls at a distance (O22). A length set by a link's *own* curl inherits this: the lengthened links are only
  where the relic is, so decision 3 alone has no reach. Reach has to come from decision 4: the lengths around a relic
  are *solved*, with the relic's curl as the source.
- Counting links at the owner's weights makes every diagonal tie with its edge path (the distance is Manhattan) and the
  pull differs by direction by 1/√2 and 1/√3 at every range; Regge's lengths leave 0.92 in the worst direction, not
  shrinking with range (`sandbox/gravity_carrier_isotropy.py`, 28 October). The measured pull is the same in every
  direction to far better than that (*general knowledge, to verify*), so a link carrier that is the gravity we see must
  hide its directions. This is the brief's standing problem, not solved here.
- A smooth quantity on the points, sourced by relics, gives Newton's shape on the cubic lattice (O61). That is the
  control arm's known answer.

## 3. The form, fixed before any run (ours; hers once she confirms or edits)

State: the wiring (as now) plus a positive length ℓ_e on every link and diagonal of the six-link lattice, starting at the
lattice's lengths ℓ⁰_e. Energy:

    H[wiring, ℓ] = H_curv[wiring, ℓ] + 4(λ − 1) Σ_e |c_e| + α Σ_e |c_e| (ℓ_e − ℓ⁰_e) / ℓ⁰_e

- H_curv is the published curvature sum with lengths in it: Ollivier's curvature is defined on weighted graphs
  (transport cost over shortest-path distances, the mass at a point spread over its neighbours), and at ℓ = ℓ⁰ on the
  flat lattice it is the toy's energy exactly, 16(3N − S) + 4X. This is the part Regge varies.
- The second term is the curling cost as now.
- The third is the only new ingredient: a relic's curl couples to the length of its own links with strength α (decision
  3: "set by its energy, its curve"). One constant. α = 0 is the toy as it stands.

**Regge's step (decision 7).** With the wiring held, the lengths relax to a stationary point of H in ℓ. Whether that
stationary point has a halo round a relic, and of what shape, is a property of H_curv's second variation at the flat
lattice, which is the exact question of section 4. **The smoothing control:** replace H_curv's dependence on ℓ by
½ k Σ_{e~f} (ℓ_e − ℓ_f)² over neighbouring links (a rule put in by hand); its stationary point is Poisson's equation on
links sourced by α|c_e|, Newton's shape by O61's calculation moved onto links. Same relics, same observable, known answer:
it checks the apparatus, not the hypothesis.

**Response (decision 5).** With the lengths held, a loop's moves are accepted as now, with the change in the summed
length of the loop's links added to ΔH at weight 1 (a loop shifts toward a shorter path). *Ours:* a cleaner form, and
the one that matches Update 40's clock reading, is to offer a point's moves at a rate set by the lengths of its links;
either is a knob and the first is simpler. Hers to choose.

## 4. The exact question that decides whether reach emerges (step 1, no run)

Compute, on a flat 6 × 6 × 6 (then 8 × 8 × 8) six-link torus with its diagonals at Regge's lengths, the matrix of
second derivatives of H_curv with respect to the lengths at ℓ = ℓ⁰ (Ollivier's transport cost per edge is a small linear
programme, so each entry is exact), and its spectrum and Green's function.

- **If the matrix has zero modes with a continuous band above them (gapless)**, a point source gives a halo falling
  as a power of distance, and reach emerges from the curvature itself with no rule put in; the continuum relative is
  that the second variation of the Einstein–Hilbert action about flat space is the massless graviton's kinetic term
  (*general knowledge, to verify*). Then compare the halo's shape with O61's 1/r.
- **If the matrix is gapped**, every halo falls off exponentially and Regge's route gives no gravity in this family;
  the brief falls back to the control arm as the model, and says so.
- **If H_curv does not depend on the lengths at all at the flat point** (possible: Ollivier's curvature on a lattice can
  be locally constant in the lengths), the question is moot and the answer is the same as gapped.

A number to write before computing: *ours*, the lowest non-zero eigenvalue at L = 6 and 8, with the claim that it falls
toward zero with L if gapless and stays fixed if gapped; L = 10 held out (rule 14).

**Step 1 computed, 2026-10-28, 14:37 UTC** (`sandbox/regge_step1_stiffness.py`, `_b.py`; a look, exact). The prediction written in the script's header (linear, no stationary point) failed. At the flat point the curvature is **quadratic** in the link lengths: one link at 1 + δ costs 12 δ²/(1 + δ), the same at L = 6 and 8; two links interact by −4 δ²/(1 + δ) at exactly the six parallel offsets one step away and by zero at every other offset and for every perpendicular pair; a uniform scaling of every length costs exactly zero. So the stiffness is **K = 4 (6I − A) on each axis family of links separately**, A the cubic adjacency of link positions: the lattice Laplacian, **gapless**, with uniform scaling as its zero mode and lowest non-zero eigenvalue 8(1 − cos 2π/L), falling as 1/L². The halo of a source on one family is the lattice Green's function, the point-scalar row of `sandbox/gravity_carrier_isotropy.py`: 1/r at long range, isotropic to 0.993 at r = 12. **Reach emerges from the toy's own curvature with nothing put in.** Two things it also says: the three families do not talk, so a relic whose curl sits on x-links makes a halo of x-lengths only (the brief's standing direction problem returns here in a new form); and the sign of the halo follows the sign of α, which is a knob. Held out under rule 14, written before it ran: the same two numbers at L = 10; **read 14:44 UTC: as predicted** (0.028571 and −0.009524 to every printed digit, perpendicular 0). Step 2 can be written.

## 5. The first test (step 2, pre-registered after step 1 reads)

Two relics (O56's curled line of four, or whatever step 1 of `gravity_brief.md` finds to be a dip) on a flat six-link
torus, named points, sealed, lengths relaxed from their curl by the model (Regge) and by the control (smoothing), each
loop allowed to shift toward a shorter path; the observable is `gravity_brief.md`'s potential of mean force F(r).
**Her prediction: CLOSES.** Ours is written after step 1. Held-out size under rule 14.

**The sign of α, put to the author 2026-10-28, 15:09 UTC** (*ours; general knowledge, to verify*). Two measured facts fix two signs. (i) Light passing near mass arrives later (the Shapiro delay, measured to 2 × 10⁻⁵ by Cassini), and the toy's travel time is the summed length along the shortest route, so the halo must *lengthen* links near matter: α < 0 on the axis links. A diagonal taken as a shortcut only near matter would make light *faster* there, the wrong sign, unless it is counted at her link weight (4 ticks for √6), which is slower than its Euclidean length (4 ticks against 2.45) and so a delay. (ii) Matter attracts. In Einstein's gravity a free body follows the path of *longest* proper time, not shortest length; both facts come from one field with one sign. The confirmed response rule, "a loop shifts toward a shorter path", is the opposite convention, so with α < 0 it gives *repulsion*. CLOSES therefore needs (α > 0, shorter) or (α < 0, longer); only the second also delays light. **Her decision of the same message: step 2 runs with the families uncoupled and reports the direction dependence first.** T84 (draft) runs both signs of α under the confirmed rule and reads the light delay through the halo exactly, so that both facts are scored whichever she chooses.

## 6. What this cannot do, said plainly

- It cannot hide the lattice's directions; the 8 % anisotropy of Regge's lengths is in the carrier from the start.
- It cannot give time dilation: the toy has no time. The nearest it offers is Update 40's clock reading of the response
  rule, which is a candidate, not a result.
- It cannot say what α is; α is scanned and published, and a value that reproduces a measured number is not a result
  until rule 13's checks are done.

## 7. Published relatives (none read in full; read status to be recorded in REFERENCES.bib before any is cited)

Regge (1961), gravity on a lattice of edge lengths; Hamber's reviews of simplicial quantum gravity; Ollivier (2009),
Ricci curvature of Markov chains on metric spaces, which defines the curvature on weighted graphs; Lin, Lu and Yau
(2011) for the graph form; Kaluza–Klein for a length and a phase on one object. The light carrier already built
(`graphity.u1`, Update 96) is Wilson's.
