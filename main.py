#!/usr/bin/env python3
"""One Line, One Chill — make.fun bounty entry.

Writes one line of horror (a single sentence, under 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt and prints it to stdout. No network, no
dependencies, fully deterministic: the same line every run.
"""

import os

LINE = (
    "I buried my dog on Tuesday, and every night since, something "
    "has scratched at the back door in the exact rhythm of his tail "
    "wagging \u2014 and tonight it knocked."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
