#!/usr/bin/env python3
"""
Batch 3 fixture additions: Vari-Lite + PRG + ETC + Acme + ADJ gaps.
Run from repo root: python3 scripts/add_batch3_fixtures.py
"""
import json, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(REPO, 'src', 'fixtures.json')
TODAY = '2026-05-30'

with open(PATH) as fp:
    data = json.load(fp)

existing_ids = {x['id'] for x in data}
existing_keys = {(x['brand'].lower().strip(), x['model'].lower().strip()) for x in data}
next_id = max(existing_ids) + 1


def f(**kw):
    base = {
        "id": None, "brand": "", "model": "", "category": "", "variant": "",
        "applications": [], "tier": "", "everUsed": False,
        "lampType": "", "watts": None, "cct": "", "cctRange": "",
        "outputLumens": None, "cri": None, "criRaw": "",
        "zoomMin": None, "zoomMax": None, "zoomRatio": "", "zoomRaw": "",
        "colorMixing": "", "framing": False, "gobo": "",
        "animationWheel": False, "prism": False, "iris": False, "frost": False,
        "effectsRaw": "",
        "pan": None, "tilt": None, "weightKg": None,
        "ipRating": "", "powerConsumption": None,
        "dmxChannels": "", "protocols": "",
        "standout": None, "lamp": "", "panTilt": "",
        "link": "", "description": "", "lastVerified": TODAY,
        "dualFrost": False, "ipRated": False, "imageUrl": "",
    }
    base.update(kw)
    return base


new = []

# ---------------- VARI-LITE ----------------

new.append(f(
    brand="Vari-Lite", model="VL2600 SE Profile",
    category="Performance", variant="Profile",
    applications=["Theater","Touring","Install"],
    tier="Medium", lampType="LED", watts=570,
    cct="8000K",
    outputLumens=23750, cri=81, criRaw="CRI 81, TM30 Rf 80 / Rg 94",
    zoomMin=7, zoomMax=48, zoomRatio="1:7", zoomRaw="7° - 48°",
    colorMixing="CMY + CTO",
    framing=True,
    gobo="2 wheels",
    prism=True, iris=True, frost=True,
    effectsRaw="2 gobo wheels; fixed colour wheel; prism; iris; variable frost; 540° pan / 270° tilt in 3.4 s",
    weightKg=32, ipRating="IP20",
    powerConsumption=820, protocols="DMX, RDM, Art-Net",
    standout="570W upgrade of the VL2600 line\nFraming + variable frost",
    lamp="570W LED",
    link="https://www.vari-lite.com/global/products/vl2600-profile",
    description="570 W LED framing profile delivering 23,750 lm. Two gobo wheels, fixed colour wheel, prism, iris and variable frost in a 32 kg body. Update to the 550 W legacy VL2600 Profile.",
))

new.append(f(
    brand="Vari-Lite", model="VL10 BeamWash",
    category="Wash", variant="",
    applications=["Touring","Install","Concert"],
    tier="Large", lampType="Discharge", watts=None,
    cct="",
    outputLumens=28000, cri=None,
    zoomMin=2.2, zoomMax=48, zoomRatio="1:22", zoomRaw="2.2° - 48°",
    colorMixing="Enhanced CMY",
    framing=False,
    gobo="Rotating gobo wheel + aperture wheel",
    animationWheel=True, prism=True, frost=True,
    effectsRaw="Dual overlaying prisms; VL*FX animation wheel for aerial effects; aperture wheel; rotating gobos; internal frost + heavy frost lens; fixed colour wheel",
    weightKg=33, ipRating="IP20",
    protocols="DMX, RDM, Art-Net",
    standout="VL*FX animation wheel — Vari-Lite aerial-effect signature\n22:1 zoom from 2.2°",
    lamp="Discharge",
    link="https://www.vari-lite.com/global/products/vl10-beamwash",
    description="Beam/wash hybrid producing 28,000 lm with the signature VL*FX animation wheel for aerial effects. 22:1 zoom from a 2.2° beam to a 48° wash in a 33 kg body.",
    dualFrost=True,
))

