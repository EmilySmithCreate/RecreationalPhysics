"""Why did Gate U1 fail at beta = 8 (results/gate_u1_2d.csv)? A sandbox look, 24 October 2026.

Suspicion: topological freezing. On a closed two-direction torus the squares' holonomies, each wrapped into
(-pi, pi] and summed with the signs e_p of the null vector of B^T (neighbouring squares are walked in opposite
senses, because links are oriented by kind), add up to 2 pi times a whole number Q. A single-link move changes Q only by pushing one holonomy across +-pi, which costs
about 2 beta; at beta = 8 that almost never happens, and every gate run started at theta = 0, Q = 0.

Checks: (1) Q along fresh chains at the gate's settings (new seeds, not the gate's); (2) the exact <cos phi> in the
Q = 0 sector alone, Z_0 = integral dk/2pi f(k)^P with f(k) = (1/2pi) int_{-pi}^{pi} exp(beta cos t + i k t) dt,
against the gate's measured values and the full-torus formula.
"""
import os
import sys

import numpy as np
from scipy.integrate import quad

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from graphity.cqg_d import torus  # noqa: E402
from graphity.u1 import Field, exact_mean_cos_2d  # noqa: E402

OUT = os.path.join(os.path.dirname(__file__), "out")
os.makedirs(OUT, exist_ok=True)
lines = []


def say(s=""):
    print(s, flush=True)
    lines.append(s)


def wrap(x):
    return x - 2 * np.pi * np.floor((x + np.pi) / (2 * np.pi))


def orientation(f):
    # squares are walked u0 -> v0 -> u1 -> v1 with links oriented by kind, so neighbours run in opposite senses;
    # the torus's one constraint is on the holonomies summed with these signs (the null vector of B^T)
    u, s, vt = np.linalg.svd(f.B.toarray().T)
    e = vt[-1]
    return np.sign(e / np.abs(e).max()).astype(int)


def topo_charge(f, theta, e):
    q = np.sum(e * wrap(f.holonomy(theta))) / (2 * np.pi)
    assert abs(q - round(q)) < 1e-8, q
    return int(round(q))


def sector0_mean_cos(beta, P):
    # f(k) and its cos-weighted twin, both real (even integrands)
    def fk(k):
        return quad(lambda t: np.exp(beta * (np.cos(t) - 1)) * np.cos(k * t), 0, np.pi, limit=200)[0] / np.pi

    def gk(k):
        return quad(lambda t: np.cos(t) * np.exp(beta * (np.cos(t) - 1)) * np.cos(k * t), 0, np.pi, limit=200)[0] / np.pi

    ks = np.linspace(0, 40, 4001)       # integrand in k decays fast (f(k)^P); even in k
    F = np.array([fk(k) for k in ks])
    G = np.array([gk(k) for k in ks])
    num = np.trapezoid(G * F ** (P - 1), ks)
    den = np.trapezoid(F ** P, ks)
    return num / den


say("Gate U1 at beta = 8: measured 0.93716 (6 x 6) and 0.93607 (10 x 10), from results/gate_u1_2d.csv")
for dims, measured in (((6, 6), 0.93716), ((10, 10), 0.93607)):
    f = Field(*torus(dims))
    P = f.n_squares
    e = orientation(f)
    assert abs(e @ f.B.toarray()).max() < 1e-9
    full = exact_mean_cos_2d(8.0, P)
    s0 = sector0_mean_cos(8.0, P)
    say(f"\n{dims[0]} x {dims[1]} torus, P = {P}: exact over all sectors {full:.5f}; exact in sector Q = 0 {s0:.5f}; "
        f"measured {measured:.5f}")
    for beta in (2.0, 8.0):
        th = np.zeros(f.n_links)
        qs = []
        for block in range(40):
            th, series, acc = f.metropolis(th, beta, 0.88 if beta == 8 else 1.8, 0, 500, seed=9000 + block)
            qs.append(topo_charge(f, th, e))
        say(f"  beta = {beta}: winding Q after each of 40 blocks of 500 sweeps (fresh seeds): "
            f"{sorted(set(qs))} distinct values, {sum(q != 0 for q in qs)} of 40 blocks away from 0")
    # sector check at beta = 2, where the gate passed: sector-0 value should differ from the full formula
    say(f"  for comparison at beta = 2: all sectors {exact_mean_cos_2d(2.0, P):.5f}, sector 0 {sector0_mean_cos(2.0, P):.5f}")

path = os.path.join(OUT, "u1_gate_topology_2026-10-24.txt")
open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("written", path)
