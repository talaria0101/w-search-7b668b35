#!/usr/bin/env python3
"""Build report/01-top-100.md from data/providers.tsv.

Selection: drop rows whose credit_kind is `dup` (aliases of another row) or
`none` (no free tier), and rows with score 0 or an unknown allowance. Sort by
score descending, ties broken by name. Take the top 100 and name the rest in
the excluded section.

`score` is a curated relevance/generosity judgment, not a measurement; it is
used only for ordering. The table mixes hosted APIs, self-hosted software and
libraries; the `delivery` column says which.

Run: python3 scripts/build_top100.py
Exit 1 when fewer than 100 rows survive the filter.
"""
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TSV = ROOT / "data" / "providers.tsv"
OUT = ROOT / "report" / "01-top-100.md"

COLUMNS = [
    "name", "category", "home", "pricing", "docs", "free_allowance",
    "credit_kind", "card_required", "signup_bonus", "paid_from_usd",
    "maturity", "score", "source", "date", "delivery",
]


def load():
    with TSV.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        missing = [c for c in COLUMNS if c not in (reader.fieldnames or [])]
        if missing:
            sys.exit(f"FATAL: providers.tsv missing columns: {missing}")
        return list(reader)


def is_excluded_kind(row):
    """`dup` aliases and `none` (no free tier) never rank."""
    return row["credit_kind"].strip() in {"dup", "none"}


def main():
    rows = load()

    kept, excluded = [], []
    for row in rows:
        name = row["name"].strip()
        if is_excluded_kind(row):
            reason = "duplicate/alias" if row["credit_kind"].strip() == "dup" else "no free tier"
            excluded.append((name, reason))
            continue
        try:
            score = int(row["score"])
        except ValueError:
            excluded.append((name, f"non-numeric score {row['score']!r}"))
            continue
        if score == 0:
            excluded.append((name, "score 0 (no usable free tier captured)"))
            continue
        if not row["free_allowance"].strip() or row["free_allowance"].strip().lower() == "unknown":
            excluded.append((name, "free allowance not captured"))
            continue
        row["_score"] = score
        kept.append(row)

    kept.sort(key=lambda r: (-r["_score"], r["name"].lower()))

    if len(kept) < 100:
        print(f"FATAL: expected at least 100 rows after filtering, got {len(kept)}",
              file=sys.stderr)
        for i, r in enumerate(kept, 1):
            print(f"  keep {i:3d} score={r['_score']:3d} {r['name']}", file=sys.stderr)
        sys.exit(1)

    # The table is the top 100; anything below the cut is named in the report
    # rather than silently dropped.
    below_cut = kept[100:]
    kept = kept[:100]

    lines = []
    lines.append("# Top 100 providers by free tier generosity\n")
    lines.append(
        "Ranked by `score` (see `data/providers.tsv` for the raw column). Every "
        "figure is from the cited row's `source` URL, captured 2026-10-19; HTTP "
        "code and sha256 for each are in `evidence/index.tsv`.\n"
    )
    lines.append(
        "`kind` is `recurring` (resets each month), `one-time` (single grant), "
        "`trial` (expires), or `none`. `card` is whether a credit card is "
        "required to get the free tier. `delivery` is `hosted`, `self-hosted` "
        "or `library`.\n"
    )
    lines.append(
        "`score` and `maturity` are curated judgments used for ordering, not "
        "measurements. The table mixes hosted APIs, keyless public APIs, "
        "self-hosted software and libraries; the `delivery` column tells them "
        "apart, and a row is not comparable across delivery types.\n"
    )
    lines.append("")
    lines.append("| # | provider | cat | home | pricing | docs | free allowance | kind | card | signup bonus | paid from (USD) | source | delivery |")
    lines.append("|--:|---|---|---|---|---|---|---|---|---|---|---|--:|")

    for i, r in enumerate(kept, 1):
        def cell(key):
            return r[key].strip() or "-"
        lines.append(
            "| {i} | {name} | {cat} | {home} | {pricing} | {docs} | {free} | {kind} | {card} | {bonus} | {paid} | {src} | {delivery} |".format(
                i=i,
                name=cell("name"),
                cat=cell("category"),
                home=cell("home"),
                pricing=cell("pricing"),
                docs=cell("docs"),
                free=cell("free_allowance"),
                kind=cell("credit_kind"),
                card=cell("card_required"),
                bonus=cell("signup_bonus"),
                paid=cell("paid_from_usd"),
                src=cell("source"),
                delivery=cell("delivery"),
            )
        )

    lines.append("")
    lines.append("## Excluded from this table\n")
    lines.append(
        f"The inventory has {len(kept) + len(below_cut) + len(excluded)} rows. "
        "Rows filtered out before ranking, with the reason, then rows that "
        "ranked below the 100th place. All remain in `data/providers.tsv` so "
        "the duplicate and unknown captures stay auditable.\n"
    )
    lines.append("| provider | reason |")
    lines.append("|---|---|")
    for name, reason in excluded:
        lines.append(f"| {name} | {reason} |")
    for r in below_cut:
        lines.append(
            f"| {r['name'].strip()} | ranked {r['_score']} "
            f"(below the 100th-place cut at {kept[-1]['_score']}) |"
        )
    lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")

    print(f"wrote {OUT} ({len(kept)} rows)")
    print(f"excluded {len(excluded)} rows:")
    for name, reason in excluded:
        print(f"  - {name}: {reason}")


if __name__ == "__main__":
    main()
