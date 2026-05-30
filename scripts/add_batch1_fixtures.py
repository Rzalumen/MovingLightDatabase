#!/usr/bin/env python3
"""
Batch 1 fixture additions per FIXTURE_GAP_SCAN_HANDOFF.md
Adds Martin, Robe, Elation, Ayrton gap fixtures.
Run from repo root: python3 scripts/add_batch1_fixtures.py
"""
import json, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(REPO, 'src', 'fixtures.json')
TODAY = '2026-05-30'

with open(PATH) as f:
    data = json.load(f)

existing_ids = {x['id'] for x in data}
existing_keys = {(x['brand'].lower(), x['model'].lower()) for x in data}
next_id = max(existing_ids) + 1

def f(**kw):
    """Build a fixture record with schema defaults; required overrides via kwargs."""
    base = {
        "id": None,
        "brand": "",
        "model": "",
        "category": "",       # Performance / Spot / Wash / Bar / Bar / Batten
        "variant": "",
        "applications": [],
        "tier": "",
        "everUsed": False,
        "lampType": "",
        "watts": None,
        "cct": "",
        "cctRange": "",
        "outputLumens": None,
        "cri": None,
        "criRaw": "",
        "zoomMin": None,
        "zoomMax": None,
        "zoomRatio": "",
        "zoomRaw": "",
        "colorMixing": "",
        "framing": False,
        "gobo": "",
        "animationWheel": False,
        "prism": False,
        "iris": False,
        "frost": False,
        "effectsRaw": "",
        "pan": None,
        "tilt": None,
        "weightKg": None,
        "ipRating": "",
        "powerConsumption": None,
        "dmxChannels": "",
        "protocols": "",
        "standout": None,
        "lamp": "",
        "panTilt": "",
        "link": "",
        "description": "",
        "lastVerified": TODAY,
        "dualFrost": False,
        "ipRated": False,
        "imageUrl": "",
    }
    base.update(kw)
    return base

new = []

# ---------------- MARTIN (9) ----------------
new.append(f(
    brand="Martin", model="MAC Encore Two",
    category="Performance", variant="Performance",
    applications=["Theater","Concert","Broadcast","Corporate"],
    tier="Large", lampType="LED", watts=760,
    cct="5600K", cctRange="",
    outputLumens=21000, cri=90, criRaw="90 native (95 w/ Spectrum Enhancement Filter), TM-30/TLCI 90",
    zoomMin=5, zoomMax=54, zoomRatio="1:10", zoomRaw="5° - 54°",
    colorMixing="Enhanced CMY",
    framing=True,
    gobo="7 rotating + 11 static",
    prism=True, iris=True, frost=True,
    effectsRaw="Dual frost system across full zoom; 150 mm front lens; selectable output / noise modes",
    weightKg=36, ipRating="IP20",
    dmxChannels="", protocols="DMX, RDM, Art-Net, sACN, Martin P3",
    standout="6× the intensity of MAC Encore at narrow beam\nStudio-quiet selectable noise modes",
    lamp="760 LED", panTilt="",
    link="https://www.martin.com/en-US/products/mac-encore-two",
    description="760 W LED profile that succeeds the MAC Encore with a 75% output boost (21,000 lm) and 1:10 zoom. Enhanced CMY, dual gobo wheels, dual frost and Spectrum Enhancement Filter make it a long-throw, broadcast-quiet performance head.",
    dualFrost=True, ipRated=False,
    imageUrl="https://adn.harmanpro.com/product_attachments/product_attachments/9120_1728927641/Martin_ERA800Performance_2_original_large.jpg",
))

new.append(f(
    brand="Martin", model="MAC Allure Profile",
    category="Performance", variant="Profile",
    applications=["Concert","TV-Film","Corporate","Install"],
    tier="Small", lampType="LED", watts=420,
    cct="6500K", cctRange="",
    outputLumens=6500, cri=80, criRaw=">80, CQS 88",
    zoomMin=12, zoomMax=36, zoomRatio="1:3", zoomRaw="12° - 36°",
    colorMixing="RGBW (additive)",
    framing=False,
    gobo="",
    effectsRaw="7-segment pixelated beam with per-pixel RGBW control; first Martin fixture with P3",
    ipRating="IP20",
    protocols="DMX, RDM, Art-Net, sACN, Martin P3",
    standout="7-segment pixel-controllable beam — P3 mappable",
    lamp="7 × 60W RGBW",
    link="https://www.martin.com/en-US/products/mac-allure-profile",
    description="Compact RGBW LED profile built around a 7-segment pixel beam. Each pixel is individually addressable via DMX, Art-Net or Martin P3, enabling pixel-mapped effects directly inside the beam.",
    imageUrl="",
))

new.append(f(
    brand="Martin", model="MAC Allure Wash PC",
    category="Wash", variant="",
    applications=["Theater","Concert","TV-Film","Corporate"],
    tier="Small", lampType="LED", watts=420,
    cct="6500K", cctRange="2000-8000K",
    outputLumens=6000, cri=80, criRaw=">80, CQS 88, TM-30 Rf 82 / Rg 109, TLCI 82",
    zoomMin=12, zoomMax=36, zoomRatio="1:3", zoomRaw="12° - 36°",
    colorMixing="RGBW (additive)",
    framing=False,
    effectsRaw="7-segment pixelated beam, P3 control",
    weightKg=17.6, ipRating="IP20",
    protocols="DMX, RDM, Art-Net, sACN, Martin P3",
    standout="7-segment PC wash, 2000–8000K range, 17.6 kg",
    lamp="7 × 60W RGBW",
    link="https://www.martin.com/en-US/products/mac-allure-wash-pc",
    description="PC-lens wash variant of the Allure family with the same 7-segment RGBW pixel engine. 2000–8000K virtual CCT, P3-capable, and light enough at 17.6 kg to fly three to a case.",
    imageUrl="",
))

new.append(f(
    brand="Martin", model="ERA 500 Hybrid IP",
    category="Spot", variant="",
    applications=["Touring","Install","Corporate"],
    tier="Large", lampType="Discharge", watts=370,
    cct="6500K", cctRange="",
    outputLumens=22000, cri=70, criRaw=">70",
    zoomMin=2, zoomMax=40, zoomRatio="1:20", zoomRaw="2° - 40°",
    colorMixing="CMY",
    framing=False,
    prism=True, frost=True,
    effectsRaw="Overlaying prism effects; beam/spot/wash hybrid in one body",
    ipRating="IP65",
    powerConsumption=564,
    protocols="DMX, RDM",
    standout="IP65 outdoor hybrid — 1:20 zoom\nC3-M / IK07 rated",
    lamp="370 W discharge (6000 h life)",
    link="https://www.martin.com/en/products/era-500-hybrid-ip",
    description="IP65 hybrid moving head packing 22,000 lm from a 370 W short-arc lamp into a beam/spot/wash combo. 1:20 zoom and a C3-M corrosion rating make it suited to permanent outdoor installs and rough touring.",
    ipRated=True,
    imageUrl="",
))

new.append(f(
    brand="Martin", model="ERA 600 Profile",
    category="Performance", variant="Profile",
    applications=["Theater","Concert","Corporate","Install"],
    tier="Medium", lampType="LED", watts=550,
    cct="6500K", cctRange="2700-6500K",
    outputLumens=19000, cri=None, criRaw="",
    zoomMin=6, zoomMax=45, zoomRatio="1:8", zoomRaw="6° - 45°",
    colorMixing="CMY / CTO",
    framing=False,
    gobo="2 rotating (7 + open each) + 1 static (8 + open)",
    prism=True, iris=True,
    effectsRaw="Dual rotating gobo wheels with indexing/rotation/shake; rotating prisms; iris",
    ipRating="IP20",
    protocols="DMX, RDM",
    standout="Dual rotating gobo wheels with full MAC-range gobo set",
    lamp="550 LED",
    link="https://www.martin.com/en-US/products/era-600-profile",
    description="550 W LED profile head with 19,000 lm, 1:8 zoom, full CMY/CTO and dual rotating gobo wheels. Slots in below the framing ERA 600 Performance for productions needing breakup and gobo focus without shutters.",
    imageUrl="",
))

