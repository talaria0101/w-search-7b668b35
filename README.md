# Unified Web Fetch, Search and Crawl Gateway

A technical inventory, comparative benchmark, and reference gateway routing implementation across 100 web fetch, search, scraping, and crawling providers for autonomous AI agents.

## Core Capabilities and Architecture

This repository provides everything needed to deploy an unblocked, high-throughput web access gateway without requiring paid subscriptions or credit cards:

1. Exhaustive 100-Provider Inventory: Documented endpoints, home pages, pricing URLs, llms.txt documentation, quotas, cadences, credit card requirements, anti-bot mechanisms, rendering engines, and rate limits.
2. 8 Deep Technical Architecture Reviews: Focused reviews of Tinyfish, Keenable, Firecrawl, Jina AI, Tavily, Exa, Crawl4AI, and Serper.
3. 5 Post-Analyses:
   - 5-account capacity modeling (yielding 14.48 million requests per month).
   - Anti-bot bypass rankings across Cloudflare Turnstile, Datadome, Kasada, and Akamai.
   - One-time trial credits vs. monthly recurring allowances breakdown.
   - Market maturity and ecosystem adoption matrix.
   - Post-signup bonus triggers and credit expansion mechanics.
4. Runnable Reference Gateway (`gateway_router.py`): Zero-dependency Python implementation supporting multi-account rotation, fallback cascading, and unified `/v1/search` and `/v1/fetch` endpoints.
5. Machine-Readable Dataset (`providers.json`): Structured metadata across all 100 cataloged providers.

## High-Level Benchmark Metrics

| Metric | Measurement |
|---|---|
| Total Providers Evaluated | 100 verified services |
| Aggregate Monthly Volume (1 Account per Provider) | 2,897,475 requests per month |
| Aggregate Monthly Volume (5 Accounts per Provider) | 14,487,375 requests per month |
| Recurring Cadence (Monthly / Daily / Continuous / Sovereign) | 44 providers |
| One-Time Signup Trial Cadence | 56 providers |
| No Credit Card Required | 96 of 100 providers |
| Credit Card Verification Required | 4 providers (Brave, Bright Data, SOAX, Azure Bing) |
| Industrial Anti-Bot Bypass (Datadome/Kasada/Turnstile) | 28 providers |

## Top Standout Free Tiers for Autonomous Agents

| Provider | Primary Function | Free Quota | Cadence | No CC? | Best Used For |
|---|---|---|---|---|---|
| Tinyfish | Search & Fetch | 12k search/day + 1k fetch/day | Daily Resets | Yes | High-volume primary search & read layer |
| Keenable | Search & Fetch | 100k requests/month | Monthly | Yes | Bulk research and continuous indexing |
| Jina AI | Reader & Search | 1M tokens free + 20 RPM keyless | Recurring | Yes | Default single-page reader prefix |
| Crawl4AI | Deep Crawler | Unlimited (Open Source) | Unlimited | Yes | Local self-hosted Playwright crawling |
| Tavily | Research Search | 1k search credits/month | Monthly | Yes | Research-grade search with answer synthesis |
| Firecrawl | Scraper & Crawler | 1k credits/month (or unlimited local) | Monthly | Yes | Complex multi-page site mapping and LLM JSON |
| Serper | Google SERP | 2.5k queries on signup | One-Time | Yes | Ultra fast structured Google SERP results |
| Webscraping.ai | Anti-Bot Scraping | 2k requests/month | Monthly | Yes | Automated rotating proxy web scraping |
| Scrape.do | Residential Scraping | 1k requests/month | Monthly | Yes | Residential proxy unblocking of tough domains |
| Apify | Serverless Scrapers | $5 monthly platform credit | Monthly | Yes | Serverless actor execution and web monitoring |
| Spider.cloud | High-Speed Scraper | 500 pages free trial | One-Time | Yes | Ultra low latency Rust crawler core |
| ZenRows | Anti-Bot Bypass | 1k free credits | One-Time | Yes | Defeating strict Datadome and Kasada targets |
| Scrapfly | Anti-Scraping Bypass | 1k free credits | One-Time | Yes | Full Chrome DevTools session unblocking |

## Repository Structure

- `REPORT.md`: Comprehensive 2,900+ line technical report containing the master 100-provider catalog, 8 deep reviews, 5 post-analyses, and gateway architecture blueprints.
- `providers.json`: Full machine-readable catalog of all 100 providers with 16 structured metadata fields per provider.
- `gateway_router.py`: Runnable reference implementation of the unified gateway router.
- `LICENSE`: 0BSD License (public domain equivalent, zero restrictions).

## Quick Start: Running the Reference Gateway

The reference gateway router requires only Python 3 standard library:

```bash
# Verify the provider catalog and run self-test
python3 gateway_router.py --status

# Execute a search across the unified fallback ladder
python3 gateway_router.py --search "autonomous agent web gateways"

# Execute a clean page fetch across reader fallbacks
python3 gateway_router.py --fetch "https://example.com"
```

## License

This work is released under the 0BSD License. See `LICENSE` for details.
