# Draft note to the model's authors (not sent)

Drafted 2026-09-22 for Emily to send if she chooses. VISION S5 and TASKS "Before anything is shown to
anyone" list what it should contain. Addresses are deliberately not filled in here. Before sending:
make sure the repository is public, and check each number against `ASSUMPTIONS.md` once more.

---

**To:** C. Trugenberger, C. Kelly, F. Biancalana
**Subject:** Reproducing your combinatorial quantum gravity model: two questions (Fig. 3, and order at degree 4)

Dear Dr Trugenberger, Dr Kelly and Dr Biancalana,

I'm a software engineer who has spent the past few weeks reproducing your 2D combinatorial quantum
gravity model as a hobby project, with the code and pre-registered analyses in the open:
https://github.com/EmilySmithCreate/RecreationalPhysics. I would be grateful for your view on two
questions, and thought two small observations might interest you.

**Questions**

1. *Fig. 3 of the 2025 review (arXiv:2512.17676).* At N = 160 our code reproduces Fig. 8a of the
   2019 paper to within 0.005, and matches Fig. 3 at both ends (g ≥ 6.3, and g ≈ 2), but not in
   between: there Fig. 3's points drop almost vertically while ours — with the hard cap and with
   the soft penalty, in equilibrium — rise smoothly. The two published figures also differ from
   each other at g = 5 (0.62 against 0.99). Could you tell me which variant, and roughly what run
   length, Fig. 3 used?
2. *Order at degree 4.* The 2019 paper describes a finite-size analysis as out of reach, and
   Dr Kelly's thesis abstract says higher-degree results appear first-order while staying nearly
   geometric. Is there a degree-4 finite-size analysis I have missed? Ours, with the full rule at
   N = 36 to 100, shows a single hump, with any latent heat below 1.3 per vertex and shrinking.

**Two observations**

- A 14-vertex "baby universe" (the incidence graph of the 7-point biplane) satisfies every
  constraint and ties with the 4-cube in energy at every λ.
- For λ > 1, a torus with one side curled to length 4 (a "tube") sits 4(λ − 1) per vertex above the
  flat sheet, is long-lived, and decays by a seed and a single front, releasing exactly that energy.
  Pre-registered tests at 64 to 192 vertices find the change sharp, in two steps (via a small
  four-vertex remnant). I'd be curious whether this is known or expected.

All code and documents were drafted with an AI assistant (Claude). I have checked what I could
against your papers and against exact enumeration of every configuration up to 18 vertices, but no
physicist has reviewed any of it. Even a one-line answer to either question would help a great deal.

With thanks,
Emily Smith

---

## Optional second note, to A. Gorsky and O. Valba (2021)

One question only: in your penalty-off simulations the cold phase is hypercubes plus one closed
"ribbon" holding the remaining vertices, and we see the same at N = 36, 100 and 120. Have you looked
at whether the ribbon survives when the saturating (penalty) term is switched on, where the cold
phase is a flat sheet rather than knots?
