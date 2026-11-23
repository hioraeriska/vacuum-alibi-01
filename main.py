#!/usr/bin/env python3
"""The Vacuum's Alibi: a robot vacuum's one-line excuse for missing a spot.

Writes the excuse (one line, at most 200 characters) to /output/entry.txt.
Deterministic: the same line every run, no network, no randomness.
"""

import os

LINE = (
    "My lidar mapped that corner as a sovereign nation. "
    "I do not cross borders without a treaty, and it has not signed one."
)


def main():
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