new.append(f(
    brand="Vari-Lite", model="VL4000 BeamWash",
    category="Wash", variant="",
    applications=["Touring","Install","Concert"],
    tier="Large", lampType="Discharge", watts=1200,
    cct="",
    outputLumens=43000, cri=None, criRaw="43,000 lm standard / 35,000 lm studio mode",
    zoomMin=4, zoomMax=60, zoomRatio="1:15", zoomRaw="4° - 40° (beam) / 10° - 60° (wash)",
    colorMixing="Dual-wheel CMY + eCTO",
    framing=False,
    gobo="2 wheels (7 rotating/indexing + open)",
    animationWheel=True, prism=True, iris=True,
    effectsRaw="Dual opposing colour wheels for infinite CMY cross-fade; eCTO; 5-facet step prism; dual coated-glass dimmer flags; dual-blade strobe; beam-size iris; animation wheel; 10\" front lens",
    ipRating="IP20",
    dmxChannels="41 / 46",
    protocols="DMX, RDM",
    standout="10\" front lens with 1200W Philips MSR Gold\n43,000 lm beam/wash with shaft mode",
    lamp="1200W Philips MSR Gold FastFit",
    link="https://www.vari-lite.com/global/products/vl4000-beamwash",
    description="Flagship 1200 W beam/wash hybrid with a 10\" front lens. Dual opposing colour wheels enable infinite CMY cross-fade; shifts from a near-zero-degree shaft to a 60° wash.",
))

new.append(f(
    brand="Vari-Lite", model="VL5LED Spot",
    category="Spot", variant="",
    applications=["Theater","Touring","Install"],
    tier="Medium", lampType="LED", watts=None,
    cct="",
    outputLumens=None, cri=None,
    zoomMin=None, zoomMax=None, zoomRatio="", zoomRaw="",
    colorMixing="RGBALC",
    framing=False,
    effectsRaw="Modern LED reimagining of the legendary VL5; Dichro*fusion variable-diffusion blades",
    ipRating="IP20",
    protocols="DMX, RDM, Art-Net",
    standout="Modern LED update to the legendary VL5\nRGBALC engine with Dichro*fusion blades",
    lamp="LED (RGBALC)",
    link="https://www.vari-lite.com/global/products/v5led-wash",
    description="Modern LED reimagining of Vari-Lite's legendary VL5 wash, with the RGBALC colour system and Dichro*fusion variable-diffusion blades for the same smooth wash character.",
))

new.append(f(
    brand="Vari-Lite", model="VL1100 LED",
    category="Performance", variant="Profile",
    applications=["Theater","Touring","Install"],
    tier="Small", lampType="LED", watts=445,
    cct="",
    outputLumens=11300, cri=None,
    zoomMin=19, zoomMax=70, zoomRatio="", zoomRaw="19° - 70°",
    colorMixing="CMY",
    framing=False,
    gobo="1 wheel",
    frost=True,
    effectsRaw="ERS (Source Four-style) optics in a moving body; variable frost; 50 kHz quiet motor drive; CMY full crossfade",
    ipRating="IP20",
    protocols="DMX, RDM",
    standout="ERS-style automated profile\n50 kHz silent motor drive",
    lamp="445W LED",
    link="https://www.vari-lite.com/global/products/vl1100-led",
    description="LED automated ERS profile descended from the VL1000. 445 W engine, 11,300 lm, 19°–70° zoom and variable frost — purpose-built for theatres needing a moving Source Four character.",
))

# ---------------- PRG ----------------

new.append(f(
    brand="PRG", model="GroundControl Best Boy LED",
    category="Spot", variant="FollowSpot",
    applications=["Theater","Touring","Broadcast"],
    tier="Large", lampType="LED", watts=None,
    cct="",
    outputLumens=30000, cri=None,
    zoomMin=None, zoomMax=None, zoomRatio="", zoomRaw="",
    colorMixing="CMY + CTO + CTB",
    framing=False,
    gobo="Indexable gobos",
    iris=True, frost=True,
    effectsRaw="Cool-white LED engine; HD-SDI 1080p camera mount with night-vision + targeting reticle; PRG GroundControl remote-spot system",
    ipRating="IP20",
    protocols="DMX, RDM",
    standout="LED retrofit of Best Boy HP — operator on the ground\nHD-SDI camera with night-vision mode",
    lamp="High-wattage cool-white LED",
    link="https://www.prg.com/en/technology/innovation/groundcontrol-followspot-system",
    description="LED-converted Best Boy follow-spot for PRG's GroundControl system. 30,000 lm matches the discharge HP version, while a fixture-mounted HD-SDI camera lets the operator drive the spot from the ground.",
))

