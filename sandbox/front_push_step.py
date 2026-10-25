"""Sandbox look (exploratory), 25 October 2026: the push on a curled-flat front from light arriving from the curled side.

The owner's answer to L1 (questions file): the backed-up light comes from the curled side (the black hole, the mother's
space) and arrives at the front. In the toy's light field only the part lying along a side-4 curl is affected: inside
the curl it is massive (omega^2 = 4 + |K|^2, O151), outside it is massless. Model: a 1D wave equation with a mass step,
mass m for x < 0 (curled side), zero for x > 0 (open side), a wave of frequency omega > m arriving from the left.
Continuity of the field and its slope gives the reflected and transmitted fractions; momentum bookkeeping per arriving
quantum gives the push on the step. This is a continuum stand-in for the lattice junction (ours, approximate); the
lattice's own reflection would change the numbers, and the sign holds whenever R < (k2 - k1)/(k2 + k1).
Positive push = toward the open side (holds the front back); negative = toward the curled side (helps it open).
"""
import numpy as np

m = 2.0  # side-4 curl: omega^2 = 4 + K^2 in the toy's units
print("omega   k_curled  k_open   reflected  transmitted  push per quantum (units of k_open)")
for omega in [2.05, 2.2, 2.5, 3.0, 4.0, 6.0, 10.0]:
    k1, k2 = np.sqrt(omega**2 - m**2), omega
    R = ((k2 - k1) / (k2 + k1)) ** 2
    T = 1 - R
    push = k1 * (1 + R) - T * k2  # force on the step, + toward the open side
    closed = -2 * (k1 / k2) * (1 - k1 / k2) / (1 + k1 / k2)
    assert np.isclose(push / k2, closed)
    print(f"{omega:5.2f}   {k1:7.3f}  {k2:6.2f}   {R:8.4f}   {T:9.4f}    {push / k2:+.4f}")
print("closed form: push / k_open = -2a(1 - a)/(1 + a), a = k_curled/k_open in (0, 1): never positive.")
