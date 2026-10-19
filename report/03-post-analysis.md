# Post-analysis

Five analyses over the inventory in `data/providers.tsv` (127 rows) and the
finite-request subset in `data/analysis_a_units.tsv` (19 rows).

Every count below is produced by `scripts/build_post_analysis.py` into
`data/post_analysis_tables.tsv` and by `scripts/build_analysis_a.py` into
`data/analysis_a_totals.tsv`. Re-run both to reproduce. Numbers here are quoted
from those files, not counted by hand.

---

## (a) Total request volume if each provider had 5 accounts

### Method

Only providers whose free allowance is a documented **number of requests per
month** enter the sum. Everything else is excluded and named, because adding a
credit balance, a per-second rate limit or an uncapped API to a request total
would produce a number that means nothing.

Each included row is one entry in `data/analysis_a_units.tsv` with a category, a
class, a monthly request count, a basis and a source URL. `build_analysis_a.py`
refuses to run if any source URL is not a 200 or 202 in `evidence/index.tsv`, so
no row can cite a page that was never fetched.

The class split is deliberate:

- **core**: the provider itself answers web fetch, search or crawl requests.
  These are the providers the gateway would call directly.
- **adjacent**: the provider answers a different data question (Q&A, weather,
  news) that the gateway may also want, but it is not web fetch/search/crawl.

### Per-account and 5-account totals

| Scope | Requests/account | Requests for 5 accounts |
|---|---:|---:|
| All included | 759,821 | 3,799,105 |
| Core (web fetch/search/crawl) | 159,821 | 799,105 |
| Adjacent (data APIs) | 600,000 | 3,000,000 |

Source: `data/analysis_a_totals.tsv`.

### Where the volume comes from

| Category | Requests/account |
|---|---:|
| social (StackExchange) | 300,000 |
| weather (Open-Meteo) | 300,000 |
| search | 115,500 |
| fetch | 30,471 |
| news | 13,500 |
| serp | 300 |
| browser | 50 |
| **total** | **759,821** |

Two adjacent rows are 79% of the total. StackExchange (300,000/month, keyed) and
Open-Meteo (300,000/month, non-commercial) each contribute more than every core
provider combined (159,821). A core-only gateway would not see most of this
volume.

### The 19 included rows, by class

**Core (159,821/account):** Keenable 100,000; TinyFish 30,000; Currents 7,500;
Parallel 5,000; NewsAPI.org 3,000; Marketaux 3,000; Google Programmable Search
3,000; You.com 3,000; Exa 2,500; Tavily 1,000; Brave 1,000; AnyAPI 300; SerpApi
250; Microlink 100; Cloro 71; Zenserp 50; Anchor Browser 50.

**Adjacent (600,000/account):** StackExchange 300,000; Open-Meteo 300,000.

### Excluded classes

Named, with the reason each cannot be summed:

| Class | Why excluded |
|---|---|
| Credits not documented as 1:1 with requests | a credit may buy less than one request (Tavily advanced search = 2 credits), so credits are an upper bound, not a request count |
| One-time signup credits | not a monthly flow; counted separately in (c) |
| Trials | expire; not a recurring allowance |
| Rate limits only | requests/second is throughput, not a monthly budget |
| Uncapped / no published limit | no finite number to add |
| No free tier | zero |
| Self-hosted / library | no hosted quota applies |

### Assumptions

- 1 credit = 1 request **only** where the provider documents that rate. Where it
  does not, the row was excluded rather than guessed.
- USD bonuses are converted to requests at the captured per-request price.
- A "month" is 30 days. Providers using a calendar month are approximated.
- Rate limits are not treated as monthly allowances.
- Five accounts per provider is a **modelling multiplier**. It does not assert
  that five accounts are permitted by any provider. Most free tiers are one per
  person; a second account is a separate decision the inventory does not make.
