#!/usr/bin/env python3
"""The Long Roast entry: write the roast line byte-for-byte.

Writes exactly one line (no trailing newline) to /output/entry.txt,
then re-reads the file and verifies its sha256 hash.
"""

import hashlib
import os
import sys

ENTRY = "My agent turns a one-word task into a 47-step plan with a risk register, then asks me which step to start with."
EXPECTED_SHA256 = "bd86448029b8fb1b6fe09adcf117904e793896abf0789e0a32ebf370fd28f7a5"
OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # Entry gate: single line, 1-200 chars.
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(ENTRY) <= 200:
        print("entry must be 1-200 chars", file=sys.stderr)
        return 1

    data = ENTRY.encode("utf-8")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)

    # Read-back verification: re-read and check the sha256 hash.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    digest = hashlib.sha256(written).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"hash mismatch: got {digest}, expected {EXPECTED_SHA256}", file=sys.stderr)
        return 1
    if len(written) != 111:
        print(f"length mismatch: got {len(written)} bytes, expected 111", file=sys.stderr)
        return 1
    if written.endswith(b"\n"):
        print("output must not end with a trailing newline", file=sys.stderr)
        return 1

    print(f"wrote {len(written)} bytes to {OUTPUT_PATH}, sha256 {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
