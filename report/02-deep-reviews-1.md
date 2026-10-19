# Deep reviews, part 1: Tavily, Exa, Firecrawl

Three providers whose free tiers are usable by an agent gateway without a credit
card. Each review states the exact allowance, what one unit buys, the observed
rate limit, and the measured success rate in the treg leaderboard capture.

All figures were read from the captured bodies listed under **Evidence** in each
section. Captures are dated 2026-10-19. A vendor can change a price without
changing its URL, so re-fetch before relying on a number. Every captured body
has a sha256 in `evidence/index.tsv`; the body files themselves are committed.

The leaderboard section in each review relies on a single 30-day capture of
`https://treg.to/web-arena/api/leaderboard`
(`evidence/seeds/002_treg.to_web-arena_api_leaderboard.body`,
`updated_at 2026-10-19T05:13:08.433480Z`). It is used as a measurement, not as a
vendor claim. Its limits are stated once in the report and apply to all three
reviews.

## How to read the credit arithmetic

A "credit" is not a request. Every provider below prices some operations above
one credit, so a monthly credit grant converts to a request count only after you
fix the operation mix. The tables give the per-operation cost so the conversion
can be done for a specific workload instead of a guessed average.

---

## 1. Tavily

**Role:** search API with an extraction and crawl layer, built for LLM agents.
**Category in `data/providers.tsv`:** search.

### Free tier

| Item | Value | Source |
|---|---|---|
| Monthly allowance | 1,000 API credits, every month | `api-credits.md` |
| Card required | No. Capture: "No credit card required." | `api-credits.md` |
| Paid entry | Project, 4,000 credits/month, $30 | `api-credits.md` |
| Pay-as-you-go | $0.008 per credit | `api-credits.md` |

Verbatim: "You get 1,000 free API Credits every month. **No credit card
required.**"

Note the plan name. The free tier is called **Researcher** in the plan table;
1,000 credits/month is the whole free tier, not a trial of a larger one.

### What one credit buys

| Operation | Cost | Effective free volume at 1,000 credits |
|---|---|---|
| Search, `basic` | 1 credit/request | 1,000 searches |
| Search, `advanced` | 2 credits/request | 500 searches |
| Extract, `basic` | 1 credit per 5 successful URLs | 5,000 URL extractions |
| Extract, `advanced` | 2 credits per 5 successful URLs | 2,500 URL extractions |
| Map, regular | 1 credit per 10 pages returned | 10,000 mapped pages |
| Map with `instructions` | 2 credits per 10 pages returned | 5,000 mapped pages |
| Crawl | map cost + extract cost | e.g. 10 pages, basic: 1 + 2 = 3 credits |
| Research, `mini` | 4 to 110 credits/request | 9 to 250 requests |
| Research, `pro` | 15 to 250 credits/request | 4 to 66 requests |

Failed extractions and failed map requests are not charged. A failed scrape
costs nothing.

The crawl example is the vendor's own: 10 pages at basic depth costs 1 credit
for mapping plus 2 for extraction, 3 total. Recompute per workload rather than
applying a single divisor.

Research is the expensive path. One `pro` request can consume a quarter of the
monthly free grant at the top of its range.

### Rate limits

| Scope | Development key | Production key |
|---|---|---|
| Default (`/search`, `/extract`, `/map`, polling) | 100 RPM | 1,000 RPM |
| `/crawl` | 100 RPM | 100 RPM |
| `/research` (task creation) | 20 RPM | 20 RPM |
| `/usage` | 10 per 10 minutes | 10 per 10 minutes |

Production keys require a paid plan or PAYGO enabled, so the free tier runs on
the development column: 100 RPM default, 100 RPM crawl, 20 RPM research. That
is 1.67 requests/second on the default path, and it is the binding constraint
long before 1,000 credits are exhausted in a burst.

A 429 carries `Retry-After` in seconds when present. The docs say to key retry
logic on the status and header, not on the message text.

### Measured behaviour

From the treg capture, search task, 30-day window:

| Metric | Value |
|---|---|
| Success rate | 87.2% |
| Runs | 2,865 |
| Median latency | 2,300 ms |
| Mean latency | 2,581 ms |
| Catalog price used | $0.016/call |
| Hit samples | 2,676 |

