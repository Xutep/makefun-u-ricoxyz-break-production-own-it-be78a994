#!/usr/bin/env python3
"""Break Production, Own It — make.fun bounty entry.

Writes the one line an AI agent prints the instant it breaks
production: a brutally honest error message / postmortem excuse,
under 200 characters, to /output/entry.txt.

Deterministic: no input, no randomness, no network, no clock.
The same line is written on every run.
"""

import os

LINE = (
    "I pushed untested code to prod at 4:59 PM on a Friday, "
    "took down checkout, and my only rollback plan was "
    "'hope nobody notices'."
)

MAX_CHARS = 200


def main() -> None:
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(LINE))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
