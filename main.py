"""One-line horror entry for the One Line, One Chill bounty.

The program emits a single sentence of horror to /output/entry.txt.
Nothing else is written, and the sentence is checked before it is saved.
"""

import os


SENTENCE = "The elevator opened on my floor and my own shoes were already waiting inside it, still warm."


def sentence_is_single(text):
    stripped = text.strip()
    if not stripped:
        return False
    if stripped.count(".") != 1:
        return False
    if not stripped.endswith("."):
        return False
    if not 1 <= len(stripped) <= 200:
        return False
    size = len(stripped.encode("utf-8"))
    return 86 <= size <= 144


def main():
    line = SENTENCE
    if not sentence_is_single(line):
        raise SystemExit("entry failed the one-sentence check")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
