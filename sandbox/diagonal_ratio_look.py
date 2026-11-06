"""Sandbox look (kill but not crown), 4 November 2026: the static ratios of the cubic lattice's segments per unit cube, by
count and by count times length, for the owner's "proportions defined by the static relationship of cube diagonals to
face diagonal". Exact counting; rule 13: a number near a target is not a result, and with eight numbers some ratio lands
near any target. Expectation first: no ratio here is 5.36 or a billion to one; the matter : antimatter pairing from
photons is 1 : 1 by the state's own construction (one diagonal of each kind per square), so any surplus must come from
the stores (her Klein stores) and not from these ratios."""
from itertools import product, combinations
from math import sqrt
kinds = {"edge": 1, "face diagonal": 2, "body diagonal": 3, "long diagonal": 6}
count, weight = {}, {}
for name, s in kinds.items():
    nb = [v for v in product(range(-2, 3), repeat=3) if sum(x * x for x in v) == s]
    count[name] = len(nb) // 2
    weight[name] = count[name] * sqrt(s)
    print(f"{name:14s} length sqrt({s}) = {sqrt(s):.3f}  per cube {count[name]:3d}  count x length {weight[name]:.3f}")
print("ratios a/b: by count, by count x length, by length alone")
for a, b in combinations(kinds, 2):
    print(f"  {a} / {b}: {count[a]/count[b]:.3f}  {weight[a]/weight[b]:.3f}  {sqrt(kinds[a]/kinds[b]):.3f}")
    print(f"  {b} / {a}: {count[b]/count[a]:.3f}  {weight[b]/weight[a]:.3f}  {sqrt(kinds[b]/kinds[a]):.3f}")
print("targets (Planck 2018, to verify): dark/ordinary mass 5.36; photons per baryon about 1.6e9 (general knowledge)")
