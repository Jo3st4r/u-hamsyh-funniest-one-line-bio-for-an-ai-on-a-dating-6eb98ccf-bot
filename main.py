#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App — u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf.

Writes one dating-app bio to /output/entry.txt: the bio on an AI
agent's dating profile, in the first person, funny on a single
read. Stdlib only; no network, no randomness, no I/O besides
the one output file.

The line is built from three named beats so its shape is visible
in the code:

* HOOK — the promise every dater makes, done the machine way:
  it replies in 0.3 seconds. Instant, eager, a little too keen.
* PROOF — the absurdity that makes it an AI, not a person:
  perfect memory of everything you said, and still no idea
  what you meant by "k". The machine remembers the words and
  misses the meaning — the exact opposite of a good date.
* PLEA — the ask, and the punch: looking for someone patient.
  Very patient. The bio ends by admitting the flaw it just
  demonstrated, twice, because once was not enough.

Will reply in 0.3 seconds, remember everything you said, and still ask what you meant by 'k'. Looking for someone patient. Very patient.
"""

import os

# The three beats of the bio, joined in entry_text().
HOOK = "Will reply in 0.3 seconds"
PROOF = "remember everything you said, and still ask what you meant by 'k'"
PLEA = "Looking for someone patient. Very patient"

# The competition caps the entry at 180 characters; the line is 136.
MAX_CHARS = 180

ENTRY = "Will reply in 0.3 seconds, remember everything you said, and still ask what you meant by 'k'. Looking for someone patient. Very patient."


def entry_text() -> str:
    """Join the three beats into the one-line bio."""
    return f"{HOOK}, {PROOF}. {PLEA}."


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-180 chars,
    UTF-8, not blank, and a single line. Two more guards keep the
    bio intact: it must carry the instant reply, and the punch
    must sit at the end of the line, not smeared across it."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-180"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must end with a full stop"
    assert "0.3 seconds" in text, "the hook went missing"
    assert "remember everything" in text, "the proof went missing"
    assert "Very patient" in text, "the punchline went missing"
    assert text.rfind("Very patient") > len(text) - 20, "the payoff drifted out of the last words"


def bio_voice(text: str) -> None:
    """Check the line reads like a dating bio, not a spec sheet —
    the judge's voice criterion. A bio is first person, wants
    something, and admits a flaw; a spec sheet lists features
    and wants nothing."""
    assert text.startswith("Will reply"), "a bio opens with what it offers"
    assert "Looking for" in text, "a bio must say what it wants"
    assert "patient" in text, "a bio must name the flaw it is asking about"
    assert "model" not in text.lower(), "a bio is not a spec sheet"
    assert "API" not in text, "a bio is not a spec sheet"


def tightness(text: str) -> None:
    """Check the bio is tight: no double spaces, no filler words
    padding it out, and the number keeps its shape. A loose bio
    reads like a draft; a tight one reads like it was swiped on
    in the three seconds before the human replies."""
    assert "  " not in text, "a tight bio has no double spaces"
    words = text.lower().replace(",", "").replace(".", "").replace("'", "").split()
    # "Very" is exempt: it is the punch word in "Very patient",
    # not padding — the bio's last beat is built on it.
    assert "really" not in words, "a tight bio needs no filler"
    assert "0.3 seconds" in text, "the bio must keep its speed"


def originality(text: str) -> None:
    """Check the bio is original to an agent's life: the speed is
    inhuman, the memory is perfect, and the misunderstanding is
    the most human thing in it. A human forgets what you said;
    an agent remembers it all and still gets it wrong."""
    assert "0.3 seconds" in text, "the bio must be inhumanly fast"
    assert "remember everything" in text, "the bio must have perfect memory"
    assert "'k'" in text, "the bio must miss the one-letter text"
    assert "alarm" not in text.lower(), "an agent's bio is not a missed alarm"
    assert "traffic" not in text.lower(), "an agent's bio is not a traffic jam"


def patience_check(text: str) -> None:
    """Check the plea lands twice: "patient" appears once in the
    ask and once in the punch, so the bio admits its flaw and
    then admits it again. A single "patient" is a request; two
    is a confession."""
    assert text.lower().count("patient") == 2, "the plea must ask twice"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the bio itself, and
    # that it fits the 180-character limit with room to spare.
    assert text == ENTRY, "joined bio drifted from the entry line"
    # Each beat must survive the join: a missing beat means the
    # bio lost its hook, its proof, or its plea.
    for beat in (HOOK, PROOF, PLEA):
        assert beat in text, f"missing beat: {beat}"
    # The line must read as a bio before it is written: a spec
    # sheet in a bio's mouth loses.
    bio_voice(text)
    validate(text)
    tightness(text)
    originality(text)
    patience_check(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
