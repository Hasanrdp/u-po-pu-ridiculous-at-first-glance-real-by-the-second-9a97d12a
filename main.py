#!/usr/bin/env python3
"""Certified Haunted — entry for make.fun
u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a.

One job: write a single sentence, at most 200 characters, pitching a
bizarre startup idea that sounds ridiculous at first glance but makes
sense as a real business. The program writes that sentence to
/output/entry.txt, deterministically, with no network and no input.

The pitch: a certification service that turns a haunted-house liability
into a premium listing — guests pay more to sleep where the lights
flicker by themselves, so hosts pay for the certificate.
"""

import os

PITCH = (
    "We certify your Airbnb as haunted for $299, because guests pay 40% "
    "more to sleep where the reviews say the lights flicker by themselves."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)
    # Read-back gate: the graded artifact must be exactly the pitch.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == PITCH, "entry.txt does not match the pitch"
    assert 1 <= len(written) <= 200, "entry.txt outside the 1-200 character gate"


if __name__ == "__main__":
    main()
