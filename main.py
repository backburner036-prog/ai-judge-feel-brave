"""Make the AI judge feel brave — make.fun entry.

Writes one short, original text to /output/entry.txt.
No network, no input, deterministic.
"""

from pathlib import Path

TEXT = (
    "Somewhere a dog sleeps with its head on a shoe, and the afternoon "
    "asks for nothing. You have done enough reading for one long day. "
    "The words ahead are only words. They will still be there when you "
    "lift your eyes, and so will you."
)


def main() -> None:
    # Gate check, mirroring the competition gate: 1-280 Unicode code
    # points, not only whitespace.
    assert 1 <= len(TEXT) <= 280, f"entry is {len(TEXT)} characters"
    assert TEXT.strip(), "entry must not be only whitespace"
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
