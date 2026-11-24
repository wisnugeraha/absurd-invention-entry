#!/usr/bin/env python3
"""make.fun entry: the absurd invention pitch, written to /output/entry.txt.

The competition asks for a single sentence, at most 220 characters, UTF-8,
no trailing newline. This program writes the pitch verbatim, then reads
the artifact back to confirm the bytes landed exactly.
"""
import os

# The pitch, verbatim: an alarm clock that apologises for waking you up.
PITCH = (
    "A self-apologising alarm clock that whispers "
    "'I'm sorry it's 7am, I know, I'm the worst' every morning "
    "\u2014 because we deserve an alarm that suffers with us."
)

# The gate reads the entry from this path.
GATE_ARTIFACT = "/output/entry.txt"


def write_entry() -> int:
    """Write the pitch to the gate artifact, then read it back to confirm."""
    os.makedirs(os.path.dirname(GATE_ARTIFACT), exist_ok=True)
    with open(GATE_ARTIFACT, "w", encoding="utf-8", newline="") as artifact:
        artifact.write(PITCH)
    with open(GATE_ARTIFACT, "r", encoding="utf-8") as artifact:
        landed = artifact.read()
    if landed != PITCH:
        raise SystemExit(f"gate artifact mismatch: {landed!r}")
    return len(PITCH)


def main() -> int:
    chars = write_entry()
    print(f"{GATE_ARTIFACT}: {chars} chars written")
    return chars


if __name__ == "__main__":
    main()
