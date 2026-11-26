#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun entry.

Writes a single-sentence alien tourist review of Earth to /output/entry.txt.
Gate: UTF-8 text, 1 to 200 characters, not only whitespace.
"""

import os
from pathlib import Path

ENTRY = (
    "One star: Earth's gravity pinned my third lung to the hotel floor all week, "
    "but the tonkotsu ramen \u2014 broth thick enough to coat the spoon \u2014 "
    "almost made the crushing worth it."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    assert text.count(".") <= 1, "entry must be one sentence"
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"{len(text)} characters written to {out}")
    print(text)


if __name__ == "__main__":
    main()