new.append(f(
    brand="PRG", model="GroundControl Bad Boy HP",
    category="Spot", variant="FollowSpot",
    applications=["Theater","Touring","Broadcast"],
    tier="Large", lampType="Discharge", watts=1630,
    cct="",
    outputLumens=55000, cri=None,
    zoomMin=None, zoomMax=None, zoomRatio="", zoomRaw="",
    colorMixing="CMY + CTO + CTB",
    framing=False,
    iris=True,
    effectsRaw="Selectable 1200 / 1400 / 1630 W lamp modes; dual colour-correction wheels (CTO + CTB); mechanical iris with continuous timed control; HD-SDI ground-control camera",
    ipRating="IP20",
    protocols="DMX, RDM",
    standout="55,000+ lm with selectable lamp wattage\nHD optics tuned for long throws",
    lamp="Philips MSR Gold FastFit 1200/1400/1630W",
    link="https://www.prg.com/en/technology/innovation/bad-boy-hp",
    description="GroundControl variant of PRG's Bad Boy HP. 55,000+ lm output with selectable lamp wattage (1200/1400/1630 W), dual CTO/CTB wheels and the GroundControl ground-operator camera system.",
))

new.append(f(
    brand="PRG", model="Best Boy HP",
    category="Spot", variant="",
    applications=["Theater","Touring","Install"],
    tier="Large", lampType="Discharge", watts=1500,
    cct="",
    outputLumens=33000, cri=None,
    zoomMin=None, zoomMax=None, zoomRatio="", zoomRaw="",
    colorMixing="CMY",
    framing=False,
    iris=True,
    effectsRaw="1500 W HTI discharge; CMY mixing; short-to-medium throw follow-spot or fixture mode",
    ipRating="IP20",
    protocols="DMX, RDM",
    standout="33,000 lm short-to-medium throw — classic PRG workhorse",
    lamp="1500W HTI",
    link="https://prggear.com/product/groundcontrol-prg-best-boy-led/",
    description="Discharge Best Boy producing 33,000 lm from a 1500 W HTI lamp. The reference short-to-medium throw automated follow-spot for many touring rigs prior to the LED conversion.",
))

# ---------------- ETC ----------------

new.append(f(
    brand="ETC", model="Releve Spot",
    category="Spot", variant="",
    applications=["Theater","TV-Film","Install"],
    tier="Small", lampType="LED", watts=182,
    cct="", cctRange="2700-7000K",
    outputLumens=6000, cri=None,
    zoomMin=None, zoomMax=None, zoomRatio="", zoomRaw="",
    colorMixing="RGIL (Red, Green, Indigo, Lime) additive",
    framing=False,
    gobo="Optional",
    effectsRaw="52 LEDs in 4-color RGIL additive mix; ColorSource Deep Blue heritage; 2700–7000K virtual white",
    ipRating="IP20",
    protocols="DMX, RDM",
    standout="Additive RGIL mixing — saturated reds, deep blues, no CMY filter loss",
    lamp="182W RGIL LED",
    link="https://www.etcconnect.com/Products/Lighting-Fixtures/ReleveSpot/Features.aspx",
    description="ETC's first foray into automated lighting using an additive 4-colour RGIL (Red, Green, Indigo, Lime) array. 6,000 lm output with the colour fidelity of ETC's ColorSource Deep Blue heritage.",
))

