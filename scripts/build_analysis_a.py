#!/usr/bin/env python3
"""Compute the 5-account volume estimate from data/analysis_a_units.tsv.

Every included row carries a monthly request count and the basis for converting
the provider's published allowance into requests. Rows whose allowance is a
credit, a trial, a one-time grant, a rate limit, or uncaptured are not in this
file; they are named in `EXCLUDED_CLASSES` below and in report/03.

The script:
  * verifies every `source` is in evidence/index.tsv with HTTP 200 or 202,
    so a stale source URL fails the build rather than being published;
  * recomputes the per-class and overall totals and asserts the arithmetic;
  * writes data/analysis_a_totals.tsv and prints the summary.

Run: python3 scripts/build_analysis_a.py
"""
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UNITS = ROOT / "data" / "analysis_a_units.tsv"
INDEX = ROOT / "evidence" / "index.tsv"
OUT = ROOT / "data" / "analysis_a_totals.tsv"

ACCOUNTS = 5
OK_CODES = {"200", "202"}

EXCLUDED_CLASSES = [
    "credit-based allowances where 1 credit != 1 request was not documented "
    "(Firecrawl, Diffbot, ZenRows, ScrapingAnt, Bright Data, Browserless, "
    "Crawl4AI, Scrape.do, Context.dev)",
    "one-time grants, reported separately, not multiplied "
    "(Serper 2,500, Linkup 4,000, Search1API 100, ScrapingBee 1,000, "
    "Scrapfly 1,000, ScrapeBadger 1,000, Hyperbrowser 5,000, "
    "Browserbase 1,000+1,000, Crawlbase 5,000, Notte, Steel.dev, Octen, Valyu, "
    "Scrapingdog 100, ScrapeGraphAI 500, Talordata 500, Newscatcher 2,000)",
    "trials and time-boxed grants, reported separately "
    "(Urlbox, Serply, Olostep, Core.ac.uk, Serp House, HasData, ScraperAPI, "
    "DataForSEO, Oxylabs, Zyte)",
    "rate limits, which are not monthly allowances and are listed separately "
    "(GitHub 60/hour or 5,000/hour, npm, PyPI, Overpass, OpenLibrary 3 req/s, "
    "MusicBrainz 1 req/s, Zenodo 5,000/hour, Europe PMC, Semantic Scholar "
    "1 req/s, Crossref, PubMed, Hacker News Algolia 10,000/hour, Reddit 100 QPM)",
    "uncapped or unpriced free APIs with no published number "
    "(Wikipedia, Wikidata, Common Crawl, GDELT, Wayback CDX, Nominatim, "
    "DuckDuckGo Instant Answer)",
    "products with no free API tier "
    "(Perplexity, OpenAI Web Search, Anthropic Web Search, xAI Live Search, "
    "DeepSeek Search, Mojeek, Ahrefs, Semrush, Kagi, Value SERP)",
    "self-hosted software and libraries, whose throughput is the operator's "
    "hardware, not a vendor allowance (SearXNG, Whoogle, LibreY, 4get, Mwmbl, "
    "YaCy, Postlight Parser, Trafilatura, Readability)",
]


def load_index_codes():
    codes = {}
    with INDEX.open(encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            codes[row["url"].strip()] = row["http_code"].strip()
    return codes


def main():
    codes = load_index_codes()
    with UNITS.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))

    errors = []
    for row in rows:
        src = row["source"].strip()
        if codes.get(src) not in OK_CODES:
            errors.append(f"{row['provider']}: source not 200/202 in index: {src}")
        if row["include_in_total"].strip() != "yes":
            errors.append(f"{row['provider']}: row present but not marked include_in_total=yes")
        try:
            int(row["monthly_requests_per_account"])
        except ValueError:
            errors.append(f"{row['provider']}: non-integer monthly count {row['monthly_requests_per_account']!r}")
    if errors:
        print("FAIL")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    by_class = {}
    for row in rows:
        n = int(row["monthly_requests_per_account"])
        cls = row["provider_class"].strip()
        by_class[cls] = by_class.get(cls, 0) + n

    per_account_all = sum(int(r["monthly_requests_per_account"]) for r in rows)
    per_account_core = by_class.get("core", 0)
    per_account_adjacent = by_class.get("adjacent", 0)

    # Assert the parts recompute the whole.
    assert per_account_core + per_account_adjacent == per_account_all, "class split does not sum"

    lines = ["scope\trequests_per_account\trequests_for_5_accounts"]
    lines.append(f"all_included\t{per_account_all}\t{per_account_all * ACCOUNTS}")
    lines.append(f"core_web_fetch_search_crawl\t{per_account_core}\t{per_account_core * ACCOUNTS}")
    lines.append(f"adjacent_data_apis\t{per_account_adjacent}\t{per_account_adjacent * ACCOUNTS}")
    for cls in sorted(by_class):
        lines.append(f"class:{cls}\t{by_class[cls]}\t{by_class[cls] * ACCOUNTS}")
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"rows included: {len(rows)}")
    print(f"per account (all included):    {per_account_all:,}")
    print(f"per account (core only):       {per_account_core:,}")
    print(f"per account (adjacent only):   {per_account_adjacent:,}")
    print(f"5 accounts (all included):     {per_account_all * ACCOUNTS:,}")
    print(f"5 accounts (core only):        {per_account_core * ACCOUNTS:,}")
    print(f"wrote {OUT}")
    print("excluded classes (reported separately in report/03):")
    for c in EXCLUDED_CLASSES:
        print(f"  - {c}")


if __name__ == "__main__":
    main()
