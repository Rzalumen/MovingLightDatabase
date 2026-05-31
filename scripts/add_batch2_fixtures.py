#!/usr/bin/env python3
"""
Batch 2 fixture additions: Chauvet + Claypaky + GLP + High End Systems gaps.
Run from repo root: python3 scripts/add_batch2_fixtures.py
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

# ---------------- CHAUVET ----------------

new.append(f(
    brand="Chauvet", model="Maverick Storm 1 Spot",
    category="Spot", variant="",
    applications=["Touring","Install","Concert"],
    tier="Medium", lampType="LED", watts=480,
    cct="6604K",
    outputLumens=14500, cri=None,
    zoomMin=7.1, zoomMax=51, zoomRatio="1:7", zoomRaw="7.1° - 51°",
    colorMixing="CMY + CTO",
    framing=False,
    gobo="1 rotating + 1 static",
    animationWheel=True, prism=True, iris=True, frost=True,
    effectsRaw="5-facet rotating prism, light + medium frost, iris, animation wheel; SunShield optical protection",
    ipRating="IP65",
    protocols="DMX, RDM, Art-Net, sACN, W-DMX",
    standout="Compact IP65 cool-white spot — 14,500 lm",
    lamp="480W Cool White LED",
    link="https://chauvetprofessional.com/product/maverick-storm-1-spot/",
    description="Compact IP65 cool-white moving spot with CMY+CTO mixing, dual frost and animation in a lightweight die-cast housing. Built for touring grids and outdoor festival use.",
    dualFrost=True, ipRated=True,
))

new.append(f(
    brand="Chauvet", model="Maverick Storm 1 Hybrid",
    category="Spot", variant="",
    applications=["Touring","Install","Concert"],
    tier="Large", lampType="Discharge", watts=420,
    cct="7700K",
    outputLumens=30978, cri=None,
    zoomMin=0.9, zoomMax=36, zoomRatio="", zoomRaw="0.9°-23.7° (beam) / 1.1°-36° (spot)",
    colorMixing="CMY",
    framing=False,
    gobo="9 rotating + 17 static",
    animationWheel=True, prism=True, frost=True,
    effectsRaw="Stackable 5-facet linear + 8-facet round rotating prisms; animation wheel; heavy frost converts beam to wash",
    ipRating="IP65",
    protocols="DMX, RDM, Art-Net, sACN, W-DMX",
    standout="IP65 beam/spot/wash hybrid — 30,978 lm",
    lamp="420W Osram discharge (2500h life)",
    link="https://chauvetprofessional.com/product/maverick-storm-1-hybrid/",
    description="IP65 beam/spot/wash hybrid built around a 420 W Osram 7700 K discharge lamp. Stackable prisms, heavy frost wash mode, and 30,978 lm in a touring-ready body.",
    ipRated=True,
))

new.append(f(
    brand="Chauvet", model="Maverick Storm 1 Wash",
    category="Wash", variant="",
    applications=["Touring","Install","Concert"],
    tier="Small", lampType="LED", watts=380,
    cct="", cctRange="2800-10000K",
    outputLumens=6000, cri=None,
    zoomMin=11, zoomMax=42, zoomRatio="", zoomRaw="11° - 42°",
    colorMixing="RGBW",
    framing=False,
    effectsRaw="19 × 20W quad-colour LEDs; virtual gobo wheel with background colours; full pixel-mapping; 50,000 h LED life",
    ipRating="IP65",
    protocols="DMX, RDM, Art-Net, sACN, W-DMX, Kling-Net",
    standout="IP65 RGBW wash with pixel-mapping and virtual gobos",
    lamp="19 × 20W RGBW",
    link="https://chauvetprofessional.com/product/maverick-storm-1-wash/",
    description="Compact IP65 RGBW wash with 19 individually addressable 20 W quad-colour LEDs and a 2,800–10,000 K virtual CCT range. Pixel-mapping plus a virtual-gobo background-colour mode.",
    ipRated=True,
))

new.append(f(
    brand="Chauvet", model="Maverick Storm 2 Profile",
    category="Performance", variant="Profile",
    applications=["Touring","Install","Concert"],
    tier="Medium", lampType="LED", watts=580,
    cct="", cctRange="",
    outputLumens=28000, cri=None,
    zoomMin=5.5, zoomMax=58.6, zoomRatio="1:10", zoomRaw="5.5° - 58.6°",
    colorMixing="CMY + CTO",
    framing=True,
    gobo="2 wheels",
    prism=True, iris=True, frost=True,
    effectsRaw="Sharp 4-blade framing shutter system; 5-facet prism; iris; frost; CRI + CTB filters; SunShield power-down lens protection",
    weightKg=31.9, ipRating="IP65",
    protocols="DMX, RDM, Art-Net, sACN, W-DMX",
    standout="IP65 framing profile — 28,000 lm in 31.9 kg",
    lamp="580W Cool White LED",
    link="https://chauvetprofessional.com/product/maverick-storm-2-profile/",
    description="IP65 framing profile with a 580 W cool-white LED engine producing 28,000 lm. Full framing shutters, dual gobos and a 5.5°–58.6° zoom; SunShield optical protection when powered down.",
    ipRated=True,
))

new.append(f(
    brand="Chauvet", model="Maverick Storm 4 Profile",
    category="Performance", variant="Profile",
    applications=["Touring","Install","Concert"],
    tier="Large", lampType="LED", watts=1250,
    cct="",
    outputLumens=None, cri=None,
    zoomMin=None, zoomMax=None, zoomRatio="1:8.5", zoomRaw="",
    colorMixing="CMY + CTO",
    framing=True,
    gobo="2 rotating",
    prism=True,
    effectsRaw="4-blade framing with rotation; 5-facet round + linear prisms; integrated SunShield",
    ipRating="IP65",
    protocols="DMX, RDM, Art-Net, sACN, W-DMX",
    standout="Top-of-line IP65 1250W profile",
    lamp="1250W LED",
    link="https://www.chauvetprofessional.com/products/maverick-storm-4-profile/",
    description="Flagship IP65 1250 W LED profile with 4-blade framing, dual rotating gobo wheels and stackable round + linear prisms.",
    ipRated=True,
))

new.append(f(
    brand="Chauvet", model="Maverick Storm 4 SoloWash",
    category="Wash", variant="",
    applications=["Touring","Install","Concert"],
    tier="Large", lampType="LED", watts=1250,
    cct="7500K",
    outputLumens=78300, cri=None,
    zoomMin=7.1, zoomMax=74.1, zoomRatio="1:9.5", zoomRaw="7.1° - 74.1°",
    colorMixing="CMY + CTO",
    framing=True,
    gobo="Rotating + interchangeable geometric gobos",
    animationWheel=True, iris=True, frost=True,
    effectsRaw="Framing shutters, animation wheel, frost, iris, independent colour wheel with CRI + CTB filters",
    ipRating="IP65",
    protocols="DMX, RDM, Art-Net, sACN, W-DMX",
    standout="78,300 lm IP65 single-source wash — stadium-scale\nFraming shutters on a wash fixture",
    lamp="1250W LED",
    link="https://chauvetprofessional.com/product/maverick-storm-4-solowash/",
    description="Stadium-class IP65 1250 W LED wash delivering 78,300 lm — Chauvet's biggest single-source wash. Includes framing shutters (unusual for a wash) and a 9.5:1 zoom.",
    ipRated=True,
))

new.append(f(
    brand="Chauvet", model="Maverick Silens 2 Profile",
    category="Performance", variant="Profile",
    applications=["Theater","TV-Film","Corporate","Install"],
    tier="Medium", lampType="LED", watts=560,
    cct="",
    outputLumens=10000, cri=95, criRaw="CRI 95+",
    zoomMin=5, zoomMax=50, zoomRatio="1:10", zoomRaw="5° - 50°",
    colorMixing="CMY + CTO + ± green",
    framing=True,
    gobo="1 rotating + 1 static",
    prism=True, frost=True,
    effectsRaw="100% convection cooled — fan-free; emulated red-shift for tungsten punch; 4-blade framing with ±60° rotation",
    weightKg=34.4, ipRating="IP20",
    protocols="DMX, RDM, Art-Net, sACN, CRMX",
    standout="100% silent — no fans\nCRI 95+ engine for theatre/broadcast",
    lamp="560W LED",
    link="https://chauvetprofessional.com/product/maverick-silens-2-profile/",
    description="Fan-free 560 W LED framing profile aimed at theatres and broadcast studios. CRI 95+ engine with ± green trim, emulated red-shift for tungsten warmth, and ±60° framing-frame rotation.",
))

new.append(f(
    brand="Chauvet", model="Maverick Force 1 Spot",
    category="Spot", variant="",
    applications=["Touring","Install"],
    tier="Medium", lampType="LED", watts=470,
    cct="7500K",
    outputLumens=20000, cri=None,
    zoomMin=7, zoomMax=50, zoomRatio="1:7", zoomRaw="7° - 50°",
    colorMixing="CMY + CTO",
    framing=False,
    gobo="Custom glass rotating + static",
    animationWheel=True, prism=True, iris=True, frost=True,
    effectsRaw="Continuous animation wheel; 5-facet rotating prism; motorised iris/zoom/focus/frost; CTB + CRI colour-wheel filters",
    weightKg=22.7, ipRating="IP20",
    protocols="DMX, RDM, Art-Net, sACN, W-DMX",
    standout="Compact under-50 lb spot — 20,000 lm",
    lamp="470W Cool White LED",
    link="https://chauvetprofessional.com/product/maverick-force-1-spot/",
    description="Compact 470 W cool-white LED moving spot delivering 20,000 lm in a sub-50 lb body. Custom glass gobos, continuous animation wheel and full effects suite.",
))

new.append(f(
    brand="Chauvet", model="Maverick Force 2 Profile",
    category="Performance", variant="Profile",
    applications=["Touring","Install","Theater"],
    tier="Medium", lampType="LED", watts=580,
    cct="",
    outputLumens=20000, cri=None,
    zoomMin=7, zoomMax=55, zoomRatio="1:8", zoomRaw="7° - 55°",
    colorMixing="CMY + CTO",
    framing=True,
    gobo="2 rotating",
    prism=True,
    effectsRaw="4-blade framing with 120° rotation; dual stackable rotating gobo wheels; 5-facet prism",
    ipRating="IP20",
    protocols="DMX, RDM, Art-Net, sACN, W-DMX",
    standout="20,000 lm framing profile under 60 lb",
    lamp="580W Cool White LED",
    link="https://chauvetprofessional.com/product/maverick-force-2-profile/",
    description="580 W cool-white LED framing profile delivering 20,000 lm. 4-blade framing with 120° rotation, dual stackable gobo wheels and a 1:8 zoom in a sub-60 lb body.",
))

new.append(f(
    brand="Chauvet", model="Maverick Force X Profile",
    category="Performance", variant="Profile",
    applications=["TV-Film","Touring","Install"],
    tier="Medium", lampType="LED", watts=520,
    cct="",
    outputLumens=19640, cri=72, criRaw="CRI 72.2 (87.6 with filter)",
    zoomMin=3.3, zoomMax=58.5, zoomRatio="1:17", zoomRaw="3.3° - 58.5°",
    colorMixing="CMY",
    framing=True,
    gobo="1 rotating + 1 static",
    prism=True, frost=True,
    effectsRaw="4-blade dual-axis framing; 5-facet prism; frost; 145 mm front lens; selectable 600 / 1500 / 2000 / 65000 Hz PWM for camera work",
    protocols="DMX, RDM, Art-Net, sACN, CRMX",
    standout="65 kHz PWM — built for high-speed sensors/cameras\n1:17 zoom range",
    lamp="520W LED",
    link="https://chauvetprofessional.com/product/maverick-force-x-profile/",
    description="520 W LED profile engineered around camera workflows: selectable PWM up to 65 kHz for flicker-free sensors and LED walls, dual-axis 4-blade framing, and a 17:1 zoom in a 145 mm front lens.",
))

new.append(f(
    brand="Chauvet", model="Maverick Force X Spot",
    category="Spot", variant="",
    applications=["TV-Film","Touring","Install"],
    tier="Medium", lampType="LED", watts=520,
    cct="",
    outputLumens=17325, cri=None,
    zoomMin=3.5, zoomMax=57.7, zoomRatio="1:18", zoomRaw="3.5° - 57.7°",
    colorMixing="CMY",
    framing=False,
    gobo="2 wheels",
    prism=True, frost=True,
    effectsRaw="Dual gobo wheels; 5-facet prism; frost; 65 kHz PWM",
    protocols="DMX, RDM, Art-Net, sACN, CRMX",
    standout="1:18 zoom with 65 kHz PWM for cameras",
    lamp="520W LED",
    link="https://chauvetprofessional.com/product/maverick-force-x-spot/",
    description="Non-framing sibling to the Force X Profile. Same 520 W engine and high-speed PWM, with an 18:1 zoom and dual gobo wheels.",
))

new.append(f(
    brand="Chauvet", model="STRIKE V",
    category="Bar / Batten", variant="",
    applications=["Touring","Install","Concert"],
    tier="Medium", lampType="LED", watts=None,
    cct="",
    outputLumens=None, cri=None,
    zoomMin=9.9, zoomMax=105.7, zoomRatio="", zoomRaw="9.9° - 105.7°",
    colorMixing="RGBW (per-pixel)",
    framing=False,
    effectsRaw="48 individually controllable RGBW LEDs in dual layers — 24×6W top + 24×50W bottom; 180° motorised tilt; variable electronic frost; magnetic stealth filter to conceal pixels off-state",
    ipRating="IP65",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="Dual-layer motorised strobe/wash — 180° tilt\nMagnetic stealth filter conceals pixels off-state",
    lamp="24 × 6W + 24 × 50W RGBW",
    link="https://chauvetprofessional.com/product/strike-v/",
    description="IP65 motorised strobe/wash hybrid with two layers of RGBW pixels (24 × 6 W up top, 24 × 50 W on the bottom plate) on a 180° tilt yoke. Variable electronic frost and a magnetic stealth filter for off-state concealment.",
    ipRated=True,
))

new.append(f(
    brand="Chauvet", model="Rogue Outcast 2 Beam",
    category="Spot", variant="",
    applications=["Touring","Install"],
    tier="Medium", lampType="Discharge", watts=300,
    cct="8000K",
    outputLumens=None, cri=None, criRaw="204,855 lx @ 49.2'",
    zoomMin=0.8, zoomMax=1.6, zoomRatio="", zoomRaw="Beam 0.8° / Field 1.6°",
    colorMixing="None (colour wheels)",
    framing=False,
    gobo="17 static + continuous scroll",
    prism=True, frost=True,
    effectsRaw="8-facet + 5-facet rotating prisms; motorised focus; 14 colours + white solid/split/scroll",
    weightKg=20.5, ipRating="IP65",
    protocols="DMX, RDM",
    standout="IP65 sub-1° beam — single-lamp pure beam fixture",
    lamp="300W NSL Ushio discharge",
    link="https://chauvetprofessional.com/product/rogue-outcast-2-beam/",
    description="IP65 pure-beam fixture: a 300 W Ushio discharge lamp produces a 0.8° beam at 204,855 lx @ 49.2'. 17 static gobos with continuous scroll, dual prisms, in a 20.5 kg body.",
    ipRated=True,
))

new.append(f(
    brand="Chauvet", model="Rogue Outcast 3 Spot",
    category="Spot", variant="",
    applications=["Touring","Install"],
    tier="Medium", lampType="LED", watts=None,
    cct="",
    outputLumens=None, cri=None,
    zoomMin=4.9, zoomMax=38.7, zoomRatio="", zoomRaw="4.9° - 38.7°",
    colorMixing="CMY + CTO",
    framing=False,
    gobo="2 wheels",
    prism=True, iris=True, frost=True,
    effectsRaw="Dual colour wheels; dual gobo wheels; prism, iris, frost",
    ipRating="IP65",
    protocols="DMX, RDM",
    standout="Compact IP65 LED spot — wide 1:8 zoom",
    lamp="LED",
    link="https://chauvetprofessional.com/product/rogue-outcast-3-spot/",
    description="Compact IP65 LED moving spot in the Rogue Outcast line with dual colour wheels, dual gobo wheels and a full prism/iris/frost set.",
    ipRated=True,
))

# ---------------- CLAYPAKY ----------------

new.append(f(
    brand="Claypaky", model="Sharpy Plus",
    category="Spot", variant="",
    applications=["Touring","Install","Concert"],
    tier="Medium", lampType="Discharge", watts=330,
    cct="",
    outputLumens=None, cri=None, criRaw="300,000 lx @ 10 m",
    zoomMin=3, zoomMax=36, zoomRatio="1:12", zoomRaw="3° - 36°",
    colorMixing="CMY",
    framing=False,
    gobo="8 rotating + 18 static",
    animationWheel=True, prism=True,
    effectsRaw="3 colour wheels (15 colours) + 2 CTO; 4-facet + 8-facet rotating prisms; animation wheel; linear soft-edge frost",
    weightKg=23, ipRating="IP20",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="Sharpy DNA evolved with CMY + 12:1 zoom\n300,000 lx @ 10 m",
    lamp="330W Osram Sirius HRI X8 (1500h)",
    link="https://www.claypaky.it/products/sharpy-plus/",
    description="Evolution of the original Sharpy with the same razor-thin beam character but a 330 W Sirius HRI X8 lamp, full CMY mixing and a 3°–36° zoom in 23 kg.",
))

new.append(f(
    brand="Claypaky", model="Sharpy X Frame",
    category="Performance", variant="",
    applications=["Touring","Install","Theater"],
    tier="Medium", lampType="Discharge", watts=550,
    cct="8000K",
    outputLumens=18800, cri=None, criRaw="432,000 lx @ 10 m",
    zoomMin=2, zoomMax=52, zoomRatio="", zoomRaw="3°-52° (spot) / 2°-29° (beam)",
    colorMixing="Linear CMY + linear CTO",
    framing=True,
    gobo="8 HD rotating + 18 static",
    animationWheel=True, prism=True, iris=True, frost=True,
    effectsRaw="14 dichroic colour wheel; 4-blade framing system; 4-facet + 8-facet rotating prisms; linear heavy frost (wash mode); animation wheel; motorised iris/zoom/focus",
    ipRating="IP20",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="Sharpy with framing shutters\n550W discharge — 432,000 lx @ 10 m",
    lamp="550W Philips MSD 25R",
    link="https://www.claypaky.it/products/sharpy-xframe/",
    description="Adds a 4-blade framing system to the Sharpy formula. 550 W Philips 25R, 18,800 lm and zoom ranges of 3°–52° (spot) / 2°–29° (beam) with linear CMY/CTO and HD glass gobos.",
))

new.append(f(
    brand="Claypaky", model="Axcor Profile 600",
    category="Performance", variant="Profile",
    applications=["Theater","Touring","TV-Film"],
    tier="Medium", lampType="LED", watts=500,
    cct="6500K", cctRange="",
    outputLumens=18100, cri=None, criRaw="HC version CRI ~90 (5600K, 11,500 lm)",
    zoomMin=5.3, zoomMax=47.2, zoomRatio="1:9", zoomRaw="5.3° - 47.2°",
    colorMixing="CMY + linear CTO",
    framing=True,
    gobo="7 rotating",
    animationWheel=True, prism=True, iris=True, frost=True,
    effectsRaw="4-plane motorised framing; 5-colour wheel; 4-facet rotating prism; interchangeable animation wheel; variable frost; high-precision iris",
    ipRating="IP20",
    dmxChannels="40 / 44",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="High-output + High-CRI engine variants\n4-plane framing",
    lamp="500W White LED",
    link="https://www.claypaky.it/products/axcor-profile-600/",
    description="500 W LED framing profile available in high-output (6500 K) or high-CRI Teatro (5600 K, ~CRI 90) engine variants. 4-plane motorised framing, full effects suite, 5.3°–47.2° zoom.",
))

new.append(f(
    brand="Claypaky", model="Sinfonya Profile 600",
    category="Performance", variant="Profile",
    applications=["Theater","Touring","Corporate","Install"],
    tier="Medium", lampType="LED", watts=600,
    cct="",
    outputLumens=12050, cri=95, criRaw="CRI up to 95",
    zoomMin=5, zoomMax=60, zoomRatio="1:12", zoomRaw="5° - 60°",
    colorMixing="RGBAL",
    framing=True,
    gobo="1 rotating wheel (6 HD indexable, replaceable)",
    iris=True, frost=True,
    effectsRaw="ACCUFRAME 4-blade framing system on 2 focal planes (40× the precision of traditional framing); LINEGUARD opposing frost flags; 16-blade motorised iris; pan/tilt absolute position",
    weightKg=36.8,
    protocols="DMX, RDM, Art-Net, sACN, LumenRadio (optional)",
    standout="ACCUFRAME — 40× framing precision\nTONEDOWN silent mode (27 dB)",
    lamp="600W RGBAL",
    link="https://www.claypaky.it/products/sinfonya-profile-600/",
    description="600 W RGBAL LED framing profile with Claypaky's ACCUFRAME 2-plane framing system (40× the precision of a traditional shutter assembly) and a TONEDOWN silent mode at 27 dB. 160 mm front lens.",
))

new.append(f(
    brand="Claypaky", model="Skylos",
    category="Spot", variant="",
    applications=["Install","Touring"],
    tier="Medium", lampType="Laser", watts=300,
    cct="10000K",
    outputLumens=10717, cri=None,
    zoomMin=0.5, zoomMax=5, zoomRatio="1:10", zoomRaw="0.5° - 5°",
    colorMixing="None (15-colour wheel)",
    framing=False,
    prism=True, frost=True,
    effectsRaw="15-colour wheel; rotating 6-facet + 5-facet linear + fixed 4-facet prism (moonflower stack); 5° frost; 24-bit dimmer; sealed white-laser engine 30,000 h",
    powerConsumption=600, ipRating="IP66",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="300W white laser searchlight — 4000W Xenon equivalent\nIP66 / -40°C operating; C5-M marine grade",
    lamp="300W Sealed white-laser engine",
    link="https://www.claypaky.it/products/skylos/",
    description="IP66 white-laser searchlight delivering the output of a 4000 W Xenon at 600 W. 300 mm front lens, 0.5°–5° beam, 30,000 h source life and operation down to −40 °C with internal heating.",
    ipRated=True,
))

new.append(f(
    brand="Claypaky", model="Volero Wave",
    category="Bar / Batten", variant="",
    applications=["Touring","Install","Concert"],
    tier="Small", lampType="LED", watts=320,
    cct="", cctRange="2500-8000K",
    outputLumens=None, cri=None,
    zoomMin=2.9, zoomMax=2.9, zoomRatio="", zoomRaw="2.9° fixed beam",
    colorMixing="RGBW",
    framing=False,
    effectsRaw="8 independent moving heads on one batten; each 40W RGBW + mirror-based optic; 220° tilt per head; linear CTC 2500-8000K; 24-bit dimming; high-speed strobe",
    ipRating="IP20",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="Batten of 8 mirror-optic moving beams\n2.9° collimated parallel-beam output",
    lamp="8 × 40W RGBW",
    link="https://www.claypaky.it/products/volero-wave/",
    description="Eight independently moving 40 W RGBW heads on one batten, each producing a 2.9° collimated parallel beam through a mirror-based optical system. 220° tilt per head.",
))

# ---------------- GLP ----------------

new.append(f(
    brand="GLP", model="impression X5 IP Bar",
    category="Bar / Batten", variant="",
    applications=["Touring","Install","Concert"],
    tier="Medium", lampType="LED", watts=720,
    cct="", cctRange="2500-10000K",
    outputLumens=7500, cri=None,
    zoomMin=4.5, zoomMax=60, zoomRatio="", zoomRaw="4.5° - 60°",
    colorMixing="RGBL",
    framing=False,
    effectsRaw="18 × 40W RGBL pixels; motorised tilt; per-pixel control",
    weightKg=27, ipRating="IP65",
    powerConsumption=750,
    protocols="DMX, RDM, Art-Net, sACN",
    standout="IP65 18-cell RGBL bar — full pixel control",
    lamp="18 × 40W RGBL",
    link="https://www.glp.de/en/products/moving-lights-led/impression-x5-ip-bar",
    description="IP65 motorised batten in the X5 family with 18 RGBL pixels (40 W each), 7,500 lm output and a 4.5°–60° zoom. 27 kg body with per-pixel mapping.",
    ipRated=True,
))

new.append(f(
    brand="GLP", model="impression X5 IP Maxx",
    category="Wash", variant="",
    applications=["Touring","Install","Concert"],
    tier="Large", lampType="LED", watts=1500,
    cct="", cctRange="2500-10000K",
    outputLumens=24000, cri=None,
    zoomMin=3.5, zoomMax=66, zoomRatio="1:19", zoomRaw="3.5° - 66°",
    colorMixing="RGBL",
    framing=False,
    effectsRaw="37 × 40W RGBL pixels; per-pixel mapping; auto-ranging 100-240V supply",
    weightKg=35, ipRating="IP65",
    powerConsumption=1500,
    protocols="DMX, RDM, Art-Net, sACN",
    standout="37-pixel RGBL wash — 24,000 lm\nIP65 with 19:1 zoom",
    lamp="37 × 40W RGBL",
    link="https://www.glp.de/en/products/moving-lights-led/x5-maxx",
    description="Top-of-line IP65 X5 wash with 37 individually addressable 40 W RGBL pixels, 24,000 lm output and a 19:1 zoom from 3.5°–66°.",
    ipRated=True,
))

new.append(f(
    brand="GLP", model="impression FR10",
    category="Bar / Batten", variant="",
    applications=["Touring","Install","Concert"],
    tier="Small", lampType="LED", watts=600,
    cct="", cctRange="2500-10000K",
    outputLumens=8000, cri=None,
    zoomMin=3.7, zoomMax=34, zoomRatio="1:7", zoomRaw="3.7° - 34°",
    colorMixing="RGBW",
    framing=False,
    effectsRaw="10 × 60W RGBW; 643° pan / 210° tilt with 16-bit position feedback; homogenised Fresnel lens",
    powerConsumption=740,
    protocols="DMX, RDM, Art-Net, sACN",
    standout="Moving batten with 643° pan range\nHomogenised Fresnel optic",
    lamp="10 × 60W RGBW",
    link="https://www.germanlightproducts.com/product/impression-fr10-bar/",
    description="Moving batten with 10 × 60 W RGBW sources behind a homogenised Fresnel optic. 643° pan, 210° tilt, 16-bit position feedback, 8,000 lm.",
))

# ---------------- HIGH END SYSTEMS ----------------

new.append(f(
    brand="High End Systems", model="SolaFrame Theatre",
    category="Performance", variant="Performance",
    applications=["Theater","TV-Film","Install"],
    tier="Medium", lampType="LED", watts=440,
    cct="",
    outputLumens=16200, cri=None, criRaw="High CRI engine",
    zoomMin=7, zoomMax=42, zoomRatio="1:6", zoomRaw="7° - 42°",
    colorMixing="CMY + linear CTO",
    framing=True,
    gobo="Fixed + indexing rotating",
    animationWheel=True, prism=True, iris=True, frost=True,
    effectsRaw="Fanless silent operation; 4-plane framing shutters; animation effects; iris; frost; prism; 50,000 h L70 LED life",
    weightKg=50.4, ipRating="IP20",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="First fanless silent automated luminaire\nCRI-tuned 440W engine — 16,200 lm",
    lamp="440W High CRI LED",
    link="https://www.highend.com/products/lighting/solaframe",
    description="The first fanless, silent automated luminaire. 440 W high-CRI LED engine delivers 16,200 lm with full 4-plane framing and the SolaSpot family's effects package.",
))

new.append(f(
    brand="High End Systems", model="SolaSpot 1000",
    category="Spot", variant="",
    applications=["Theater","Touring","Install"],
    tier="Medium", lampType="LED", watts=440,
    cct="6900K",
    outputLumens=18000, cri=None,
    zoomMin=11, zoomMax=48, zoomRatio="1:4", zoomRaw="11° - 48°",
    colorMixing="CMY + CTO",
    framing=False,
    gobo="Fixed wheel + 1 rotating animation",
    animationWheel=True, prism=True, iris=True, frost=True,
    effectsRaw="Rotating animation wheel; fixed gobo wheel; fixed colour wheel; iris; frost; prism",
    ipRating="IP20",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="440W Ultra-Bright engine — 18,000 lm",
    lamp="440W Ultra-Bright White LED",
    link="https://www.etcconnect.com/Products/Legacy/Live-Events-High-End-Systems/Lighting-Fixtures/SolaSpot/1000/Features.aspx",
    description="440 W Ultra-Bright white LED spot with rotating animation wheel, CMY/CTO mixing and an 11°–48° zoom. 18,000 lm.",
))

new.append(f(
    brand="High End Systems", model="SolaSpot 2000",
    category="Spot", variant="",
    applications=["Theater","Touring","Install"],
    tier="Medium", lampType="LED", watts=600,
    cct="6900K",
    outputLumens=25000, cri=None,
    zoomMin=8, zoomMax=38, zoomRatio="", zoomRaw="8° - 38°",
    colorMixing="CMY + CTO",
    framing=False,
    gobo="6 interchangeable rotating + open",
    prism=True, iris=True, frost=True,
    effectsRaw="6-position colour wheel + open with bi-directional rainbow; CMY + CTO; iris; frost; prism",
    ipRating="IP20",
    dmxChannels="43",
    protocols="DMX, RDM",
    standout="600W Bright White — 25,000 lm",
    lamp="600W Bright White LED",
    link="https://www.highend.com/products/lighting/solaspot",
    description="600 W Bright White LED spot with 6 interchangeable rotating gobos, CMY + CTO mixing and a 25,000 lm output. 540° pan / 265° tilt.",
))

new.append(f(
    brand="High End Systems", model="SolaWash 1000",
    category="Wash", variant="",
    applications=["Touring","Install","Theater"],
    tier="Medium", lampType="LED", watts=None,
    cct="",
    outputLumens=20000, cri=None,
    zoomMin=12, zoomMax=55, zoomRatio="1:5", zoomRaw="12° - 55°",
    colorMixing="CMY + linear CTO",
    framing=True,
    iris=True, frost=True,
    effectsRaw="Full framing shutter system (unusual for wash); 7-position replaceable colour wheel; iris; dual linear frost (medium/heavy); TM-30 filter pushes Ultra-Bright engine to CRI 85+",
    ipRating="IP20",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="Wash with full framing shutters\n20,000 lm Ultra-Bright with TM-30 to CRI 85+",
    lamp="LED (Ultra-Bright / High-CRI engines)",
    link="https://www.etcconnect.com/Products/Legacy/Live-Events-High-End-Systems/Lighting-Fixtures/SolaWash/1000/Features.aspx",
    description="LED wash with full framing shutters and dual linear frost. Two engine options (Ultra-Bright 20,000 lm or High-CRI), with a TM-30 filter that pushes the Ultra-Bright to CRI 85+.",
    dualFrost=True,
))

new.append(f(
    brand="High End Systems", model="SolaWash 2000",
    category="Wash", variant="",
    applications=["Touring","Install","Theater"],
    tier="Large", lampType="LED", watts=600,
    cct="",
    outputLumens=20000, cri=None, criRaw="Ultra-Bright; High-CRI engine option (6500K or 3200K)",
    zoomMin=None, zoomMax=None, zoomRatio="", zoomRaw="",
    colorMixing="CMY + linear CTO",
    framing=True,
    iris=True, frost=True,
    effectsRaw="Full curtain 4-blade framing; dual linear diffusion; CMY + linear CTO",
    ipRating="IP20",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="Big-brother wash with framing — 600W engine",
    lamp="600W LED",
    link="https://www.etcconnect.com/Products/Legacy/Live-Events-High-End-Systems/Lighting-Fixtures/SolaWash/2000/Features.aspx",
    description="Larger sibling to the SolaWash 1000: 600 W LED engine, dual linear diffusion, and a 4-blade curtain framing system. Ultra-Bright or High-CRI (6500 K / 3200 K) variants.",
    dualFrost=True,
))

new.append(f(
    brand="High End Systems", model="TurboRay",
    category="Wash", variant="",
    applications=["Touring","Concert","Install"],
    tier="Small", lampType="LED", watts=240,
    cct="", cctRange="2800-8000K",
    outputLumens=6000, cri=None,
    zoomMin=3, zoomMax=24, zoomRatio="1:8", zoomRaw="3° - 24°",
    colorMixing="RGBW + deep red + blue dichroic",
    framing=False,
    gobo="Animated gobo",
    effectsRaw="4 × 60W Osram Ostar RGBW; radial diffuser; animated gobo; split colours; Hazefree lens coating",
    protocols="DMX, RDM, Art-Net, sACN",
    standout="Hazefree lens coating preserves beam quality in haze\nDeep-red + blue dichroic extend RGBW palette",
    lamp="4 × 60W Osram Ostar RGBW",
    link="https://www.etcconnect.com/Products/Legacy/Live-Events-High-End-Systems/Lighting-Fixtures/Effects/TurboRay/Features.aspx",
    description="Compact RGBW wash/beam hybrid with 4 × 60 W Osram Ostar LEDs in a square configuration. Adds deep-red and blue dichroics for extended palette, plus a Hazefree lens coating for haze-heavy stages.",
))

# Assign IDs and skip duplicates
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
