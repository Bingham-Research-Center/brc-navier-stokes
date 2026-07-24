"""Exponent ledger for intermediate feedback-pressure localisation."""

from __future__ import annotations

import json
from typing import Dict


def localization_powers(alpha: float) -> Dict[str, float]:
    """Return the powers of h in the intermediate-scale estimates."""
    if alpha <= 0.0:
        raise ValueError("alpha must be positive")
    return {
        "near_local_energy": 3.0 / 2.0 - alpha / 2.0,
        "near_cutoff": 2.0 + alpha / 2.0,
        "first_feedback_tail": 1.0 / 4.0 + alpha / 2.0,
        "second_feedback_tail": -1.0 / 4.0 + 15.0 * alpha / 2.0,
        "source_radius_gap": 3.0 - alpha,
    }


def admissible_alpha(alpha: float) -> bool:
    """Whether all algebraic pressure contributions vanish."""
    powers = localization_powers(alpha)
    return (
        powers["near_local_energy"] > 0.0
        and powers["near_cutoff"] > 0.0
        and powers["first_feedback_tail"] > 0.0
        and powers["second_feedback_tail"] > 0.0
        and powers["source_radius_gap"] > 0.0
    )


def admissible_interval() -> tuple[float, float]:
    """The sharp open alpha interval from the displayed estimates."""
    return (1.0 / 30.0, 3.0)


def pressure_ceiling(
    h: float,
    alpha: float = 1.0 / 10.0,
) -> float:
    """Dimensionless algebraic ceiling, with constants suppressed."""
    if not 0.0 < h <= 1.0:
        raise ValueError("h must lie in (0, 1]")
    if not admissible_alpha(alpha):
        raise ValueError("alpha is outside the admissible interval")
    powers = localization_powers(alpha)
    return (
        h ** powers["near_local_energy"]
        + h ** powers["near_cutoff"]
        + h ** powers["first_feedback_tail"]
        + h ** powers["second_feedback_tail"]
    )


def main() -> None:
    alpha = 1.0 / 10.0
    powers = localization_powers(alpha)
    payload = {
        "experiment": "intermediate source-feedback localisation",
        "admissible_interval": list(admissible_interval()),
        "chosen_alpha": alpha,
        "powers": powers,
        "ceiling_at_1e-8": pressure_ceiling(1.0e-8, alpha),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
