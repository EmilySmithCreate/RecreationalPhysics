# The U(1) field on the rewiring graph (design brief, 24 October 2026)

*For the owner. Nothing is built or run from it until she has answered its decisions (VISION S1; Update 100, her
"yes" to writing it). Kinds of statement: exact, published (with how much was read), ours, hers. At λ ≠ 1 the toy is
our family around the published model, never combinatorial quantum gravity.*

## Current definitions (read first; rule 20)

- **The field (built, gated):** a phase on every link of the toy's graph, oriented from kind 0 to kind 1; every 4-cycle
  is a square; energy κ Σ (1 − cos φ) over squares, or in Monte Carlo the weight exp(β Σ cos φ); a winding move is
  needed at large β (ASSUMPTIONS Q29; Gate U1″ passed).
- **The graph (published model and our family):** the toy's switch moves at coupling g, energy H = 16(DN − S) + 4λX in
  the toy's units (D = 2 for four links, 3 for six).
- **Proposed here, not decided:** the joint weight of a graph G and a field θ is exp(−H(G)/g + β Σ_p cos φ_p(G, θ)).

## Why this is the route (O152)

A fresh red-team reader judged nothing on particles publishable today and named one route: the field on the
dynamical graph, with a pre-registered effect on a quantity the toy already measures. The exact first look gives that
effect a sign and a size before any run.

## What is exact already (`sandbox/u1_graph_free_energy.py`; ours)

1. **Integrating out the field rewards squares.** At fixed wiring, Z_U1(G) = Σ over integer fluxes n with Bᵀn = 0 of
   Π_p I_{n_p}(β) (the character expansion, as in Gate U1). Its leading term is I₀(β)^P, P the number of squares, so the
   field adds ln I₀(β) per square to the log weight: at coupling g, an energy −g ln I₀(β) per square.
2. **The tube has more squares than the sheet.** The 4 × L tube carries a quarter of a square per point more (its rings
   round the curl): at N = 64, 80 against 64. So the field favours the curled state. At leading order this is a shift
   of the curling cost, λ_eff − 1 = (λ − 1) − (g/16) ln I₀(β) (ours; from the tube's extra 4(λ − 1) per point and its
   extra quarter square per point). At λ = 1.25, g = 1.5, β = 2 that is about 1.17.
3. **The next terms are not small for the tube.** The null space of Bᵀ (closed surfaces made of squares) is 1 for the
   sheet and 16 for the 4 × 16 tube (36 for 4 × 36), so the surface terms of the expansion matter for curled states.
4. **A flat 6 × L torus and the square sheet have equal square counts** (144 each at N = 144), so the field does not
   choose between flat tori at leading order; it only separates curled from flat.

## Decisions for the owner (S1)

1. **How a phase rides a switch.** A switch removes links (u1, v1), (u2, v2) and makes (u1, v2), (u2, v1). Options:
   (a) the new links get fresh phases drawn uniformly, the old ones are forgotten (simplest; detailed balance holds with
   Metropolis on the joint weight, since the proposal is symmetric on the product space); (b) the new phases are chosen
   to keep the holonomy round the switched square, as a field carried with the wiring (closer to "the field rides on
   the links"; needs its own detailed-balance argument); (c) the field is integrated out exactly and only its weight
   Z_U1(G) enters the switch acceptance (no phases at all in the chain; exact only where Z_U1 can be computed).
   *Ours:* (c) for the first test, because it gives the cleanest prediction; (a) for runs where the field itself is
   looked at.
2. **The field's coupling β, and whether it is tied to g.** A fixed β (the field's own constant), or β = κ/g with one
   κ (the field at the same temperature as the graph). *Ours:* β = κ/g, since one temperature for everything is what a
   bath means; κ scanned and every value published.
3. **The first observable.** (a) The tube's waiting time against the sheet at λ = 1.25, with and without the field
   (the known Arrhenius law, O13 and Update 9, gives a baseline with no fitted number); (b) where the metastable window
   closes in λ (T8's map); (c) the T78 and T79 surcharge on curl in the published model's warm graphs at λ = 1.
   *Ours:* (a), since the leading-order prediction is a number before anything runs.
4. **Four links or six.** *Ours:* four first (the tube and sheet are understood exactly there; Update 95 keeps six as
   the three-dimensional story).
5. **Her predictions** for whichever test she chooses, recorded before it runs, with a held-out size (rule 14).

## Exact steps before any run

1. Z_U1(G) exactly for the sheet and the tube at N = 64 and 144, including the surface terms (a sum over the null
   space of Bᵀ, truncated where the Bessel ratios fall below 10⁻¹²), against a Monte Carlo of the field at fixed wiring
   with the gated sampler.
2. The effective curling cost from step 1, as a function of g and β, written down as the registered prediction.
3. A prior-work note (rule 15) on matter and gauge fields coupled to dynamical graphs and triangulations (Candido et al.
   2010.15714 on CDT is the nearest found on 24 October; `docs/reading/notes/2026-10-24_prior_work_u1_curl_mass.md`).
4. For option 1 (a) or (b): a kernel with the rule-6 tests (networkx brute force, incremental against full
   recomputation, constraint preservation, same seed).

## What would kill it

If the exact Z_U1 ratio between tube and sheet does not depend on β in the range where the field is weakly coupled, or
if the measured waiting times do not move by the registered amount at the held-out size, the field's effect on the
tube is not what the leading order says, and the route is reconsidered before anything is written up.
