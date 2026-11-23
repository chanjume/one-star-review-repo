#!/usr/bin/env python3
"""Write one one-star review of something essential to /output/entry.txt.

The essential thing is gravity, reviewed like a faulty product: one
concrete grievance (phone, keys, dignity, same week) and a punchline
that turns on the double meaning of "falling for it". One line, 99 chars.
"""
import os

LINE = "Gravity: dropped my phone, my keys and my dignity in the same week. One star. Still falling for it."


def main():
    assert 1 <= len(LINE) <= 160, "entry must be 1-160 characters"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
