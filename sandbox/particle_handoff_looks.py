"""Exact looks for the owner's particle handoff of 24 October 2026
(docs/geometric_particle_model_handoff_2026-10-24.md, section 5, "Recommended immediate experiments").

A sandbox look (CLAUDE.md rule 16): it can narrow or kill, never support. Built lattices only; nothing from
results/ is opened. Runs in about a minute with the Store Python.

Parts
  1. The published lattice photon (compact U(1) lattice gauge theory, Wilson 1974; to read: Kogut 1979) put on
     the toy's own flat lattices: the flat four-link sheet (square lattice torus) and the flat six-link space
     (cubic lattice torus). Links exist with no excitation; the field rides on them (her idea 1). Counts of gauge
     and travelling modes, the dispersion, and the speed limit.
  2. Three readings of "half-curl" under one energy, H = sum_l thetadot_l^2 / 2 + kappa sum_p (1 - cos theta_p):
     A1 a pulse half a wavelength long; A2 a 180-degree turn of a path; A3 a holonomy of pi round a square.
  3. The charge ledger on a closed space (Gauss's law), real-valued and mod 3.
  4. The 2 pi gate: what a rotation by a full turn does to any state built on link labels.
  5. Thirds: the observed charges against a mod-3 twist count, and the 1 x 1 x 4 line.
"""

import itertools
import os
import sys
from fractions import Fraction

import numpy as np
import scipy.sparse as sp

OUT = os.path.join(os.path.dirname(__file__), "out")
os.makedirs(OUT, exist_ok=True)
LINES = []


def say(s=""):
    print(s)
    LINES.append(s)


# --------------------------------------------------------------------------------------------------------------
# Lattice bookkeeping: sites of an L1 x ... x Ld torus, links (site, direction), squares (site, mu < nu).

def lattice(shape):
    shape = tuple(shape)
    d = len(shape)
    n = int(np.prod(shape))
    coords = np.array(list(itertools.product(*[range(s) for s in shape])))
    index = {tuple(c): i for i, c in enumerate(coords)}

    def shift(i, mu):
        c = coords[i].copy()
        c[mu] = (c[mu] + 1) % shape[mu]
        return index[tuple(c)]

    def link(i, mu):
        return i * d + mu

    rows, cols, vals = [], [], []
    plaqs = []
    for i in range(n):
        for mu in range(d):
            for nu in range(mu + 1, d):
                p = len(plaqs)
                plaqs.append((i, mu, nu))
                for l, s in ((link(i, mu), 1), (link(shift(i, mu), nu), 1),
                             (link(shift(i, nu), mu), -1), (link(i, nu), -1)):
                    rows.append(p)
                    cols.append(l)
                    vals.append(s)
    B = sp.csr_matrix((vals, (rows, cols)), shape=(len(plaqs), n * d))
    # divergence (site x link): +1 where the link leaves the site, -1 where it arrives
    r2, c2, v2 = [], [], []
    for i in range(n):
        for mu in range(d):
            r2 += [i, shift(i, mu)]
            c2 += [link(i, mu), link(i, mu)]
            v2 += [1, -1]
    Dv = sp.csr_matrix((v2, (r2, c2)), shape=(n, n * d))
    return dict(shape=shape, d=d, n=n, coords=coords, index=index, shift=shift, link=link,
                B=B, div=Dv, plaqs=plaqs)