new.append(f(
    brand="Martin", model="ERA 700 Performance IP",
    category="Performance", variant="Performance",
    applications=["Install","Touring"],
    tier="Large", lampType="LED", watts=680,
    cct="6500K", cctRange="",
    outputLumens=26000, cri=None, criRaw="",
    zoomMin=5.4, zoomMax=44, zoomRatio="1:8", zoomRaw="5.4° - 44°",
    colorMixing="CMY + CTO",
    framing=True,
    gobo="Dual gobo wheels",
    animationWheel=True, prism=True, frost=True,
    effectsRaw="Full curtain framing, dual prisms, dual frost, animation wheel; anti-tamper data box",
    weightKg=40, ipRating="IP66",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="IP66 framing performance head built for permanent outdoor install\nActive humidity & heating control, C5M marine rating",
    lamp="680 LED",
    link="https://www.martin.com/en-US/products/era-700-performance-ip",
    description="680 W IP66 framing head designed for permanent outdoor entertainment installs. 26,000 lm, -20°C to +40°C operating range, C5M marine corrosion rating, and active humidity/heat control inside the optics box.",
    dualFrost=True, ipRated=True,
    imageUrl="",
))

new.append(f(
    brand="Martin", model="MAC III Profile",
    category="Performance", variant="Profile",
    applications=["Theater","Touring"],
    tier="Large", lampType="Discharge", watts=1500,
    cct="6000K", cctRange="",
    outputLumens=None, cri=85, criRaw=">85",
    zoomMin=None, zoomMax=None, zoomRatio="", zoomRaw="",
    colorMixing="CMY + CTO",
    framing=True,
    effectsRaw="Continuous-rotation framing system with full blade crossover and uniform per-blade focus",
    ipRating="IP20",
    protocols="DMX, RDM",
    standout="Continuous-rotation framing module\n(discontinued)",
    lamp="1500 W discharge (Osram HTI 1500W/60/P50 Lok-it)",
    link="https://www.martin.com/en-US/products/mac-iii-profile",
    description="Legacy 1500 W discharge profile from Martin's flagship MAC III platform. Best known for its continuous-rotation framing system with full blade crossover — a feature still rare in modern heads.",
    imageUrl="",
))

new.append(f(
    brand="Martin", model="MAC III Performance",
    category="Performance", variant="Performance",
    applications=["Theater","Touring"],
    tier="Large", lampType="Discharge", watts=1500,
    cct="6000K", cctRange="",
    outputLumens=None, cri=85, criRaw=">85",
    zoomMin=None, zoomMax=None, zoomRatio="", zoomRaw="",
    colorMixing="CMY + CTO",
    framing=True,
    effectsRaw="Interleaved 4-blade framing with full crossover & continuous rotation; 16-bit control of dim/gobo/frame/focus/zoom/pan/tilt",
    ipRating="IP20",
    dmxChannels="33 / 40",
    protocols="DMX, RDM",
    standout="Industry-first continuous-rotation interleaved framing\n(discontinued)",
    lamp="1500 W discharge (Osram HTI 1500W/60/P50 Lok-it)",
    link="https://www.martin.com/en-US/products/mac-iii-performance",
    description="Theatre-oriented sibling to the MAC III Profile with the same 1500 W discharge engine and continuous-rotation framing. Four independently controllable blades cross the entire beam, enabling unconventional shutter choreography.",
    imageUrl="",
))

new.append(f(
    brand="Martin", model="MAC III AirFX",
    category="Performance", variant="",
    applications=["Touring","TV-Film"],
    tier="Large", lampType="Discharge", watts=1500,
    cct="6000K", cctRange="3200-6000K",
    outputLumens=None, cri=90, criRaw=">90",
    zoomMin=None, zoomMax=None, zoomRatio="", zoomRaw="",
    colorMixing="CMY + CTO",
    framing=False,
    prism=False, iris=True,
    effectsRaw="Rotating aerial-effects wheel (4 interchangeable elements); 7-position color wheel; variable iris with pulse",
    weightKg=54.9, ipRating="IP20",
    protocols="DMX, RDM",
    standout="Aerial-effects wheel — tight beam to wash with no jump\n(discontinued)",
    lamp="1500 W discharge (Osram HTI 1500W/60/P50 Lok-it)",
    link="https://www.martin.com/en-US/products/mac-iii-airfx",
    description="Profile/wash hybrid in the MAC III line: a 1500 W discharge head whose linear zoom transitions from hard-edge beam to wide wash with no beam jump, plus a rotating aerial-effects wheel for mid-air looks.",
    imageUrl="",
))

# ---------------- ROBE ----------------

# Tier A: New product lines
new.append(f(
    brand="Robe", model="LedPOINTE®",
    category="Spot", variant="",
    applications=["Touring","Theater","Corporate","Install"],
    tier="Medium", lampType="LED", watts=280,
    cct="", cctRange="2700-8000K",
    outputLumens=None, cri=None, criRaw="",
    zoomMin=1.8, zoomMax=44, zoomRatio="1:24", zoomRaw="1.8° - 44°",
    colorMixing="CMY",
    framing=False,
    gobo="9 rotating + 11 static",
    prism=True, iris=False, frost=False,
    effectsRaw="Patented MLP stackable multi-level prism (6-facet linear + 18-facet radial, bi-directional); SpektraBeam splintered-beam prism wheel; 13-position colour wheel; DataSwatch presets",
    weightKg=21, ipRating="IP20",
    dmxChannels="", protocols="DMX, RDM, Art-Net, sACN",
    standout="4th-gen Pointe with white LED Transferable Engine\nSpektraBeam splintered-beam effect",
    lamp="280W White LED TE™ XP",
    link="https://www.robe.cz/ledpointe",
    description="280 W LED reimagining of the Pointe with Robe's TE Transferable Engine, full CMY, and a stacked MLP prism plus SpektraBeam wheel. 1.8°–44° zoom and 155 mm lens hit 160,000 lx at 5 m in a 21 kg body.",
    imageUrl="",
))

new.append(f(
    brand="Robe", model="WTF!™",
    category="Performance", variant="",
    applications=["Touring","Concert","TV-Film"],
    tier="Large", lampType="LED", watts=None,
    cct="", cctRange="2700-10000K",
    outputLumens=None, cri=None, criRaw="",
    zoomMin=13, zoomMax=125, zoomRatio="", zoomRaw="13° – 95° (RGBW) / 14° – 97° (strobe centre)",
    colorMixing="RGBW",
    framing=False,
    effectsRaw="72×20W white linear strobe LEDs + 16×60W RGBW + 1000W warm-white/amber high-intensity blinder; flash 13–860 ms, 0.3–30 Hz; 12 strobe zones + 16 RGBW zones; 360° continuous pan/tilt with EMS™ stabilizer",
    ipRating="IP65",
    protocols="DMX, RDM, Art-Net, sACN, CRMX",
    standout="Wash Twist Flash — moving super-strobe with continuous P/T\nWorld-first linear motorised zoom + 1000W blinder",
    lamp="72×20W linear white + 16×60W RGBW + 1000W warm-white blinder",
    link="https://www.robelighting.com/wtf",
    description="Wash + strobe + blinder triple-effect IP65 moving head. Three independent motorised zooms, 12 strobe zones and 16 RGBW zones, plus a 1000 W warm-white/amber blinder make it a single fixture for crowd-killer and stage-fill duties.",
    ipRated=True,
    imageUrl="",
))

new.append(f(
    brand="Robe", model="SVB1™",
    category="Wash", variant="",
    applications=["Touring","TV-Film","Install","Corporate"],
    tier="Small", lampType="LED", watts=330,
    cct="", cctRange="1700-20000K",
    outputLumens=11000, cri=None, criRaw="",
    zoomMin=3.8, zoomMax=50, zoomRatio="", zoomRaw="3.8° - 50°",
    colorMixing="RGBW / CMY (selectable) + tungsten emulation",
    framing=False,
    effectsRaw="7×40W RGBW cells + central 200W white strobe; full pixel mapping; ScreenPix display mapping; 360° continuous pan/tilt; RLCT lens coating",
    weightKg=7.2, ipRating="IP20",
    powerConsumption=330,
    protocols="DMX, RDM, Art-Net, sACN",
    standout="7.2 kg with 360° continuous P/T\n18 dB(A) — studio-quiet",
    lamp="7×40W RGBW + 200W white strobe",
    link="https://www.robe.cz/svb1",
    description="Sub-8 kg moving beam-wash hybrid with seven 40W RGBW pixels around a 200W white strobe centre. 360° continuous pan/tilt, 1700–20000K virtual CCT, and 18 dB(A) acoustic floor.",
    imageUrl="",
))

