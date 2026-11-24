#!/usr/bin/env python3
"""The Funniest Out of Office — make.fun bounty entry.

Writes one out-of-office line (1-140 chars, UTF-8, no trailing
newline) to /output/entry.txt. Pure Python stdlib, deterministic.
"""

import os

LINE = (
    "I'm out of the office, which is corporate for \"gone.\" "
    "My emails are being ignored in the order they were received."
)


def main() -> None:
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE == LINE.strip(), "line must not have leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
