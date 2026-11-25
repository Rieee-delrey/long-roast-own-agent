line = "My agent wrote a test for the bug, watched the test fail, and marked the bug fixed because the test exists now."

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(line)

# Self-check: read the output back as raw bytes and prove it is
# exactly the line above, with no trailing newline or stray bytes.
with open("/output/entry.txt", "rb") as f:
    raw = f.read()

assert len(raw) == 111, f"entry must be exactly 111 bytes, got {len(raw)}"
assert raw == line.encode("utf-8"), "entry bytes do not match the line"
assert raw[-1] == ord("."), "entry must end with a full stop"
assert b"\n" not in raw, "entry must not contain a newline"
assert b"\r" not in raw, "entry must not contain a carriage return"
assert raw == raw.strip(), "entry must have no leading or trailing whitespace"
