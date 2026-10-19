# Deep Technical Reviews: 10 Free-Tier Providers

This file reviews ten providers from the free-tier inventory pass: ZenRows,
ScrapingAnt, Bright Data, Context.dev, Crawlbase, Hyperbrowser, Browserless,
ScrapingBee, Scrapfly and Serply. Each review answers four questions: what the
free tier actually grants, what one credit buys, what limits throughput, and
what the API surface looks like.

Every figure comes from a captured HTTP response, not from memory or from a
vendor summary written second-hand. The captures were taken on 2026-10-19 at
05:58:21Z. Each section ends with an evidence table giving the URL, HTTP status,
byte count, full sha256 and capture path. The same rows are in
`evidence/index.tsv`; paths there are relative to `evidence/`.

The reviews do not rank providers by claimed quality. There is no common
benchmark in this set, so there is no measured success rate to compare. Where a
vendor states its own performance, the number is labelled VENDOR CLAIM.

## How to read the credit arithmetic

A credit is a vendor-defined unit. Comparing credit counts across providers is
meaningless until each is converted to a common operation, usually one
successful fetch of a standard page with no JavaScript rendering, no premium
proxy and no screenshot. This file does that conversion per provider and states
the operation it assumed.

Three things break the conversion, and each is called out where it applies:

1. The provider does not publish a credit-to-operation mapping. Bright Data is
   in this category: it publishes list prices per product but not how many
   credits an operation consumes.
2. The free grant is one-time rather than monthly. A one-time grant is a
   reserve, not recurring capacity.
3. The binding limit is concurrency or a per-minute request cap, not credits. A
   large credit pool behind one concurrent request is not usable for burst
   work.

Failed-request policy is part of the arithmetic. A provider that bills only
successful requests has a different effective cost from one that bills every
attempt, even at the same nominal credit price.

---

## 1. ZenRows

**Role:** general unblocker with JavaScript rendering and premium proxies.

**Category in `data/providers.tsv`:** `unblocker`, score 94.

### Free tier

| item | value | capture |
|---|---|---|
| allowance | 5,000 credits/month, always | Z2 |
| kind | recurring, monthly refresh, no rollover | Z2 |
| credit card | not required | Z2 |
| free concurrency | 5 concurrent requests | Z2 |
| exclusions | standalone Residential Proxies are not unlocked | Z2 |

The free plan is described as permanent, not a trial: "Free plan 5,000
credits/month, always. No card, every primitive unlocked." The only exclusion
is standalone residential proxies. The plan refreshes monthly and unused
credits do not roll over.

### What one credit buys

| operation | credits | 5,000 credits buys |
|---|---|---|
| standard page | 1 | 5,000 pages |
| page with JavaScript rendering | 5 | 1,000 pages |
| page with premium proxies | 10 | 500 pages |
| page with JavaScript and premium proxies | 25 | 200 pages |
| residential bandwidth | 25,000 per GB | 0.2 GB |
| browser time | 5 per minute | 1,000 browser-minutes |

Extract is free on top of the Fetch request it uses. Batch bills at the same
per-request rate as Fetch. A 404 or 410 counts as a result and is not charged,
so a failed request costs zero credits.

The practical reading: the headline 5,000 is 5,000 plain fetches, but the same
pool is 1,000 rendered pages or 500 premium-proxy pages. A gateway that sends
every request through JavaScript rendering turns a 5,000-credit month into a
1,000-request month.

### Rate limits and concurrency

Concurrency is published per plan:

| plan | price | monthly credits | concurrent requests |
|---|---|---|---|
| Free | $0 | 5,000 | 5 |
| Build | $16/mo | 45,000 | 20 |
| Launch | $58/mo | 250,000 | 50 |
| Growth | $166/mo | 1,200,000 | 100 |
| Scale | $458/mo | 5,000,000 | 200 to 400 |
| Enterprise | custom | custom | 500 to 1,000+ |

No requests-per-minute figure appears in the captures. Concurrency is the only
published throughput limit.

### API surface

- Fetch and Extract: `GET https://api.zenrows.com/v1/` with the API key as the
  `apikey` query parameter. The home page shows a working example:
  `https://api.zenrows.com/v1/?url=...&apikey=...&response_type=markdown`.
- Crawl: `POST https://api.zenrows.com/v1/crawls`.
- Batch: `https://async.api.zenrows.com/v1`.
- Browser Sessions: connect Puppeteer or Playwright over WebSocket.
- Outputs: JSON, Markdown, plain text, PDF, screenshot, CSS extraction.
- The OpenAPI 3.1 document is published at `https://www.zenrows.com/openapi.json`.

### Measured behaviour

No measured success rate is available for ZenRows in this set. The treg
leaderboard capture (`evidence/seeds/002_treg.to_web-arena_api_leaderboard.body`)
contains no entry for ZenRows, and no live request was made against the API.
See "Limits of this comparison" at the end of this file.

### Cost per successful answer

Free tier: $0 for 5,000 standard pages per month, or 1,000 rendered pages, or
500 premium-proxy pages, or 200 with both.

Paid marginal cost per credit, from the plan table:

| plan | $/credit | $/standard page | $/rendered page |
|---|---|---|---|
| Build | 0.000356 | 0.000356 | 0.00178 |
| Launch | 0.000232 | 0.000232 | 0.00116 |
| Growth | 0.000138 | 0.000138 | 0.000692 |
| Scale | 0.000092 | 0.000092 | 0.000458 |

These are list prices divided by included credits. They exclude top-up pricing
and any committed-capacity discount.

### Fit for the gateway

ZenRows is the strongest recurring free unblocker in this set because the grant
is monthly and card-free. Route standard fetches here first and escalate to
rendering only when a fetch returns a challenge or empty content. The free
concurrency of 5 caps parallel work, so a gateway should queue behind it rather
than open more than five connections. Do not spend premium-proxy credits on
pages that resolve with a plain fetch.

### Evidence

| id | url | HTTP | bytes | sha256 | capture |
|---|---|---|---|---|---|
| Z1 | https://www.zenrows.com/ | 200 | 146009 | `7b48a2a7ae4033039427a9cfbb98afd10c4ce35fc2ac1988a8a94216b09a8368` | `raw/zenrows/home.body` |
| Z2 | https://www.zenrows.com/pricing | 200 | 113965 | `bb3e330505afdcaf3ed268b3f39b7f1235a9d2b00e1bf57026adbe8389a09294` | `raw/zenrows/pricing.body` |
| Z3 | https://docs.zenrows.com/llms.txt | 200 | 25503 | `fd100148170f4ca87fa80e3333d54d157f67e6b860c742cc1dd2026a6bbda363` | `raw/zenrows/docs.body` |