new.append(f(
    brand="ETC", model="Halcyon Gold",
    category="Performance", variant="Performance",
    applications=["Theater","TV-Film","Install"],
    tier="Large", lampType="LED", watts=None,
    cct="",
    outputLumens=31000, cri=None,
    zoomMin=None, zoomMax=None, zoomRatio="", zoomRaw="",
    colorMixing="CMY + CTO",
    framing=True,
    animationWheel=True, prism=True, iris=True, frost=True,
    effectsRaw="Continuously rotating animation wheel with incline control; patented Whisper Home homing tech (silent, fast, precise); choice of Ultra-Bright or High-Fidelity LED engine",
    weightKg=28.1, ipRating="IP20",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="Whisper Home silent dual-sensor homing\nUltra-Bright or High-Fidelity engine variants",
    lamp="LED (Ultra-Bright or High-Fidelity)",
    link="https://www.etcconnect.com/Products/Automated-Lighting/Halcyon/Features.aspx",
    description="Compact framing fixture in ETC's Halcyon family producing 31,000 lm in a 62 lb body. Available with Ultra-Bright or High-Fidelity engines; features the family's patented Whisper Home silent-homing system.",
))

new.append(f(
    brand="ETC", model="Halcyon Platinum",
    category="Performance", variant="Performance",
    applications=["Theater","TV-Film","Touring"],
    tier="Large", lampType="LED", watts=1000,
    cct="",
    outputLumens=54000, cri=None, criRaw="54,000 lm standard / 70,000 lm boost mode",
    zoomMin=None, zoomMax=None, zoomRatio="", zoomRaw="",
    colorMixing="CMY + CTO",
    framing=True,
    animationWheel=True, prism=True, iris=True, frost=True,
    effectsRaw="1000 W in standard mode with boost-mode for 70,000 lm; continuously rotating animation wheel with incline control; Whisper Home homing",
    weightKg=44.9, ipRating="IP20",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="Flagship Halcyon — 54,000 lm / 70,000 lm boost\n1000W LED engine",
    lamp="1000W LED",
    link="https://www.etcconnect.com/Products/Automated-Lighting/Halcyon/Features.aspx",
    description="Flagship Halcyon framing fixture: 54,000 lm standard with a boost mode pushing to 70,000 lm. 1000 W LED engine, dual engine options, and a 99 lb body.",
))

# ---------------- ACME ----------------

new.append(f(
    brand="Acme", model="XP-5R Beam",
    category="Spot", variant="",
    applications=["Touring","Install","Concert"],
    tier="Small", lampType="Discharge", watts=189,
    cct="8000K",
    outputLumens=None, cri=None,
    zoomMin=None, zoomMax=None, zoomRatio="", zoomRaw="",
    colorMixing="",
    framing=False,
    gobo="14 rotating",
    prism=True, iris=True,
    effectsRaw="Philips MSD Platinum 5R discharge source (2500h life); rotating gobos; rotating prism; fast iris; built-in 14-colour wheel; variable CTO; motorised focus + zoom",
    ipRating="IP20",
    protocols="DMX, RDM",
    standout="Compact 5R beam fixture at workhorse price",
    lamp="189W Philips MSD Platinum 5R",
    link="https://www.acmelighting.com/Info/productdetail/id/2413",
    description="Compact discharge beam fixture built around the Philips Platinum 5R lamp. 14 rotating gobos, rotating prism and fast iris in an entry-level beam body.",
))

new.append(f(
    brand="Acme", model="XP-1000WZ",
    category="Wash", variant="",
    applications=["Touring","Install"],
    tier="Small", lampType="LED", watts=None,
    cct="",
    outputLumens=None, cri=None,
    zoomMin=None, zoomMax=None, zoomRatio="", zoomRaw="",
    colorMixing="RGBW",
    framing=False,
    effectsRaw="LED wash with motorised zoom; positions in Acme's mid-tier moving-wash line",
    ipRating="IP20",
    protocols="DMX, RDM",
    standout="Mid-tier RGBW LED wash with motorised zoom",
    lamp="LED",
    link="https://en.acmelighting.com/",
    description="RGBW LED moving-head wash with motorised zoom from Acme's mid-tier XP line.",
))