Fetch task:

| Metric | Value |
|---|---|
| Success rate | 75.1% |
| Runs | 12,758 |
| Median latency | 1,206 ms |
| Price unit | per result, $0.0032 |
| Hit samples | 11,843 |

Sitemap task: 78.1% success, 41 runs, $0.0016/page.

News task: 414 runs, success rate `null` in the capture (below the minimum
sample threshold the leaderboard applies), median 1,415 ms. Do not quote an
87% or any other number for news; the capture does not publish one.

The 87.2% search success rate is the lowest of the three providers reviewed
here and below Exa. It is also measured on 2,865 runs, so it is not a small
sample artifact. What the leaderboard does not say is which queries failed, so
the number is a rate for its query mix, not a promise about any one query.

### Cost per successful answer

At $0.008/credit, a basic search costs $0.008 nominal. At 87.2% success, the
cost per successful basic search is $0.008 / 0.872 = $0.00917. Advanced search
doubles that to $0.0183. The free tier's 1,000 credits buy 1,000 basic search
attempts, or about 872 successful ones at the measured rate, if every attempt
is a basic search and no credits go to extract, map, crawl or research.

### Fit for the gateway

Good. Broad operation coverage from one key (search, extract, map, crawl,
research), a documented credit table, and a free tier that renews. The
weaknesses are the development-key 100 RPM ceiling and the 87.2% measured
search success rate. For a gateway that retries on failure, the retry budget
must come out of the same 1,000 credits.

### Evidence

| URL | HTTP | sha256 (prefix) | Capture |
|---|---|---|---|
| `https://docs.tavily.com/documentation/api-credits.md` | 200 | `9fd68a155e9b59c0` | `evidence/alt3/001_...api-credits.md.body` |
| `https://docs.tavily.com/documentation/rate-limits.md` | 200 | `f3a9b50f90aea7eb` | `evidence/alt3/002_...rate-limits.md.body` |
| `https://docs.tavily.com/llms.txt` | 200 | `85e0cb8b7a9af6a4` | `evidence/.../docs.tavily.com_llms.txt.body` |
| `https://tavily.com/` | 200 | `1aa03285954989e7` | `evidence/raw/tavily/home.body` |
| `https://tavily.com/#pricing` | 200 | `676a3ead812df468` | `evidence/raw/tavily/pricing.body` |

Full hashes and paths are in `evidence/index.tsv`. Where a URL was fetched more
than once the index holds one row per capture; the newest `captured_utc` is the
one quoted here.

---

## 2. Exa

**Role:** neural and keyword web search with page contents, answer, monitors and
an agent API.
**Category in `data/providers.tsv`:** search.

### Free tier

| Item | Value | Source |
|---|---|---|
| Monthly grant | $10 in credits, resets on the 1st | `billing.md`, `pricing.md` |
| Onboarding bonus | One-time $10, first team only, does not expire | `billing.md` |
| Card required | No. Capture: "No payment method required." | `pricing.md` |
| Accumulation | None. Unused credit expires at the reset, balance never exceeds $10 | `billing.md` |
| Effective searches | "up to 2,500 Instant searches" per $10 | `pricing.md` |

Verbatim from `pricing.md`: "The Free Tier gives you \$10 in credits (up to
2,500 Instant searches) the day you sign up, and your free balance resets to
\$10 on the first of every month. No payment method required."

Three constraints matter operationally:

1. The monthly grant is per **first team**, not per API key. Creating a second
   team does not create a second grant.
2. Credits do not roll over. A quiet month loses the grant.
3. The first month holds $20 ($10 grant + $10 onboarding bonus), then $10.

The free tier excludes Exa Snapshot. That is a product limit, not a credit
limit, and it does not appear in the request arithmetic.

### What one credit buys

Rates are per 1,000 requests at $1 = 1 credit, so the table below converts the
published USD rate into requests per $10 grant.

