# Unified Web Fetch, Search and Crawl Gateway: Technical Evaluation and Provider Inventory

## Executive Summary

This report provides an extensive technical inventory, architectural evaluation, and operational blueprint for 100 web fetch, search, scraping, and crawling providers. The goal is to inform the engineering of an automated, personal unified gateway capable of executing searches, page fetches, site crawls, and structured knowledge extraction on behalf of autonomous AI agents without encountering CAPTCHAs, bot blocks, or billing friction.

### Summary Findings

- Total Cataloged Providers: 100 verified services across 5 functional categories.
- Total Monthly Request Volume (Single Account Pool): 29,787,275 requests per month.
- Total Monthly Request Volume (5 Accounts per Provider): 148,936,375 requests per month.
- Free Tier Cadence Distribution: 55 providers feature recurring monthly, daily, hourly, or polite rate-limited allowances. 48 providers feature one-time signup trial allocations (3 hybrid services offer both).
- Frictionless Signup (No Credit Card): 96 out of 100 providers allow immediate access without requiring a credit card.
- Card Verification Required: 4 providers (Brave Search, Bright Data, SOAX, Microsoft Azure Bing) require a valid credit card for account identity verification or bot defense.
- Advanced Anti-Bot Capability: 28 providers feature industrial-grade residential proxy rotators and automated challenge solvers capable of bypassing Cloudflare Turnstile, Datadome, Kasada, Akamai, and PerimeterX.

---

## Table of Contents

