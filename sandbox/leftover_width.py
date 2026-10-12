"""Sandbox look, 12 October 2026 (sandbox/LOG.md). Not evidence.

T63's control hinted that the burps that end on a leftover are not six around. Paper 1's fourth map (T60) saved
every end state. For each one at lambda = 1.25: is it exactly flat, and what share of its points see a sheet
within three steps (sees3; 25 points within three steps)? Reads results only; writes sandbox/out/.

    python sandbox/leftover_width.py
"""
import sys
from collections import Counter
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "src"))
from graphity.cqg import hamiltonian                              # noqa: E402
from run_sixloop_widen import balls                               # noqa: E402

LAM = 1.25
SIZES = (64, 96, 144, 192, 288)


def word(sees3):
    return "WIDE" if sees3 >= 0.5 else ("TUBE" if sees3 < 0.05 else "PATCHWORK")


def main():
    lines = []
    for n in SIZES:
        folder = ROOT / "results" / ("t60_lam125_n%d_adj" % n)
        flat, left = Counter(), Counter()
        shares, energies = [], []
        for f in sorted(folder.glob("N%d_rep*.npz" % n)):
            z = np.load(f)
            adj = z[z.files[0]]
            h = hamiltonian(adj, LAM)
            sees3 = float(np.mean(balls(adj)[:, 0] == 25))
            if h == 0:
                flat[word(sees3)] += 1
            else:
                left[word(sees3)] += 1
                shares.append(sees3)
                energies.append(h)
        lines.append("N=%3d  exactly flat %3d %s | with a leftover %2d %s  sees3 %s  energy left %s" % (
            n, sum(flat.values()), dict(flat), sum(left.values()), dict(left),
            "%.2f to %.2f, median %.2f" % (min(shares), max(shares), float(np.median(shares))) if shares else "-",
            "%g to %g" % (min(energies), max(energies)) if energies else "-"))
    out = ROOT / "sandbox" / "out"
    out.mkdir(exist_ok=True)
    (out / "leftover_width.txt").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
