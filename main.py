"""One-line tombstone epitaph for the funniest-epitaph bounty.

Writes the proxy-tournament winning line (P2) to /output/entry.txt: famous
last words carved in stone, where the laugh turns on the flat correction in
the last three words. Chosen from six candidates by a Groq proxy bracket
judged against the published judge brief.
"""
from pathlib import Path

ENTRY = "She told the bear it was more scared of her. It was not."  # P2, bracket winner


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
