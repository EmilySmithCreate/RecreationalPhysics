# Twist and curl: the rules as equalities and inequalities (draft, 27 October 2026)

*Written at the owner's request of 19:39 UTC ("I want us to write the math of this relationship in a simple
equality/inequalities"), from her answers of 16:42 to 19:39 UTC (verbatim in `sandbox/NOTEBOOK.md`; VISION Updates 133
and 134). Each line says whose it is: **hers** (her rule, her words put in order), **exact** (arithmetic), **ours** (our
translation or reasoning, unverified), **open** (a choice still hers). Nothing here has been run. A rule is put in, so
whatever it says is not a result; the results are what follows from the rules together.*

## The two quantities

- **Curl** on a link e: c_e = S_e − 4 (six links; flat space has 4 squares on every link). c_e > 0 is curl, c_e < 0 is
  anticurl. *Exact:* the hard-core rule bounds it, −4 ≤ c_e ≤ +1, so the toy's curl is lopsided (O164; Update 134).
- **Twist** on a square p: τ_p, the light field's phase round the square, measured in turns, −½ < τ_p ≤ ½ (`graphity.u1`).
  *Exact:* +τ and −τ cost the same, so twist is a true mirror pair.

## The rules

1. **Balance** (hers, 25 October; soft form 27 October): Σ_e c_e = 4(S − 3N), held near zero by the penalty
   (μ₀/N)(S − 3N)².
2. **Prices** (hers, A2): a unit of curl costs 4(λ − 1), a unit of anticurl 4λ; one λ everywhere.
   *Exact:* this is λ times the toy's energy at λ′ = 2 − 1/λ (O164 addendum).
3. **Twist makes curling dearer** (hers, T1; the form ours, open): each unit of curl on a link costs κ·T_e more, with
   T_e = Σ over the link's squares of (1 − cos 2πτ_p): 0 with no twist, 2 at a half turn, the same for ±τ.
   **Open:** does κ act on curl only, or on anticurl too?
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

1. Rule 3: κ on curl only, or on anticurl too.
2. Rule 7: what the spin sum is.
3. Question 5: how the twist moves when a link is rewired (fresh, carried, averaged out, drawn to suit its neighbours).
4. Rule 4 as written makes every move conserve twist and balance curl at once; whether the toy's single switch can ever
   satisfy it is an exact count to run first (ours: it may need two switches at once, as the hard rule did).
5. Where the twist lives. Rules 3 to 5 put it on squares (the light field's phase, built, a true mirror pair); rule 6
   follows Update 97, which put thirds on cube body diagonals and halves on face diagonals. A face diagonal crosses one
   square and a body diagonal crosses a cube, so the two can be joined (a square's twist read along its diagonal; a
   cube's from its six faces), but how is a choice: hers.
