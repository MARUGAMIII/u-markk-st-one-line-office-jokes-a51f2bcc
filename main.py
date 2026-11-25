#!/usr/bin/env python3
"""One-Line Office Jokes.

Writes the entry - one single-line joke about office life - to
/output/entry.txt. Standard library only, fully deterministic: the same
line is written on every run.
"""

import os

# The entry itself: one single-line joke about office life. The setup is a
# relatable video-call detail (muting yourself and talking on anyway) and
# the laugh lands on the last few words — the meeting was at its most
# productive with nobody hearing a word of it. Do not change this text:
# it is the submitted entry, verified byte-identical across runs.
ENTRY = (
    "I muted myself on the call and kept talking for ten minutes, "
    "which is still the most productive meeting I've ever had."
)

# The gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1-199
# characters, not only whitespace, a single line, and plain ASCII.
MAX_ENTRY_CHARS = 199


def validate_gate(text: str) -> None:
    """Raise ValueError if the entry would fail the competition gate."""
    if not 1 <= len(text) <= MAX_ENTRY_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_ENTRY_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.isascii():
        raise ValueError("entry must be plain ASCII")


def main() -> None:
    """Validate the entry against the gate, then write it to the output file."""
    validate_gate(ENTRY)
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(out_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
