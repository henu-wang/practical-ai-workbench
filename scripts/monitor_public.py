#!/usr/bin/env python3
"""Read-only public release checks. Technical accessibility never proves indexing."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import tempfile
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlsplit, urlunsplit
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
ROBOTS_SOURCE = "https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec"
UA = "TokRepo-Public-Technical-Check/1.0"


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def public_url(value):
    parts = urlsplit(value)
    if parts.scheme not in {"http", "https"} or not parts.hostname or parts.username or parts.password:
        raise ValueError("Use an HTTP(S) URL without embedded credentials.")
    return value


def fetch(url, timeout=20, max_bytes=2 * 1024 * 1024):
    started = utc_now()
    response = None
    try:
        try:
            response = urlopen(Request(public_url(url), headers={"User-Agent": UA}), timeout=timeout)
        except HTTPError as exc:
            response = exc
        with response:
            body = response.read(max_bytes + 1)
            headers = response.headers
            xrobots = headers.get_all("X-Robots-Tag") or []
            return {
                "url": url, "final_url": response.geturl(), "started_at": started,
                "checked_at": utc_now(), "http_status": response.code,
                "headers": {name: headers.get(name) for name in
                            ("Content-Type", "Content-Length", "ETag", "Last-Modified", "Date")
                            if headers.get(name) is not None},
                "x_robots_tag": xrobots, "body_truncated": len(body) > max_bytes,
                "body_bytes_read": min(len(body), max_bytes), "_body": body[:max_bytes],
                "error": None,
            }
    except (OSError, URLError, ValueError) as exc:
        return {
            "url": url, "final_url": None, "started_at": started,
            "checked_at": utc_now(), "http_status": None, "headers": {},
            "x_robots_tag": [], "body_truncated": False, "body_bytes_read": 0,
            "_body": b"", "error": {"type": type(exc).__name__, "message": str(exc)},
        }


class PageHTML(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.canonicals, self.robots, self.links = [], [], []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "link" and "canonical" in attrs.get("rel", "").lower().split():
            self.canonicals.append(attrs.get("href", ""))
        if tag == "meta" and attrs.get("name", "").lower() in {"robots", "googlebot"}:
            self.robots.append({"agent": attrs["name"].lower(), "content": attrs.get("content", "")})
        if tag == "a" and attrs.get("href"):
            self.links.append({"href": attrs["href"], "download": "download" in attrs})


def normalize_url(value):
    parts = urlsplit(value)
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), parts.path or "/", parts.query, parts.fragment))


def has_noindex(value):
    # "none" is shorthand for noindex,nofollow. Do not mistake nofollow for noindex.
    return bool(re.search(r"(?i)\b(?:noindex|none)\b", value))


def inspect_page(result, expected_url, template_root):
    parsed = PageHTML()
    issues = []
    if result["http_status"] != 200:
        issues.append("page_http_not_200")
    if result["body_truncated"]:
        issues.append("page_body_truncated")
    parsed.feed(result["_body"].decode("utf-8", errors="replace"))
    canonical_urls = [urljoin(result["final_url"] or expected_url, value) for value in parsed.canonicals]
    canonical_ok = (len(canonical_urls) == 1 and bool(parsed.canonicals[0].strip())
                    and normalize_url(canonical_urls[0]) == normalize_url(expected_url))
    if not canonical_ok:
        issues.append("missing_multiple_or_nonself_canonical")
    noindex = [item for item in parsed.robots if has_noindex(item["content"])]
    x_noindex = [value for value in result["x_robots_tag"] if has_noindex(value)]
    if noindex or x_noindex:
        issues.append("noindex_or_none_directive")
    if result["final_url"] and normalize_url(result["final_url"]) != normalize_url(expected_url):
        issues.append("unexpected_page_redirect")
    template_links = sorted({
        urljoin(result["final_url"] or expected_url, item["href"])
        for item in parsed.links
        if urljoin(result["final_url"] or expected_url, item["href"]).startswith(template_root)
    })
    return {
        "http": clean_http(result), "expected_url": expected_url, "canonical_urls": canonical_urls,
        "self_canonical": canonical_ok, "meta_robots": parsed.robots,
        "noindex_found": bool(noindex or x_noindex), "template_links": template_links,
        "issues": issues, "technical_pass": not issues, "indexing_status": "unknown",
    }


def clean_http(result):
    return {key: value for key, value in result.items() if key != "_body"}


def robots_groups(body):
    """Relevant Googlebot/* groups; longest matching allow/disallow path wins."""
    groups, agents, rules = [], [], []
    for line in body.lstrip("\ufeff").splitlines():
        line = line.split("#", 1)[0].strip()
        if ":" not in line:
            continue
        field, value = (part.strip() for part in line.split(":", 1))
        field = field.lower()
        if field == "user-agent":
            if rules:
                groups.append((agents, rules))
                agents, rules = [], []
            agents.append(value.lower())
        elif field in {"allow", "disallow"} and agents and value:
            rules.append((field, value))
    if agents:
        groups.append((agents, rules))
    specific = [rules for agents, rules in groups if "googlebot" in agents]
    chosen = specific or [rules for agents, rules in groups if "*" in agents]
    return [rule for group in chosen for rule in group]


def rule_allows(rules, url):
    parts = urlsplit(url)
    path = parts.path + ("?" + parts.query if parts.query else "")
    matches = []
    for action, pattern in rules:
        anchored = pattern.endswith("$")
        stem = pattern[:-1] if anchored else pattern
        expression = "^" + re.escape(stem).replace(r"\*", ".*") + ("$" if anchored else "")
        if re.search(expression, path):
            matches.append((len(stem.replace("*", "")), action == "allow", pattern))
    if not matches:
        return {"allowed": True, "matched_rule": None}
    _, allowed, pattern = max(matches)  # Equal length: allow wins.
    return {"allowed": allowed, "matched_rule": pattern}


def inspect_robots(host_result, repo_result, pages):
    status = host_result["http_status"]
    policy, evaluations = "unknown", {}
    if status == 200 and not host_result["body_truncated"]:
        body = host_result["_body"].decode("utf-8", errors="replace")
        rules = robots_groups(body)
        evaluations = {url: rule_allows(rules, url) for url in pages}
        policy = "blocked" if any(not value["allowed"] for value in evaluations.values()) else "allowed_by_fetched_rules"
    elif status is not None and 400 <= status < 500 and status != 429:
        policy = "no_valid_robots_file_no_restrictions_under_google_documented_behavior"
    return {
        "effective_host_root": clean_http(host_result),
        "policy": policy, "googlebot_url_evaluations": evaluations,
        "observed_googlebot_crawl": "unknown",
        "explanation": (
            "Only origin-root /robots.txt is effective. A project-directory robots.txt is informational. "
            "Google treats 4xx other than 429 as no valid rules; this does not establish an actual crawl or index entry. "
            "Network errors, 429, 5xx and truncated robots responses remain unknown here; cached Google state is unavailable."
        ),
        "repository_robots": {"http": clean_http(repo_result), "effective_for_crawlers": False},
        "reference": ROBOTS_SOURCE,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=ROOT / "recipes.json")
    parser.add_argument("--site-url", help="Override manifest site_url for a deployed host or local QA server.")
    parser.add_argument("--recipe-prefix", default="workflows/", help="Default published recipe route prefix.")
    parser.add_argument("--output", type=Path, help="JSON receipt path; default is a unique file outside the repository.")
    parser.add_argument("--timeout", type=float, default=20)
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args(argv)
    if args.workers < 1 or args.timeout <= 0:
        parser.error("--workers and --timeout must be positive")
    manifest = json.loads(args.manifest.read_text())
    base = public_url(args.site_url or manifest["site_url"]).rstrip("/") + "/"
    template_root = urljoin(base, "templates/")
    origin = urlsplit(base)
    root_robots_url = urlunsplit((origin.scheme, origin.netloc, "/robots.txt", "", ""))
    repo_robots_url = urljoin(base, "robots.txt")
    sitemap_url = urljoin(base, "sitemap.xml")
    recipe_urls = {recipe["slug"]: urljoin(base, args.recipe_prefix.strip("/") + "/" + recipe["slug"] + "/")
                   for recipe in manifest["recipes"]}
    if not recipe_urls or len(recipe_urls) != len(manifest["recipes"]):
        parser.error("Manifest requires a non-empty list of unique recipe slugs.")
    urls = sorted({base, *recipe_urls.values(), root_robots_url, repo_robots_url, sitemap_url})
    with ThreadPoolExecutor(max_workers=min(args.workers, 8)) as pool:
        fetched = dict(zip(urls, pool.map(lambda url: fetch(url, args.timeout), urls)))
    pages = {url: inspect_page(fetched[url], url, template_root) for url in [base, *recipe_urls.values()]}
    sitemap = fetched[sitemap_url]
    sitemap_entries, sitemap_error = [], None
    if sitemap["http_status"] == 200 and not sitemap["body_truncated"]:
        try:
            tree = ET.fromstring(sitemap["_body"])
            if tree.tag.rsplit("}", 1)[-1] != "urlset":
                raise ValueError("Expected this project's urlset sitemap; sitemap indexes are not expanded.")
            sitemap_entries = [element.text.strip() for element in tree.iter()
                               if element.tag.rsplit("}", 1)[-1] == "loc" and element.text]
        except (ET.ParseError, ValueError) as exc:
            sitemap_error = str(exc)
    else:
        sitemap_error = "sitemap_http_not_200_or_truncated"
    for url, page in pages.items():
        page["in_sitemap"] = (None if sitemap_error is not None else
                              normalize_url(url) in {normalize_url(item) for item in sitemap_entries})
        if page["in_sitemap"] is False:
            page["issues"].append("page_missing_from_sitemap")
        page["technical_pass"] = not page["issues"]
    # Inspect downloaded links as actually published; no invented attachment names.
    template_urls = sorted({url for page in pages.values() for url in page["template_links"]})
    template_checks = {}
    with ThreadPoolExecutor(max_workers=min(args.workers, 8)) as pool:
        for url, result in zip(template_urls, pool.map(lambda url: fetch(url, args.timeout, 2048), template_urls)):
            looks_html = ("text/html" in result["headers"].get("Content-Type", "").lower()
                          or result["_body"].lstrip().lower().startswith((b"<!doctype html", b"<html")))
            expected_html = urlsplit(url).path.lower().endswith((".html", ".htm"))
            ok = result["http_status"] == 200 and not (looks_html and not expected_html)
            template_checks[url] = {"http": clean_http(result), "technical_pass": ok,
                                    "unexpected_html_instead_of_attachment": looks_html and not expected_html,
                                    "content_or_runtime_validated": False}
    warnings = [f"no_template_link_discovered:{slug}" for slug, url in recipe_urls.items()
                if not pages[url]["template_links"]]
    robots = inspect_robots(fetched[root_robots_url], fetched[repo_robots_url], list(pages))
    technical_ok = (all(page["technical_pass"] for page in pages.values())
                    and all(item["technical_pass"] for item in template_checks.values())
                    and sitemap_error is None and robots["policy"] != "blocked")
    unknown = robots["policy"] == "unknown" or bool(warnings)
    state = "fail" if not technical_ok else ("needs_review" if unknown else "pass")
    receipt = {
        "schema_version": 1, "checked_at": utc_now(), "site_url": base,
        "manifest": str(args.manifest), "recipe_count": len(recipe_urls),
        "technical_status": state, "home": pages[base],
        "recipes": {slug: pages[url] for slug, url in recipe_urls.items()},
        "templates": template_checks,
        "sitemap": {"http": clean_http(sitemap), "entries": sitemap_entries, "error": sitemap_error},
        "robots": robots, "warnings": warnings,
        "search_observation": {"indexed": "unknown", "gsc_impressions": None, "gsc_clicks": None,
                               "queries": None, "countries": None, "position": None},
        "limits": [
            "Technical checks are not URL Inspection, indexing, ranking, traffic or asset-use evidence.",
            "Template HTTP200 does not verify the document opens or the recipe executes.",
            "Only template links found in public HTML are requested; missing recipe links require review.",
            "No account credentials, analytics API token or search-engine impersonation is used.",
        ],
    }
    output = args.output
    if output is None:
        with tempfile.NamedTemporaryFile(prefix="tokrepo-public-monitor-", suffix=".json", delete=False) as handle:
            output = Path(handle.name)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"technical_status": state, "recipe_count": len(recipe_urls),
                      "template_count": len(template_checks), "output": str(output),
                      "indexed": "unknown"}))
    return 1 if state == "fail" else (2 if state == "needs_review" else 0)


if __name__ == "__main__":
    raise SystemExit(main())
