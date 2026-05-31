#!/usr/bin/env python3
"""
Backfill remaining missing imageUrls in src/fixtures.json by parsing
manufacturer product pages.

Run from repo root:
    python3 scripts/backfill_remaining_images.py

Requires:
    pip install requests beautifulsoup4

What it does:
  1. Loads src/fixtures.json
  2. For every fixture whose imageUrl is empty and whose `link` is a
     real http(s) URL (not a PDF, not blank), fetches the page
  3. Extracts a product hero image using brand-aware rules
     (og:image first, then brand-specific patterns)
  4. Writes the result back to src/fixtures.json
  5. Prints a summary of fills/misses
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
from typing import Optional

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print(
        "ERROR: please run `pip install requests beautifulsoup4` first",
        file=sys.stderr,
    )
    sys.exit(1)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIXTURES = os.path.join(ROOT, "src", "fixtures.json")

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0) "
    "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15"
)

# ----- brand-specific image extractors -----
# Each function takes (soup, html_text, page_url) and returns the
# absolute hero image URL, or None if it cannot find one.


def absolutize(img: str, page_url: str) -> str:
    if img.startswith("//"):
        return "https:" + img
    if img.startswith("/"):
        from urllib.parse import urljoin

        return urljoin(page_url, img)
    return img


def og_image(soup: BeautifulSoup) -> Optional[str]:
    for prop in ("og:image", "og:image:url", "twitter:image", "twitter:image:src"):
        m = soup.find("meta", property=prop) or soup.find("meta", attrs={"name": prop})
        if m and m.get("content"):
            url = m["content"].strip()
            # Skip obvious placeholders
            low = url.lower()
            if any(x in low for x in ("/og-image", "logo", "placeholder", "default-share")):
                continue
            return url
    return None


def extract_martin(soup, html, page_url):
    # Martin pages have a clean og:image
    return og_image(soup)


def extract_robe(soup, html, page_url):
    # Robe og:image is a generic site placeholder. Use the first
    # cdn.aws.robe.cz/v1/image/resize/<hash>?width=452 (product hero).
    m = re.search(
        r"https://cdn\.aws\.robe\.cz/v1/image/resize/[a-f0-9]+\?width=452[^\"' )]+",
        html,
    )
    return m.group(0).replace("&amp;", "&") if m else None


def extract_elation(soup, html, page_url):
    # Elation uses Shopify; og:image is reliable.
    url = og_image(soup)
    if url:
        return url
    m = re.search(
        r"https://cdn\.shopify\.com/s/files/[^\"']+?\.(?:jpg|jpeg|png|webp)",
        html,
    )
    return m.group(0) if m else None


def extract_ayrton(soup, html, page_url):
    url = og_image(soup)
    if url:
        return url
    # Ayrton wp-content/uploads images
    m = re.search(
        r"https://www\.ayrton\.eu/wp-content/uploads/[^\"' )]+?\.(?:jpg|jpeg|png|webp)",
        html,
    )
    return m.group(0) if m else None


def extract_chauvet(soup, html, page_url):
    url = og_image(soup)
    if url:
        return url
    m = re.search(
        r"https://chauvetprofessional\.com/wp-content/uploads/[^\"' )]+?\.(?:jpg|jpeg|png|webp)",
        html,
    )
    return m.group(0) if m else None


def extract_claypaky(soup, html, page_url):
    url = og_image(soup)
    if url:
        return url
    m = re.search(
        r"https://www\.claypaky\.it/[^\"' )]+?\.(?:jpg|jpeg|png|webp)",
        html,
    )
    return m.group(0) if m else None


def extract_glp(soup, html, page_url):
    url = og_image(soup)
    if url:
        return url
    m = re.search(
        r"https://(?:www\.)?(?:glp\.de|germanlightproducts\.com)/[^\"' )]+?\.(?:jpg|jpeg|png|webp)",
        html,
    )
    return m.group(0) if m else None


def extract_highend(soup, html, page_url):
    url = og_image(soup)
    if url:
        return url
    m = re.search(
        r"https://(?:www\.)?(?:etcconnect\.com|highend\.com)/[^\"' )]+?\.(?:jpg|jpeg|png|webp)",
        html,
    )
    return m.group(0) if m else None


def extract_varilite(soup, html, page_url):
    url = og_image(soup)
    if url:
        return url
    m = re.search(
        r"https://www\.vari-lite\.com/[^\"' )]+?\.(?:jpg|jpeg|png|webp)",
        html,
    )
    return m.group(0) if m else None


def extract_prg(soup, html, page_url):
    return og_image(soup)


def extract_etc(soup, html, page_url):
    return og_image(soup)


def extract_acme(soup, html, page_url):
    url = og_image(soup)
    if url:
        return url
    m = re.search(
        r"https://(?:en\.)?acmelighting\.com/[^\"' )]+?\.(?:jpg|jpeg|png|webp)",
        html,
    )
    return m.group(0) if m else None


def extract_adj(soup, html, page_url):
    return og_image(soup)


BRAND_EXTRACTORS = {
    "Martin": extract_martin,
    "Robe": extract_robe,
    "Elation": extract_elation,
    "Ayrton": extract_ayrton,
    "Chauvet": extract_chauvet,
    "Claypaky": extract_claypaky,
    "GLP": extract_glp,
    "High End Systems": extract_highend,
    "Vari-Lite": extract_varilite,
    "PRG": extract_prg,
    "ETC": extract_etc,
    "Acme": extract_acme,
    "ADJ": extract_adj,
}


def fetch(url: str) -> Optional[str]:
    try:
        r = requests.get(
            url,
            headers={
                "User-Agent": UA,
                "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.9",
            },
            timeout=20,
            allow_redirects=True,
        )
        if r.status_code != 200:
            print(f"    HTTP {r.status_code}", file=sys.stderr)
            return None
        return r.text
    except Exception as e:
        print(f"    fetch error: {e}", file=sys.stderr)
        return None


def main():
    with open(FIXTURES) as fp:
        data = json.load(fp)

    targets = [x for x in data if not (x.get("imageUrl") or "").strip()]
    print(f"Found {len(targets)} fixtures missing imageUrl")

    filled = 0
    no_link = 0
    bad_link = 0
    missed: list[tuple[int, str, str, str]] = []

    for rec in targets:
        link = (rec.get("link") or "").strip()
        if not link:
            no_link += 1
            continue
        if not link.startswith("http"):
            bad_link += 1
            continue
        if link.lower().endswith(".pdf"):
            # PDF links won't have an HTML page; skip and let user fill manually
            missed.append((rec["id"], rec["brand"], rec["model"], "PDF link"))
            continue

        print(f"id {rec['id']:3} | {rec['brand']} {rec['model']}")
        print(f"  -> {link}")
        html = fetch(link)
        if not html:
            missed.append((rec["id"], rec["brand"], rec["model"], "fetch failed"))
            time.sleep(0.4)
            continue

        soup = BeautifulSoup(html, "html.parser")
        extractor = BRAND_EXTRACTORS.get(rec["brand"], lambda s, h, u: og_image(s))
        img = extractor(soup, html, link)
        if img:
            img = absolutize(img, link)
            rec["imageUrl"] = img
            filled += 1
            print(f"  OK: {img[:100]}")
        else:
            missed.append((rec["id"], rec["brand"], rec["model"], "no image found"))
            print("  MISS")

        # Save incrementally so a crash doesn't lose work
        with open(FIXTURES, "w") as fp:
            json.dump(data, fp, indent=2, ensure_ascii=False)

        time.sleep(0.4)

    print()
    print(f"  Filled:   {filled}")
    print(f"  No link:  {no_link}")
    print(f"  Bad link: {bad_link}")
    print(f"  Misses:   {len(missed)}")
    if missed:
        print()
        print("Misses (need manual lookup):")
        for fid, brand, model, why in missed:
            print(f"  id {fid:3} | {brand} {model}  --  {why}")


if __name__ == "__main__":
    main()