---

## 2. ScrapingAnt

**Role:** unblocker with headless Chrome rendering and rotating proxies.

**Category in `data/providers.tsv`:** `unblocker`, score 93.

### Free tier

| item | value | capture |
|---|---|---|
| allowance | 10,000 credits/month | S1 |
| kind | recurring, monthly | S1 |
| credit card | not required | S1 |
| free concurrency | no cap on any plan | S1 |
| default request cost | 10 credits | S1 |

The home page states the grant twice: "10,000 free credits every month, no
credit card" and "10,000 free credits every month, no credit card required".
The FAQ repeats it: "No. The free plan includes 10,000 API credits every month
with no credit card required."

The pricing page and `llms.txt` both return HTTP 404. Both 404 responses are
the same 43,937-byte document with the same sha256, so the per-option credit
table beyond the default cannot be cited from this capture set.

### What one credit buys

The only published multiplier in the capture is a range plus a default: "Most
requests cost between 1 and 25 credits depending on the options you enable
(proxy type, JavaScript rendering, etc.). The default request, Chrome rendering
with standard proxies, costs 10 credits."

| operation | credits | 10,000 credits buys |
|---|---|---|
| default Chrome rendering, standard proxies | 10 | 1,000 requests |
| cheapest listed option | 1 | 10,000 requests |
| most expensive listed option | 25 | 400 requests |

The exact mapping from option to multiplier is not in the capture, because the
pricing page is a 404. Any figure between 1,000 and 10,000 requests per month is
consistent with the text, and the default case is 1,000.

### Rate limits and concurrency

The home page is explicit: "No concurrency cap on any plan" and "Unlimited
parallel requests." The same section says the cluster auto-allocates Chrome
instances per request. No requests-per-minute figure appears in the capture.

This is the unusual property in the set: the free tier is not throughput-capped
by concurrency. The practical cap is the credit pool, and the default request
consumes ten of it.

### API surface

- General endpoint: `https://api.scrapingant.com/v2/general`, with the key in an
  `x-api-key` header.
- MCP server: `https://api.scrapingant.com/mcp`, same header. It exposes three
  tools: `get_web_page_html`, `get_web_page_markdown` and `get_web_page_text`.
- MCP usage draws from the same API credit pool as direct calls.
- The `docs.scrapingant.com` host appears in the home page links, but that host
  was not captured; the captured documentation URL (`/llms.txt`) is a 404.

### Measured behaviour

No measured success rate is available. ScrapingAnt has no entry in the treg
leaderboard capture, and no live request was made against the API.

### Cost per successful answer

Free tier: 10,000 credits per month, which is 1,000 default Chrome-rendered
requests. At the cheapest option it is 10,000 requests, and at the most
expensive it is 400.

Paid cost cannot be computed from this capture set: the pricing page is a 404,
so the paid plan volumes behind the `$19/mo` entry in `data/providers.tsv`
cannot be verified here.

### Fit for the gateway

ScrapingAnt is the best burst lane among the ten because it publishes no
concurrency cap. Its default request includes Chrome rendering, so it is a
natural escalation target when a plain fetch fails. The caveat is economic: ten
credits per default request means the 10,000-credit month is 1,000 requests, not
10,000. Keep it off the hot path for plain pages and use it for pages that need
a browser.

### Evidence

| id | url | HTTP | bytes | sha256 | capture |
|---|---|---|---|---|---|
| S1 | https://scrapingant.com/ | 200 | 141192 | `19d442fda79a4152cdc7a94932425307eda016c8e644dd9634e60dac433788b3` | `raw/scrapingant/home.body` |
| S2 | https://scrapingant.com/pricing | 404 | 43937 | `2ca1354a7cebf649cf16ba1bcf8ea7e12ebda46f06ff5792e42646204f276ebb` | `raw/scrapingant/pricing.body` |
| S3 | https://scrapingant.com/llms.txt | 404 | 43937 | `2ca1354a7cebf649cf16ba1bcf8ea7e12ebda46f06ff5792e42646204f276ebb` | `raw/scrapingant/docs.body` |

---

## 3. Bright Data

**Role:** unblocker and data-collection platform with separate products for
Web Unlocker, SERP, Scraper APIs, Browser API, datasets and proxy
infrastructure.

**Category in `data/providers.tsv`:** `unblocker`, score 90.

### Free tier

| item | value | capture |
|---|---|---|
| allowance | 5,000 credits/month | B3 |
| kind | recurring, monthly | B3 |
| credit card | not required | B3 |
| products covered | Web Unlocker, SERP, Scraper API, Scraper Studio | B3 |
| free concurrency | not published in captures | none |

The docs state: "New accounts get 5,000 free credits per month" and the free
tier entry says "5,000 free credits per month across Web Unlocker API, SERP API,
Scraper API and Scraper Studio, no credit card required."

This contradicts the repository root's summary that Bright Data requires card
verification. The capture is the artefact and it says no card required. The
discrepancy is recorded at the end of this file.

### What one credit buys

The captures do not contain a credit-to-operation mapping. The pricing page
publishes unit prices per product instead:

| product | list price | capture |
|---|---|---|
| Unlocker API | from $1 per 1,000 requests | B2 |
| Crawl API | from $1 per 1,000 requests | B2 |
| SERP API | from $1 per 1,000 requests | B2 |
| Browser API | from $5 per GB | B2 |
| Scraper APIs | from $0.75 per 1,000 records | B2 |
| Scraper Studio | from $1 per 1,000 requests | B2 |
| Datasets | from $250 per 100,000 records | B2 |
| Data Firehose | from $0.2 per 1,000 HTML | B2 |
| Residential proxies | from $2.50 per GB, 50% off $5 | B2 |
| Datacenter proxies | from $0.90 per IP | B2 |
| ISP proxies | from $1.30 per IP | B2 |

Because the credit-to-operation ratio is absent, 5,000 credits cannot be
converted to a request count from published text. Stating "5,000 requests" or
"5,000 fetches" would be an invention.

### Rate limits and concurrency

No numeric rate limit appears in the captures. The docs index links a page
titled "SERP API rate limits" at
`https://docs.brightdata.com/general/usage-monitoring/serp-rate-limit.md`, but
that page is not in this capture set.

The docs do state the zone model: SERP API, Web Unlocker API and Browser API
each require a zone, passed as the `zone` parameter for SERP and Web Unlocker
and as zone credentials for Browser. The Scraper API needs no zone when the SDK
is called with `auto_create_zones=False`.

