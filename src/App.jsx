import React, { useState, useMemo, useEffect } from "react";
import { Search, X, GitCompare, Lightbulb, ChevronDown, ChevronUp, Check, SlidersHorizontal, Plus, Minus, ExternalLink, Scissors } from "lucide-react";

import FIXTURES from "./fixtures.json";

const CAT_COLORS = { "Spot / Profile": "#e8b339", "Wash": "#5ab7d4", "Bar / Batten": "#c77dff" };
const LAMP_COLORS = { "LED": "#6ee7a8", "Discharge": "#f4a259", "Laser": "#ff6b6b", "Other": "#9aa5b1" };
const APP_COLORS = { "Touring": "#f4a259", "Theater": "#e8b339", "TV-Film": "#ff6b9d", "Install": "#5ab7d4", "Corporate": "#9d8df1" };
const TIER_COLORS = { "Small": "#7dd3a0", "Medium": "#e8b339", "Large": "#f4845f" };
const TIER_DESC = { "Small": "< 10k lm", "Medium": "10\u201330k lm", "Large": "\u2265 30k lm" };
const CRI_BANDS = [{ label: "90+", min: 90 }, { label: "80+", min: 80 }, { label: "70+", min: 70 }];

function clean(s) { return (s || "").replace(/\s+/g, " ").trim(); }
function fmt(n) { return n == null ? "\u2014" : n.toLocaleString(); }
function zoomStr(f) { return f.zoomMin != null ? (f.zoomMin === f.zoomMax ? f.zoomMin + "\u00b0" : f.zoomMin + "\u00b0\u2013" + f.zoomMax + "\u00b0") : "\u2014"; }

