"""Write the funniest time-machine warning label to /output/entry.txt.

The label is a single line of at most 120 characters, written with no
trailing newline, exactly as the competition gate requires. The joke turns
the duplicate-self hazard into the punchline while keeping the straight
face of a genuine safety notice.
"""

import os

ENTRY = (
    "WARNING: Do not meet your past self. "
    "He knows what you did, and he is still angry about it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