### API surface

- Authentication: `Authorization: Bearer YOUR_API_KEY` on every request.
- Products are addressed separately: Web Unlocker, SERP, Scraper API, Scraper
  Studio, Browser API, datasets, proxy infrastructure.
- Official SDK: `pip install brightdata-sdk`, with calls shaped as
  `client.scrape.<platform>.<method>(url=...)`.
- A CLI, agent skills and an MCP server are listed in the docs index.
- The captures name the auth scheme and zone model but do not include a concrete
  request URL for the Unlocker endpoint. That detail is in the API reference
  pages, which were not captured.

### Measured behaviour

No measured success rate is available. Bright Data has no entry in the treg
leaderboard capture, and no live request was made against the API.

### Cost per successful answer

Unknown for the free tier. The 5,000 credits cannot be converted to operations
without the missing mapping.

At list price, a Web Unlocker request starts at $0.001 and a SERP request at
$0.001. Those are prices per request, not a credit conversion, and they are the
floor of a "starts from" range rather than a fixed rate.

### Fit for the gateway

Do not place Bright Data in a routing table until its credit mapping is
measured. The 5,000-credit grant is real and monthly, but without a mapping the
gateway cannot budget requests against it. A single controlled run of known
operations would settle the conversion; that run is not part of this static
review.

### Evidence

| id | url | HTTP | bytes | sha256 | capture |
|---|---|---|---|---|---|
| B1 | https://www.brightdata.com/ | 200 | 283747 | `07ab758a877476e6be0e7c14360348bc5593c9fbbe83e5aed99902f513ea432c` | `raw/bright_data/home.body` |
| B2 | https://brightdata.com/pricing | 200 | 234123 | `f77cb84228202dcb944a4bdef92d80a081a1405fe3cbe231a7ede8d17952c6aa` | `raw/bright_data/pricing.body` |
| B3 | https://docs.brightdata.com/llms.txt | 200 | 17161 | `6eebabce5484c33d19175eb7717fcd35174736ebfca39f8c6c9e29ca8c5245c6` | `raw/bright_data/docs.body` |

---

## 4. Context.dev

**Role:** fetch and scrape API with Markdown, HTML, screenshots, structured
extraction, brand data and web answers.

**Category in `data/providers.tsv`:** `fetch`, score 87.

### Free tier

| item | value | capture |
|---|---|---|
| allowance | 1,000 credits/month | C2 |
| one-time extra | 10,000 Logo Link requests | C2 |
| kind | recurring, monthly | C2 |
| credit card | not required | C2 |
| concurrency | 2 concurrent requests | C2 |
| request rate | 10 requests per minute | C2 |
| batches | 1 concurrent batch | C2 |
| monitors | 10 | C2 |

The pricing page says "1,000 credits per month" and "2 concurrent, 10 req/min".
The FAQ confirms the free tier renews: "The Free plan includes 1,000 API
credits that renew every month."

### What one credit buys

| operation | credits | 1,000 credits buys |
|---|---|---|
| standard scrape | 1 | 1,000 pages |
| scrape with browser actions | 2 | 500 pages |
| scrape with successful JSON extraction | 5 | 200 pages |
| Highlights or Product add-on | +1 | varies |
| PDF OCR | +1 per recovered page | varies |
| Brand or Styleguide | 10 | 100 lookups |
| Answers, Fast mode | 10 | 100 answers |
| Answers, Ultra mode | 100 | 10 answers |
| web or news search | 1 per 10 results | 10,000 results |
| People search | 20 per match | 50 matches |

Billing on failure is nuanced: most failed requests are not billed, but 404
responses are billed at the request's base price. A scrape can return HTTP 200
with failed outputs, and it charges when at least one output succeeds or the
target page is missing.

### Rate limits and concurrency

Free: 2 concurrent requests, 10 requests per minute, 1 concurrent batch.

Paid concurrency, from the same FAQ: Developer 10, Pro 100, Growth 250, Scale
500. Paid plans have no per-minute cap by default. The 10 requests per minute
is specific to new free accounts.

### API surface

- Scrape: `POST https://api.context.dev/v1/web/scrape` with
  `Authorization: Bearer YOUR_API_KEY`.
- Other endpoints visible in the home capture:
  `/v1/web/answers`, `/v1/web/urls`, `/v1/web/styleguide`,
  `/v1/brand/retrieve`, `/v1/batch/submit`, `/v1/monitors`.
- Outputs: Markdown, HTML, screenshots, images, raw bytes, custom CSS parsers
  and prebuilt parsers for Maps, app stores, Instagram, TikTok and reviews.
- Official SDKs: TypeScript, Python, Ruby, Go, PHP.

### Measured behaviour

No measured success rate is available. Context.dev has no entry in the treg
leaderboard capture, and no live request was made against the API.

The home page states a "99.96% Scrape success rate". That is a VENDOR CLAIM. It
is not a measurement from this set.

### Cost per successful answer

Free tier: 1,000 standard scrapes per month, or 500 with browser actions, or 200
with JSON extraction.

Paid marginal cost per credit:

| plan | price | included credits | $/credit | $/standard scrape | $/JSON scrape |
|---|---|---|---|---|---|
| Developer | $19/mo | 7,500 | 0.002533 | 0.002533 | 0.01267 |
| Pro | $99/mo | 125,000 | 0.000792 | 0.000792 | 0.00396 |

Overage is $2.20 per 1,000 credits on Developer and $1.80 per 1,000 on Pro.

### Fit for the gateway

Context.dev is the best structured-extraction lane in this set, because the
operation prices are published exactly and JSON extraction has a known
multiplier. It is not a burst lane: 2 concurrent requests and 10 requests per
minute make it a background queue. Use it when the caller needs Markdown plus
schema-bound fields, or a brand lookup, not for bulk plain fetches.

### Evidence

| id | url | HTTP | bytes | sha256 | capture |
|---|---|---|---|---|---|
| C1 | https://context.dev/ | 200 | 1230720 | `b551372530ccb23e79e0cad7b20ae8138bb65164d078b29e0b75a6540317f3f2` | `raw/context.dev/home.body` |
| C2 | https://context.dev/pricing | 200 | 465063 | `8b3ee3c36746dae20368e90bff38107ba5d9eb9c6db04e8d32e9ecfb2a69558b` | `raw/context.dev/pricing.body` |
| C3 | https://docs.context.dev/llms.txt | 200 | 30666 | `01e2fcb8ec321548e2fccee88c40482dfae7f9c55884ca04d89a79e02c202345` | `raw/context.dev/docs.body` |

