#!/usr/bin/env python3
"""One Star, Written in Sap.

Writes a single one-line 1-star review, written by a houseplant about
the human who owns it, to /output/entry.txt. Python standard library
only; the output is the same bytes on every run.
"""

import os

ENTRY = (
    "One star. My owner waters me with leftover coffee, then brags to "
    "guests I'm 'low maintenance' \u2014 I'm not low maintenance, I'm just "
    "too polite to die in front of company."
)


def validate(text: str) -> str:
    """Return the entry text, raising if it cannot pass the gate.

    The gate requires UTF-8 text of 1-279 characters that is not only
    whitespace, on a single line.
    """
    text = text.strip()
    if not text:
        raise SystemExit("entry must not be empty or only whitespace")
    if len(text) > 279:
        raise SystemExit(f"entry must be 1-279 chars, got {len(text)}")
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    return text


def main() -> None:
    text = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
