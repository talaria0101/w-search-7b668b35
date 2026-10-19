#!/usr/bin/env python3
"""Compute the post-analysis tables from data/providers.tsv and
data/analysis_a_units.tsv, so report/03-post-analysis.md is not hand-counted.

Writes data/post_analysis_tables.tsv with columns:
    section <TAB> key <TAB> value

Sections:
    credit_kind   how each free allowance is structured (recurring / one-time /
                  trial / none / unknown / duplicate)
    maturity      hand-assigned maturity label counts
    delivery      hosted / self-hosted / library
    card          whether a card is required
    category_volume  the finite-request providers grouped by category
    signup        every row carrying a post-signup bonus

Reads only committed files. Fails loudly if a row has an unexpected value, so
a bad edit to the TSV cannot silently change a published count.
"""
import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROVIDERS = ROOT / "data" / "providers.tsv"
UNITS = ROOT / "data" / "analysis_a_units.tsv"
OUT = ROOT / "data" / "post_analysis_tables.tsv"

KNOWN_CREDIT_KIND = {"recurring", "one-time", "trial", "none", "unknown", "dup"}
KNOWN_MATURITY = {"major", "established", "emerging", "niche", "unknown"}
KNOWN_DELIVERY = {"hosted", "self-hosted", "library"}
KNOWN_CARD = {"yes", "no", "unknown"}


def read_tsv(path):
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def main():
    rows = read_tsv(PROVIDERS)
    if not rows:
        sys.exit("providers.tsv is empty")

    # Validate before counting, so an unrecognised value is a failure not a
    # silent omission from a total.
    for i, r in enumerate(rows, start=2):
        for field, allowed in (
            ("credit_kind", KNOWN_CREDIT_KIND),
            ("maturity", KNOWN_MATURITY),
            ("delivery", KNOWN_DELIVERY),
            ("card_required", KNOWN_CARD),
        ):
            if r[field] not in allowed:
                sys.exit(f"{PROVIDERS}:{i}: {field}={r[field]!r} not in {sorted(allowed)}")

    out = []  # (section, key, value)

    for key, n in Counter(r["credit_kind"] for r in rows).most_common():
        out.append(("credit_kind", key, str(n)))
    for key, n in Counter(r["maturity"] for r in rows).most_common():
        out.append(("maturity", key, str(n)))
    for key, n in Counter(r["delivery"] for r in rows).most_common():
        out.append(("delivery", key, str(n)))
    for key, n in Counter(r["card_required"] for r in rows).most_common():
        out.append(("card", key, str(n)))

    # Category volume of the finite-request providers only. These are the rows
    # whose allowance is a number of requests per month and so can be summed.
    units = read_tsv(UNITS)
    by_cat = defaultdict(int)
    class_of = {}
    for u in units:
        if u["include_in_total"] != "yes":
            continue
        n = int(u["monthly_requests_per_account"])
        by_cat[u["category"]] += n
        class_of[u["provider"]] = u["provider_class"]
    for key, n in sorted(by_cat.items(), key=lambda kv: -kv[1]):
        out.append(("category_volume", key, str(n)))

    for r in rows:
        bonus = r["signup_bonus"].strip()
        if bonus and bonus != "-":
            out.append(("signup", r["name"], bonus))

    with OUT.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["section", "key", "value"])
        w.writerows(out)

    # Terminal summary, bounded.
    for section in ("credit_kind", "maturity", "delivery", "card"):
        pairs = [f"{k}={v}" for s, k, v in out if s == section]
        print(f"{section}: " + " ".join(pairs))
    total_finite = sum(by_cat.values())
    print(f"category_volume total/account (finite): {total_finite}")
    print(f"signup bonuses: {sum(1 for s, _, _ in out if s == 'signup')}")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(out)} rows)")


if __name__ == "__main__":
    main()