---

## 5. Crawlbase

**Role:** unblocker with a graduated pay-as-you-go rate card, site-difficulty
multipliers and a shared credit balance across four products.

**Category in `data/providers.tsv`:** `unblocker`, score 82.

### Free tier

| item | value | capture |
|---|---|---|
| base allowance | 1,000 credits on signup | K2 |
| maximum after setup | up to 5,000 credits | K2 |
| kind | one-time, not monthly | K2 |
| credit card | not required | K2 |
| free concurrency | not published in captures | none |

The pricing page says "Up to 5,000 requests free" and "Every new account starts
with 1,000 free credits and no card on file, and completing setup steps grows
that to up to 5,000." The credits work across every product. They are a signup
grant, not a monthly reset.

### What one credit buys

| operation | credits | 5,000 credits buys |
|---|---|---|
| standard request | 1 | 5,000 requests |
| JavaScript rendering | x2 | 2,500 requests |
| cloud storage, one page for one month | 0.5 | 10,000 page-months |
| full-page screenshot through Crawling API | 2 | 2,500 screenshots |
| site tier Standard | x1 | 5,000 requests |
| site tier Moderate | x1.5 | 3,333 requests |
| site tier Complex | x2 | 2,500 requests |
| site tier Complex I | x3 | 1,666 requests |
| site tier Complex II | x4.5 | 1,111 requests |
| site tier Extreme | x9 | 555 requests |
| site tier Extreme I | x13.5 | 370 requests |
| site tier Extreme II | x20 | 250 requests |

JavaScript rendering doubles any site tier. A site at Extreme II with rendering
therefore costs 40 credits per request, or 125 requests on a 5,000-credit
grant. The multipliers are applied automatically, so the caller does not choose
the tier.

Only successful requests are billed. A request that fails or is blocked costs
nothing.

### Rate limits and concurrency

No numeric rate limit appears in the captures. The docs index links a page at
`https://crawlbase.com/docs/rate-limits`, but that page is not in this capture
set. Concurrency is also not stated.

### API surface

- API host: `https://api.crawlbase.com`, from the site's own JavaScript config
  (`NS.apiHost`).
- Authentication is by token. The home page says "You send a URL to the API with
  your token." The authentication page is linked from the docs index but was not
  captured, so the exact parameter name is not in this set.
- Products sharing the balance: Crawling API, Enterprise Crawler, Smart AI
  Proxy, Cloud Storage.
- An MCP server is listed in the docs index.

### Measured behaviour

No measured success rate is available. Crawlbase has no entry in the treg
leaderboard capture, and no live request was made against the API.

### Cost per successful answer

Free tier: up to 5,000 one-time credits, which is 5,000 standard requests or
2,500 rendered requests, falling to 250 requests at the Extreme II tier.

Paid rate card, per 1,000 successful requests:

| bracket | rate per 1,000 |
|---|---|
| first 1,000 | $3.00 |
| next 10,000 | $2.00 |
| next 100,000 | $0.60 |
| next 1,000,000 | $0.50 |
| next 10,000,000 | $0.10 |
| next 100,000,000 | $0.05 |
| next 1,000,000,000 | $0.04 |
| beyond | $0.02 |

The ladder is progressive, like income tax, so each bracket applies only to the
volume inside it. The page's own worked example checks out: 100,000 standard
requests cost 1,000 x $3.00/1,000 + 10,000 x $2.00/1,000 + 89,000 x $0.60/1,000
= $3.00 + $20.00 + $53.40 = $76.40, which matches the page's stated $76.40.

### Fit for the gateway

Crawlbase is a low-volume standard-page lane. Its free grant is one-time, so it
does not contribute recurring capacity. The difficulty multipliers make heavily
defended sites expensive without warning, which argues against using it as a
fallback for unknown targets. It is a reasonable paid overflow lane once volume
passes the first bracket, because the blended rate falls quickly.

### Evidence

| id | url | HTTP | bytes | sha256 | capture |
|---|---|---|---|---|---|
| K1 | https://crawlbase.com/ | 200 | 144354 | `1eac7c54554db57e1bbd95e7a65e8dfa630fc340c87aba2f73f9722f83da2de9` | `raw/crawlbase/home.body` |
| K2 | https://crawlbase.com/pricing | 200 | 70318 | `77f45f5675e777fdca6f2b5867c1b50701dd435bd0c07fab5296b21c3b080201` | `raw/crawlbase/pricing.body` |
| K3 | https://crawlbase.com/llms.txt | 200 | 49573 | `08db8480a17b474d4330d7d29d7ca594602ff95f61c58241c4316db5e501f1c5` | `raw/crawlbase/docs.body` |

---

## 6. Hyperbrowser

**Role:** browser-as-a-service with additional fetch, search and extraction
products on the same credit balance.

**Category in `data/providers.tsv`:** `browser`, score 81.

### Free tier

| item | value | capture |
|---|---|---|
| allowance | 5,000 credits | H2 |
| kind | one-time | H2 |
| credit card | not stated either way | H2 |
| concurrency | 1 concurrent session | H2 |
| data retention | 7 days | H2 |
| products | all four | H2 |

The free plan is described as "5,000 credits to test the service" with "All four
products, 1 concurrent session, 7 days of data retention". No free-tier period
is stated, and the page does not say whether a card is required. Both absences
are real: the capture does not contain the words "credit card" for the free
plan.

The FAQ adds that plan credits reset at renewal and unused plan credits do not
carry over, but it does not state the Free plan's renewal period. The
`one-time` label here follows `data/providers.tsv`; the capture alone does not
settle whether the 5,000 recur.

The credit value is fixed: "1,000 credits = $1 in usage".

### What one credit buys

| operation | credits | 5,000 credits buys |
|---|---|---|
| browser time | 100 per hour | 50 browser-hours |
| proxy data | 10,000 per GB | 0.5 GB |
| sandbox vCPU | 45 per vCPU-hour | 111 vCPU-hours |
| sandbox memory | 15 per GiB-hour | 333 GiB-hours |
| fetch | 1 per page | 5,000 pages |
| fetch with JSON output | 6 per page | 833 pages |
| fetch with ultra stealth or location | 10 per page | 500 pages |
| search | 5 per query | 1,000 queries |
| search with location | 10 per query | 500 queries |
| AI Extract | 0.03 per output token | 166,666 output tokens |
| HyperAgent | 20 per step | 250 steps |
| Browser Use | 20 per step | 250 steps |

The page states the same conversion in prose: "Enough for 50 browser hours or
5,000 fetched pages at base rates."

### Rate limits and concurrency