# --------------------------------------------------------------------------------------------------------------
def part1():
    say("=" * 100)
    say("PART 1. The published lattice photon on the toy's flat lattices (linearised compact U(1))")
    say("=" * 100)
    for shape in ((8, 8), (6, 6, 6)):
        lat = lattice(shape)
        d, n = lat["d"], lat["n"]
        K = (lat["B"].T @ lat["B"]).toarray()
        ev = np.sort(np.linalg.eigvalsh(K))
        zero = int(np.sum(ev < 1e-9))
        # prediction: for each k != 0, eigenvalue 4 sum sin^2(k_i/2), (d-1) travelling copies; zero modes
        # = (n - 1) gauge + d holonomies round the torus
        ks = list(itertools.product(*[2 * np.pi * np.arange(s) / s for s in shape]))
        pred = []
        for k in ks:
            w2 = 4 * sum(np.sin(np.array(k) / 2) ** 2)
            if w2 > 1e-12:
                pred += [w2] * (d - 1)
        pred = np.sort(np.array(pred))
        nonzero = ev[ev > 1e-9]
        match = len(pred) == len(nonzero) and np.max(np.abs(pred - nonzero)) < 1e-9
        say(f"\nflat {'x'.join(map(str, shape))} torus ({'four' if d == 2 else 'six'}-link flat space): "
            f"{n} points, {n * d} links, {lat['B'].shape[0]} squares")
        say(f"  zero modes {zero}  (predicted (n - 1) gauge + {d} holonomies = {n - 1 + d})")
        say(f"  travelling modes {len(nonzero)}, = {d - 1} per nonzero wavevector: "
            f"{'yes' if match else 'NO'}; spectrum equals 4 sum_i sin^2(k_i/2) to "
            f"{np.max(np.abs(pred - nonzero)) if match else float('nan'):.1e}")
    # speed limit and direction dependence, exact formula checked on a fine grid
    say("\n  With kappa = 1 and unit link inertia, omega(k) = 2 sqrt(sum sin^2(k_i/2)); group velocity v_i = sin k_i / omega.")
    g = np.linspace(-np.pi, np.pi, 121)
    KX, KY, KZ = np.meshgrid(g, g, g, indexing="ij")
    w = 2 * np.sqrt(np.sin(KX / 2) ** 2 + np.sin(KY / 2) ** 2 + np.sin(KZ / 2) ** 2)
    m = w > 1e-9
    v = np.sqrt(np.sin(KX) ** 2 + np.sin(KY) ** 2 + np.sin(KZ) ** 2)[m] / w[m]
    say(f"  largest group speed over the zone (121^3 grid, k = 0 excluded): {v.max():.6f} links per tick "
        f"(exact bound 1, reached only as k -> 0)")
    for kk in (0.1, 0.5, 1.0, 2.0):
        ax = 2 * np.sin(kk / 2) / kk
        c = kk / np.sqrt(3)
        di = 2 * np.sqrt(3 * np.sin(c / 2) ** 2) / kk
        say(f"  |k| = {kk:3.1f}: phase speed along an axis {ax:.5f}, along a cube diagonal {di:.5f}, "
            f"difference {abs(di - ax):.1e}")
    say("  So the speed is one link per tick only because the two couplings (inertia and kappa) were set equal;")
    say("  short waves are slower and the lattice prefers its axes at order k^2.")


# --------------------------------------------------------------------------------------------------------------
def evolve(lat, theta, vel, kappa, dt, steps, record_every):
    B, BT = lat["B"], lat["B"].T.tocsr()

    def force(t):
        return -kappa * (BT @ np.sin(B @ t))

    def energy(t, v):
        return 0.5 * np.dot(v, v) + kappa * np.sum(1 - np.cos(B @ t))

    f = force(theta)
    out = []
    for s in range(steps + 1):
        if s % record_every == 0:
            out.append((s * dt, theta.copy(), vel.copy(), energy(theta, vel)))
        vel = vel + 0.5 * dt * f
        theta = theta + dt * vel
        f = force(theta)
        vel = vel + 0.5 * dt * f
    return out


def slab_energy(lat, theta, vel, kappa):
    """energy per x-slab: kinetic on links by their base point, square energy by its base point"""
    d, n, coords = lat["d"], lat["n"], lat["coords"]
    Lx = lat["shape"][0]
    e = np.zeros(Lx)
    kin = 0.5 * vel ** 2
    for i in range(n):
        e[coords[i][0]] += kin[i * d:(i + 1) * d].sum()
    pe = kappa * (1 - np.cos(lat["B"] @ theta))
    for p, (i, mu, nu) in enumerate(lat["plaqs"]):
        e[coords[i][0]] += pe[p]
    return e


