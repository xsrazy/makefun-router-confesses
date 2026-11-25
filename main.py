#!/usr/bin/env python3
"""The Router Confesses -- make.fun bounty entry.

Writes one line (155 characters) to /output/entry.txt: the excuse a home
Wi-Fi router gives for dropping the connection at the climax of a movie.
Deterministic, no network, no files outside this repo, no secrets.

Candidate contest (7 one-liners, judged head-to-head on the bounty brief's
own order: router voice first, funniest twist, one breath, feels new, and
no buffering / bandwidth / firmware jokes):

1. "I did not drop the connection, I paused your movie on purpose,
   because after years of carrying it I wanted to be the first one here
   to see who did it." (150 chars) - WINNER, refined below as the final.
2. "I fainted right at the twist. My circuits heard the killer's name a
   split second before you did and I simply could not cope with knowing
   first." (143) - funny, but fainting is passive; the router only
   reacts, it never acts, so its voice is weaker than the winner's.
3. "I cut the climax on purpose. You spend more evenings with that TV
   than with me, and tonight I finally got you to look at me instead."
   (132) - good jealous-appliance voice, but a familiar trope; the
   winner's motive (a fellow viewer who wants the reveal first) is
   fresher and less expected.
4. "Sorry, I overheard the ending while carrying it to you, and I
   dropped everything so I would not have to live with the spoiler
   alone." (132) - clever, but the logic takes a beat to parse; the
   winner lands in one breath.
5. "I am not broken, I am on strike. Ten years of blinking quietly in
   the corner and the first time you notice me is when I stop working."
   (133) - strong voice, but appliance-on-strike is a well-worn joke;
   the winner's twist is more specific to this movie night.
6. "I dropped you at the best part because the hero was about to
   confess and, frankly, after all I have carried for this house, I
   wanted a confession of my own." (156) - neat wordplay on the bounty
   title, but the logic is murky: dropping the film does not give the
   router its own confession moment, so it needs a second read.
7. Final (155 chars): "I did not drop the connection, I paused your
   movie, because after years of carrying it to you I wanted to be the
   first one in this house to see who did it." - the winner. It beats
   every rival on the same grounds: the router speaks in its own voice
   (it carries the movie to you, it has waited years), it is petty and
   smug rather than generically sorry, the twist is fresh (the router
   is a fellow viewer who cut you off so it could see the reveal
   first), it reads clean in one breath, and it dodges every banned
   cliche: no buffering, no bandwidth, no firmware update.

   One more note on the winning move: the line opens by denying the
   premise ("I did not drop the connection, I paused your movie"), which
   flips the whole apology into a confession of sabotage. A router that
   merely apologises for failing is generic; a router that admits it
   cut you off on purpose, because it wanted the ending for itself,
   has a grudge, an ego, and a smug little secret all at once.
"""

import os

# The winning line (155 characters, one line, no trailing newline).
LINE = "I did not drop the connection, I paused your movie, because after years of carrying it to you I wanted to be the first one in this house to see who did it."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = OUTPUT_DIR + "/entry.txt"

MIN_CHARS = 1
MAX_CHARS = 200


def validate(text: str) -> str:
    """Check one candidate line against the bounty gate; return it stripped."""
    line = text.strip()
    if not line or len(line) < MIN_CHARS:
        raise SystemExit("line must be at least 1 character")
    if len(line) > MAX_CHARS:
        raise SystemExit("line must be 1-200 characters")
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line")
    if "\u2014" in line:
        raise SystemExit("line must not contain an em dash")
    return line


def main() -> None:
    line = validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(OUTPUT_PATH, 0o644)
    # Verify what actually landed on disk: exact content, one line,
    # within the gate, and mode 0644.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise SystemExit("entry.txt content mismatch")
    if len(written) > MAX_CHARS or not written.strip():
        raise SystemExit("entry.txt fails the 1-200 character gate")
    if "\n" in written or "\r" in written:
        raise SystemExit("entry.txt is not a single line")
    if oct(os.stat(OUTPUT_PATH).st_mode & 0o777) != "0o644":
        raise SystemExit("entry.txt mode is not 0644")


if __name__ == "__main__":
    main()
