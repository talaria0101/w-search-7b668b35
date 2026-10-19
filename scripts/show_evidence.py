#!/usr/bin/env python3
"""Print the captured text for an evidence URL, bounded, for verification.

Usage: python3 scripts/show_evidence.py <url> [pattern]
Looks the URL up in evidence/index.tsv, reads the captured body, strips tags,
and prints either the whole (bounded) text or only lines matching `pattern`.
Never dumps a whole large HTML page to the terminal.
"""
import csv
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "evidence" / "index.tsv"


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: show_evidence.py <url> [pattern]")
    url = sys.argv[1]
    pat = sys.argv[2] if len(sys.argv) > 2 else None
    with INDEX.open(encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            if row["url"].strip() != url:
                continue
            path = ROOT / "evidence" / row["path"].strip()
            if not path.exists():
                sys.exit(f"captured body missing: {path}")
            raw = path.read_text(encoding="utf-8", errors="replace")
            raw = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", raw, flags=re.S | re.I)
            text = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", raw)))
            print(f"# {row['url']}  HTTP {row['http_code']}  sha256 {row['sha256']}  {row['captured_utc']}")
            print(f"# {row['path']}")
            if pat:
                for m in dict.fromkeys(re.findall(pat, text, re.I)):
                    print("  ..." + m.strip()[:600] + "...")
            else:
                print(text[:4000])
            return
    sys.exit(f"URL not in evidence index: {url}")


if __name__ == "__main__":
    main()
