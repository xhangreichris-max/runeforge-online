"""
RuneForge Page Builder
======================
Reads pages-config.json + template.html
Generates all HTML pages automatically
Also updates tools.js and sitemap.xml

Usage:
  python build.py              # Build all pages
  python build.py --page vampire  # Build one page only
"""

import json
import os
import sys
import re
from datetime import datetime

# ── PATHS ──────────────────────────────────────────────
ROOT_DIR     = os.path.dirname(os.path.abspath(__file__))
TEMPLATE     = os.path.join(ROOT_DIR, 'template.html')
CONFIG       = os.path.join(ROOT_DIR, 'pages-config.json')
OUTPUT_DIR   = ROOT_DIR  # pages go in root
TOOLS_JS     = os.path.join(ROOT_DIR, 'tools.js')
SITEMAP      = os.path.join(ROOT_DIR, 'sitemap.xml')

# ── LOAD FILES ─────────────────────────────────────────
def load_template():
    with open(TEMPLATE, 'r', encoding='utf-8') as f:
        return f.read()

def load_config():
    with open(CONFIG, 'r', encoding='utf-8') as f:
        return json.load(f)

# ── BUILD FILTERS HTML ─────────────────────────────────
def build_filters(filters):
    html = ''
    for i, f in enumerate(filters):
        active = ' active' if i == 0 else ''
        html += f'<button class="filter-pill{active}" data-filter="{f["value"]}">{f["label"]}</button>\n      '
    return html.strip()

# ── BUILD RELATED CHIPS ────────────────────────────────
def build_related_chips(chips):
    html = ''
    for chip in chips:
        html += f'<a href="{chip["url"]}" class="chip">{chip["label"]}</a>\n    '
    return html.strip()

# ── BUILD SIDEBAR LINKS ────────────────────────────────
def build_sidebar_links(links):
    html = ''
    for link in links:
        html += f'<a href="{link["url"]}">{link["label"]}</a>\n      '
    return html.strip()

# ── BUILD SIDEBAR TIPS ─────────────────────────────────
def build_sidebar_tips(tips):
    html = ''
    for tip in tips:
        html += f'<li>{tip}</li>\n        '
    return html.strip()

# ── BUILD FAQ HTML ─────────────────────────────────────
def build_faq_html(faqs):
    html = ''
    for faq in faqs:
        html += f'''  <details>
    <summary>{faq["q"]}</summary>
    <div class="faq-answer">{faq["a"]}</div>
  </details>
'''
    return html.strip()

# ── BUILD FAQ SCHEMA ───────────────────────────────────
def build_faq_schema(faqs):
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": []
    }
    for faq in faqs:
        schema["mainEntity"].append({
            "@type": "Question",
            "name": faq["q"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": faq["a"]
            }
        })
    return json.dumps(schema, ensure_ascii=False)

# ── BUILD FOOTER LINKS ─────────────────────────────────
def build_footer_links(links):
    html = ''
    for link in links:
        html += f'<a href="{link["url"]}">{link["label"]}</a>\n        '
    return html.strip()

# ── BUILD PAGE FROM CONFIG ─────────────────────────────
def build_page(template, page):
    html = template

    replacements = {
        '{{META_TITLE}}':              page['meta_title'],
        '{{META_DESC}}':               page['meta_desc'],
        '{{PAGE_ID}}':                 page['id'],
        '{{PAGE_NAME}}':               page['page_name'],
        '{{PAGE_NAME_LOWER}}':         page['page_name'].lower(),
        '{{OG_TITLE}}':                page['og_title'],
        '{{H1_TEXT}}':                 page['h1_text'],
        '{{HERO_SUB}}':                page['hero_sub'],
        '{{HERO_BG}}':                 page['hero_bg'],
        '{{EYEBROW_TEXT}}':            page['eyebrow_text'],
        '{{HOWTO_STEP1}}':             page['howto_step1'],
        '{{BREADCRUMB_CATEGORY_NAME}}':page['breadcrumb_category_name'],
        '{{BREADCRUMB_CATEGORY_ID}}':  page['breadcrumb_category_id'],
        '{{FILTERS_HTML}}':            build_filters(page['filters']),
        '{{RELATED_CHIPS}}':           build_related_chips(page['related_chips']),
        '{{SEO_ARTICLE}}':             page['seo_article'],
        '{{SIDEBAR_LINKS}}':           build_sidebar_links(page['sidebar_links']),
        '{{SIDEBAR_TIPS}}':            build_sidebar_tips(page['sidebar_tips']),
        '{{SIDEBAR_PRO_TIP}}':         page['sidebar_pro_tip'],
        '{{FAQ_HTML}}':                build_faq_html(page['faq_items']),
        '{{FAQ_SCHEMA}}':              build_faq_schema(page['faq_items']),
        '{{FOOTER_LINKS}}':            build_footer_links(page['footer_links']),
        '{{NAME_DATA_JSON}}':          json.dumps(page['name_data'], ensure_ascii=False),
    }

    for placeholder, value in replacements.items():
        html = html.replace(placeholder, value)

    return html

