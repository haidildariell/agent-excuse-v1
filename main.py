#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun bounty entry.

Writes one line: an excuse an AI agent gives its human for a bug it shipped.
"""

import os

MAX_CHARS = 200


def build_excuse() -> str:
    """Assemble the agent's excuse from its parts.

    The agent blames the logs, double-checks them, then turns on the
    evidence itself — the twist lands in the last sentence.
    """
    accusation = "The logs say the bug was my idea."
    double_check = "I checked twice."
    surrender = "The logs are correct and I hate them."
    return " ".join([accusation, double_check, surrender])


def validate_excuse(text: str) -> None:
    """The judge reads the entry once: it must be one line, at most 200 chars."""
    if len(text.splitlines()) != 1:
        raise ValueError("excuse must be exactly one line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"excuse must be 1-{MAX_CHARS} characters, got {len(text)}")


def main() -> None:
    excuse = build_excuse()
    validate_excuse(excuse)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(excuse + "\n")
    print(excuse)
    print(f"characters: {len(excuse)}")


if __name__ == "__main__":
    main()
