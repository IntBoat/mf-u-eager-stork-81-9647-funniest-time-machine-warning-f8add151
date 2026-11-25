#!/usr/bin/env python3
"""Funniest Time Machine Warning Label (make.fun).

Writes the entry -- one funny one-line warning label for a time machine --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = 'Do not wave at yourself. He will wave back, follow you home, and eat your leftovers from next Tuesday.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