# ── UPDATE TOOLS.JS ────────────────────────────────────
def update_tools_js(pages):
    """
    Reads existing tools.js and appends new entries.
    Only adds entries that don't already exist (checks by id).
    """
    if not os.path.exists(TOOLS_JS):
        print(f"  ⚠️  tools.js not found at {TOOLS_JS} — skipping")
        return

    with open(TOOLS_JS, 'r', encoding='utf-8') as f:
        content = f.read()

    added = 0
    for page in pages:
        entry = page.get('tools_js_entry')
        if not entry:
            continue
        page_id = entry['id']
        if f'"id": "{page_id}"' in content or f"id: \"{page_id}\"" in content:
            print(f"  ↷  tools.js: {page_id} already exists — skip")
            continue

        # Build the new entry string
        tags_str = ', '.join([f'"{t}"' for t in entry['tags']])
        new_entry = f"""  {{
    id: "{entry['id']}",
    name: "{entry['name']}",
    desc: "{entry['desc']}",
    category: "{entry['category']}",
    tags: [{tags_str}],
    icon: `{entry['icon']}`,
    url: "{entry['url']}",
    volume: {entry['volume']},
    kd: {entry['kd']},
    featured: {'true' if entry.get('featured') else 'false'}
  }},"""

        # Insert before the closing ]; of RUNEFORGE_TOOLS
        content = content.replace('\n];', f'\n{new_entry}\n];', 1)
        added += 1
        print(f"  ✅ tools.js: added {page_id}")

    if added > 0:
        with open(TOOLS_JS, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  💾 tools.js updated with {added} new entries")

# ── UPDATE SITEMAP.XML ─────────────────────────────────
def update_sitemap(pages):
    """
    Reads existing sitemap.xml and adds new URLs.
    Only adds URLs that don't already exist.
    """
    if not os.path.exists(SITEMAP):
        print(f"  ⚠️  sitemap.xml not found — skipping")
        return

    with open(SITEMAP, 'r', encoding='utf-8') as f:
        content = f.read()

    today = datetime.now().strftime('%Y-%m-%d')
    added = 0

    for page in pages:
        url = f"https://runeforge.online/{page['id']}.html"
        if url in content:
            print(f"  ↷  sitemap: {page['id']} already exists — skip")
            continue

        priority = page.get('sitemap_priority', '0.8')
        new_url = f"""
  <url>
    <loc>{url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{priority}</priority>
  </url>"""

        content = content.replace('</urlset>', f'{new_url}\n</urlset>')
        added += 1
        print(f"  ✅ sitemap: added {page['id']}")

    if added > 0:
        with open(SITEMAP, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  💾 sitemap.xml updated with {added} new URLs")

# ── MAIN BUILD ─────────────────────────────────────────
def main():
    print("\n🔨 RuneForge Page Builder")
    print("=" * 40)

    # Check if building single page
    single_page = None
    if '--page' in sys.argv:
        idx = sys.argv.index('--page')
        if idx + 1 < len(sys.argv):
            single_page = sys.argv[idx + 1]
            print(f"  Building single page: {single_page}")

    # Load files
    try:
        template = load_template()
        pages    = load_config()
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

    # Filter if single page
    if single_page:
        pages = [p for p in pages if single_page in p['id']]
        if not pages:
            print(f"❌ Page '{single_page}' not found in config")
            sys.exit(1)

    print(f"\n📄 Building {len(pages)} page(s)...\n")

    # Build each page
    built = []
    for page in pages:
        output_file = os.path.join(OUTPUT_DIR, f"{page['id']}.html")

        try:
            html = build_page(template, page)

            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html)

            print(f"  ✅ Built: {page['id']}.html")
            built.append(page)

        except KeyError as e:
            print(f"  ❌ Error building {page['id']}: missing key {e}")
        except Exception as e:
            print(f"  ❌ Error building {page['id']}: {e}")

    # Update tools.js and sitemap.xml
    if built:
        print(f"\n📝 Updating tools.js and sitemap.xml...")
        update_tools_js(built)
        update_sitemap(built)

    print(f"\n✅ Done! {len(built)}/{len(pages)} pages built successfully.")
    print("=" * 40 + "\n")

if __name__ == '__main__':
    main()