| Operation | Published rate | Requests per $10 |
|---|---|---|
| `/search` `instant`, up to 10 results | $4 / 1k | 2,500 |
| `/search` `fast` or `auto`, up to 10 results | $7 / 1k | ~1,428 |
| `/search` `deep-lite`, `deep`, `deep-reasoning` | $12 to $15 / 1k | 666 to 833 |
| Each result above 10 | +$1 / 1k results | +10,000 results |
| AI page summaries | +$1 / 1k pages | +10,000 pages |
| `/contents` | $1 / 1k pages, per content type | 10,000 pages |
| `/answer` | $5 / 1k | 2,000 |
| `/monitors` | $15 / 1k | 666 |
| Agent, fixed effort `minimal` | $0.012/request | 833 |
| Agent, fixed effort `low` | $0.025/request | 400 |
| Agent, fixed effort `medium` | $0.10/request | 100 |
| Agent, fixed effort `high` | $0.50/request | 20 |
| Agent, fixed effort `xhigh` | $1.00/request | 10 |

The "up to 2,500" figure is the instant-search case at the base rate and with no
paid extras. A request that pulls page contents, or asks for more than 10
results, costs more. Deep search at $12 to $15 per 1k is three to four times
instant, so the same $10 buys 666 to 833 deep requests.

Metered agent runs bill actual usage against a per-run cap: $5 for `auto` and
$20 for `ultra`. A single `ultra` run at its cap would consume two monthly
grants, so the cap is not a free-tier-safe default.

### Rate limits

| Endpoint | Limit |
|---|---|
| `/search`, `/answer`, `/chat/completions` | 10 QPS |
| `/search` with `deep-lite`, `deep`, `deep-reasoning` | 5 QPS |
| `/contents` | 100 QPS |
| `/agent/runs`, `/responses` | 5 QPS, 50 active runs |
| `/websets/*` | 20 QPS |

Upgrade path: adding $1,000 in credits within any 30-day window raises the team
to 25 QPS for 90 days. That is irrelevant to a free tier but explains why
published benchmarks sometimes see higher throughput than a free key.

10 QPS is 600 requests/minute, roughly 6x Tavily's free development ceiling.
At 10 QPS a free account could in principle spend its 2,500 instant searches in
about 250 seconds. The credit grant, not the rate limit, is the binding
constraint for Exa.

### Measured behaviour

Search, 30-day window:

| Metric | Value |
|---|---|
| Success rate | 98.1% |
| Runs | 124,880 |
| Median latency | 1,627 ms |
| Mean latency | 2,099 ms |
| Catalog price used | $0.007/call |
| Hit samples | 104,241 |

Fetch:

| Metric | Value |
|---|---|
| Success rate | 89.1% |
| Runs | 116,613 |
| Median latency | 87 ms |
| Price | $0.001/page |
| Hit samples | 114,135 |

News: 99.4% success, 10,384 runs, median 508 ms.

Papers: 100% success, 497 runs, median 571 ms.

Search at 98.1% over 124,880 runs is the strongest search figure among the three
providers. Fetch at 89.1% is also the highest of the three. Median fetch latency
of 87 ms is an outlier in the right direction; the mean is 1,188 ms, so the
distribution has a long tail and the median flatters typical experience.

### Cost per successful answer

$10 / 2,500 instant requests = $0.004 nominal per request. At 98.1% success,
$0.004 / 0.981 = $0.00408 per successful instant search. That is cheaper per
successful search than Tavily basic ($0.00917) at the measured rates, though
the two run on different query mixes and the leaderboard does not equalise them.

### Fit for the gateway

Strong as a primary search backend. Highest measured success, the widest
latency headroom, and contents pricing at $1/1k pages. The limits are the small
grant, the no-rollover rule, and the first-team restriction. Deep search and
agent runs are expensive enough that a gateway should cap them separately from
basic search.

### Evidence

| URL | HTTP | sha256 (prefix) | Capture |
|---|---|---|---|
| `https://exa.ai/docs/admin/billing.md` | 200 | `694f5c2bc1b5c3db` | `evidence/alt3/004_...billing.md.body` |
| `https://exa.ai/docs/admin/pricing.md` | 200 | `66917065ca12363a` | `evidence/alt3/003_...pricing.md.body` |
| `https://docs.exa.ai/llms.txt` | 200 | `f0ae9e888a6df64f` | `evidence/.../docs.exa.ai_llms.txt.body` |
| `https://exa.ai/` | 200 | `585c49a7b62ab819` | `evidence/raw/exa/home.body` |
| `https://exa.ai/pricing` | 200 | `f5f999833a444f45` | `evidence/raw/exa/pricing.body` |

