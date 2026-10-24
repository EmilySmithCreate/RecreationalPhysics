"""Sandbox look (CLAUDE.md rule 16: may narrow or kill, never support): light at a boundary between curled and flat
space, in the photon field of `graphity.u1` (24 October 2026).

The owner's prediction, recorded before this look (VISION Update 100): "boundary is there is no charge. Maybe it moves
on a different plane." Our reading, to be confirmed by her: light (the field lying in the open directions) crosses the
boundary unchanged; the field component along the curl (the Wilson-line scalar of O151, omega^2 = 4 + |K|^2 inside a
side-4 curl) cannot enter the curled region.

The graph (built by hand, option (i) of the task; nothing from results/ is read). No lattice torus has both a curled
and a flat region. This one is a flat sheet rolled into a cylinder of circumference W along y, closed along x (length
Lx); in the columns Lf <= x < Lx the two y-links (W/2 - 1, W/2) and (W - 1, 0) of every ring are replaced by
(W/2 - 1, 0) and (W - 1, W/2): one switch per column, which splits the ring of W into two rings of W/2. So the x-ring
runs through a flat cylinder of circumference W and then through two parallel tubes of circumference W/2 ("pants" at
both ends). With W = 8 the tubes have side 4: curled, the ring round them a square. With W = 12 they have side 6:
open, the control (same pants geometry, no side-4 ring). Optionally a third direction z, a ring of Lz = 6 (open), at
every point (six links). Every side even, colour (x + y + z) mod 2; the graph is checked 2D-regular, bipartite and
valid (`cqg_d.is_valid`, the hard-core rule).

The measurement (linear regime, Field.evolve at amplitude 1e-3): an exact right-moving packet of flat-space modes
(a Gaussian in k_x built on the uniform x-ring, so no left-moving part), started in the flat region, polarised along
y (the direction that is curled in the tubes) or along z (open in both regions), with a fixed transverse pattern
(k_z for polarisation y, k_y for polarisation z). At the time the incident centre would be 35 columns past the
boundary, the energy (link kinetic energy split half to each end, square energy 1 - cos split a quarter to each
corner) is summed over the flat columns (reflected) and the tube columns (transmitted); the transmitted kinetic energy
is split between y-links (the field along the curl) and x/z-links (field in the open directions). A reference run on
the uniform flat graph of the same size says how much of the packet a perfectly transparent "boundary" leaves behind.

Run: python sandbox/u1_boundary_look.py   (a few minutes)
"""
from __future__ import annotations

import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
from graphity import cqg_d, u1  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
os.makedirs(OUT, exist_ok=True)
lines = []


def say(s=""):
    print(s, flush=True)
    lines.append(s)


# ------------------------------------------------------------------ the graph
class Pants:
    def __init__(self, W, Lx, Lf, Lz=None, split=True):
        assert W % 4 == 0 and Lx % 2 == 0 and (Lz is None or (Lz % 2 == 0 and Lz >= 6))
        self.W, self.Lx, self.Lf, self.Lz, self.split = W, Lx, Lf, Lz, split
        nz = 1 if Lz is None else Lz
        self.nz = nz
        D = 2 if Lz is None else 3
        N = Lx * W * nz
        coords = np.array([(x, y, z) for x in range(Lx) for y in range(W) for z in range(nz)])
        self.coords = coords
        idx = lambda x, y, z: (x * W + y) * nz + z  # noqa: E731
        h = W // 2
        adj = np.empty((N, 2 * D), dtype=np.int64)
        self.link_axis = {}   # frozenset pair -> (axis, start vertex in the + direction)
        for i, (x, y, z) in enumerate(coords):
            tube = split and x >= Lf
            if tube:
                yn = 0 if y == h - 1 else (h if y == W - 1 else y + 1)
                yp = h - 1 if y == 0 else (W - 1 if y == h else y - 1)
            else:
                yn, yp = (y + 1) % W, (y - 1) % W
            nb = [idx((x + 1) % Lx, y, z), idx((x - 1) % Lx, y, z), idx(x, yn, z), idx(x, yp, z)]
            if D == 3:
                nb += [idx(x, y, (z + 1) % nz), idx(x, y, (z - 1) % nz)]
            adj[i] = nb
            self.link_axis[frozenset((i, nb[0]))] = (0, i)
            self.link_axis[frozenset((i, nb[2]))] = (1, i)
            if D == 3:
                self.link_axis[frozenset((i, nb[4]))] = (2, i)
        self.adj = adj
        self.part = (coords.sum(axis=1) % 2).astype(np.int64)
        self.D = D
        # checks
        assert np.all(self.part[adj] != self.part[:, None]), "not bipartite"
        assert cqg_d.is_valid(adj), "not valid (regular, simple, hard-core)"
        self.f = u1.Field(adj, self.part)
        f = self.f
        self.axis = np.empty(f.n_links, dtype=np.int64)
        self.sign = np.empty(f.n_links)
        self.start = np.empty(f.n_links, dtype=np.int64)
        for l in range(f.n_links):
            ax, s = self.link_axis[frozenset((int(f.tail[l]), int(f.head[l])))]
            self.axis[l], self.start[l] = ax, s
            self.sign[l] = 1.0 if s == f.tail[l] else -1.0
        self.vx = coords[:, 0]

    def vertex_energy(self, theta, vel):
        f = self.f
        e = np.zeros(f.n)
        kin = 0.5 * vel ** 2
        np.add.at(e, f.tail, 0.5 * kin)
        np.add.at(e, f.head, 0.5 * kin)
        pot = 1.0 - np.cos(f.B @ theta)
        for j in range(4):
            np.add.at(e, f.squares[:, j], 0.25 * pot)
        return e, kin


