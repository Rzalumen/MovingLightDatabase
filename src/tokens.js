// tokens.js — Design system tokens for Moving Light Database
// All colors, fonts, and design constants live here.
// Never hardcode hex values in components. Import from this file.

// ── FONT FAMILIES ─────────────────────────────────────────
export const FONTS = {
  // Used for: fixture names, headings, logo wordmark
  display: "'Geist', 'Inter', -apple-system, system-ui, sans-serif",

  // Used for: all UI body text, buttons, labels, descriptions
  ui: "'Inter', -apple-system, system-ui, sans-serif",

  // Used for: numeric spec values, technical labels, code-like data
  mono: "'JetBrains Mono', 'IBM Plex Mono', monospace",
};

// ── CORE SURFACE & TEXT ───────────────────────────────────
export const COLORS = {
  // Backgrounds (darkest → lightest)
  bgBase:        "#0E0E11",  // Main page background
  bgElevated:    "#0F0F12",  // Cards, inputs, filter chip backgrounds
  bgRow:         "#0C0C0E",  // Result table background
  bgHover:       "#131316",  // Row hover state
  bgCardSurface: "#1F1F28",  // Expanded card outer surface — lifted above page bg

  // Borders
  borderSubtle:   "#18181C",  // Default border on cards, tables
  borderDefault:  "#222228",  // Default border on chips, inputs
  borderHover:    "#333339",  // Hover border state
  borderDivider:  "#131316",  // Internal dividers (between rows)

  // Text
  textPrimary:   "#EDEDEF",  // Default text, fixture names, primary content
  textSecondary: "#C8C8D2",  // Secondary text, brand caps, descriptions
  textMuted:     "#8A8A98",  // Muted labels, ghost text
  textDim:       "#7A7A88",  // Very muted (slightly lighter than original #6E6E7C)
  textGhost:     "#6E6E7C",  // Most-muted text, dash placeholders
  textPlaceholder: "#7E7E8C",// Input placeholder text

  // ── ACTION / STATE (amber — RESERVED) ───────────────────
  // Amber is reserved for USER ACTIONS only:
  // - Watching button (active state)
  // - Compare button (active state on desktop row)
  // - Filter "active" badges
  // Do NOT use amber for category coloring or content classification.
  actionAmber:        "#E8B339",
  actionAmberBg:      "rgba(232, 179, 57, 0.1)",
  actionAmberMuted:   "rgba(232, 179, 57, 0.55)",

  // ── BRAND IDENTITY (periwinkle — RESERVED) ──────────────
  // Periwinkle is reserved for brand names everywhere they appear:
  // collapsed row, expanded card, compare modal. Distinct from
  // amber (action) and cyan (standout).
  brandPeriwinkle: "#A8B8D8",

  // ── STANDOUT / BRAND-SELECTED (cyan — RESERVED) ─────────
  // Cyan is reserved for:
  // - Standout indicator dot on fixture rows
  // - Selected brand pills/items in filters
  standoutCyan:       "#7DD3FC",
  standoutCyanBg:     "rgba(125, 211, 252, 0.1)",
  standoutCyanBorder: "rgba(125, 211, 252, 0.2)",
  standoutCyanMuted:  "#8FA9B5",  // For muted text version of standout (e.g., row label)
  standoutCyanText:   "#B4D8E8",  // For text inside the expanded card standout pill

  // ── APPLICATION (neutral — differentiated by icon) ──────
  // Active Application chips use neutral white/gray, not unique colors.
  // The Tabler icon does the differentiation.
  appActiveBorder: "#C8C8D2",
  appActiveBg:     "rgba(200, 200, 210, 0.06)",
  appActiveText:   "#EDEDEF",

  // ── TYPE (4 distinct, non-paired colors) ────────────────
  typePerformance: "#FF6B3D",  // Coral-red — framing fixtures
  typeSpot:        "#F2D466",  // Pale yellow — non-framing spot/beam
  typeWash:        "#4ECDC4",  // Teal — wash fixtures
  typeBar:         "#C77DFF",  // Purple — bar / batten

  // ── OUTPUT TIER (sequential green→coral) ────────────────
  outputSmall:  "#6EE7A8",  // Green — small venues / clubs
  outputMedium: "#B4E075",  // Yellow-green — mid-size / theatre
  outputLarge:  "#F08A60",  // Coral — arena / stadium

  // ── FEATURES / SEMANTIC ─────────────────────────────────
  successGreen: "#6EE7A8",  // CRI 90+, framing yes indicator
  warningAmber: "#E8B339",  // CRI 80-89 indicator (same as actionAmber)

  // ── SPEC LABEL COLOR ────────────────────────────────────
  // Used in expanded card for "MAX OUTPUT", "FRAMING SHUTTERS", etc. labels
  specLabelAmber: "#C0A674",

  // ── BRAND LOGO SLOT BACKGROUND ─────────────────────────
  // Subtle dark surface for brand logo squares in the brand pill row
  brandLogoBg: "#1C1C22",

  // ── ACTIVE FILTER BAR (sticky) ─────────────────────────
  activeBarBg:     "#0E0E11",
  activeBarBorder: "#1F1F25",
};

// ── PALETTE GETTERS (for chip active states) ──────────────
// Returns the matching color + background for a category value.
export const getTypeColor = (type) => {
  switch (type) {
    case "Performance":     return COLORS.typePerformance;
    case "Spot":            return COLORS.typeSpot;
    case "Wash":            return COLORS.typeWash;
    case "Bar / Batten":    return COLORS.typeBar;
    default:                return COLORS.textSecondary;
  }
};

export const getTierColor = (tier) => {
  switch (tier) {
    case "Small":   return COLORS.outputSmall;
    case "Medium":  return COLORS.outputMedium;
    case "Large":   return COLORS.outputLarge;
    default:        return COLORS.textSecondary;
  }
};

// ── DESIGN CONSTANTS ──────────────────────────────────────
export const RADIUS = {
  sm: 6,    // Small chips, pills
  md: 8,    // Standard chips, spec boxes
  lg: 11,   // Inputs, large buttons
  xl: 12,   // Cards, expanded panels
};

export const SPACING = {
  xs: 4,
  sm: 6,
  md: 8,
  lg: 12,
  xl: 16,
  xxl: 22,
};