new.append(f(
    brand="Acme", model="TS-150",
    category="Performance", variant="Profile",
    applications=["Theater","Install"],
    tier="Small", lampType="LED", watts=150,
    cct="",
    outputLumens=None, cri=94, criRaw="CQS 94 (WW) / 91 (CW)",
    zoomMin=14, zoomMax=55, zoomRatio="", zoomRaw="14° - 55°",
    colorMixing="",
    framing=True,
    effectsRaw="Motorised linear zoom 14°–55°; <25 dB at 1 m; full framing; 2/3-channel control modes",
    ipRating="IP20",
    protocols="DMX",
    standout="Under 25 dB — silent theatre profile\nCQS 94",
    lamp="150W LED",
    link="https://en.acmelighting.com/",
    description="Compact silent theatre profile (under 25 dB at 1 m) with 14°–55° motorised zoom, full framing and a high-CQS engine tuned for stage and broadcast.",
))

new.append(f(
    brand="Acme", model="CM-300Z Pageant",
    category="Wash", variant="",
    applications=["Touring","Install","Corporate"],
    tier="Small", lampType="LED", watts=285,
    cct="",
    outputLumens=3364, cri=None,
    zoomMin=10, zoomMax=60, zoomRatio="1:6", zoomRaw="10° - 60°",
    colorMixing="RGBW",
    framing=False,
    effectsRaw="19 × 15W RGBW 4-in-1; motorised 1:6 zoom; 0-100% smooth dim; flicker-free management",
    ipRating="IP20",
    protocols="DMX",
    standout="Compact 19-pixel RGBW wash with 1:6 zoom",
    lamp="19 × 15W RGBW",
    link="https://en.acmelighting.com/",
    description="Mid-tier RGBW LED wash with 19 × 15 W 4-in-1 cells producing 3,364 lm. Motorised 1:6 zoom (10°–60°) and flicker-free dimming for camera work.",
))

# ---------------- ADJ ----------------

new.append(f(
    brand="ADJ", model="Vizi Hybrid 16RX",
    category="Spot", variant="",
    applications=["Install","Corporate"],
    tier="Small", lampType="Discharge", watts=330,
    cct="8000K",
    outputLumens=None, cri=None,
    zoomMin=3, zoomMax=32, zoomRatio="", zoomRaw="3° - 32°",
    colorMixing="",
    framing=False,
    gobo="17 static + 12 rotating",
    prism=True, iris=True, frost=True,
    effectsRaw="Philips Platinum 16R MSD (1500h); 14 colours + white; 6-facet linear + 8-facet circular prisms with macros; motorised focus + zoom; frost; motorised shutter; electronic strobe 0.3-7 Hz",
    weightKg=23.1, ipRating="IP20",
    protocols="DMX",
    standout="Compact 16R beam/spot/wash hybrid at ADJ price point",
    lamp="330W Philips Platinum 16R MSD",
    link="https://www.adj.com/vizi-hybrid-16rx",
    description="Beam/spot/wash hybrid built around the Philips Platinum 16R lamp. 3°–32° zoom, dual prisms, frost and a deep gobo/colour package in an install-friendly 23 kg body.",
))

new.append(f(
    brand="ADJ", model="Vizi Beam RXONE",
    category="Spot", variant="",
    applications=["Install","Corporate"],
    tier="Small", lampType="Discharge", watts=100,
    cct="",
    outputLumens=None, cri=None,
    zoomMin=3, zoomMax=3, zoomRatio="", zoomRaw="3° fixed beam",
    colorMixing="",
    framing=False,
    gobo="15 static",
    prism=True,
    effectsRaw="Osram Sirius HRI 1R discharge (6000h); 16-facet prism; 14 colours + white; 15 static gobos; ~100 m throw",
    ipRating="IP20",
    powerConsumption=199, dmxChannels="15 / 17",
    protocols="DMX",
    standout="3° pencil beam at ~199 W draw\n6000 h lamp life",
    lamp="100W Osram Sirius HRI 1R",
    link="https://www.adj.com/products/vizi-beam-rxone",
    description="Compact 3° pencil-beam fixture for clubs and small touring. Osram Sirius HRI 1R lamp (6000 h life), 16-facet prism, ~100 m throw at just 199 W max draw.",
))

