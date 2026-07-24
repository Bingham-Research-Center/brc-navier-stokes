"""Exponent ledger for the first causal feedback interaction."""

from __future__ import annotations

import json
from typing import Dict


def first_interaction_tail_powers() -> Dict[str, tuple[float, float]]:
    """Return (time power, radius-decay power) in the squared L2 tail."""
    return {
        "inner_source": (9.0 / 2.0, 5.0),
        "first_q_tail": (4.0, 7.0),
        "second_q_tail": (5.0 / 2.0, 15.0),
    }


def intermediate_pressure_powers(alpha: float) -> Dict[str, float]:
    """Powers of h after splitting the source coefficient at h^-alpha."""
    if alpha <= 0.0:
        raise ValueError("alpha must be positive")
    return {
        "near_local_energy": 3.0 / 2.0 - alpha / 2.0,
        "near_cutoff": 2.0 + alpha / 2.0,
        "far_inner_source": 3.0 / 4.0 + 5.0 * alpha / 2.0,
        "far_first_q_tail": 1.0 / 2.0 + 7.0 * alpha / 2.0,
        "far_second_q_tail": -1.0 / 4.0 + 15.0 * alpha / 2.0,
        "source_radius_gap": 3.0 - alpha,
    }


def admissible_alpha(alpha: float) -> bool:
    """Whether every first-interaction source pressure term vanishes."""
    powers = intermediate_pressure_powers(alpha)
    return all(power > 0.0 for power in powers.values())


def exterior_shell_powers(source_radius_power: float = 3.0) -> Dict[str, float]:
    """Powers after summing exterior shells from R0=h^-source_radius_power."""
    if source_radius_power <= 0.0:
        raise ValueError("source_radius_power must be positive")
    return {
        "inner_source": 9.0 / 4.0 + 2.0 * source_radius_power,
        "first_q_tail": 2.0 + 3.0 * source_radius_power,
        "second_q_tail": 5.0 / 4.0 + 7.0 * source_radius_power,
    }


def pressure_ceiling(
    h: float,
    alpha: float = 1.0 / 10.0,
) -> float:
    """Dimensionless first-interaction pressure ceiling."""
    if not 0.0 < h <= 1.0:
        raise ValueError("h must lie in (0, 1]")
    if not admissible_alpha(alpha):
        raise ValueError("alpha is outside the admissible interval")
    powers = intermediate_pressure_powers(alpha)
    shell_powers = exterior_shell_powers()
    return sum(h**power for key, power in powers.items() if key != "source_radius_gap") + sum(
        h**power for power in shell_powers.values()
    )


def main() -> None:
    alpha = 1.0 / 10.0
    payload = {
        "experiment": "first causal feedback interaction",
        "tail_powers": first_interaction_tail_powers(),
        "chosen_alpha": alpha,
        "intermediate_pressure_powers": intermediate_pressure_powers(alpha),
        "exterior_shell_powers": exterior_shell_powers(),
        "ceiling_at_1e-8": pressure_ceiling(1.0e-8, alpha),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