# ------------------------------------------------------------------ the packet
def k_perp_sq(kp):
    return 4.0 * np.sin(kp / 2.0) ** 2


def packet(g, pol, k0, kp, x0, sigma, amp):
    """Exact right-moving flat-space packet: theta_l = sign_l Y(y, z) f(x) on links along `pol`."""
    Lx = g.Lx
    m = np.arange(1, Lx // 2)
    k = 2 * np.pi * m / Lx
    om = np.sqrt(4 * np.sin(k / 2) ** 2 + k_perp_sq(kp))
    a = np.exp(-(k - k0) ** 2 * sigma ** 2 / 2) * np.exp(-1j * k * x0)
    xs = np.arange(Lx)
    ph = np.exp(1j * np.outer(xs, k))
    fx = np.real(ph @ a)
    gx = np.real(ph @ (-1j * om * a))
    s = amp / np.abs(fx).max()
    fx, gx = fx * s, gx * s
    th = np.zeros(g.f.n_links)
    vel = np.zeros(g.f.n_links)
    sel = np.flatnonzero(g.axis == pol)
    c = g.coords[g.start[sel]]
    if pol == 1:
        Y = np.cos(kp * c[:, 2])          # pattern along z (k_z)
    else:
        Y = np.cos(kp * c[:, 1])          # pattern along y (k_y), flat-ring coordinate
    th[sel] = g.sign[sel] * Y * fx[c[:, 0]]
    vel[sel] = g.sign[sel] * Y * gx[c[:, 0]]
    w0 = np.sqrt(4 * np.sin(k0 / 2) ** 2 + k_perp_sq(kp))
    vg = np.sin(k0) / w0
    return th, vel, w0, vg


def run(g, pol, k0, kp, amp=1e-3, x0=50.0, sigma=10.0, past=35.0, dt=0.1):
    th, vel, w0, vg = packet(g, pol, k0, kp, x0, sigma, amp)
    q0 = np.abs(g.f.charge(vel)).max()
    e0, _ = g.vertex_energy(th, vel)
    E0 = e0.sum()
    T = (g.Lf + past - x0) / vg
    steps = int(round(T / dt))
    th, vel = g.f.evolve(th, vel, kappa=1.0, dt=dt, steps=steps)
    e, kin = g.vertex_energy(th, vel)
    q1 = np.abs(g.f.charge(vel)).max()
    flat = g.vx < g.Lf
    near = (np.abs(g.vx - g.Lf) < 8) | (g.vx < 8) | (g.vx >= g.Lx - 8)
    tube_links = g.vx[g.start] >= g.Lf
    ky = kin[tube_links & (g.axis == 1)].sum()
    kall = kin[tube_links].sum()
    return dict(w0=w0, vg=vg, T=T, R=e[flat].sum() / E0, Tr=e[~flat].sum() / E0, near=e[near].sum() / E0,
                drift=abs(e.sum() - E0) / E0, q0=q0 / amp, q1=q1 / amp,
                ycurl=(ky / kall) if kall > 1e-30 * E0 else float("nan"))


def show(tag, r, ref):
    say(f"  {tag:<34s} w = {r['w0']:.3f}  v_g = {r['vg']:.3f}  reflected {r['R']:.4f}  transmitted {r['Tr']:.4f}"
        f"  (reference: left behind {ref['R']:.4f})  near-boundary {r['near']:.4f}  y-link share of transmitted"
        f" kinetic {r['ycurl']:.3f}  |dE|/E {r['drift']:.1e}  max|Q|/amp {r['q0']:.0e} -> {r['q1']:.0e}")


def main():
    t0 = time.time()
    say("Light at a curled/flat boundary in the photon field of graphity.u1 (sandbox look, 24 October 2026).")
    say("Graph: flat cylinder of circumference W along y, closed along x (Lx); in columns x >= Lf each y-ring of W is")
    say("split by one switch into two rings of W/2. W = 8: tubes of side 4 (curled); W = 12: tubes of side 6 (control).")
    say("Polarisation y = along the direction that is curled in the tubes; z = third direction, open everywhere.")
    say("Reflected / transmitted = share of the packet's energy in the flat / tube columns when the incident centre")
    say("would be 35 columns past the boundary. Reference = same packet on the uniform flat graph (no split).")
    say("Exact background (O151, ours): inside a side-4 tube the y-component has w^2 = 4 + K_x^2 + K_perp^2, while")
    say("flat-side light has w^2 = K_x^2 + K_perp^2 <= 4 + K_perp^2, so the y-component cannot enter as itself at any")
    say("frequency of the band (with k_z conserved). The only open channels are conversions at the seam.")
    ks = [0.6, 1.2, 2.0, 2.6]

    say("\n--- two directions (four links), Lx = 320, Lf = 120: polarisation y, normal incidence")
    for W in (8, 12):
        g = Pants(W, 320, 120)
        ref = Pants(W, 320, 120, split=False)
        say(f" W = {W} (tubes of side {W // 2}): N = {g.f.n}, links {g.f.n_links}, squares {g.f.n_squares}"
            f" (uniform: {ref.f.n_squares}); valid, bipartite")
        for k in ks:
            show(f"pol y, k_x = {k}", run(g, 1, k, 0.0), run(ref, 1, k, 0.0))
    g = Pants(8, 320, 120)
    ref = Pants(8, 320, 120, split=False)
    show("linearity: pol y k=1.2 amp 1e-2", run(g, 1, 1.2, 0.0, amp=1e-2), run(ref, 1, 1.2, 0.0, amp=1e-2))

    say("\n--- three directions (six links), Lz = 6, Lx = 320, Lf = 120")
    for W in (8, 12):
        g = Pants(W, 320, 120, Lz=6)
        ref = Pants(W, 320, 120, Lz=6, split=False)
        say(f" W = {W} (tubes of side {W // 2}): N = {g.f.n}, links {g.f.n_links}, squares {g.f.n_squares}"
            f" (uniform: {ref.f.n_squares}); valid, bipartite   [{time.time() - t0:.0f} s]")
        cases = []
        for k in (1.2, 2.0):
            cases.append((f"pol y, k_z = 0, k_x = {k}", 1, k, 0.0))
        for k in (1.2, 2.0):
            cases.append((f"pol y, k_z = pi (w > 2), k_x = {k}", 1, k, np.pi))
        for k in (1.2, 2.0):
            cases.append((f"pol z, k_y = 0, k_x = {k}", 2, k, 0.0))
        for k in (1.2, 2.0):
            cases.append((f"pol z, k_y = 2pi/{W}, k_x = {k}", 2, k, 2 * np.pi / W))
        cases.append((f"pol z, k_y = 4pi/{W}, k_x = 1.2", 2, 1.2, 4 * np.pi / W))
        for tag, pol, k, kp in cases:
            show(tag, run(g, pol, k, kp), run(ref, pol, k, kp))
    say(f"\n(total {time.time() - t0:.0f} s)")
    with open(os.path.join(OUT, "u1_boundary_look_2026-10-24.txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