- This is an **upper bound on request count**, not a quality-adjusted volume.
  Requests that fail, or that buy a worse answer, still count here.

**What would change it:** a provider documenting a different 1:1 rate, any free
tier changing its monthly grant, or a reviewer disputing a class assignment
(core vs adjacent). The class assignment is the softest input; the request
counts are captured.

---

## (b) Best results, and where fetching is hardest

### Source and its limits

`evidence/seeds/002_treg.to_web-arena_api_leaderboard.body`,
`updated_at 2026-10-19T05:13:08.433480Z`, 30-day window, cached and refusals
excluded. It is a gateway's aggregation of provider calls, not a controlled test.

**What it does not establish:** treg is not an anti-bot laboratory. Low fetch
success for a provider can mean the provider was blocked, or that it failed,
timed out, or returned an unusable body. The capture does not separate those
causes. Read the numbers as "how often a call through this provider produced a
usable result", not as a bot-defence score for the provider or for any target.

### Search, ordered by success rate

| Provider | Success | Runs | Median ms | Price |
|---|---:|---:|---:|---|
| firecrawl | 99.8% | 9,604 | 687 | $0.01/call |
| keenable | 99.1% | 14,814 | 841 | $0.004/call |
| exa | 98.1% | 124,880 | 1,627 | $0.007/call |
| olostep | 97.0% | 2,499 | 1,803 | $0.01/call |
| perplexity | 94.1% | 30,567 | 281 | $0.001/call |
| linkup | 94.1% | 704 | 1,603 | $0.055/call |
| serper | 89.5% | 536,710 | 1,415 | $0.001/call |
| tavily | 87.2% | 2,865 | 2,300 | $0.016/call |
| octen | 86.9% | 178 | 270 | $0.005/call |
| tinyfish | 86.8% | 565,677 | 1,715 | $0.0/call |
| crawl4ai | 84.8% | 157,937 | 1,661 | $0.00015/call |
| you | 79.2% | 834 | 586 | $0.005/call |
| branddev | 78.1% | 7,144 | 1,258 | $0.002534/call |
| scrapegraphai | 69.0% | 174 | 10,466 | $0.16/result |
| search1api | 51.8% | 15,303 | 4,668 | $0.001/call |
| parallel | 45.8% | 3,074 | 600 | $0.001/call |
| spidercloud | 35.4% | 15,061 | 3,591 | $0.001/call |
| diffbot | 32.0% | 100 | 162 | $0.001196/call |

### Fetch, ordered by success rate

| Provider | Success | Runs | Median ms | Price |
|---|---:|---:|---:|---|
| linkup | 100.0% | 14,572 | 1,620 | $0.01/call |
| exa | 89.1% | 116,613 | 87 | $0.001/page |
| tinyfish | 81.9% | 512,006 | 2,704 | $0.0/call |
| olostep | 79.6% | 29,205 | 6,055 | $0.002/call |
| tavily | 75.1% | 12,758 | 1,206 | $0.0032/result |
| serper | 67.0% | 522 | 1,179 | $0.01/call |
| branddev | 63.5% | 12,864 | 2,282 | $0.002534/call |
| scrapegraphai | 63.2% | 4,335 | 2,391 | $0.004/call |
| crawl4ai | 45.2% | 1,106,394 | 1,771 | $0.00015/page |
| you | 44.6% | 16,464 | 1,757 | $0.001/page |
| search1api | 41.7% | 27,375 | 5,001 | $0.001/call |
| anyapi | 37.3% | 115,453 | 3,581 | $0.0009/call |
| firecrawl | 32.2% | 148,810 | 2,085 | $0.005/page |
| parallel | 26.6% | 4,843 | 4,194 | $0.001/page |
| keenable | 17.8% | 4,755 | 345 | $0.004/call |

### Maps

dataforseo 100% (345,748 runs), serpapi 100% (5,350), apify 91.8% (2,362).

### Reading

