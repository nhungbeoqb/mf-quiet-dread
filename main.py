#!/usr/bin/env python3
"""Write the entry text to /output/entry.txt.

Entry: a one-line code review comment approving a pull request with
quiet existential dread. The dread is the code's immortality against
the reviewer's mortality, delivered as a flat three-beat escalation
(company -> on-call rotation -> me) with the twist on the last word,
then a resigned shrug instead of an imperative: "merging anyway"
keeps the approval while letting the dread leak out of the ending.
"""

import os

TEXT = "Approved. This code will outlive the company, the on-call rotation, and eventually me \u2014 merging anyway."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
