"""
RuneForge Page Builder
======================
English:
  Reads pages-config.json + template.html
  Writes [page-id].html to the repo root
  Updates tools.js and sitemap.xml
German:
  Reads pages-config-de.json + template-de.html
  Writes de/[page-id].html
  Updates tools-de.js and sitemap-de.xml

Usage:
  python build.py                 # Build English pages only (default, unchanged)
  python build.py --page vampire  # Build one English page only
  python build.py --de            # Build German pages only
  python build.py --all           # Build English + German
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

# ── PATHS (GERMAN) ──────────────────────────────────────
TEMPLATE_DE  = os.path.join(ROOT_DIR, 'template-de.html')
CONFIG_DE    = os.path.join(ROOT_DIR, 'pages-config-de.json')
OUTPUT_DIR_DE= os.path.join(ROOT_DIR, 'de')
TOOLS_JS_DE  = os.path.join(ROOT_DIR, 'tools-de.js')
SITEMAP_DE   = os.path.join(ROOT_DIR, 'sitemap-de.xml')

# ── LOAD FILES ─────────────────────────────────────────
def load_template():
    with open(TEMPLATE, 'r', encoding='utf-8') as f:
        return f.read()

def load_config():
    with open(CONFIG, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_template_de():
    with open(TEMPLATE_DE, 'r', encoding='utf-8') as f:
        return f.read()

def load_config_de():
    with open(CONFIG_DE, 'r', encoding='utf-8') as f:
        return json.load(f)

# ── URL HELPERS ─────────────────────────────────────────
def clean_url(url, prefix=''):
    """Strip a trailing .html so generated links use clean URLs.
    Optionally prepend a path prefix (e.g. '/de/') for German internal links."""
    stripped = url[:-5] if url.endswith('.html') else url
    return f'{prefix}{stripped}' if prefix else stripped

# ── BUILD FILTERS HTML ─────────────────────────────────
def build_filters(filters):
    html = ''
    for i, f in enumerate(filters):
        active = ' active' if i == 0 else ''
        html += f'<button class="filter-pill{active}" data-filter="{f["value"]}">{f["label"]}</button>\n      '
    return html.strip()

# ── BUILD RELATED CHIPS ────────────────────────────────
def build_related_chips(chips, url_prefix=''):
    html = ''
    for chip in chips:
        html += f'<a href="{clean_url(chip["url"], url_prefix)}" class="chip">{chip["label"]}</a>\n    '
    return html.strip()

# ── BUILD SIDEBAR LINKS ────────────────────────────────
def build_sidebar_links(links, url_prefix=''):
    html = ''
    for link in links:
        html += f'<a href="{clean_url(link["url"], url_prefix)}">{link["label"]}</a>\n      '
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
def build_faq_schema(faqs, lang=None):
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": []
    }
    if lang:
        schema["inLanguage"] = lang
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
def build_footer_links(links, url_prefix=''):
    html = ''
    for link in links:
        html += f'<a href="{clean_url(link["url"], url_prefix)}">{link["label"]}</a>\n        '
    return html.strip()

# ── BUILD NAME TABLE (GERMAN) ──────────────────────────
def build_name_table(entries, heading):
    """
    Renders the curated name-table section for German pages.
    Returns an empty string when entries is missing/empty so the
    {{NAME_TABLE}} placeholder produces no markup at all.
    """
    if not entries:
        return ''

    rows = ''
    for e in entries:
        rows += f'      <tr><td>{e["name"]}</td><td>{e["race"]}</td><td>{e["gender"]}</td><td>{e["meaning"]}</td></tr>\n'

    return f'''<section class="name-table-section">
  <h2 class="name-table-title">{heading}</h2>
  <table>
    <thead><tr><th>Name</th><th>Rasse</th><th>Geschlecht</th><th>Bedeutung</th></tr></thead>
    <tbody>
{rows}    </tbody>
  </table>
</section>'''

# ── BUILD HREFLANG BLOCK (ENGLISH -> DE TWIN) ──────────
def build_hreflang_block(page):
    """
    Reciprocal hreflang for an English page that has a live German
    twin (page['de_slug'] set). Returns '' when there is no German
    twin yet: an hreflang link pointing at a page that doesn't exist
    is worse than no hreflang at all.
    """
    de_slug = page.get('de_slug', '')
    if not de_slug:
        return ''

    page_id = page['id']
    return (
        f'<link rel="alternate" hreflang="en" href="https://runeforge.online/{page_id}">\n'
        f'<link rel="alternate" hreflang="de" href="https://runeforge.online/de/{de_slug}">\n'
        f'<link rel="alternate" hreflang="x-default" href="https://runeforge.online/{page_id}">'
    )

# ── BUILD PAGE FROM CONFIG ─────────────────────────────
def build_page(template, page):
    html = template

    replacements = {
        '{{META_TITLE}}':              page['meta_title'],
        '{{META_DESC}}':               page['meta_desc'],
        '{{ROBOTS}}':                  page.get('robots', 'index, follow'),
        '{{PAGE_ID}}':                 page['id'],
        '{{HREFLANG_BLOCK}}':          build_hreflang_block(page),
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

# ── BUILD GERMAN PAGE FROM CONFIG ──────────────────────
def build_page_de(template, page):
    html = template

    # hreflang conditional: if there's no English twin, drop the
    # en + x-default lines entirely rather than pointing them at
    # a bare "https://runeforge.online/{{EN_TWIN}}" -> "/" URL.
    en_twin = page.get('en_twin', '')
    if not en_twin:
        html = html.replace(
            '<link rel="alternate" hreflang="en" href="https://runeforge.online/{{EN_TWIN}}">\n', '')
        html = html.replace(
            '<link rel="alternate" hreflang="x-default" href="https://runeforge.online/{{EN_TWIN}}">\n', '')

    replacements = {
        '{{META_TITLE}}':              page['meta_title'],
        '{{META_DESC}}':               page['meta_desc'],
        '{{ROBOTS}}':                  page.get('robots', 'index, follow'),
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
        '{{RELATED_CHIPS}}':           build_related_chips(page['related_chips'], url_prefix='/de/'),
        '{{SEO_ARTICLE}}':             page['seo_article'],
        '{{SIDEBAR_LINKS}}':           build_sidebar_links(page['sidebar_links'], url_prefix='/de/'),
        '{{SIDEBAR_TIPS}}':            build_sidebar_tips(page['sidebar_tips']),
        '{{SIDEBAR_PRO_TIP}}':         page['sidebar_pro_tip'],
        '{{FAQ_HTML}}':                build_faq_html(page['faq_items']),
        '{{FAQ_SCHEMA}}':              build_faq_schema(page['faq_items'], lang='de'),
        '{{FOOTER_LINKS}}':            build_footer_links(page['footer_links'], url_prefix='/de/'),
        '{{NAME_DATA_JSON}}':          json.dumps(page['name_data'], ensure_ascii=False),
        '{{EN_TWIN}}':                 en_twin,
        '{{NAME_TABLE}}':              build_name_table(page.get('name_table'), page.get('name_table_heading', '')),
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
    url: "{clean_url(entry['url'])}",
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

# ── UPDATE TOOLS-DE.JS ─────────────────────────────────
def update_tools_js_de(pages):
    """
    Reads existing tools-de.js and appends new entries.
    Only adds entries that don't already exist (checks by id).
    Mirrors update_tools_js() but targets TOOLS_JS_DE and prefixes
    generated urls with /de/.
    """
    if not os.path.exists(TOOLS_JS_DE):
        print(f"  ⚠️  tools-de.js not found at {TOOLS_JS_DE} — skipping")
        return

    with open(TOOLS_JS_DE, 'r', encoding='utf-8') as f:
        content = f.read()

    added = 0
    for page in pages:
        entry = page.get('tools_js_entry')
        if not entry:
            continue
        page_id = entry['id']
        if f'"id": "{page_id}"' in content or f"id: \"{page_id}\"" in content:
            print(f"  ↷  tools-de.js: {page_id} already exists — skip")
            continue

        tags_str = ', '.join([f'"{t}"' for t in entry['tags']])
        new_entry = f"""  {{
    id: "{entry['id']}",
    name: "{entry['name']}",
    desc: "{entry['desc']}",
    category: "{entry['category']}",
    tags: [{tags_str}],
    icon: `{entry['icon']}`,
    url: "{clean_url(entry['url'], '/de/')}",
    volume: {entry['volume']},
    kd: {entry['kd']},
    featured: {'true' if entry.get('featured') else 'false'}
  }},"""

        content = content.replace('\n];', f'\n{new_entry}\n];', 1)
        added += 1
        print(f"  ✅ tools-de.js: added {page_id}")

    if added > 0:
        with open(TOOLS_JS_DE, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  💾 tools-de.js updated with {added} new entries")

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
        url = f"https://runeforge.online/{page['id']}"
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

# ── UPDATE SITEMAP-DE.XML ──────────────────────────────
def update_sitemap_de(pages):
    """
    Reads existing sitemap-de.xml and adds new URLs.
    Only adds URLs that don't already exist.
    Each <url> gets xhtml:link hreflang alternates (de always,
    en only when the page has an en_twin).
    """
    if not os.path.exists(SITEMAP_DE):
        print(f"  ⚠️  sitemap-de.xml not found — skipping")
        return

    with open(SITEMAP_DE, 'r', encoding='utf-8') as f:
        content = f.read()

    today = datetime.now().strftime('%Y-%m-%d')
    added = 0

    for page in pages:
        url = f"https://runeforge.online/de/{page['id']}"
        if url in content:
            print(f"  ↷  sitemap-de: {page['id']} already exists — skip")
            continue

        priority = page.get('sitemap_priority', '0.8')
        en_twin = page.get('en_twin', '')

        hreflang_links = f'\n    <xhtml:link rel="alternate" hreflang="de" href="{url}"/>'
        if en_twin:
            hreflang_links += f'\n    <xhtml:link rel="alternate" hreflang="en" href="https://runeforge.online/{en_twin}"/>'

        new_url = f"""
  <url>
    <loc>{url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{priority}</priority>{hreflang_links}
  </url>"""

        content = content.replace('</urlset>', f'{new_url}\n</urlset>')
        added += 1
        print(f"  ✅ sitemap-de: added {page['id']}")

    if added > 0:
        with open(SITEMAP_DE, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  💾 sitemap-de.xml updated with {added} new URLs")

# ── BUILD: ENGLISH ──────────────────────────────────────
def build_english(single_page=None):
    """English build path, extracted from the old main() with behavior unchanged
    (including the sys.exit(1) calls on a missing file or unmatched --page)."""
    try:
        template = load_template()
        pages    = load_config()
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

    if single_page:
        pages = [p for p in pages if single_page in p['id']]
        if not pages:
            print(f"❌ Page '{single_page}' not found in config")
            sys.exit(1)

    print(f"\n📄 Building {len(pages)} English page(s)...\n")

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

    if built:
        print(f"\n📝 Updating tools.js and sitemap.xml...")
        update_tools_js(built)
        update_sitemap(built)

    print(f"\n✅ English: {len(built)}/{len(pages)} pages built successfully.")

# ── BUILD: GERMAN ───────────────────────────────────────
def build_german():
    try:
        template_de = load_template_de()
        pages_de    = load_config_de()
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

    os.makedirs(OUTPUT_DIR_DE, exist_ok=True)

    print(f"\n📄 Building {len(pages_de)} German page(s)...\n")

    built = []
    for page in pages_de:
        output_file = os.path.join(OUTPUT_DIR_DE, f"{page['id']}.html")

        try:
            html = build_page_de(template_de, page)

            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html)

            print(f"  ✅ Built: de/{page['id']}.html")
            built.append(page)

        except KeyError as e:
            print(f"  ❌ Error building {page['id']}: missing key {e}")
        except Exception as e:
            print(f"  ❌ Error building {page['id']}: {e}")

    if built:
        print(f"\n📝 Updating tools-de.js and sitemap-de.xml...")
        update_tools_js_de(built)
        update_sitemap_de(built)

    print(f"\n✅ German: {len(built)}/{len(pages_de)} pages built successfully.")

# ── MAIN BUILD ─────────────────────────────────────────
def main():
    print("\n🔨 RuneForge Page Builder")
    print("=" * 40)

    # Check if building single English page
    single_page = None
    if '--page' in sys.argv:
        idx = sys.argv.index('--page')
        if idx + 1 < len(sys.argv):
            single_page = sys.argv[idx + 1]
            print(f"  Building single page: {single_page}")

    build_de  = '--de' in sys.argv
    build_all = '--all' in sys.argv

    if build_all:
        build_english(single_page)
        build_german()
    elif build_de:
        build_german()
    else:
        build_english(single_page)

    print("\n" + "=" * 40 + "\n")

if __name__ == '__main__':
    main()