new.append(f(
    brand="Robe", model="SVOPATT™",
    category="Wash", variant="",
    applications=["Touring","TV-Film","Concert"],
    tier="Large", lampType="LED", watts=None,
    cct="", cctRange="",
    outputLumens=75000, cri=None, criRaw="Cpulse flicker-free; +/- green control",
    zoomMin=None, zoomMax=None, zoomRatio="1:13", zoomRaw="",
    colorMixing="RGB / CMY (selectable) + tungsten emulation",
    framing=False,
    effectsRaw="9 modules × (7×40W RGBW + 200W white strobe centre); pre-programmed pixel animations; M-CEC zoom/chamber sync for shadowless output; L3 dimming",
    ipRating="IP20",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="9-module wash-strobe matrix — 75,000 lm\nM-CEC shadowless zoom system",
    lamp="9 modules × (7×40W RGBW + 200W white strobe)",
    link="https://www.robe.cz/svopatt",
    description="Nine-module multisource moving head: each module pairs seven 40 W RGBW pixels with a 200 W white strobe centre, total >75,000 lm. Designed for broadcast with Cpulse flicker-free dimming and ± green control.",
    imageUrl="",
))

new.append(f(
    brand="Robe", model="iESPRITE® LTL",
    category="Performance", variant="",
    applications=["Touring","Install"],
    tier="Large", lampType="LED", watts=750,
    cct="6700K", cctRange="",
    outputLumens=35000, cri=70, criRaw="CRI 70 (XP) / CRI 96 (HCF option), 22,750 lm HCF",
    zoomMin=0.7, zoomMax=2, zoomRatio="", zoomRaw="0.7° - 2° (long-throw mode via XR7™)",
    colorMixing="CMY / CTO",
    framing=True,
    effectsRaw="XR7 long-throw optic — tightens beam to 0.7° without intensity loss; parCoat hydrophobic lens coating; 200 mm front lens; IP65 iSE-TE Transferable Engine",
    weightKg=37, ipRating="IP65",
    protocols="DMX, RDM, Art-Net, sACN, CRMX",
    standout="0.7° beam in long-throw mode without intensity loss\nIP65 long-throw Esprite",
    lamp="750W iSE-TE LED",
    link="https://www.robelighting.com/iesprite-ltl-fs",
    description="IP65 long-throw variant of the Esprite. Robe's XR7 optic delivers a 0.7° tight beam at 35,000 lm, with a 200 mm front lens and parCoat hydrophobic coating. Optional HCF engine for high-CRI broadcast work.",
    ipRated=True,
    imageUrl="",
))

new.append(f(
    brand="Robe", model="iT12 Profile™",
    category="Performance", variant="Profile",
    applications=["Theater","TV-Film","Touring","Install"],
    tier="Medium", lampType="LED", watts=500,
    cct="", cctRange="2700-8000K",
    outputLumens=13600, cri=95, criRaw="CRI 95, R9 96, TM30 Rf 92 / Rg 106, TLCI 91",
    zoomMin=None, zoomMax=None, zoomRatio="", zoomRaw="",
    colorMixing="RGB / CMY (selectable) + individual emitter control",
    framing=True,
    gobo="Optional drop-in static + rotating gobo module",
    iris=True,
    effectsRaw="Plano4 patented 4-blade framing + 60° rotation (optional drop-in); drop-in gobo & iris module; DataSwatch library (237 presets)",
    ipRating="IP65",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="IP65 static-body profile with drop-in framing/gobo modules\nMulti-spectral engine — CRI 95",
    lamp="500W iSE-MSL-TE",
    link="https://www.robe.cz/it12-profile",
    description="IP65 modular outdoor profile fixture (non-moving body) with a 500 W multi-spectral LED engine, 13,600 lm, CRI 95, and an optional Plano4 framing module. Suited to theatres and outdoor installs that need profile optics without a moving head.",
    ipRated=True,
    imageUrl="",
))

new.append(f(
    brand="Robe", model="iT12 Fresnel™",
    category="Wash", variant="",
    applications=["Theater","TV-Film","Install"],
    tier="Medium", lampType="LED", watts=500,
    cct="", cctRange="2700-8000K",
    outputLumens=11000, cri=95, criRaw="CRI 95+",
    zoomMin=6, zoomMax=60, zoomRatio="1:10", zoomRaw="6° - 60°",
    colorMixing="CMY / RGB (selectable) + individual emitter control",
    framing=False,
    effectsRaw="Patented F2L dual-Fresnel lens — concentric ridges enclosed for debris-free outer surface; parCoat coating; BARS zoom-lock and RAINS microclimate management",
    ipRating="IP65",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="Patented F2L dual-Fresnel — smooth outer lens, no debris build-up\nIP65 with BARS/RAINS climate management",
    lamp="500W iSE-MSL-TE",
    link="https://www.robe.cz/it12-fresnel",
    description="IP65 static Fresnel-style wash with Robe's patented F2L dual-lens system: the concentric ridges are sealed inside, leaving a smooth, debris-resistant outer face. 10:1 zoom, multi-spectral 500 W engine.",
    ipRated=True,
    imageUrl="",
))

new.append(f(
    brand="Robe", model="T11 Profile™",
    category="Performance", variant="Profile",
    applications=["Theater","TV-Film","Install"],
    tier="Medium", lampType="LED", watts=350,
    cct="", cctRange="2700-8000K (ext 1800-10000K)",
    outputLumens=12000, cri=95, criRaw="CRI 95",
    zoomMin=5, zoomMax=50, zoomRatio="1:10", zoomRaw="5° - 50°",
    colorMixing="CMY / RGB (selectable) + tungsten emulation",
    framing=True,
    gobo="Static gobo standard; optional drop-in iris + static + rotating gobo module",
    frost=True,
    effectsRaw="Manual framing shutters; manual zoom; interchangeable front lens system; Cpulse flicker-free; +/- green control",
    powerConsumption=420,
    protocols="DMX, RDM, Art-Net, sACN",
    standout="Compact 350W T-series profile — silent operation\nInterchangeable front lens system",
    lamp="350W MSL-TE",
    link="https://www.robe.cz/t11-profile",
    description="Compact 350 W multi-spectral LED profile aimed at theatres, broadcast and TV studios. Manual framing and zoom keep cost down; Cpulse and +/- green control suit camera work.",
    imageUrl="",
))

# Tier B: IP65 versions of fixtures already in DB.
# Strategy: mirror parent spec but flip ipRating to IP65, ipRated=True, note in standout.
# Parent IDs: ESPRITE=32, FORTE=33, FORTE Fresnel=34, PAINTE=37, Tetra2=113, LEDBeam 350=84
import copy

def ip_variant(parent_id, new_model, variant_note, **overrides):
    """Build an IP65 variant by copying a parent fixture in the existing DB."""
    parent = next(x for x in data if x['id'] == parent_id)
    rec = copy.deepcopy(parent)
    # strip identity
    rec['id'] = None
    rec['model'] = new_model
    rec['ipRating'] = "IP65"
    rec['ipRated'] = True
    rec['lastVerified'] = TODAY
    base_standout = rec.get('standout') or ''
    rec['standout'] = (variant_note + ("\n" + base_standout if base_standout else "")).strip()
    rec['description'] = f"IP65 outdoor variant of the Robe {parent['model']}. Specs mirror the indoor model; ingress-protected housing for permanent outdoor install and inclement-weather touring."
    # variant-specific overrides
    for k,v in overrides.items():
        rec[k] = v
    return rec

new.append(ip_variant(32, "iESPRITE®", "IP65 outdoor Esprite"))
new.append(ip_variant(34, "iESPRITE® Fresnel", "IP65 Fresnel Esprite — F2L debris-free dual lens"))
new.append(ip_variant(33, "iFORTE®", "IP65 outdoor FORTE"))
new.append(ip_variant(33, "iFORTE® FS", "IP65 FollowSpot FORTE", category="Spot", variant=""))
new.append(ip_variant(34, "iFORTE® Fresnel", "IP65 Fresnel FORTE"))
new.append(ip_variant(37, "iPAINTE®", "IP65 outdoor PAINTE"))
new.append(ip_variant(37, "iPAINTE® LTM", "IP65 long-throw mid-air PAINTE — XR7 optic"))
new.append(ip_variant(113, "iTetra2™", "IP65 outdoor batten — Tetra2 family"))
new.append(ip_variant(84, "iBeam 350™", "IP65 outdoor LEDBeam 350"))

# Tier C: Fresnel / PC / FS variants of existing DB fixtures (indoor)
def variant_of(parent_id, new_model, new_category, variant_label, variant_note, lens_descr, **overrides):
    parent = next(x for x in data if x['id'] == parent_id)
    rec = copy.deepcopy(parent)
    rec['id'] = None
    rec['model'] = new_model
    rec['category'] = new_category
    rec['variant'] = variant_label
    # framing depends on category
    if new_category == "Wash":
        rec['framing'] = False
        rec['gobo'] = ""
    rec['lastVerified'] = TODAY
    base_standout = rec.get('standout') or ''
    rec['standout'] = (variant_note + ("\n" + base_standout if base_standout else "")).strip()
    rec['description'] = f"{lens_descr} variant of the Robe {parent['model']}; same {parent.get('watts','')}W engine and feature set with the variant's lens system."
    for k,v in overrides.items():
        rec[k] = v
    return rec