- **Best search:** firecrawl (99.8%), keenable (99.1%), exa (98.1%). Exa's figure
  rests on 124,880 runs; firecrawl's on 9,604; keenable's on 14,814. All three
  are strong samples.
- **Best fetch:** linkup (100%, 14,572 runs), exa (89.1%, 116,613 runs), tinyfish
  (81.9%, 512,006 runs). Tinyfish's sample is the largest in the table and its
  fetch success is among the highest, which is a stronger result than a small
  perfect sample.
- **Where fetching breaks down:** keenable 17.8%, parallel 26.6%, firecrawl
  32.2%, anyapi 37.3%, on samples from 4,755 to 148,810. Firecrawl's gap between
  99.8% search and 32.2% fetch is the widest in the capture and argues against
  using one provider's search quality as a proxy for its fetch quality.
- **Latency:** search medians span 162 ms (diffbot) to 4,668 ms (search1api).
  Fetch medians span 87 ms (exa) to 6,055 ms (olostep). The spread is large
  enough that latency, not success rate, decides some gateway designs.
- **Free-tier relevance:** tinyfish search at $0.0/call and 86.8% over 565,677
  runs is the strongest free-price result in either table.

Caveat repeated: none of this is a bot-protection test. A controlled test would
call each provider against the same fixed set of hostile pages with the same
timeouts, which was not done here.

---

## (c) One-time credits versus monthly credits

Counts from `data/post_analysis_tables.tsv` (all 127 rows):

| `credit_kind` | Rows | Meaning |
|---|---:|---|
| recurring | 69 | a monthly allowance that renews |
| one-time | 20 | signup credit, granted once |
| trial | 12 | time-limited |
| none | 11 | paid only, no free tier |
| dup | 10 | alias of another row |
| unknown | 5 | page unreachable or allowance not published |

### One-time rows (20)

Jina Reader/Search (10M tokens/key); Crawlbase (up to 5,000); Hyperbrowser
(5,000 credits); ScrapingBee (1,000); Scrapfly (1,000); Serper (2,500 queries);
ScrapeBadger (1,000); ScrapeGraphAI (500); Search1API (100); SearchApi.io (100);
Browserbase (1,000 search + 1,000 fetch + $5 model tokens); Steel.dev ($30);
NewsCatcher (2,000); Scrapingdog (100); Octen ($5 balance); Valyu ($10, $20 with
work email); Linkup (4,000 queries); Notte ($10); LiteScrape (5 calls); Talordata
(500 SERP responses).

A one-time credit is a fixed pool. It does not refill, so its value is a single
integration and test budget, not a standing allowance. For a long-running
gateway these rows matter less than the 69 recurring ones.

### Trial rows (12)

Serply (2,500 credits, 30 days); DataForSEO ($1 trial + sandbox); Oxylabs ($5);
Zyte ($5); HasData (~1,000); ScraperAPI (7-day + 5,000 credits); Olostep (500
requests); Serpent API (~$1); Serp House (4,000 credits/month trial);
Serpstat (limited free tier + 7-day trial); Urlbox (7-day trial); Core.ac.uk
(30-day trial).

Trials are worse than one-time credits for a permanent gateway: they expire on a
clock as well as on spend.

### The distinction that matters

- **recurring + one-time:** Tavily, Exa, Context.dev and Jina combine a monthly
  grant with a signup bonus. Those are the rows to prefer.
- **recurring only:** the 69 minus that overlap.
- **one-time or trial only:** 32 rows. Usable to evaluate a provider, not to run
  it.

---

## (d) Maturity, popularity and market awareness

Counts from `data/post_analysis_tables.tsv`:

| `maturity` | Rows |
|---|---:|
| established | 56 |
| emerging | 36 |
| niche | 16 |
| major | 15 |
| unknown | 4 |

This is a **hand-assigned judgement**, not a measurement. There is no captured
popularity metric (no traffic, revenue, funding or user counts) behind any row.
Treat the label as a reading of the provider's public profile at capture time.

