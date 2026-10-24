"""Does the field favour or disfavour the curled tube? It depends on the zero of each square's energy (24 October 2026).

Found by the rule-22 audit of 24 October: the record used two forms of the field's energy as if they were the same,
the Wilson weight exp(beta sum_p cos phi_p) and Q29's energy kappa sum_p (1 - cos phi_p). They differ by a constant
per square, exp(-beta P), and the toy's number of squares P changes with the wiring (the tube has 16 more than the
sheet at N = 64). So, per square, the leading factor is I0(beta) (a reward) under the first form and
exp(-beta) I0(beta) (a penalty, since I0(beta) < exp(beta)) under the second.

This look takes the exact tube-minus-sheet ln Z of `sandbox/u1_exact_free_energy.py` (Wilson form) from its output
file and converts it to the (1 - cos) form by subtracting beta * dP, then gives lambda_eff - 1 at lambda = 1.25, g = 1.5
under both. A sandbox look (rule 16).
"""
import os

import numpy as np
from scipy.special import ive, iv

OUT = os.path.join(os.path.dirname(__file__), "out")
src = os.path.join(OUT, "u1_exact_free_energy_2026-10-24.txt")
rows = []
for line in open(src, encoding="utf-8"):
    parts = line.split()
    if len(parts) == 9 and parts[0] in ("64", "144"):
        try:
            rows.append((int(parts[0]), float(parts[1]), float(parts[5])))   # N, beta, dlnZ exact (Wilson form)
        except ValueError:
            pass
lines = ["Per-square leading factor:   Wilson form ln I0(beta)   |   (1 - cos) form ln(exp(-beta) I0(beta))"]
for b in (0.5, 1.0, 2.0, 3.0, 4.3):
    lines.append(f"   beta {b:3.1f}:  {np.log(iv(0, b)):+.4f}   |   {np.log(ive(0, b)):+.4f}")
lines.append("")
lines.append("lambda_eff - 1 at lambda = 1.25, g = 1.5 (exact tube - sheet, both forms); dP = N/4 extra squares in the tube")
lines.append("    N  beta   dlnZ Wilson   lam_eff-1 Wilson   dlnZ (1-cos)   lam_eff-1 (1-cos)")
for n, b, d in rows:
    dP = n // 4
    d1 = d - b * dP
    lines.append(f"  {n:4d}  {b:4.1f}   {d:10.4f}   {0.25 - 1.5 * d / (4 * n):12.5f}   {d1:12.4f}   {0.25 - 1.5 * d1 / (4 * n):12.5f}")
lines.append("")
lines.append("Read: under the Wilson weight the field lowers the curling cost; under Q29's own energy (zero for a square with no")
lines.append("twist of phase) it raises it, at every beta tried. Which zero is right is a modelling choice, the owner's under S1.")
text = "\n".join(lines)
print(text)
open(os.path.join(OUT, "u1_normalisation_look_2026-10-24.txt"), "w", encoding="utf-8").write(text + "\n")