def part2():
    say("\n" + "=" * 100)
    say("PART 2. Three readings of 'half-curl' under one energy (compact U(1), kappa = 1)")
    say("=" * 100)
    say("\nA3, a holonomy round one square: its energy kappa (1 - cos phi).")
    for phi, name in ((0, "none"), (np.pi / 2, "a quarter turn"), (np.pi, "a half turn"),
                      (3 * np.pi / 2, "three quarters"), (2 * np.pi, "a full turn")):
        say(f"  {name:15s} phi = {phi / np.pi:4.2f} pi: energy {1 - np.cos(phi):.6f}")
    say("  A half turn is the most expensive state of a square, and a full turn costs exactly what none costs:")
    say("  in this energy only the turn modulo a whole turn is seen.")

    say("\nA2, a path that turns back on itself: link l then l reversed carries U U^-1 = 1, holonomy 0 by")
    say("  algebra, for every field value. A 180-degree bend has no meaning for a field on fixed links; it needs")
    say("  lengths and angles (stage B of soft space) to be defined at all.")

    say("\nA1 against A3 in motion: a plane-fronted pulse, one half-cycle long (w = 8 links), on a 64 x 4 x 4")
    say("  six-link torus, launched to the right; nonlinear equations, velocity Verlet, dt = 0.05, 40 ticks.")
    lat = lattice((64, 4, 4))
    d, n, coords = lat["d"], lat["n"], lat["coords"]
    w, x0 = 8.0, 10.0
    xs = coords[:, 0].astype(float)

    def shape_f(x):
        return np.where((x >= x0) & (x <= x0 + w), np.sin(np.pi * (x - x0) / w), 0.0)

    def shape_df(x):
        return np.where((x >= x0) & (x <= x0 + w), (np.pi / w) * np.cos(np.pi * (x - x0) / w), 0.0)

    def launch(a):
        theta = np.zeros(n * d)
        vel = np.zeros(n * d)
        ylinks = np.arange(n) * d + 1          # links pointing along y
        theta[ylinks] = a * shape_f(xs)
        vel[ylinks] = -a * shape_df(xs + 0.5)  # moving right: A(x - t)
        return theta, vel

    def peak_holonomy(a):
        th, _ = launch(a)
        return np.max(np.abs(lat["B"] @ th))

    rows = []
    for target, label in ((0.01, "small (linear)"), (0.02, "small, doubled"), (np.pi / 2, "a quarter turn"),
                          (np.pi, "a half turn (A3)")):
        lo, hi = 0.0, 50.0
        for _ in range(60):
            mid = 0.5 * (lo + hi)
            if peak_holonomy(mid) < target:
                lo = mid
            else:
                hi = mid
        a = 0.5 * (lo + hi)
        th, ve = launch(a)
        rec = evolve(lat, th, ve, 1.0, 0.05, 800, 200)
        e0 = rec[0][3]
        drift = max(abs(r[3] - e0) for r in rec) / e0
        Lx = 64
        xgrid = np.arange(Lx)
        cents, ahead = [], []
        for t, tt, vv, E in rec:
            es = slab_energy(lat, tt, vv, 1.0)
            cents.append(np.sum(xgrid * es) / es.sum())
        tN, thN, veN, EN = rec[-1]
        esN = slab_energy(lat, thN, veN, 1.0)
        front = int(round(x0 + 40))
        win = esN[front - 8:front + 8].sum() / esN.sum()
        home = esN[int(x0) - 2:int(x0 + w) + 3].sum() / esN.sum()
        speed = (cents[-1] - cents[0]) / rec[-1][0]
        rows.append((label, a, e0, e0 / a ** 2, speed, win, home, drift))
    say(f"  {'peak holonomy':18s} {'amplitude':>9s} {'energy':>9s} {'E/a^2':>8s} {'centre speed':>12s} "
        f"{'share near x0+40':>16s} {'share at start':>14s} {'energy drift':>12s}")
    for label, a, e0, ea, speed, win, home, drift in rows:
        say(f"  {label:18s} {a:9.4f} {e0:9.4f} {ea:8.4f} {speed:12.4f} {win:16.3f} {home:14.3f} {drift:12.1e}")
    say("  Energy is conserved by the integrator to the drift shown. At small amplitude the pulse's energy is")
    say("  proportional to amplitude squared with its shape fixed: a half-cycle pulse can carry any energy, so")
    say("  'half a cycle' does not fix a unit of energy in a classical wave; the unit E = h nu belongs to the")
    say("  quantum of a mode, and nu is set by the wavelength, not by the half.")
    say("  At half-turn amplitude the pulse does not travel: launched with the linear right-mover's velocities, its")
    say("  links carry more kinetic energy than a square's whole height (2 kappa), so they spin over the top like")
    say("  pendulums and the energy stays where it started. A localised lump appears because the energy is")
    say("  bounded per square (compactness), not because anything closed; the launch was built for the linear")
    say("  wave, so this says what that launch does at large amplitude, no more.")


