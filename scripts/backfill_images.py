#!/usr/bin/env python3
"""
Backfill imageUrl for fixtures by parsing og:image / twitter:image
from the fixture's `link` field (manufacturer product page).

Skips fixtures with no link or non-product links (e.g. PDFs, news articles).
Run from repo root: python3 scripts/backfill_images.py
"""
import json, os, re, sys, time
from urllib.request import Request, urlopen
from urllib.parse import urljoin
import ssl

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(REPO, 'src', 'fixtures.json')

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15"
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

OG_RE = re.compile(
    r'<meta[^>]+(?:property|name)\s*=\s*["\'](?:og:image|og:image:url|twitter:image|twitter:image:src)["\'][^>]+content\s*=\s*["\']([^"\']+)["\']',
    re.IGNORECASE,
)
OG_RE_REVERSED = re.compile(
    r'<meta[^>]+content\s*=\s*["\']([^"\']+)["\'][^>]+(?:property|name)\s*=\s*["\'](?:og:image|og:image:url|twitter:image|twitter:image:src)["\']',
    re.IGNORECASE,
)


def find_image(url: str) -> str | None:
    if not url or not url.startswith('http'):
        return None
    # Skip PDFs and news articles — they won't have product og:image
    lower = url.lower()
    if lower.endswith('.pdf'):
        return None
    try:
        req = Request(url, headers={"User-Agent": UA, "Accept": "text/html"})
        with urlopen(req, timeout=15, context=CTX) as resp:
            html = resp.read(400_000).decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"  fetch error: {e}", file=sys.stderr)
        return None
    for rx in (OG_RE, OG_RE_REVERSED):
        m = rx.search(html)
        if m:
            img = m.group(1).strip()
            # absolutize
            if img.startswith('//'):
                img = 'https:' + img
            elif img.startswith('/'):
                img = urljoin(url, img)
            # Skip obvious logos/placeholders
            low = img.lower()
            if any(x in low for x in ('logo', 'placeholder', 'default-share', 'sprite')):
                return None
            return img
    return None


def main():
    with open(PATH) as fp:
        data = json.load(fp)
    targets = [x for x in data if not (x.get('imageUrl') or '').strip()]
    print(f"Targets: {len(targets)}")
    filled = 0
    no_link = 0
    failed = []
    for rec in targets:
        link = rec.get('link') or ''
        if not link:
            no_link += 1
            continue
        print(f"id {rec['id']:3} | {rec['brand']} {rec['model']}")
        print(f"  -> {link[:80]}")
        img = find_image(link)
        if img:
            rec['imageUrl'] = img
            filled += 1
            print(f"  OK: {img[:90]}")
        else:
            failed.append(rec)
            print(f"  MISS")
        time.sleep(0.5)

    with open(PATH, 'w') as out:
        json.dump(data, out, indent=2, ensure_ascii=False)

    print()
    print(f"Filled:  {filled}")
    print(f"No link: {no_link}")
    print(f"Missed:  {len(failed)}")
    if failed:
        print("Missed fixtures:")
        for x in failed:
            print(f"  id {x['id']:3} | {x['brand']} {x['model']} | {x.get('link','')[:80]}")


if __name__ == '__main__':
    main()
