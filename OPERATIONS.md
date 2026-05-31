# Moving Light Database — Operations Guide

How to add and maintain fixtures in the database. Built for growth to 500+ fixtures.

---

## The two files

| File | What it is | Who edits it |
|---|---|---|
| `fixtures.json` | The data — every fixture record | Edited every time fixtures are added |
| `App.jsx` (dashboard) | The app — layout, search, filters | **Never edited when adding fixtures** |

**The golden rule:** adding fixtures means editing **`fixtures.json` only**. Never touch the dashboard
code to add data. This is what keeps the dashboard from breaking as the database grows.

---

## The fixture schema

Every fixture in `fixtures.json` is one object with these fields. Fill what you can find;
leave the rest as the empty value shown. **Never invent a value.**

### Identity & classification
| Field | Type | Notes |
|---|---|---|
| `id` | number | Unique. Next number after the current highest. |
| `brand` | string | Manufacturer, official spelling (e.g. `"Robe"`, `"Ayrton"`). |
| `model` | string | Official model name, exact spelling (see Name Accuracy below). |
| `category` | string | One of: `"Spot / Profile"`, `"Wash"`, `"Bar / Batten"`. |
| `variant` | string | `"Performance"`, `"Profile"`, or `""`. See Performance/Profile rule. |
| `applications` | array | Any of: `"Touring"`, `"Theater"`, `"TV-Film"`, `"Install"`, `"Corporate"`. |
| `tier` | string | `"Small"` (<10k lm), `"Medium"` (10-30k), `"Large"` (>=30k). Set from output. |
| `everUsed` | boolean | Personal "have used this" flag. Default `false`. |

### Light source
| Field | Type | Notes |
|---|---|---|
| `lampType` | string | `"LED"`, `"Discharge"`, `"Laser"`, or `"Other"`. |
| `watts` | number | Lamp/engine wattage. `null` if unknown. |
| `cct` | string | Fixed color temp, e.g. `"6500K"`. `""` if variable/unknown. |
| `cctRange` | string | Variable CCT range, e.g. `"2700-6500K"`. `""` if none. |

### Performance
| Field | Type | Notes |
|---|---|---|
| `outputLumens` | number | Fixture output in lumens (NOT light-engine output). `null` if unknown. |
| `cri` | number | Numeric CRI for filtering, e.g. `90`. `null` if unknown. |
| `criRaw` | string | CRI as printed, e.g. `">70 (90 w/ filter)"`. |

### Optics
| Field | Type | Notes |
|---|---|---|
| `zoomMin` | number | Tightest zoom angle in degrees. `null` if unknown. |
| `zoomMax` | number | Widest zoom angle in degrees. `null` if unknown. |
| `zoomRatio` | string | e.g. `"1:8"`. `""` if unknown. |
| `zoomRaw` | string | Zoom as printed, e.g. `"7° - 56°"`. |

### Color & effects
| Field | Type | Notes |
|---|---|---|
| `colorMixing` | string | e.g. `"CMY / CTO"`, `"RGBW"`. |
| `framing` | boolean | **Has framing shutters.** Decision-critical — get this right. |
| `gobo` | string | Gobo wheel summary, e.g. `"7 rotating + 8 static"`. |
| `animationWheel` | boolean | Has an animation wheel. |
| `prism` | boolean | Has a prism. |
| `iris` | boolean | Has an iris. |
| `frost` | boolean | Has a frost filter. |
| `effectsRaw` | string | Free-text effects detail (prism type, frost count, etc.). |

### Movement / physical / control
| Field | Type | Notes |
|---|---|---|
| `panTilt` | string | e.g. `"Pan: 540° / Tilt: 268°"`. |
| `weightKg` | number | Weight in kilograms. `null` if unknown. |
| `ipRating` | string | e.g. `"IP20"`, `"IP65"`. `""` if unknown. |
| `powerConsumption` | number | Max power draw in watts. `null` if unknown. |
| `dmxChannels` | string | DMX channel count(s), e.g. `"32 / 40"`. |
| `protocols` | string | e.g. `"DMX, RDM, Art-Net, sACN"`. |