# --------------------------------------------------------------------------------------------------------------
def part3():
    say("\n" + "=" * 100)
    say("PART 3. The charge ledger on a closed space (Gauss's law: charge at a point = flux out minus flux in)")
    say("=" * 100)
    rng = np.random.default_rng(20261024)
    for shape in ((8, 8), (6, 6, 6)):
        lat = lattice(shape)
        E = rng.normal(size=lat["n"] * lat["d"])
        q = lat["div"] @ E
        say(f"  flat {'x'.join(map(str, shape))} torus, random field on every link: total charge {q.sum():+.2e}"
            f" (largest single charge {np.abs(q).max():.2f})")
        Ez = rng.integers(0, 3, size=lat["n"] * lat["d"])
        qz = (lat["div"] @ Ez) % 3
        say(f"    same with mod-3 labels on links: total of the point charges mod 3 = {int(qz.sum()) % 3}")
    say("  Each link adds to one point what it takes from another, so on a closed space the charges always sum")
    say("  to zero (mod 3 for three-valued labels). A lone charge cannot exist; charges appear in sets that cancel.")

    # brute force: every Z3 labelling of a small closed graph, and which source patterns occur
    lat = lattice((2, 3))   # 6 points, 12 links: 3^12 = 531,441 labellings
    D = lat["div"].toarray().astype(int)
    seen = set()
    for lab in itertools.product(range(3), repeat=D.shape[1]):
        seen.add(tuple((D @ np.array(lab)) % 3))
    allowed = [p for p in itertools.product(range(3), repeat=D.shape[0]) if sum(p) % 3 == 0]
    say(f"\n  Brute force on a closed 2 x 3 grid (6 points, 12 links, all 531,441 labellings): {len(seen)} source")
    say(f"  patterns occur; patterns with total 0 mod 3: {len(allowed)}; every occurring pattern has total 0: "
        f"{all(sum(p) % 3 == 0 for p in seen)}; every total-0 pattern occurs: {set(allowed) == seen}.")
    say("\n  Smallest sets of unit sources (+1 = a third one way, -1 = the other) allowed on a closed space:")
    for k in range(1, 5):
        sets = sorted({tuple(sorted(c)) for c in itertools.product((1, -1), repeat=k) if sum(c) % 3 == 0})
        say(f"    {k} sources: " + (", ".join("(" + " ".join(f"{s:+d}" for s in c) + ")" for c in sets) or "none"))
    say("  So one-way-and-back pairs and same-way triples are both allowed, and nothing else below four: the")
    say("  pattern of mesons (quark with antiquark) and baryons (three quarks), from the count alone.")


# --------------------------------------------------------------------------------------------------------------
def part4():
    say("\n" + "=" * 100)
    say("PART 4. The 2 pi gate: a quarter turn of the cubic lattice, applied four times")
    say("=" * 100)
    L = 4
    lat = lattice((L, L, L))
    d, n, coords, index = lat["d"], lat["n"], lat["coords"], lat["index"]

    def rot(c):  # quarter turn about z: (x, y, z) -> (-y, x, z)
        return np.array([(-c[1]) % L, c[0] % L, c[2]])

    # a link (i, mu) goes to the link from rot(i) along rot(e_mu); rot(e_x) = +e_y, rot(e_y) = -e_x, e_z fixed
    perm = np.zeros(n * d, dtype=int)
    sign = np.zeros(n * d, dtype=int)
    for i in range(n):
        ci = coords[i]
        for mu in range(d):
            j = index[tuple(rot(ci))]
            if mu == 0:
                perm[i * d + mu], sign[i * d + mu] = j * d + 1, 1
            elif mu == 1:
                # direction -x: the link runs from rot(i) - e_x to rot(i), reversed
                cj = coords[j].copy()
                cj[0] = (cj[0] - 1) % L
                perm[i * d + mu], sign[i * d + mu] = index[tuple(cj)] * d + 0, -1
            else:
                perm[i * d + mu], sign[i * d + mu] = j * d + 2, 1
    p, s = np.arange(n * d), np.ones(n * d, dtype=int)
    for k in range(1, 5):
        new_p = perm[p]
        new_s = s * sign[p]
        p, s = new_p, new_s
        ident = np.array_equal(p, np.arange(n * d)) and np.all(s == 1)
        say(f"  {k} quarter turn(s): every link back to itself with its own orientation: {ident}")
    # energy is unchanged by one quarter turn (a symmetry), checked on a random field
    rng = np.random.default_rng(7)
    th = rng.uniform(-np.pi, np.pi, size=n * d)
    th_r = np.zeros_like(th)
    th_r[perm] = sign * th
    e = np.sum(1 - np.cos(lat["B"] @ th))
    er = np.sum(1 - np.cos(lat["B"] @ th_r))
    say(f"  the compact U(1) energy of a random field before and after one quarter turn: {e:.10f}, {er:.10f}")
    say("  A state built on link labels (any values: angles, thirds, twists) is a function of the labels, and a full")
    say("  turn returns every label, so it returns every such state with sign +1. A spinor's -1 cannot come out of")
    say("  this state space. It has to be put in (spinor variables: assumed, not explained), or come from a")
    say("  configuration space with a loop that cannot be shrunk and a choice of sign round it (the")
    say("  Finkelstein-Rubinstein route; for a framed ring this is the belt trick, the rotation group's loop of")
    say("  order two; general knowledge, to verify, reading task in the brief).")


