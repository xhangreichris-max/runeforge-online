import xml.etree.ElementTree as ET
import urllib.request
import json

KEY = "f1070114dd2941a781a77d3418ec5422"
BASE = "https://runeforge.online"
SITEMAPS = [
    "https://runeforge.online/sitemap.xml",
    "https://runeforge.online/sitemap-de.xml"
]

def get_urls_from_sitemap(sitemap_url):
    urls = []
    with urllib.request.urlopen(sitemap_url) as r:
        tree = ET.parse(r)
    ns = {'sm': 'https://www.sitemaps.org/schemas/sitemap/0.9'}
    for loc in tree.findall('.//sm:loc', ns):
        urls.append(loc.text.strip())
    return urls

all_urls = []
for sitemap in SITEMAPS:
    all_urls.extend(get_urls_from_sitemap(sitemap))

print(f"Total URLs: {len(all_urls)}")

payload = {
    "host": "runeforge.online",
    "key": KEY,
    "keyLocation": f"{BASE}/{KEY}.txt",
    "urlList": all_urls
}

req = urllib.request.Request(
    "https://api.indexnow.org/indexnow",
    data=json.dumps(payload).encode(),
    headers={"Content-Type": "application/json"},
    method="POST"
)

with urllib.request.urlopen(req) as r:
    print(f"Status: {r.status}")
    print(f"Response: {r.read().decode()}")