- **major**: large companies with broad market awareness: Semrush, Perplexity,
  OpenAI Web Search, Anthropic Web Search, xAI Live Search, DeepSeek Search,
  Google Gemini Grounding, Google Gemini, Google AI, Wikipedia API, Wikidata,
  Perplexity Sonar, GitHub REST API, PyPI JSON API, npm registry API.
- **established**: well-known vendors with a settled product: Diffbot, You.com,
  Brave, Exa, Tavily, Firecrawl, Bright Data, Oxylabs, Zyte, ScrapingBee and
  similar.
- **emerging**: newer entrants: Parallel, TinyFish, LangSearch, Kernel, Anchor
  Browser, Notte, Steel.dev and similar.
- **niche**: small or single-purpose: Marginalia, Mwmbl, YaCy, 4get, Talordata,
  ProxiesAPI and similar.

### What the label is and is not

It is: a claim about public profile, useful for sorting a "try these first" list.

It is not: a quality score. Firecrawl is `established` and has the highest
search success in the capture. Diffbot is `established` and has the lowest search
success. Maturity and measured performance do not correlate in this data.

### Where awareness does help

`major` rows are mostly `none` for a free tier (Semrush, Ahrefs, Perplexity,
Anthropic, xAI, DeepSeek). The pattern is that the highest-profile commercial
search APIs do not offer a free tier, while the `established` and `emerging`
rows below them mostly do. For a no-card gateway this is the useful reading of
the maturity column: the free allowance lives in the second tier.

---

## (e) Post-signup bonuses

Every row with a non-empty `signup_bonus`, from `data/post_analysis_tables.tsv`:

| Provider | Bonus |
|---|---|
| Parallel | Up to $80 at signup + $5/mo credits; up to $250 startups |
| Apify | $500 for 6 months (new) |
| Linkup | $5,000 credits for startups (application) |
| Exa | $10 onboarding (one-time, first team) |
| You.com | $100 credit |
| Context.dev | 10K Logo Link requests |
| Jina Reader/Search | 10M tokens |
| TinyFish | Get $8 free |
| Valyu | $20 with work email |
| Diffbot | Students get Startup tier free |

Count: **10 rows**.

### Work-email bonus

**Valyu** is the only row where a work email changes the bonus: $10 default, $20
with a work email. No other captured page offered a bonus conditional on email
domain.

### Card-required bonuses

Card requirement is `unknown` for 16 rows and `yes` for 13. The 13 `yes` rows are
almost all `none` or `unknown` free tiers (Semrush, Ahrefs, Kagi, Mojeek,
Perplexity, OpenAI, Anthropic, xAI, DeepSeek, Google AI, Mistral Web Search,
Perplexity Sonar, a serpapi alias): they require a card because they have no free
tier at all. No row offers a signup bonus *in exchange for* a card within the
free tier.

`unknown` is 16 rows whose page did not state a card requirement. Those are not
"no card"; they are unverified.

### Newsletter bonus

**None captured.** No fetched pricing or signup page offered a credit in
exchange for a newsletter signup. This is an empty result, not an omission: the
pricing and docs captures for all 127 rows were searched and none contained a
newsletter-for-credits term. If a provider offers one behind a signup modal that
requires an account to see, this inventory would not see it either.

### Other notable bonuses

- **Parallel:** the largest cash onboarding in the set, up to $80, plus $5/month.
- **Exa:** $10 onboarding on top of the $10 monthly grant, first team only.
- **You.com:** $100 credit, worth 20,000 searches at the captured $5/1k rate.
- **Jina:** 10M tokens per new key.
- **Context.dev:** 10K Logo Link requests, a separate product allowance rather
  than cash.

Bonus figures are as captured on 2026-10-19 and are the vendor's claims. None was
redeemed or verified against a live account here.