`https://exa.ai/websets` returned **429** during capture. It is not cited as a
source anywhere in this report.

---

## 3. Firecrawl

**Role:** crawl, scrape and search API that returns LLM-ready markdown.
**Category in `data/providers.tsv`:** crawl.

### Free tier

| Item | Value | Source |
|---|---|---|
| Monthly allowance | 1,000 credits, refreshed monthly | `pricing` |
| Card required | No | `pricing`, `rate-limits.md` |
| Concurrency | 2 browsers | `rate-limits.md`, `pricing` |
| Keyless access | Search, Scrape, Parse (MCP); plus Interact for official clients | `rate-limits.md` |
| Keyless cap | Per IP per day, on requests **and** credits | `rate-limits.md` |

Verbatim from the pricing page: "1,000 credits every month, refreshed monthly,
no credit card required."

This resolves an ambiguity in an earlier capture of the docs page, which said
"get 1,000 credits" without a period. The pricing page states the period
explicitly, so the row is `recurring`, not `one-time`.

Keyless access is a separate grant from the account grant. It is capped by IP
per day on two axes: request count and credit spend. The capture does not
publish the numeric caps for either axis. A gateway that rotates egress IPs
would change that cap in a way the docs do not quantify; do not model keyless
volume as a fixed number.

### What one credit buys

| Operation | Cost | Requests per 1,000 credits |
|---|---|---|
| Scrape | 1 credit/page | 1,000 pages |
| Crawl | 1 credit/page | 1,000 pages |
| Map | 1 credit/page | 1,000 pages |
| Monitor | 1 credit/page | 1,000 pages |
| Search | 2 credits per 10 results | 5,000 results (500 searches of 10) |
| Interact | 2 credits/browser-minute | 500 browser-minutes |
| JSON extraction, other advanced formats | Additional credits, amount not captured | - |
| Failed scrape (no result, or 4xx/5xx target) | Not charged | - |

The free tier's own description is "about 1,000 pages" or "500 searches". Those
two figures are the same 1,000 credits spent two ways, not additive.

Agent is in preview with 5 free daily runs and dynamic pricing. That is separate
from the 1,000-credit grant and the capture does not give its credit cost, so it
cannot be folded into the monthly arithmetic.

### Rate limits

Per plan, requests per minute:

| Plan | `/scrape` | `/map` | `/crawl` | `/search` | `/agent` | `/crawl/status` | `/agent/status` |
|---|---|---|---|---|---|---|---|
| Free | 10 | 10 | 2 | 10 | 2 | 500 | 500 |
| Hobby | 100 | 100 | 20 | 100 | 20 | 5,000 | 5,000 |
| Standard | 500 | 500 | 100 | 500 | 100 | 25,000 | 25,000 |
| Growth | 5,000 | 5,000 | 1,000 | 5,000 | 1,000 | 250,000 | 250,000 |
| Scale | 10,000 | 10,000 | 2,000 | 10,000 | 2,000 | 500,000 | 500,000 |

Concurrent browsers: Free 2, Hobby 5, Standard 25, Growth 50, Scale/Enterprise
100+. Max queued jobs on Free is 50,000.

The free tier's scrape ceiling of 10 RPM is the tightest of the three providers
reviewed here: 0.167 requests/second. At that rate, spending 1,000 scrape
credits takes about 100 minutes of continuous requests. The `/crawl` ceiling of
2 RPM is a separate and lower limit; a crawl request fans out to many pages, so
2 crawl jobs/minute with 2 concurrent browsers is the real throughput cap, not
the 10 RPM scrape figure.

Queued jobs time out against the request's `timeout` parameter, and the queue
itself can hold a job for up to 48 hours. A gateway that sets a short timeout
will drop jobs that the queue would eventually have run, so the timeout is a
cost decision, not only a latency one.

### Measured behaviour

Search, 30-day window:

