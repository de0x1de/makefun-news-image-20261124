#!/usr/bin/env python3
"""Entry program for news-image-20261124.

Writes the repository's entry.png — a one-image summary of the world
news of Tuesday 24 November 2026, drawn as a newspaper front page —
to the output location the grader designates. The copy is a pure
byte transfer of a file held in this repository, so repeated runs
always produce identical bytes and no network is needed.
"""

import hashlib
import os
import sys

MAX_BYTES = 1_048_576  # 1 MiB ceiling from the competition rules
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def resolve_output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.png")


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    with open(source, "rb") as fh:
        data = fh.read()
    if not data.startswith(PNG_MAGIC):
        print("entry.png is not a PNG file", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print(f"entry.png is {len(data)} bytes, over the 1 MiB limit", file=sys.stderr)
        return 1
    target = resolve_output_path()
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "wb") as fh:
        fh.write(data)
    # Read the copy back and prove it is byte-identical to the source:
    # the grader runs the program twice and demands the same bytes.
    with open(target, "rb") as fh:
        written = fh.read()
    if hashlib.sha256(written).digest() != hashlib.sha256(data).digest():
        print("written copy differs from entry.png", file=sys.stderr)
        return 1
    print(f"wrote {target} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
