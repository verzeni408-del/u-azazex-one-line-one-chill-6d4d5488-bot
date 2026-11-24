"""One Line, One Chill entry writer (v1, writer session).

Writes the exact one-sentence horror entry to /output/entry.txt
(no trailing newline), with guards for sentence count and length.
"""

from pathlib import Path

ENTRY = (
    "I called my own number from the hotel phone, and a man who sounded "
    "exactly like me picked up and told me never to come home."
)

MAX_CHARS = 200


def main():
    if ENTRY.count(".") != 1:
        raise ValueError("entry must be exactly 1 sentence")
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError("entry must be 1-200 characters")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
