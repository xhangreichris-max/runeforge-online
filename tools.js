// ============================================================
// RUNEFORGE — TOOLS CONFIG
// Add new tools here ONLY. Homepage auto-updates.
// ============================================================

const RUNEFORGE_TOOLS = [

  // ── NAMES ────────────────────────────────────────────────
  {
    id: "villain-name-generator",
    name: "Villain Name Generator",
    desc: "Dark, menacing names for antagonists, dark lords, and warlords.",
    category: "names",
    tags: ["dark fantasy", "rpg", "fiction"],
    icon: `<path d="M12 2l9 4.9V17L12 22l-9-4.9V6.9z"/>`,
    url: "villain-name-generator.html",
    volume: 3600,
    kd: 20,
    featured: true
  },
  {
    id: "elf-name-generator",
    name: "Elf Name Generator",
    desc: "Melodic, flowing names for elves across all fantasy worlds.",
    category: "names",
    tags: ["elf", "fantasy", "dnd"],
    icon: `<path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14H9V8h2v8zm4 0h-2V8h2v8z"/>`,
    url: "elf-name-generator.html",
    volume: 14800,
    kd: 28,
    featured: true
  },
  {
    id: "dark-elf-name-generator",
    name: "Dark Elf Name Generator",
    desc: "Harsh, sinister names for drow and shadow elves.",
    category: "names",
    tags: ["dark elf", "drow", "dnd"],
    icon: `<path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2z"/>`,
    url: "dark-elf-name-generator.html",
    volume: 1900,
    kd: 15,
    featured: false
  },
  {
    id: "orc-name-generator",
    name: "Orc Name Generator",
    desc: "Brutal, guttural names for orcs, half-orcs, and warriors.",
    category: "names",
    tags: ["orc", "half-orc", "dnd", "skyrim"],
    icon: `<path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2z"/>`,
    url: "orc-name-generator.html",
    volume: 3600,
    kd: 18,
    featured: true
  },
  {
    id: "tiefling-name-generator",
    name: "Tiefling Name Generator",
    desc: "Infernal names for tieflings in D&D 5e, BG3, and beyond.",
    category: "names",
    tags: ["tiefling", "dnd", "bg3"],
    icon: `<path d="M12 2L8 8H4l4 6H4l8 8 8-8h-4l4-6h-4L12 2z"/>`,
    url: "tiefling-name-generator.html",
    volume: 2400,
    kd: 23,
    featured: false
  },
  {
    id: "dwarf-name-generator",
    name: "Dwarf Name Generator",
    desc: "Strong, stout names for dwarves from D&D, LOTR, and Warhammer.",
    category: "names",
    tags: ["dwarf", "dnd", "lotr"],
    icon: `<path d="M12 12c2.7 0 4.8-2.1 4.8-4.8S14.7 2.4 12 2.4 7.2 4.5 7.2 7.2 9.3 12 12 12zm0 2.4c-3.2 0-9.6 1.6-9.6 4.8v2.4h19.2v-2.4c0-3.2-6.4-4.8-9.6-4.8z"/>`,
    url: "dwarf-name-generator.html",
    volume: 2900,
    kd: 17,
    featured: false
  },
  {
    id: "goblin-name-generator",
    name: "Goblin Name Generator",
    desc: "Wily, chaotic names for goblins in D&D, WoW, and tabletop RPGs.",
    category: "names",
    tags: ["goblin", "dnd", "wow"],
    icon: `<circle cx="12" cy="8" r="5"/><path d="M3 21v-2a7 7 0 0 1 14 0v2"/>`,
    url: "goblin-name-generator.html",
    volume: 1900,
    kd: 19,
    featured: false
  },
  {
    id: "dnd-name-generator",
    name: "D&D Name Generator",
    desc: "Authentic D&D names for every race — humans, elves, dwarves, tieflings, half-orcs, and halflings.",
    category: "names",
    tags: ["dnd", "d&d", "5e", "bg3"],
    icon: `<path d="M12 2l9 4.9V17L12 22l-9-4.9V6.9z"/>`,
    url: "dnd-name-generator.html",
    volume: 3600,
    kd: 35,
    featured: true
  },
  {
    id: "mage-name-generator",
    name: "Mage Name Generator",
    desc: "Arcane names for wizards, mages, and spellcasters.",
    category: "names",
    tags: ["mage", "wizard", "fantasy"],
    icon: `<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>`,
    url: "mage-name-generator.html",
    volume: 2400,
    kd: 26,
    featured: false
  },
  {
    id: "alien-name-generator",
    name: "Alien Name Generator",
    desc: "Otherworldly species and character names for sci-fi universes.",
    category: "names",
    tags: ["alien", "sci-fi", "species"],
    icon: `<circle cx="12" cy="12" r="10"/><path d="M12 8v4l3 3"/>`,
    url: "alien-name-generator.html",
    volume: 1900,
    kd: 12,
    featured: false
  },
  {
    id: "vampire-name-generator",
    name: "Vampire Name Generator",
    desc: "Elegant and haunting names for vampires and the undead.",
    category: "names",
    tags: ["vampire", "undead", "dark fantasy"],
    icon: `<path d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm0-2a8 8 0 1 0 0-16 8 8 0 0 0 0 16z"/>`,
    url: "vampire-name-generator.html",
    volume: 1900,
    kd: 12,
    featured: false
  },
  {
    id: "necromancer-name-generator",
    name: "Necromancer Name Generator",
    desc: "Dark death-magic names for liches, undead lords, and necromancers.",
    category: "names",
    tags: ["necromancer", "lich", "dark fantasy"],
    icon: `<path d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10z"/>`,
    url: "necromancer-name-generator.html",
    volume: 1600,
    kd: 14,
    featured: false
  },

  // ── PLACES ───────────────────────────────────────────────
  {
    id: "kingdom-name-generator",
    name: "Kingdom Name Generator",
    desc: "Regal, powerful names for kingdoms, empires, and realms.",
    category: "places",
    tags: ["kingdom", "realm", "fantasy"],
    icon: `<path d="M4 22h16M4 18v-8l8-4 8 4v8M12 10v12"/>`,
    url: "kingdom-name-generator.html",
    volume: 5400,
    kd: 24,
    featured: true
  },
  {
    id: "fantasy-city-name-generator",
    name: "City Name Generator",
    desc: "Evocative names for fantasy cities, towns, and settlements.",
    category: "places",
    tags: ["city", "town", "fantasy"],
    icon: `<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>`,
    url: "fantasy-city-name-generator.html",
    volume: 2900,
    kd: 22,
    featured: false
  },
  {
    id: "tavern-name-generator",
    name: "Tavern Name Generator",
    desc: "Memorable inn and tavern names for your D&D campaigns.",
    category: "places",
    tags: ["tavern", "inn", "dnd"],
    icon: `<path d="M17 8h1a4 4 0 1 1 0 8h-1"/><path d="M3 8h14v9a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4V8z"/>`,
    url: "tavern-name-generator.html",
    volume: 720,
    kd: 16,
    featured: true
  },
  {
    id: "dungeon-name-generator",
    name: "Dungeon Name Generator",
    desc: "Dark, foreboding names for dungeons and underground lairs.",
    category: "places",
    tags: ["dungeon", "dnd", "rpg"],
    icon: `<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M9 9h6M9 15h6"/>`,
    url: "dungeon-name-generator.html",
    volume: 90,
    kd: 12,
    featured: false
  },

  // ── CREATURES ────────────────────────────────────────────
  {
    id: "creature-name-generator",
    name: "Creature Name Generator",
    desc: "Fearsome names for monsters, beasts, and fantasy creatures.",
    category: "creatures",
    tags: ["creature", "monster", "beast"],
    icon: `<circle cx="9" cy="12" r="1"/><circle cx="15" cy="12" r="1"/><path d="M8 20v2h8v-2"/><path d="M16 20a2 2 0 0 0 1.56-3.25 8 8 0 1 0-11.12 0A2 2 0 0 0 8 20"/>`,
    url: "creature-name-generator.html",
    volume: 480,
    kd: 13,
    featured: true
  },
  {
    id: "mythical-creature-generator",
    name: "Mythical Creature Generator",
    desc: "Names for dragons, griffins, phoenixes, and legendary beasts.",
    category: "creatures",
    tags: ["mythical", "dragon", "beast"],
    icon: `<path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>`,
    url: "mythical-creature-generator.html",
    volume: 320,
    kd: 16,
    featured: false
  },

  // ── WEAPONS & ITEMS ──────────────────────────────────────
  {
    id: "weapon-name-generator",
    name: "Weapon Name Generator",
    desc: "Legendary names for swords, axes, bows, and magical weapons.",
    category: "weapons",
    tags: ["weapon", "sword", "magic item"],
    icon: `<line x1="12" y1="2" x2="12" y2="22"/><path d="M8 6l4-4 4 4M8 18l4 4 4-4"/>`,
    url: "weapon-name-generator.html",
    volume: 390,
    kd: 14,
    featured: true
  },
  {
    id: "magic-item-generator",
    name: "Magic Item Generator",
    desc: "Enchanted artifact names for D&D loot and fantasy inventories.",
    category: "weapons",
    tags: ["magic item", "artifact", "dnd"],
    icon: `<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>`,
    url: "magic-item-generator.html",
    volume: 70,
    kd: 2,
    featured: false
  },

  {
    id: "dark-lord-name-generator",
    name: "Dark Lord Name Generator",
    desc: "Evil overlord names for ancient tyrants, warlords, shadow lords, and cursed rulers in D&D and fantasy fiction.",
    category: "names",
    tags: ["dark lord", "villain", "dark fantasy"],
    icon: `<path d='M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10z'/>`,
    url: "dark-lord-name-generator.html",
    volume: 1400,
    kd: 11,
    featured: false
  },
  {
    id: "wood-elf-name-generator",
    name: "Wood Elf Name Generator",
    desc: "Forest elf names for rangers, druids, warriors, and elders in D&D 5e and fantasy fiction.",
    category: "names",
    tags: ["wood elf", "elf", "forest", "D&D"],
    icon: `<path d='M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10z'/>`,
    url: "wood-elf-name-generator.html",
    volume: 1800,
    kd: 13,
    featured: false
  },
  {
    id: "blood-elf-name-generator",
    name: "Blood Elf Name Generator",
    desc: "Lore-accurate sin'dorei names for WoW, D&D, and fantasy fiction — paladins, mages, rangers, and nobility.",
    category: "names",
    tags: ["blood elf", "elf", "WoW", "sin'dorei"],
    icon: `<path d='M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10z'/>`,
    url: "blood-elf-name-generator.html",
    volume: 2200,
    kd: 15,
    featured: false
  },
  {
    id: "half-orc-name-generator",
    name: "Half-Orc Name Generator",
    desc: "Half-orc names for warriors, tribal characters, city-raised nobles, and outlanders in D&D and fantasy fiction.",
    category: "names",
    tags: ["half-orc", "orc", "D&D"],
    icon: `<path d='M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10z'/>`,
    url: "half-orc-name-generator.html",
    volume: 1600,
    kd: 10,
    featured: false
  },
  {
    id: "bg3-name-generator",
    name: "BG3 Name Generator",
    desc: "Authentic Baldur's Gate 3 character names built on Larian's naming logic — for custom Tavs, Durges, and tabletop conversions.",
    category: "names",
    tags: ["bg3", "baldurs gate", "larian", "dnd"],
    icon: `<path d='M12 2l9 4.9V17L12 22l-9-4.9V6.9z'/>`,
    url: "bg3-name-generator.html",
    volume: 720,
    kd: 18,
    featured: false
  },
  {
    id: "yordle-name-generator",
    name: "Yordle Name Generator",
    desc: "Whimsical, bouncy, mechanical names for yordle-inspired characters — fan fiction, tabletop reskins, and original creations.",
    category: "names",
    tags: ["yordle", "league of legends", "whimsical"],
    icon: `<circle cx='12' cy='8' r='5'/><path d='M3 21v-2a7 7 0 0 1 14 0v2'/>`,
    url: "yordle-name-generator.html",
    volume: 70,
    kd: 5,
    featured: false
  },
  {
    id: "hexblood-name-generator",
    name: "Hexblood Name Generator",
    desc: "Eerie hag-touched names — distorted birth names and curse-given names rooted in coven transformation lore.",
    category: "names",
    tags: ["hexblood", "hag", "ravenloft", "dnd"],
    icon: `<path d='M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10z'/>`,
    url: "hexblood-name-generator.html",
    volume: 30,
    kd: 6,
    featured: false
  },
  {
    id: "wendigo-name-generator",
    name: "Wendigo Name Generator",
    desc: "Names for the wendigo horror-fiction archetype — antlered, forest-bound creatures from modern horror media.",
    category: "creatures",
    tags: ["wendigo", "horror", "monster"],
    icon: `<circle cx='9' cy='12' r='1'/><circle cx='15' cy='12' r='1'/><path d='M16 20a2 2 0 0 0 1.56-3.25 8 8 0 1 0-11.12 0A2 2 0 0 0 8 20'/>`,
    url: "wendigo-name-generator.html",
    volume: 50,
    kd: 7,
    featured: false
  },
  {
    id: "vesk-name-generator",
    name: "Vesk Name Generator",
    desc: "Militaristic vesk names for Starfinder — hard consonants, clan structure, and earned epithets from the Veskarium.",
    category: "names",
    tags: ["vesk", "starfinder", "sci-fi"],
    icon: `<circle cx='12' cy='12' r='10'/><path d='M12 8v4l3 3'/>`,
    url: "vesk-name-generator.html",
    volume: 30,
    kd: 8,
    featured: false
  },
  {
    id: "pathfinder-name-generator",
    name: "Pathfinder Name Generator",
    desc: "Authentic Golarion names by nation — Taldor, Varisia, Osirion — and race for Pathfinder 2e campaigns.",
    category: "names",
    tags: ["pathfinder", "golarion", "2e"],
    icon: `<path d='M12 2l9 4.9V17L12 22l-9-4.9V6.9z'/>`,
    url: "pathfinder-name-generator.html",
    volume: 390,
    kd: 15,
    featured: false
  },
  {
    id: "mythical-name-generator",
    name: "Mythical Name Generator",
    desc: "Names for mythical beings, places, and artifacts rooted in Greek, Norse, Celtic, and Egyptian tradition.",
    category: "names",
    tags: ["mythical", "mythology", "worldbuilding"],
    icon: `<path d='M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5'/>`,
    url: "mythical-name-generator.html",
    volume: 90,
    kd: 9,
    featured: false
  },
];

// ── CATEGORY CONFIG ──────────────────────────────────────
const RUNEFORGE_CATEGORIES = [
  {
    id: "names",
    label: "Name Generators",
    desc: "Names for characters, races, and creatures",
    icon: `<path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/>`
  },
  {
    id: "places",
    label: "Place Generators",
    desc: "Kingdoms, cities, taverns, and dungeons",
    icon: `<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>`
  },
  {
    id: "creatures",
    label: "Creature Generators",
    desc: "Monsters, beasts, and mythical animals",
    icon: `<circle cx="9" cy="12" r="1"/><circle cx="15" cy="12" r="1"/><path d="M8 20v2h8v-2"/><path d="M16 20a2 2 0 0 0 1.56-3.25 8 8 0 1 0-11.12 0A2 2 0 0 0 8 20"/>`
  },
  {
    id: "weapons",
    label: "Weapon & Item Generators",
    desc: "Legendary weapons and enchanted artifacts",
    icon: `<line x1="12" y1="2" x2="12" y2="22"/><path d="M8 6l4-4 4 4M8 18l4 4 4-4"/>`
  }
];