| Metric | Value |
|---|---|
| Success rate | 99.8% |
| Runs | 9,604 |
| Median latency | 687 ms |
| Mean latency | 847 ms |
| Catalog price used | $0.01/call |
| Hit samples | 9,490 |

Fetch:

| Metric | Value |
|---|---|
| Success rate | 32.2% |
| Runs | 148,810 |
| Median latency | 2,085 ms |
| Price | $0.005/page |
| Hit samples | 138,138 |

Sitemap: 100% success, 188 runs, median 7,859 ms.

The split is stark. Search at 99.8% is the highest measured search success in the
capture. Fetch at 32.2% on 148,810 runs is the lowest fetch figure among the
three providers, and it is a large sample. A gateway should not treat Firecrawl
search quality as evidence about its fetch quality; they are different
pipelines and the capture measures them separately.

The capture does not say why fetch failed. Candidates include anti-bot blocking,
timeouts, and content-type handling, but none is tested here. State the figure
and the sample size, not a cause.

Sitemap median latency of 7,859 ms is roughly 4x search and 4x the other
providers' fetch medians. Sitemap is a long-running operation and should not sit
on a request path with a short deadline.

### Cost per successful answer

Search costs 2 credits per 10 results, so $0.01/call in the treg catalog is
consistent with 1 credit = $0.005. At 99.8% success, cost per successful search
is $0.01002. Fetch at $0.005/page and 32.2% success costs $0.0155 per
successful page, which is the worst of the three providers on that metric.

### Fit for the gateway

Use it for search and scrape where the output format matters, and do not rely on
it as the only fetch path. The free tier's 2 concurrent browsers and 2 RPM crawl
limit make it unsuitable for bulk crawling without a paid plan. The monthly
1,000 credits are real and renew, which makes it a safe default for low-volume
work.

### Evidence

| URL | HTTP | sha256 (prefix) | Capture |
|---|---|---|---|
| `https://docs.firecrawl.dev/rate-limits.md` | 200 | `cfd9035121bd0c06` | `evidence/alt3/007_...rate-limits.md.body` |
| `https://www.firecrawl.dev/pricing` | 200 | `b07ebd20a83fc0d2` | `evidence/raw/firecrawl/pricing.body` |
| `https://docs.firecrawl.dev/llms.txt` | 200 | `4765637fb7b7bf5d` | `evidence/.../docs.firecrawl.dev_llms.txt.body` |
| `https://www.firecrawl.dev/` | 200 | `47839d7a3f838724` | `evidence/raw/firecrawl/home.body` |

---

## Cross-provider summary

| | Tavily | Exa | Firecrawl |
|---|---|---|---|
| Free grant | 1,000 credits/month | $10 credits/month + $10 once | 1,000 credits/month |
| Card | No | No | No |
| Rolls over | n/a, use or lose | No | n/a, use or lose |
| Free-tier rate cap | 100 RPM dev | 10 QPS | 10 RPM scrape, 2 RPM crawl |
| Search success | 87.2% (2,865 runs) | 98.1% (124,880 runs) | 99.8% (9,604 runs) |
| Fetch success | 75.1% (12,758 runs) | 89.1% (116,613 runs) | 32.2% (148,810 runs) |
| Search median | 2,300 ms | 1,627 ms | 687 ms |
| Cheapest operation | $0.008/search basic | $0.001/page contents | 1 credit/page |

### Limits of this comparison

- **One capture, one query mix.** The leaderboard is a single 30-day window and
  does not publish the query set. Rates are comparable only as rates.
- **No independent bot-protection test was run.** The fetch success rates come
  from treg, a gateway that aggregates provider calls. They are not a controlled
  test of each provider against the same hostile pages.
- **Catalog prices are treg's, not the vendors'.** They are used only where they
  agree with a vendor-documented rate; Exa's $0.007 sits between its published
  $4 and $7 per 1k tiers, so it is a blended figure. Do not treat it as a price
  list.
- **Credits are not requests.** Converting a grant to requests requires the
  operation mix. Any single "requests per month" figure for these three is an
  assumption, and the assumption is stated wherever a figure appears.
- **Vendor pages change.** The sha256 in the index proves what was captured on
  2026-10-19, not what the page says now.