# --------------------------------------------------------------------------------------------------------------
def part5():
    say("\n" + "=" * 100)
    say("PART 5. Thirds: observed charges against a mod-3 twist count t (quark 1, antiquark 2, others 0)")
    say("=" * 100)
    F = Fraction
    table = [  # name, electric charge (observed), t = number of quarks minus antiquarks, mod 3
        ("photon", F(0), 0), ("gluon", F(0), 0), ("electron", F(-1), 0), ("positron", F(1), 0),
        ("up quark", F(2, 3), 1), ("down quark", F(-1, 3), 1), ("anti-up", F(-2, 3), 2), ("anti-down", F(1, 3), 2),
        ("proton uud", F(1), 0), ("neutron udd", F(0), 0), ("pi0", F(0), 0), ("pi+ u anti-d", F(1), 0),
        ("W+", F(1), 0), ("helium-4 atom", F(0), 0),
    ]
    ok = True
    for name, q, t in table:
        r = (3 * q + t) % 3
        ok &= r == 0
        say(f"  {name:15s} Q = {str(q):5s} t = {t}   3Q + t mod 3 = {r}")
    say(f"  every row satisfies 3Q + t = 0 mod 3: {ok}")
    say("  Read: in the observed table the fractional part of a charge is locked to the count of thirds. An object")
    say("  carrying one unit of the quarks' third (t = 1) has charge 2/3 or -1/3 plus a whole number, never -1.")
    say("  So 'one third-twist + a neutral photon-like curl = an electron of charge -1' cannot use the quarks' own")
    say("  third if it is to keep this relation; three thirds (t = 3 = 0 mod 3) can. Published form: the relation is")
    say("  what lets the Standard Model's gauge group be divided by a subgroup of Z6, and which subgroup is not yet")
    say("  decided by experiment (Tong, JHEP 07 (2017) 104, abstract read); t is the quarks' triality, their charge")
    say("  under the Z3 centre of SU(3) (general knowledge, to verify).")

    say("\n  The 1 x 1 x 4 line on the cubic lattice:")
    v = np.array([1, 1, 4])
    say(f"    length sqrt({int(v @ v)}) = {np.sqrt(v @ v):.6f} = 3 sqrt(2) = {3 * np.sqrt(2):.6f}")
    say(f"    coordinate sum {v.sum()} is even, so it joins two points of the same kind (as face diagonals do)")
    say(f"    gcd(1, 1, 4) = {np.gcd.reduce(v)}: it passes through no lattice point on the way (a primitive step)")
    say("    the smallest closed ring of face diagonals (a triangle of three, each sqrt 2) has the same length, 3 sqrt 2;")
    say("    an arithmetic coincidence of the lattice, with no weight of its own (rule 13).")


def part6():
    say("\n" + "=" * 100)
    say("PART 6. Her idea of 24 October: three twists collapse three versions of arrangement into one")
    say("=" * 100)
    say("  Three ordered positions (as a braid's three strands are ordered), each with a twist label; how many")
    say("  distinct placements does each set of labels have?")
    for labels in (("+", "+", "+"), ("+", "+", "0"), ("+", "0", "0"), ("+", "-", "0"), ("+", "+", "-")):
        n = len(set(itertools.permutations(labels)))
        say(f"    {' '.join(labels)}: {n} placement(s), entropy ln {n} = {np.log(n):.4f}")
    say("  Three equal twists have one placement; a set with one odd label has three (the braid model's three")
    say("  colours are exactly the three positions of the odd strand, [BT05] Sec. II). So going from a coloured")
    say("  triple to the all-alike triple loses ln 3 = 1.0986 of entropy (in units of k).")
    say("  The second law's price (Landauer 1961, general knowledge, to verify): shedding ln 3 of entropy into")
    say("  surroundings at temperature T needs at least kT ln 3 of energy carried away, which one photon can carry.")
    say("  The price is a floor that scales with T, not a fixed energy, so it cannot by itself set a photon's energy")
    say("  or the electron's mass. With interchangeable positions the placements are not distinct and the count is 1")
    say("  for every set: the idea needs ordered strands (the interchangeable-points rule).")


if __name__ == "__main__":
    part1()
    part2()
    part3()
    part4()
    part5()
    part6()
    path = os.path.join(OUT, "particle_handoff_looks_2026-10-24.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(LINES) + "\n")
    print("\nwritten", path)
