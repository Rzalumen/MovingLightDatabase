#!/usr/bin/env python3
"""
Add VELLO Light Co. moving-head fixtures to fixtures.json.

VELLO is a Chinese OEM/ODM stage-lighting manufacturer in Guangzhou.
Tier-wise, the brand sits below the touring-grade lines (Robe, Martin, etc.)
already in the DB — closer to ADJ in catalog tone. Specs that VELLO's
site doesn't publish (true fixture-out lumens, CRI, TM-30, weight) are
left as null/"" per the never-invent rule.

Source: https://www.vellolight.com/moving-head-series/
Image URLs use VELLO's CDN (vellolight.com/upload/img/...).
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

BRAND = "VELLO"
IMG_BASE = "https://www.vellolight.com/upload/img/GY879209523016/"


def f(**kw):
    base = {
        "id": None, "brand": BRAND, "model": "", "category": "", "variant": "",
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

# ----- Moving-head catalogue (from /moving-head-series/) -----

new.append(f(
    model="Laser Beam AK880 IP",
    category="Spot", variant="",
    applications=["Touring","Install","Concert"],
    tier="Medium", lampType="Laser",
    effectsRaw="165 mm laser-beam optic; IP-rated outdoor housing; sharp dynamic beam effects",
    ipRating="IP65",
    protocols="DMX, RDM",
    standout="165 mm laser-beam optic — IP-rated outdoor",
    lamp="Laser engine",
    link="https://www.vellolight.com/product/ak880-ip/",
    description="Outdoor IP-rated laser-source moving beam built around a 165 mm front lens. Aimed at large outdoor productions where a sharp aerial beam is the primary look.",
    ipRated=True,
    imageUrl=IMG_BASE + "3-9.png",
))

new.append(f(
    model="BEAM AK550 IP66",
    category="Spot", variant="",
    applications=["Touring","Install","Concert"],
    tier="Medium", lampType="Discharge", watts=550,
    zoomMin=2, zoomMax=2, zoomRatio="", zoomRaw="2° fixed beam",
    colorMixing="14-colour wheel",
    framing=False,
    gobo="15 + open",
    prism=True, frost=True,
    effectsRaw="Ushio NSLU7A 390W discharge; 14-colour wheel; 15 gobos + open; dual prisms (8-facet + 16-facet honeycomb); linear frost and focus; 540° pan / 270° tilt with 16-bit movement and automatic position correction; LCD touch display",
    ipRating="IP66",
    protocols="DMX, Master/Slave, standalone",
    standout="IP66 outdoor beam — Ushio 390W discharge\nDual prisms incl. honeycomb",
    lamp="Ushio NSLU7A 390W",
    link="https://www.vellolight.com/product/led-light-moving-head-ak550-ip66-beam/",
    description="IP66 outdoor 550 W moving-head spot driven by a Japanese Ushio 390 W discharge bulb. 2° beam, dual prisms including a honeycomb element, and an LCD touch display in a compact body aimed at touring and outdoor events.",
    ipRated=True,
    imageUrl=IMG_BASE + "ak550-1.png",
))

new.append(f(
    model="LED BSWF1000",
    category="Performance", variant="",
    applications=["Touring","Install","Concert","Broadcast"],
    tier="Large", lampType="LED", watts=850,
    cri=90, criRaw="CRI 90+",
    colorMixing="CMY",
    framing=True,
    effectsRaw="4-in-1 hybrid (beam/spot/wash/framing); 850W white LED engine; smooth CMY mixing",
    ipRating="IP20",
    powerConsumption=1000,
    protocols="DMX, RDM",
    standout="4-in-1 hybrid (beam/spot/wash/framing)\n850W high-CRI LED engine",
    lamp="850W White LED 4-in-1",
    link="https://www.vellolight.com/product/led-moving-head-beam-light-bswf1000/",
    description="Top-of-line VELLO hybrid combining beam, spot, wash and framing functions in one body. 850 W high-CRI white LED engine for theatre / touring / broadcast use.",
    imageUrl=IMG_BASE + "bswf1000.png",
))

new.append(f(
    model="LED BSW600",
    category="Spot", variant="",
    applications=["Touring","Install","Concert"],
    tier="Medium", lampType="LED", watts=550,
    zoomMin=4, zoomMax=42, zoomRatio="", zoomRaw="4° - 42°",
    colorMixing="CMY (3 wheels)",
    framing=False,
    gobo="7 rotating + 9 static metal",
    prism=True,
    effectsRaw="Apotronics 550W white LED engine; 3 CMY wheels; 3-facet circular prism; 540° pan / 270° tilt 16-bit; linear dimming; automatic position correction",
    ipRating="IP20",
    powerConsumption=650,
    protocols="DMX, RDM",
    standout="3-in-1 beam/spot/wash — Apotronics 550W LED",
    lamp="550W Apotronics White LED",
    link="https://www.vellolight.com/product/led-moving-head-stage-light-bsw600/",
    description="650 W 3-in-1 beam/spot/wash moving head built around a 550 W Apotronics white LED engine. CMY mixing via three wheels, 4°–42° zoom, and 16-bit precision movement.",
    imageUrl=IMG_BASE + "bsw600-3.png",
))

new.append(f(
    model="Moving Head BEAM 450",
    category="Spot", variant="",
    applications=["Touring","Install"],
    tier="Medium", lampType="Discharge", watts=420,
    colorMixing="",
    framing=False,
    effectsRaw="Original Osram 420W bulb; beam/spot/wash hybrid in compact body",
    ipRating="IP20",
    protocols="DMX",
    standout="Compact beam/spot/wash hybrid — Osram 420W",
    lamp="Osram 420W discharge",
    link="https://www.vellolight.com/product/led-moving-head-light-beam450/",
    description="Compact moving-head fixture with an original Osram 420 W discharge bulb. Combines beam, spot and wash functions in one body for general-purpose touring and install use.",
    imageUrl=IMG_BASE + "beam450-3.png",
))

new.append(f(
    model="BEAM 400",
    category="Spot", variant="",
    applications=["Touring","Install","Concert"],
    tier="Medium", lampType="Discharge", watts=371,
    zoomMin=1.8, zoomMax=1.8, zoomRatio="", zoomRaw="1.8° fixed beam",
    colorMixing="14-colour wheel",
    framing=False,
    gobo="12 + open",
    prism=True, frost=True,
    effectsRaw="Osram SIRIUS 371W discharge; 14-colour wheel; 12 fixed gobos + open; 16-facet circular rotating prism; linear frost and focus; 540° pan / 270° tilt 16-bit",
    ipRating="IP20",
    powerConsumption=500,
    protocols="DMX",
    standout="Sharp 1.8° beam — Osram SIRIUS 371W\nComparable to traditional 750W heads",
    lamp="Osram SIRIUS 371W",
    link="https://www.vellolight.com/product/moving-head-stage-light-beam400/",
    description="500 W professional moving beam powered by an Osram SIRIUS 371 W discharge bulb. 1.8° sharp beam, 14-colour wheel, 12 fixed gobos and a 16-facet rotating prism in a tour-ready package.",
    imageUrl=IMG_BASE + "beam400-2.png",
))

new.append(f(
    model="BSW450 Outdoor",
    category="Spot", variant="",
    applications=["Touring","Install"],
    tier="Medium", lampType="Discharge", watts=420,
    colorMixing="",
    framing=False,
    effectsRaw="Original Osram 420W bulb; beam/spot/wash hybrid in outdoor-rated housing",
    ipRating="IP65",
    protocols="DMX",
    standout="IP65 outdoor beam/spot/wash — Osram 420W",
    lamp="Osram 420W discharge",
    link="https://www.vellolight.com/product/dmx-moving-head-lights-outdoor-bsw450/",
    description="Outdoor IP-rated moving head built around an original Osram 420 W bulb. Combines beam, spot and wash modes in one fixture for outdoor stages.",
    ipRated=True,
    imageUrl=IMG_BASE + "bsw450-1.png",
))

new.append(f(
    model="BEAM 360",
    category="Spot", variant="",
    applications=["Touring","Install","Concert"],
    tier="Small", lampType="Discharge", watts=311,
    zoomMin=1.8, zoomMax=1.8, zoomRatio="", zoomRaw="1.8° fixed beam",
    colorMixing="14-colour wheel",
    framing=False,
    gobo="12 + open",
    prism=True, frost=True,
    effectsRaw="Osram SIRIUS 311W discharge; 14-colour wheel; 12 fixed metal gobos + open; dual prisms (8-facet circular + 8+16 multi-facet); linear frost and focus; 540° pan / 270° tilt 16-bit",
    ipRating="IP20",
    powerConsumption=400,
    protocols="DMX",
    standout="Sharp 1.8° beam — Osram SIRIUS 311W\nDual prisms (circular + combination)",
    lamp="Osram SIRIUS 311W",
    link="https://www.vellolight.com/product/led-moving-head-stage-light-beam360/",
    description="400 W high-power moving beam with an Osram SIRIUS 311 W lamp delivering a 1.8° beam. 14 colours, 12 metal gobos, dual prisms — comparable to a traditional 575 W moving head.",
    imageUrl=IMG_BASE + "beam360-2-7.png",
))

new.append(f(
    model="LED Bee Eyes K20",
    category="Wash", variant="",
    applications=["Touring","Install","Concert"],
    tier="Medium", lampType="LED", watts=760,
    cct="", cctRange="2700-8000K",
    zoomMin=4, zoomMax=60, zoomRatio="1:15", zoomRaw="4° - 60°",
    colorMixing="RGBW",
    framing=False,
    effectsRaw="19 × 40W Osram RGBW; individual per-LED control + pixel mapping; rotating lens wheel for dynamic effects; CTO 2700-8000K; 540° pan / 270° tilt; multiple DMX modes",
    ipRating="IP20",
    powerConsumption=750,
    protocols="DMX",
    standout="19-cell Osram RGBW wash with rotating lens\nPer-pixel control",
    lamp="19 × 40W Osram RGBW",
    link="https://www.vellolight.com/product/led-bee-eyes-lights-k20/",
    description="750 W 'bee-eye' style moving wash with 19 × 40 W Osram RGBW cells. 4°–60° electronic zoom, 2700–8000 K virtual CCT, individual pixel control and a rotating lens wheel.",
    imageUrl=IMG_BASE + "led-bee-eyes-k20-2.png",
))

new.append(f(
    model="LED XP800 (4-in-1)",
    category="Wash", variant="",
    applications=["Touring","Install","Theater"],
    tier="Medium", lampType="LED", watts=600,
    cct="", cctRange="2800-8500K",
    zoomMin=6, zoomMax=50, zoomRatio="", zoomRaw="6° - 50°",
    colorMixing="RGBW",
    framing=False,
    effectsRaw="37 × 20W Osram RGBW; 3-ring pixel control; CTO 2800-8500K; 540° pan / 310° tilt; high-speed 3-phase motors; 16/28 DMX channels",
    ipRating="IP20",
    dmxChannels="16 / 28",
    protocols="DMX",
    standout="37-cell RGBW wash — 3-ring pixel control\n310° tilt range",
    lamp="37 × 20W Osram RGBW",
    link="https://www.vellolight.com/product/led-moving-head-light-xp800-4in1/",
    description="600 W moving-head wash with 37 × 20 W Osram RGBW cells laid out in three rings for layered pixel effects. Wide 6°–50° electronic zoom and 540° pan / 310° tilt.",
    imageUrl=IMG_BASE + "led-xp800-4in1-5.png",
))

new.append(f(
    model="Max Wash X7 (7-in-1)",
    category="Wash", variant="",
    applications=["TV-Film","Touring","Install","Concert"],
    tier="Medium", lampType="LED", watts=760,
    cct="", cctRange="3200-6800K",
    cri=95, criRaw="CRI >= 95",
    zoomMin=6.1, zoomMax=50, zoomRatio="", zoomRaw="6.1° - 50°",
    colorMixing="RGB+A+C+L 7-in-1",
    framing=False,
    effectsRaw="19 × 40W RGB+A+C+L 7-in-1; 3-ring pixel control; CTO presets at 3200/4200/5600/6800K; 540° pan / 310° tilt; high-speed motors; heat-proof housing",
    ipRating="IP20",
    powerConsumption=750,
    protocols="DMX",
    standout="7-in-1 RGB+A+C+L wash — CRI ≥ 95\nFour CTO preset whites",
    lamp="19 × 40W 7-in-1 RGB+A+C+L",
    link="https://www.vellolight.com/product/led-max-moving-head-wash-light-x7-7in1/",
    description="High-CRI 7-in-1 (RGB + amber + cyan + lime) wash with 19 × 40 W cells delivering CRI ≥ 95. Four CTO preset whites and 3-ring pixel control; targets concerts and TV studios.",
    imageUrl=IMG_BASE + "x7-1.png",
))

new.append(f(
    model="Bee Eye K7",
    category="Wash", variant="",
    applications=["Touring","Install","Concert"],
    tier="Small", lampType="LED", watts=500,
    cct="", cctRange="2700-8000K",
    zoomMin=4, zoomMax=45, zoomRatio="", zoomRaw="4° - 45°",
    colorMixing="RGBW",
    framing=False,
    effectsRaw="7 × 60W Osram RGBW main + 48 × 0.5W RGB auxiliary halo LEDs; individual pixel control; rotation-lens effects; 540° pan / 270° tilt",
    ipRating="IP20",
    protocols="DMX",
    standout="7-cell bee-eye with 48-pixel RGB halo ring",
    lamp="7 × 60W Osram RGBW + 48 × 0.5W RGB aux",
    link="https://www.vellolight.com/product/bee-eye-led-moving-head-k7/",
    description="Compact 500 W bee-eye style wash with seven 60 W Osram RGBW LEDs plus a 48-pixel RGB auxiliary halo for accent effects. 4°–45° zoom and rotation-lens effects.",
    imageUrl=IMG_BASE + "k7-2.png",
))

new.append(f(
    model="LED MEGA K30 IP",
    category="Wash", variant="",
    applications=["Touring","Install","Concert"],
    tier="Small", lampType="LED",
    colorMixing="RGBW per pixel",
    framing=False,
    effectsRaw="Per-pixel control for 2D/3D pixel-mapping; NFC wireless configuration; IP-rated housing",
    ipRating="IP65",
    protocols="DMX, NFC",
    standout="NFC-configurable LED par with per-pixel control",
    lamp="Pixel LED array",
    link="https://www.vellolight.com/product/led-mega-k30-ip/",
    description="IP-rated pixel-mapping fixture with NFC wireless configuration and per-LED control. Aimed at productions wanting fine-grained pixel choreography on the fixture body itself.",
    ipRated=True,
    imageUrl=IMG_BASE + "99f5250d81a73600ea229c36ca4dbada.png",
))

# ----- Outdoor Storm fixtures (from homepage) -----

new.append(f(
    model="LED Storm 2500 IP",
    category="Wash", variant="",
    applications=["Touring","Install","Concert"],
    tier="Large", lampType="LED", watts=None,
    colorMixing="RGBW",
    framing=False,
    effectsRaw="Smart-glass electronic frost; outdoor IP-rated housing",
    ipRating="IP65",
    powerConsumption=1000,
    protocols="DMX",
    standout="Smart-glass electronic frost — no mechanical actuator",
    lamp="LED",
    link="https://www.vellolight.com/product/led-outdoor-moving-head-storm-light-2500-ip/",
    description="IP-rated outdoor moving head with VELLO's smart-glass electronic frost in place of a mechanical frost flag. 1000 W max draw.",
    ipRated=True,
    imageUrl=IMG_BASE + "led-storm-2500ip.png",
))

new.append(f(
    model="LED Storm 3500 IP",
    category="Wash", variant="",
    applications=["Touring","Install","Concert"],
    tier="Large", lampType="LED", watts=None,
    colorMixing="RGBW",
    framing=False,
    effectsRaw="High-power RGBW strobe with segmented pixel control; outdoor IP-rated housing",
    ipRating="IP65",
    powerConsumption=1500,
    protocols="DMX",
    standout="RGBW strobe with segmented pixel control\n1500W outdoor wash",
    lamp="LED",
    link="https://www.vellolight.com/product/outdoor-led-moving-storm-light-3500-ip/",
    description="Larger Storm-series outdoor moving wash with a powerful RGBW engine and segmented pixel control over the strobe layer. 1500 W max draw in an IP-rated body.",
    ipRated=True,
    imageUrl=IMG_BASE + "led-storm-3500ip.png",
))

new.append(f(
    model="LED TOP Wash P4",
    category="Wash", variant="",
    applications=["Touring","Install","Concert"],
    tier="Medium", lampType="LED", watts=None,
    colorMixing="RGBW",
    framing=False,
    effectsRaw="44 × 15W Cree RGBW 4-in-1 LEDs; high-power output wash",
    ipRating="IP20",
    powerConsumption=700,
    protocols="DMX",
    standout="44-cell Cree RGBW wash — high-power output",
    lamp="44 × 15W Cree RGBW",
    link="https://www.vellolight.com/product/led-moving-head-light-led-top-p4/",
    description="High-power wash fixture using 44 × 15 W Cree RGBW 4-in-1 LEDs. Aimed at large concerts and events where bulk RGBW output matters.",
    imageUrl=IMG_BASE + "led-top-p4.png",
))


# ----- Assign IDs and apply -----

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

print(f"Added {len(new)} VELLO fixtures. New total: {len(data)}. Next id: {next_id}")
