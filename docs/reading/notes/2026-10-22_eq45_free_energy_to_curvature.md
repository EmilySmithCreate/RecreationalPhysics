# Reading note: Trugenberger's Eq. (45), free energy to curvature

**Date:** 22 October 2026. **Who read:** an assistant agent, from the arXiv texts (searched, not summarized).
Everything below is a quotation or is marked ours.

**What was searched.** `https://arxiv.org/html/2512.17676v2` ([T25]; HTML to text, Sec. VI.1 at characters 66,800
to 70,800 of 98,599); `https://arxiv.org/pdf/2211.01002` ([T23] v2) and `https://arxiv.org/pdf/2112.03778` ([T22]),
both without HTML versions, text through pypdf. Terms: "de Sitter", "Lorentzian", "Wick", "continuation", "signature",
"changes sign", "Planck length", "ξ", "Joule", "seconds", "n(g)", "constitutive", "qualitative", "free energy",
"allotrop". Broken hyphenation was repaired in the quotes, nothing else.

## 1. Eq. (45) verbatim, and how it is reached

[T25] Sec. VI.1, as the HTML renders it (the division by ℓ is read from the fraction layout; *ours:* with G_N/c⁴ in
metres per joule, both sides are then dimensionless):

> −(⟨K⟩ − 4Λ₂) ℓ² = (κ/ℓ) F,  κ = n(g) 8πG_N / c⁴,  (45)
> in units where the free energy F is measured in Joule with respect to the surrounding geometric matrix with
> curvature 4Λ₂. G_N is Newton's gravitational constant and n(g) is a numerical factor depending on the original
> coupling g.

The symbols, as far as the text defines them. **ℓ** (Sec. IV.2): "endow the links of the graph with a uniform
length scale ℓ". **K** (Sec. IV.2): the curvature of the tessellated surface, "K = −1/R²", with "K(g) in units of
1/ℓ²" fixed by "the graph minimizing the free energy at every coupling g". **⟨K⟩**: its ensemble average over the
bubble. **Λ₂**: only the clause "the surrounding geometric matrix with curvature 4Λ₂"; Λ₃ likewise, "the bulk
curvature 4Λ₃" (Eq. 46). **n(g)**: nothing beyond the sentence above. **Joule**: no conversion anywhere.

It is posited, not derived. The whole motivation is one paragraph:

> Let us now consider a random phase bubble embedded in a constant curvature graph at low, but finite coupling. [...]
> These energy and entropy effects conspire to generate the higher free energy of the random phase bubble with respect
> to the geometric surrounding. But also, each vertex on the boundary has a lower curvature since less squares and
> longer cycles imply a larger excess angle at the vertex, so that the curvature is more negative than in the
> geometric phase [...] Since the number of boundary vertices depends on the bubble size, this lower negative
> curvature is associated with the higher free energy, but this relation is statistical in nature since many
> microstates of slightly different curvature, due to long cycles entropy, characterize the ensemble with a given free
> energy. The ensemble equation is thus [Eq. (45)]

So: curvature deficit and free-energy excess both live on the boundary vertices and scale with their number, and a
linear relation is written down. "Statistical in nature" is the last clause: at a given F many microstates of slightly
different curvature contribute, so only ⟨K⟩ is tied to F. No constant is computed; n(g) absorbs it.

## 2. "The Lorentzian picture"

In VI.1 it is one sentence: "In the Lorentzian picture the curvature changes sign." The basis is not a Wick rotation
of the action but an asymptotic equivalence of trajectories: on a negatively curved surface a defect's Brownian motion
becomes ballistic in the radial coordinate, "z_t = vt" (Eq. 31), which ties the universal time to that coordinate.
Then ([T25] Sec. V.1, after Eq. 33):

> Up to an exponentially small correction, these trajectories are the same as the comoving geodesics on a 2D
> Lorentzian manifold of positive curvature K = +J² [...] This is 2D de Sitter space-time [...] One can use both
> descriptions; however, with positive curvature, the universal time t becomes the coordinate time of a Lorentzian
> manifold. This is a form of Wick equivalence arising between the two signs of curvature.

[T22], abstract: "With this asymptotic Lorentzian picture, the original negative curvature of the Riemannian manifold
turns into a positive cosmological constant. The Lorentzian picture, however, is valid only asymptotically and cannot
be extrapolated back in coordinate time." Its Eqs. (33) to (34): the same hyperboloid, "embedded in Minkowski space
with metric (+1, +1, −1), however [...] becomes a Lorentzian manifold of constant positive curvature H²". [T23]:
"asymptotically, the sign of the curvature is ambiguous: 'free fall' in constant positive curvature becomes
equivalent to Brownian motion in constant negative curvature", and "The absolute value of the negative curvature becomes the cosmological constant [33]." "Wick" occurs
once in [T23], for the sub-leading random process only ("this amounts to the familiar Wick rotation").
"Continuation": not found in any of the three texts.

## 3. What fixes ℓ, n(g) and the joule