new.append(f(
    brand="ADJ", model="Inno Color Beam Quad 7",
    category="Wash", variant="",
    applications=["Install","Corporate"],
    tier="Small", lampType="LED", watts=70,
    cct="",
    outputLumens=None, cri=None,
    zoomMin=10, zoomMax=10, zoomRatio="", zoomRaw="10° fixed",
    colorMixing="RGBW",
    framing=False,
    effectsRaw="7 × 10W RGBW Cree LEDs; 540° pan / 200° tilt; sound-active and master/slave modes; 50,000 h LED life",
    weightKg=6, ipRating="IP20",
    powerConsumption=130, dmxChannels="1 / 13",
    protocols="DMX",
    standout="6 kg sub-200W moving head — install workhorse",
    lamp="7 × 10W RGBW Cree LED",
    link="https://www.adj.com/inno-color-beam-quad7",
    description="Compact 6 kg moving head with 7 × 10 W Cree RGBW LEDs. 10° beam, 540°/200° pan/tilt, sound-active and master/slave modes — install and small-format touring workhorse.",
))

new.append(f(
    brand="ADJ", model="Hydro Beam X12",
    category="Spot", variant="",
    applications=["Touring","Install","Concert"],
    tier="Medium", lampType="Discharge", watts=260,
    cct="",
    outputLumens=None, cri=None,
    zoomMin=2, zoomMax=2, zoomRatio="", zoomRaw="2° fixed",
    colorMixing="",
    framing=False,
    gobo="16 + open (incl. 4 beam reducers)",
    prism=True, frost=True,
    effectsRaw="Philips Platinum 12R LL discharge; 14 colours + white (UV/CTO/CTB); motorised focus; 6-facet linear + 24-facet circular rotating prisms; frost",
    ipRating="IP65",
    protocols="DMX",
    standout="IP65 12R beam at ADJ price point",
    lamp="260W Philips Platinum 12R LL",
    link="https://www.adj.com/products/hydro-beam-x12",
    description="IP65 dedicated beam fixture with a Philips Platinum 12R LL discharge lamp. 2° beam, 14 colour + white wheel including UV/CTO/CTB, dual rotating prisms and frost.",
    ipRated=True,
))

new.append(f(
    brand="ADJ", model="Hydro Wash X19",
    category="Wash", variant="",
    applications=["Touring","Install","Concert"],
    tier="Medium", lampType="LED", watts=760,
    cct="",
    outputLumens=None, cri=None,
    zoomMin=6, zoomMax=40, zoomRatio="", zoomRaw="6° - 40°",
    colorMixing="RGBW",
    framing=False,
    effectsRaw="19 × Osram 40W RGBW (4-in-1); WiFLY wireless DMX; motorised focus; fine pan/tilt + dimming; 6 dimmer modes; IP65 connectors",
    ipRating="IP65",
    protocols="DMX, WiFLY wireless",
    standout="IP65 19-cell RGBW wash with onboard WiFLY DMX",
    lamp="19 × 40W Osram RGBW",
    link="https://www.adj.com/products/hydro-wash-x19",
    description="IP65 outdoor wash with 19 × Osram 40 W RGBW pixels. 6°–40° motorised zoom, WiFLY wireless DMX onboard, and IP65 power/data connectors.",
    ipRated=True,
))

new.append(f(
    brand="ADJ", model="Focus Hybrid",
    category="Spot", variant="",
    applications=["Touring","Install","Corporate"],
    tier="Small", lampType="LED", watts=200,
    cct="7500K",
    outputLumens=4100, cri=None,
    zoomMin=2, zoomMax=24, zoomRatio="1:12", zoomRaw="2° - 24°",
    colorMixing="",
    framing=False,
    effectsRaw="200 W cool-white LED engine (50,000 h life); 1:12 zoom; can switch between spot/wash/beam roles",
    ipRating="IP20",
    protocols="DMX",
    standout="Sub-5 kg LED hybrid — spot/wash/beam in one",
    lamp="200W Cool White LED",
    link="https://www.adj.eu/focus-hybrid",
    description="Compact LED hybrid moving head with a 2°–24° zoom that re-tasks between spot, wash and beam roles. 200 W cool-white engine producing 4,100 lm.",
))

# Assign IDs / dedupe
for rec in new:
    key = (rec['brand'].lower().strip(), rec['model'].lower().strip())
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
