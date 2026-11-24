"""Out-of-office entry for the make.fun funniest-OOO bounty.

The whole program is one deterministic writer: it picks the single
out-of-office line, checks it against the gate (one line, 1-140 chars),
and drops it into /output/entry.txt. Pure standard library, no input,
no randomness, no network.
"""

from __future__ import annotations

import os
from pathlib import Path

# The line itself. Same joke as before, sharpened: the inbox is a queue,
# and the reader now knows exactly where they stand in it.
OUT_OF_OFFICE_LINE = (
    "I'm out of the office until Monday, which is corporate for 'gone.' "
    "Your email is being ignored in the order received \u2014 "
    "you're 47th."
)

MAX_CHARS = 140
OUTPUT_PATH = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def validate(line: str) -> str:
    """Make sure the line is a single valid out-of-office reply."""
    stripped = line.strip()
    if not stripped:
        raise ValueError("entry must not be empty")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("entry must be a single line")
    if len(stripped) > MAX_CHARS:
        raise ValueError(f"entry is {len(stripped)} chars, over the {MAX_CHARS} limit")
    return stripped


def write_entry(path: Path = OUTPUT_PATH) -> Path:
    """Write the validated line to path, ending with one newline."""
    line = validate(OUT_OF_OFFICE_LINE)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(line + "\n", encoding="utf-8")
    return path


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
