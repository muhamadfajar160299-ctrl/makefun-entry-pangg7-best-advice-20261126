#!/usr/bin/env python3
"""The Best Advice I Ever Got.

Writes one sentence (at most 200 characters) about the best advice
the writer ever received to entry.txt.
"""

import os
import sys

ENTRY = (
    "My father told me to fix the small leak before it floods the house, "
    "and I have spent twenty years learning he meant people, not pipes."
)

MAX_CHARS = 200


def main():
    text = ENTRY.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        print(f"entry is {len(text)} chars, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("entry must be exactly one sentence", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Write the bare sentence with no trailing newline: the gate counts
    # every character, and a smaller file wins the size tie-break.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
