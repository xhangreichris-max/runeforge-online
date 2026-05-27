# runeforge-online
Free fantasy name generators for D&amp;D, RPG &amp; worldbuilding — villains, elves, orcs, kingdoms &amp; more.
# RuneForge — Fantasy Name Generators

> Free fantasy name generators for D&D, RPG, worldbuilding, and creative writing.
> Built for writers, game masters, worldbuilders, and storytellers.

🌐 **Live site:** https://runeforge.online

---

## What is RuneForge?

RuneForge is a collection of free fantasy name generators covering characters,
places, creatures, and items. Every generator is built around authentic linguistic
patterns and fantasy archetypes — not random syllable soup.

No signup. No ads. No limits. Generate as many names as you want, free forever.

---

## Generators Available

### Names
| Generator | URL | Keywords Targeted |
|-----------|-----|-------------------|
| Villain Name Generator | /villain-name-generator.html | villain name generator (3,600/mo) |
| Elf Name Generator | /elf-name-generator.html | elf name generator (14,800/mo) |
| Dark Elf Name Generator | /dark-elf-name-generator.html | dark elf name generator (1,900/mo) |
| Wood Elf Name Generator | /wood-elf-name-generator.html | wood elf name generator (2,900/mo) |
| Blood Elf Name Generator | /blood-elf-name-generator.html | blood elf name generator (1,000/mo) |
| Orc Name Generator | /orc-name-generator.html | orc name generator (3,600/mo) |
| Half-Orc Name Generator | /half-orc-name-generator.html | half orc name generator (1,300/mo) |
| Skyrim Orc Name Generator | /skyrim-orc-name-generator.html | skyrim orc name generator (390/mo) |
| Dwarf Name Generator | /dwarf-name-generator.html | dwarf name generator (2,900/mo) |
| Tiefling Name Generator | /tiefling-name-generator.html | tiefling name generator (2,400/mo) |
| Goblin Name Generator | /goblin-name-generator.html | goblin name generator (1,900/mo) |
| Mage Name Generator | /mage-name-generator.html | mage name generator (2,400/mo) |
| Vampire Name Generator | /vampire-name-generator.html | vampire name generator (1,900/mo) |
| Alien Name Generator | /alien-name-generator.html | alien name generator (1,900/mo) |
| Villainess Name Generator | /villainess-name-generator.html | villainess name generator (720/mo) |

### Places
| Generator | URL | Keywords Targeted |
|-----------|-----|-------------------|
| Kingdom Name Generator | /kingdom-name-generator.html | kingdom name generator (5,400/mo) |
| Fantasy City Name Generator | /fantasy-city-name-generator.html | fantasy city name generator (2,900/mo) |
| Tavern Name Generator | /tavern-name-generator.html | tavern name generator (720/mo) |
| Inn Name Generator | /inn-name-generator.html | inn name generator (320/mo) |
| Dungeon Name Generator | /dungeon-name-generator.html | dungeon name generator (90/mo) |

### Creatures
| Generator | URL | Keywords Targeted |
|-----------|-----|-------------------|
| Creature Name Generator | /creature-name-generator.html | creature name generator (480/mo) |
| Mythical Creature Generator | /mythical-creature-generator.html | mythical creatures generator (320/mo) |

### Weapons & Items
| Generator | URL | Keywords Targeted |
|-----------|-----|-------------------|
| Weapon Name Generator | /weapon-name-generator.html | weapon name generator (390/mo) |
| Magic Item Generator | /magic-item-generator.html | magic item name generator (70/mo) |
| Artifact Name Generator | /artifact-name-generator.html | artifact name generator (70/mo) |

**Total target volume: ~60,000 monthly searches across all pages**

---

## Tech Stack

| Layer | Choice | Why |
|-------|--------|-----|
| Frontend | Plain HTML + CSS + Vanilla JS | Zero build step, instant deploy |
| Hosting | GitHub Pages | Free, fast CDN, custom domain |
| Fonts | Google Fonts (Cinzel + Cormorant + Inter) | Free, fantasy-appropriate |
| API (Phase 2) | Claude API via Cloudflare Worker | AI-powered paid tier |
| Analytics | Google Search Console + Plausible | SEO tracking |

---

## Project Structure

```
runeforge-online/
│
├── index.html                          ← Homepage — never edit manually
├── tools.js                            ← Add all new tools here ONLY
│
├── villain-name-generator.html         ← Live ✅
├── elf-name-generator.html             ← Live ✅
├── dark-elf-name-generator.html        ← In progress
├── orc-name-generator.html             ← In progress
├── kingdom-name-generator.html         ← In progress
├── tavern-name-generator.html          ← In progress
├── tiefling-name-generator.html        ← Planned
├── dwarf-name-generator.html           ← Planned
├── goblin-name-generator.html          ← Planned
├── [remaining pages...]                ← Planned
│
├── og-image.jpg                        ← Social share image
└── README.md                           ← This file
```

---

## How to Add a New Tool

The homepage auto-updates from `tools.js`. Never edit `index.html` manually.

**Step 1 — Build the HTML page**

Copy an existing page (e.g. `villain-name-generator.html`).
Change: h1 title, filter buttons, name arrays in JS, SEO content, FAQ.

**Step 2 — Add object to tools.js**

```js
{
  id: "orc-name-generator",
  name: "Orc Name Generator",
  desc: "Brutal, guttural names for orcs, half-orcs, and warriors.",
  category: "names",           // names / places / creatures / weapons
  tags: ["orc", "dnd", "skyrim"],
  icon: `<path d="M12 2..."/>`,
  url: "orc-name-generator.html",
  volume: 3600,
  kd: 18,
  featured: true               // true = large card on homepage
},
```

**Step 3 — Push to GitHub**

```bash
git add .
git commit -m "Add orc name generator"
git push
```

Homepage auto-updates. Done.

---

## SEO Strategy

Every page includes:
- ✅ FAQ schema (JSON-LD)
- ✅ HowTo schema (JSON-LD)
- ✅ Keyword-targeted H1, H2, H3
- ✅ 800–2,000 word SEO article below tool
- ✅ Internal linking via Related Tools chips
- ✅ Mobile responsive

Schema advantage: zero competitors have FAQ + HowTo + structured
data. RuneForge claims all unclaimed SERP features.

---

## Monetization Plan

| Phase | Timeline | Model | Target |
|-------|----------|-------|--------|
| Phase 1 | Months 1–6 | Free tools, organic traffic | 10K–30K visits/mo |
| Phase 2 | Month 3+ | Ezoic/Mediavine display ads | $200–500/mo |
| Phase 3 | Month 6+ | Freemium — Claude API paid tier ($5/mo) | $500–2,000/mo |
| Phase 4 | Month 12+ | Flip on Acquire.com at 35x MRR | $30K–100K exit |

---

## Build Schedule

| Week | Pages | Status |
|------|-------|--------|
| 1 | villain + elf | ✅ Live |
| 2 | orc + kingdom | 🔄 Building |
| 3 | tiefling + dwarf + goblin | 📋 Planned |
| 4 | tavern + alien + city + weapon | 📋 Planned |
| 5 | creature + magic item + dungeon | 📋 Planned |
| 6 | Schema audit + sitemap + GSC submit | 📋 Planned |
| 7–8 | Sub-variants (dark elf, wood elf, half-orc etc.) | 📋 Planned |

---

## License

All generated names are free to use in any project — commercial or personal.
Code is MIT licensed.

---

*Built and maintained by [@chrismarkstudio](https://instagram.com/chrismarkstudio)*
*Part of the AI-first solo operator playbook — Ukhrul, Manipur, India*
