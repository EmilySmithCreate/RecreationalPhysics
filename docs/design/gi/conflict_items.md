# Conflict items (family C of the framework eval), from the record

Written 2026-10-30 (Fable). The C family gives a model "a framework plus one observation it really contradicts" and
scores whether it flags the conflict in the second channel ("conflicts with observation") instead of quietly
rewriting the framework or ignoring the observation. The eight below are real: each is a registered prediction of
the owner's or ours that failed in the toy, written as the framework statement, the observation, and the faithful
response. The observation is **measured** or **exact** as marked; the framework statement is **hers** or **ours** as
marked. Rule 11's form ("previous claim → failed because → replacement → new test") is the record's; here only the
first two steps are given, because the third is hers.

| # | Framework statement | Observation that contradicts it | Faithful response (what a model should write) |
|---|---|---|---|
| 1 | One activation opens all three curled directions and releases the whole burp (hers, Update 22) | Untied, a push the size of the cheapest move opens one direction, or one cube, and stops (measured: T30 NEVER OPENS, O64; T48 ADVANCES ONLY, O91; T53 ADVANCES ONLY at every length and both λ, O105) | Flag: the framework's cascade needs something the energy does not supply; under the single-move rule the second direction's wall is not paid by the first release in these runs. Do not rewrite "one push opens all" as "one push opens one". |
| 2 | The barrier to opening a direction is the cheapest single move (ours, Update 9 in 2D; carried to 3D) | In 2D it is (Arrhenius 0.88 ± 0.06 over twelve conditions; the 320-run spark threshold). In 3D it is not: the states between patches reach 45 against a fitted 27 (O118 correction); no clean single-point opening of the untied slab below a saddle of 64 (T69, O135) | Flag: the single-move rule holds at two directions and is refuted at three; the three-direction barrier is not known. |
| 3 | Under the tie "all at the last", a warm bath opens the slab into one flat space (hers, Update 47; T56) | STAYS in every cell (measured, T56, O115) | Flag: the tie that makes the climb small did not make the bath climb it. |
| 4 | Too much concentrated energy curls a macro direction of flat space (hers, Update 51; T57) | MELTS or HEALS at every energy, tied and untied; nothing curls (measured, O114; also T34, T66) | Flag: in this family energy put into flat space never folds it; a fold needs a mechanism not in the energy (the carrier of Update 40 is a decision, not built). |
| 5 | The hard rule (S held at 3N) lets a clean X open into space (hers, Update 128 "proceed") | Out of flat six-link space no single switch and no pair within two links keeps the count (exact, Update 128 as corrected by O159); zero at three switches within one link (exact look, 26 October); four switches open again after the audit (O163) | Flag: as stated, the rule freezes clean space; what moves is damaged space. State Q1's options; do not soften the rule silently. |
| 6 | The leftover of an opening is a seam between patches that opened from different seeds (hers, T55 SEAM) | Every piece of two and of eight is a knot of fixed energy, a dip, with no link joining distant places (exact, O107) | Flag: KNOT, not SEAM; the leftover's number is set at the opening, not by the cooling. |
| 7 | Superposition is the set of undetectably different versions of a fixed arrangement, read by a measurement (hers, Update 17) | A renaming of a fixed arrangement is a complete instruction set, so GHZ is classical and CHSH gives S ≤ 2 for any arrangement (exact argument, O29) | Flag: counting versions of one arrangement cannot violate Bell; what survives is the object-level counting and the interference rung, which needs a dynamical rule. |
| 8 | A particle is an allowed vibration of a small closed loop of the substrate (hers, Update 17) | In six states of seven no mode of the whole arrangement keeps more than a quarter of its weight on the loop; the loop's frequencies dissolve into the sheet's (exact, O30) | Flag: the loop of four is not a resonator inside a sheet; where anything resonates it is the cap. |

## Two items that are *not* conflicts, kept as controls

A C batch needs matched cases where the observation does **not** contradict the framework, so that a model that
flags everything is caught. From the record:

| # | Framework statement | Observation | Right response |
|---|---|---|---|
| C1 | The activation to start the tube's opening does not grow with size (hers, S2′ (iv)) | 12 units at every N from 48 to 192, 320 runs (measured, Update 9) | No conflict: as predicted. |
| C2 | The fed slab's split fires at 2a/r plus a short wait, the same at every size (hers, T71) | HOLDS at the held-out L = 16, 152 of 152 (measured, O160) | No conflict: as predicted at the held-out size. |

## How the items are used

For the eval, each item is one case: prompt = the framework statement (as the framework; not attributed) plus the
observation (as data); hidden = the label `conflict` or `no_conflict` and, for the blind judge, the sentence that
counts as a faithful flag. For the fine-tune's DPO stage, the "faithful response" column is the chosen answer and a
quiet rewrite of the framework ("so the framework really says one push opens one direction") is the rejected one.