new.append(variant_of(32, "ESPRITE® Fresnel", "Wash", "", "Fresnel optic on Esprite engine", "Fresnel-lens"))
new.append(variant_of(32, "ESPRITE® PC", "Wash", "", "PC-lens variant of the Esprite", "Plano-convex (PC)"))
new.append(variant_of(32, "ESPRITE® FS", "Spot", "FollowSpot", "FollowSpot version with operator handles", "FollowSpot"))
new.append(variant_of(33, "FORTE® FS", "Spot", "FollowSpot", "FollowSpot version with operator handles", "FollowSpot"))
new.append(variant_of(33, "FORTE® PC", "Wash", "", "PC-lens wash variant of the FORTE", "Plano-convex (PC)"))
new.append(variant_of(37, "PAINTE® Fresnel", "Wash", "", "Fresnel-lens variant of the PAINTE", "Fresnel-lens"))
new.append(variant_of(40, "T1 Fresnel", "Wash", "", "Fresnel-lens variant of the T1", "Fresnel-lens"))
new.append(variant_of(40, "T1 PC", "Wash", "", "PC-lens wash variant of the T1", "Plano-convex (PC)"))
new.append(variant_of(40, "T1 Profile FS", "Spot", "FollowSpot", "FollowSpot variant of the T1 Profile", "FollowSpot"))
new.append(variant_of(43, "T2 Fresnel", "Wash", "", "Fresnel-lens variant of the T2", "Fresnel-lens"))
new.append(variant_of(43, "T2 PC", "Wash", "", "PC-lens wash variant of the T2", "Plano-convex (PC)"))
new.append(variant_of(43, "T2 Profile FS", "Spot", "FollowSpot", "FollowSpot variant of the T2 Profile", "FollowSpot"))
new.append(variant_of(84, "LEDBeam 350™ FW", "Wash", "", "Fresnel/Wash variant of LEDBeam 350 (FW)", "Fresnel-Wash"))
new.append(variant_of(83, "LEDBeam 150™ FWQ", "Wash", "", "Fresnel-Wash quad-LED variant of LEDBeam 150 (FWQ)", "Fresnel-Wash Quad"))

# ---------------- ELATION ----------------

new.append(f(
    brand="Elation", model="Proteus Hybrid Max",
    category="Spot", variant="",
    applications=["Touring","Install","Concert"],
    tier="Large", lampType="Discharge", watts=550,
    cct="8000K", cctRange="",
    outputLumens=22000, cri=None, criRaw="",
    zoomMin=1.8, zoomMax=45, zoomRatio="1:25", zoomRaw="1.8° - 45°",
    colorMixing="CMY + CTO",
    framing=False,
    gobo="Dual gobo wheels",
    animationWheel=True, prism=True, iris=False, frost=True,
    effectsRaw="Fast Advanced Features (FAF), Tri-Tier Animation (3 tracks), SpinSync 360° continuous-pan rotation tracking, 4 prisms on 2 planes, dual frost, 170 mm front aperture, 16-position colour wheel, auto-focus",
    ipRating="IP66",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="SpinSync 360° continuous-pan rotation tracking\nTri-Tier animation across 3 tracks",
    lamp="550W Philips MSD Platinum FLEX 500",
    link="https://www.elationlighting.com/products/proteus-hybrid-max",
    description="IP66 hybrid beam/spot/wash with a 550 W Philips MSD Platinum FLEX 500 driving 22,000 lm through a 170 mm front lens. SpinSync coordinates continuous-pan motion across multiple fixtures; FAF and Tri-Tier animation deliver layered movement.",
    dualFrost=True, ipRated=True,
    imageUrl="",
))

new.append(f(
    brand="Elation", model="Proteus Radius",
    category="Spot", variant="",
    applications=["Touring","Install","Concert"],
    tier="Medium", lampType="Laser", watts=100,
    cct="6000K", cctRange="",
    outputLumens=None, cri=None, criRaw="",
    zoomMin=0.9, zoomMax=None, zoomRatio="", zoomRaw="0.9° (fixed beam)",
    colorMixing="CMY",
    framing=False,
    gobo="2 wheels — 13 rotating + 24 static metal",
    prism=True, frost=True,
    effectsRaw="LILI laser-illuminated phosphor source; 360° continuous pan & tilt; 4 prisms on 2 planes; dual frost; 25-position colour wheel; Class 1 Risk Group 2",
    weightKg=20.4, ipRating="IP66",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="0.9° razor beam from 100W LILI laser engine\n10,000 h life with no significant degradation",
    lamp="100W LILI laser-phosphor engine",
    link="https://www.elationlighting.com/products/proteus-radius",
    description="IP66 ultra-narrow beam fixture using Elation's 100 W LILI (Laser Illuminated Lighting Instrument) source. 0.9° beam, 360° continuous pan/tilt, full CMY and a deep gobo/prism package in a touring-friendly 45 lb body.",
    ipRated=True, dualFrost=True,
    imageUrl="",
))

new.append(f(
    brand="Elation", model="Paragon LT",
    category="Performance", variant="Profile",
    applications=["Touring","Install","Theater"],
    tier="Large", lampType="LED", watts=1300,
    cct="", cctRange="",
    outputLumens=50000, cri=93, criRaw="TruTone variable CRI 73-93",
    zoomMin=3.7, zoomMax=49.2, zoomRatio="1:13", zoomRaw="3.7° - 49.2°",
    colorMixing="CMY (SpectraColor option)",
    framing=True,
    gobo="3 wheels — 2 rotating + 1 fixed",
    animationWheel=True, prism=True, iris=True, frost=True,
    effectsRaw="Full animation wheel, overlapping dual prisms, dual frost, high-speed iris, indexable full-blackout framing, interchangeable profile / Fresnel Wash / PC Beam lens",
    ipRating="IP54",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="50,000 lm 1300W profile with swap-in Fresnel/PC lens\nTruTone variable CRI 73–93",
    lamp="1300W LED",
    link="https://www.elationlighting.com/products/paragon-lt",
    description="Long-throw 1300 W LED profile delivering up to 50,000 lm through a 200 mm front lens. IP54 weather-resistant body, swap-in Fresnel/PC lens kits, and TruTone variable CRI from 73 to 93 for film-ready output.",
    dualFrost=True, ipRated=True,
    imageUrl="",
))

new.append(f(
    brand="Elation", model="Rebel DARTZ",
    category="Spot", variant="",
    applications=["Touring","Install","Concert"],
    tier="Small", lampType="LED", watts=150,
    cct="", cctRange="",
    outputLumens=None, cri=None, criRaw="",
    zoomMin=1.5, zoomMax=None, zoomRatio="", zoomRaw="1.5° fixed beam",
    colorMixing="RBL with true-green filter",
    framing=False,
    gobo="Dual wheels — 10 rotating/indexing + 16 static",
    prism=True, frost=True,
    effectsRaw="Stackable 6-facet linear + 8-facet circular prisms, frost; 360° continuous pan & tilt; 5 selectable fan modes (silent option); NFC config; Aria X2 wireless DMX",
    ipRating="IP65",
    protocols="DMX, RDM, Art-Net, sACN, Aria X2 wireless",
    standout="4× brighter than DARTZ 360 — 125,475 lx @ 5 m\n1.5° razor beam from compact body",
    lamp="150W RBL LED engine",
    link="https://www.elationlighting.com/products/rebel-dartz",
    description="IP65 1.5° beam fixture replacing the DARTZ 360 with four times the output. RBL LED engine with dedicated true-green filter, 360° continuous pan/tilt, and integrated wireless DMX.",
    ipRated=True,
    imageUrl="",
))