**ℓ** ([T25] Sec. IV.2): "To make contact with manifolds, we shall henceforth endow the links of the graph with a
uniform length scale ℓ and identify the correlation length with the Planck length, ξ(g)ℓ = ℓ_P(g). With this
definition, the Planck length vanishes at g = 0 whereas at g = g_cr it equals the graph diameter." ξ(g) is the decay
length of the square-square correlation (Eq. 23), in graph steps. So ℓ needs a measured ξ(g) and an outside ℓ_P.
[T22] does the same with a running coupling, "(N/N_f)^{1/D} ℓ = ℓ_P(f)", and sets "ℓ_P^{D−2}(f)/ℏ = G_N(f)".
**n(g)**: not found beyond section 1. **The joule**: [T25] Sec. V names the units: "the length ℓ and the inverse
number of elementary moves per unit time, which are the two sole fundamental units in the model." Eq. (44) uses "the
previously introduced time t̃ measured in seconds"; that introduction is not in the review but in [T23]: "t = D t̃ is actually a length², whereas t̃ is measured in 'seconds'
[...] one length scale and a fundamental speed c = DH". No energy unit is defined in any of the three papers.
**Numerical values: none, confirmed.** The only mass formula is [T23] Eq. (34), "m = ℏH/2c", left in H and c.

## 4. Which objects

Random-phase bubbles ([T25] VI.1): "Since both the free energy and the curvature of these random phase defects are
higher than the surrounding manifold on which they live it is natural to identify them with matter particles". The
allotropes (VI.3):

> we can have metastable domains characterized by a higher number □_dom than the prevailing configuration □ and
> therefore having a larger free energy than the space around them at a given g. Because of this higher free energy
> they have also a higher curvature (in the Lorentzian picture) and interact gravitationally. But they are neither
> empty space nor ordinary matter.

So the review does give curvature to an ordered region with *more squares per vertex* than its surroundings, through
its higher free energy. Two things it does not reconcile (ours): the Fig. 9 caption shows the opposite case,
"vertices surrounded by two squares within an hyperbolic tessellation with all vertices surrounded by three squares
[...] with a higher absolute curvature and free energy"; and Sec. IV.2 has |K| *fall* as squares per vertex rise
("the absolute value of the curvature of the tessellated surface typically decreases, until it vanishes for four
squares around each vertex"). Squares per *edge*, surplus squares, (S_e − 2)₊: not found in Sec. VI. The rule is
free energy at the given g, not the square count.

## 5. Eqs. (46), (47) and the caveat

> (⟨R(x)⟩ − 4Λ₃) = κ f(x),  (46)

"where f is the free energy density, measured here with respect to the bulk curvature 4Λ₃", after "dividing both sides
by ℓ³" for a point-like bubble at rest in the comoving frame. Then:

> In a generic frame, the energy-momentum tensor of a dust of such particles moving along geodesics must be defined by
> a local (maximum two derivatives), symmetric geometric tensor which is covariantly conserved and has eq. (46) as its
> trace. The unique such geometric tensor is the Einstein tensor augmented by a cosmological constant term [95], which
> gives ⟨R_μν⟩ − ½⟨R⟩ g_μν + Λ₃ g_μν = κ T_μν, (47) These are Einstein's equations of general relativity (with a
> cosmological term), with the difference that T_μν must be interpreted as a (density) thermodynamic potential and the
> equations hold as statistical ensemble averages. In this model these are not dynamical equations but, rather,
> macroscopic constitutive equations of matter as defined by the microscopic network degrees of freedom.

[95] is Lovelock, J. Math. Phys. 12, 498 (1971). The rigour sentence the record quotes is in the abstract: "The network
model seems to naturally encode several of the large-distance features of cosmology, albeit still at a qualitative
level." Sec. V adds, of the defect motion: "it is an open question, beyond the scope of this review, how the
collective translation can occur in terms of elementary edge moves."

## 6. Ours, unverified: a number without ℓ or a joule

For two objects in the same background at the same g, Eq. (45) divides to F₁/F₂ = (⟨K⟩₁ − 4Λ₂)/(⟨K⟩₂ − 4Λ₂): every
conversion constant cancels, and through Eq. (47) free energies stand in the ratio of masses. That needs (i) F, not
H, for each object (long-cycle entropy is in F; at g → 0 F tends to the energy, which our exact dips give); (ii) an
independent reading of ⟨K⟩ for the same objects by the Sec. IV.2 geometrization, so both sides of Eq. (45) are
checked on the toy instead of assumed; (iii) an identification of two toy objects with two physical things of measured
mass ratio, which no paper supplies; without it the knots of O107 (energies 14, 20 to 30, 8) give ratios, not
predictions. Rule 13 applies before any comparison.

## What this does not settle

Whether Eq. (45)'s linear form or sign holds for any object; whether a region with surplus squares has higher or lower
|K| (the review's two statements point opposite ways); the value of n(g); and whether the curling cost at λ ≠ 1, absent
from the review's energy, changes what F means in Eq. (45). The papers were searched for these six questions, not
read in full for this note.