### Source tracking
| Field | Type | Notes |
|---|---|---|
| `link` | string | Manufacturer product page URL. `""` if genuinely not found. |
| `description` | string | 1-2 sentence blurb, paraphrased from the source (not copied). |
| `lastVerified` | string | Date specs were checked, `"YYYY-MM-DD"`. |

---

## Adding a fixture — step by step

1. **Confirm the fixture should be added.** Someone decides "add the Robe iFORTE." The
   database does not discover fixtures on its own.

2. **Search for it.** Query format: `{brand} {model} specifications`. Example:
   `Robe iFORTE specifications weight DMX`.

3. **Pick the source** (see Source Priority below). Open the best one.

4. **Extract every schema field you can.** Use empty values (`null` / `""` / `false`) for
   anything the source doesn't state. Do not guess.

5. **Write the `description`** — 1-2 sentences, in your own words, summarising what the
   fixture is and its standout feature. Do not copy the manufacturer's text verbatim.

6. **Set `link`** to the manufacturer product page. If only a reseller page exists, leave
   `link` as `""` rather than linking a reseller.

7. **Set `lastVerified`** to today's date.

8. **Set `id`** to the next unused number.

9. **Append the object to `fixtures.json`.** Do not edit existing records unless correcting them.

10. **Deploy** (see Deploying below).

---

## Source priority

Use the highest-priority source available. Record which type was used (it informs trust).

1. **Manufacturer product page** — always preferred for accuracy and for the `link` field.
   Key manufacturer URLs by brand:
   - Martin: `martin.com/en-US/products/`
   - Robe: `robe.cz/products/`
   - Ayrton: `ayrton.eu/products/`
   - Elation: `elationlighting.com/products/`
   - Claypaky: `claypaky.it/en/products/`
   - GLP: `glp.de/en/products/`
   - Chauvet: `chauvetprofessional.com/products/`
   - Vari-Lite: `vari-lite.com/en-US/products/`
   - High End Systems: `highend.com/products/`
   - PRG (own fixtures): `prg.com` or `prggear.com`

2. **Manufacturer spec sheet / PDF** — often linked from the product page. Preferred over
   rental-house pages for technical accuracy.

3. **Trusted rental-house inventory** — use these three specifically. They carry clean,
   complete spec tables (weight, dimensions, DMX, power) and are reliable secondary sources:
   - **4Wall**: `4wall.com/rentals/lighting-equipment/moving-lights/` — organized by brand,
     individual product pages have weight, size, DMX. Two pages of moving lights inventory.
   - **PRG Gear**: `prggear.com/product-category/lighting-rental/` — curated touring inventory,
     individual pages have size and weight tables. Primary source for PRG's own fixtures
     (Best Boy, Icon Edge, Bad Boy) which are not available elsewhere.
   - **Christie Lites**: `christielites.com/profile/228w2w10w159w` (Profile),
     `christielites.com/wash/228w2w10w161w` (Wash),
     `christielites.com/beam/228w2w10w167w` (Beam),
     `christielites.com/hybrid/228w2w10w160w` (Hybrid).
     Good for confirming fixtures are actively used in professional rental.

4. **Open Fixture Library** (`open-fixture-library.org`) — reliable for DMX channel counts,
   dimensions, weight, and RDM data.

5. **Lighting & Sound America** (`lightingandsoundamerica.com`) — **use for `description`
   flavour and news only.** Good for finding which fixtures shipped on which tours and for
   catching announcements between manufacturer site updates. **Never** use as a source for
   numeric specs (wattage, lumens, zoom, weight, CRI, etc.) — always confirm those against
   the manufacturer. **Never** use as the `link` value.

6. **Distributor/reseller pages** — e.g. Full Compass, Solotech. Use only as a last resort,
   and **never** as the `link` value.

If sources disagree, prefer the manufacturer. If the manufacturer is silent on a field,
a rental-house number is acceptable.

## New fixture discovery

When growing the database, check these rental-house inventories for fixtures not yet in
`fixtures.json`. If a fixture appears in multiple rental inventories, it is actively used
in the industry and belongs in the database.

