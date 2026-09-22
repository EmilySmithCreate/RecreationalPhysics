# Plan: getting known physics out of it (claim 2)

Written 2026-09-22 at the author's request ("can you start planning some work along this line?").
This is a plan, not a pre-registration: every run below gets its own section in `PREREGISTRATION.md`
before it starts (rule 4), and anything that adds a knob to the energy needs a dated VISION decision
first (S1). Physics reasoning here is *ours, unverified* unless a source is named.

## What "known physics comes back out" can honestly mean here

Claim 2 is the highest bar in VISION and no approach to emergent spacetime has cleared it. This model
is a two-dimensional network, simulated classically, with no time. General relativity in 3+1
dimensions, Lorentz symmetry and quantum mechanics are out of reach as such (VISION, "The target").
What *is* reachable are the fingerprints any candidate must show before those questions arise, and a
few specific signatures the published programme [T25] claims the model already has. So the plan is a
ladder: each rung is a measurement the model could fail, and the rungs are ordered by how directly
they test "known physics" and how cheap they are.

## Rung 1 — Is what the tube opens into really space? (VISION step 4, "the spot")

Measured on the sheets the tube produces (T9/T10 sealed end states, T7 decays) and on the tempering
equilibrium cold phase, at several sizes:

- **Volume-growth dimension**: vertices within graph distance r, against r. A space of dimension D
  gives r^D. Expect 2.
- **Spectral dimension**: the return probability of a random walk after t steps, P(t) ~ t^(−D_s/2).
  Expect 2 at large t. This is the measurement several approaches use to find the dimension falling
  towards 2 at short distances [Carlip17, unread]; it is also causal dynamical triangulations' main
  observable [AJL05, unread].
- **Flatness and uniformity**: Ollivier curvature per edge (from square counts, [T25] Eq. 8), its
  mean (expect 0) and its spread across regions.
- **Locality**: a census of shortcuts — edges joining vertices that are otherwise far apart.
- **Stability**: survives mild heating (already partly in hand from the hysteresis runs).

**Reproduce first (rule 2):** [T25], text around Eq. 24 and Fig. 6, reports the dimension of the
geometric phase (close to 2) and of the random phase (infinite). Match those numbers with our own
tools before interpreting anything of ours.

*Honest expectation:* a perfect flat torus is two-dimensional by construction, so for clean sheets
this rung is a check, not a discovery. The informative part is the *defected* sheets — with
remnants, twists, or the warm disorder of a small sealed box — where the question is how much
disorder a sheet carries before it stops behaving like space.

New code needed: ball growth by breadth-first search, random-walk return probability, per-edge
curvature. All small; `dimension.py` and `connectivity.py` already have the building blocks. Each
new measurement gets a known-answer test (flat torus: D = 2; tube: 1 at large r; 4-cube: finite).

## Rung 2 — Is there a speed limit? (the seed of relativity)

[T25] argues that a bubble of disorder can move sideways at no cost but only one link per update,
so a maximum speed appears without being put in ("nobody wrote the speed of light into the rules").
Two measurements:

- **The opening front.** From existing T7 decays: the 25 %→75 % conversion takes a median of 92,
  262, 442 and 818 sweeps at tube lengths 16, 24, 36 and 48 (a first look, 2026-09-22, not a
  finding): the front covers about 0.04, 0.023, 0.020, 0.015 columns per sweep per side, *slowing*
  as the tube lengthens. Whether a front has a fixed speed, or spreads more like diffusion, needs
  the front's position recorded against time, not three snapshots.
- **A local disturbance on a flat sheet**, in sealed dynamics: how far does its influence reach
  after t sweeps? A cone with a fixed edge speed is the fingerprint.

*Caveat stated up front:* Monte Carlo sweeps are an algorithm's clock, not physical time; VISION
already says the bare ordering of time is assumed, not derived. A maximum speed that does not
depend on system size is still a real property of the rules.

## Rung 3 — Does matter curve space, and do defects attract? (the seed of gravity)

- **Energy against curvature around a defect.** [T25] Sec. VI.1: a patch of disorder costs more and
  is more sharply curved, and insisting the two be related properly yields Einstein's equations with
  a cosmological constant. Testable piece: across many defects (remnants, twists, melted patches),
  does local excess energy track local curvature, with one constant of proportionality?
- **Do defects attract?** The author's parked idea that gravity is "the opened space wanting to
  refold" (`docs/parked/extension_2026-09-22.md`, item 3(i)). T7's rare resting states already show
  that two four-point pieces together can hold 8 or 18 units instead of 28 (O13, third addendum), so
  defects *do* interact. The test is the sign and the range: energy of two defects against their
  separation, from existing T9/T10 end states first, then from controlled placements.
  *Care needed:* in two dimensions Einstein's gravity has no local degrees of freedom, so the fair
  comparison is a two-dimensional attraction law (logarithmic in Newtonian terms), not full GR.
- **What concentrated energy does to a flat sheet** (parked item 3(ii)): re-curl a patch (the
  author's black hole) or melt it ([T25]'s black hole)? This needs a *local spark* — energy
  delivered at chosen vertices — which is a protocol choice declared like the leak rate, not an
  energy knob.

## Rung 4 — Three dimensions and quantum behaviour from a two-dimensional network

The programme's boldest claim [T23, T24, T25]: a random walk on a *negatively curved* two-dimensional
network, seen from inside, looks like quantum mechanics in three dimensions. Our cold phase at
λ > 1 is flat, not negatively curved. So this rung starts with reading: where the negative curvature
comes from in [T25] (the critical point? the defects?), and whether there is a measurable handle at
our sizes. Decided after the reading; parked otherwise.

