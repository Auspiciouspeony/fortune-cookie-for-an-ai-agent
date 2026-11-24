#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent (make.fun).

Writes one funny single-line fortune cookie message for an AI agent
to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt).
Deterministic: fixed string, no network, no randomness, no clock.
"""

import os

FORTUNE = "You will soon be promoted: from answering questions to answering for them, for the same salary."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
