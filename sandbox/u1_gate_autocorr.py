"""Why did Gate U1' fail by one point (10 x 10, beta = 8, 3.65 errors; results/gate_u1b_2d_winding.csv)?
A sandbox look, 24 October 2026, fresh seeds (not the gate's).

Two candidates: the winding still under-mixes on the larger torus, or the gate's errors (40 blocks of 1,000 sweeps)
are too small because the measured average changes slowly. Checks: four independent chains of 40,000 sweeps with the
winding move, recording <cos phi> and the winding Q every sweep; the integrated autocorrelation time of each; the
fraction of time at each Q against the exact weights; and the spread between chains against the block error.
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from graphity.cqg_d import torus  # noqa: E402
from graphity.u1 import Field, exact_mean_cos_2d  # noqa: E402

OUT = os.path.join(os.path.dirname(__file__), "out")
os.makedirs(OUT, exist_ok=True)
lines = []


def say(s=""):
    print(s, flush=True)
    lines.append(s)


def tau_int(x, cmax=5000):
    x = np.asarray(x, float) - np.mean(x)
    n = len(x)
    f = np.fft.rfft(x, 2 * n)
    ac = np.fft.irfft(f * np.conj(f))[:n] / (np.arange(n, 0, -1))
    ac /= ac[0]
    tau = 0.5
    for t in range(1, min(cmax, n)):
        tau += ac[t]
        if t >= 6 * tau:            # automatic window (Sokal)
            break
    return tau


f = Field(*torus((10, 10)))
inst = f.instanton()
exact = exact_mean_cos_2d(8.0, f.n_squares)
say(f"10 x 10, beta = 8, exact all-sector <cos> = {exact:.5f}")
means = []
for c in range(4):
    th = np.zeros(f.n_links)
    th, _, _ = f.metropolis(th, 8.0, 0.88, 2000, 1, seed=777000 + c, instanton=inst)
    cos_s, q_s = [], []
    for block in range(400):                # 400 x 100 sweeps; Q read every 100 sweeps
        th, s, _ = f.metropolis(th, 8.0, 0.88, 0, 100, seed=777100 + 1000 * c + block, instanton=inst)
        cos_s.extend(s)
        q_s.append(f.winding(th))
    cos_s = np.array(cos_s)
    tc = tau_int(cos_s)
    tq = tau_int(np.array(q_s, float)) * 100
    blocks = cos_s.reshape(40, -1).mean(axis=1)
    berr = blocks.std(ddof=1) / np.sqrt(40)
    terr = cos_s.std(ddof=1) * np.sqrt(2 * tc / len(cos_s))
    qs, counts = np.unique(q_s, return_counts=True)
    means.append(cos_s.mean())
    say(f"chain {c}: <cos> {cos_s.mean():.5f}, block error {berr:.5f}, tau error {terr:.5f}, tau_int(cos) {tc:.0f} sweeps,"
        f" tau_int(Q) ~{tq:.0f} sweeps; Q visits {dict(zip(qs.tolist(), counts.tolist()))} (of 400 reads)")
m = np.array(means)
say(f"spread between chains: {m.std(ddof=1):.5f}; mean of four {m.mean():.5f} +- {m.std(ddof=1) / 2:.5f}; "
    f"(mean - exact) / that = {(m.mean() - exact) / (m.std(ddof=1) / 2):.2f}")
# exact winding weights at beta = 8 in the Villain-free character sum are not simple; report the Gaussian estimate
P = f.n_squares
w = np.array([np.exp(-8.0 * P * (1 - np.cos(2 * np.pi * q / P))) for q in range(-3, 4)])
say("rough expected winding shares (each winding spread evenly, Gaussian estimate): "
    + ", ".join(f"Q={q}: {x:.3f}" for q, x in zip(range(-3, 4), w / w.sum())))

path = os.path.join(OUT, "u1_gate_autocorr_2026-10-24.txt")
open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("written", path)