Sweep order for discovery:
1. `4wall.com/rentals/lighting-equipment/moving-lights/` (pages 1 and 2)
2. `prggear.com/product-category/lighting-rental/?fwp_categories=profile-and-spot-lights`
3. Christie Lites Profile, Wash, Beam, Hybrid pages (URLs above)
4. `mainlight.com/rentals?category=moving-lights` — inventory is JavaScript-rendered so
   browse manually or search `site:mainlight.com rentals moving lights` to surface fixtures.
   Good source for newer Robe, Ayrton, and ETC fixtures they tend to stock early.

Compare found fixtures against `fixtures.json` before adding — avoid duplicates.

**Workflow for rental-site discovery:** the rental listing confirms the fixture is actively
used in the industry. Always go to the manufacturer page for full specs — weight, DMX,
power, zoom, CRI. The rental site is the discovery trigger; the manufacturer page is the
data source.

---

## Critical rules

### Name accuracy
Use the **official** model name, exact spelling. Manufacturers' real names often differ
from how fixtures get written informally. Examples found while building this database:
- "Viper Air Fix" → official name is **MAC Viper AirFX**
- "Viper XIP" → official name is **MAC Viper XIP**

A wrong name makes a fixture hard to find in search. Check the manufacturer page header.

### Performance / Profile = framing shutters
Industry convention: a **Performance** variant has framing shutters; a **Profile** variant
does not. **There are exceptions** — always confirm `framing` from the actual spec sheet
rather than assuming from the name. Set `variant` and `framing` independently.

### Flag discrepancies — never silently overwrite
If a source contradicts a value already in the database, **do not just overwrite it.**
Note the discrepancy for review. Example found while building: the cheat sheet listed the
MAC ERA 800's CRI as `>79`; Martin's official spec says `>70`. The official value was used
*and the change was flagged.*

### Never invent data
An empty field (`null` / `""`) is correct and fine. A guessed value is data corruption.
If a spec can't be found, leave it empty.

### Engine output vs fixture output
Manufacturers quote two lumen figures: light-engine output (higher) and fixture output
(real, lower). Always record **fixture output** in `outputLumens`.

---

## Deploying

Once `fixtures.json` is updated:

1. Commit the change to the GitHub repo.
2. Vercel auto-deploys within ~1 minute.
3. The live dashboard — and everyone's installed PWA — picks up the new data on next open.

No app code changes. No version numbers. New fixture in `fixtures.json` = new fixture in
the dashboard.

---

## Periodic maintenance

- **Re-verify links** every few months — manufacturers restructure their websites and URLs
  go dead. Update `link` and `lastVerified` when re-checked.
- **Spec corrections** — when a discrepancy is confirmed, update the value and bump
  `lastVerified`.

---

## Current status

- **129 fixtures** in the database (114 original + 15 Martin fully researched).
- **All 23 Martin fixtures** fully researched to the full schema with verified links,
  weights, IP ratings, power consumption, DMX channels, protocols, and descriptions.
  Martin is the reference brand — use any Martin record as an example of a complete entry.
- **48 fixtures queued for addition** — identified from 4Wall, PRG, and Christie Lites
  inventories. Brands: Acme (5), ADJ (1), Ayrton (4), Chauvet (9), Claypaky (5),
  Elation (8), ETC (1), GLP (2), High End Systems (3), Martin (5), PRG (2), Robe (5),
  Vari-Lite (3). New brands: Acme, ADJ, ETC.
- **Remaining brands** (Robe, Elation, Ayrton, GLP, Vari-Lite, Chauvet, High End, Claypaky,
  PRG) still need the full research pass for their existing fixtures.

## Trusted rental source URLs (for reference)

| Source | Moving Lights URL |
|---|---|
| 4Wall | `4wall.com/rentals/lighting-equipment/moving-lights` |
| PRG Gear | `prggear.com/product-category/lighting-rental/` |
| Christie Lites (Profile) | `christielites.com/profile/228w2w10w159w` |
| Christie Lites (Wash) | `christielites.com/wash/228w2w10w161w` |
| Christie Lites (Beam) | `christielites.com/beam/228w2w10w167w` |
| Christie Lites (Hybrid) | `christielites.com/hybrid/228w2w10w160w` |
| Main Light | `mainlight.com/rentals?category=moving-lights` (browse manually) |
