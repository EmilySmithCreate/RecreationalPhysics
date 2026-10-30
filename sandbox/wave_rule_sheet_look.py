"""A look (sandbox lane; the owner's decision of 30 October, "We definitely need waves in the toy": the wave rule of
docs/design/amplitude_rule_brief.md section 3 adopted as the first form). The brief's section 4 interference test, run here
as a look on a saved resting state before it is pre-registered with her prediction in the strict lane. Kills but never crowns.

The rule: a complex amplitude psi on every point of the arrangement, i dpsi/dt = L psi with L the graph Laplacian,
probability |psi|^2. The excitation starts on one point of a closed loop of four that sits in a flat sheet (the saved T7
end states, the same ones T15 rung 0b used). Two routes of equal length lead round the loop to the opposite point.

Exact, isolated loop of four (the brief): probability at the opposite point is sin^4 t: exactly 1 at t = pi/2 and exactly 0
at t = pi. That is what a wave does and a random walk cannot (its probability rises monotonically to 1/4).

WRITTEN BEFORE COMPUTING (ours): inside the sheet the loop's four points are joined to the sheet by their other links, so
the amplitude leaks out; the probability at the opposite point never reaches 1 and its first peak is below 0.3; by t = pi
most of the probability (> 70 %) is off the loop; the clean zero at t = pi is lost. Rung 0b already found no mode of the
whole arrangement living on the loop, and this is the time-domain face of that. If instead the peak exceeds 0.9 and the
probability returns below 0.05 at t = pi, the loop is a resonator after all and rung 0b's reading would be wrong.
Reported: the probability at the opposite point and the probability on the loop against t, for each loop in each saved
state, beside the isolated-loop curve; the peak value and time; the loop probability at t = pi.

Uses scripts/analyse_t15_resonator.py for the adjacency, the Laplacian and the loop finder (nothing new computed there).
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "src"))
from analyse_t15_resonator import dense, laplacian, loops_and_cubes  # noqa: E402

STATES = ["results/t7d_lam125_n144_adj/N144_rep3.npz", "results/t7d_lam125_n144_adj/N144_rep5.npz"]
TIMES = np.linspace(0.0, 2 * np.pi, 81)


def evolve(lap, start, times):
    w, v = np.linalg.eigh(lap)
    c = v[start, :]  # components of the start state in the eigenbasis (real)
    out = []
    for t in times:
        psi = v @ (np.exp(-1j * w * t) * c)
        out.append(np.abs(psi) ** 2)
    return np.array(out)


def opposite(adj, loop, start):
    nbrs = {int(x) for x in adj[start] if x >= 0}
    return [p for p in loop if p != start and p not in nbrs][0]


if __name__ == "__main__":
    iso = np.sin(TIMES) ** 4
    print("isolated loop of four, exact: p(opposite) = sin^4 t; at t = pi/2: %.3f; at t = pi: %.3f" % (
        np.sin(np.pi / 2) ** 4, np.sin(np.pi) ** 4))
    for s in STATES:
        d = np.load(ROOT / s)
        adj = d["adj"]
        loops, cubes = loops_and_cubes(adj)
        lap = laplacian(dense(adj))
        print("%s: N = %d, loops of four %d, cubes %d" % (s, adj.shape[0], len(loops), len(cubes)))
        for loop in loops:
            start = loop[0]
            opp = opposite(adj, loop, start)
            prob = evolve(lap, start, TIMES)
            p_opp = prob[:, opp]
            p_loop = prob[:, loop].sum(axis=1)
            k = int(np.argmax(p_opp))
            i_pi = int(np.argmin(np.abs(TIMES - np.pi)))
            i_h = int(np.argmin(np.abs(TIMES - np.pi / 2)))
            print("   loop %s -> opposite %d: peak p(opp) = %.3f at t = %.2f (isolated 1.000 at 1.57); p(opp) at pi/2 = %.3f, at pi = %.3f (isolated 0); p(on loop) at pi/2 = %.3f, at pi = %.3f" % (
                loop, opp, p_opp[k], TIMES[k], p_opp[i_h], p_opp[i_pi], p_loop[i_h], p_loop[i_pi]))
            rows = [(TIMES[i], p_opp[i], p_loop[i], iso[i]) for i in range(0, len(TIMES), 8)]
            print("      t      p(opp)  p(loop)  isolated")
            for t, a, b, c in rows:
                print("      %.2f   %.3f   %.3f    %.3f" % (t, a, b, c))
    print("Crowns nothing; the strict-lane version waits for her prediction (amplitude_rule_brief.md, section 4).")