export default function App() {
  const [query, setQuery] = useState("");
  const [apps, setApps] = useState(new Set());
  const [cats, setCats] = useState(new Set());
  const [tiers, setTiers] = useState(new Set());
  const [brands, setBrands] = useState(new Set());
  const [lamps, setLamps] = useState(new Set());
  const [criMin, setCriMin] = useState(0);
  const [featFraming, setFeatFraming] = useState(false);
  const [featAnim, setFeatAnim] = useState(false);
  const [featUsed, setFeatUsed] = useState(false);
  const [sortBy, setSortBy] = useState("output-desc");
  const [moreOpen, setMoreOpen] = useState(false);
  const [expanded, setExpanded] = useState(new Set());
  const [compare, setCompare] = useState([]);
  const [showCompare, setShowCompare] = useState(false);
  const [isMobile, setIsMobile] = useState(false);

  useEffect(() => {
    const c = () => setIsMobile(window.innerWidth < 760);
    c(); window.addEventListener("resize", c);
    return () => window.removeEventListener("resize", c);
  }, []);

  const allBrands = useMemo(() => [...new Set(FIXTURES.map(f => f.brand))].sort(), []);
  const allApps = ["Touring", "Theater", "TV-Film", "Install", "Corporate"];
  const allCats = ["Spot / Profile", "Wash", "Bar / Batten"];
  const allTiers = ["Small", "Medium", "Large"];
  const allLamps = ["LED", "Discharge", "Laser", "Other"];

  function toggle(set, setter, val) {
    const n = new Set(set);
    n.has(val) ? n.delete(val) : n.add(val);
    setter(n);
  }

  const hasActiveFilter = query || apps.size || cats.size || tiers.size || brands.size || lamps.size || criMin || featFraming || featAnim || featUsed;
  const moreCount = brands.size + lamps.size + (criMin?1:0) + (featFraming?1:0) + (featAnim?1:0) + (featUsed?1:0);

  const filtered = useMemo(() => {
    if (!hasActiveFilter) return [];
    let r = FIXTURES.filter(f => {
      if (query) {
        const q = query.toLowerCase();
        const hay = (f.model + " " + f.brand + " " + f.category + " " + (f.unique||"") + " " + (f.description||"") + " " + (f.colorMixing||"") + " " + (f.lamp||"") + " " + (f.applications||[]).join(" ")).toLowerCase();
        if (!hay.includes(q)) return false;
      }
      if (apps.size && !(f.applications||[]).some(a => apps.has(a))) return false;
      if (cats.size && !cats.has(f.category)) return false;
      if (tiers.size && !tiers.has(f.tier)) return false;
      if (brands.size && !brands.has(f.brand)) return false;
      if (lamps.size && !lamps.has(f.lampType)) return false;
      if (criMin && !(f.cri != null && f.cri >= criMin)) return false;
      if (featFraming && !f.framing) return false;
      if (featAnim && !f.animationWheel) return false;
      if (featUsed && !f.everUsed) return false;
      return true;
    });
    const [key, dir] = sortBy.split("-");
    r = [...r].sort((a, b) => {
      let av, bv;
      if (key === "output") { av = a.outputLumens || 0; bv = b.outputLumens || 0; }
      else if (key === "watts") { av = a.watts || 0; bv = b.watts || 0; }
      else if (key === "cri") { av = a.cri || 0; bv = b.cri || 0; }
      else if (key === "zoom") { av = a.zoomMin || 999; bv = b.zoomMin || 999; }
      else { av = a.model.toLowerCase(); bv = b.model.toLowerCase(); }
      if (av < bv) return dir === "asc" ? -1 : 1;
      if (av > bv) return dir === "asc" ? 1 : -1;
      return 0;
    });
    return r;
  }, [query, apps, cats, tiers, brands, lamps, criMin, featFraming, featAnim, featUsed, sortBy, hasActiveFilter]);

  function toggleExpand(id) {
    const n = new Set(expanded);
    n.has(id) ? n.delete(id) : n.add(id);
    setExpanded(n);
  }
  function toggleCompare(f) {
    setCompare(c => {
      if (c.find(x => x.id === f.id)) return c.filter(x => x.id !== f.id);
      if (c.length >= 4) return c;
      return [...c, f];
    });
  }
  const inCompare = id => compare.some(x => x.id === id);
  function clearAll() {
    setQuery(""); setApps(new Set()); setCats(new Set()); setTiers(new Set());
    setBrands(new Set()); setLamps(new Set()); setCriMin(0);
    setFeatFraming(false); setFeatAnim(false); setFeatUsed(false);
  }

  return (
    <div style={{ minHeight: "100vh", background: "#0d0f12", color: "#e6e8eb", fontFamily: "'DM Sans', -apple-system, sans-serif" }}>
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap');
        * { box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
        ::-webkit-scrollbar { width: 8px; height: 8px; }
        ::-webkit-scrollbar-track { background: #16191e; }
        ::-webkit-scrollbar-thumb { background: #2e333b; border-radius: 4px; }
        input::placeholder { color: #5a6069; }
        .row-item { transition: background .1s ease; }
        @media (hover:hover) { .row-item:hover { background: #181b20 !important; } }
        .seg { transition: all .12s ease; user-select: none; }
        .seg:active { transform: scale(.97); }
        .expand { animation: exp .18s ease; }
        @keyframes exp { from { opacity: 0; } to { opacity: 1; } }
        .slide-up { animation: su .22s cubic-bezier(.2,.8,.2,1); }
        @keyframes su { from { transform: translateY(100%); } to { transform: translateY(0); } }
        a { color: inherit; }
      `}</style>

      {/* Header */}
      <div style={{ borderBottom: "1px solid #1e2228", background: "#0d0f12", position: "sticky", top: 0, zIndex: 50 }}>
        <div style={{ maxWidth: 1180, margin: "0 auto", padding: isMobile ? "12px 14px" : "16px 24px" }}>
          <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
            <div style={{ width: isMobile ? 32 : 36, height: isMobile ? 32 : 36, borderRadius: 9, background: "linear-gradient(135deg,#e8b339,#f4a259)", display: "flex", alignItems: "center", justifyContent: "center", flexShrink: 0 }}>
              <Lightbulb size={isMobile ? 18 : 20} color="#0d0f12" strokeWidth={2.5} />
            </div>
            <div style={{ flex: 1, minWidth: 0 }}>
              <div style={{ fontSize: isMobile ? 15 : 17, fontWeight: 700, letterSpacing: "-.02em" }}>Moving Light Database</div>
              <div style={{ fontSize: 10, color: "#6a7079", fontFamily: "'Space Mono', monospace" }}>{FIXTURES.length} FIXTURES {"\u00b7"} {allBrands.length} BRANDS</div>
            </div>
            {!isMobile && compare.length > 0 && (
              <button onClick={() => setShowCompare(true)}
                style={{ display: "flex", alignItems: "center", gap: 7, padding: "9px 15px", background: "linear-gradient(135deg,#e8b339,#f4a259)", color: "#0d0f12", border: "none", borderRadius: 9, fontSize: 13, fontWeight: 700, cursor: "pointer", fontFamily: "inherit" }}>
                <GitCompare size={15} /> Compare ({compare.length})
              </button>
            )}
          </div>
        </div>
      </div>

      <div style={{ maxWidth: 1180, margin: "0 auto", padding: isMobile ? "16px 14px 90px" : "22px 24px 40px" }}>

        <div style={{ position: "relative", marginBottom: 18 }}>
          <Search size={17} style={{ position: "absolute", left: 13, top: "50%", transform: "translateY(-50%)", color: "#6a7079" }} />
          <input value={query} onChange={e => setQuery(e.target.value)} placeholder="Search by model, brand, or feature..."
            style={{ width: "100%", padding: isMobile ? "12px 38px" : "13px 40px", background: "#16191e", border: "1px solid #262b32", borderRadius: 10, color: "#e6e8eb", fontSize: isMobile ? 16 : 14.5, outline: "none", fontFamily: "inherit" }} />
          {query && <X size={16} onClick={() => setQuery("")} style={{ position: "absolute", right: 13, top: "50%", transform: "translateY(-50%)", color: "#6a7079", cursor: "pointer" }} />}
        </div>

        <PrimaryFilter label="Application" items={allApps} active={apps} onToggle={v => toggle(apps, setApps, v)} colors={APP_COLORS} isMobile={isMobile} />
        <PrimaryFilter label="Type" items={allCats} active={cats} onToggle={v => toggle(cats, setCats, v)} colors={CAT_COLORS} isMobile={isMobile} />
        <PrimaryFilter label="Output Tier" items={allTiers} active={tiers} onToggle={v => toggle(tiers, setTiers, v)} colors={TIER_COLORS} sub={TIER_DESC} isMobile={isMobile} />

        <div style={{ marginBottom: 18 }}>
          <div onClick={() => setMoreOpen(o => !o)} style={{ display: "inline-flex", alignItems: "center", gap: 6, cursor: "pointer", fontSize: 12.5, color: "#9aa5b1", fontWeight: 600, padding: "4px 0" }}>
            <SlidersHorizontal size={14} /> More filters
            {moreCount > 0 && <span style={{ background: "#e8b339", color: "#0d0f12", borderRadius: 9, padding: "0px 6px", fontSize: 10.5, fontWeight: 700 }}>{moreCount}</span>}
            {moreOpen ? <ChevronUp size={14} /> : <ChevronDown size={14} />}
          </div>
          {moreOpen && (
            <div className="expand" style={{ marginTop: 12, padding: 14, background: "#13161a", border: "1px solid #1e2228", borderRadius: 11 }}>
              <div style={{ fontSize: 10.5, fontWeight: 700, color: "#7a818b", textTransform: "uppercase", letterSpacing: ".05em", marginBottom: 8 }}>Color Rendering (CRI)</div>
              <div style={{ display: "flex", gap: 7, flexWrap: "wrap", marginBottom: 4 }}>
                {CRI_BANDS.map(b => (
                  <Seg key={b.label} active={criMin === b.min} onClick={() => setCriMin(criMin === b.min ? 0 : b.min)}>CRI {b.label}</Seg>
                ))}
              </div>
              <SubFilter label="Brand" items={allBrands} active={brands} onToggle={v => toggle(brands, setBrands, v)} />
              <SubFilter label="Light Source" items={allLamps} active={lamps} onToggle={v => toggle(lamps, setLamps, v)} colors={LAMP_COLORS} />
              <div style={{ fontSize: 10.5, fontWeight: 700, color: "#7a818b", textTransform: "uppercase", letterSpacing: ".05em", margin: "12px 0 8px" }}>Features</div>
              <div style={{ display: "flex", gap: 7, flexWrap: "wrap" }}>
                <Seg active={featFraming} onClick={() => setFeatFraming(v => !v)}>Framing shutters</Seg>
                <Seg active={featAnim} onClick={() => setFeatAnim(v => !v)}>Animation wheel</Seg>
                <Seg active={featUsed} onClick={() => setFeatUsed(v => !v)}>Used before {"\u2605"}</Seg>
              </div>
            </div>
          )}
        </div>

        {!hasActiveFilter ? (
          <EmptyState isMobile={isMobile} />
        ) : filtered.length === 0 ? (
          <div style={{ textAlign: "center", padding: "70px 20px", color: "#5a6069" }}>
            <Lightbulb size={38} style={{ opacity: .3, marginBottom: 12 }} />
            <div style={{ fontSize: 15 }}>No fixtures match these filters</div>
            <button onClick={clearAll} style={{ marginTop: 14, padding: "8px 16px", background: "#16191e", border: "1px solid #262b32", borderRadius: 8, color: "#9aa5b1", fontSize: 13, cursor: "pointer", fontFamily: "inherit" }}>Clear all filters</button>
          </div>
        ) : (
          <>
            <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: 10, gap: 10 }}>
              <div style={{ fontSize: 13, color: "#9aa5b1" }}>
                <span style={{ color: "#e6e8eb", fontWeight: 700 }}>{filtered.length}</span> result{filtered.length !== 1 ? "s" : ""}
                <span onClick={clearAll} style={{ marginLeft: 12, fontSize: 12, color: "#6a7079", cursor: "pointer" }}>Clear all</span>
              </div>
              <select value={sortBy} onChange={e => setSortBy(e.target.value)}
                style={{ background: "#16191e", border: "1px solid #262b32", borderRadius: 8, color: "#e6e8eb", fontSize: 12.5, padding: "7px 9px", outline: "none", fontFamily: "inherit", cursor: "pointer" }}>
                <option value="output-desc">Output {"\u2193"}</option>
                <option value="output-asc">Output {"\u2191"}</option>
                <option value="cri-desc">CRI {"\u2193"}</option>
                <option value="watts-desc">Wattage {"\u2193"}</option>
                <option value="zoom-asc">Tightest zoom</option>
                <option value="model-asc">Model A{"\u2013"}Z</option>
              </select>
            </div>
            <div style={{ border: "1px solid #1e2228", borderRadius: 11, overflow: "hidden" }}>
              {/* column header on desktop */}
              {!isMobile && (
                <div style={{ display: "flex", alignItems: "center", gap: 14, padding: "9px 16px", background: "#101216", borderBottom: "1px solid #1e2228" }}>
                  <span style={{ width: 9 }} />
                  <div style={{ flex: 1, fontSize: 9.5, fontWeight: 700, color: "#5a6069", letterSpacing: ".06em" }}>FIXTURE</div>
                  <div style={{ width: 78, textAlign: "right", fontSize: 9.5, fontWeight: 700, color: "#5a6069", letterSpacing: ".06em" }}>OUTPUT</div>
                  <div style={{ width: 78, textAlign: "right", fontSize: 9.5, fontWeight: 700, color: "#5a6069", letterSpacing: ".06em" }}>FRAMING</div>
                  <div style={{ width: 78, textAlign: "right", fontSize: 9.5, fontWeight: 700, color: "#5a6069", letterSpacing: ".06em" }}>ZOOM</div>
                  <div style={{ width: 78, textAlign: "right", fontSize: 9.5, fontWeight: 700, color: "#5a6069", letterSpacing: ".06em" }}>CRI</div>
                  <span style={{ width: 17 }} />
                </div>
              )}
              {filtered.map((f, i) => (
                <ResultRow key={f.id} f={f} isMobile={isMobile} last={i === filtered.length - 1}
                  expanded={expanded.has(f.id)} onToggle={() => toggleExpand(f.id)}
                  inCompare={inCompare(f.id)} compareFull={compare.length >= 4} onCompare={() => toggleCompare(f)} />
              ))}
            </div>
          </>
        )}
      </div>

      {isMobile && compare.length > 0 && (
        <div style={{ position: "fixed", bottom: 0, left: 0, right: 0, background: "#13161a", borderTop: "1px solid #262b32", padding: "12px 14px", zIndex: 150, display: "flex", alignItems: "center", gap: 10 }}>
          <div style={{ fontSize: 13, color: "#9aa5b1", flex: 1 }}><span style={{ color: "#e8b339", fontWeight: 700 }}>{compare.length}</span> to compare</div>
          <button onClick={() => setCompare([])} style={{ padding: "9px 12px", background: "#1e2228", border: "none", borderRadius: 8, color: "#9aa5b1", fontSize: 13, fontWeight: 600, fontFamily: "inherit" }}>Clear</button>
          <button onClick={() => setShowCompare(true)} style={{ padding: "9px 16px", background: "linear-gradient(135deg,#e8b339,#f4a259)", border: "none", borderRadius: 8, color: "#0d0f12", fontSize: 13, fontWeight: 700, fontFamily: "inherit", display: "flex", alignItems: "center", gap: 6 }}>
            <GitCompare size={14} /> Compare
          </button>
        </div>
      )}

      {showCompare && <CompareModal items={compare} isMobile={isMobile} onClose={() => setShowCompare(false)} onRemove={id => setCompare(c => c.filter(x => x.id !== id))} />}
    </div>
  );
}

function PrimaryFilter({ label, items, active, onToggle, colors, sub, isMobile }) {
  return (
    <div style={{ marginBottom: 12 }}>
      <div style={{ fontSize: 10.5, fontWeight: 700, color: "#7a818b", textTransform: "uppercase", letterSpacing: ".06em", marginBottom: 7 }}>{label}</div>
      <div style={{ display: "flex", gap: 7, flexWrap: "wrap" }}>
        {items.map(it => {
          const on = active.has(it);
          const col = colors[it] || "#e8b339";
          return (
            <div key={it} className="seg" onClick={() => onToggle(it)}
              style={{ display: "flex", flexDirection: "column", alignItems: "flex-start", gap: 1, padding: isMobile ? "9px 13px" : "9px 15px", background: on ? col + "22" : "#16191e", border: "1.5px solid " + (on ? col : "#262b32"), borderRadius: 9, cursor: "pointer", flex: isMobile ? "1 0 auto" : "0 0 auto" }}>
              <span style={{ display: "flex", alignItems: "center", gap: 6, fontSize: 13.5, fontWeight: 600, color: on ? col : "#c2c7cf" }}>
                <span style={{ width: 8, height: 8, borderRadius: 3, background: col }} />
                {it}
                {on && <Check size={13} />}
              </span>
              {sub && <span style={{ fontSize: 10, color: on ? col : "#6a7079", fontFamily: "'Space Mono', monospace", marginLeft: 14 }}>{sub[it]}</span>}
            </div>
          );
        })}
      </div>
    </div>
  );
}

function SubFilter({ label, items, active, onToggle, colors }) {
  return (
    <div style={{ marginBottom: 12, marginTop: 12 }}>
      <div style={{ fontSize: 10.5, fontWeight: 700, color: "#7a818b", textTransform: "uppercase", letterSpacing: ".05em", marginBottom: 8 }}>{label}</div>
      <div style={{ display: "flex", gap: 7, flexWrap: "wrap" }}>
        {items.map(it => (
          <Seg key={it} active={active.has(it)} onClick={() => onToggle(it)} dot={colors && colors[it]}>{it}</Seg>
        ))}
      </div>
    </div>
  );
}

function Seg({ active, onClick, children, dot }) {
  return (
    <div className="seg" onClick={onClick}
      style={{ display: "flex", alignItems: "center", gap: 6, padding: "7px 11px", background: active ? "#e8b33920" : "#0d0f12", border: "1px solid " + (active ? "#e8b339" : "#262b32"), borderRadius: 7, fontSize: 12.5, cursor: "pointer", color: active ? "#e8b339" : "#c2c7cf", fontWeight: 500 }}>
      {dot && <span style={{ width: 7, height: 7, borderRadius: 3, background: dot }} />}
      {children}
      {active && <Check size={12} />}
    </div>
  );
}

function EmptyState({ isMobile }) {
  return (
    <div style={{ textAlign: "center", padding: isMobile ? "50px 20px" : "80px 20px", color: "#5a6069" }}>
      <div style={{ width: 60, height: 60, borderRadius: 16, background: "#13161a", border: "1px solid #1e2228", display: "flex", alignItems: "center", justifyContent: "center", margin: "0 auto 18px" }}>
        <Search size={26} color="#3e444d" />
      </div>
      <div style={{ fontSize: 16, fontWeight: 600, color: "#9aa5b1", marginBottom: 6 }}>Find a fixture</div>
      <div style={{ fontSize: 13.5, lineHeight: 1.6, maxWidth: 360, margin: "0 auto" }}>
        Pick an <span style={{ color: "#f4a259" }}>application</span>, <span style={{ color: "#e8b339" }}>type</span>, or <span style={{ color: "#f4845f" }}>output tier</span> above {"\u2014"} or search by name {"\u2014"} to see matching fixtures.
      </div>
    </div>
  );
}

function FramingBadge({ on, align }) {
  return (
    <span style={{ display: "inline-flex", alignItems: "center", gap: 4, justifyContent: align || "flex-end", fontSize: 11.5, fontWeight: 700, color: on ? "#6ee7a8" : "#5a6069" }}>
      {on ? <><Scissors size={11} /> Yes</> : "\u2014"}
    </span>
  );
}

function CriBadge({ v, align }) {
  if (v == null) return <span style={{ fontSize: 12, color: "#5a6069" }}>{"\u2014"}</span>;
  const col = v >= 90 ? "#6ee7a8" : v >= 80 ? "#e8b339" : "#9aa5b1";
  return <span style={{ fontSize: 12.5, fontWeight: 700, fontFamily: "'Space Mono', monospace", color: col }}>{v}</span>;
}

function ResultRow({ f, expanded, onToggle, inCompare, compareFull, onCompare, last, isMobile }) {
  return (
    <div style={{ borderBottom: last && !expanded ? "none" : "1px solid #1e2228", background: expanded ? "#13161a" : "transparent" }}>
      <div className="row-item" onClick={onToggle} style={{ display: "flex", alignItems: "center", gap: isMobile ? 10 : 14, padding: isMobile ? "12px 13px" : "12px 16px", cursor: "pointer" }}>
        <span style={{ width: 9, height: 9, borderRadius: 3, background: CAT_COLORS[f.category], flexShrink: 0 }} />
        <div style={{ flex: 1, minWidth: 0 }}>
          <div style={{ display: "flex", alignItems: "center", gap: 7 }}>
            <span style={{ fontSize: isMobile ? 14 : 15, fontWeight: 700, letterSpacing: "-.01em", overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>{clean(f.model)}</span>
            {f.everUsed && <span style={{ color: "#e8b339", fontSize: 12, flexShrink: 0 }}>{"\u2605"}</span>}
          </div>
          <div style={{ fontSize: 11.5, color: "#6a7079", marginTop: 1, fontWeight: 600, letterSpacing: ".02em", textTransform: "uppercase" }}>{f.brand}</div>
        </div>
        {!isMobile ? (
          <>
            <div style={{ width: 78, textAlign: "right" }}>
              <span style={{ fontSize: 12.5, fontWeight: 600, fontFamily: "'Space Mono', monospace", color: "#c2c7cf" }}>{f.outputLumens ? fmt(f.outputLumens) : "\u2014"}</span>
            </div>
            <div style={{ width: 78, textAlign: "right" }}><FramingBadge on={f.framing} /></div>
            <div style={{ width: 78, textAlign: "right" }}>
              <span style={{ fontSize: 12, fontWeight: 600, fontFamily: "'Space Mono', monospace", color: "#c2c7cf" }}>{zoomStr(f)}</span>
            </div>
            <div style={{ width: 78, textAlign: "right" }}><CriBadge v={f.cri} /></div>
          </>
        ) : (
          <div style={{ display: "flex", flexDirection: "column", alignItems: "flex-end", gap: 2, flexShrink: 0 }}>
            <span style={{ fontSize: 12, color: "#9aa5b1", fontFamily: "'Space Mono', monospace" }}>{f.outputLumens ? fmt(f.outputLumens) + " lm" : "\u2014"}</span>
            <span style={{ display: "flex", gap: 7, alignItems: "center" }}>
              {f.framing && <span style={{ fontSize: 10, color: "#6ee7a8", fontWeight: 700, display: "flex", alignItems: "center", gap: 2 }}><Scissors size={9} />Frm</span>}
              {f.cri != null && <span style={{ fontSize: 10.5, fontFamily: "'Space Mono', monospace", color: f.cri >= 90 ? "#6ee7a8" : "#7a818b", fontWeight: 700 }}>CRI {f.cri}</span>}
            </span>
          </div>
        )}
        <div style={{ flexShrink: 0, color: "#5a6069" }}>{expanded ? <ChevronUp size={17} /> : <ChevronDown size={17} />}</div>
      </div>

      {expanded && (
        <div className="expand" style={{ padding: isMobile ? "0 13px 14px" : "0 16px 16px" }}>
          <div style={{ background: "#0d0f12", border: "1px solid #1e2228", borderRadius: 10, padding: isMobile ? 13 : 16 }}>
            <div style={{ display: "flex", gap: 5, flexWrap: "wrap", marginBottom: 13 }}>
              {(f.applications||[]).map(a => (
                <span key={a} style={{ fontSize: 9.5, fontWeight: 700, color: APP_COLORS[a], background: APP_COLORS[a] + "1c", padding: "3px 7px", borderRadius: 4, textTransform: "uppercase", letterSpacing: ".03em" }}>{a}</span>
              ))}
              {f.tier && <span style={{ fontSize: 9.5, fontWeight: 700, color: TIER_COLORS[f.tier], background: (TIER_COLORS[f.tier]||"#888") + "1c", padding: "3px 7px", borderRadius: 4, textTransform: "uppercase", letterSpacing: ".03em" }}>{f.tier} output</span>}
              {f.variant && <span style={{ fontSize: 9.5, fontWeight: 700, color: "#9aa5b1", background: "#9aa5b115", padding: "3px 7px", borderRadius: 4, textTransform: "uppercase", letterSpacing: ".03em" }}>{f.variant}</span>}
            </div>

            {f.description && (
              <div style={{ fontSize: 12.5, color: "#9aa5b1", lineHeight: 1.55, marginBottom: 13, fontStyle: "italic" }}>{f.description}</div>
            )}

            <div style={{ display: "grid", gridTemplateColumns: isMobile ? "1fr 1fr" : "1fr 1fr 1fr", gap: 8, marginBottom: 13 }}>
              <SpecBox label="Max Output" value={f.outputLumens ? fmt(f.outputLumens) + " lm" : "\u2014"} />
              <SpecBox label="Framing Shutters" value={f.framing ? "Yes" : "No"} highlight={f.framing} />
              <SpecBox label="CRI" value={clean(f.criRaw) || (f.cri != null ? String(f.cri) : "\u2014")} />
              <SpecBox label="Lamp" value={(f.watts ? f.watts + "W " : "") + (f.lampType || "") || "\u2014"} />
              <SpecBox label="Color Temp" value={clean(f.cct) || clean(f.cctRange) || "\u2014"} />
              <SpecBox label="Zoom" value={f.zoomMin != null ? zoomStr(f) + (f.zoomRatio ? "  (" + f.zoomRatio + ")" : "") : (clean(f.zoomRaw) || "\u2014")} />
              <SpecBox label="Color Mixing" value={clean(f.colorMixing) || "\u2014"} />
              <SpecBox label="Pan / Tilt" value={clean(f.panTilt) || "\u2014"} />
              <SpecBox label="Weight" value={f.weightKg ? f.weightKg + " kg" : "\u2014"} />
              <SpecBox label="IP Rating" value={clean(f.ipRating) || "\u2014"} />
              <SpecBox label="Power Draw" value={f.powerConsumption ? f.powerConsumption + " W" : "\u2014"} />
              <SpecBox label="DMX Channels" value={clean(f.dmxChannels) || "\u2014"} />
              <SpecBox label="Protocols" value={clean(f.protocols) || "\u2014"} wide={isMobile} />
              <SpecBox label="Animation Wheel" value={f.animationWheel ? "Yes" : "No"} />
              <SpecBox label="Effects" value={clean(f.effectsRaw) || "\u2014"} wide />
              <SpecBox label="Gobo" value={clean(f.gobo) || "\u2014"} wide />
            </div>

            <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
              <button onClick={e => { e.stopPropagation(); onCompare(); }} disabled={!inCompare && compareFull}
                style={{ flex: "1 1 160px", padding: "11px", background: inCompare ? "#e8b339" : "#1e2228", border: "none", borderRadius: 8, color: inCompare ? "#0d0f12" : (compareFull ? "#4a5059" : "#e6e8eb"), fontSize: 13, fontWeight: 600, cursor: (!inCompare && compareFull) ? "default" : "pointer", fontFamily: "inherit", display: "flex", alignItems: "center", justifyContent: "center", gap: 6 }}>
                {inCompare ? <><Minus size={14} /> Remove from comparison</> : <><Plus size={14} /> Add to comparison</>}
              </button>
              {f.link ? (
                <a href={f.link} target="_blank" rel="noopener noreferrer" onClick={e => e.stopPropagation()}
                  style={{ flex: "1 1 160px", padding: "11px", background: "#1e2228", borderRadius: 8, color: "#e6e8eb", fontSize: 13, fontWeight: 600, textDecoration: "none", display: "flex", alignItems: "center", justifyContent: "center", gap: 6 }}>
                  <ExternalLink size={14} /> Product page
                </a>
              ) : (
                <div style={{ flex: "1 1 160px", padding: "11px", background: "#15171b", borderRadius: 8, color: "#4a5059", fontSize: 12, fontWeight: 500, display: "flex", alignItems: "center", justifyContent: "center", gap: 6 }}>
                  <ExternalLink size={13} /> No link yet
                </div>
              )}
            </div>
            {f.lastVerified && <div style={{ fontSize: 10, color: "#4a5059", marginTop: 10, fontFamily: "'Space Mono', monospace" }}>SPECS VERIFIED {f.lastVerified}</div>}
          </div>
        </div>
      )}
    </div>
  );
}

function SpecBox({ label, value, wide, highlight }) {
  return (
    <div style={{ background: highlight ? "#6ee7a812" : "#16191e", border: highlight ? "1px solid #6ee7a830" : "1px solid transparent", borderRadius: 7, padding: "8px 10px", gridColumn: wide ? "1 / -1" : "auto" }}>
      <div style={{ fontSize: 9.5, color: "#6a7079", fontWeight: 700, textTransform: "uppercase", letterSpacing: ".04em", marginBottom: 3 }}>{label}</div>
      <div style={{ fontSize: 12.5, color: highlight ? "#6ee7a8" : "#e6e8eb", whiteSpace: "pre-line", lineHeight: 1.45, fontWeight: highlight ? 700 : 400 }}>{value}</div>
    </div>
  );
}

function CompareModal({ items, onClose, onRemove, isMobile }) {
  if (!items.length) return null;
  const fields = [
    ["category", "Type", f => f.category],
    ["apps", "Applications", f => (f.applications||[]).join(", ") || "\u2014"],
    ["framing", "Framing Shutters", f => f.framing ? "Yes" : "No"],
    ["cri", "CRI", f => f.cri != null ? (clean(f.criRaw) || String(f.cri)) : "\u2014", f => f.cri || 0],
    ["maxOutput", "Max Output", f => f.outputLumens ? fmt(f.outputLumens) + " lm" : "\u2014", f => f.outputLumens || 0],
    ["watts", "Wattage", f => f.watts ? f.watts + " W" : "\u2014", f => f.watts || 0],
    ["lamp", "Light Source", f => (f.lampType || "\u2014")],
    ["cct", "Color Temp", f => clean(f.cct) || clean(f.cctRange) || "\u2014"],
    ["colorMixing", "Color Mixing", f => clean(f.colorMixing) || "\u2014"],
    ["zoom", "Zoom Range", f => f.zoomMin != null ? zoomStr(f) + (f.zoomRatio ? " (" + f.zoomRatio + ")" : "") : "\u2014"],
    ["zoomMin", "Tightest Zoom", f => f.zoomMin != null ? f.zoomMin + "\u00b0" : "\u2014", f => f.zoomMin != null ? -f.zoomMin : -999],
    ["panTilt", "Pan / Tilt", f => clean(f.panTilt) || "\u2014"],
    ["weight", "Weight", f => f.weightKg ? f.weightKg + " kg" : "\u2014", f => f.weightKg ? -f.weightKg : -999],
    ["ip", "IP Rating", f => clean(f.ipRating) || "\u2014"],
    ["power", "Power Draw", f => f.powerConsumption ? f.powerConsumption + " W" : "\u2014"],
    ["dmx", "DMX Channels", f => clean(f.dmxChannels) || "\u2014"],
    ["protocols", "Protocols", f => clean(f.protocols) || "\u2014"],
    ["animation", "Animation Wheel", f => f.animationWheel ? "Yes" : "No"],
    ["gobo", "Gobo", f => clean(f.gobo) || "\u2014"],
    ["effects", "Effects", f => clean(f.effectsRaw) || "\u2014"],
  ];
  return (
    <div onClick={onClose} style={{ position: "fixed", inset: 0, background: "rgba(0,0,0,.72)", backdropFilter: "blur(3px)", display: "flex", alignItems: isMobile ? "flex-end" : "center", justifyContent: "center", zIndex: 100, padding: isMobile ? 0 : 16 }}>
      <div className={isMobile ? "slide-up" : ""} style={{ background: "#13161a", border: "1px solid #262b32", borderRadius: isMobile ? "16px 16px 0 0" : 14, width: isMobile ? "100%" : "min(1080px,96vw)", maxHeight: isMobile ? "92vh" : "90vh", overflow: "hidden", display: "flex", flexDirection: "column" }} onClick={e => e.stopPropagation()}>
        <div style={{ padding: isMobile ? "16px 18px" : "18px 22px", borderBottom: "1px solid #1e2228", display: "flex", justifyContent: "space-between", alignItems: "center" }}>
          <div style={{ fontSize: isMobile ? 15 : 17, fontWeight: 700, display: "flex", alignItems: "center", gap: 9 }}>
            <GitCompare size={isMobile ? 17 : 19} color="#e8b339" /> Compare <span style={{ fontSize: 12, color: "#6a7079", fontFamily: "'Space Mono', monospace" }}>{items.length}/4</span>
          </div>
          <X size={24} onClick={onClose} style={{ cursor: "pointer", color: "#6a7079" }} />
        </div>
        <div style={{ overflow: "auto" }}>
          <table style={{ width: "100%", borderCollapse: "collapse", minWidth: (isMobile ? 120 : 170) + items.length * (isMobile ? 145 : 195) }}>
            <thead>
              <tr>
                <th style={{ position: "sticky", left: 0, background: "#13161a", textAlign: "left", padding: isMobile ? "12px" : "14px 16px", fontSize: 11, color: "#7a818b", fontWeight: 700, textTransform: "uppercase", width: isMobile ? 120 : 170, zIndex: 2 }}>Spec</th>
                {items.map(f => (
                  <th key={f.id} style={{ padding: isMobile ? "12px" : "14px 16px", textAlign: "left", borderLeft: "1px solid #1e2228", minWidth: isMobile ? 145 : 185 }}>
                    <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", gap: 8 }}>
                      <div>
                        <div style={{ fontSize: 10, fontWeight: 700, color: CAT_COLORS[f.category], textTransform: "uppercase", letterSpacing: ".04em" }}>{f.brand}</div>
                        <div style={{ fontSize: isMobile ? 12.5 : 14, fontWeight: 700, marginTop: 2, lineHeight: 1.25 }}>{clean(f.model)}</div>
                      </div>
                      <X size={15} onClick={() => onRemove(f.id)} style={{ cursor: "pointer", color: "#5a6069", flexShrink: 0 }} />
                    </div>
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {fields.map(([key, label, render, scoreFn], ri) => {
                let bestId = null;
                if (scoreFn && items.length > 1) {
                  let bv = -Infinity;
                  items.forEach(f => { const s = scoreFn(f); if (s > bv) { bv = s; bestId = f.id; } });
                  if (bv <= 0 && key !== "zoomMin" && key !== "weight") bestId = null;
                }
                return (
                  <tr key={key} style={{ background: ri % 2 ? "#0f1216" : "transparent" }}>
                    <td style={{ position: "sticky", left: 0, background: ri % 2 ? "#0f1216" : "#13161a", padding: isMobile ? "10px 12px" : "11px 16px", fontSize: 11, color: "#7a818b", fontWeight: 600, textTransform: "uppercase", letterSpacing: ".03em", zIndex: 1 }}>{label}</td>
                    {items.map(f => (
                      <td key={f.id} style={{ padding: isMobile ? "10px 12px" : "11px 16px", fontSize: isMobile ? 12 : 13, borderLeft: "1px solid #1e2228", color: bestId === f.id ? "#6ee7a8" : "#d4d8de", fontWeight: bestId === f.id ? 700 : 400, whiteSpace: "pre-line", lineHeight: 1.45, verticalAlign: "top" }}>
                        {render(f)}
                        {bestId === f.id && <span style={{ marginLeft: 6, fontSize: 9, background: "#6ee7a820", color: "#6ee7a8", padding: "1px 5px", borderRadius: 4, fontWeight: 700, whiteSpace: "nowrap" }}>BEST</span>}
                      </td>
                    ))}
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
