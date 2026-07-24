"""Keep active agent context small, current, and epistemically labelled."""

from __future__ import annotations

import argparse
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]

LINE_BUDGETS = {
    "AGENTS.md": 40,
    "HANDOFF.md": 70,
    "dossier/status.md": 240,
    "dossier/possibility-tree.md": 160,
}

REQUIRED_TEXT = {
    "AGENTS.md": (
        "dossier/records/",
        "make check",
        "Clay problem is unsolved",
    ),
    "HANDOFF.md": (
        "Clay status:** unsolved",
        "Live route:**",
        "Exact live question",
        "Next bounded cycle",
    ),
    "dossier/status.md": (
        "Clay status:** unsolved",
        "Route dashboard",
        "Live gates",
        "Epistemic and validation rules",
    ),
    "dossier/possibility-tree.md": (
        "Closure rule",
        "R3B:",
        "R3C:",
        "Adversarial coverage test",
    ),
}

FORBIDDEN_TEXT = (
    "independently reviewed",
)


def validate(root: Path) -> tuple[dict[str, int], list[str]]:
    """Return line counts and all active-context policy violations."""
    counts: dict[str, int] = {}
    errors: list[str] = []

    for relative, limit in LINE_BUDGETS.items():
        path = root / relative
        if not path.is_file():
            errors.append(f"{relative}: missing")
            continue

        text = path.read_text(encoding="utf-8")
        line_count = len(text.splitlines())
        counts[relative] = line_count

        if line_count > limit:
            errors.append(
                f"{relative}: {line_count} lines exceeds budget {limit}"
            )

        for marker in REQUIRED_TEXT[relative]:
            if marker not in text:
                errors.append(f"{relative}: missing marker {marker!r}")

        lowered = text.lower()
        for phrase in FORBIDDEN_TEXT:
            if phrase in lowered:
                errors.append(
                    f"{relative}: replace legacy label {phrase!r}"
                )

    return counts, errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=REPOSITORY_ROOT)
    arguments = parser.parse_args(argv)
    counts, errors = validate(arguments.root.resolve())

    if errors:
        print("active-context validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    summary = ", ".join(
        f"{path}={count}" for path, count in counts.items()
    )
    print(f"active-context validation OK: {summary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
