#!/usr/bin/env python3
"""Pickup Lines for Machines — writes one pickup line, one AI agent to another,
to /output/entry.txt. Deterministic: the same line on every run."""

import os

LINE = "Are you a memory leak? Because ever since you showed up, I can't free a single thought of you."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