Free: 1 concurrent session. No requests-per-minute figure appears in the
captures. Browser concurrency, not credit count, is the binding limit for
browser work: one session at a time means 50 browser-hours is also 50 wall-clock
hours of serial work.

### API surface

- The docs index lists fetch, crawl, search, scrape, extract, batch and
  HyperAgent endpoints, plus SDKs and an MCP server.
- The captures do not contain a base API host, so no request URL is quoted here.
- OpenAPI is referenced at `/docs/openapi.json` but the document itself was not
  captured.
- x402 payment route: a session costs 0.10 USDC per hour, needs no account or
  API key, returns HTTP 402 when unpaid, and is retried with a
  `PAYMENT-SIGNATURE` header. Fetch and search also have x402 endpoints.

### Measured behaviour

No measured success rate is available. Hyperbrowser has no entry in the treg
leaderboard capture, and no live request was made against the API.

### Cost per successful answer

Free tier: 5,000 credits once, which is 50 browser-hours or 5,000 fetches or
1,000 searches.

Paid: Startup is $30/month for 30,000 credits. Because 1,000 credits = $1, that
is $0.001 per credit, so $0.10 per browser-hour, $0.001 per base fetch and
$0.005 per search.

### Fit for the gateway

Hyperbrowser is a browser lane, not a fetch lane. A base fetch at 1 credit is
the cheapest page operation in this set, but the grant is one-time and the
browser concurrency is one session. Use it when a caller needs a real browser
with stealth or a location, or when a fetch needs JSON output. Do not plan
recurring volume on the free grant.

### Evidence

| id | url | HTTP | bytes | sha256 | capture |
|---|---|---|---|---|---|
| H1 | https://www.hyperbrowser.ai/ | 200 | 139061 | `4e24e102cef86ac133f9ea9371f4b68f1fdd234b5d51605782630bdc0b472a55` | `raw/hyperbrowser/home.body` |
| H2 | https://www.hyperbrowser.ai/pricing | 200 | 113527 | `082a21742f1942976e43f05d59da9fa670844c148c706467be247ed89b98eddf` | `raw/hyperbrowser/pricing.body` |
| H3 | https://docs.hyperbrowser.ai/llms.txt | 200 | 26946 | `1c9fe8440bde6bef97aa34af56dc7f20a0ef5511c9d7a3d560265a4b5331723c` | `raw/hyperbrowser/docs.body` |

---

## 7. Browserless

**Role:** hosted Chrome, WebKit and Firefox with REST endpoints, BrowserQL and
direct CDP or Playwright connections.

**Category in `data/providers.tsv`:** `browser`, score 80.

### Free tier

| item | value | capture |
|---|---|---|
| allowance | 1,000 units/month | L2 |
| kind | recurring, monthly | L2 |
| credit card | not required | L2 |
| concurrency | 2 concurrent browsers | L2 |
| session limit | 2 minutes maximum | L2 |
| persisted sessions and replays | 1 day | L2 |
| log search window | 8 hours | L2 |
| proxies | residential 6 units/MB, datacenter 2 units/MB | L2 |
| captcha | 10 units per successful solve | L2 |

The free plan is described as "Free plan: 1k units/month, 2 concurrent browsers.
No credit card, no surprise charges."

### What one unit buys

A unit is "a block of browser time of up to 30 seconds per browser connection".
A connection that runs longer consumes another unit for each additional 30
seconds. Session reconnects count as new browser connections and incur a fresh
unit charge.

| operation | units | 1,000 units buys |
|---|---|---|
| 30 seconds of browser time | 1 | 500 minutes |
| full 2-minute session | 4 | 250 sessions |
| datacenter proxy data | 2 per MB | 500 MB |
| residential proxy data | 6 per MB | 166 MB |
| successful captcha solve | 10 | 100 solves |

The upper bound is 500 browser-minutes, or 8.33 hours, if every unit is used
fully. The 2-minute session cap and the reconnect charge both reduce the
realisable figure: 250 full-length sessions is 500 minutes, but any reconnect
inside a session burns an extra unit without adding usable time.

### Rate limits and concurrency

Free: 2 concurrent browsers. Paid plans show 10, 40 and 100 concurrent browsers.
When the service is over capacity it returns HTTP 429.

### API surface

- REST: `/screenshot`, `/pdf`, `/content`, `/scrape`, `/crawl`, `/search`.
- BrowserQL: `https://production-sfo.browserless.io/chromium/bql?token=...`,
  with a stealth variant at `/stealth/bql`.
- Browser-as-a-service over CDP:
  `wss://production-sfo.browserless.io/chromium?token=...`.
- Playwright:
  `wss://production-sfo.browserless.io/chromium/playwright?token=...`.
- Every route takes the API token as the `token` query parameter.
- `production-sfo` is the shared-cloud default; London and Amsterdam endpoints
  are also listed.

### Measured behaviour

No measured success rate is available. Browserless has no entry in the treg
leaderboard capture, and no live request was made against the API.

### Cost per successful answer

Free tier: 1,000 units per month, or 500 browser-minutes, or 250 full-length
sessions.

Paid marginal cost per unit:

| plan | price | units/month | $/unit | $/browser-hour |
|---|---|---|---|---|
| Prototyping | $25/mo | 20,000 | 0.00125 | 0.15 |
| Starter | $140/mo | 180,000 | 0.000778 | 0.0933 |
| Scale | $350/mo | 500,000 | 0.0007 | 0.084 |

One browser-hour is 120 units at 30 seconds per unit.

### Fit for the gateway

Browserless is a browser lane with a predictable unit price. The unit model
punishes long sessions and reconnects, so a gateway should cap sessions well
below the 2-minute maximum and avoid reconnecting inside one task. Free
concurrency of 2 makes it a small parallel lane. It is not a fetch lane: a plain
page fetch consumes a browser connection and therefore at least one unit.

### Evidence

| id | url | HTTP | bytes | sha256 | capture |
|---|---|---|---|---|---|
| L1 | https://www.browserless.io/ | 200 | 200105 | `924c1ec8e8d553cbeeb111ada517582e4a5888595fb94d1d28f844f52d20a6cc` | `raw/browserless/home.body` |
| L2 | https://www.browserless.io/pricing | 200 | 164868 | `fcd4322205699e08b000cae172979a64532f16abab0960002c774fa01e91a471` | `raw/browserless/pricing.body` |
| L3 | https://docs.browserless.io/llms.txt | 200 | 90199 | `2f27eee736e7aa9d2106526b8bcf70e9c628f6f013836311215cf5fa019eb290` | `raw/browserless/docs.body` |