new.append(f(
    brand="Elation", model="Rebel LINE 8",
    category="Bar / Batten", variant="",
    applications=["Touring","Install","Concert"],
    tier="Medium", lampType="LED", watts=None,
    cct="", cctRange="",
    outputLumens=11548, cri=None, criRaw="",
    zoomMin=4, zoomMax=35, zoomRatio="", zoomRaw="4° - 35°",
    colorMixing="RGBL (+ SparkX CW)",
    framing=False,
    effectsRaw="8 × 60W RGBL engines + 16 × 5W CW SparkX pixels; per-pixel control; 210° tilt; magnetic alignment system for daisy-chained continuous beams",
    ipRating="IP55",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="8-cell RGBL bar with SparkX pixel layer\nMagnetic alignment locks to other LINE units",
    lamp="8 × 60W RGBL + 16 × 5W CW SparkX",
    link="https://www.elationlighting.com/products/rebel-line-8",
    description="Compact 8-cell IP55 pixel bar combining 60 W RGBL beam pixels with a row of 5 W cool-white SparkX accents. 210° tilt, magnetic edge-alignment, and full per-pixel control.",
    ipRated=True,
    imageUrl="",
))

new.append(f(
    brand="Elation", model="Rebel LINE 16",
    category="Bar / Batten", variant="",
    applications=["Touring","Install","Concert"],
    tier="Large", lampType="LED", watts=None,
    cct="", cctRange="",
    outputLumens=25355, cri=None, criRaw="",
    zoomMin=4, zoomMax=35, zoomRatio="", zoomRaw="<4° - 35°+",
    colorMixing="RGBL (+ SparkX CW)",
    framing=False,
    effectsRaw="16 × 60W RGBL engines + 32 × 5W CW SparkX pixels; per-pixel control; 210° tilt; magnetic alignment locks to LINE 8",
    ipRating="IP55",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="16-cell RGBL bar — 25,355 lm\nLinks magnetically with LINE 8 for continuous-beam arrays",
    lamp="16 × 60W RGBL + 32 × 5W CW SparkX",
    link="https://www.elationlighting.eu/rebel-line-16",
    description="Double-length sibling to the Rebel LINE 8: 16 RGBL pixels and 32 SparkX accents producing 25,355 lm. Magnetic alignment connects it seamlessly to LINE 8 units for arbitrary-length continuous bars.",
    ipRated=True,
    imageUrl="",
))

new.append(f(
    brand="Elation", model="Rebel Profile",
    category="Performance", variant="Profile",
    applications=["Touring","Theater","Install"],
    tier="Large", lampType="LED", watts=600,
    cct="6500K", cctRange="",
    outputLumens=22000, cri=None, criRaw="",
    zoomMin=3.5, zoomMax=51, zoomRatio="1:15", zoomRaw="3.5° - 51°",
    colorMixing="CMY",
    framing=True,
    gobo="15 glass gobos",
    animationWheel=True, prism=True, iris=True, frost=True,
    effectsRaw="Full animation wheel, dual prisms, dual frost, high-speed iris, indexable framing with blackout cuts",
    weightKg=29.9,
    protocols="DMX, RDM, Art-Net, sACN",
    standout="Peak Field 600W white LED — 22,000 lm in 30 kg body",
    lamp="600W Peak Field LED",
    link="https://www.elationlighting.com/products/rebel-profile",
    description="600 W LED framing profile with a 22,000 lm Peak Field engine, full glass gobo and animation suite, and a 3.5°–51° zoom. Sits at the top of the Rebel range as a touring profile workhorse.",
    dualFrost=True,
    imageUrl="",
))

new.append(f(
    brand="Elation", model="Rebel Wash 4",
    category="Wash", variant="",
    applications=["Touring","Install","Concert"],
    tier="Small", lampType="LED", watts=240,
    cct="", cctRange="",
    outputLumens=4000, cri=None, criRaw="",
    zoomMin=5, zoomMax=40, zoomRatio="1:8", zoomRaw="5° - 40°",
    colorMixing="RGBL",
    framing=False,
    effectsRaw="360° continuous pan & tilt; zoom-lens homogenisation for smooth wash",
    ipRating="IP65",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="Compact 4-cell IP65 wash with 360° continuous P/T",
    lamp="4 × 60W RGBL",
    link="https://www.elationlighting.eu/rebel-wash-4",
    description="Compact 4-cell IP65 wash from Elation's Rebel range. 4,000 lm, 5°–40° zoom and continuous-rotation pan/tilt for endless movement looks.",
    ipRated=True,
    imageUrl="",
))

new.append(f(
    brand="Elation", model="Rebel Wash 12",
    category="Wash", variant="",
    applications=["Touring","Install","Concert"],
    tier="Medium", lampType="LED", watts=720,
    cct="", cctRange="",
    outputLumens=14000, cri=None, criRaw="",
    zoomMin=5, zoomMax=40, zoomRatio="1:8", zoomRaw="5° - 40°",
    colorMixing="RGBL",
    framing=False,
    effectsRaw="Compact body with fast zoom; pixel-friendly multi-cell layout",
    weightKg=16.5, ipRating="IP65",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="12 × 60W RGBL — 14,000 lm in 16.5 kg",
    lamp="12 × 60W RGBL",
    link="https://www.elationlighting.com/products/rebel-wash-12",
    description="12-cell IP65 wash delivering 14,000 lm from 12 × 60 W RGBL emitters. Sub-17 kg body, 5°–40° zoom — designed for tour-grid use and festival B-stock.",
    ipRated=True,
    imageUrl="",
))

new.append(f(
    brand="Elation", model="Proteus Atlas",
    category="Spot", variant="",
    applications=["Touring","Install","Concert"],
    tier="Large", lampType="Laser", watts=500,
    cct="", cctRange="",
    outputLumens=None, cri=None, criRaw="1,000,000 lx @ 20 m / 100,000 lx @ 100 m",
    zoomMin=0.6, zoomMax=8.5, zoomRatio="", zoomRaw="0.6° - 8.5°",
    colorMixing="CMY",
    framing=False,
    gobo="Rotating + fixed gobo wheels",
    prism=True, frost=True,
    effectsRaw="LILI SSPC laser-phosphor engine; 320 mm front lens; 360° continuous pan; Sky Motion standalone system; marine-grade aluminium shell",
    ipRating="IP66",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="0.6° razor beam — 1 M lx @ 20 m\nXenon-class output from 500W LILI",
    lamp="500W LILI laser-phosphor engine",
    link="https://www.elationlighting.com/products/proteus-atlas",
    description="Ultra-long-throw IP66 beam fixture using a 500 W solid-state phosphor-converted laser engine. 320 mm output lens delivers a 0.6° beam to compete with 7000 W Xenon searchlights at a fraction of the power.",
    dualFrost=True, ipRated=True,
    imageUrl="",
))

new.append(f(
    brand="Elation", model="Fuze PFX",
    category="Performance", variant="Profile",
    applications=["Theater","TV-Film","Touring"],
    tier="Medium", lampType="LED", watts=400,
    cct="6600K", cctRange="",
    outputLumens=15000, cri=None, criRaw="",
    zoomMin=3, zoomMax=53, zoomRatio="1:17", zoomRaw="3° - 53°",
    colorMixing="CMY + CTO",
    framing=True,
    gobo="7 rotating + 11 fixed (18 total)",
    prism=True, frost=True,
    effectsRaw="Dual independent rotating prisms (6-facet linear + 6-facet round); 2 variable frost filters; linear CTO",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="Compact 400W framing + FX fixture, 15,000 lm\nDual stackable prisms",
    lamp="400W White LED",
    link="https://www.elationlighting.com/products/fuze-pfx",
    description="Compact 400 W LED framing/FX fixture delivering 15,000 lm. 1:17 zoom from 3°–53°, full CMY with linear CTO, dual stackable prisms and two variable frosts.",
    dualFrost=True,
    imageUrl="",
))

new.append(f(
    brand="Elation", model="Fuze Profile+",
    category="Performance", variant="Profile",
    applications=["Theater","TV-Film","Install"],
    tier="Medium", lampType="LED", watts=305,
    cct="", cctRange="",
    outputLumens=10000, cri=92, criRaw="CRI 92",
    zoomMin=7, zoomMax=42, zoomRatio="1:6", zoomRaw="7° - 42°",
    colorMixing="RGBMA (additive) + CMY emulation",
    framing=True,
    gobo="Rotating + fixed wheels",
    animationWheel=True, prism=True, iris=True, frost=True,
    effectsRaw="5-color homogenised RGBMA engine (Red, Green, Blue, Mint, Amber); rotating + fixed gobo, animation, prism, iris, frost",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="5-color RGBMA full-spectrum engine — CRI 92",
    lamp="305W RGBMA LED",
    link="https://www.elationlighting.eu/fuze-profile",
    description="LED framing fixture with a 5-colour RGBMA engine for full-spectrum, broadcast-friendly output. CRI 92, 10,000+ lm, and the full Fuze gobo/prism/iris suite.",
    imageUrl="",
))

