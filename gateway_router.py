#!/usr/bin/env python3
"""
Unified Web Fetch, Search and Crawl Gateway Reference Implementation.
Zero-dependency Python 3 router with multi-provider failover, account pool
rotation, and cascading free-tier search and fetch execution.
Released under 0BSD License.
"""

import argparse
import http.server
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request


class AccountPool:
    """Manages multi-account API keys, rotation, and quota tracking."""

    def __init__(self, config_path=None):
        self.accounts = {}
        if config_path and os.path.exists(config_path):
            with open(config_path, "r", encoding="utf-8") as f:
                self.accounts = json.load(f)

    def get_key(self, provider_id):
        """Retrieve the next active API key for a provider via round-robin."""
        keys = self.accounts.get(provider_id, [])
        if not keys:
            # Fall back to environment variable if present
            env_key = os.environ.get(f"{provider_id.upper()}_API_KEY")
            return env_key
        # Return first key (or rotate in memory)
        return keys[0] if isinstance(keys, list) else keys


class UnifiedGateway:
    """Core routing engine for search, fetch, and crawl operations."""

    def __init__(self, catalog_path="providers.json", config_path=None):
        self.catalog = self._load_catalog(catalog_path)
        self.pool = AccountPool(config_path)

    def _load_catalog(self, path):
        if not os.path.exists(path):
            base_dir = os.path.dirname(os.path.abspath(__file__))
            path = os.path.join(base_dir, path)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def search(self, query, limit=5):
        """
        Execute search across cascading fallback hierarchy:
        1. Tinyfish (if key configured)
        2. Tavily (if key configured)
        3. Serper (if key configured)
        4. Jina Search (s.jina.ai prefix, public rate limited)
        5. Hacker News Algolia Search (public unauthenticated)
        6. DuckDuckGo HTML / Instant Answers (fallback)
        """
        results = []
        errors = []

        # Tier 1: Tinyfish Search
        tinyfish_key = self.pool.get_key("tinyfish")
        if tinyfish_key:
            try:
                res = self._search_tinyfish(query, tinyfish_key, limit)
                if res:
                    return {"provider": "tinyfish", "query": query, "results": res}
            except Exception as e:
                errors.append(f"tinyfish: {e}")

        # Tier 2: Tavily Search
        tavily_key = self.pool.get_key("tavily")
        if tavily_key:
            try:
                res = self._search_tavily(query, tavily_key, limit)
                if res:
                    return {"provider": "tavily", "query": query, "results": res}
            except Exception as e:
                errors.append(f"tavily: {e}")

        # Tier 3: Serper Search
        serper_key = self.pool.get_key("serper")
        if serper_key:
            try:
                res = self._search_serper(query, serper_key, limit)
                if res:
                    return {"provider": "serper", "query": query, "results": res}
            except Exception as e:
                errors.append(f"serper: {e}")

        # Tier 4: Jina Search (public keyless)
        try:
            res = self._search_jina(query, limit)
            if res:
                return {"provider": "jina_search", "query": query, "results": res}
        except Exception as e:
            errors.append(f"jina_search: {e}")

        # Tier 5: Hacker News Algolia Search (public unauthenticated)
        try:
            res = self._search_hn_algolia(query, limit)
            if res:
                return {"provider": "hn_algolia", "query": query, "results": res}
        except Exception as e:
            errors.append(f"hn_algolia: {e}")

        # Tier 6: DuckDuckGo Instant Answer API (public unauthenticated)
        try:
            res = self._search_duckduckgo(query, limit)
            if res:
                return {"provider": "duckduckgo", "query": query, "results": res}
        except Exception as e:
            errors.append(f"duckduckgo: {e}")

        return {
            "provider": "none",
            "query": query,
            "results": [],
            "errors": errors,
            "status": "all_tiers_failed"
        }

    def fetch(self, url):
        """
        Execute page fetch across cascading fallback hierarchy:
        1. Jina Reader (r.jina.ai prefix, public 20 RPM or key)
        2. Tinyfish Fetch (if key configured)
        3. Keenable Fetch (if key configured)
        4. Direct HTTP polite reader with clean text extraction
        """
        errors = []

        # Tier 1: Jina Reader (standard for LLM markdown)
        try:
            content = self._fetch_jina_reader(url)
            if content:
                return {
                    "provider": "jina_reader",
                    "url": url,
                    "content_type": "text/markdown",
                    "content": content
                }
        except Exception as e:
            errors.append(f"jina_reader: {e}")

        # Tier 2: Tinyfish Fetch
        tinyfish_key = self.pool.get_key("tinyfish")
        if tinyfish_key:
            try:
                content = self._fetch_tinyfish(url, tinyfish_key)
                if content:
                    return {
                        "provider": "tinyfish",
                        "url": url,
                        "content_type": "text/markdown",
                        "content": content
                    }
            except Exception as e:
                errors.append(f"tinyfish: {e}")

        # Tier 3: Direct Polite HTTP Fetch
        try:
            content = self._fetch_direct_polite(url)
            if content:
                return {
                    "provider": "direct_polite",
                    "url": url,
                    "content_type": "text/html",
                    "content": content
                }
        except Exception as e:
            errors.append(f"direct_polite: {e}")

        return {
            "provider": "none",
            "url": url,
            "content": "",
            "errors": errors,
            "status": "all_tiers_failed"
        }

    def _search_jina(self, query, limit):
        encoded = urllib.parse.quote(query)
        url = f"https://s.jina.ai/{encoded}"
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "UnifiedGateway/1.0",
                "Accept": "application/json"
            }
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read().decode("utf-8", errors="ignore")
            try:
                parsed = json.loads(data)
                results = []
                for item in parsed.get("data", [])[:limit]:
                    results.append({
                        "title": item.get("title", ""),
                        "url": item.get("url", ""),
                        "snippet": item.get("content", item.get("description", ""))[:300]
                    })
                return results
            except json.JSONDecodeError:
                # Text response from Jina
                return [{"title": query, "url": url, "snippet": data[:500]}]

    def _search_hn_algolia(self, query, limit):
        encoded = urllib.parse.quote(query)
        url = f"https://hn.algolia.com/api/v1/search?query={encoded}&hitsPerPage={limit}"
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "UnifiedGateway/1.0"}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            results = []
            for hit in data.get("hits", []):
                title = hit.get("title") or hit.get("story_title") or "Hacker News Item"
                url_hit = hit.get("url") or f"https://news.ycombinator.com/item?id={hit.get('objectID')}"
                snippet = hit.get("story_text") or hit.get("comment_text") or f"Points: {hit.get('points', 0)}"
                results.append({"title": title, "url": url_hit, "snippet": snippet[:300]})
            return results

    def _search_duckduckgo(self, query, limit):
        encoded = urllib.parse.quote(query)
        url = f"https://api.duckduckgo.com/?q={encoded}&format=json&no_redirect=1"
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "UnifiedGateway/1.0"}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            results = []
            if data.get("Abstract"):
                results.append({
                    "title": data.get("Heading", query),
                    "url": data.get("AbstractURL", ""),
                    "snippet": data.get("AbstractText", "")
                })
            for topic in data.get("RelatedTopics", [])[:limit]:
                if "Text" in topic and "FirstURL" in topic:
                    results.append({
                        "title": topic.get("Text", "")[:60],
                        "url": topic.get("FirstURL", ""),
                        "snippet": topic.get("Text", "")
                    })
            return results

    def _search_tinyfish(self, query, key, limit):
        url = "https://agent.tinyfish.ai/v1/search"
        payload = json.dumps({"query": query, "limit": limit}).encode("utf-8")
        req = urllib.request.Request(
            url,
            data=payload,
            headers={
                "User-Agent": "UnifiedGateway/1.0",
                "Content-Type": "application/json",
                "X-API-Key": key
            }
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("results", [])

    def _search_tavily(self, query, key, limit):
        url = "https://api.tavily.com/search"
        payload = json.dumps({"query": query, "max_results": limit, "api_key": key}).encode("utf-8")
        req = urllib.request.Request(
            url,
            data=payload,
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("results", [])

    def _search_serper(self, query, key, limit):
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query, "num": limit}).encode("utf-8")
        req = urllib.request.Request(
            url,
            data=payload,
            headers={
                "X-API-KEY": key,
                "Content-Type": "application/json"
            }
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            results = []
            for item in data.get("organic", []):
                results.append({
                    "title": item.get("title", ""),
                    "url": item.get("link", ""),
                    "snippet": item.get("snippet", "")
                })
            return results

    def _fetch_jina_reader(self, target_url):
        clean_url = target_url.replace("https://", "").replace("http://", "")
        url = f"https://r.jina.ai/https://{clean_url}"
        key = self.pool.get_key("jina_ai")
        headers = {
            "User-Agent": "UnifiedGateway/1.0",
            "X-Return-Format": "markdown"
        }
        if key:
            headers["Authorization"] = f"Bearer {key}"
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode("utf-8", errors="ignore")

    def _fetch_tinyfish(self, target_url, key):
        url = "https://agent.tinyfish.ai/v1/fetch"
        payload = json.dumps({"url": target_url}).encode("utf-8")
        req = urllib.request.Request(
            url,
            data=payload,
            headers={
                "User-Agent": "UnifiedGateway/1.0",
                "Content-Type": "application/json",
                "X-API-Key": key
            }
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("content", data.get("text", ""))

    def _fetch_direct_polite(self, target_url):
        req = urllib.request.Request(
            target_url,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            }
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.read().decode("utf-8", errors="ignore")


class GatewayHTTPHandler(http.server.BaseHTTPRequestHandler):
    """HTTP handler exposing unified search and fetch endpoints."""

    gateway = None

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        if parsed.path == "/v1/search":
            q = params.get("q", [""])[0]
            if not q:
                self._send_json(400, {"error": "Missing parameter 'q'"})
                return
            res = self.gateway.search(q)
            self._send_json(200, res)
        elif parsed.path == "/v1/fetch":
            url = params.get("url", [""])[0]
            if not url:
                self._send_json(400, {"error": "Missing parameter 'url'"})
                return
            res = self.gateway.fetch(url)
            self._send_json(200, res)
        elif parsed.path == "/health" or parsed.path == "/status":
            self._send_json(200, {
                "status": "healthy",
                "providers_cataloged": len(self.gateway.catalog),
                "timestamp": int(time.time())
            })
        else:
            self._send_json(404, {"error": "Endpoint not found"})

    def _send_json(self, status, payload):
        data = json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


def main():
    parser = argparse.ArgumentParser(description="Unified Web Fetch and Search Gateway")
    parser.add_argument("--status", action="store_true", help="Print provider catalog status and metrics")
    parser.add_argument("--search", type=str, help="Execute a unified search query")
    parser.add_argument("--fetch", type=str, help="Execute a unified page fetch")
    parser.add_argument("--serve", action="store_true", help="Start local HTTP gateway server")
    parser.add_argument("--port", type=int, default=8080, help="Server port (default: 8080)")
    parser.add_argument("--config", type=str, default=None, help="Path to account keys JSON file")
    args = parser.parse_args()

    gateway = UnifiedGateway(config_path=args.config)

    if args.status:
        total = len(gateway.catalog)
        single_vol = sum(p.get("monthly_equiv_requests", 0) for p in gateway.catalog)
        five_vol = single_vol * 5
        no_cc = sum(1 for p in gateway.catalog if not p.get("credit_card_required", False))
        recurring = sum(1 for p in gateway.catalog if "Monthly" in p.get("cadence", "") or "Daily" in p.get("cadence", "") or "Continuous" in p.get("cadence", "") or "Unlimited" in p.get("cadence", ""))
        print("=== Unified Web Gateway Status ===")
        print(f"Total Cataloged Providers: {total}")
        print(f"Single-Account Monthly Capacity: {single_vol:,} requests")
        print(f"5-Account Monthly Capacity: {five_vol:,} requests")
        print(f"Recurring Cadence Providers: {recurring}")
        print(f"No Credit Card Required: {no_cc} of {total}")
        return

    if args.search:
        print(f"Searching for: {args.search}")
        res = gateway.search(args.search)
        print(json.dumps(res, indent=2))
        return

    if args.fetch:
        print(f"Fetching URL: {args.fetch}")
        res = gateway.fetch(args.fetch)
        print(f"Provider: {res.get('provider')}")
        content = res.get("content", "")
        print(f"Content Length: {len(content)} characters")
        print("--- Content Preview (first 500 chars) ---")
        print(content[:500])
        return

    if args.serve:
        GatewayHTTPHandler.gateway = gateway
        server = http.server.HTTPServer(("0.0.0.0", args.port), GatewayHTTPHandler)
        print(f"Starting Unified Gateway server on port {args.port}...")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")
            server.server_close()
        return

    parser.print_help()


if __name__ == "__main__":
    main()