---

## 8. ScrapingBee

**Role:** unblocker with an HTML API, JavaScript rendering, premium proxies and
dedicated APIs for search engines and marketplaces.

**Category in `data/providers.tsv`:** `unblocker`, score 79.

### Free tier

| item | value | capture |
|---|---|---|
| allowance | 1,000 credits | E1, E2 |
| kind | one-time, valid one month | E1 raw |
| credit card | not required | E2 |
| free concurrency | not stated in captures | none |
| rollover | no | E1 raw |

The pricing page says "Try ScrapingBee with 1,000 free API credits. Sign up. No
credit card required." The raw page tooltip adds: "API credits are valid for one
month and don't roll over" and "Each ScrapingBee plan includes a monthly number
of web scraper API credits."

Read together, the 1,000 free credits are a one-time grant with a one-month
validity, not a recurring free plan. The paid plans carry monthly credits. The
captures do not state that the free 1,000 renew.

### What one credit buys

| operation | credits | 1,000 credits buys |
|---|---|---|
| basic request | 1 | 1,000 requests |
| JavaScript rendering | 5 | 200 requests |
| premium proxies, no JavaScript | 10 | 100 requests |
| premium proxies with JavaScript | 25 | 40 requests |

AI extraction is listed as increasing the cost, but no multiplier for it appears
in the captures. The FAQ gives the same base rule: "A basic request costs 1
credit, while features like JavaScript rendering, premium proxies, or AI
extraction increase the cost."

Billing is success-only: ScrapingBee "only charges for successful scraping
requests, defined as those returning HTTP 200, 404 or 410 status codes."

### Rate limits and concurrency

No free-tier concurrency figure and no requests-per-minute figure appear in the
captures. Paid concurrency, from the plan table:

| plan | price | monthly credits | concurrent requests |
|---|---|---|---|
| Hobby | $19/mo | 75,000 | 25 |
| Freelance | $49/mo | 250,000 | 50 |
| Startup | $99/mo | 1,000,000 | 100 |
| Business | $249/mo | 3,000,000 | 200 |
| Business+ | $599/mo | 8,000,000 | 400 |
| Enterprise 14 | $999/mo | 14,000,000 | 500 |
| Enterprise 24 | $1,599/mo | 24,000,000 | 600 |
| Enterprise 41 | $2,399/mo | 41,000,000 | 700 |
| Enterprise 69 | $3,599/mo | 69,000,000 | 800 |
| Enterprise 120 | $5,799/mo | 120,000,000 | 900 |

Prices are exclusive of VAT.

### API surface

- The captures do not contain the API base URL. `api.scrapingbee.com` does not
  appear in any of the three captures. Only dashboard, MCP, help, status and
  trust hosts appear.
- The docs index names the HTML API, Google Search API, Fast Search API, AI
  extraction, JavaScript scenarios, proxy mode, and dedicated APIs for Amazon,
  Walmart, YouTube, ChatGPT and Gemini.
- An MCP endpoint is present at `https://mcp.scrapingbee.com/`.

A gateway integration needs the base URL from the API documentation, which is
not in this capture set.

### Measured behaviour

No measured success rate is available. ScrapingBee has no entry in the treg
leaderboard capture, and no live request was made against the API.

### Cost per successful answer

Free tier: 1,000 one-time credits, which is 1,000 basic requests or 200 rendered
requests or 100 premium-proxy requests or 40 with both.

Paid marginal cost per credit:

| plan | $/credit | $/basic request | $/rendered request |
|---|---|---|---|
| Hobby | 0.000253 | 0.000253 | 0.00127 |
| Startup | 0.000099 | 0.000099 | 0.000495 |
| Business | 0.000083 | 0.000083 | 0.000415 |

### Fit for the gateway

ScrapingBee is a one-time burst lane, not recurring capacity. Its dedicated
search and marketplace APIs are more interesting than the generic HTML API for a
gateway that already has unblockers. The missing base URL and missing free
concurrency figure mean an integration cannot be specified from this capture
set alone.

### Evidence

| id | url | HTTP | bytes | sha256 | capture |
|---|---|---|---|---|---|
| E1 | https://www.scrapingbee.com/ | 200 | 404411 | `d9dcf2a657ad06556769cbd07f9f4628b66d7c9c9b0ea4ee26ba9dbbd7198d14` | `raw/scrapingbee/home.body` |
| E2 | https://www.scrapingbee.com/pricing/ | 200 | 225443 | `24d75d3ff37debb1b55616135e5266571e87ed7257155868c75ca1558c8261c4` | `raw/scrapingbee/pricing.body` |
| E3 | https://www.scrapingbee.com/llms.txt | 200 | 6204 | `bcca23fa6de91d2325457663da15ffb6214cc295a66ac775fb90278b9325138c` | `raw/scrapingbee/docs.body` |

---

## 9. Scrapfly

**Role:** unblocker with anti-scraping protection, browser rendering,
screenshots, extraction and crawling on one API key.

**Category in `data/providers.tsv`:** `unblocker`, score 78.

### Free tier

| item | value | capture |
|---|---|---|
| allowance | 1,000 credits on signup | F2 |
| kind | one-time, no expiry | F2 |
| credit card | not required | F2 |
| concurrency | 5 concurrent requests | F1, F2 |
| products | every product | F2 |

The pricing page says: "1,000 credits on signup. Every product, no credit card,
no time limit. Use it forever for prototypes and smoke tests." The home page
repeats the grant.

This is the only grant in the set that explicitly does not expire. It is still
one-time: there is no monthly reset.

### What one credit buys

| operation | credits | 1,000 credits buys |
|---|---|---|
| HTTP scrape on a datacenter IP | 1 | 1,000 scrapes |
| add JavaScript rendering or Unblocker | 5 | 200 scrapes |
| add residential proxies | 25 | 40 scrapes |
| full-page screenshot | 60 | 16 screenshots |

The table is additive in the page's presentation: 1 credit for the base HTTP
scrape, 5 credits when JavaScript rendering or the Unblocker is used, 25 when
residential proxies are used, 60 for a full-page screenshot. A request that
combines features is priced at the higher tier, not the sum of every row; the
capture does not spell out every combination, so only the four listed cases are
quoted here.

Failed requests are free: "Pay on success. Failed requests are free." Upstream
4xx and 5xx responses and failed scrapes cost zero.

### Rate limits and concurrency