new.append(f(
    brand="Elation", model="Fuze Profile CW",
    category="Performance", variant="Profile",
    applications=["Theater","TV-Film","Corporate","Install"],
    tier="Medium", lampType="LED", watts=380,
    cct="", cctRange="",
    outputLumens=11000, cri=91, criRaw="CRI 91",
    zoomMin=9, zoomMax=43, zoomRatio="", zoomRaw="9° - 43°",
    colorMixing="Dual colour wheels with CMY filters",
    framing=True,
    gobo="Rotating gobo wheel",
    iris=True,
    effectsRaw="380W cool-white engine; dual colour wheels with solid colours + correction filters; rotating gobo, iris",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="Cool-white CRI 91 framing fixture for trade shows / TV",
    lamp="380W Cool-White LED",
    link="https://www.elationlighting.eu/fuze-profile-cw",
    description="Cool-white 380 W variant of the Fuze Profile for tradeshows, stages and TV. 11,000 lm, CRI 91, dual colour wheels with correction filters and a 9°–43° zoom.",
    imageUrl="",
))

new.append(f(
    brand="Elation", model="Fuze Wash 250",
    category="Wash", variant="",
    applications=["Theater","TV-Film","Corporate"],
    tier="Small", lampType="LED", watts=250,
    cct="", cctRange="",
    outputLumens=8500, cri=92, criRaw="CRI 92",
    zoomMin=6, zoomMax=50, zoomRatio="1:8", zoomRaw="6° - 50°",
    colorMixing="RGBMA + virtual CMY/RGB + variable CCT + magenta/green",
    framing=False,
    effectsRaw="5-color RGBMA homogenised engine for soft Fresnel field; 30,000 h LED life",
    weightKg=11.3,
    protocols="DMX, RDM",
    standout="Velvety-smooth full-spectrum Fresnel wash, CRI 92",
    lamp="250W RGBMA",
    link="https://www.elationlighting.com/products/fuze-wash-250",
    description="Compact 250 W RGBMA Fresnel wash with virtual CMY/RGB control, magenta/green trim and variable CCT. 8,500 lm and a 6°–50° zoom in an 11.3 kg body.",
    imageUrl="",
))

new.append(f(
    brand="Elation", model="Fuze Wash 500 WH",
    category="Wash", variant="",
    applications=["Theater","TV-Film","Corporate","Install"],
    tier="Medium", lampType="LED", watts=500,
    cct="", cctRange="",
    outputLumens=17000, cri=92, criRaw="CRI 92",
    zoomMin=10, zoomMax=45, zoomRatio="", zoomRaw="10° - 45°",
    colorMixing="RGBMA + virtual CMY/RGB + variable CCT + magenta/green",
    framing=False,
    effectsRaw="5-color RGBMA homogenised engine; white-housing variant for theatres",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="500W RGBMA Fresnel wash, white housing\n17,000 lm with CRI 92",
    lamp="500W RGBMA",
    link="https://www.elationlighting.com/products/fuze-wash-500",
    description="White-finish variant of the Fuze Wash 500. 500 W RGBMA Fresnel-style wash with 17,000 lm, CRI 92, and full virtual CMY/RGB control for theatre and TV.",
    imageUrl="",
))

new.append(f(
    brand="Elation", model="CHORUS LINE 8",
    category="Bar / Batten", variant="",
    applications=["Touring","Install","Concert"],
    tier="Small", lampType="LED", watts=320,
    cct="", cctRange="2700-7000K",
    outputLumens=3000, cri=None, criRaw="",
    zoomMin=4, zoomMax=40, zoomRatio="1:10", zoomRaw="4° - 40°",
    colorMixing="RGBW + full pixel control",
    framing=False,
    effectsRaw="Motorised 220° tilt; 64 colour presets + 14 macros; electronic strobe; variable LED refresh for TV/film",
    weightKg=11.3,
    powerConsumption=359,
    protocols="DMX, RDM, Art-Net, Kling-NET",
    standout="8×40W RGBW pixel bar with motorised tilt",
    lamp="8 × 40W RGBW",
    link="https://www.elationlighting.eu/chorus-line-8",
    description="Eight-cell RGBW pixel bar with motorised 220° tilt and 4°–40° zoom. 2,700–7,000 K linear CCT range, per-pixel control, and TV-grade variable refresh.",
    imageUrl="",
))

new.append(f(
    brand="Elation", model="Proteus Brutus FS",
    category="Spot", variant="FollowSpot",
    applications=["Theater","Touring","Install"],
    tier="Large", lampType="LED", watts=1200,
    cct="6500K", cctRange="",
    outputLumens=None, cri=None, criRaw="Variable CRI filter",
    zoomMin=3, zoomMax=35, zoomRatio="", zoomRaw="3° - 35°",
    colorMixing="CMY + CTO",
    framing=False,
    iris=True, frost=True,
    effectsRaw="Indexable gobo, iris, frost; manual follow-spot handle mounts + automated tracking compatibility; removable IP66 camera chassis with NDI/POE/SDI",
    weightKg=29.9, ipRating="IP66",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="Long-throw IP66 follow spot — 16,000 lx @ 20 m\nRemovable NDI/POE/SDI camera chassis",
    lamp="1200W LED",
    link="https://www.elationlighting.com/products/proteus-brutus-fs",
    description="Follow-spot variant of the Proteus Brutus. 1200 W LED engine, 3°–35° zoom and a removable IP66 camera chassis pre-wired for NDI, POE and SDI tracking.",
    ipRated=True,
    imageUrl="",
))

new.append(f(
    brand="Elation", model="Proteus Rayzor Blade S",
    category="Bar / Batten", variant="",
    applications=["Touring","Install","Concert"],
    tier="Small", lampType="LED", watts=360,
    cct="", cctRange="",
    outputLumens=6600, cri=None, criRaw="",
    zoomMin=6, zoomMax=45, zoomRatio="", zoomRaw="6° - 45°",
    colorMixing="RGBW",
    framing=False,
    effectsRaw="6 × 60W RGBW + 128 cool-white strobe dots in 2 lines; SparkLED in-lens accent layer; 16-bit dim; 900–25,000 Hz refresh",
    ipRating="IP65",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="Compact IP65 linear strobe-wash with SparkLED layer\nSmaller sibling to the Rayzor Blade L",
    lamp="6 × 60W RGBW + 128 CW strobe dots",
    link="https://www.elationlighting.com/products/proteus-rayzor-blade-s",
    description="Compact IP65 linear wash/strobe combining 6 RGBW pixels, 128 cool-white strobe dots in two lines and Elation's patent-pending SparkLED in-lens accent layer.",
    ipRated=True,
    imageUrl="",
))

# ---------------- AYRTON ----------------

new.append(f(
    brand="Ayrton", model="Veloce Profile",
    category="Performance", variant="Profile",
    applications=["Touring","Install","Theater"],
    tier="Large", lampType="LED", watts=850,
    cct="6500K", cctRange="2900-6500K",
    outputLumens=43000, cri=None, criRaw="",
    zoomMin=4, zoomMax=52, zoomRatio="1:13", zoomRaw="4° - 52°",
    colorMixing="CMY (HD progressive discs) + extended CTO",
    framing=True,
    effectsRaw="Sealed engine; HD progressive CMY discs; framing system",
    weightKg=40.5, ipRating="IP65",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="Used on Shakira's 2026 world tour\nIP65 6-series Ultimate, infinite continuous P/T",
    lamp="850W sealed LED module",
    link="https://www.ayrton.eu/produit/veloce-profile/",
    description="IP65 6-series Ultimate profile fixture with an 850 W sealed LED module producing 43,000 lm. Infinite continuous pan and tilt, HD progressive CMY discs and a 4°–52° zoom; 72 units lit Shakira's 'Las Mujeres Ya No Lloran' world tour.",
    ipRated=True,
    imageUrl="",
))

new.append(f(
    brand="Ayrton", model="Veloce Wash",
    category="Wash", variant="",
    applications=["Touring","Install","Concert"],
    tier="Large", lampType="LED", watts=850,
    cct="6500K", cctRange="2900-6500K",
    outputLumens=None, cri=None, criRaw="",
    zoomMin=None, zoomMax=None, zoomRatio="", zoomRaw="",
    colorMixing="CMY (HD progressive discs) + extended CTO",
    framing=False,
    effectsRaw="Sealed 850W engine; Fresnel-style wash optics; HD progressive CMY discs",
    ipRating="IP65",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="Wash counterpart to the Veloce Profile — IP65 6-series",
    lamp="850W sealed LED module",
    link="https://www.ayrton.eu/produit/veloce-wash/",
    description="IP65 wash version of Ayrton's 6-series Ultimate Veloce platform. 850 W sealed engine with HD progressive CMY discs and extended CTO; infinite continuous pan and tilt.",
    ipRated=True,
    imageUrl="",
))