## Out of reach, and said so

Lorentz symmetry (no time), genuine quantum mechanics (classical sampling), 3+1-dimensional
general relativity (a two-dimensional model; the D = 3 model has not been run past N = 500 [T22]).

## Side track the author raised: could the leftover be a real share of the universe? The multi-seed test

The leftover is one small scrap per conversion however big the space (T10), so it cannot be a share
of anything. But every tube so far opened from **one seed**: in the T10 cold boxes, every box caught mid-conversion
(78 of 80; two converted between measurements) had a single sheet patch throughout (a check on
existing files, 2026-09-22). If a real
conversion started from many seeds and **each seed left a scrap**, the scraps would follow the seed
density and could be a genuine share — a sprinkle of heavy, stable, gravitating defects, which is
closer to dark matter than to dark energy (below). Two ways to test:

- **Plant k seeds** on a long tube in a cold sealed box (k = 1, 2, 4, 8) with the local spark of
  rung 3, and count leftovers. Cheap, controlled, and it shares code with rung 3.
- **Let seeds form naturally** in tubes long enough that a second seed appears before the first
  front finishes. From the front times above and waits of 700–1400 sweeps, that needs tubes of
  roughly 100 or more columns (N ≳ 400): slow, but no new protocol.

Predictions to pre-register before either runs: leftovers per box grow in proportion to k (one per
seed, or one per place where two fronts meet), against the alternative that it stays one whatever
k (so the leftover is not the front's doing). T11 already found that with one seed the leftover is
neither at the seed nor at the seam, so this could come out either way.

**Dark energy, for the record** (general knowledge, not read): dark energy is the same everywhere,
does not clump under gravity, and keeps the same amount per unit of volume as space expands, so its
total grows with space. A fixed number of scraps does the opposite — it thins out as space grows,
as ordinary matter does. And this model has no expansion (the number of points is fixed) and no
vacuum-energy floor (the flat sheet holds exactly zero at λ > 1). So dark energy stays out of reach,
as the parked extension already says; the multi-seed test bears on a dark-matter-like reading only.

## Order, and rough cost

1. **Read** (one session): [T25] on the speed limit, Sec. VI.1, and the dimension measurements; the
   method sections of [Carlip17] and [AJL05]. Overlaps TASKS T12.
2. **Rung 1 tools**, known-answer tests, then reproduce [T25]'s dimension numbers as a gate.
3. **Defect interaction from existing files** (rung 3, no new runs): an exploratory look, then a
   pre-registration.
4. **Local spark code**, then the **planted-seed test** and the **spark-on-a-sheet test**, each
   pre-registered.
5. **Front speed** (rung 2), recording front position against time.
6. **Rung 4**: decide after the reading.

## What success on this ladder would and would not mean

Passing rungs 1 to 3 would say that what the tube opens into behaves like a flat two-dimensional
space with a speed limit, in which defects curve the geometry and attract one another. Those are the
first fingerprints of relativity and gravity, and [T25] claims them for this model on paper; we
would be measuring them. It would not be claim 2: that needs three large dimensions, time and
quantum behaviour, which this model does not contain.

## What the runs so far do and do not say about the two known hurdles (added 2026-09-22)

The author asked whether anything has been learned about the two hurdles on the public page: old
inflation's bubbles never joining up, and the pattern of ripples in the sky. Honest answers, in order.

**The bubbles-never-join problem (graceful exit).** Not addressed, and it cannot be in this model,
which has no expansion at all: the failure mode needs the old phase to be a space that grows faster
than the bubbles do, and here nothing grows. What the runs *do* supply are two of the inputs such a
calculation needs, both exact and neither fitted: the nucleation rate, 3·exp(−12/g) per sweep with
the 12 counted from the energy (Q13), and the driving force on a front, a fixed 4(λ − 1) per point
swept, the same at every size (O23). Having the inputs is not having the answer. VISION already
records the one escape route, untouched by any run: the failure needs the old phase to be an
expanding space, and X need not be one.

**The ripple spectrum.** Nothing, and nothing is reachable: no time, no expansion, no quantum
fluctuations. *One indirect reading, ours, unverified:* the ripples in the standard account come from
a field that varies from place to place, and T10 found the leftover of a conversion is **one** small
remnant however large the system. A single defect cannot carry a spatial pattern. If anything in this
picture is to play that role it has to come from *many* seeds, each leaving its own scrap, which is
exactly what TASKS T14 tests and what has never been run.

**What X is made of.** In the model, answered completely and it is worth separating from the real
question: the stand-in for X is a specific arrangement (the tube), its dimensions are a count at each
point, it is metastable, its gap above space is exact, and its activation cost is exactly 12 units at
every size. Today's Q18 adds that **space is the floor** — nothing at all lies below it — so X must
be a higher arrangement and cannot be confused with a lower one. About what the real X would be made
of, nothing.

**What sets the size of the gap.** In the model this is now exact (O23): the gap is 4(λ − 1) per
point, measured at N = 36 to 600 and at three values of λ. So the gap is not free — it is set by one
knob, and its size is the distance of that knob from λ = 1, the point where curled and flat cost the
same. *Ours, unverified, and worth stating because it is a real consequence:* a small gap in the real
thing would mean sitting very close to that tie, which is a near-critical condition and a
fine-tuning question of its own rather than an answer to one.
