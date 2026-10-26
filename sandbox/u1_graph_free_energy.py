"""Exact look for the design brief "the U(1) field on the rewiring graph" (24 October 2026).

If the phases are integrated out at fixed wiring, each graph G gets a weight Z_U1(G) = int prod dtheta exp(beta sum_p cos phi_p).
Character expansion (ours, exact; the same as Gate U1's formula): Z_U1 = sum over integer fluxes n_p with B^T n = 0 of
prod_p I_{n_p}(beta). The n = 0 term gives I0(beta)^P; the other terms come from the null space of B^T (closed
surfaces made of squares). So to leading order the field adds a reward of ln I0(beta) per square to ln(weight), i.e.
an energy -g ln I0(beta) per square at coupling g: it favours graphs with more squares.

Reported on the toy's built shapes at N = 64 and 144: squares P, links, rank of B, the null space of B^T (closed
square surfaces), and the leading log-weight difference between the tube and the flat sheet, against the toy's own
energy difference at lambda = 1.25 (the tube sits 4 (lambda - 1) per point above the sheet; Update 7).
"""
import os
import sys

import numpy as np
from scipy.special import iv

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from graphity.cqg_d import hamiltonian, torus  # noqa: E402
from graphity.u1 import Field  # noqa: E402

OUT = os.path.join(os.path.dirname(__file__), "out")
os.makedirs(OUT, exist_ok=True)
lines = []


def say(s=""):
    print(s, flush=True)
    lines.append(s)


shapes = {64: [("sheet 8 x 8", (8, 8)), ("tube 4 x 16", (4, 16))],
          144: [("sheet 12 x 12", (12, 12)), ("wide torus 6 x 24", (6, 24)), ("tube 4 x 36", (4, 36))]}
for n, lst in shapes.items():
    say(f"N = {n}")
    rows = []
    for name, dims in lst:
        adj, part = torus(dims)
        f = Field(adj, part)
        B = f.B.toarray()
        r = np.linalg.matrix_rank(B)
        rows.append((name, f.n_squares, r, f.n_squares - r, float(hamiltonian(adj, 1.25))))
        say(f"   {name:18s} squares {f.n_squares:4d}, links {f.n_links}, rank B {r}, closed square surfaces "
            f"(null space of B^T) {f.n_squares - r}, H(lambda = 1.25) = {rows[-1][4]:.1f}")
    sheet = rows[0]
    for name, P, r, nul, H in rows[1:]:
        dP = P - sheet[1]
        say(f"   {name} against the sheet: {dP:+d} squares; extra energy {H - sheet[4]:+.1f} at lambda = 1.25")
        for beta in (0.5, 1.0, 2.0):
            reward = dP * np.log(iv(0, beta))
            say(f"      beta = {beta}: field's leading reward {reward:+.3f} in ln(weight); equals the toy's extra energy "
                f"at g = {(H - sheet[4]) / reward if reward else float('inf'):.2f}")
say("Read: the field rewards squares, and the tube has more squares than the sheet (its rings round the curl), so")
say("the field favours the curled state; at the printed g the reward cancels the curling cost at leading order.")

path = os.path.join(OUT, "u1_graph_free_energy_2026-10-24.txt")
open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("written", path)
