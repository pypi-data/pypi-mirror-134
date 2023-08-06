"""Some docstring"""

from __future__ import annotations

from typing import Tuple


def equilibrium(S: float, P: float, keq: float) -> Tuple[float, float]:
    """Some docstring"""
    Total = S + P
    S = Total / (1 + keq)
    P = keq * Total / (1 + keq)
    return S, P
