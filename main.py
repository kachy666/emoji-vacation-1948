#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — make.fun entry.

Writes exactly one emoji to /output/entry.txt: Mount Fuji (U+1F5FB).
The whole dream vacation in a single peak — no sand, no plane, no palm
tree. A named place, not a generic postcard: the trip is Japan, and the
mountain everyone on earth recognises is the whole itinerary. One code
point, one character, no words at all.
"""

import os

# Mount Fuji — one code point, the dream vacation is a named place.
EMOJI = "\U0001F5FB"


def main() -> None:
    text = EMOJI
    if not (1 <= len(text) <= 8):
        raise ValueError(f"entry must be 1-8 characters, got {len(text)}")
    if any(ch.isalpha() or ch.isspace() for ch in text):
        raise ValueError("entry must contain no letters or whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"{text} ({len(text)} char)")


if __name__ == "__main__":
    main()