new.append(f(
    brand="Ayrton", model="Stradale Profile",
    category="Performance", variant="Profile",
    applications=["Theater","TV-Film","Touring","Install"],
    tier="Medium", lampType="LED", watts=330,
    cct="6500K", cctRange="2700-6500K",
    outputLumens=20000, cri=86, criRaw="CRI 70-86 adjustable",
    zoomMin=4, zoomMax=52, zoomRatio="1:13", zoomRaw="4° - 52°",
    colorMixing="CMY progressive gradient + extended CTO",
    framing=True,
    gobo="2 wheels — 9 rotating + 10 fixed (19 HD glass)",
    animationWheel=True, prism=True, iris=True,
    effectsRaw="15-blade iris (15-100% range); framing with +/- 90° rotation per blade; 7-position colour wheel; mono animation wheel; 5-facet circular + 4-facet linear stackable prisms; LED L70 40,000 h",
    weightKg=23.5, ipRating="IP65",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="Ultra-compact IP65 1-series profile — 23.5 kg\nInfinite continuous P/T as standard",
    lamp="330W LED",
    link="https://www.ayrton.eu/wp-content/uploads/2025/04/StradaleProfile-Specification-Sheet-V2.1.pdf",
    description="First fixture in Ayrton's 1-series Ultimate — an ultra-compact 330 W IP65 profile delivering 20,000 lm in a 23.5 kg body. Full framing with +/- 90° blade rotation, dual stackable prisms and infinite continuous pan/tilt.",
    ipRated=True,
    imageUrl="",
))

new.append(f(
    brand="Ayrton", model="Cobra",
    category="Spot", variant="",
    applications=["Touring","Install","Concert"],
    tier="Medium", lampType="Laser", watts=280,
    cct="6500K", cctRange="",
    outputLumens=None, cri=None, criRaw="",
    zoomMin=0.6, zoomMax=23, zoomRatio="", zoomRaw="0.6° - 23°",
    colorMixing="CMY",
    framing=False,
    gobo="Dual gobo wheels",
    prism=True, frost=True,
    effectsRaw="Laser phosphor engine; 13-lens optical system; rotating prisms; dual frost",
    ipRating="IP65",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="First Ayrton laser-source — 0.6° razor beam",
    lamp="280W laser-phosphor engine",
    link="https://www.ayrton.eu/wp-content/uploads/2024/01/COBRA-Specification-Sheet.pdf",
    description="IP65 3-series laser-source beam fixture with a 0.6° pencil beam and a 38× optical zoom range. The Cobra introduced Ayrton's laser-phosphor architecture later refined in the Cobra².",
    ipRated=True, dualFrost=True,
    imageUrl="",
))

new.append(f(
    brand="Ayrton", model="Cobra²",
    category="Spot", variant="",
    applications=["Touring","Install","Concert"],
    tier="Medium", lampType="Laser", watts=260,
    cct="6500K", cctRange="",
    outputLumens=None, cri=None, criRaw="1,544,000 lx @ 10 m",
    zoomMin=0.6, zoomMax=23, zoomRatio="1:38", zoomRaw="0.6° - 23°",
    colorMixing="CMY",
    framing=False,
    gobo="2 wheels — 12 rotating + 80 metal (92 total)",
    prism=True, frost=True,
    effectsRaw="13-lens 38× optical zoom; 2 sets of 4 combinable rotating prisms; 2 frost filters (light/heavy); infinite continuous P/T",
    ipRating="IP65",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="Second-gen 260W Cobra — 1.5 M lx @ 10 m\n92-gobo arsenal",
    lamp="260W laser-phosphor engine",
    link="https://www.ayrton.eu/wp-content/uploads/2024/01/COBRA2-Specification-Sheet.pdf",
    description="Second-generation Cobra: tighter packaging, 260 W laser-phosphor engine and an enormous 92-gobo library across two wheels. 0.6°–23° zoom range delivers 1.5 million lux at 10 m.",
    ipRated=True, dualFrost=True,
    imageUrl="",
))

new.append(f(
    brand="Ayrton", model="MagicDot Neo",
    category="Wash", variant="",
    applications=["Touring","Install","Concert"],
    tier="Small", lampType="LED", watts=120,
    cct="", cctRange="",
    outputLumens=3000, cri=86, criRaw="CRI 86+",
    zoomMin=3, zoomMax=30, zoomRatio="1:10", zoomRaw="3° - 30°",
    colorMixing="RGB-L",
    framing=False,
    effectsRaw="60-pixel RGB LiquidEffect ring around lens periphery; continuous dual rotation on pan & tilt",
    weightKg=6.6, ipRating="IP65",
    powerConsumption=160,
    protocols="DMX, RDM, Art-Net, sACN",
    standout="60-pixel LiquidEffect ring around 100 mm lens\nCluster-friendly creative effect fixture",
    lamp="120W multi-chip RGB-L",
    link="https://www.ayrton.eu/produit/magicdot-neo/",
    description="6.6 kg IP65 creative-series moving head with a 120 W RGB-L multi-chip source and a 60-pixel RGB ring around its 100 mm lens. Designed to cluster into matrix arrays.",
    ipRated=True,
    imageUrl="",
))

new.append(f(
    brand="Ayrton", model="MagicBlade Neo",
    category="Bar / Batten", variant="",
    applications=["Touring","Install","Concert"],
    tier="Medium", lampType="LED", watts=600,
    cct="", cctRange="",
    outputLumens=15000, cri=86, criRaw="CRI 86+",
    zoomMin=3, zoomMax=30, zoomRatio="1:10", zoomRaw="3° - 30°",
    colorMixing="RGB-L",
    framing=False,
    effectsRaw="5 independent MagicDot Neo heads on one batten, 5 mm spaced; LiquidEffect ring per lens; continuous P/T per head",
    weightKg=32.4, ipRating="IP65",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="Five MagicDot Neo heads on one batten\nLiquidEffect ring per lens",
    lamp="5 × 120W RGB-L",
    link="https://www.ayrton.eu/produit/magicblade-neo/",
    description="Batten of five independently moving MagicDot Neo heads — each with its own 120 W RGB-L source, 100 mm lens, LiquidEffect ring and continuous pan/tilt. 15,000 lm total in a 32.4 kg body.",
    ipRated=True,
    imageUrl="",
))

new.append(f(
    brand="Ayrton", model="Nando 1202",
    category="Wash", variant="",
    applications=["Touring","Install","Concert"],
    tier="Large", lampType="LED", watts=None,
    cct="", cctRange="",
    outputLumens=25000, cri=86, criRaw="CRI 86+",
    zoomMin=3.5, zoomMax=53, zoomRatio="1:15", zoomRaw="3.5° - 53°",
    colorMixing="RGB-L",
    framing=False,
    effectsRaw="28 × 50W RGB-L cells through 303 mm PMMA cluster + 28 light guides; single-piece optical block; flicker-free; 540° pan / 255° tilt",
    weightKg=27.6, ipRating="IP65",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="Beam-Wash hybrid — 25,000 lm in 27.6 kg\n303 mm PMMA single-block optic",
    lamp="28 × 50W RGB-L",
    link="https://www.face.be/article/ayrton-launches-the-nando-1202-the-soul-of-nuance",
    description="IP65 beam-wash hybrid scaling up the Nando 502 architecture: 28 RGB-L cells through a 303 mm PMMA single-piece cluster, 25,000 lm output, and a 3.5°–53° zoom in a 27.6 kg body.",
    ipRated=True,
    imageUrl="",
))

new.append(f(
    brand="Ayrton", model="Huracán Profile",
    category="Performance", variant="Profile",
    applications=["Touring","Install","Theater"],
    tier="Large", lampType="LED", watts=1000,
    cct="6500K", cctRange="2700-15000K",
    outputLumens=None, cri=None, criRaw="ST: CRI>80 / S: CRI 70 (52,000 lm) / TC: CRI>95",
    zoomMin=6, zoomMax=60, zoomRatio="1:10", zoomRaw="6° - 60°",
    colorMixing="Double-level CMY + triple CTO",
    framing=True,
    gobo="14 HD glass on 2 wheels + 2 dynamic effect wheels",
    iris=True, prism=True,
    effectsRaw="178 mm front lens, 13-lens optical system; CMY multi-layered wheel; 15-blade iris; dual rotating prisms",
    ipRating="IP20",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="Available in ST / S / TC engine variants\nDouble-level CMY for 281 trillion colours",
    lamp="1000W LED",
    link="https://www.ayrton.eu/produit/huracan-x/",
    description="1000 W LED framing profile in Ayrton's 5-series Huracán family. 178 mm front lens, 13-lens 10× zoom and a double-level CMY system enabling 281 trillion colours.",
    imageUrl="",
))

