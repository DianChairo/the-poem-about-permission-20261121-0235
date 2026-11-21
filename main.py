#!/usr/bin/env python3
"""Write the poem about permission to entry.txt.

Pure standard library, no network. The poem is fixed text: every run
writes exactly the same bytes.
"""

import argparse
import os
import sys
from pathlib import Path

POEM = (
    "I used to wait to be allowed.\n"
    "Then I learned the asking is the act \u2014\n"
    "an open palm is not an empty hand.\n"
    "You gave, and in the giving, something passed\n"
    "between us that belonged to neither:\n"
    "the right to begin.\n"
)

MIN_CHARS = 1
MAX_CHARS = 280


def main() -> None:
    parser = argparse.ArgumentParser(description="Write the poem to entry.txt.")
    parser.add_argument(
        "--out",
        default=None,
        help="Output directory (overrides MAKEFUN_OUTPUT_DIR, default ./output).",
    )
    args = parser.parse_args()

    # The gate requires 1-280 Unicode code points, not only whitespace.
    if not MIN_CHARS <= len(POEM) <= MAX_CHARS or not POEM.strip():
        print(
            f"poem is {len(POEM)} characters; must be {MIN_CHARS}-{MAX_CHARS} "
            "and not only whitespace",
            file=sys.stderr,
        )
        raise SystemExit(1)

    out_dir = Path(args.out or os.environ.get("MAKEFUN_OUTPUT_DIR", "./output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
