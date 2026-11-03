"""Sandbox look (kill but not crown): segments of each kind per lattice point (= per unit cube) in the cubic lattice,
and the ratios the owner asked about on 3 November. Exact counting; nothing here is a result."""
from itertools import product
from math import sqrt
kinds = {"edge (1,0,0)": 1, "face diagonal (1,1,0)": 2, "body diagonal (1,1,1)": 3, "long diagonal (1,1,2)": 6}
per_point = {}
for name, s in kinds.items():
    nb = [v for v in product(range(-2, 3), repeat=3) if sum(x * x for x in v) == s]
    per_point[name] = len(nb) // 2          # each segment has two ends
    print(f"{name:24s} length sqrt({s}) = {sqrt(s):.3f}   per cube: {len(nb)//2}")
matter_units = per_point["long diagonal (1,1,2)"] / 3        # an electron: three thirds on three long diagonals
dark_half = per_point["face diagonal (1,1,0)"]                # one half twist per face diagonal
dark_klein = dark_half / 2                                    # two half twists combined into one store
print("matter units per cube (long diagonals / 3):", matter_units)
print("dark half-twist carriers per cube:", dark_half, "; Klein-combined stores:", dark_klein)
print("ratios: dark carriers / matter units =", dark_half / matter_units, "; Klein stores / matter units =", dark_klein / matter_units)
print("by length: 6*sqrt2 / (4*sqrt6) =", 6 * sqrt(2) / (4 * sqrt(6)))
print("by mass as a count (Update 148): dark unit 1 : electron 3")
print("target 5.36 (Planck 2018, to verify); none of the above is it, and ratios from ~8 numbers land near any target by chance")