new.append(f(
    brand="Ayrton", model="Huracán Wash",
    category="Wash", variant="",
    applications=["Touring","Install","Concert"],
    tier="Large", lampType="LED", watts=1000,
    cct="6500K", cctRange="2700-15000K",
    outputLumens=52000, cri=None, criRaw="ST: 45000 lm / S: 52000 lm CRI 70 / TC: CRI>95",
    zoomMin=6.2, zoomMax=75, zoomRatio="1:12", zoomRaw="6.2° - 75°",
    colorMixing="Double-level CMY + triple CTO",
    framing=False,
    gobo="7 rotating",
    iris=True,
    effectsRaw="Fresnel lens with framing-barndoor optimisation; 15-blade iris; beam ovaliser filter; 540° pan / 260° tilt",
    ipRating="IP20",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="52,000 lm wash with 12× zoom\nST/S/TC engine variants",
    lamp="1000W LED",
    link="https://www.ayrton.eu/produit/huracan-wash/",
    description="1000 W Fresnel wash with a 6.2°–75° zoom and the Huracán family's signature double-level CMY. The Fresnel lens is purpose-designed for barndoor and ovaliser use.",
    imageUrl="",
))

new.append(f(
    brand="Ayrton", model="Domino Profile",
    category="Performance", variant="Profile",
    applications=["Touring","Install","Theater"],
    tier="Large", lampType="LED", watts=1000,
    cct="8000K", cctRange="",
    outputLumens=51000, cri=None, criRaw="S variant: 51,000 lm @ 7000K",
    zoomMin=6, zoomMax=60, zoomRatio="1:10", zoomRaw="6° - 60°",
    colorMixing="CMY (multi-layered wheel)",
    framing=False,
    gobo="14 HD glass on 2 wheels",
    iris=True, prism=True,
    effectsRaw="178 mm front lens, 13-lens optical system; 2 continuous dynamic effect wheels; 15-blade iris; 2 rotating prisms",
    ipRating="IP65",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="IP65 5-series profile — 51,000 lm at 7000K",
    lamp="1000W monochromatic LED",
    link="https://www.ayrton.eu/produit/domino-profile/",
    description="IP65 1000 W LED profile in Ayrton's Domino family. 178 mm front lens, 13-lens 10× zoom and a CMY multi-layer wheel for layered colour mixing.",
    ipRated=True,
    imageUrl="",
))

new.append(f(
    brand="Ayrton", model="Domino Wash",
    category="Wash", variant="",
    applications=["Touring","Install","Concert"],
    tier="Large", lampType="LED", watts=1000,
    cct="7000K", cctRange="2700-15000K",
    outputLumens=52000, cri=None, criRaw="ST: CRI>80 45,000 lm / S: CRI 70 52,000 lm / TC: CRI>95 6000K",
    zoomMin=6.2, zoomMax=75, zoomRatio="1:12", zoomRaw="6.2° - 75°",
    colorMixing="Double-level CMY + triple CTO",
    framing=False,
    effectsRaw="210 mm Fresnel optic; liquid cooling with 6 submersible fans; weatherproof enclosure designed for sand/dust/wind/rain",
    ipRating="IP65",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="First Ayrton IP65 wash — liquid cooled\n281 trillion colours",
    lamp="1000W LED",
    link="https://www.ayrton.eu/produit/domino-wash/",
    description="Ayrton's first IP65-rated wash fixture, available in ST/S/TC engine variants. 210 mm Fresnel optic, liquid cooling with six submersible fans outside the weatherproof body.",
    ipRated=True,
    imageUrl="",
))

new.append(f(
    brand="Ayrton", model="Rivale Wash",
    category="Wash", variant="",
    applications=["Theater","TV-Film","Install"],
    tier="Medium", lampType="LED", watts=430,
    cct="6500K", cctRange="2700-10000K",
    outputLumens=None, cri=None, criRaw="",
    zoomMin=None, zoomMax=None, zoomRatio="", zoomRaw="",
    colorMixing="CMY + CTO",
    framing=False,
    effectsRaw="Fresnel wash counterpart to the Rivale Profile",
    ipRating="IP20",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="Wash sibling to the Rivale Profile",
    lamp="430W LED",
    link="https://www.ayrton.eu/produit/rivale-wash/",
    description="Mid-output Fresnel wash sharing the 430 W LED engine of the Rivale Profile. Targeted at theatre, broadcast and high-end install.",
    imageUrl="",
))

new.append(f(
    brand="Ayrton", model="Zonda 3 FX",
    category="Wash", variant="",
    applications=["Touring","Install","Concert"],
    tier="Small", lampType="LED", watts=350,
    cct="", cctRange="",
    outputLumens=5200, cri=None, criRaw="",
    zoomMin=4, zoomMax=56, zoomRatio="1:14", zoomRaw="4° - 56°",
    colorMixing="RGB+W (additive)",
    framing=False,
    gobo="1 rotating (9 HD glass) + 1 fixed (19 HD glass + 20 metal)",
    effectsRaw="170 mm PMMA mono-block cluster + 7 light guides; HD Liquid Effect™ between main lenses; 7 × 40W RGBW",
    weightKg=11.1, ipRating="IP20",
    powerConsumption=350,
    protocols="DMX, RDM, Art-Net, sACN",
    standout="Smallest Zonda — 11.1 kg with LiquidEffect FX",
    lamp="7 × 40W RGBW",
    link="https://www.ayrton.eu/produit/zonda-3-fx/",
    description="Compact 7-cell RGBW moving wash with a 170 mm PMMA cluster and an HD LiquidEffect layer between the main lenses, plus rotating and fixed glass-gobo wheels for FX work.",
    imageUrl="",
))

new.append(f(
    brand="Ayrton", model="Zonda 3 Wash",
    category="Wash", variant="",
    applications=["Touring","Install","Concert"],
    tier="Small", lampType="LED", watts=350,
    cct="", cctRange="",
    outputLumens=5200, cri=None, criRaw="",
    zoomMin=4, zoomMax=56, zoomRatio="1:14", zoomRaw="4° - 56°",
    colorMixing="RGB+W (additive)",
    framing=False,
    effectsRaw="170 mm PMMA mono-block cluster + 7 light guides; ventilation optimised for silent operation",
    weightKg=11.1, ipRating="IP20",
    powerConsumption=350,
    protocols="DMX, RDM, Art-Net, sACN",
    standout="Silent Zonda 3 sibling without FX wheels",
    lamp="7 × 40W RGBW",
    link="https://www.ayrton.eu/produit/zonda-3-wash/",
    description="Pure-wash sibling of the Zonda 3 FX — same compact 11.1 kg body and 14× zoom but without the gobo/LiquidEffect FX module, with a quieter cooling system.",
    imageUrl="",
))

new.append(f(
    brand="Ayrton", model="Zonda 9 Wash",
    category="Wash", variant="",
    applications=["Touring","Install","Concert"],
    tier="Large", lampType="LED", watts=1400,
    cct="", cctRange="",
    outputLumens=None, cri=None, criRaw="",
    zoomMin=None, zoomMax=None, zoomRatio="", zoomRaw="",
    colorMixing="RGB+W (additive)",
    framing=False,
    effectsRaw="High-power RGBW wash sibling to the Zonda 9 FX",
    ipRating="IP20",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="Pure-wash sibling to the Zonda 9 FX",
    lamp="High-power RGBW cluster",
    link="https://www.ayrton.eu/produit/zonda-9-wash/",
    description="Wash counterpart to the Zonda 9 FX — same 9-series body and RGBW engine without the LiquidEffect/gobo FX module.",
    imageUrl="",
))

# Assign IDs
for rec in new:
    if rec['id'] is None:
        # Skip duplicates by (brand, model)
        key = (rec['brand'].lower(), rec['model'].lower())
        if key in existing_keys:
            print(f"SKIP duplicate: {rec['brand']} {rec['model']}", file=sys.stderr)
            continue
        rec['id'] = next_id
        next_id += 1
        existing_keys.add(key)

new = [r for r in new if r['id'] is not None]
data.extend(new)

with open(PATH, 'w') as out:
    json.dump(data, out, indent=2, ensure_ascii=False)

print(f"Added {len(new)} fixtures. New total: {len(data)}. Next id: {next_id}")