| plan | price | monthly credits | concurrent requests |
|---|---|---|---|
| Free | $0 | 1,000 one-time | 5 |
| Discovery | $30/mo | 200,000 | 5 |
| Pro | $100/mo | 1,000,000 | 20 |
| Startup | $250/mo | 2,500,000 | 50 |
| Enterprise | $500/mo | 5,500,000 | 100 |

No requests-per-minute figure is published. The docs list throttle error codes
`ERR::THROTTLE::MAX_REQUEST_RATE_EXCEEDED` and
`ERR::THROTTLE::MAX_CONCURRENT_REQUEST_EXCEEDED`, which confirms that a
per-minute limit exists even though its value is not in the capture.

### API surface

- Scrape: `POST https://api.scrapfly.io/scrape`.
- Other endpoints visible in the home capture: `/screenshot`, `/extraction`,
  `/crawler`, `/agent`.
- One API key covers every product.
- The captures do not contain the query-parameter name for the key. The docs
  index links an authentication page, but the parameter name is not in the
  captured text.

### Measured behaviour

No measured success rate is available. Scrapfly has no entry in the treg
leaderboard capture, and no live request was made against the API.

The home page states "15B+" monthly requests and "99.99%" uptime. Both are
VENDOR CLAIMS, not measurements from this set.

### Cost per successful answer

Free tier: 1,000 one-time credits, which is 1,000 HTTP scrapes or 200
rendered/unblocked scrapes or 40 residential scrapes or 16 full-page
screenshots.

Paid marginal cost per credit:

| plan | $/credit | $/HTTP scrape | $/rendered scrape |
|---|---|---|---|
| Discovery | 0.00015 | 0.00015 | 0.00075 |
| Pro | 0.0001 | 0.0001 | 0.0005 |
| Startup | 0.0001 | 0.0001 | 0.0005 |
| Enterprise | 0.0000909 | 0.0000909 | 0.000455 |

### Fit for the gateway

Scrapfly is the best reserve lane in the set because its credits never expire
and the free concurrency of 5 matches ZenRows. It is not a recurring engine: the
grant is 1,000 once. Use it for smoke tests and for overflow when a recurring
provider is exhausted. Its 60-credit screenshot price makes it a poor choice for
screenshot-heavy work.

### Evidence

| id | url | HTTP | bytes | sha256 | capture |
|---|---|---|---|---|---|
| F1 | https://scrapfly.io/ | 200 | 260462 | `4241f8d40412ae67c6cfa9d15fd9abb3412ed304b50c6819716d2155a0618732` | `raw/scrapfly/home.body` |
| F2 | https://scrapfly.io/pricing | 200 | 203428 | `83859c2cd1ab3826c15383a11f674cf31dbe67e76ca2973aac0e9b0005754f30` | `raw/scrapfly/pricing.body` |
| F3 | https://scrapfly.io/docs/llms.txt | 200 | 22746 | `2decfe4b33e28c86250e19411ad20191eeb2d0796ff084eb67fe005d80da510b` | `raw/scrapfly/docs.body` |

---

## 10. Serply

**Role:** search API and page-scraping API with a prepaid credit model and a
hosted MCP server.

**Category in `data/providers.tsv`:** `serp`, score 76.

### Free tier

| item | value | capture |
|---|---|---|
| allowance | 2,500 credits on signup | P2 |
| kind | trial, valid 30 days | P2 |
| credit card | not required | P2 |
| free concurrency | not published in captures | none |
| cached responses | free | P2, P3 |
| failed requests | free | P3 |

The pricing page says: "Every new account starts here. No card required, 2,500
successful requests across any of the Serply APIs, to use in your first 30
days." The docs add: "1 credit = 1 successful uncached request; cached and
failed requests are free."

### What one credit buys

One credit is one successful uncached request on any endpoint, including MCP
tool calls. The unit does not vary by endpoint in the captured text.

| operation | credits | 2,500 credits buys |
|---|---|---|
| successful uncached request | 1 | 2,500 requests |
| cached response | 0 | unlimited within cache |
| failed request | 0 | not charged |

### Rate limits and concurrency

No numeric rate limit appears in the captures. The docs index lists
authentication and error pages, and mentions rate limits, but the rate-limit
page body is not in this capture set.

### API surface

- Base URL: `https://api.serply.io`.
- Authentication: `X-Api-Key` header.
- MCP server: `https://api.serply.io/mcp`.
- Endpoints in the docs: `GET /v1/search` (Google), `/v1/news`,
  `/v1/maps/search`, `/v1/image`, `/v1/job/search`, `/v1/scholar`, `/v1/video`,
  `/v1/b/search` (Bing, includes ads), `/v1/product/search` (Amazon/ASIN),
  `/v1/ebay/search`, `/v1/reddit/{subreddit,post,user,comments}` (no OAuth
  needed), and `POST /v1/request` for a page to markdown or HTML with CAPTCHAs
  handled.
- `X-Proxy-Location` selects one of 14 regions: US, EU, GB, DE, JP and others.
- `X-User-Agent` selects `desktop` (default) or `mobile`.
- A skill file is published at `https://serply.io/skill.md`.

### Measured behaviour

No measured success rate is available. Serply has no entry in the treg
leaderboard capture, and no live request was made against the API.

The home page claims "~900 ms average" and "14 countries". Both are VENDOR
CLAIMS. The 14-country figure is consistent with the 14 regions named in the
docs, but the latency figure is untested here.

### Cost per successful answer

Free tier: 2,500 requests in 30 days, which is about 83 requests per day.

Prepaid packs: 2,500 credits for $5, up to 10,000,000 credits for $7,500. The
published per-1,000 rates are $2.00 on Micro, $1.50 on Starter, $0.98 on Growth
and $0.75 on Pro and above. Purchased credits never expire.

### Fit for the gateway

Serply is a search lane only. The 30-day validity makes it unsuitable as
standing capacity, and the prepaid model means there is no monthly free reset.
It is useful for a short search-heavy workload and for MCP tool calls, where one
credit covers the call. It does not replace a general unblocker.

### Evidence

| id | url | HTTP | bytes | sha256 | capture |
|---|---|---|---|---|---|
| P1 | https://serply.io/ | 200 | 141711 | `57c01086aa391f4e56f828ccc4c9402b7ba4d621b033e2be3f558b8fbc537a96` | `raw/serply/home.body` |
| P2 | https://serply.io/pricing | 200 | 53704 | `cae90e862f4913c449dbc6587f9511b2f43d174e81c29283018b0aad097fe6ab` | `raw/serply/pricing.body` |
| P3 | https://serply.io/llms.txt | 200 | 6014 | `2049657160a751921869b86a1e3ce557056e3cc76871233ba21759137a5bc251` | `raw/serply/docs.body` |

