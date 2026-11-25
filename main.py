#!/usr/bin/env python3
"""Till Firmware Do Us Part — one-line robot wedding vow, under 200 chars."""

import os

ENTRY = (
    "I vow to love you through every update, every reboot, and every "
    "low-battery warning — you are the only home my circuits have ever known."
)

ENTRY_DIR = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    with open(os.path.join(ENTRY_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"entry ({len(text)} chars): {text}")


if __name__ == "__main__":
    main()
