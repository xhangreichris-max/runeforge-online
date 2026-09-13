// ============================================================
// RUNEFORGE — TOOLS-DE CONFIG
// German tools config. Add new German pages here ONLY.
// de/index.html auto-updates from this file.
// ============================================================

const RUNEFORGE_TOOLS = [
];

// ── CATEGORY CONFIG ──────────────────────────────────────
// icon values are raw SVG <path>/<circle> markup (same shapes as the
// equivalent English categories in tools.js), not emoji — de/index.html
// wraps this string directly inside an <svg>...</svg> via iconSVG(),
// which does not render bare emoji/text nodes.
const RUNEFORGE_CATEGORIES = [
  {id: "namen", label: "Namensgeneratoren",
   desc: "Namen für Charaktere, Rassen und Kreaturen",
   icon: `<path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/>`},
  {id: "orte", label: "Ortsgeneratoren",
   desc: "Königreiche, Städte, Tavernen und Dungeons",
   icon: `<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>`},
  {id: "kreaturen", label: "Kreaturgeneratoren",
   desc: "Monster, Bestien und mythische Wesen",
   icon: `<circle cx="9" cy="12" r="1"/><circle cx="15" cy="12" r="1"/><path d="M8 20v2h8v-2"/><path d="M16 20a2 2 0 0 0 1.56-3.25 8 8 0 1 0-11.12 0A2 2 0 0 0 8 20"/>`},
];