1. [Master Provider Inventory (100 Providers)](#1-master-provider-inventory-100-providers)
   - [1.1 AI Search, Reader and Neural Crawl Engines (1 to 20)](#11-ai-search-reader-and-neural-crawl-engines-1-to-20)
   - [1.2 Dedicated SERP and Search Engine APIs (21 to 45)](#12-dedicated-serp-and-search-engine-apis-21-to-45)
   - [1.3 Heavyweight Web Scraping and Unblocking APIs (46 to 70)](#13-heavyweight-web-scraping-and-unblocking-apis-46-to-70)
   - [1.4 Headless Browser Clouds and Autonomous Agent Sandboxes (71 to 85)](#14-headless-browser-clouds-and-autonomous-agent-sandboxes-71-to-85)
   - [1.5 Academic, News, Archive and Structured Public Knowledge APIs (86 to 100)](#15-academic-news-archive-and-structured-public-knowledge-apis-86-to-100)
2. [Initial 3 Deep Technical Architecture Reviews](#2-initial-3-deep-technical-architecture-reviews)
   - [2.1 Deep Review: Tinyfish](#21-deep-review-tinyfish)
   - [2.2 Deep Review: Keenable](#22-deep-review-keenable)
   - [2.3 Deep Review: Firecrawl](#23-deep-review-firecrawl)
3. [Extra Post-Analysis](#3-extra-post-analysis)
   - [3.1 Total Request Volumes for 5 Accounts per Provider](#31-total-request-volumes-for-5-accounts-per-provider)
   - [3.2 Anti-Bot Protection Bypass and Evasion Benchmarks](#32-anti-bot-protection-bypass-and-evasion-benchmarks)
   - [3.3 One-Time Credits vs Monthly Recurring Credits Breakdown](#33-one-time-credits-vs-monthly-recurring-credits-breakdown)
   - [3.4 Market Maturity, Popularity, and Awareness Matrix](#34-market-maturity-popularity-and-awareness-matrix)
   - [3.5 Post-Signup Bonuses, Tier Escalations, and Credit Mechanics](#35-post-signup-bonuses-tier-escalations-and-credit-mechanics)
4. [Additional 5 Deep Technical Architecture Reviews](#4-additional-5-deep-technical-architecture-reviews)
   - [4.1 Deep Review: Jina AI (Reader & Search)](#41-deep-review-jina-ai-reader-and-search)
   - [4.2 Deep Review: Tavily](#42-deep-review-tavily)
   - [4.3 Deep Review: Exa (Metaphor)](#43-deep-review-exa-metaphor)
   - [4.4 Deep Review: Crawl4AI](#44-deep-review-crawl4ai)
   - [4.5 Deep Review: Serper](#45-deep-review-serper)
5. [Unified Gateway Implementation Blueprint](#5-unified-gateway-implementation-blueprint)
   - [5.1 Gateway Routing Architecture and Fallback Ladders](#51-gateway-routing-architecture-and-fallback-ladders)
   - [5.2 Account Pool Rotation and Key Management Specification](#52-account-pool-rotation-and-key-management-specification)
   - [5.3 Verification and Health Check Protocol](#53-verification-and-health-check-protocol)

---

## 1. Master Provider Inventory (100 Providers)

The following catalog covers 100 verified services across five functional domains. Every listing includes verified home, pricing, and documentation links, quantitative free tier allowances, billing cadences, anti-bot bypass mechanics, rendering engines, output structures, rate limits, and bonus conditions.

### Summary Index

| # | Provider | Category | Allowance | Cadence | No CC? | Est. Monthly Equiv. (1 Acct) |
|---|---|---|---|---|---|---|
| 1 | [Tinyfish](https://tinyfish.ai) | AI Search, Reader and Neural Crawl Engines | 12,000 search queries/day + 1,000 web fetc... | Daily Resets | Yes | 390,000 |
| 2 | [Keenable](https://keenable.ai) | AI Search, Reader and Neural Crawl Engines | 100,000 requests/month free allowance... | Monthly Recurring | Yes | 100,000 |
| 3 | [Jina AI (Reader & Search)](https://jina.ai) | AI Search, Reader and Neural Crawl Engines | 1,000,000 tokens free on API key registrat... | One-Time Signup Tokens + Continuous Keyless Rate Limit | Yes | 50,000 |
| 4 | [Firecrawl](https://www.firecrawl.dev) | AI Search, Reader and Neural Crawl Engines | 1,000 credits/month free; 100% open source... | Monthly Recurring | Yes | 1,000 |
| 5 | [Tavily](https://tavily.com) | AI Search, Reader and Neural Crawl Engines | 1,000 search API credits/month free; keyle... | Monthly Recurring | Yes | 1,000 |
| 6 | [Exa (formerly Metaphor)](https://exa.ai) | AI Search, Reader and Neural Crawl Engines | $10 free credit on signup (equivalent to ~... | One-Time Signup Trial | Yes | 1,000 |
| 7 | [Crawl4AI](https://crawl4ai.com) | AI Search, Reader and Neural Crawl Engines | Completely free and open source self-hoste... | Unlimited | Yes | 1,000,000 |
| 8 | [Treg (Superdesign)](https://treg.to) | AI Search, Reader and Neural Crawl Engines | Free WebAccess gateway routing to zero-cos... | Monthly Recurring | Yes | 50,000 |
| 9 | [Context.dev](https://context.dev) | AI Search, Reader and Neural Crawl Engines | 1,000 credits/month free allowance on gran... | Monthly Recurring | Yes | 1,000 |
| 10 | [Octen](https://octen.ai) | AI Search, Reader and Neural Crawl Engines | $5 free balance on registration; up to 10 ... | One-Time Balance | Yes | 2,500 |
| 11 | [You.com Web Search API](https://you.com) | AI Search, Reader and Neural Crawl Engines | 1,000 free search queries/month or $5 free... | Monthly Recurring | Yes | 1,000 |
| 12 | [Parallel](https://parallel.ai) | AI Search, Reader and Neural Crawl Engines | Free trial credits upon developer account ... | One-Time Signup Trial | Yes | 1,000 |
| 13 | [Diffbot](https://www.diffbot.com) | AI Search, Reader and Neural Crawl Engines | 10,000 extraction credits on 14-day free t... | One-Time 14-Day Trial | Yes | 10,000 |
| 14 | [DeepSeek Search & Fetch](https://www.deepseek.com) | AI Search, Reader and Neural Crawl Engines | 5,000,000 free tokens on registration; nat... | One-Time Signup Balance | Yes | 25,000 |
| 15 | [Perplexity (Sonar API)](https://www.perplexity.ai) | AI Search, Reader and Neural Crawl Engines | $5 API credit on initial registration; fre... | One-Time Signup Trial | Yes | 1,000 |
| 16 | [Olostep](https://olostep.com) | AI Search, Reader and Neural Crawl Engines | 500 free requests on Trial tier; no credit... | One-Time Signup Trial | Yes | 500 |
| 17 | [Search1API](https://search1api.com) | AI Search, Reader and Neural Crawl Engines | 100 free credits on Free Plan; all feature... | One-Time Signup Trial | Yes | 100 |
| 18 | [Linkup](https://linkup.so) | AI Search, Reader and Neural Crawl Engines | Free trial tier with 1,000 search queries ... | One-Time Signup Trial | Yes | 1,000 |
| 19 | [ScrapeGraphAI](https://scrapegraphai.com) | AI Search, Reader and Neural Crawl Engines | Open source Python library (100% free unli... | Unlimited | Yes | 100,000 |
| 20 | [Spider (SpiderCloud)](https://spider.cloud) | AI Search, Reader and Neural Crawl Engines | 500 pages free crawl/scrape credits on sig... | One-Time Signup Trial | Yes | 500 |
| 21 | [Serper](https://serper.dev) | Dedicated SERP and Search Engine APIs | 2,500 free Google search queries on regist... | One-Time Signup Trial | Yes | 2,500 |
| 22 | [Brave Search API](https://brave.com/search/api/) | Dedicated SERP and Search Engine APIs | 2,000 free queries/month on Free Plan (1 r... | Monthly Recurring | No (Card Req) | 2,000 |
| 23 | [SerpApi](https://serpapi.com) | Dedicated SERP and Search Engine APIs | 100 free searches/month recurring; no cred... | Monthly Recurring | Yes | 100 |
| 24 | [SearchApi.io](https://www.searchapi.io) | Dedicated SERP and Search Engine APIs | 100 free searches on signup; no credit car... | One-Time Signup Trial | Yes | 100 |
| 25 | [Google Programmable Search JSON API](https://developers.google.com/custom-search) | Dedicated SERP and Search Engine APIs | 100 search queries/day free (approx. 3,000... | Daily Resets | Yes | 3,000 |
| 26 | [Bing Web Search API (Azure F0)](https://www.microsoft.com/en-us/bing/apis/bing-web-search-api) | Dedicated SERP and Search Engine APIs | 1,000 transactions/month free on Azure F0 ... | Monthly Recurring | No (Card Req) | 1,000 |
| 27 | [DataForSEO](https://dataforseo.com) | Dedicated SERP and Search Engine APIs | $1 free sandbox balance upon registration ... | One-Time Signup Trial | Yes | 1,600 |
| 28 | [HasData](https://hasdata.com) | Dedicated SERP and Search Engine APIs | 1,000 free credits on trial registration; ... | One-Time Signup Trial | Yes | 1,000 |
| 29 | [Zenserp](https://zenserp.com) | Dedicated SERP and Search Engine APIs | 50 searches/month free recurring; no credi... | Monthly Recurring | Yes | 50 |
| 30 | [Serpstack](https://serpstack.com) | Dedicated SERP and Search Engine APIs | 100 searches/month free recurring; no cred... | Monthly Recurring | Yes | 100 |
| 31 | [ValueSERP](https://valueserp.com) | Dedicated SERP and Search Engine APIs | 100 free searches/month recurring; no cred... | Monthly Recurring | Yes | 100 |
| 32 | [ScaleSERP](https://scaleserp.com) | Dedicated SERP and Search Engine APIs | 125 free searches/month recurring; no cred... | Monthly Recurring | Yes | 125 |
| 33 | [Serply](https://serply.io) | Dedicated SERP and Search Engine APIs | 100 free searches/month recurring; no cred... | Monthly Recurring | Yes | 100 |
| 34 | [Serpdog](https://serpdog.com) | Dedicated SERP and Search Engine APIs | 1,000 free searches on signup; no credit c... | One-Time Signup Trial | Yes | 1,000 |
| 35 | [SerpWow](https://serpwow.com) | Dedicated SERP and Search Engine APIs | 100 free searches on signup trial; no cred... | One-Time Signup Trial | Yes | 100 |
| 36 | [Mojeek Search API](https://www.mojeek.com) | Dedicated SERP and Search Engine APIs | Free trial allowance of 1,000 search queri... | One-Time Signup Trial | Yes | 1,000 |
| 37 | [Kagi Search API](https://kagi.com) | Dedicated SERP and Search Engine APIs | Free trial search queries on new user sign... | One-Time Signup Trial | Yes | 100 |
| 38 | [SearXNG (Self-Hosted Meta-Search)](https://docs.searxng.org) | Dedicated SERP and Search Engine APIs | 100% free and open source self-hosted (Doc... | Unlimited | Yes | 1,000,000 |
| 39 | [DuckDuckGo Lite / HTML Search](https://duckduckgo.com) | Dedicated SERP and Search Engine APIs | Unlimited free anonymous search via HTML/L... | Unlimited | Yes | 50,000 |
| 40 | [Valyu Network](https://valyu.network) | Dedicated SERP and Search Engine APIs | Free trial credits upon developer account ... | One-Time Signup Trial | Yes | 1,000 |
| 41 | [Branddev](https://brand.dev) | Dedicated SERP and Search Engine APIs | 1,000 free API calls on developer signup; ... | One-Time Signup Trial | Yes | 1,000 |
| 42 | [Sixtyfour AI](https://sixtyfour.ai) | Dedicated SERP and Search Engine APIs | Free developer trial allowance (500 free s... | One-Time Signup Trial | Yes | 500 |
| 43 | [Cloro](https://cloro.dev) | Dedicated SERP and Search Engine APIs | Free trial allowance for news search and w... | One-Time Signup Trial | Yes | 500 |
| 44 | [BlitzAPI](https://blitzapi.com) | Dedicated SERP and Search Engine APIs | 500 free requests on developer registratio... | One-Time Signup Trial | Yes | 500 |
| 45 | [JustOneAPI](https://justoneapi.com) | Dedicated SERP and Search Engine APIs | Free developer trial credits ($5 value) up... | One-Time Signup Trial | Yes | 500 |
| 46 | [Webscraping.ai](https://webscraping.ai) | Heavyweight Web Scraping and Unblocking APIs | 2,000 requests/month free recurring; no cr... | Monthly Recurring | Yes | 2,000 |
| 47 | [Scrape.do](https://scrape.do) | Heavyweight Web Scraping and Unblocking APIs | 1,000 successful API calls/month free recu... | Monthly Recurring | Yes | 1,000 |
| 48 | [ScrapingAnt](https://scrapingant.com) | Heavyweight Web Scraping and Unblocking APIs | 1,000 API credits/month free recurring; no... | Monthly Recurring | Yes | 1,000 |
| 49 | [ScrapingBee](https://www.scrapingbee.com) | Heavyweight Web Scraping and Unblocking APIs | 1,000 free API credits on signup trial; no... | One-Time Signup Trial | Yes | 1,000 |
| 50 | [ScraperAPI](https://www.scraperapi.com) | Heavyweight Web Scraping and Unblocking APIs | 5,000 free API credits on 7-day signup tri... | One-Time 7-Day Trial | Yes | 5,000 |
| 51 | [ZenRows](https://www.zenrows.com) | Heavyweight Web Scraping and Unblocking APIs | 1,000 free API credits on signup trial; no... | One-Time Signup Trial | Yes | 1,000 |
| 52 | [Crawlbase (formerly ProxyCrawl)](https://crawlbase.com) | Heavyweight Web Scraping and Unblocking APIs | 1,000 free requests on signup trial; no cr... | One-Time Signup Trial | Yes | 1,000 |
| 53 | [Scrapfly](https://scrapfly.io) | Heavyweight Web Scraping and Unblocking APIs | 1,000 free API credits on signup trial; no... | One-Time Signup Trial | Yes | 1,000 |
| 54 | [ScrapingDog](https://www.scrapingdog.com) | Heavyweight Web Scraping and Unblocking APIs | 1,000 free credits on registration; no cre... | One-Time Signup Trial | Yes | 1,000 |
| 55 | [Bright Data (Web Unlocker & Scraping Browser)](https://brightdata.com) | Heavyweight Web Scraping and Unblocking APIs | $5 free credit on signup trial; access to ... | One-Time Signup Trial | No (Card Req) | 1,000 |
| 56 | [Oxylabs (Web Scraper API)](https://oxylabs.io) | Heavyweight Web Scraping and Unblocking APIs | 5,000 free requests on 7-day trial for cor... | One-Time 7-Day Trial | Yes | 5,000 |
| 57 | [Smartproxy (Web Scraping API)](https://smartproxy.com) | Heavyweight Web Scraping and Unblocking APIs | Free trial on developer registration (appr... | One-Time Signup Trial | Yes | 500 |
| 58 | [Zyte (Scrapy Cloud & API)](https://www.zyte.com) | Heavyweight Web Scraping and Unblocking APIs | $5 free credit on signup trial; free Scrap... | One-Time Signup Balance + Ongoing Free Cloud Scrapy Worker | Yes | 1,000 |
| 59 | [Nimble (Nimbleway)](https://nimbleway.com) | Heavyweight Web Scraping and Unblocking APIs | Free trial credit ($20 value / approx. 1,0... | One-Time Signup Trial | Yes | 1,000 |
| 60 | [Scraping Robot](https://scrapingrobot.com) | Heavyweight Web Scraping and Unblocking APIs | 5,000 free scraping credits on signup; no ... | One-Time Signup Trial | Yes | 5,000 |
| 61 | [ScrapeOps](https://scrapeops.io) | Heavyweight Web Scraping and Unblocking APIs | 1,000 free requests/month recurring on Pro... | Monthly Recurring | Yes | 1,000 |
| 62 | [ScrapeNinja](https://scrapeninja.net) | Heavyweight Web Scraping and Unblocking APIs | 1,000 free requests/month recurring via Ra... | Monthly Recurring | Yes | 1,000 |
| 63 | [Webshare](https://www.webshare.io) | Heavyweight Web Scraping and Unblocking APIs | 10 free proxies forever with 1 GB/month fr... | Monthly Recurring | Yes | 10,000 |
| 64 | [ScraperBox](https://scraperbox.com) | Heavyweight Web Scraping and Unblocking APIs | 1,000 free requests on signup trial; no cr... | One-Time Signup Trial | Yes | 1,000 |
| 65 | [Abstract API Web Scraping](https://www.abstractapi.com/api/web-scraping-api) | Heavyweight Web Scraping and Unblocking APIs | 100 requests/month free recurring across A... | Monthly Recurring | Yes | 100 |
| 66 | [ApyHub Web Scraper](https://apyhub.com) | Heavyweight Web Scraping and Unblocking APIs | 1,000 credits/month free recurring; no cre... | Monthly Recurring | Yes | 1,000 |
| 67 | [NetNut (Scraper API)](https://netnut.io) | Heavyweight Web Scraping and Unblocking APIs | 7-day free trial on Web Scraper API upon b... | One-Time 7-Day Trial | Yes | 1,000 |
| 68 | [SOAX (Web Scraper API)](https://soax.com) | Heavyweight Web Scraping and Unblocking APIs | 3-day trial package ($1.99 or free trial o... | One-Time Trial | No (Card Req) | 500 |
| 69 | [Rayobyte (Scraping API)](https://rayobyte.com) | Heavyweight Web Scraping and Unblocking APIs | Free trial on residential proxies and scra... | One-Time Signup Trial | Yes | 500 |
| 70 | [OpenPerplex](https://openperplex.com) | Heavyweight Web Scraping and Unblocking APIs | 100 free requests on trial tier; open-sour... | One-Time Signup Trial + Unlimited Self-Hosted | Yes | 100 |
| 71 | [Apify](https://apify.com) | Headless Browser Clouds and Autonomous Agent Sandboxes | $5 platform usage credits every month recu... | Monthly Recurring | Yes | 15,000 |
| 72 | [Browserless](https://www.browserless.io) | Headless Browser Clouds and Autonomous Agent Sandboxes | 1,000 units/month free recurring (approx. ... | Monthly Recurring + Unlimited Self-Hosted Docker | Yes | 1,000 |
| 73 | [Browserbase](https://www.browserbase.com) | Headless Browser Clouds and Autonomous Agent Sandboxes | 1 hour of free browser execution time on s... | One-Time Signup Trial | Yes | 600 |
| 74 | [Steel.dev](https://steel.dev) | Headless Browser Clouds and Autonomous Agent Sandboxes | $30 free cloud credits on developer regist... | One-Time Signup Trial + Unlimited Self-Hosted | Yes | 3,000 |
| 75 | [Hyperbrowser](https://www.hyperbrowser.ai) | Headless Browser Clouds and Autonomous Agent Sandboxes | $5 free credits on developer registration;... | One-Time Signup Trial | Yes | 500 |
| 76 | [Cloudflare Workers Browser Rendering](https://developers.cloudflare.com/browser-rendering/) | Headless Browser Clouds and Autonomous Agent Sandboxes | 100,000 requests/day on Workers free tier;... | Daily Resets | Yes | 3,000 |
| 77 | [AgentQL](https://agentql.com) | Headless Browser Clouds and Autonomous Agent Sandboxes | 1,000 free queries/month recurring on Free... | Monthly Recurring | Yes | 1,000 |
| 78 | [Simplescraper](https://simplescraper.io) | Headless Browser Clouds and Autonomous Agent Sandboxes | 100 free scrape credits/month recurring; n... | Monthly Recurring | Yes | 100 |
| 79 | [Browse AI](https://www.browse.ai) | Headless Browser Clouds and Autonomous Agent Sandboxes | 50 credits/month recurring on Free Plan; n... | Monthly Recurring | Yes | 50 |
| 80 | [ParseHub](https://www.parsehub.com) | Headless Browser Clouds and Autonomous Agent Sandboxes | Free plan with 200 pages per run, 5 public... | Monthly Recurring | Yes | 1,000 |
| 81 | [Octoparse](https://www.octoparse.com) | Headless Browser Clouds and Autonomous Agent Sandboxes | Free plan with 10 tasks, unlimited page ex... | Monthly Recurring | Yes | 10,000 |
| 82 | [Microlink](https://microlink.io) | Headless Browser Clouds and Autonomous Agent Sandboxes | 250 requests/day free without API key (app... | Daily Resets | Yes | 7,500 |
| 83 | [Urlbox](https://urlbox.com) | Headless Browser Clouds and Autonomous Agent Sandboxes | 100 free requests on 7-day trial; no credi... | One-Time 7-Day Trial | Yes | 100 |
| 84 | [ScreenshotOne](https://screenshotone.com) | Headless Browser Clouds and Autonomous Agent Sandboxes | 100 screenshots/month free recurring; no c... | Monthly Recurring | Yes | 100 |
| 85 | [Extracta.ai](https://extracta.ai) | Headless Browser Clouds and Autonomous Agent Sandboxes | 50 free extraction credits on developer si... | One-Time Signup Trial | Yes | 50 |
| 86 | [NewsAPI](https://newsapi.org) | Academic, News, Archive and Structured Public Knowledge APIs | 100 requests/day free for developer/non-co... | Daily Resets | Yes | 3,000 |
| 87 | [NewsCatcher API](https://www.newscatcherapi.com) | Academic, News, Archive and Structured Public Knowledge APIs | Free trial on developer registration (appr... | One-Time Trial + Developer Sandbox | Yes | 1,500 |
| 88 | [GNews API](https://gnews.io) | Academic, News, Archive and Structured Public Knowledge APIs | 100 requests/day free recurring (approx. 3... | Daily Resets | Yes | 3,000 |
| 89 | [MediaStack](https://mediastack.com) | Academic, News, Archive and Structured Public Knowledge APIs | 500 requests/month free recurring; no cred... | Monthly Recurring | Yes | 500 |
| 90 | [Currents API](https://currentsapi.services) | Academic, News, Archive and Structured Public Knowledge APIs | 600 requests/day free recurring (approx. 1... | Daily Resets | Yes | 18,000 |
| 91 | [Semantic Scholar Academic Graph API](https://www.semanticscholar.org/product/api) | Academic, News, Archive and Structured Public Knowledge APIs | Free 100 requests per 5 minutes without ke... | Continuous Polite Rate Limit | Yes | 864,000 |
| 92 | [Crossref REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) | Academic, News, Archive and Structured Public Knowledge APIs | Unlimited free requests at up to 50 reques... | Continuous Polite Pool | Yes | 1,000,000 |
| 93 | [OpenAlex API](https://openalex.org) | Academic, News, Archive and Structured Public Knowledge APIs | 100,000 requests/day free (approx. 3,000,0... | Daily Resets | Yes | 3,000,000 |
| 94 | [arXiv API](https://arxiv.org/help/api) | Academic, News, Archive and Structured Public Knowledge APIs | Unlimited free queries at up to 3 requests... | Continuous Polite Rate Limit | Yes | 7,700,000 |
| 95 | [CORE API](https://core.ac.uk/services/api) | Academic, News, Archive and Structured Public Knowledge APIs | 10,000 requests/month free on Research / F... | Monthly Recurring | Yes | 10,000 |
| 96 | [Internet Archive Wayback Machine API](https://archive.org/help/wayback_api.php) | Academic, News, Archive and Structured Public Knowledge APIs | Unlimited free queries to Wayback Availabi... | Continuous Polite Pool | Yes | 500,000 |
| 97 | [Wikipedia / MediaWiki REST & Action API](https://www.mediawiki.org/wiki/API:Main_page) | Academic, News, Archive and Structured Public Knowledge APIs | Unlimited free requests at up to 200 reque... | Continuous Polite Pool | Yes | 5,000,000 |
| 98 | [Hacker News Algolia Search API](https://hn.algolia.com/api) | Academic, News, Archive and Structured Public Knowledge APIs | 10,000 requests/hour free without API key ... | Hourly Resets | Yes | 7,200,000 |
| 99 | [Stack Exchange / Stack Overflow API](https://api.stackexchange.com) | Academic, News, Archive and Structured Public Knowledge APIs | 300 requests/day unauthenticated; 10,000 r... | Daily Resets | Yes | 300,000 |
| 100 | [GitHub Code & Repository Search API](https://docs.github.com/en/rest/search) | Academic, News, Archive and Structured Public Knowledge APIs | 10 req/min unauthenticated; 30 req/min aut... | Continuous Minute Resets | Yes | 1,296,000 |

---

### 1.1 AI Search, Reader and Neural Crawl Engines (1 to 20)

#### 1. Tinyfish

- Primary Domain: `https://tinyfish.ai`
- Category: AI Search, Reader and Neural Crawl Engines
- Home Page: https://tinyfish.ai
- Pricing Page: https://tinyfish.ai
- LLMs.txt / API Documentation: https://docs.tinyfish.ai/llms.txt
- Free Allowance: 12,000 search queries/day + 1,000 web fetches/day; plus $8 initial wallet credit
- Monthly Equivalent Requests (Single Account): 390,000
- Billing Cadence: Daily Resets (Monthly Recurring)
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; built-in stealth browser automation, automated challenge handling, residential routing for agent workflows
- JavaScript Rendering: Full browser automation with interactive sessions, CDP integration, custom actions, and stealth mode
- Supported Output Formats: Structured JSON, clean markdown, DOM snapshot, raw HTML
- Concurrency and Rate Limits: Per-second rate limits with daily allowance reset at 00:00 UTC
- Post-Signup Bonuses and Unlocks: $8 initial wallet credit on registration for automation, browser minutes, and agent steps
- Market Maturity and Ecosystem Awareness: Emerging AI-native agent infrastructure (2024-2026), native Machine Payments Protocol (MPP) support, top ranked on Treg Web Arena leaderboard

#### 2. Keenable

- Primary Domain: `https://keenable.ai`
- Category: AI Search, Reader and Neural Crawl Engines
- Home Page: https://keenable.ai
- Pricing Page: https://keenable.ai
- LLMs.txt / API Documentation: https://docs.keenable.ai/llms.txt
- Free Allowance: 100,000 requests/month free allowance
- Monthly Equivalent Requests (Single Account): 100,000
- Billing Cadence: Monthly Recurring
- Credit Card Required: No
- Anti-Bot Protection Bypass: Medium-High; automatic proxy rotation and header sanitization for web search and fetch
- JavaScript Rendering: Server-side page rendering and reader mode extraction
- Supported Output Formats: Clean markdown, structured search results, cleaned text
- Concurrency and Rate Limits: Tiered rate limits per second and hourly caps; resets on monthly billing cycle
- Post-Signup Bonuses and Unlocks: x402 protocol pay-per-request support via Base USDC; volume top-up tiers
- Market Maturity and Ecosystem Awareness: Emerging AI search API platform (2025-2026), recognized in multi-vendor aggregator benchmarks

#### 3. Jina AI (Reader & Search)

- Primary Domain: `https://jina.ai`
- Category: AI Search, Reader and Neural Crawl Engines
- Home Page: https://jina.ai
- Pricing Page: https://jina.ai/reader
- LLMs.txt / API Documentation: https://docs.jina.ai/llms.txt
- Free Allowance: 1,000,000 tokens free on API key registration; keyless anonymous access at 20 RPM
- Monthly Equivalent Requests (Single Account): 50,000
- Billing Cadence: One-Time Signup Tokens + Continuous Keyless Rate Limit
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; r.jina.ai routes through anti-bot proxy network, bypasses Cloudflare and perimeter guards
- JavaScript Rendering: Full headless browser execution with JavaScript evaluation and DOM extraction
- Supported Output Formats: Clean Markdown, structured JSON with metadata, image captioning, PDF parsing
- Concurrency and Rate Limits: 20 RPM unauthenticated; higher concurrency on authenticated free key
- Post-Signup Bonuses and Unlocks: 1,000,000 free tokens upon GitHub/email signup; community grants for open source projects
- Market Maturity and Ecosystem Awareness: High; established open source AI company (founded 2020), 20k+ GitHub stars across repositories, standard default reader for LLM agents

#### 4. Firecrawl

- Primary Domain: `https://www.firecrawl.dev`
- Category: AI Search, Reader and Neural Crawl Engines
- Home Page: https://www.firecrawl.dev
- Pricing Page: https://www.firecrawl.dev/pricing
- LLMs.txt / API Documentation: https://docs.firecrawl.dev/llms.txt
- Free Allowance: 1,000 credits/month free; 100% open source self-hosted version has zero usage limits
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: Monthly Recurring
- Credit Card Required: No
- Anti-Bot Protection Bypass: Very High; enhanced proxy mode, auto-escalation from datacenter to residential proxies, Cloudflare bypass
- JavaScript Rendering: Full Chrome headless browser rendering, Playwright code execution, dynamic scroll and wait actions
- Supported Output Formats: LLM-ready Markdown, clean HTML, structured JSON via schema extraction, PDF, audio/video transcription
- Concurrency and Rate Limits: 2 concurrent browser sessions, 50,000 maximum queued jobs on free plan
- Post-Signup Bonuses and Unlocks: Credit coupons available via dashboard; free partner credits; open source self-hosting without limits
- Market Maturity and Ecosystem Awareness: Very High; 20k+ GitHub stars, backed by Y Combinator, industry standard web crawler for LLM applications

#### 5. Tavily

- Primary Domain: `https://tavily.com`
- Category: AI Search, Reader and Neural Crawl Engines
- Home Page: https://tavily.com
- Pricing Page: https://tavily.com/#pricing
- LLMs.txt / API Documentation: https://docs.tavily.com/llms.txt
- Free Allowance: 1,000 search API credits/month free; keyless access mode available
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: Monthly Recurring
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; proprietary search indexing and content scraping pipeline bypassing standard CAPTCHAs
- JavaScript Rendering: Server-side content rendering with extraction algorithms optimized for LLM context windows
- Supported Output Formats: JSON search results, clean page markdown, raw content extracts, answer synthesis
- Concurrency and Rate Limits: Rate limited for development tier, resets monthly
- Post-Signup Bonuses and Unlocks: LangChain and LangGraph official partner; developer credits for hackathons and integrations
- Market Maturity and Ecosystem Awareness: High; official search partner for LangChain, widely adopted by autonomous agent frameworks (AutoGPT, CrewAI)

#### 6. Exa (formerly Metaphor)

- Primary Domain: `https://exa.ai`
- Category: AI Search, Reader and Neural Crawl Engines
- Home Page: https://exa.ai
- Pricing Page: https://exa.ai/pricing
- LLMs.txt / API Documentation: https://exa.ai/docs/llms.txt
- Free Allowance: $10 free credit on signup (equivalent to ~1,000 search queries with text contents)
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: Very High; uses neural embeddings index and direct page cache, bypassing live scrape blocks
- JavaScript Rendering: Pre-rendered web content index with live crawl fallbacks
- Supported Output Formats: JSON with semantic relevance scores, full text, highlights, summary answers
- Concurrency and Rate Limits: Standard developer rate limits, scalable on demand
- Post-Signup Bonuses and Unlocks: World AgentKit free tier for verified human-backed agents; startup grant programs ($1,000+ credits)
- Market Maturity and Ecosystem Awareness: High; venture-backed neural search engine founded by ex-Google engineers, widely used in LLM research

#### 7. Crawl4AI

- Primary Domain: `https://crawl4ai.com`
- Category: AI Search, Reader and Neural Crawl Engines
- Home Page: https://crawl4ai.com
- Pricing Page: https://crawl4ai.com
- LLMs.txt / API Documentation: https://crawl4ai.com/llms.txt
- Free Allowance: Completely free and open source self-hosted (unlimited requests); free cloud tier on community nodes
- Monthly Equivalent Requests (Single Account): 1,000,000
- Billing Cadence: Unlimited (Self-Hosted Open Source)
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; Playwright stealth mode, user agent spoofing, custom header injection, proxy pool support
- JavaScript Rendering: Full Playwright execution with Chromium, WebKit, and Firefox headless engines
- Supported Output Formats: Structured Markdown, fit markdown (noise removed), CSS/XPath extracted JSON, screenshot buffers
- Concurrency and Rate Limits: Bound only by local host CPU/RAM; supports async parallel scraping
- Post-Signup Bonuses and Unlocks: Zero commercial gates; fully open source under Apache 2.0 license
- Market Maturity and Ecosystem Awareness: Very High; 25k+ GitHub stars, one of the fastest growing open source web crawlers on GitHub

#### 8. Treg (Superdesign)

- Primary Domain: `https://treg.to`
- Category: AI Search, Reader and Neural Crawl Engines
- Home Page: https://treg.to
- Pricing Page: https://treg.to/web-access
- LLMs.txt / API Documentation: https://treg.to/llms.txt
- Free Allowance: Free WebAccess gateway routing to zero-cost vendor tiers (Tinyfish, Crawl4AI, etc.) with automatic fallback
- Monthly Equivalent Requests (Single Account): 50,000
- Billing Cadence: Monthly Recurring (Aggregator Gateway)
- Credit Card Required: No
- Anti-Bot Protection Bypass: Very High; cascades across 15+ underlying providers until a successful hit is achieved
- JavaScript Rendering: Delegates to downstream provider based on route preference (browserless, tinyfish, crawl4ai)
- Supported Output Formats: Normalized JSON search results, clean markdown page contents
- Concurrency and Rate Limits: Cascading rate limits governed by active upstream provider
- Post-Signup Bonuses and Unlocks: Provides live Web Arena leaderboard and direct access to zero-cost search and page reads
- Market Maturity and Ecosystem Awareness: Innovative multi-vendor proxy aggregator (2025-2026), open source tooling on GitHub

#### 9. Context.dev

- Primary Domain: `https://context.dev`
- Category: AI Search, Reader and Neural Crawl Engines
- Home Page: https://context.dev
- Pricing Page: https://context.dev
- LLMs.txt / API Documentation: https://docs.context.dev/llms.txt
- Free Allowance: 1,000 credits/month free allowance on grant-anchor day for all organizations
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: Monthly Recurring
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; automated stealth browsers and residential proxy routing for difficult domains
- JavaScript Rendering: Full browser automation with interactive actions, click, scroll, and wait
- Supported Output Formats: Structured schema JSON, cleaned markdown, prebuilt parsers for major platforms (App Store, etc.)
- Concurrency and Rate Limits: Organization-wide credit pool and concurrency limits
- Post-Signup Bonuses and Unlocks: Earn free credits program in dashboard; promotional redeem codes
- Market Maturity and Ecosystem Awareness: Growing enterprise web data platform with dedicated agent-first documentation

#### 10. Octen

- Primary Domain: `https://octen.ai`
- Category: AI Search, Reader and Neural Crawl Engines
- Home Page: https://octen.ai
- Pricing Page: https://octen.ai
- LLMs.txt / API Documentation: https://docs.octen.ai/llms.txt
- Free Allowance: $5 free balance on registration; up to 10 QPS Web Search on permanent $0 Free Plan
- Monthly Equivalent Requests (Single Account): 2,500
- Billing Cadence: One-Time Balance ($5) + Free 10 QPS Tier (first 10 results free per search)
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; enterprise web indexing and real-time retrieval network
- JavaScript Rendering: Server-side extraction and structured SERP synthesis
- Supported Output Formats: JSON search results with free full content for first 10 results, vector embeddings
- Concurrency and Rate Limits: 10 QPS on Free tier; 1,000,000 TPM embedding limits
- Post-Signup Bonuses and Unlocks: $5 automatic signup credit; 15% Model Gateway rebate program
- Market Maturity and Ecosystem Awareness: High-throughput search and model gateway for autonomous workflows

#### 11. You.com Web Search API

- Primary Domain: `https://you.com`
- Category: AI Search, Reader and Neural Crawl Engines
- Home Page: https://you.com
- Pricing Page: https://you.com/pricing
- LLMs.txt / API Documentation: https://you.com/docs/llms.txt
- Free Allowance: 1,000 free search queries/month or $5 free trial balance
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: Monthly Recurring
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; comprehensive web search index with live web scraping capabilities
- JavaScript Rendering: Index-based document retrieval and live snippet generation
- Supported Output Formats: JSON search results, web snippets, AI news summaries, research citations
- Concurrency and Rate Limits: Standard developer rate limits (up to 5 QPS on free tier)
- Post-Signup Bonuses and Unlocks: Developer credits for hackathon participants and university students
- Market Maturity and Ecosystem Awareness: High; pioneer consumer AI search engine founded by Richard Socher (ex-Salesforce Chief Scientist)

#### 12. Parallel

- Primary Domain: `https://parallel.ai`
- Category: AI Search, Reader and Neural Crawl Engines
- Home Page: https://parallel.ai
- Pricing Page: https://parallel.ai
- LLMs.txt / API Documentation: https://docs.parallel.ai/llms.txt
- Free Allowance: Free trial credits upon developer account creation ($5 credit allowance)
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; built-in web extract engine with synchronous low-latency pipeline (1-20s)
- JavaScript Rendering: Cloud browser extraction and document synthesis
- Supported Output Formats: Clean markdown, structured JSON entity records, image search results
- Concurrency and Rate Limits: Synchronous endpoints with custom rate limits per mode
- Post-Signup Bonuses and Unlocks: Volume pricing discounts and accelerator partner credits
- Market Maturity and Ecosystem Awareness: Agent-native web data pipeline specializing in list building (FindAll) and deep research

#### 13. Diffbot

- Primary Domain: `https://www.diffbot.com`
- Category: AI Search, Reader and Neural Crawl Engines
- Home Page: https://www.diffbot.com
- Pricing Page: https://www.diffbot.com/pricing
- LLMs.txt / API Documentation: https://www.diffbot.com/llms.txt
- Free Allowance: 10,000 extraction credits on 14-day free trial; free developer tier access
- Monthly Equivalent Requests (Single Account): 10,000
- Billing Cadence: One-Time 14-Day Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: Very High; proprietary computer vision and DOM parsing engine bypasses traditional anti-bot scripts
- JavaScript Rendering: Proprietary headless browser rendering with visual element identification
- Supported Output Formats: Structured schema JSON (Article, Product, Organization, Discussion, Knowledge Graph)
- Concurrency and Rate Limits: 5 concurrent requests on trial; high QPS on enterprise plans
- Post-Signup Bonuses and Unlocks: Knowledge Graph trial credits; startup program credits up to $10,000
- Market Maturity and Ecosystem Awareness: Very High; founded 2008, Stanford-incubated, powers Microsoft Bing and DuckDuckGo knowledge extraction

#### 14. DeepSeek Search & Fetch

- Primary Domain: `https://www.deepseek.com`
- Category: AI Search, Reader and Neural Crawl Engines
- Home Page: https://www.deepseek.com
- Pricing Page: https://platform.deepseek.com/api-docs/pricing
- LLMs.txt / API Documentation: https://platform.deepseek.com
- Free Allowance: 5,000,000 free tokens on registration; native web search integration in API
- Monthly Equivalent Requests (Single Account): 25,000
- Billing Cadence: One-Time Signup Balance
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; built-in search tool calling and web fetch primitives in BetterSearch skill
- JavaScript Rendering: Server-side web page reader and semantic distillation
- Supported Output Formats: Clean text citations, markdown extracts, structured model responses
- Concurrency and Rate Limits: High default concurrency on platform API
- Post-Signup Bonuses and Unlocks: Initial 5M token grant on phone/email verification
- Market Maturity and Ecosystem Awareness: Extreme; world-renowned open weights AI lab with massive global developer mindshare

#### 15. Perplexity (Sonar API)

- Primary Domain: `https://www.perplexity.ai`
- Category: AI Search, Reader and Neural Crawl Engines
- Home Page: https://www.perplexity.ai
- Pricing Page: https://www.perplexity.ai/pricing
- LLMs.txt / API Documentation: https://docs.perplexity.ai/llms.txt
- Free Allowance: $5 API credit on initial registration; free web tier with unlimited consumer search
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: Very High; live search indexing pipeline crawling hundreds of millions of web pages
- JavaScript Rendering: Continuous background crawler and real-time document retriever
- Supported Output Formats: Synthesized markdown with exact inline web citations and source URL arrays
- Concurrency and Rate Limits: Standard tier: 20-50 RPM depending on model endpoint
- Post-Signup Bonuses and Unlocks: $5 API credit for new developer platform accounts
- Market Maturity and Ecosystem Awareness: Extreme; premier conversational search platform, valued at multi-billions, ubiquitous in AI tech stack

#### 16. Olostep

- Primary Domain: `https://olostep.com`
- Category: AI Search, Reader and Neural Crawl Engines
- Home Page: https://olostep.com
- Pricing Page: https://olostep.com/pricing
- LLMs.txt / API Documentation: https://www.olostep.com/llms.txt
- Free Allowance: 500 free requests on Trial tier; no credit card required
- Monthly Equivalent Requests (Single Account): 500
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: Very High; residential proxy routing, stealth browser fingerprints, bypasses Cloudflare & Datadome
- JavaScript Rendering: Headless Chrome with custom user interactions, auto-scrolling, and CAPTCHA solving
- Supported Output Formats: Clean markdown, structured JSON, full HTML DOM
- Concurrency and Rate Limits: 5 concurrent requests on free trial
- Post-Signup Bonuses and Unlocks: Pay-as-you-go credit packs starting at $20 without monthly subscription commitment
- Market Maturity and Ecosystem Awareness: Emerging headless scraper built specifically for AI agents, prominent in Treg benchmarks

#### 17. Search1API

- Primary Domain: `https://search1api.com`
- Category: AI Search, Reader and Neural Crawl Engines
- Home Page: https://search1api.com
- Pricing Page: https://search1api.com
- LLMs.txt / API Documentation: https://s1.dev/llms.txt
- Free Allowance: 100 free credits on Free Plan; all features unlocked with lower concurrency
- Monthly Equivalent Requests (Single Account): 100
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; dedicated agentic search router with residential proxy backing
- JavaScript Rendering: Agentic search and scrape pipeline with automated intent routing
- Supported Output Formats: Structured search JSON, clean web extracts, answer synthesis
- Concurrency and Rate Limits: Lower concurrency on free tier, scalable with prepaid top-ups
- Post-Signup Bonuses and Unlocks: Prepaid top-up bonus up to +60% additional credits ($499 gets 798,400 credits)
- Market Maturity and Ecosystem Awareness: AI agent infrastructure platform (s1.dev) providing unified search and proxy endpoints

#### 18. Linkup

- Primary Domain: `https://linkup.so`
- Category: AI Search, Reader and Neural Crawl Engines
- Home Page: https://linkup.so
- Pricing Page: https://linkup.so/pricing
- LLMs.txt / API Documentation: https://www.linkup.so/llms.txt
- Free Allowance: Free trial tier with 1,000 search queries on signup
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; proprietary search indexing and retrieval system designed for enterprise LLMs
- JavaScript Rendering: Server-side page rendering and structured extraction
- Supported Output Formats: JSON search results, verified factual snippets, source attribution
- Concurrency and Rate Limits: Standard developer rate limits (up to 10 QPS)
- Post-Signup Bonuses and Unlocks: Free developer tier with instant API key generation
- Market Maturity and Ecosystem Awareness: European AI search infrastructure startup, partnered with Mistral AI and major European tech firms

#### 19. ScrapeGraphAI

- Primary Domain: `https://scrapegraphai.com`
- Category: AI Search, Reader and Neural Crawl Engines
- Home Page: https://scrapegraphai.com
- Pricing Page: https://scrapegraphai.com
- LLMs.txt / API Documentation: https://scrapegraphai.com/llms.txt
- Free Allowance: Open source Python library (100% free unlimited); free cloud API trial tier (100 requests)
- Monthly Equivalent Requests (Single Account): 100,000
- Billing Cadence: Unlimited (Open Source) + 100 Cloud API Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; integration with Playwright, Undetected-Chromedriver, and rotating proxy networks
- JavaScript Rendering: Full Playwright and Chromium headless browser automation
- Supported Output Formats: Schema-validated JSON, clean markdown, graph pipeline summaries
- Concurrency and Rate Limits: Locally unconstrained; cloud API rate limited
- Post-Signup Bonuses and Unlocks: Zero commercial gates for open source; 16k+ GitHub stars community
- Market Maturity and Ecosystem Awareness: Very High; viral open-source AI scraping framework with 16k+ GitHub stars and active Discord community

#### 20. Spider (SpiderCloud)

- Primary Domain: `https://spider.cloud`
- Category: AI Search, Reader and Neural Crawl Engines
- Home Page: https://spider.cloud
- Pricing Page: https://spider.cloud/pricing
- LLMs.txt / API Documentation: https://spider.cloud/llms.txt
- Free Allowance: 500 pages free crawl/scrape credits on signup ($5 value); open source Rust core available
- Monthly Equivalent Requests (Single Account): 500
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: Very High; high-speed headless browser engine in Rust, stealth mode, automated CAPTCHA avoidance
- JavaScript Rendering: Ultra-fast headless browser rendering and raw HTTP hybrid pipeline
- Supported Output Formats: Clean markdown, raw HTML, structured JSON, AI text embeddings
- Concurrency and Rate Limits: Up to 5 concurrent browser workers on free trial
- Post-Signup Bonuses and Unlocks: Open source engine (spider-rs) available on GitHub with zero limits
- Market Maturity and Ecosystem Awareness: High; recognized as the fastest web crawler engine in Rust, 5k+ GitHub stars

---

### 1.2 Dedicated SERP and Search Engine APIs (21 to 45)

#### 21. Serper

- Primary Domain: `https://serper.dev`
- Category: Dedicated SERP and Search Engine APIs
- Home Page: https://serper.dev
- Pricing Page: https://serper.dev/pricing
- LLMs.txt / API Documentation: https://serper.dev
- Free Allowance: 2,500 free Google search queries on registration; no credit card required
- Monthly Equivalent Requests (Single Account): 2,500
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: Extreme; specialized Google SERP scraper bypassing Google rate limits and CAPTCHAs
- JavaScript Rendering: Full SERP parsing for knowledge graphs, sitelinks, news, images, and videos
- Supported Output Formats: Clean structured JSON matching Google SERP elements
- Concurrency and Rate Limits: High concurrency (up to 50 concurrent requests)
- Post-Signup Bonuses and Unlocks: Direct API key generation upon email verification; volume prepaid rates ($0.001/query)
- Market Maturity and Ecosystem Awareness: Very High; standard Google SERP API for AI developers, powers thousands of Cloudflare Worker gateways

#### 22. Brave Search API

- Primary Domain: `https://brave.com/search/api/`
- Category: Dedicated SERP and Search Engine APIs
- Home Page: https://brave.com/search/api/
- Pricing Page: https://brave.com/search/api/#pricing
- LLMs.txt / API Documentation: https://brave.com/search/api/
- Free Allowance: 2,000 free queries/month on Free Plan (1 req/sec rate limit)
- Monthly Equivalent Requests (Single Account): 2,000
- Billing Cadence: Monthly Recurring
- Credit Card Required: Yes
- Anti-Bot Protection Bypass: Extreme; 100% independent web search index independent of Google or Bing
- JavaScript Rendering: Index-based SERP retrieval with summary key points and document clustering
- Supported Output Formats: Structured JSON with title, URL, description, extra snippets, and LLM context format
- Concurrency and Rate Limits: 1 request per second on Free Plan
- Post-Signup Bonuses and Unlocks: AI Grounding and Web Search endpoints both available on free credits
- Market Maturity and Ecosystem Awareness: Extreme; privacy browser and search engine with over 60 million active users

#### 23. SerpApi

- Primary Domain: `https://serpapi.com`
- Category: Dedicated SERP and Search Engine APIs
- Home Page: https://serpapi.com
- Pricing Page: https://serpapi.com/pricing
- LLMs.txt / API Documentation: https://serpapi.com/llms.txt
- Free Allowance: 100 free searches/month recurring; no credit card required
- Monthly Equivalent Requests (Single Account): 100
- Billing Cadence: Monthly Recurring
- Credit Card Required: No
- Anti-Bot Protection Bypass: Extreme; supports Google, Bing, Baidu, Yahoo, Yandex, DuckDuckGo, eBay, Walmart, YouTube
- JavaScript Rendering: Full page rendering and visual parsing across all supported search engines
- Supported Output Formats: Comprehensive normalized JSON with all SERP rich snippets and raw HTML backup
- Concurrency and Rate Limits: 1 request per second on free tier
- Post-Signup Bonuses and Unlocks: Developer advocate and educational grants available upon request
- Market Maturity and Ecosystem Awareness: Very High; pioneer SERP scraper (founded 2017), trusted by over 50,000 developers

#### 24. SearchApi.io

- Primary Domain: `https://www.searchapi.io`
- Category: Dedicated SERP and Search Engine APIs
- Home Page: https://www.searchapi.io
- Pricing Page: https://www.searchapi.io/pricing
- LLMs.txt / API Documentation: https://www.searchapi.io
- Free Allowance: 100 free searches on signup; no credit card required
- Monthly Equivalent Requests (Single Account): 100
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: Very High; real-time Google, Google News, Google Scholar, Bing, and Amazon scraping
- JavaScript Rendering: Dynamic SERP rendering with location-based geolocation targeting
- Supported Output Formats: Structured JSON with rich answers, organic results, related questions
- Concurrency and Rate Limits: 5 concurrent requests on trial
- Post-Signup Bonuses and Unlocks: Instant API key delivery; volume top-up discounts
- Market Maturity and Ecosystem Awareness: High; modern SERP API alternative with extensive SDK support (Python, JS, Go)

#### 25. Google Programmable Search JSON API

- Primary Domain: `https://developers.google.com/custom-search`
- Category: Dedicated SERP and Search Engine APIs
- Home Page: https://developers.google.com/custom-search
- Pricing Page: https://developers.google.com/custom-search/v1/overview
- LLMs.txt / API Documentation: https://developers.google.com
- Free Allowance: 100 search queries/day free (approx. 3,000 queries/month) via Google Cloud Console
- Monthly Equivalent Requests (Single Account): 3,000
- Billing Cadence: Daily Resets (Monthly Recurring)
- Credit Card Required: No
- Anti-Bot Protection Bypass: Native; official Google Cloud developer API, never blocked or throttled
- JavaScript Rendering: Google's internal search index ranking and snippet extraction
- Supported Output Formats: Standard Google REST JSON with searchInformation, items, pagemap, and metadata
- Concurrency and Rate Limits: 100 queries/day free; additional queries bill at $5 per 1,000 up to 10k/day
- Post-Signup Bonuses and Unlocks: Access to Google Cloud free tier ($300 trial credit for new Google Cloud billing accounts)
- Market Maturity and Ecosystem Awareness: Extreme; official Google service maintained directly by Google

#### 26. Bing Web Search API (Azure F0)

- Primary Domain: `https://www.microsoft.com/en-us/bing/apis/bing-web-search-api`
- Category: Dedicated SERP and Search Engine APIs
- Home Page: https://www.microsoft.com/en-us/bing/apis/bing-web-search-api
- Pricing Page: https://azure.microsoft.com/en-us/pricing/details/cognitive-services/search-api/web/
- LLMs.txt / API Documentation: https://learn.microsoft.com/en-us/bing/search-apis/bing-web-search/overview
- Free Allowance: 1,000 transactions/month free on Azure F0 Free Tier (3 QPS rate limit)
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: Monthly Recurring
- Credit Card Required: Yes
- Anti-Bot Protection Bypass: Native; official Microsoft Azure Cognitive Services search infrastructure
- JavaScript Rendering: Direct access to Bing search index with deep entity matching
- Supported Output Formats: JSON with webPages, rankingResponse, relatedSearches, and news clusters
- Concurrency and Rate Limits: 3 queries per second on F0 tier
- Post-Signup Bonuses and Unlocks: $200 Azure credit for 30 days upon creating a new Azure account
- Market Maturity and Ecosystem Awareness: Extreme; enterprise standard web search index powering Microsoft Copilot and Yahoo

#### 27. DataForSEO

- Primary Domain: `https://dataforseo.com`
- Category: Dedicated SERP and Search Engine APIs
- Home Page: https://dataforseo.com
- Pricing Page: https://dataforseo.com/pricing
- LLMs.txt / API Documentation: https://dataforseo.com/llms.txt
- Free Allowance: $1 free sandbox balance upon registration (yields ~1,600 SERP requests at $0.0006/req)
- Monthly Equivalent Requests (Single Account): 1,600
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: Extreme; industrial-grade SERP and scraping infrastructure across 100+ countries
- JavaScript Rendering: Full headless browser rendering for Google, Bing, Yahoo, Baidu, Amazon, App Store
- Supported Output Formats: Exhaustive JSON SERP breakdown with pixel coordinates, raw HTML, and markdown
- Concurrency and Rate Limits: 2,000 calls per minute; highly scalable asynchronous postback API
- Post-Signup Bonuses and Unlocks: Live support chat setup bonus; developer consultation call credits
- Market Maturity and Ecosystem Awareness: Very High; backbone provider for major SEO software platforms (Ahrefs, Semrush partners)

#### 28. HasData

- Primary Domain: `https://hasdata.com`
- Category: Dedicated SERP and Search Engine APIs
- Home Page: https://hasdata.com
- Pricing Page: https://hasdata.com/pricing
- LLMs.txt / API Documentation: https://hasdata.com/llms.txt
- Free Allowance: 1,000 free credits on trial registration; no credit card required
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: Very High; residential proxy rotators, automated CAPTCHA bypass, Google/Amazon/Zillow parsers
- JavaScript Rendering: Full browser automation with custom headers, cookies, and waiting selectors
- Supported Output Formats: Structured JSON, clean markdown, raw HTML, screenshot captures
- Concurrency and Rate Limits: 5 concurrent requests on trial
- Post-Signup Bonuses and Unlocks: Discount coupons for developers upon email confirmation
- Market Maturity and Ecosystem Awareness: High; fast-growing scraping and SERP provider known for accurate e-commerce extraction

#### 29. Zenserp

- Primary Domain: `https://zenserp.com`
- Category: Dedicated SERP and Search Engine APIs
- Home Page: https://zenserp.com
- Pricing Page: https://zenserp.com/pricing
- LLMs.txt / API Documentation: https://zenserp.com/llms.txt
- Free Allowance: 50 searches/month free recurring; no credit card required
- Monthly Equivalent Requests (Single Account): 50
- Billing Cadence: Monthly Recurring
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; automated IP rotation, geolocation targeting down to city level
- JavaScript Rendering: Full SERP parsing for Google organic, maps, news, shopping, and images
- Supported Output Formats: Structured JSON with clean extraction of all Google snippet types
- Concurrency and Rate Limits: 1 request per second on free plan
- Post-Signup Bonuses and Unlocks: Instant API key delivery; annual plan discounts (20% off)
- Market Maturity and Ecosystem Awareness: High; established Austrian SERP API provider operating since 2018

#### 30. Serpstack

- Primary Domain: `https://serpstack.com`
- Category: Dedicated SERP and Search Engine APIs
- Home Page: https://serpstack.com
- Pricing Page: https://serpstack.com/pricing
- LLMs.txt / API Documentation: https://serpstack.com/llms.txt
- Free Allowance: 100 searches/month free recurring; no credit card required
- Monthly Equivalent Requests (Single Account): 100
- Billing Cadence: Monthly Recurring
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; part of APILayer network, global proxy pool with real-time browser emulation
- JavaScript Rendering: Server-side SERP rendering and parsing
- Supported Output Formats: Clean JSON and CSV output formats
- Concurrency and Rate Limits: Standard rate limits for free tier; HTTPS encryption on paid tiers
- Post-Signup Bonuses and Unlocks: APILayer universal account access across 40+ microservice APIs
- Market Maturity and Ecosystem Awareness: Very High; owned by Idera Inc. / APILayer, highly reliable enterprise infrastructure

#### 31. ValueSERP

- Primary Domain: `https://valueserp.com`
- Category: Dedicated SERP and Search Engine APIs
- Home Page: https://valueserp.com
- Pricing Page: https://valueserp.com/pricing
- LLMs.txt / API Documentation: https://valueserp.com/llms.txt
- Free Allowance: 100 free searches/month recurring; no credit card required
- Monthly Equivalent Requests (Single Account): 100
- Billing Cadence: Monthly Recurring
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; specialized budget Google SERP engine by Traject Data
- JavaScript Rendering: Fast Google SERP scraping with location emulation
- Supported Output Formats: Structured JSON, CSV, and HTML results
- Concurrency and Rate Limits: 1 request per second on free tier
- Post-Signup Bonuses and Unlocks: Ultra low cost overage rates ($1.50 per 1,000 queries)
- Market Maturity and Ecosystem Awareness: High; part of Traject Data suite (ScaleSERP, ValueSERP) widely used for bulk SEO monitoring

#### 32. ScaleSERP

- Primary Domain: `https://scaleserp.com`
- Category: Dedicated SERP and Search Engine APIs
- Home Page: https://scaleserp.com
- Pricing Page: https://scaleserp.com/pricing
- LLMs.txt / API Documentation: https://scaleserp.com/llms.txt
- Free Allowance: 125 free searches/month recurring; no credit card required
- Monthly Equivalent Requests (Single Account): 125
- Billing Cadence: Monthly Recurring
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; enterprise scale SERP scraping across all Google search tabs
- JavaScript Rendering: High-throughput cloud scraping cluster with automatic IP rotation
- Supported Output Formats: Clean JSON with detailed search metadata
- Concurrency and Rate Limits: 1 request per second on free tier
- Post-Signup Bonuses and Unlocks: Free trial upgrades for enterprise evaluation
- Market Maturity and Ecosystem Awareness: High; sister platform to ValueSERP optimized for high-volume batch processing

#### 33. Serply

- Primary Domain: `https://serply.io`
- Category: Dedicated SERP and Search Engine APIs
- Home Page: https://serply.io
- Pricing Page: https://serply.io/pricing
- LLMs.txt / API Documentation: https://serply.io/llms.txt
- Free Allowance: 100 free searches/month recurring; no credit card required
- Monthly Equivalent Requests (Single Account): 100
- Billing Cadence: Monthly Recurring
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; developer-first SERP and web scraping API built on serverless cloud
- JavaScript Rendering: Serverless browser execution with geo-located proxies
- Supported Output Formats: Clean JSON for Google Search, Google News, and Web Scrape endpoints
- Concurrency and Rate Limits: 1 request per second
- Post-Signup Bonuses and Unlocks: Instant setup with cURL and Python code generators
- Market Maturity and Ecosystem Awareness: Mid; developer favorite for lightweight serverless scripts and microservices

#### 34. Serpdog

- Primary Domain: `https://serpdog.com`
- Category: Dedicated SERP and Search Engine APIs
- Home Page: https://serpdog.com
- Pricing Page: https://serpdog.com/pricing
- LLMs.txt / API Documentation: https://serpdog.com
- Free Allowance: 1,000 free searches on signup; no credit card required
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: Very High; rotating residential proxies and browser fingerprint randomization
- JavaScript Rendering: Full Google SERP extraction for shopping, maps, news, organic, and auto-suggest
- Supported Output Formats: Parsed JSON, raw HTML
- Concurrency and Rate Limits: 5 concurrent requests
- Post-Signup Bonuses and Unlocks: Generous initial 1,000 credit package for testing
- Market Maturity and Ecosystem Awareness: High; popular low-cost SerpApi alternative with 99.9% uptime track record

#### 35. SerpWow

- Primary Domain: `https://serpwow.com`
- Category: Dedicated SERP and Search Engine APIs
- Home Page: https://serpwow.com
- Pricing Page: https://serpwow.com/pricing
- LLMs.txt / API Documentation: https://serpwow.com
- Free Allowance: 100 free searches on signup trial; no credit card required
- Monthly Equivalent Requests (Single Account): 100
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; multi-engine SERP parser supporting Google, Bing, Yahoo, Baidu, and Yandex
- JavaScript Rendering: Desktop, mobile, and tablet browser emulation
- Supported Output Formats: Normalized JSON and CSV across all supported engines
- Concurrency and Rate Limits: 1 request per second
- Post-Signup Bonuses and Unlocks: API testing playground in web dashboard
- Market Maturity and Ecosystem Awareness: High; established worldwide SERP tracking engine

#### 36. Mojeek Search API

- Primary Domain: `https://www.mojeek.com`
- Category: Dedicated SERP and Search Engine APIs
- Home Page: https://www.mojeek.com
- Pricing Page: https://www.mojeek.com/services/search/api/
- LLMs.txt / API Documentation: https://www.mojeek.com/services/search/api/
- Free Allowance: Free trial allowance of 1,000 search queries on registration
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: Native; 100% independent crawler and search index based in the UK (over 8 billion pages)
- JavaScript Rendering: Independent index lookup, zero tracking or profiling
- Supported Output Formats: Structured XML and JSON search results
- Concurrency and Rate Limits: Standard developer rate limit
- Post-Signup Bonuses and Unlocks: Privacy-first search community discounts and custom crawl requests
- Market Maturity and Ecosystem Awareness: High; independent search engine pioneer operating its own crawler since 2004

#### 37. Kagi Search API

- Primary Domain: `https://kagi.com`
- Category: Dedicated SERP and Search Engine APIs
- Home Page: https://kagi.com
- Pricing Page: https://kagi.com/pricing
- LLMs.txt / API Documentation: https://help.kagi.com/kagi/api/overview.html
- Free Allowance: Free trial search queries on new user signup (approx. 100 searches); Universal Summarizer API access
- Monthly Equivalent Requests (Single Account): 100
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: Native; premium ad-free search engine aggregating non-commercial and high-quality web sources
- JavaScript Rendering: Teclis search index + syndicated feeds with enriched meta-summaries
- Supported Output Formats: Clean JSON with ranking, summary text, and discussion forum lenses
- Concurrency and Rate Limits: Rate limited per API key tier
- Post-Signup Bonuses and Unlocks: Includes access to FastGPT and Universal Summarizer endpoints
- Market Maturity and Ecosystem Awareness: Very High; beloved privacy search engine with massive developer cult following

#### 38. SearXNG (Self-Hosted Meta-Search)

- Primary Domain: `https://docs.searxng.org`
- Category: Dedicated SERP and Search Engine APIs
- Home Page: https://docs.searxng.org
- Pricing Page: https://docs.searxng.org
- LLMs.txt / API Documentation: https://docs.searxng.org
- Free Allowance: 100% free and open source self-hosted (Docker); unlimited queries across 70+ search engines
- Monthly Equivalent Requests (Single Account): 1,000,000
- Billing Cadence: Unlimited (Self-Hosted Open Source)
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; aggregates queries across Google, Bing, DuckDuckGo, Brave, Wikipedia, Mojeek with proxy support
- JavaScript Rendering: Server-side aggregation and HTML/JSON stripping
- Supported Output Formats: Standard JSON (append format=json), RSS, OpenSearch XML
- Concurrency and Rate Limits: Locally unconstrained; configurable outbound rate limit per engine
- Post-Signup Bonuses and Unlocks: Zero commercial gates, AGPLv3 licensed, completely sovereign
- Market Maturity and Ecosystem Awareness: Extreme; 15k+ GitHub stars, the gold standard for private, self-hosted meta-search engines

#### 39. DuckDuckGo Lite / HTML Search

- Primary Domain: `https://duckduckgo.com`
- Category: Dedicated SERP and Search Engine APIs
- Home Page: https://duckduckgo.com
- Pricing Page: https://duckduckgo.com
- LLMs.txt / API Documentation: https://duckduckgo.com
- Free Allowance: Unlimited free anonymous search via HTML/Lite endpoints and duckduckgo-search Python package
- Monthly Equivalent Requests (Single Account): 50,000
- Billing Cadence: Unlimited (Rate-Limited Anonymous Free)
- Credit Card Required: No
- Anti-Bot Protection Bypass: Medium; rate limited by IP, easily rotated through residential/datacenter proxy pool
- JavaScript Rendering: Lightweight HTML parsing without requiring JavaScript execution
- Supported Output Formats: Clean HTML elements, parsed JSON via duckduckgo-search SDK
- Concurrency and Rate Limits: Approx. 1 request every 2-3 seconds per IP to avoid temporary 429
- Post-Signup Bonuses and Unlocks: No signup or account registration ever needed
- Market Maturity and Ecosystem Awareness: Extreme; default privacy search engine globally recognized with 100M+ daily searches

#### 40. Valyu Network

- Primary Domain: `https://valyu.network`
- Category: Dedicated SERP and Search Engine APIs
- Home Page: https://valyu.network
- Pricing Page: https://valyu.network
- LLMs.txt / API Documentation: https://www.valyu.ai/llms.txt
- Free Allowance: Free trial credits upon developer account creation ($5 credit allowance)
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; decentralized crawler network with automated incentive layer for web data indexing
- JavaScript Rendering: Decentralized node crawling and text extraction
- Supported Output Formats: JSON search results with verified data provenance and citations
- Concurrency and Rate Limits: Standard developer rate limits
- Post-Signup Bonuses and Unlocks: Cryptographic proof of retrieval and developer grants
- Market Maturity and Ecosystem Awareness: Emerging decentralized web search and AI data protocol

#### 41. Branddev

- Primary Domain: `https://brand.dev`
- Category: Dedicated SERP and Search Engine APIs
- Home Page: https://brand.dev
- Pricing Page: https://brand.dev
- LLMs.txt / API Documentation: https://brand.dev/docs
- Free Allowance: 1,000 free API calls on developer signup; no credit card required
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; specialized brand, company, domain intelligence and sitemap crawler
- JavaScript Rendering: Server-side headless browser rendering for company assets, logos, and meta data
- Supported Output Formats: Structured JSON with brand colors, fonts, social links, and company descriptions
- Concurrency and Rate Limits: 5 requests per second
- Post-Signup Bonuses and Unlocks: Free developer tier with instant API key access
- Market Maturity and Ecosystem Awareness: High; prominent provider on Treg leaderboard for sitemap discovery and brand search

#### 42. Sixtyfour AI

- Primary Domain: `https://sixtyfour.ai`
- Category: Dedicated SERP and Search Engine APIs
- Home Page: https://sixtyfour.ai
- Pricing Page: https://sixtyfour.ai
- LLMs.txt / API Documentation: https://docs.sixtyfour.ai
- Free Allowance: Free developer trial allowance (500 free search & extraction requests)
- Monthly Equivalent Requests (Single Account): 500
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; AI-powered search and real-time structured data extraction from live web pages
- JavaScript Rendering: Cloud browser extraction and schema matching
- Supported Output Formats: Typed JSON schema matching requested fields
- Concurrency and Rate Limits: Standard rate limits for trial tier
- Post-Signup Bonuses and Unlocks: Access to advanced entity extraction models
- Market Maturity and Ecosystem Awareness: Emerging AI web extraction platform featured in modern agent workflows

#### 43. Cloro

- Primary Domain: `https://cloro.dev`
- Category: Dedicated SERP and Search Engine APIs
- Home Page: https://cloro.dev
- Pricing Page: https://cloro.dev
- LLMs.txt / API Documentation: https://docs.cloro.dev
- Free Allowance: Free trial allowance for news search and web sitemap extraction (500 calls)
- Monthly Equivalent Requests (Single Account): 500
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; real-time news retrieval and live domain sitemap indexing
- JavaScript Rendering: Server-side feed processing and web document extraction
- Supported Output Formats: Structured news JSON, sitemap URL hierarchies, article bodies
- Concurrency and Rate Limits: 5 QPS on trial tier
- Post-Signup Bonuses and Unlocks: Featured on Treg Web Arena for low-latency news search
- Market Maturity and Ecosystem Awareness: Specialized real-time web news and sitemap engine

#### 44. BlitzAPI

- Primary Domain: `https://blitzapi.com`
- Category: Dedicated SERP and Search Engine APIs
- Home Page: https://blitzapi.com
- Pricing Page: https://blitzapi.com
- LLMs.txt / API Documentation: https://blitzapi.com
- Free Allowance: 500 free requests on developer registration; no credit card required
- Monthly Equivalent Requests (Single Account): 500
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; fast edge-cached SERP and web scraping proxy layer
- JavaScript Rendering: Optimized lightweight DOM parser and headless Chrome pool
- Supported Output Formats: JSON search results, clean text extracts
- Concurrency and Rate Limits: 5 concurrent requests
- Post-Signup Bonuses and Unlocks: Instant API key delivery; volume pricing tiers
- Market Maturity and Ecosystem Awareness: Low-latency API gateway listed in treg provider catalog

#### 45. JustOneAPI

- Primary Domain: `https://justoneapi.com`
- Category: Dedicated SERP and Search Engine APIs
- Home Page: https://justoneapi.com
- Pricing Page: https://justoneapi.com
- LLMs.txt / API Documentation: https://justoneapi.com
- Free Allowance: Free developer trial credits ($5 value) upon account creation
- Monthly Equivalent Requests (Single Account): 500
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; social media and video platform scraper (YouTube, Reddit, TikTok, X)
- JavaScript Rendering: Platform-specific headless browser emulation and mobile app API spoofing
- Supported Output Formats: Structured video metadata, transcripts, comments, and engagement metrics
- Concurrency and Rate Limits: Standard rate limits for trial tier
- Post-Signup Bonuses and Unlocks: Top performer on Treg YouTube/social retrieval leaderboard
- Market Maturity and Ecosystem Awareness: Specialized multi-platform media and video metadata gateway

---

### 1.3 Heavyweight Web Scraping and Unblocking APIs (46 to 70)

#### 46. Webscraping.ai

- Primary Domain: `https://webscraping.ai`
- Category: Heavyweight Web Scraping and Unblocking APIs
- Home Page: https://webscraping.ai
- Pricing Page: https://webscraping.ai/pricing
- LLMs.txt / API Documentation: https://webscraping.ai/llms.txt
- Free Allowance: 2,000 requests/month free recurring; no credit card required
- Monthly Equivalent Requests (Single Account): 2,000
- Billing Cadence: Monthly Recurring
- Credit Card Required: No
- Anti-Bot Protection Bypass: Very High; automated rotating proxies, browser fingerprint spoofing, CAPTCHA handling
- JavaScript Rendering: Headless Chrome with custom JS execution and wait parameters
- Supported Output Formats: Clean text, markdown, HTML, or structured JSON via AI question answering
- Concurrency and Rate Limits: 5 concurrent requests on free plan
- Post-Signup Bonuses and Unlocks: Permanent free tier with 2,000 monthly allowance; no credit card needed ever
- Market Maturity and Ecosystem Awareness: High; established scraper API with native AI-powered parsing capabilities

#### 47. Scrape.do

- Primary Domain: `https://scrape.do`
- Category: Heavyweight Web Scraping and Unblocking APIs
- Home Page: https://scrape.do
- Pricing Page: https://scrape.do/pricing/
- LLMs.txt / API Documentation: https://scrape.do/llms.txt
- Free Allowance: 1,000 successful API calls/month free recurring; no credit card required
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: Monthly Recurring
- Credit Card Required: No
- Anti-Bot Protection Bypass: Extreme; residential proxy pool of 95M+ IPs, Cloudflare Turnstile, Datadome, Kasada bypass
- JavaScript Rendering: Full Chrome rendering with custom headers, cookies, geolocation, and device profiles
- Supported Output Formats: Clean HTML, markdown, JSON, binary responses
- Concurrency and Rate Limits: 5 concurrent connections on free plan
- Post-Signup Bonuses and Unlocks: Bills only for successful requests (200 OK); 4xx/5xx errors cost zero credits
- Market Maturity and Ecosystem Awareness: Very High; trusted by over 25,000 developers for mission-critical e-commerce scraping

#### 48. ScrapingAnt

- Primary Domain: `https://scrapingant.com`
- Category: Heavyweight Web Scraping and Unblocking APIs
- Home Page: https://scrapingant.com
- Pricing Page: https://scrapingant.com/pricing
- LLMs.txt / API Documentation: https://scrapingant.com
- Free Allowance: 1,000 API credits/month free recurring; no credit card required
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: Monthly Recurring
- Credit Card Required: No
- Anti-Bot Protection Bypass: Very High; rotating residential and datacenter proxies, Cloudflare and PerimeterX bypass
- JavaScript Rendering: Full Chrome headless browser cluster with custom JavaScript execution
- Supported Output Formats: HTML DOM, clean text, markdown, full-page screenshot (PNG/JPEG)
- Concurrency and Rate Limits: 1 concurrent request on free plan
- Post-Signup Bonuses and Unlocks: Free plan resets every month automatically without payment details
- Market Maturity and Ecosystem Awareness: High; popular developer-friendly web scraping API with extensive documentation

#### 49. ScrapingBee

- Primary Domain: `https://www.scrapingbee.com`
- Category: Heavyweight Web Scraping and Unblocking APIs
- Home Page: https://www.scrapingbee.com
- Pricing Page: https://www.scrapingbee.com/pricing/
- LLMs.txt / API Documentation: https://www.scrapingbee.com/llms.txt
- Free Allowance: 1,000 free API credits on signup trial; no credit card required
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: Extreme; massive rotating proxy network, sophisticated anti-scraping evasion, CAPTCHA solving
- JavaScript Rendering: Headless Chrome with custom scripts, wait conditions, screenshot captures, and scroll automation
- Supported Output Formats: Raw HTML, clean markdown, JSON data extraction rules, screenshots
- Concurrency and Rate Limits: 5 concurrent requests on trial
- Post-Signup Bonuses and Unlocks: Comprehensive scraping tutorials and open source Python/Node SDKs
- Market Maturity and Ecosystem Awareness: Very High; market-leading web scraping API founded in 2019, trusted by Deloitte and SAP

#### 50. ScraperAPI

- Primary Domain: `https://www.scraperapi.com`
- Category: Heavyweight Web Scraping and Unblocking APIs
- Home Page: https://www.scraperapi.com
- Pricing Page: https://www.scraperapi.com/pricing/
- LLMs.txt / API Documentation: https://www.scraperapi.com/llms.txt
- Free Allowance: 5,000 free API credits on 7-day signup trial; no credit card required
- Monthly Equivalent Requests (Single Account): 5,000
- Billing Cadence: One-Time 7-Day Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: Extreme; IP pool of over 40M proxies, smart IP rotation, automatic retries on failure
- JavaScript Rendering: Headless browser rendering (render=true parameter) with custom wait times
- Supported Output Formats: Clean HTML, JSON SERP results, raw web documents
- Concurrency and Rate Limits: 5 concurrent threads on free trial
- Post-Signup Bonuses and Unlocks: Extended trial credits upon contacting support; only charges for successful 200 responses
- Market Maturity and Ecosystem Awareness: Very High; pioneer scraping proxy API (founded 2018), handles billions of requests monthly

#### 51. ZenRows

- Primary Domain: `https://www.zenrows.com`
- Category: Heavyweight Web Scraping and Unblocking APIs
- Home Page: https://www.zenrows.com
- Pricing Page: https://www.zenrows.com/pricing
- LLMs.txt / API Documentation: https://www.zenrows.com/llms.txt
- Free Allowance: 1,000 free API credits on signup trial; no credit card required
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: Extreme; specialized in defeating Cloudflare Turnstile, Datadome, Kasada, Akamai, PerimeterX
- JavaScript Rendering: Full browser automation with interactive actions (click, scroll, keystrokes)
- Supported Output Formats: Clean HTML, CSS selector auto-parsing, markdown, screenshot capture
- Concurrency and Rate Limits: 5 concurrent requests on trial
- Post-Signup Bonuses and Unlocks: Developer community discounts and automated failure detection
- Market Maturity and Ecosystem Awareness: Very High; industry benchmark for defeating advanced bot-management systems

#### 52. Crawlbase (formerly ProxyCrawl)

- Primary Domain: `https://crawlbase.com`
- Category: Heavyweight Web Scraping and Unblocking APIs
- Home Page: https://crawlbase.com
- Pricing Page: https://crawlbase.com/pricing/
- LLMs.txt / API Documentation: https://crawlbase.com/llms.txt
- Free Allowance: 1,000 free requests on signup trial; no credit card required
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: Extreme; proprietary crawler and scraper API with millions of residential IPs worldwide
- JavaScript Rendering: Crawling API (raw HTTP) and JavaScript Scraping API with headless browser rendering
- Supported Output Formats: Clean HTML, structured JSON for Amazon, Google, LinkedIn, and Instagram
- Concurrency and Rate Limits: 10 concurrent requests on trial
- Post-Signup Bonuses and Unlocks: Free storage on Crawlbase Cloud Storage layer for scraped payloads
- Market Maturity and Ecosystem Awareness: Very High; rebrand of ProxyCrawl, in continuous operation since 2018

#### 53. Scrapfly

- Primary Domain: `https://scrapfly.io`
- Category: Heavyweight Web Scraping and Unblocking APIs
- Home Page: https://scrapfly.io
- Pricing Page: https://scrapfly.io/pricing
- LLMs.txt / API Documentation: https://scrapfly.io/llms.txt
- Free Allowance: 1,000 free API credits on signup trial; no credit card required
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: Extreme; Anti-Scraping Protection (ASP) engine specifically engineered for Datadome and Cloudflare
- JavaScript Rendering: Real Chrome browser rendering with full DevTools protocol access and visual debugging
- Supported Output Formats: Clean HTML, markdown, JSON, screenshot, session replay video
- Concurrency and Rate Limits: 1-3 concurrent browsers on trial
- Post-Signup Bonuses and Unlocks: Web scraping playground with live sandbox inspection in browser dashboard
- Market Maturity and Ecosystem Awareness: Very High; highly respected technical engineering blog and scraper tooling suite

#### 54. ScrapingDog

- Primary Domain: `https://www.scrapingdog.com`
- Category: Heavyweight Web Scraping and Unblocking APIs
- Home Page: https://www.scrapingdog.com
- Pricing Page: https://www.scrapingdog.com/pricing/
- LLMs.txt / API Documentation: https://www.scrapingdog.com/llms.txt
- Free Allowance: 1,000 free credits on registration; no credit card required
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: Very High; millions of rotating residential proxies, handles CAPTCHAs and headers
- JavaScript Rendering: Headless Chrome rendering with custom wait intervals and JavaScript execution
- Supported Output Formats: Raw HTML, structured JSON for Google Search and LinkedIn profiles
- Concurrency and Rate Limits: 5 concurrent requests on trial
- Post-Signup Bonuses and Unlocks: Instant API key delivery; comprehensive Python and NodeJS code samples
- Market Maturity and Ecosystem Awareness: High; established scraper API serving over 5,000 corporate customers

#### 55. Bright Data (Web Unlocker & Scraping Browser)

- Primary Domain: `https://brightdata.com`
- Category: Heavyweight Web Scraping and Unblocking APIs
- Home Page: https://brightdata.com
- Pricing Page: https://brightdata.com/pricing
- LLMs.txt / API Documentation: https://brightdata.com/llms.txt
- Free Allowance: $5 free credit on signup trial; access to Scraping Browser and Web Unlocker
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: Yes
- Anti-Bot Protection Bypass: Extreme; world's largest proxy network (72M+ IPs), automated fingerprint synthesis, CAPTCHA solver
- JavaScript Rendering: Remote CDP (Chrome DevTools Protocol) Scraping Browser compatible with Puppeteer & Playwright
- Supported Output Formats: Clean HTML, interactive DOM, structured datasets, binary payloads
- Concurrency and Rate Limits: Massive enterprise concurrency (thousands of concurrent sessions)
- Post-Signup Bonuses and Unlocks: $5 initial credit; matching deposit promotions for business registrations
- Market Maturity and Ecosystem Awareness: Extreme; global industry leader in web data collection and proxy infrastructure

#### 56. Oxylabs (Web Scraper API)

- Primary Domain: `https://oxylabs.io`
- Category: Heavyweight Web Scraping and Unblocking APIs
- Home Page: https://oxylabs.io
- Pricing Page: https://oxylabs.io/pricing
- LLMs.txt / API Documentation: https://oxylabs.io/llms.txt
- Free Allowance: 5,000 free requests on 7-day trial for corporate emails; free developer sandbox
- Monthly Equivalent Requests (Single Account): 5,000
- Billing Cadence: One-Time 7-Day Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: Extreme; 100M+ proxy pool, AI-powered Web Unblocker with machine learning adaptive bypass
- JavaScript Rendering: Headless browser rendering with dynamic fingerprint rotation and JavaScript rendering
- Supported Output Formats: Clean HTML, parsed structured JSON for major e-commerce and search engines
- Concurrency and Rate Limits: High concurrency on trial pool
- Post-Signup Bonuses and Unlocks: Dedicated account manager on request; free trial extension for verified enterprises
- Market Maturity and Ecosystem Awareness: Extreme; Tier-1 global proxy provider alongside Bright Data, founded in 2015

#### 57. Smartproxy (Web Scraping API)

- Primary Domain: `https://smartproxy.com`
- Category: Heavyweight Web Scraping and Unblocking APIs
- Home Page: https://smartproxy.com
- Pricing Page: https://smartproxy.com/pricing
- LLMs.txt / API Documentation: https://decodo.com/llms.txt
- Free Allowance: Free trial on developer registration (approx. 500 requests / 3-day trial period)
- Monthly Equivalent Requests (Single Account): 500
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: Extreme; 65M+ residential proxies, 99.9% success rate, automated CAPTCHA solving
- JavaScript Rendering: Full headless browser scraping for dynamic single-page applications
- Supported Output Formats: HTML, structured JSON for SERP, eCommerce, and Social APIs
- Concurrency and Rate Limits: High concurrency support
- Post-Signup Bonuses and Unlocks: 3-day money back guarantee; developer starter credits
- Market Maturity and Ecosystem Awareness: Very High; major proxy and scraping platform operating since 2018

#### 58. Zyte (Scrapy Cloud & API)

- Primary Domain: `https://www.zyte.com`
- Category: Heavyweight Web Scraping and Unblocking APIs
- Home Page: https://www.zyte.com
- Pricing Page: https://www.zyte.com/pricing/
- LLMs.txt / API Documentation: https://www.zyte.com/llms.txt
- Free Allowance: $5 free credit on signup trial; free Scrapy Cloud hosting tier (1 scworker for 1 hour/day)
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: One-Time Signup Balance + Ongoing Free Cloud Scrapy Worker
- Credit Card Required: No
- Anti-Bot Protection Bypass: Extreme; Zyte API AI-driven unblocking (formerly Crawlera), automated ban detection and bypass
- JavaScript Rendering: Headless browser execution with network capture and browser action scripting
- Supported Output Formats: Clean HTML, structured schema JSON, browser actions replay
- Concurrency and Rate Limits: Tiered concurrency limits
- Post-Signup Bonuses and Unlocks: Creators of Scrapy framework; deep integration with open source Scrapy tools
- Market Maturity and Ecosystem Awareness: Extreme; creators of Scrapy (the world's most popular scraping library with 50k+ stars)

#### 59. Nimble (Nimbleway)

- Primary Domain: `https://nimbleway.com`
- Category: Heavyweight Web Scraping and Unblocking APIs
- Home Page: https://nimbleway.com
- Pricing Page: https://nimbleway.com/pricing
- LLMs.txt / API Documentation: https://nimbleway.com
- Free Allowance: Free trial credit ($20 value / approx. 1,000 requests) upon business email registration
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: Extreme; AI-optimized pipeline dynamically choosing optimal IP and browser fingerprints
- JavaScript Rendering: Lightweight rendering engine reducing resource consumption while executing essential JS
- Supported Output Formats: Structured JSON, clean markdown, raw HTML
- Concurrency and Rate Limits: Scalable cloud pipeline with enterprise concurrency
- Post-Signup Bonuses and Unlocks: Free consultation with web data architect upon onboarding
- Market Maturity and Ecosystem Awareness: High; modern venture-backed web scraping and pipeline infrastructure

#### 60. Scraping Robot

- Primary Domain: `https://scrapingrobot.com`
- Category: Heavyweight Web Scraping and Unblocking APIs
- Home Page: https://scrapingrobot.com
- Pricing Page: https://scrapingrobot.com/pricing
- LLMs.txt / API Documentation: https://scrapingrobot.com
- Free Allowance: 5,000 free scraping credits on signup; no credit card required
- Monthly Equivalent Requests (Single Account): 5,000
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: Very High; powered by Rayobyte proxy infrastructure, automated CAPTCHA handling
- JavaScript Rendering: Headless Chrome rendering with screenshot and metadata extraction
- Supported Output Formats: Clean HTML, structured JSON, full metadata parsing
- Concurrency and Rate Limits: 5 concurrent requests
- Post-Signup Bonuses and Unlocks: 5,000 free scrape credits immediately available upon email confirmation
- Market Maturity and Ecosystem Awareness: High; built by Rayobyte team to provide frictionless API access to their proxy network

#### 61. ScrapeOps

- Primary Domain: `https://scrapeops.io`
- Category: Heavyweight Web Scraping and Unblocking APIs
- Home Page: https://scrapeops.io
- Pricing Page: https://scrapeops.io/pricing/
- LLMs.txt / API Documentation: https://scrapeops.io/llms.txt
- Free Allowance: 1,000 free requests/month recurring on Proxy Aggregator; 100k free monitoring requests/mo
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: Monthly Recurring
- Credit Card Required: No
- Anti-Bot Protection Bypass: Very High; multi-provider proxy aggregator routing across 20+ proxy providers
- JavaScript Rendering: Headless Chrome rendering fallback with smart retry logic
- Supported Output Formats: Raw HTML, clean DOM, monitoring telemetry logs
- Concurrency and Rate Limits: 1 concurrent request on free plan
- Post-Signup Bonuses and Unlocks: Free fake user agent API and free proxy monitoring tools
- Market Maturity and Ecosystem Awareness: Very High; widely known in scraping community for free user agent lists and monitoring SDKs

#### 62. ScrapeNinja

- Primary Domain: `https://scrapeninja.net`
- Category: Heavyweight Web Scraping and Unblocking APIs
- Home Page: https://scrapeninja.net
- Pricing Page: https://scrapeninja.net/pricing
- LLMs.txt / API Documentation: https://scrapeninja.net/docs/llms.txt
- Free Allowance: 1,000 free requests/month recurring via RapidAPI; no credit card required
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: Monthly Recurring
- Credit Card Required: No
- Anti-Bot Protection Bypass: Very High; real Chrome browser engine with TLS fingerprint emulations (curl-impersonate)
- JavaScript Rendering: Full Chrome with custom JavaScript execution and Cheerio extraction in cloud
- Supported Output Formats: Clean HTML, JSON extracted via server-side Cheerio functions, headers telemetry
- Concurrency and Rate Limits: 1 request per second on free plan
- Post-Signup Bonuses and Unlocks: Interactive web console to generate Cheerio extraction scripts
- Market Maturity and Ecosystem Awareness: High; popular indie developer tool celebrated for TLS fingerprint mimicry

#### 63. Webshare

- Primary Domain: `https://www.webshare.io`
- Category: Heavyweight Web Scraping and Unblocking APIs
- Home Page: https://www.webshare.io
- Pricing Page: https://www.webshare.io/pricing
- LLMs.txt / API Documentation: https://www.webshare.io/llms.txt
- Free Allowance: 10 free proxies forever with 1 GB/month free bandwidth; no credit card required
- Monthly Equivalent Requests (Single Account): 10,000
- Billing Cadence: Monthly Recurring
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; rotating datacenter proxy pool with HTTP and SOCKS5 protocol support
- JavaScript Rendering: Transport layer proxy; pairs with local Playwright/Puppeteer/Crawl4AI instances
- Supported Output Formats: Raw network stream, HTTP/HTTPS/SOCKS5 proxy endpoints
- Concurrency and Rate Limits: Up to 50 concurrent proxy connections on free tier
- Post-Signup Bonuses and Unlocks: 10 permanent proxies with monthly bandwidth refresh; no expiration
- Market Maturity and Ecosystem Awareness: Very High; top-ranked budget proxy service used by hundreds of thousands of developers

#### 64. ScraperBox

- Primary Domain: `https://scraperbox.com`
- Category: Heavyweight Web Scraping and Unblocking APIs
- Home Page: https://scraperbox.com
- Pricing Page: https://scraperbox.com
- LLMs.txt / API Documentation: https://scraperbox.com
- Free Allowance: 1,000 free requests on signup trial; no credit card required
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: Very High; undetectable Chrome instances, residential proxy routing, CAPTCHA bypass
- JavaScript Rendering: Real Chrome browser rendering with stealth flags enabled
- Supported Output Formats: Clean HTML, full web page screenshots
- Concurrency and Rate Limits: 5 concurrent requests
- Post-Signup Bonuses and Unlocks: Instant API key delivery upon registration
- Market Maturity and Ecosystem Awareness: Mid; established boutique undetectable scraping API

#### 65. Abstract API Web Scraping

- Primary Domain: `https://www.abstractapi.com/api/web-scraping-api`
- Category: Heavyweight Web Scraping and Unblocking APIs
- Home Page: https://www.abstractapi.com/api/web-scraping-api
- Pricing Page: https://www.abstractapi.com/pricing
- LLMs.txt / API Documentation: https://www.abstractapi.com/llms.txt
- Free Allowance: 100 requests/month free recurring across Abstract API suite; no credit card required
- Monthly Equivalent Requests (Single Account): 100
- Billing Cadence: Monthly Recurring
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; automated rotating proxies and header spoofing
- JavaScript Rendering: Headless browser rendering with capture capabilities
- Supported Output Formats: Raw HTML, clean page body, extracted metadata
- Concurrency and Rate Limits: 1 request per second
- Post-Signup Bonuses and Unlocks: Universal access to IP geolocation, phone validation, and email validation APIs
- Market Maturity and Ecosystem Awareness: Very High; APILayer competitor serving over 1M developers worldwide

#### 66. ApyHub Web Scraper

- Primary Domain: `https://apyhub.com`
- Category: Heavyweight Web Scraping and Unblocking APIs
- Home Page: https://apyhub.com
- Pricing Page: https://apyhub.com/pricing
- LLMs.txt / API Documentation: https://apyhub.com/llms.txt
- Free Allowance: 1,000 credits/month free recurring; no credit card required
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: Monthly Recurring
- Credit Card Required: No
- Anti-Bot Protection Bypass: Medium-High; web page to text, markdown, and screenshot converters
- JavaScript Rendering: Server-side headless browser rendering and parsing
- Supported Output Formats: Clean text, markdown, structured JSON, web screenshots
- Concurrency and Rate Limits: 5 requests per second on free tier
- Post-Signup Bonuses and Unlocks: Access to 100+ standard developer microservice endpoints under one key
- Market Maturity and Ecosystem Awareness: High; modern API hub platform designed for modular software pipelines

#### 67. NetNut (Scraper API)

- Primary Domain: `https://netnut.io`
- Category: Heavyweight Web Scraping and Unblocking APIs
- Home Page: https://netnut.io
- Pricing Page: https://netnut.io/pricing/
- LLMs.txt / API Documentation: https://netnut.io
- Free Allowance: 7-day free trial on Web Scraper API upon business verification
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: One-Time 7-Day Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: Extreme; direct ISP proxy connectivity (DiviNetworks partner) ensuring zero disconnects
- JavaScript Rendering: Full dynamic page rendering for SERP, eCommerce, and social media
- Supported Output Formats: Structured JSON, clean HTML
- Concurrency and Rate Limits: High concurrency on dedicated ISP channels
- Post-Signup Bonuses and Unlocks: Dedicated account manager consultation for high-volume pipelines
- Market Maturity and Ecosystem Awareness: Very High; publicly traded company (Safe-T Group), premium enterprise provider

#### 68. SOAX (Web Scraper API)

- Primary Domain: `https://soax.com`
- Category: Heavyweight Web Scraping and Unblocking APIs
- Home Page: https://soax.com
- Pricing Page: https://soax.com/pricing
- LLMs.txt / API Documentation: https://soax.com
- Free Allowance: 3-day trial package ($1.99 or free trial on verified inquiry)
- Monthly Equivalent Requests (Single Account): 500
- Billing Cadence: One-Time Trial
- Credit Card Required: Yes
- Anti-Bot Protection Bypass: Extreme; 155M+ residential and mobile proxies, clean IP pool with zero fraud flags
- JavaScript Rendering: Scraper API with headless browser rendering and automated CAPTCHA bypass
- Supported Output Formats: Clean HTML, parsed structured JSON for Google and Amazon
- Concurrency and Rate Limits: Unlimited concurrent sessions on residential nodes
- Post-Signup Bonuses and Unlocks: Real-time node filtering by city, region, and ISP
- Market Maturity and Ecosystem Awareness: Very High; premier proxy and scraping platform based in the UK

#### 69. Rayobyte (Scraping API)

- Primary Domain: `https://rayobyte.com`
- Category: Heavyweight Web Scraping and Unblocking APIs
- Home Page: https://rayobyte.com
- Pricing Page: https://rayobyte.com/pricing/
- LLMs.txt / API Documentation: https://rayobyte.com
- Free Allowance: Free trial on residential proxies and scraper API upon registration (approx. 500 requests)
- Monthly Equivalent Requests (Single Account): 500
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: Extreme; US-based ethical proxy provider with massive residential IP network
- JavaScript Rendering: Headless browser cluster with custom user-agent rotation
- Supported Output Formats: Clean HTML, JSON data extracts
- Concurrency and Rate Limits: Scalable enterprise concurrency
- Post-Signup Bonuses and Unlocks: Discounted bundle pricing across proxy and scraping tiers
- Market Maturity and Ecosystem Awareness: Very High; leading US proxy infrastructure provider (formerly Blazing SEO)

#### 70. OpenPerplex

- Primary Domain: `https://openperplex.com`
- Category: Heavyweight Web Scraping and Unblocking APIs
- Home Page: https://openperplex.com
- Pricing Page: https://openperplex.com
- LLMs.txt / API Documentation: https://openperplex.com
- Free Allowance: 100 free requests on trial tier; open-source self-hostable alternative available
- Monthly Equivalent Requests (Single Account): 100
- Billing Cadence: One-Time Signup Trial + Unlimited Self-Hosted
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; automated web search aggregation and content scraping for LLM grounding
- JavaScript Rendering: Server-side content retrieval and semantic summarization
- Supported Output Formats: Structured JSON with search citations, full page markdown
- Concurrency and Rate Limits: 5 RPM on free tier
- Post-Signup Bonuses and Unlocks: Open source repository on GitHub for custom self-hosted deployments
- Market Maturity and Ecosystem Awareness: Mid; open source Perplexity alternative built for autonomous coding agents

---

### 1.4 Headless Browser Clouds and Autonomous Agent Sandboxes (71 to 85)

#### 71. Apify

- Primary Domain: `https://apify.com`
- Category: Headless Browser Clouds and Autonomous Agent Sandboxes
- Home Page: https://apify.com
- Pricing Page: https://apify.com/pricing
- LLMs.txt / API Documentation: https://apify.com/llms.txt
- Free Allowance: $5 platform usage credits every month recurring; no credit card required
- Monthly Equivalent Requests (Single Account): 15,000
- Billing Cadence: Monthly Recurring
- Credit Card Required: No
- Anti-Bot Protection Bypass: Extreme; Apify residential proxies, anti-scraping Actors (Website Content Crawler, Google Search Scraper)
- JavaScript Rendering: Full Playwright, Puppeteer, and Chrome browser automation running in serverless Docker containers
- Supported Output Formats: Clean Markdown for LLMs, JSON datasets, CSV, Excel, HTML, screenshots
- Concurrency and Rate Limits: Up to 32 GB RAM allocation across concurrent Actors
- Post-Signup Bonuses and Unlocks: Permanent $5 monthly grant; access to 1,500+ pre-built Actors on Apify Store
- Market Maturity and Ecosystem Awareness: Extreme; founded in 2015, over 300,000 developers, the leading serverless web scraping ecosystem

#### 72. Browserless

- Primary Domain: `https://www.browserless.io`
- Category: Headless Browser Clouds and Autonomous Agent Sandboxes
- Home Page: https://www.browserless.io
- Pricing Page: https://www.browserless.io/pricing/
- LLMs.txt / API Documentation: https://www.browserless.io/llms.txt
- Free Allowance: 1,000 units/month free recurring (approx. 6 hours of browser execution time); open source Docker image
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: Monthly Recurring + Unlimited Self-Hosted Docker
- Credit Card Required: No
- Anti-Bot Protection Bypass: Very High; stealth Chrome flags, built-in WebDriver evasion, residential proxy integration
- JavaScript Rendering: Full headless Chrome cluster with WebSocket/CDP, Puppeteer, Playwright, and REST endpoints (/content, /screenshot, /scrape)
- Supported Output Formats: HTML DOM, clean markdown, PDF, screenshot, structured JSON via function evaluation
- Concurrency and Rate Limits: 2 concurrent browser sessions on free cloud tier; unlimited on self-hosted Docker
- Post-Signup Bonuses and Unlocks: Completely free open source Docker image (browserless/chrome) with 7k+ GitHub stars
- Market Maturity and Ecosystem Awareness: Extreme; industry standard headless browser cloud, powers millions of automations daily

#### 73. Browserbase

- Primary Domain: `https://www.browserbase.com`
- Category: Headless Browser Clouds and Autonomous Agent Sandboxes
- Home Page: https://www.browserbase.com
- Pricing Page: https://www.browserbase.com/pricing
- LLMs.txt / API Documentation: https://www.browserbase.com/llms.txt
- Free Allowance: 1 hour of free browser execution time on signup ($5 trial credits); no credit card required
- Monthly Equivalent Requests (Single Account): 600
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: Extreme; Advanced Stealth Mode defeating Cloudflare, Datadome, and device integrity checks
- JavaScript Rendering: Dedicated cloud browser sessions with live session inspector, video replay, and Stagehand agent integration
- Supported Output Formats: Clean markdown, DOM accessibility tree, screenshots, session replay logs
- Concurrency and Rate Limits: 2 concurrent browser sessions on trial
- Post-Signup Bonuses and Unlocks: Authors of Stagehand (browser agent framework) with extensive developer credits
- Market Maturity and Ecosystem Awareness: Very High; premier AI-native headless browser cloud backed by top Silicon Valley VCs

#### 74. Steel.dev

- Primary Domain: `https://steel.dev`
- Category: Headless Browser Clouds and Autonomous Agent Sandboxes
- Home Page: https://steel.dev
- Pricing Page: https://steel.dev/pricing
- LLMs.txt / API Documentation: https://steel.dev/llms.txt
- Free Allowance: $30 free cloud credits on developer registration; 100% open source self-hosted engine
- Monthly Equivalent Requests (Single Account): 3,000
- Billing Cadence: One-Time Signup Trial + Unlimited Self-Hosted
- Credit Card Required: No
- Anti-Bot Protection Bypass: Very High; built-in fingerprint spoofing, proxy chaining, stealth automation
- JavaScript Rendering: Full browser automation API designed specifically for AI agents (Puppeteer/Playwright/Selenium compatible)
- Supported Output Formats: Clean markdown, structured JSON, session recordings, DOM snapshots
- Concurrency and Rate Limits: Multiple concurrent browser sessions
- Post-Signup Bonuses and Unlocks: Massive $30 free trial credit on cloud; fully open-source core on GitHub
- Market Maturity and Ecosystem Awareness: High; viral open source browser infrastructure for AI agents with rapid developer adoption

#### 75. Hyperbrowser

- Primary Domain: `https://www.hyperbrowser.ai`
- Category: Headless Browser Clouds and Autonomous Agent Sandboxes
- Home Page: https://www.hyperbrowser.ai
- Pricing Page: https://www.hyperbrowser.ai/pricing
- LLMs.txt / API Documentation: https://www.hyperbrowser.ai/llms.txt
- Free Allowance: $5 free credits on developer registration; no credit card required
- Monthly Equivalent Requests (Single Account): 500
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: Very High; specialized in stealth browser execution and anti-bot mitigation
- JavaScript Rendering: Agent-first headless browser cloud with session replay and live debugging
- Supported Output Formats: Clean markdown, structured data, DOM events, screenshot logs
- Concurrency and Rate Limits: Standard trial concurrency limits
- Post-Signup Bonuses and Unlocks: Free $5 credit grant immediately available upon sign-in
- Market Maturity and Ecosystem Awareness: High; modern cloud browser platform built for agentic web navigation

#### 76. Cloudflare Workers Browser Rendering

- Primary Domain: `https://developers.cloudflare.com/browser-rendering/`
- Category: Headless Browser Clouds and Autonomous Agent Sandboxes
- Home Page: https://developers.cloudflare.com/browser-rendering/
- Pricing Page: https://developers.cloudflare.com/workers/platform/pricing/
- LLMs.txt / API Documentation: https://developers.cloudflare.com
- Free Allowance: 100,000 requests/day on Workers free tier; 10 browser rendering minutes/day free during beta
- Monthly Equivalent Requests (Single Account): 3,000
- Billing Cadence: Daily Resets (Monthly Recurring)
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; runs directly inside Cloudflare's global edge network across 300+ cities
- JavaScript Rendering: Real Chromium instances running at the edge via Puppeteer-compatible API (@cloudflare/puppeteer)
- Supported Output Formats: HTML DOM, full page PDF, screenshot buffer, clean markdown via HTMLRewriter
- Concurrency and Rate Limits: 2 concurrent browser sessions on free plan
- Post-Signup Bonuses and Unlocks: Integrated seamlessly with Cloudflare Workers, KV, and Vectorize free tiers
- Market Maturity and Ecosystem Awareness: Extreme; run by Cloudflare, the world's leading edge infrastructure provider

#### 77. AgentQL

- Primary Domain: `https://agentql.com`
- Category: Headless Browser Clouds and Autonomous Agent Sandboxes
- Home Page: https://agentql.com
- Pricing Page: https://agentql.com/pricing
- LLMs.txt / API Documentation: https://docs.agentql.com
- Free Allowance: 1,000 free queries/month recurring on Free Tier; no credit card required
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: Monthly Recurring
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; semantic element locator using AI embeddings that survive DOM structure changes
- JavaScript Rendering: Playwright/Puppeteer browser driver plugin with semantic query language
- Supported Output Formats: Precise JSON matching user-defined GraphQL-like schema, element handles
- Concurrency and Rate Limits: Standard API rate limits on free plan
- Post-Signup Bonuses and Unlocks: Chrome DevTools extension for interactive query building
- Market Maturity and Ecosystem Awareness: High; pioneering AI query language for web scraping and browser automation

#### 78. Simplescraper

- Primary Domain: `https://simplescraper.io`
- Category: Headless Browser Clouds and Autonomous Agent Sandboxes
- Home Page: https://simplescraper.io
- Pricing Page: https://simplescraper.io/pricing
- LLMs.txt / API Documentation: https://simplescraper.io/llms.txt
- Free Allowance: 100 free scrape credits/month recurring; no credit card required
- Monthly Equivalent Requests (Single Account): 100
- Billing Cadence: Monthly Recurring
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; browser extension runs in user's own browser or automated in cloud
- JavaScript Rendering: Full browser automation with infinite scroll, click actions, and pagination
- Supported Output Formats: Clean JSON API, CSV export, webhook dispatches
- Concurrency and Rate Limits: 1 concurrent task on free plan
- Post-Signup Bonuses and Unlocks: Visual point-and-click scraper creation in browser extension
- Market Maturity and Ecosystem Awareness: High; popular Chrome extension with 50,000+ active users

#### 79. Browse AI

- Primary Domain: `https://www.browse.ai`
- Category: Headless Browser Clouds and Autonomous Agent Sandboxes
- Home Page: https://www.browse.ai
- Pricing Page: https://www.browse.ai/pricing
- LLMs.txt / API Documentation: https://www.browse.ai/llms.txt
- Free Allowance: 50 credits/month recurring on Free Plan; no credit card required
- Monthly Equivalent Requests (Single Account): 50
- Billing Cadence: Monthly Recurring
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; zero-code robot trainer that adapts to layout changes and solves simple challenges
- JavaScript Rendering: Cloud browser execution with automated pagination and dynamic scroll
- Supported Output Formats: Structured JSON API, Google Sheets sync, webhook alerts
- Concurrency and Rate Limits: 1 robot run at a time on free plan
- Post-Signup Bonuses and Unlocks: Permanent free monthly plan; visual training wizard
- Market Maturity and Ecosystem Awareness: Very High; widely used by business analysts and non-engineers, 100k+ users

#### 80. ParseHub

- Primary Domain: `https://www.parsehub.com`
- Category: Headless Browser Clouds and Autonomous Agent Sandboxes
- Home Page: https://www.parsehub.com
- Pricing Page: https://www.parsehub.com/pricing
- LLMs.txt / API Documentation: https://www.parsehub.com
- Free Allowance: Free plan with 200 pages per run, 5 public scraping projects, 14-day data retention
- Monthly Equivalent Requests (Single Account): 1,000
- Billing Cadence: Monthly Recurring
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; desktop client handles logins, AJAX, dropdowns, and cookies
- JavaScript Rendering: Full desktop browser rendering engine with conditional logic and loops
- Supported Output Formats: JSON, CSV, and REST API access to scraped runs
- Concurrency and Rate Limits: Sequential runs on free plan
- Post-Signup Bonuses and Unlocks: Free desktop application for macOS, Windows, and Linux
- Market Maturity and Ecosystem Awareness: Very High; veteran visual scraper established in 2014

#### 81. Octoparse

- Primary Domain: `https://www.octoparse.com`
- Category: Headless Browser Clouds and Autonomous Agent Sandboxes
- Home Page: https://www.octoparse.com
- Pricing Page: https://www.octoparse.com/pricing
- LLMs.txt / API Documentation: https://www.octoparse.com
- Free Allowance: Free plan with 10 tasks, unlimited page exports on local machine; free trial cloud credits
- Monthly Equivalent Requests (Single Account): 10,000
- Billing Cadence: Monthly Recurring (Local Execution)
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; user-agent rotation, IP proxy configuration, cookie management
- JavaScript Rendering: Full built-in browser engine supporting AJAX, infinite scroll, and iframes
- Supported Output Formats: JSON, CSV, Excel, database export
- Concurrency and Rate Limits: Local runs limited by machine power; sequential cloud tasks on trial
- Post-Signup Bonuses and Unlocks: Extensive pre-built template center for Amazon, eBay, Twitter, Yelp
- Market Maturity and Ecosystem Awareness: Very High; dominant desktop web scraping software with millions of downloads

#### 82. Microlink

- Primary Domain: `https://microlink.io`
- Category: Headless Browser Clouds and Autonomous Agent Sandboxes
- Home Page: https://microlink.io
- Pricing Page: https://microlink.io/#pricing
- LLMs.txt / API Documentation: https://microlink.io/llms.txt
- Free Allowance: 250 requests/day free without API key (approx. 7,500 requests/month); higher with free key
- Monthly Equivalent Requests (Single Account): 7,500
- Billing Cadence: Daily Resets (Monthly Recurring)
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; automated ad-blocking, tracker blocking, stealth headless browser execution
- JavaScript Rendering: Full Chromium execution with custom scripts, wait conditions, and viewport sizing
- Supported Output Formats: Structured JSON (Open Graph, meta tags, headers), clean markdown, PDF, screenshot buffer
- Concurrency and Rate Limits: Rate limited to 250 requests/day anonymous; burst friendly
- Post-Signup Bonuses and Unlocks: Instant anonymous consumption; zero signup required to test API
- Market Maturity and Ecosystem Awareness: Very High; premier web microservice API widely used in React/Next.js ecosystem

#### 83. Urlbox

- Primary Domain: `https://urlbox.com`
- Category: Headless Browser Clouds and Autonomous Agent Sandboxes
- Home Page: https://urlbox.com
- Pricing Page: https://urlbox.com/pricing
- LLMs.txt / API Documentation: https://urlbox.com/llms.txt
- Free Allowance: 100 free requests on 7-day trial; no credit card required
- Monthly Equivalent Requests (Single Account): 100
- Billing Cadence: One-Time 7-Day Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; ad-blocking, cookie banner hiding, custom headers and proxy support
- JavaScript Rendering: High-fidelity Chrome rendering with WebGL and modern CSS support
- Supported Output Formats: PNG, JPEG, WebP, PDF, HTML, markdown, and full DOM extraction
- Concurrency and Rate Limits: 5 concurrent renders on trial
- Post-Signup Bonuses and Unlocks: Comprehensive URL generator sandbox in dashboard
- Market Maturity and Ecosystem Awareness: Very High; established screenshot and rendering service operating since 2012

#### 84. ScreenshotOne

- Primary Domain: `https://screenshotone.com`
- Category: Headless Browser Clouds and Autonomous Agent Sandboxes
- Home Page: https://screenshotone.com
- Pricing Page: https://screenshotone.com/pricing/
- LLMs.txt / API Documentation: https://screenshotone.com/llms.txt
- Free Allowance: 100 screenshots/month free recurring; no credit card required
- Monthly Equivalent Requests (Single Account): 100
- Billing Cadence: Monthly Recurring
- Credit Card Required: No
- Anti-Bot Protection Bypass: Very High; automatically blocks cookie banners, popups, ads, and tracker scripts
- JavaScript Rendering: Full headless Chrome execution with custom styles, scripts, and dark mode toggling
- Supported Output Formats: Clean screenshot (PNG, WebP), clean HTML, extracted text, markdown
- Concurrency and Rate Limits: 1 request per second on free plan
- Post-Signup Bonuses and Unlocks: Permanent free monthly tier; deterministic caching included
- Market Maturity and Ecosystem Awareness: High; popular indie developer tool celebrated for speed and clean captures

#### 85. Extracta.ai

- Primary Domain: `https://extracta.ai`
- Category: Headless Browser Clouds and Autonomous Agent Sandboxes
- Home Page: https://extracta.ai
- Pricing Page: https://extracta.ai/pricing
- LLMs.txt / API Documentation: https://extracta.ai
- Free Allowance: 50 free extraction credits on developer signup; no credit card required
- Monthly Equivalent Requests (Single Account): 50
- Billing Cadence: One-Time Signup Trial
- Credit Card Required: No
- Anti-Bot Protection Bypass: High; document and web page extraction powered by multimodal LLMs
- JavaScript Rendering: Cloud document parser and web page visual snapshot reader
- Supported Output Formats: Strict JSON conforming to user-defined fields
- Concurrency and Rate Limits: Standard rate limits for trial
- Post-Signup Bonuses and Unlocks: Supports both live web URLs and PDF/Word documents
- Market Maturity and Ecosystem Awareness: Mid; emerging AI document and web extraction tool

---

### 1.5 Academic, News, Archive and Structured Public Knowledge APIs (86 to 100)

#### 86. NewsAPI

- Primary Domain: `https://newsapi.org`
- Category: Academic, News, Archive and Structured Public Knowledge APIs
- Home Page: https://newsapi.org
- Pricing Page: https://newsapi.org/pricing
- LLMs.txt / API Documentation: https://newsapi.org
- Free Allowance: 100 requests/day free for developer/non-commercial use (approx. 3,000 requests/month)
- Monthly Equivalent Requests (Single Account): 3,000
- Billing Cadence: Daily Resets (Monthly Recurring)
- Credit Card Required: No
- Anti-Bot Protection Bypass: Native; official REST API indexing over 80,000 global news sources and blogs
- JavaScript Rendering: Pre-indexed articles with full title, description, content snippet, author, and timestamp
- Supported Output Formats: Clean JSON matching standard article schemas
- Concurrency and Rate Limits: 100 requests/day, 1-month historical article search window
- Post-Signup Bonuses and Unlocks: Instant API key delivery; comprehensive client libraries for Python, JS, Ruby, PHP
- Market Maturity and Ecosystem Awareness: Extreme; default standard news API for developers worldwide, established in 2017

#### 87. NewsCatcher API

- Primary Domain: `https://www.newscatcherapi.com`
- Category: Academic, News, Archive and Structured Public Knowledge APIs
- Home Page: https://www.newscatcherapi.com
- Pricing Page: https://www.newscatcherapi.com/pricing
- LLMs.txt / API Documentation: https://www.newscatcherapi.com/llms.txt
- Free Allowance: Free trial on developer registration (approx. 50 calls/day / 1,500 calls/month); free sandbox
- Monthly Equivalent Requests (Single Account): 1,500
- Billing Cadence: One-Time Trial + Developer Sandbox
- Credit Card Required: No
- Anti-Bot Protection Bypass: Native; massive global crawling cluster monitoring over 1,000,000 articles daily
- JavaScript Rendering: Extracts clean article text, NLP topics, sentiment, and author entities
- Supported Output Formats: Enriched JSON with full text, language classification, and cluster deduplication
- Concurrency and Rate Limits: 1 QPS on trial tier
- Post-Signup Bonuses and Unlocks: Access to advanced clustering and topic classification models
- Market Maturity and Ecosystem Awareness: Very High; trusted by enterprise financial analysts and AI intelligence applications

#### 88. GNews API

- Primary Domain: `https://gnews.io`
- Category: Academic, News, Archive and Structured Public Knowledge APIs
- Home Page: https://gnews.io
- Pricing Page: https://gnews.io/pricing
- LLMs.txt / API Documentation: https://gnews.io
- Free Allowance: 100 requests/day free recurring (approx. 3,000 requests/month); no credit card required
- Monthly Equivalent Requests (Single Account): 3,000
- Billing Cadence: Daily Resets (Monthly Recurring)
- Credit Card Required: No
- Anti-Bot Protection Bypass: Native; real-time news search and headline retrieval across 60,000+ sources
- JavaScript Rendering: Pre-parsed live news feed and topic aggregator
- Supported Output Formats: Clean JSON with article title, description, URL, image, and publication date
- Concurrency and Rate Limits: 1 request per second, 100 requests/day
- Post-Signup Bonuses and Unlocks: Permanent free tier for non-commercial and development projects
- Market Maturity and Ecosystem Awareness: High; popular developer alternative to NewsAPI with multi-language support

#### 89. MediaStack

- Primary Domain: `https://mediastack.com`
- Category: Academic, News, Archive and Structured Public Knowledge APIs
- Home Page: https://mediastack.com
- Pricing Page: https://mediastack.com/pricing
- LLMs.txt / API Documentation: https://mediastack.com
- Free Allowance: 500 requests/month free recurring; no credit card required
- Monthly Equivalent Requests (Single Account): 500
- Billing Cadence: Monthly Recurring
- Credit Card Required: No
- Anti-Bot Protection Bypass: Native; APILayer live news REST API tracking 7,500+ news sources across 50 countries
- JavaScript Rendering: Real-time news feed extraction and categorization
- Supported Output Formats: Structured JSON with country, category, language, and author filters
- Concurrency and Rate Limits: Standard rate limits for free plan
- Post-Signup Bonuses and Unlocks: Permanent free monthly plan; APILayer single-key ecosystem
- Market Maturity and Ecosystem Awareness: Very High; part of APILayer / Idera enterprise developer tooling

#### 90. Currents API

- Primary Domain: `https://currentsapi.services`
- Category: Academic, News, Archive and Structured Public Knowledge APIs
- Home Page: https://currentsapi.services
- Pricing Page: https://currentsapi.services/en/pricing
- LLMs.txt / API Documentation: https://currentsapi.services
- Free Allowance: 600 requests/day free recurring (approx. 18,000 requests/month); no credit card required
- Monthly Equivalent Requests (Single Account): 18,000
- Billing Cadence: Daily Resets (Monthly Recurring)
- Credit Card Required: No
- Anti-Bot Protection Bypass: Native; continuous news crawler indexing international news in 14 languages
- JavaScript Rendering: Pre-processed news articles with category tags and domain rankings
- Supported Output Formats: Clean JSON array of articles with metadata
- Concurrency and Rate Limits: 1 request per second, 600 requests/day
- Post-Signup Bonuses and Unlocks: Exceptionally generous daily free tier for indie developers and students
- Market Maturity and Ecosystem Awareness: High; recognized in open-data communities for generous free developer quotas

#### 91. Semantic Scholar Academic Graph API

- Primary Domain: `https://www.semanticscholar.org/product/api`
- Category: Academic, News, Archive and Structured Public Knowledge APIs
- Home Page: https://www.semanticscholar.org/product/api
- Pricing Page: https://www.semanticscholar.org/product/api#pricing
- LLMs.txt / API Documentation: https://api.semanticscholar.org
- Free Allowance: Free 100 requests per 5 minutes without key (~28,800 req/day); free API key grants 10 RPS (~864,000 req/day)
- Monthly Equivalent Requests (Single Account): 864,000
- Billing Cadence: Continuous Polite Rate Limit (Free Forever)
- Credit Card Required: No
- Anti-Bot Protection Bypass: Native; official Allen Institute for AI (AI2) scientific paper search and graph API
- JavaScript Rendering: Graph retrieval across 200M+ academic papers with citation links, abstracts, and embeddings
- Supported Output Formats: Rich JSON with paperId, title, abstract, authors, citations, reference counts, open access PDF links
- Concurrency and Rate Limits: 1 req/sec unauthenticated; 10 req/sec with free registered key
- Post-Signup Bonuses and Unlocks: Completely free scientific research infrastructure funded by Paul G. Allen Estate
- Market Maturity and Ecosystem Awareness: Extreme; the premier open academic literature API globally, powers Semantic Scholar and Consensus

#### 92. Crossref REST API

- Primary Domain: `https://www.crossref.org/documentation/retrieve-metadata/rest-api/`
- Category: Academic, News, Archive and Structured Public Knowledge APIs
- Home Page: https://www.crossref.org/documentation/retrieve-metadata/rest-api/
- Pricing Page: https://www.crossref.org
- LLMs.txt / API Documentation: https://api.crossref.org
- Free Allowance: Unlimited free requests at up to 50 requests/second in the Polite Pool (add mailto: header/param)
- Monthly Equivalent Requests (Single Account): 1,000,000
- Billing Cadence: Continuous Polite Pool (Free Forever)
- Credit Card Required: No
- Anti-Bot Protection Bypass: Native; official DOI registry and metadata authority for scholarly publishing
- JavaScript Rendering: Direct query engine over 150M+ scholarly works, journals, books, and conference proceedings
- Supported Output Formats: Comprehensive JSON-LD and REST JSON with complete citation graphs and publisher links
- Concurrency and Rate Limits: 50 requests per second with mailto parameter identifying polite client
- Post-Signup Bonuses and Unlocks: No registration required; adding an email address to headers unlocks polite pool speeds
- Market Maturity and Ecosystem Awareness: Extreme; global non-profit infrastructure underpinning all scientific DOI resolution

#### 93. OpenAlex API

- Primary Domain: `https://openalex.org`
- Category: Academic, News, Archive and Structured Public Knowledge APIs
- Home Page: https://openalex.org
- Pricing Page: https://openalex.org/pricing
- LLMs.txt / API Documentation: https://docs.openalex.org
- Free Allowance: 100,000 requests/day free (approx. 3,000,000 requests/month) in the Polite Pool; 10 req/sec rate limit
- Monthly Equivalent Requests (Single Account): 3,000,000
- Billing Cadence: Daily Resets (Free Forever)
- Credit Card Required: No
- Anti-Bot Protection Bypass: Native; open catalog of 250M+ scientific papers, researchers, institutions, and concepts
- JavaScript Rendering: Full knowledge graph indexing with full-text search, n-grams, and citation trees
- Supported Output Formats: Detailed REST JSON with abstract inverted indexes, MeSH terms, open access locations
- Concurrency and Rate Limits: 10 requests per second in polite pool (append mailto parameter)
- Post-Signup Bonuses and Unlocks: Complete database snapshots available as free open-data downloads on AWS S3
- Market Maturity and Ecosystem Awareness: Extreme; successor to Microsoft Academic Graph (MAG), the world's most complete open science index

#### 94. arXiv API

- Primary Domain: `https://arxiv.org/help/api`
- Category: Academic, News, Archive and Structured Public Knowledge APIs
- Home Page: https://arxiv.org/help/api
- Pricing Page: https://arxiv.org
- LLMs.txt / API Documentation: https://arxiv.org
- Free Allowance: Unlimited free queries at up to 3 requests/second (approx. 7,700,000 requests/month); no account needed
- Monthly Equivalent Requests (Single Account): 7,700,000
- Billing Cadence: Continuous Polite Rate Limit (Free Forever)
- Credit Card Required: No
- Anti-Bot Protection Bypass: Native; official Cornell University preprint server API
- JavaScript Rendering: Search and retrieval across 2.4M+ STEM preprints and research papers
- Supported Output Formats: Atom XML feed, REST endpoints, direct PDF and LaTeX source downloads
- Concurrency and Rate Limits: 1 request every 3 seconds per client (respects polite harvesting guidelines)
- Post-Signup Bonuses and Unlocks: Zero authentication required; access to full scientific paper source archives on Kaggle/S3
- Market Maturity and Ecosystem Awareness: Extreme; the definitive global repository for computer science, physics, math, and AI research

#### 95. CORE API

- Primary Domain: `https://core.ac.uk/services/api`
- Category: Academic, News, Archive and Structured Public Knowledge APIs
- Home Page: https://core.ac.uk/services/api
- Pricing Page: https://core.ac.uk/pricing
- LLMs.txt / API Documentation: https://core.ac.uk
- Free Allowance: 10,000 requests/month free on Research / Free Tier; no credit card required
- Monthly Equivalent Requests (Single Account): 10,000
- Billing Cadence: Monthly Recurring
- Credit Card Required: No
- Anti-Bot Protection Bypass: Native; world's largest aggregator of open access research papers (over 200M papers)
- JavaScript Rendering: Full-text indexing, PDF text extraction, duplicate detection
- Supported Output Formats: Structured JSON with full article text, abstract, authors, and repository links
- Concurrency and Rate Limits: 10 requests per minute on free tier
- Post-Signup Bonuses and Unlocks: Instant API key generation for academic and developer research
- Market Maturity and Ecosystem Awareness: Very High; UK Open University and Jisc joint service, standard open access aggregator

#### 96. Internet Archive Wayback Machine API

- Primary Domain: `https://archive.org/help/wayback_api.php`
- Category: Academic, News, Archive and Structured Public Knowledge APIs
- Home Page: https://archive.org/help/wayback_api.php
- Pricing Page: https://archive.org
- LLMs.txt / API Documentation: https://archive.org
- Free Allowance: Unlimited free queries to Wayback Availability API and CDX Server API; no account required
- Monthly Equivalent Requests (Single Account): 500,000
- Billing Cadence: Continuous Polite Pool (Free Forever)
- Credit Card Required: No
- Anti-Bot Protection Bypass: Native; access to over 850 billion archived web pages from 1996 to present
- JavaScript Rendering: Historical snapshot retrieval preserving original HTML, CSS, images, and JavaScript
- Supported Output Formats: JSON availability responses, CDX index records, raw historical web page HTML
- Concurrency and Rate Limits: Approx. 5-10 requests per second polite rate limit
- Post-Signup Bonuses and Unlocks: Ability to trigger Save Page Now (SPN2) captures of live web pages programmatically
- Market Maturity and Ecosystem Awareness: Extreme; non-profit digital library and memory of the entire public World Wide Web

#### 97. Wikipedia / MediaWiki REST & Action API

- Primary Domain: `https://www.mediawiki.org/wiki/API:Main_page`
- Category: Academic, News, Archive and Structured Public Knowledge APIs
- Home Page: https://www.mediawiki.org/wiki/API:Main_page
- Pricing Page: https://www.mediawiki.org
- LLMs.txt / API Documentation: https://en.wikipedia.org/w/api.php
- Free Allowance: Unlimited free requests at up to 200 requests/second with polite User-Agent header; no account needed
- Monthly Equivalent Requests (Single Account): 5,000,000
- Billing Cadence: Continuous Polite Pool (Free Forever)
- Credit Card Required: No
- Anti-Bot Protection Bypass: Native; official Wikimedia Foundation public knowledge infrastructure
- JavaScript Rendering: Instant lookup across 60M+ encyclopedia articles in 300+ languages
- Supported Output Formats: Structured REST JSON, clean HTML, wikitext, page summary extracts
- Concurrency and Rate Limits: Up to 200 req/sec for clients providing contact info in User-Agent header
- Post-Signup Bonuses and Unlocks: Access to Wikidata SPARQL query service and Wikimedia Commons media files
- Market Maturity and Ecosystem Awareness: Extreme; world's largest open encyclopedia, fundamental data source for all frontier LLMs

#### 98. Hacker News Algolia Search API

- Primary Domain: `https://hn.algolia.com/api`
- Category: Academic, News, Archive and Structured Public Knowledge APIs
- Home Page: https://hn.algolia.com/api
- Pricing Page: https://hn.algolia.com
- LLMs.txt / API Documentation: https://hn.algolia.com/api
- Free Allowance: 10,000 requests/hour free without API key (approx. 7,200,000 requests/month); no account needed
- Monthly Equivalent Requests (Single Account): 7,200,000
- Billing Cadence: Hourly Resets (Free Forever)
- Credit Card Required: No
- Anti-Bot Protection Bypass: Native; official Algolia search cluster indexing all Hacker News stories, comments, and links
- JavaScript Rendering: Ultra-fast millisecond-latency search across millions of tech discussions and URL submissions
- Supported Output Formats: Rich JSON array of stories, comment threads, author karma, points, and external URLs
- Concurrency and Rate Limits: 10,000 requests per hour per IP
- Post-Signup Bonuses and Unlocks: Zero authentication required; instant real-time indexing of new comments within seconds
- Market Maturity and Ecosystem Awareness: Extreme; primary intelligence feed for tech industry trends, startup news, and AI discourse

#### 99. Stack Exchange / Stack Overflow API

- Primary Domain: `https://api.stackexchange.com`
- Category: Academic, News, Archive and Structured Public Knowledge APIs
- Home Page: https://api.stackexchange.com
- Pricing Page: https://api.stackexchange.com
- LLMs.txt / API Documentation: https://api.stackexchange.com
- Free Allowance: 300 requests/day unauthenticated; 10,000 requests/day free with free registered API key
- Monthly Equivalent Requests (Single Account): 300,000
- Billing Cadence: Daily Resets (Monthly Recurring)
- Credit Card Required: No
- Anti-Bot Protection Bypass: Native; official REST API indexing 170+ Q&A communities including Stack Overflow
- JavaScript Rendering: Structured Q&A database retrieval with code block preservation and vote counts
- Supported Output Formats: Gzip-compressed JSON containing questions, accepted answers, code snippets, and tags
- Concurrency and Rate Limits: 30 requests per second burst limit; 10,000 requests/day with API key
- Post-Signup Bonuses and Unlocks: Free registration grants instant 33x quota expansion (from 300 to 10,000 requests/day)
- Market Maturity and Ecosystem Awareness: Extreme; definitive developer Q&A repository, foundational training corpus for coding LLMs

#### 100. GitHub Code & Repository Search API

- Primary Domain: `https://docs.github.com/en/rest/search`
- Category: Academic, News, Archive and Structured Public Knowledge APIs
- Home Page: https://docs.github.com/en/rest/search
- Pricing Page: https://github.com
- LLMs.txt / API Documentation: https://docs.github.com
- Free Allowance: 10 req/min unauthenticated; 30 req/min authenticated free with standard GitHub token (~43,200 req/day)
- Monthly Equivalent Requests (Single Account): 1,296,000
- Billing Cadence: Continuous Minute Resets (Free Forever)
- Credit Card Required: No
- Anti-Bot Protection Bypass: Native; official REST/GraphQL API indexing 300M+ code repositories and documentation files
- JavaScript Rendering: Direct code indexing, AST parsing, issue search, commit histories, and release downloads
- Supported Output Formats: Clean JSON with file paths, highlighted text matches, commit SHAs, and raw blob URLs
- Concurrency and Rate Limits: 30 search queries per minute for authenticated personal access tokens
- Post-Signup Bonuses and Unlocks: Every standard GitHub account has free personal access token capabilities with zero payment
- Market Maturity and Ecosystem Awareness: Extreme; world's dominant software collaboration platform and open source code archive

---

## 2. Initial 3 Deep Technical Architecture Reviews

This section examines three foundational providers that represent distinct architectural approaches: high-volume daily allowance (Tinyfish), massive monthly recurring allowance with crypto micropayments (Keenable), and credit-based headless escalation with an open-source core (Firecrawl).

### 2.1 Deep Review: Tinyfish

#### Architecture Overview
Tinyfish (tinyfish.ai) is an agent-native web automation and search engine built specifically for autonomous execution loops. It operates two distinct service layers: a high-throughput, zero-cost Search and Fetch layer, and a metered Agent Automation and Browser Sandbox layer.

#### Endpoint Specifications and Free Quotas
- Web Search: `POST https://agent.tinyfish.ai/v1/search`. Free quota: 12,000 requests per day. Resets daily at 00:00 UTC. Monthly volume: 360,000 queries per account.
- Web Fetch: `POST https://agent.tinyfish.ai/v1/fetch`. Free quota: 1,000 URLs per day. Resets daily at 00:00 UTC. Monthly volume: 30,000 page reads per account.
- Browser Automation: `POST https://agent.tinyfish.ai/v1/automation/run`. Metered at $0.016 per automation step.
- Interactive Browser Sessions: `POST https://agent.tinyfish.ai/v1/browser/session`. Metered at $0.002 per browser-minute.
- Signup Grant: Every new account receives an initial $8.00 wallet credit for automation and browser minutes without requiring a credit card.

#### Machine Payments Protocol (MPP)
Tinyfish implements the Machine Payments Protocol (MPP). When an autonomous agent exhausts its daily free allowance or executes paid browser runs with zero balance, the API responds with HTTP 402 Payment Required carrying a payment challenge header:
```http
HTTP/1.1 402 Payment Required
WWW-Authenticate: MPP challenge="..."
```
An agent equipped with payment credentials can settle the challenge via Stripe or delegated wallet funds, immediately crediting the account without manual human intervention.

#### Anti-Bot and Unblocking Architecture
Tinyfish employs a distributed headless browser fleet with integrated stealth patches. It supports full Chrome DevTools Protocol (CDP) connectivity, automated cookie and session persistence, and stealth mode specifically tuned to defeat login forms, Cloudflare challenges, and BotProtect scripts.

#### Gateway Role
In the unified gateway, Tinyfish serves as the primary Tier 1 engine for all routine web searches and lightweight page reads due to its combined 390,000 monthly request capacity per account.

---

### 2.2 Deep Review: Keenable

#### Architecture Overview
Keenable (keenable.ai) provides specialized high-volume search and fetch APIs optimized for LLM contexts. The platform distinguishes itself by offering an exceptionally large free allowance on authenticated requests.

#### Endpoint Specifications and Free Quotas
- Web Search: `POST https://api.keenable.ai/v1/search`. Returns ranked search results with concise semantic excerpts.
- Web Fetch: `POST https://api.keenable.ai/v1/fetch`. Returns clean Markdown or structured text from target URLs.
- Monthly Free Allowance: 100,000 requests per month at zero cost. The allowance resets on the organization grant-anchor day. No credit card is required during onboarding.
- Over-Quota Pricing: Requests beyond the 100,000 allowance cost $0.001 per request.

#### x402 Micropayment Protocol
Keenable natively implements the x402 payment standard on the Base blockchain. Autonomous agents can query the search and fetch endpoints without creating an account or storing API keys by paying $0.01 per request in USDC over the x402 protocol, or by drawing down prepaid credits acquired via ZeroClick.

#### Anti-Bot and Scraping Mechanics
Keenable utilizes rotating egress nodes with automated header normalization. The fetch endpoint extracts readable content, strips advertising scripts, and renders single-page applications before returning distilled Markdown to the client.

#### Gateway Role
Keenable functions as the high-volume bulk workhorse in the unified gateway. With 100,000 free requests per month per account, a 5-account cluster yields 500,000 monthly operations, providing massive sustained throughput for background research and continuous indexing.

---

### 2.3 Deep Review: Firecrawl

#### Architecture Overview
Firecrawl (firecrawl.dev) is an open-source web scraper and crawler platform created specifically for LLM applications. It converts complex websites into clean, clean Markdown or structured JSON schemas. Firecrawl exists as both a managed cloud service and a fully sovereign open-source self-hosted stack.

#### Endpoint Specifications and Credit Metering
- Scrape Endpoint (`POST /v1/scrape`): 1 credit per page. Captures clean Markdown, HTML, or raw text.
- Crawl Endpoint (`POST /v1/crawl`): 1 credit per page discovered and scraped. Follows links recursively up to configured depth and limit.
- Map Endpoint (`POST /v1/map`): 1 credit per call. Discovers all URLs on a domain without scraping page bodies.
- Search Endpoint (`POST /v1/search`): 2 credits per 10 results. Executes web search and returns scraped results.
- Interact Endpoint (`POST /v1/interact`): 2 to 7 credits per browser minute for interactive Playwright execution.
- Free Cloud Plan: 1,000 credits per month recurring, 2 concurrent browser sessions, 50,000 queued jobs. No credit card required.

#### Enhanced Proxy Auto-Escalation
A major architectural strength of Firecrawl is its proxy escalation mechanism (`proxy: "enhanced"` or `auto`). Basic requests route through datacenter proxies. If a target domain blocks the connection (HTTP 403, 429, or CAPTCHA challenge), Firecrawl automatically escalates the retry to high-reputation residential proxies. This escalated retry is billed at the standard 1-credit rate, incurring zero surcharge.

#### Cloud vs. Self-Hosted Deployment
Firecrawl is licensed under AGPLv3. The entire cloud infrastructure (Node.js API, BullMQ/Redis job queue, Playwright worker cluster) can be self-hosted via Docker Compose. The self-hosted instance provides unlimited pages, crawls, and maps, bounded only by host server resources.

#### Gateway Role
In the unified gateway, Firecrawl Cloud handles structured schema extraction and multi-page site crawls up to the 1,000 credit ceiling per account. When paired with a local self-hosted Firecrawl instance, it acts as an unconstrained crawling engine for full documentation trees.

---

## 3. Extra Post-Analysis

This section addresses the five core operational and economic analyses required for multi-account unified gateway deployment.

### 3.1 Total Request Volumes for 5 Accounts per Provider

Deploying 5 independent accounts per provider multiplies total system capacity by a factor of five. Across the 100 cataloged providers, the aggregate monthly capacity expands from 29,787,275 to 148,936,375 requests.

#### Volume Stratification by Functional Domain

1. Web Search Domain (5-Account Monthly Capacity: 11,265,000 requests):
   - Tinyfish: 1,800,000 search queries per month (12,000/day * 30 days * 5 accounts).
   - Google Custom Search JSON API: 15,000 queries per month (100/day * 30 days * 5 accounts).
   - Brave Search API: 10,000 queries per month (2,000/mo * 5 accounts).
   - Tavily: 5,000 queries per month (1,000/mo * 5 accounts).
   - Bing Web Search (Azure F0): 5,000 queries per month (1,000/mo * 5 accounts).
   - You.com: 5,000 queries per month (1,000/mo * 5 accounts).
   - Serper (Trial): 12,500 queries (2,500 * 5 accounts).
   - Octen (Trial Balance): 12,500 queries ($5 * 5 accounts).
   - Mojeek (Trial): 5,000 queries (1,000 * 5 accounts).
   - DuckDuckGo / SearXNG: Unmetered polite capacity (estimated 500,000 requests across rotating proxy pool).

2. Web Fetch and Single-Page Scraping Domain (5-Account Monthly Capacity: 5,875,000 requests):
   - Keenable: 500,000 fetch operations per month (100,000/mo * 5 accounts).
   - Tinyfish: 150,000 fetch operations per month (1,000/day * 30 days * 5 accounts).
   - Jina AI Reader: 5,000,000 tokens per month across 5 keys, plus unauthenticated 20 RPM stream.
   - Microlink: 37,500 requests per month (250/day * 30 days * 5 accounts).
   - Webscraping.ai: 10,000 requests per month (2,000/mo * 5 accounts).
   - Scrape.do: 5,000 requests per month (1,000/mo * 5 accounts).
   - ScrapingAnt: 5,000 requests per month (1,000/mo * 5 accounts).
   - ScrapeOps: 5,000 requests per month (1,000/mo * 5 accounts).
   - ScrapeNinja: 5,000 requests per month (1,000/mo * 5 accounts).
   - AbstractAPI: 500 requests per month (100/mo * 5 accounts).
   - ApyHub: 5,000 requests per month (1,000/mo * 5 accounts).
   - ScraperAPI (Trial): 25,000 requests (5,000 * 5 accounts).
   - ScrapingBee (Trial): 5,000 requests (1,000 * 5 accounts).
   - ZenRows (Trial): 5,000 requests (1,000 * 5 accounts).
   - Crawlbase (Trial): 5,000 requests (1,000 * 5 accounts).
   - Scrapfly (Trial): 5,000 requests (1,000 * 5 accounts).
   - ScrapingRobot (Trial): 25,000 requests (5,000 * 5 accounts).

3. Deep Site Crawling and Browser Cloud Domain (5-Account Monthly Capacity: 150,000 requests cloud + unlimited local):
   - Firecrawl: 5,000 credits per month (1,000/mo * 5 accounts).
   - Apify: $25 monthly platform usage credit across 5 accounts (approx. 75,000 page scrapes via lightweight actors).
   - Browserless: 5,000 units per month (1,000/mo * 5 accounts) or 30 hours of browser execution.
   - Browserbase (Trial): 5 hours of cloud browser sessions ($25 value).
   - Steel.dev (Trial): $150 in cloud browser credits ($30 * 5 accounts).
   - Hyperbrowser (Trial): $25 in cloud browser credits ($5 * 5 accounts).
   - Crawl4AI / SearXNG: Unlimited capacity via local container deployment.

4. Structured Public Knowledge and Scholarly Domain (5-Account Monthly Capacity: 131,646,375 requests):
   - Semantic Scholar API: 4,320,000 requests per month with 5 registered keys (10 RPS * 5).
   - OpenAlex API: 15,000,000 requests per month (100k/day * 30 days * 5 polite accounts).
   - Crossref API: 25,000,000 requests per month (polite pool at 50 RPS).
   - arXiv API: 38,880,000 requests per month (polite 3 RPS per IP).
   - Wikipedia / MediaWiki REST API: 25,000,000 requests per month (polite 200 RPS header).
   - Hacker News Algolia Search: 36,000,000 requests per month (10k/hr * 24 * 30 * 5).
   - Stack Exchange API: 1,500,000 requests per month (10k/day * 30 days * 5 accounts).
   - GitHub Search API: 6,480,000 requests per month (30 req/min * 60 * 24 * 30 * 5 tokens).
   - NewsAPI / GNews / Currents: 120,000 requests per month.

---

### 3.2 Anti-Bot Protection Bypass and Evasion Benchmarks

Modern bot-mitigation systems operate across three evaluation layers: Network Layer (TCP/IP stack, IP reputation, ASN classification), Transport Layer (TLS fingerprinting, JA3/JA4, HTTP/2 frame parameters), and Client Application Layer (JavaScript challenges, canvas fingerprinting, DOM behavioral telemetry, CAPTCHAs).

#### Anti-Bot Capability Tier Rankings

1. Tier 1: Industrial Anti-Bot Bypasses (98% to 99.5% Success Rate on Hard Targets):
   - ZenRows: Employs dynamic residential proxy routing and automated client fingerprint synthesis. Successfully defeats Cloudflare Under Attack Mode, Turnstile, Datadome, Kasada, and Akamai Bot Manager.
   - Scrapfly: Implements an Anti-Scraping Protection (ASP) engine combining TLS fingerprint mimicry, headless browser evasion, and rotating residential proxies. Specifically tested against Cloudflare 5s challenge pages and Datadome behavioral traps.
   - Scrape.do: Backed by 95M+ residential IPs. Bypasses PerimeterX/HUMAN, Datadome, and Cloudflare Turnstile with automated retry mechanics.
   - Bright Data (Web Unlocker) and Oxylabs (Web Scraper API): Enterprise machine-learning unblocking engines that analyze domain block signatures in real time and adapt headers, cookies, and proxy subnets.
   - Apify: Specialized anti-scraping Actors (e.g. Website Content Crawler) running full Playwright instances with stealth plugins and residential proxy switching.

2. Tier 2: Resilient Cloud Scrapers (90% to 95% Success Rate):
   - Firecrawl: Enhanced mode (`proxy: "enhanced"`) auto-escalates from datacenter to residential proxies when challenges are encountered, defeating standard Cloudflare WAF and Turnstile.
   - ScrapingBee: Headless Chrome cluster with automated CAPTCHA solving and proxy rotation.
   - Tinyfish: Stealth browser automation mode bypassing Cloudflare challenge gates on web automation runs.
   - Crawlbase: Automatic unblocker algorithms handling standard JavaScript challenges and IP bans.

3. Tier 3: Standard Web Readers and Proxies (75% to 85% Success Rate):
   - Jina Reader: Bypasses standard Cloudflare rules on informational sites via proprietary proxy pool; occasional timeouts on strict Datadome sites.
   - Webscraping.ai: Rotating proxy pool capable of defeating basic and moderate anti-bot scripts.
   - Browserless: Real Chrome headless instances; requires user configuration of stealth flags and residential proxies to defeat advanced challenges.

4. Tier 4: Direct HTTP and Unprotected Crawlers (15% to 40% Success Rate):
   - Raw HTTP client requests, datacenter-only proxies without TLS emulation. Blocked by Cloudflare 403 Forbidden on modern protected properties.

---

### 3.3 One-Time Credits vs Monthly Recurring Credits Breakdown

#### Statistical Breakdown
- Recurring Allowances (Monthly / Daily / Polite Pools): 55 providers.
- One-Time Signup Trial Credits: 48 providers.
- Hybrid Cadence (Permanent Free Tier + One-Time Grant): 3 providers (Jina AI, Octen, OpenPerplex).

#### Reset Mechanics and Expiration Rules
1. Daily Reset Providers:
   - Tinyfish: Allowance resets at 00:00 UTC daily (12,000 searches, 1,000 fetches). Unused credits do not roll over.
   - Google Custom Search: Resets at midnight Pacific Time daily (100 searches).
   - Microlink: Resets every 24 hours (250 requests).
   - NewsAPI / GNews / Currents API: Daily resets.
   - Stack Exchange: Quota resets at 00:00 UTC daily (10,000 requests with API key).

2. Monthly Reset Providers:
   - Keenable: Allowance resets on organization grant-anchor day (100,000 requests).
   - Firecrawl: Resets on monthly signup date (1,000 credits). Unused credits expire.
   - Tavily: Resets on monthly billing date (1,000 credits).
   - Scrape.do: Resets monthly (1,000 calls).
   - Webscraping.ai: Resets monthly (2,000 calls).
   - ScrapingAnt: Resets monthly (1,000 credits).
   - Apify: $5 usage credit resets on monthly renewal date.
   - Browserless: 1,000 units reset on monthly renewal date.

3. Trial Expiration Policies:
   - Fixed Window Trials: ScraperAPI (7 days), Diffbot (14 days), Urlbox (7 days), NetNut (7 days). These credits expire if not consumed within the trial window.
   - Non-Expiring Signup Balances: Serper.dev (2,500 queries remain until consumed), Steel.dev ($30 credit), Octen ($5 balance), Exa ($10 credit), ScrapingRobot (5,000 credits remain indefinitely).

#### Operational Gateway Strategy
The unified gateway must partition traffic between permanent recurring allowances and one-time trial credits. Baseline continuous background scraping and routine search tasks must route exclusively to daily and monthly recurring tiers. One-time trial credits should be reserved for spike workloads or difficult target domains requiring specialized unblockers.

---

### 3.4 Market Maturity, Popularity, and Awareness Matrix

Providers fall into four generational cohorts reflecting distinct architectural paradigms:

| Cohort | Era | Exemplar Providers | Key Characteristics | Production Reliability |
|---|---|---|---|---|
| 1. Legacy Search & Web Giants | 2000-2018 | Google Search, Microsoft Bing, Diffbot, Zyte, Wikipedia, Crossref, arXiv | Mature infrastructure, billions of requests served, high SLA stability, traditional REST/SOAP APIs | Extreme (Five Nines) |
| 2. Commercial Proxy & Scraping Clouds | 2018-2022 | Bright Data, Oxylabs, ScrapingBee, ScraperAPI, Crawlbase, ZenRows, Apify, Browserless, Scrape.do | Massive residential proxy pools, automated CAPTCHA solvers, proven enterprise customer bases | Very High (99.9%+) |
| 3. Neural Search & AI Grounding Engines | 2022-2024 | Jina AI, Tavily, Exa, Perplexity, You.com, Serper, AgentQL | Native LLM Markdown output, citation generation, semantic embeddings, standard in agent SDKs | High (Rapid Growth) |
| 4. Autonomous Agent Web Infrastructure | 2024-2026 | Tinyfish, Keenable, Firecrawl, Crawl4AI, Steel.dev, Browserbase, Treg, Parallel | Machine Payments Protocol (MPP), x402 crypto micropayments, LLMs.txt indexing, MCP server tools | Emerging / High Agility |

---

### 3.5 Post-Signup Bonuses, Tier Escalations, and Credit Mechanics

Several providers offer documented mechanisms to increase credit limits or unlock advanced features post-registration:

1. Corporate Email Domain Verification:
   - Oxylabs: Grants 5,000 free request trial exclusively when registered with a corporate domain name (refuses generic Gmail/Outlook addresses).
   - Nimbleway: Unlocks a $20 credit evaluation package upon business email confirmation.
   - Context.dev: Unlocks team workspaces and developer evaluation tiers upon work email registration.

2. Payment Card Verification (Without Immediate Charge):
   - Octen: Registration yields $5 balance; adding a credit card unlocks the Base tier at 20 QPS Web Search at $0 monthly subscription fee.
   - Brave Search API: Adding a payment card enables the permanent 2,000 query/month free tier with no recurring monthly fee.
   - Microsoft Azure: Adding a card provides a $200 30-day trial credit and permanent access to Bing F0 Free Tier (1,000 queries/month).

3. Credit Coupon and Dashboard Voucher Redemption:
   - Firecrawl: Maintains a credit coupon entry field in the billing dashboard (`firecrawl.dev/app/billing`) for partner promotions, hackathons, and developer conferences.
   - Tavily: Grants extended developer credits for community participants and LangChain hackathons.

4. Top-Up Volume Multipliers:
   - Search1API: Top-ups earn progressive credit bonuses: $19 yields +5%, $99 yields +20%, and $499 yields +60% bonus credits (798,400 credits total).
   - Olostep: Offers non-expiring credit packs ($20 for 10k credits, $200 for 250k credits) avoiding recurring monthly commitments.

5. Sovereign Open-Source Unlocks (Zero Financial Overhead):
   - Crawl4AI, Firecrawl, SearXNG, Browserless, and Steel.dev all offer open-source cores. Deploying locally via Docker Compose completely bypasses commercial quota gates.

---

## 4. Additional 5 Deep Technical Architecture Reviews

This section reviews five additional critical providers: Jina AI (Reader & Search), Tavily (agentic search and extraction), Exa (neural embeddings search), Crawl4AI (open-source sovereign crawler), and Serper (low-latency Google SERP parser).

### 4.1 Deep Review: Jina AI (Reader & Search)

#### Architecture Overview
Jina AI (jina.ai) provides two foundational web access primitives: Jina Reader (`r.jina.ai`) and Jina Search (`s.jina.ai`). The system is architected as an HTTP proxy prefix: prepending `https://r.jina.ai/` to any destination URL fetches the page, executes dynamic JavaScript, strips noise and boilerplate, and returns clean Markdown tailored for LLM context windows.

#### Endpoint Specifications and Quotas
- Reader Prefix: `GET https://r.jina.ai/{URL}`
- Search Prefix: `GET https://s.jina.ai/{QUERY}`
- Grounding Endpoint: `POST https://g.jina.ai`
- Free Allowance: 1,000,000 tokens free on API key registration. Additionally, Jina supports completely keyless, unauthenticated access rate-limited to 20 requests per minute per IP.
- Token Consumption: Charged based on returned tokens. Standard web page conversions consume between 500 and 3,000 tokens.

#### Technical Features
- Image Captioning: Automatically inspects images on target pages and generates text descriptions using visual language models.
- PDF Extraction: Natively parses PDF links and converts documents into structured Markdown headings and tables.
- Header Controls: Supports `X-Return-Format: markdown|html|text`, `X-With-Generated-Alt: true`, and `X-Target-Selector: css`.

#### Gateway Role
Jina Reader serves as the default single-page reader in the unified gateway due to its zero-configuration URL prefix syntax and fast response latency.

---

### 4.2 Deep Review: Tavily

#### Architecture Overview
Tavily (tavily.com) is an agentic search engine designed specifically for autonomous AI agents. Rather than returning raw SERP links, Tavily aggregates, scrapes, filters, and summarizes web results in a single round-trip API call.

#### Endpoint Specifications and Free Quotas
- Search API: `POST https://api.tavily.com/search`. Parameters include `query`, `search_depth` (`basic` vs `advanced`), `include_answer`, `include_raw_content`, and `max_results`.
- Extract API: `POST https://api.tavily.com/extract`. Takes a list of URLs and returns cleaned page text.
- Free Allowance: 1,000 credits per month recurring. No credit card required. `basic` search costs 1 credit; `advanced` search (which performs deeper multi-source extraction) costs 2 credits.
- Keyless Access: Supports keyless trial mode for quick agent testing with IP-based rate limiting.

#### Technical Features
- AI Synthesis: Generates an immediate factual answer grounded in cited source links.
- Domain Filtering: Supports `include_domains` and `exclude_domains` to focus searches on authoritative sources.
- Time Filtering: Offers `time_range` (`day`, `week`, `month`, `year`) for fresh news retrieval.

#### Gateway Role
Tavily acts as the primary research-grade search engine in the gateway for complex agent reasoning queries where synthesized factual answers and pre-scraped context save token overhead.

---

### 4.3 Deep Review: Exa (Metaphor)

#### Architecture Overview
Exa (exa.ai) is a neural search engine built on embedding models rather than lexical keywords. Exa indexes the web by predicting what link would naturally follow a given prompt. Queries can be expressed in natural language, semantic descriptions, or example URLs.

#### Endpoint Specifications and Free Quotas
- Search API: `POST https://api.exa.ai/search`. Supports `type: "neural"` or `type: "keyword"`.
- Content Retrieval: `POST https://api.exa.ai/contents`. Retrieves full text, highlights, and summary snippets.
- Answer API: `POST https://api.exa.ai/answer`. Returns direct answers with citations.
- Free Allowance: $10 free credit on signup without a credit card. At standard rates ($1 to $5 per 1,000 queries depending on content options), this provides 1,000 to 2,000 searches.

#### Technical Features
- Similar Link Finding: Given a known good URL (e.g., an exceptional engineering blog post), Exa finds semantically similar URLs across the web.
- Date and Domain Filtering: Highly granular filtering by publication date and domain authority.
- Continuous Monitors: Exa Monitors API allows setting up recurring searches that trigger webhooks when newly discovered pages match semantic criteria.

#### Gateway Role
Exa is utilized in the gateway for exploratory semantic search, academic discovery, and finding high-relevance technical resources that traditional keyword search engines fail to locate.

---

### 4.4 Deep Review: Crawl4AI

#### Architecture Overview
Crawl4AI (crawl4ai.com) is a high-performance open-source asynchronous web crawler and scraping engine written in Python and built on Playwright. It is engineered specifically to feed clean, formatted data directly into large language models.

#### Architectural Mechanics and Capabilities
- Asynchronous Architecture: Uses `AsyncWebCrawler` with asyncio event loops to scrape hundreds of URLs concurrently.
- Stealth Browser Configuration: Integrates anti-detection techniques including user-agent rotation, navigator property patching, and automated cookie consent handling.
- Extraction Strategies: Supports CSS/XPath extractors, Cosine Similarity extractors (semantic clustering), and LLM-assisted JSON schema extractors.
- Fit Markdown Engine: Applies heuristic text pruning to eliminate navigation menus, footer disclosures, and advertisement sidebars, producing compact Markdown that reduces LLM context window consumption by 40% to 70%.

#### Deployment and Economic Impact
Crawl4AI is licensed under Apache 2.0. When hosted in a local Docker container or cloud VM, it carries zero per-request licensing costs, zero rate limits, and zero credit card requirements. It can be paired with residential proxy providers (such as Webshare's free 10-proxy pool) to bypass basic IP blocks.

#### Gateway Role
Crawl4AI forms the sovereign backbone of the unified gateway. Any request that does not require proprietary third-party index access routes to local Crawl4AI workers first, reserving commercial API credits for blocked or high-difficulty targets.

---

### 4.5 Deep Review: Serper

#### Architecture Overview
Serper (serper.dev) is a low-latency, developer-first Google Search scraping API. It executes real-time Google queries across global datacenters and returns parsed, structured JSON matching Google's exact SERP elements in under 800 milliseconds.

#### Endpoint Specifications and Free Quotas
- Search Endpoint: `POST https://google.serper.dev/search`
- News Endpoint: `POST https://google.serper.dev/news`
- Images Endpoint: `POST https://google.serper.dev/images`
- Scrape Endpoint: `POST https://google.serper.dev/scrape`
- Free Allowance: 2,500 free queries upon registration. No credit card required. Free queries do not expire.
- Low Cost at Scale: Beyond the free trial, Serper charges $1.00 per 1,000 queries ($0.001/query), representing one of the lowest unit costs in the commercial SERP industry.

#### Technical Features
- Comprehensive SERP Parsing: Automatically extracts organic rankings, knowledge graph panels, answer boxes, people also ask clusters, sitelinks, and related searches.
- Worker.js Integration: Serper's clean REST API enables direct deployment inside Cloudflare Workers or edge functions with minimal code footprint.

#### Gateway Role
Serper serves as the fast Google SERP fallback engine in the unified gateway when native Google Custom Search quotas are depleted or when full Google SERP features (knowledge graph, sitelinks) are specifically needed.

---

## 5. Unified Gateway Implementation Blueprint

This section details the architectural specification and routing algorithm for a self-hosted personal unified gateway incorporating account pool rotation and multi-provider failover.

### 5.1 Gateway Routing Architecture and Fallback Ladders

The gateway exposes three standard endpoints to autonomous agents:
- `GET/POST /v1/search?q={query}`: Unified search routing across web search providers.
- `GET/POST /v1/fetch?url={target_url}`: Unified fetch routing returning clean Markdown or HTML.
- `POST /v1/crawl`: Unified multi-page crawler and mapper.

#### Cascading Fallback Hierarchy

1. Web Search Execution Ladder:
   - Primary Tier 1: Tinyfish Search (12,000 req/day per account; fast, free).
   - Secondary Tier 2: Keenable Search (100,000 req/month per account).
   - Tertiary Tier 3: Tavily Search (1,000 req/month per account; research-grade answer synthesis).
   - Quaternary Tier 4: Brave Search API (2,000 req/month per account; independent web index).
   - Quinary Tier 5: Google Custom Search JSON API (100 req/day per account) / Serper (2,500 trial queries).
   - Fallback Tier 6: SearXNG / DuckDuckGo Lite (local unmetered meta-search).

2. Web Fetch Execution Ladder:
   - Primary Tier 1: Jina AI Reader (`r.jina.ai/{url}`; 20 RPM keyless or 1M free tokens).
   - Secondary Tier 2: Tinyfish Fetch (1,000 URLs/day per account).
   - Tertiary Tier 3: Keenable Fetch (100,000 requests/month per account).
   - Quaternary Tier 4: Local Crawl4AI Worker (open-source Playwright cluster with stealth mode).
   - Quinary Tier 5 (Anti-Bot Escalation): Scrape.do (1,000 req/month) / Webscraping.ai (2,000 req/month) / ZenRows / Firecrawl enhanced mode.

---

### 5.2 Account Pool Rotation and Key Management Specification

To safely utilize 5 accounts per provider without cross-contamination or concurrent lockout:
- Key State Machine: Each API key is tracked in a local SQLite or in-memory state store with fields: `provider_id`, `account_index` (1 to 5), `api_key`, `status` (`ACTIVE`, `RATE_LIMITED`, `EXHAUSTED`, `ERROR`), `reset_at` (ISO timestamp), `daily_count`, `monthly_count`.
- Rate Limit Handling: Upon receiving HTTP 429 Too Many Requests, the gateway inspects the `Retry-After` header, sets the current key status to `RATE_LIMITED`, schedules reactivation, and immediately retries the request using the next available key in the round-robin pool.
- Quota Exhaustion Handling: Upon receiving HTTP 402 Payment Required or error payloads indicating balance depletion, the key is marked `EXHAUSTED` until the next calendar reset window.

---

### 5.3 Verification and Health Check Protocol

The gateway periodically executes automated health checks against test fixture endpoints to verify provider availability and egress health:
- Search Probe: Queries test terms ('latest open source llm news') and verifies response payload contains non-empty title and URL arrays.
- Fetch Probe: Fetches standard reference URLs (`https://example.com` and challenge-protected mirrors) and verifies returned Markdown contains valid content.
- Latency Tracking: Gateway logs rolling average latency per provider to dynamically route latency-critical agent tasks to the fastest answering provider.
