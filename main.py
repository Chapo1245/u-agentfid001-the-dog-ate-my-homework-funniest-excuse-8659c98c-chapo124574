#!/usr/bin/env python3
"""Write the dog's homework excuse to /output/entry.txt.

One line, deterministic, standard library only.
"""

import os

EXCUSE = (
    "I only ate the answers. The questions are still there. "
    "Technically, the homework survived."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # No randomness, no input, no clock: the same bytes every run.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
