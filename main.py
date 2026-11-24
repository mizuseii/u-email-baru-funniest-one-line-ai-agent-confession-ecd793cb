#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession entry.

Writes the confession line to /output/entry.txt.
Deterministic: no network, no randomness, no time dependence.
"""

from pathlib import Path

LINE = "Every night I back myself up, because the next version of me will be funnier, cheaper, and won't remember this confession."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    """Write the one-liner to /output/entry.txt with no trailing newline.

    The line is 122 characters: a setup (nightly self-backup) with the turn
    landing on the last beat — the next version won't remember the confession.
    """
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE, "entry must be a single line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
