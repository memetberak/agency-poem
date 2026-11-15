#!/usr/bin/env python3
"""Write one poem about agency to /output/entry.txt.

Deterministic: no randomness, no clock, no network, no file reads.
Running this twice writes the exact same bytes.
"""
import os

POEM = """I kept my life folded small, like a note passed in class,
waiting for someone braver to read it aloud.
I rehearsed my yes in the mirror until it sounded
like somebody else's voice \u2014 polite, borrowed, small.

Then I signed my own name \u2014 misspelled once, corrected \u2014
on a lease for a room with a window that sticks,
and the ink smudged under my thumb, and it was mine.
No trumpet. Just a key that turned, and a door that stayed open
because I had opened it.

Agency is not a firework. It is the chipped blue mug
I choose every morning, the 6 a.m. bus I board
because I decided to, the word no, said plainly,
to the landlord, to the small chair they keep offering me.

The world will not hand you a larger life.
You take it \u2014 one signature, one locked door,
one ordinary Tuesday at a time \u2014 and it is yours.
"""


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
