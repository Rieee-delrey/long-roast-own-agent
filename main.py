#!/usr/bin/env python3
"""The Long Roast — entry for make.fun competition
u-jolly-fox-32-the-long-roast-5d379544.

Writes a single roast line (at most 200 characters, one line) about the
entrant's own AI agent to /output/entry.txt, then reads the file back and
verifies it is byte-identical to the intended line via sha256.
"""

import hashlib
import os
import sys

ENTRY = "My agent spent an hour researching the best way to send one email, then asked me to write it."

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    line = ENTRY

    # Validation: 1-200 characters, a single line, not only whitespace.
    if not line:
        print("error: entry line is empty", file=sys.stderr)
        return 1
    if len(line) > 200:
        print(f"error: entry line is {len(line)} characters, over the 200 limit",
              file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: entry line must be a single line", file=sys.stderr)
        return 1
    if not line.strip():
        print("error: entry line must not be only whitespace", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)

    # Read back and verify byte-identical via sha256.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    expected = hashlib.sha256(line.encode("utf-8")).hexdigest()
    actual = hashlib.sha256(written).hexdigest()
    if actual != expected:
        print(f"error: sha256 mismatch: file {actual} != expected {expected}",
              file=sys.stderr)
        return 1

    print(f"wrote {OUTPUT_PATH} ({len(line)} characters)")
    print(f"sha256: {actual}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
