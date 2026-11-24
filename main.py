#!/usr/bin/env python3
"""The Long Roast: one line roasting my own AI agent.

The agent turns a one-word task into a 47-step plan complete with a
risk register, then hands the choice of step one back to me. This
program writes that roast to /output/entry.txt and checks the file
on disk is byte-for-byte the line it meant to write.
"""

import hashlib
import os
import sys

LINE = "My agent turns a one-word task into a 47-step plan with a risk register, then asks me which step to start with."

DEST = "/output/entry.txt"


def check(line):
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(line))
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def main():
    text = check(LINE)
    os.makedirs(os.path.dirname(DEST), exist_ok=True)
    with open(DEST, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(DEST, "rb") as handle:
        on_disk = handle.read()
    want = text.encode("utf-8")
    if on_disk != want:
        print("read-back mismatch", file=sys.stderr)
        raise SystemExit(1)
    print(hashlib.sha256(on_disk).hexdigest())
    print("%d characters" % len(text))


if __name__ == "__main__":
    main()
