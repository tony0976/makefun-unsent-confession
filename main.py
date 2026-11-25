#!/usr/bin/env python3
"""Writes this entry's text to /output/entry.txt."""

import os

TEXT = """To: Dad
I kept the voicemail where you said you were proud of me, and I still haven't told you I listen to it before every big meeting."""

def main():
    # The bounty scores a micro-confession in exactly two parts: a To: line naming who it was meant for, and the unsent message itself, one line each; fail loudly instead of submitting a malformed entry.
    lines = TEXT.split("\n")
    assert len(lines) == 2, f"entry must be exactly 2 lines, got {len(lines)}"
    assert lines[0].startswith("To: ") and len(lines[0]) > 4, "first line must name who it was meant for"
    assert len(lines[1]) >= 1, "the unsent message itself must not be empty"
    assert lines[1] == lines[1].strip(), "message must not have leading or trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote {len(TEXT)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