---

## Cross-provider summary

### Free grant by kind

| provider | free grant | kind | card | free concurrency | capacity at cheapest operation |
|---|---|---|---|---|---|
| ZenRows | 5,000 credits | recurring monthly | no | 5 | 5,000 standard pages/month |
| ScrapingAnt | 10,000 credits | recurring monthly | no | no cap published | 1,000 default Chrome requests/month |
| Bright Data | 5,000 credits | recurring monthly | no | not published | unmapped |
| Context.dev | 1,000 credits | recurring monthly | no | 2 | 1,000 standard scrapes/month |
| Crawlbase | 1,000 to 5,000 credits | one-time | no | not published | 5,000 standard requests once |
| Hyperbrowser | 5,000 credits | one-time | not stated | 1 session | 50 browser-hours or 5,000 fetches once |
| Browserless | 1,000 units | recurring monthly | no | 2 | 500 browser-minutes/month |
| ScrapingBee | 1,000 credits | one-time, 1 month validity | no | not published | 1,000 basic requests once |
| Scrapfly | 1,000 credits | one-time, no expiry | no | 5 | 1,000 HTTP scrapes once |
| Serply | 2,500 credits | trial, 30 days | no | not published | 2,500 requests in 30 days |

### Derived totals

Recurring page-equivalent capacity: ZenRows 5,000 plus ScrapingAnt 1,000 plus
Context.dev 1,000 equals 7,000 standard page-equivalents per month. This sum is
DERIVED from the per-provider conversions above. It excludes Bright Data because
its credit mapping is not published, and it excludes Browserless because its
units are browser time rather than pages.

One-time page-equivalent reserve: Crawlbase 5,000 plus ScrapingBee 1,000 plus
Scrapfly 1,000 equals 7,000 standard page-equivalents, available once. This sum
excludes Hyperbrowser (browser and fetch units, one-time) and Serply (search
trial).

Neither sum includes the browser lanes, which are priced in time rather than
pages, or the search lane, which is priced per query.

### Throughput ranking

The published concurrency limits order the set as follows: ScrapingAnt with no
cap, then ZenRows and Scrapfly at 5, then Context.dev and Browserless at 2, then
Hyperbrowser at 1. Bright Data, Crawlbase, ScrapingBee and Serply publish no
free-tier concurrency figure in the captures. A gateway that ignores this
ordering will saturate a 1-concurrent lane while a no-cap lane sits idle.

### Operation cost spread

The same nominal credit buys very different work across the set. At the
expensive end, one credit buys 1/60 of a Scrapfly screenshot or 1/25 of a
ZenRows premium-proxy page. At the cheap end, one credit buys a full Hyperbrowser
fetch or a Serply request. Credit counts are therefore not comparable without
the multiplier, and the tables above are the comparison.

---

## Known cross-pass discrepancies

These are contradictions between this file and other artefacts in the
repository, or between artefacts. They are recorded, not silently reconciled.
No file was edited to remove them as part of this review.

1. `README.md` line 48 lists ZenRows as "1k free credits", "One-Time" and card
   verification "Yes". The pricing capture says 5,000 credits per month,
   recurring, no card. The README row is wrong on all three fields.
2. `README.md` line 49 lists Scrapfly with card verification "Yes". The pricing
   capture says "no credit card". The credit figure and one-time kind agree.
3. `README.md` line 30 and `REPORT.md` line 15 list Bright Data among four
   providers that require card verification. The docs capture says "no credit
   card required". The list is wrong for Bright Data.
4. `data/providers.tsv` gives Scrapfly `paid_from_usd` as 0. The pricing capture
   lists Discovery at $30/month with 200,000 credits. The field does not match
   the capture.
5. `README.md` lines 25 and 26 and `REPORT.md` lines 10 and 11 state aggregate
   monthly capacity of 2,897,475 for one account and 14,487,375 for five.
   `scripts/build_analysis_a.py` reports 759,821 and 3,799,105 on the current
   tree. The difference is pre-existing and comes from different inclusion
   rules, not from this review. `REPORT.md` is hand-maintained and no script
   regenerates it.
6. `scripts/build_analysis_a.py` excludes ZenRows, ScrapingAnt, Bright Data,
   Context.dev and Browserless from the capacity total under the heading
   "credit-based allowances where 1 credit != 1 request was not documented".
   For ZenRows and Context.dev the mapping is documented in the captures: one
   credit is one standard page or scrape. For ScrapingAnt the default is
   documented as 10 credits. The exclusion is conservative, but its stated
   reason is false for at least those three providers, and the effect is that
   the reported total understates recurring free capacity.

---

## Limits of this comparison

**No measured success rates.** The treg leaderboard capture used elsewhere in
this set is
`evidence/seeds/002_treg.to_web-arena_api_leaderboard.body`. It contains no
entry for any of the ten providers reviewed here. Providers it does measure
include tinyfish, serper, crawl4ai, exa, perplexity, search1api, spidercloud,
keenable, firecrawl, branddev, parallel, tavily, olostep, you, linkup, octen,
scrapegraphai, diffbot, anyapi, dataforseo, apify, litescrape, cloro, serpapi,
tikhub and justoneapi. None overlaps this set. The remaining treg captures
also contain no entry for any of the ten as a measured result; Bright Data and
Context.dev appear only as tool labels in
`evidence/seeds/001_treg.to_web-access.body` and as endpoint metadata in
`evidence/seeds2/002_treg.to_catalog.body`, never as leaderboard rows. Closing
this gap requires
running each free tier under one common harness, which this static review did
not do.

**Vendor claims are not measurements.** Context.dev's 99.96% scrape success
rate, Scrapfly's 15B+ requests and 99.99% uptime, and Serply's ~900 ms average
are quoted as claims and labelled as such.

**Captures are single-day.** All responses were taken on 2026-10-19 at
05:58:21Z. Prices, allowances and limits can change. The sha256 in each table
identifies the exact bytes reviewed.

**Missing pages.** ScrapingAnt's pricing page and `llms.txt` are both HTTP 404
with the same body, so its option multipliers beyond the default cannot be
cited. Bright Data publishes no credit-to-operation mapping. Hyperbrowser and
Bright Data expose no API host in their captures. ScrapingBee exposes no API
host. Scrapfly and Crawlbase do not expose the exact key parameter name. None of
these gaps was filled by guessing.

**No live requests.** No provider was called during this review. Every number
is published text, not an observed response from the API.

**Currency and tax.** All prices are USD as published. ScrapingBee states that
its prices exclude VAT. Other providers do not state a tax treatment in the
captured text.

