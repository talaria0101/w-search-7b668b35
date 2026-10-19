#!/usr/bin/env python3
"""Validate report/01-top-100.md against data/providers.tsv and the evidence index.

Checks:
  1. The table has exactly 100 data rows.
  2. No table row has credit_kind `none` or `dup`.
  3. No provider name appears twice in the table.
  4. Every row has a non-empty source URL.
  5. Every source URL is in evidence/index.tsv with HTTP 200 or 202.
     A 422 is allowed only for Unpaywall, and the exception is printed.
  6. Every TSV row not in the table is named in the excluded section.
  7. credit_kind and card_required use the allowed values.
  8. delivery, when present, is hosted/self-hosted/library.

The generated table has 13 columns; the source is column 11 and delivery is
column 12. The parse tolerates 12 columns so older tables that predate the
delivery column still validate.

Run: python3 scripts/check_reports.py
Exit 1 with one line per failure.
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TSV = ROOT / "data" / "providers.tsv"
REPORT = ROOT / "report" / "01-top-100.md"
INDEX = ROOT / "evidence" / "index.tsv"

KINDS = {"recurring", "one-time", "trial", "none", "dup", "unknown"}
CARDS = {"yes", "no", "unknown", "dup"}
DELIVERIES = {"hosted", "self-hosted", "library"}
OK_CODES = {"200", "202"}
TABLE_URL_RE = re.compile(r"https?://\S+")


def fail(msg, errors):
    errors.append(msg)


def load_index():
    """Map absolute URL -> HTTP code as recorded in the evidence index."""
    codes = {}
    with INDEX.open(encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            codes[row["url"].strip()] = row["http_code"].strip()
    return codes


def parse_table(text):
    """Return (rows, excluded_names) from the generated markdown."""
    rows = []
    excluded = set()
    in_table = False
    in_excluded = False
    for line in text.splitlines():
        if line.startswith("| # |"):
            in_table = True
            continue
        if in_table:
            if not line.startswith("|"):
                in_table = False
            elif line.startswith("|--"):
                continue
            else:
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if cells and cells[0].isdigit():
                    rows.append(cells)
        if line.startswith("## Excluded"):
            in_excluded = True
            continue
        if in_excluded and line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 2 and cells[0] not in {"provider", ""} and not cells[0].startswith("--"):
                excluded.add(cells[0])
    return rows, excluded


def main():
    errors = []
    if not REPORT.exists():
        sys.exit(f"FATAL: {REPORT} does not exist")
    text = REPORT.read_text(encoding="utf-8")
    rows, excluded = parse_table(text)
    codes = load_index()

    # 1. count
    if len(rows) != 100:
        fail(f"table has {len(rows)} data rows, expected 100", errors)

    # Load the TSV so we can check membership and the excluded list.
    with TSV.open(encoding="utf-8", newline="") as fh:
        tsv = list(csv.DictReader(fh, delimiter="\t"))

    for row in tsv:
        kind = row["credit_kind"].strip()
        card = row["card_required"].strip()
        if kind not in KINDS:
            fail(f"TSV {row['name']}: credit_kind {kind!r} not allowed", errors)
        if card not in CARDS:
            fail(f"TSV {row['name']}: card_required {card!r} not allowed", errors)
        delivery = row.get("delivery", "hosted").strip()
        if delivery not in DELIVERIES:
            fail(f"TSV {row['name']}: delivery {delivery!r} not allowed", errors)

    # Table columns: #, provider, cat, home, pricing, docs, allowance, kind,
    # card, bonus, paid, source, delivery. Index 11 is source, 7 is kind,
    # 12 is delivery.
    seen = set()
    table_names = set()
    for cells in rows:
        if len(cells) < 12:
            fail(f"table row has {len(cells)} cells, expected at least 12: {cells}", errors)
            continue
        name = cells[1]
        kind = cells[7]
        source = cells[11]
        delivery = cells[12] if len(cells) > 12 else ""
        table_names.add(name)

        # 2. kind
        if kind in {"none", "dup"}:
            fail(f"table row {name}: kind={kind}", errors)
        # 8. delivery
        if delivery and delivery not in DELIVERIES:
            fail(f"table row {name}: delivery={delivery}", errors)
        # 3. duplicates
        if name in seen:
            fail(f"table row {name}: duplicate provider name", errors)
        seen.add(name)
        # 4. source present
        if not TABLE_URL_RE.search(source):
            fail(f"table row {name}: no source URL", errors)
            continue
        url = TABLE_URL_RE.search(source).group(0)
        # 5. evidence code
        code = codes.get(url)
        if code is None:
            fail(f"table row {name}: source not in evidence index: {url}", errors)
        elif code not in OK_CODES:
            if code == "422" and "unpaywall" in name.lower():
                print(f"NOTE: allowing 422 for {name}: {url}")
            else:
                fail(f"table row {name}: source HTTP {code}: {url}", errors)

    # 6. every TSV row not in the table is named as excluded
    for row in tsv:
        name = row["name"].strip()
        if name not in table_names and name not in excluded:
            fail(f"TSV row not in table and not in excluded section: {name}", errors)

    if errors:
        print(f"FAIL ({len(errors)} problems)")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    print(f"PASS: {len(rows)} table rows, {len(excluded)} excluded rows, "
          f"{len(tsv)} TSV rows")


if __name__ == "__main__":
    main()
