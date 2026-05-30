import React, { useState, useMemo, useEffect } from "react";
import { Search, X, GitCompare, ChevronDown, ChevronUp, Check, Plus, Minus, ExternalLink, Scissors, SlidersHorizontal, Droplets, Wifi, Zap, Star, Menu, Sparkles } from "lucide-react";
import { IconMasksTheater as Drama, IconMicrophone2 as Mic2, IconVideo as Video, IconBuilding as Building2 } from "@tabler/icons-react";

import FIXTURES from "./fixtures.json";
import { FONTS, COLORS, getTypeColor, getTierColor, RADIUS, SPACING } from "./tokens";

const CAT_COLORS = { "Performance":COLORS.typePerformance, "Spot":COLORS.typeSpot, "Wash":COLORS.typeWash, "Bar / Batten":COLORS.typeBar };
const LAMP_COLORS = { "LED":"#6EE7A8", "Discharge":"#F5A623", "Laser":"#FF6B6B", "Other":"#9AA5B1" };
const APP_COLORS = { "Theater":COLORS.actionAmber, "Concert":"#F4845F", "TV-Film":"#FF6B9D", "Corporate":"#9D8DF1" };
const TIER_COLORS = { "Small":"#6EE7A8", "Medium":COLORS.actionAmber, "Large":"#F4845F" };
const TIER_DESC = { "Small":"< 10k lm", "Medium":"10\u201330k lm", "Large":"\u2265 30k lm" };
const APP_ORDER = ["Theater","Concert","TV-Film","Corporate"];
const MAIN_BRANDS = ["Martin","Robe","Elation","Ayrton"];
const APP_ICONS = {
  "Theater":   Drama,
  "Concert":   Mic2,
  "TV-Film":   Video,
  "Corporate": Building2,
};

const FEAT_FILTERS = [
  { key:"framing",   label:"Framing Shutters", mobileLabel:"Framing",   icon:<Scissors size={13}/>,  color:"#6EE7A8", field:f=>f.framing },
  { key:"led",       label:"LED Source",        mobileLabel:"LED",       icon:<Zap size={13}/>,       color:"#6EE7A8", field:f=>f.lampType==="LED" },
  { key:"dualFrost", label:"Dual Frost",        mobileLabel:"Frost",     icon:<Droplets size={13}/>,  color:"#4ECDC4", field:f=>f.dualFrost },
  { key:"ipRated",   label:"IP Rated",          mobileLabel:"IP",        icon:<Wifi size={13}/>,      color:"#9D8DF1", field:f=>f.ipRated },
  { key:"animation", label:"Animation Wheel",   mobileLabel:"Animation", icon:<Sparkles size={13}/>,  color:"#F2D466", field:f=>f.animationWheel },
];

function clean(s){ return (s||"").replace(/\s+/g," ").trim(); }
function fmt(n){ return n==null?"\u2014":n.toLocaleString(); }
function zoomStr(f){ return f.zoomMin!=null?(f.zoomMin===f.zoomMax?f.zoomMin+"\u00b0":f.zoomMin+"\u00b0\u2013"+f.zoomMax+"\u00b0"):"\u2014"; }
function catLabel(cat){
  switch(cat){
    case "Performance":    return "PERF";
    case "Spot":           return "SPOT";
    case "Wash":           return "WASH";
    case "Bar / Batten":   return "BAR";
    default:               return (cat||"").toUpperCase();
  }
}
function catDisplayName(cat){
  switch(cat){
    case "Bar / Batten": return "Bar";
    default:             return cat;
  }
}

export default function App() {
  const [query,setQuery]       = useState("");
  const [apps,setApps]         = useState(new Set());
  const [cats,setCats]         = useState(new Set());
  const [tiers,setTiers]       = useState(new Set());
  const [brands,setBrands]     = useState(new Set());
  const [feats,setFeats]       = useState(new Set());
  const [lamps,setLamps]       = useState(new Set());
  const [sortBy,setSortBy]     = useState("output-desc");
  const [expanded,setExpanded] = useState(new Set());
  const [compare,setCompare]   = useState([]);
  const [showCompare,setShowCompare] = useState(false);
  const [isMobile,setIsMobile] = useState(false);
  const [watchingFilterActive,setWatchingFilterActive] = useState(false);
  const [showBrandPicker,setShowBrandPicker] = useState(false);
  const [showMobileMenu,setShowMobileMenu] = useState(false);
  const [moreFiltersExpanded,setMoreFiltersExpanded] = useState(false);
  const [watchlist,setWatchlist] = useState(()=>{
    try {
      const saved = localStorage.getItem("mld-watchlist");
      return saved ? new Set(JSON.parse(saved)) : new Set();
    } catch {
      return new Set();
    }
  });

  useEffect(()=>{
    const c=()=>setIsMobile(window.innerWidth<760);
    c(); window.addEventListener("resize",c); return()=>window.removeEventListener("resize",c);
  },[]);

  useEffect(()=>{
    try {
      localStorage.setItem("mld-watchlist", JSON.stringify([...watchlist]));
    } catch {
      // localStorage unavailable (private mode, etc.) — fail silently
    }
  },[watchlist]);

  // Lock background scroll when any mobile sheet is open
  useEffect(()=>{
    const anyOpen = showBrandPicker || showMobileMenu;
    const prev = document.body.style.overflow;
    document.body.style.overflow = anyOpen ? "hidden" : prev || "";
    return()=>{ document.body.style.overflow = prev || ""; };
  },[showBrandPicker,showMobileMenu]);

  const allBrands = useMemo(()=>[...new Set(FIXTURES.map(f=>f.brand))].sort(),[]);
  const allCats   = ["Performance","Spot","Wash","Bar / Batten"];
  const allTiers  = ["Small","Medium","Large"];
  const allLamps  = ["LED","Discharge","Laser","Other"];

  function toggle(set,setter,val){
    const n=new Set(set); n.has(val)?n.delete(val):n.add(val); setter(n);
  }

  const hasFilter = query||apps.size||cats.size||tiers.size||brands.size||feats.size||lamps.size||watchingFilterActive;
  const moreCount = lamps.size;

  const filtered = useMemo(()=>{
    if(!hasFilter) return [];
    let r = FIXTURES.filter(f=>{
      if(watchingFilterActive && !watchlist.has(f.id)) return false;
      if(query){
        const q=query.toLowerCase();
        const hay=(f.model+" "+f.brand+" "+f.category+" "+(f.standout||"")+" "+(f.description||"")+" "+(f.colorMixing||"")+" "+(f.lamp||"")+" "+(f.applications||[]).join(" ")).toLowerCase();
        if(!hay.includes(q)) return false;
      }
      if(apps.size&&!(f.applications||[]).some(a=>apps.has(a))) return false;
      if(cats.size&&!cats.has(f.category)) return false;
      if(tiers.size&&!tiers.has(f.tier)) return false;
      if(brands.size&&!brands.has(f.brand)) return false;
      for(const fk of feats){
        const ff=FEAT_FILTERS.find(x=>x.key===fk);
        if(ff&&!ff.field(f)) return false;
      }
      if(lamps.size&&!lamps.has(f.lampType)) return false;
      return true;
    });
    const [key,dir]=sortBy.split("-");
    return [...r].sort((a,b)=>{
      let av,bv;
      if(key==="output"){av=a.outputLumens||0;bv=b.outputLumens||0;}
      else if(key==="cri"){av=a.cri||0;bv=b.cri||0;}
      else if(key==="watts"){av=a.watts||0;bv=b.watts||0;}
      else if(key==="zoom"){av=a.zoomMin||999;bv=b.zoomMin||999;}
      else{av=a.model.toLowerCase();bv=b.model.toLowerCase();}
      if(av<bv) return dir==="asc"?-1:1;
      if(av>bv) return dir==="asc"?1:-1;
      return 0;
    });
  },[query,apps,cats,tiers,brands,feats,lamps,sortBy,hasFilter,watchingFilterActive,watchlist]);

  function toggleExpand(id){
    setExpanded(p=>{const n=new Set(p);n.has(id)?n.delete(id):n.add(id);return n;});
  }
  function toggleCompare(f){
    setCompare(c=>{
      if(c.find(x=>x.id===f.id)) return c.filter(x=>x.id!==f.id);
      if(c.length>=4) return c;
      return [...c,f];
    });
  }
  const inCompare=id=>compare.some(x=>x.id===id);
  function toggleWatch(id){
    setWatchlist(prev=>{
      const next = new Set(prev);
      next.has(id) ? next.delete(id) : next.add(id);
      return next;
    });
  }
  const isWatched=id=>watchlist.has(id);
  function clearAll(){
    setQuery(""); setApps(new Set()); setCats(new Set()); setTiers(new Set());
    setBrands(new Set()); setFeats(new Set()); setLamps(new Set());
    setWatchingFilterActive(false);
  }

  const activeCount=apps.size+cats.size+tiers.size+brands.size+feats.size+lamps.size;

  const activeChips = useMemo(()=>{
    const chips = [];
    if(query) chips.push({key:"query", label:`"${query}"`, onRemove:()=>setQuery("")});
    apps.forEach(a => chips.push({key:`app-${a}`, label:a, onRemove:()=>{const n=new Set(apps); n.delete(a); setApps(n);}}));
    cats.forEach(c => chips.push({key:`cat-${c}`, label:catDisplayName(c), onRemove:()=>{const n=new Set(cats); n.delete(c); setCats(n);}}));
    tiers.forEach(t => chips.push({key:`tier-${t}`, label:t, onRemove:()=>{const n=new Set(tiers); n.delete(t); setTiers(n);}}));
    brands.forEach(b => chips.push({key:`brand-${b}`, label:b, onRemove:()=>{const n=new Set(brands); n.delete(b); setBrands(n);}}));
    feats.forEach(f => chips.push({key:`feat-${f}`, label:f, onRemove:()=>{const n=new Set(feats); n.delete(f); setFeats(n);}}));
    lamps.forEach(l => chips.push({key:`lamp-${l}`, label:l, onRemove:()=>{const n=new Set(lamps); n.delete(l); setLamps(n);}}));
    return chips;
  },[query, apps, cats, tiers, brands, feats, lamps]);

  return (
    <div style={{minHeight:"100vh",background:COLORS.bgBase,color:COLORS.textPrimary,fontFamily:FONTS.ui}}>
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Geist:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');
        *{box-sizing:border-box;-webkit-tap-highlight-color:transparent;}
        ::-webkit-scrollbar{width:5px;height:5px;}
        ::-webkit-scrollbar-track{background:#111113;}
        ::-webkit-scrollbar-thumb{background:#222228;border-radius:3px;}
        input::placeholder{color:#7E7E8C;}
        .fx-row{transition:background .12s;}
        @media(hover:hover){.fx-row:hover{background:#0F0F12 !important;}}
        .chip{transition:all .11s;user-select:none;cursor:pointer;}
        .chip:active{transform:scale(.96);}
        .expand-in{animation:ei .18s cubic-bezier(.2,.8,.2,1);}
        @keyframes ei{from{opacity:0;transform:translateY(-4px)}to{opacity:1;transform:translateY(0)}}
        .slide-up{animation:su .22s cubic-bezier(.2,.8,.2,1);}
        @keyframes su{from{transform:translateY(100%)}to{transform:translateY(0)}}
        .brand-pill{transition:all .11s;user-select:none;cursor:pointer;white-space:nowrap;}
        .brand-pill:active{transform:scale(.96);}
        a{color:inherit;text-decoration:none;}
        .no-scrollbar::-webkit-scrollbar{display:none;}
        .no-scrollbar{-ms-overflow-style:none;scrollbar-width:none;}
      `}</style>

      {/* ── HEADER ── */}
      <div style={{background:COLORS.bgBase,borderBottom:"1px solid #18181C",position:"sticky",top:0,zIndex:50}}>
        <div style={{maxWidth:1180,margin:"0 auto",padding:isMobile?"12px 16px":"16px 28px",display:"flex",alignItems:"center",gap:14}}>
          <div style={{flex:1,display:"flex",alignItems:"center",gap:12}}>
            {/* Logo mark */}
            <div style={{width:36,height:36,borderRadius:RADIUS.md,background:COLORS.bgElevated,border:`1px solid ${COLORS.borderDefault}`,display:"flex",alignItems:"center",justifyContent:"center",fontFamily:FONTS.display,fontSize:15,fontWeight:800,color:COLORS.actionAmber,letterSpacing:"-.02em",flexShrink:0}}>
              ML
            </div>
            {/* Wordmark + metadata */}
            <div>
              <div style={{fontSize:isMobile?22:26,fontWeight:800,letterSpacing:"-.03em",lineHeight:1}}>Moving Light Database</div>
              <div style={{fontSize:15,color:COLORS.textSecondary,fontFamily:FONTS.mono,marginTop:2,letterSpacing:".04em"}}>
                {FIXTURES.length} FIXTURES · {allBrands.length} BRANDS
              </div>
            </div>
          </div>
          {!isMobile&&(
            <div style={{display:"flex",gap:8}}>
              <button onClick={()=>setWatchingFilterActive(v=>!v)}
                style={{display:"flex",alignItems:"center",gap:6,padding:"9px 16px",
                  background:watchingFilterActive?COLORS.actionAmber:(watchlist.size?COLORS.actionAmberBg:"transparent"),
                  color:watchingFilterActive?COLORS.bgBase:(watchlist.size?COLORS.actionAmber:COLORS.textSecondary),
                  border:`1px solid ${watchingFilterActive||watchlist.size?COLORS.actionAmber:COLORS.borderDefault}`,
                  borderRadius:RADIUS.md,fontSize:14,fontWeight:600,cursor:"pointer",fontFamily:FONTS.ui}}>
                <Star size={14} fill={watchingFilterActive?COLORS.bgBase:(watchlist.size?COLORS.actionAmber:"none")}/> Watching ({watchlist.size})
              </button>
              <button onClick={()=>compare.length&&setShowCompare(true)}
                style={{display:"flex",alignItems:"center",gap:6,padding:"9px 16px",
                  background:compare.length?COLORS.actionAmber:"transparent",
                  color:compare.length?COLORS.bgBase:COLORS.textSecondary,
                  border:`1px solid ${compare.length?COLORS.actionAmber:COLORS.borderDefault}`,
                  borderRadius:RADIUS.md,fontSize:14,fontWeight:600,
                  cursor:compare.length?"pointer":"default",opacity:compare.length?1:0.6,fontFamily:FONTS.ui}}>
                <GitCompare size={14}/> Compare ({compare.length}/4)
              </button>
            </div>
          )}
          {isMobile&&(
            <button onClick={()=>setShowMobileMenu(true)}
              style={{marginLeft:"auto",display:"flex",alignItems:"center",justifyContent:"center",width:38,height:38,background:COLORS.bgElevated,border:`1px solid ${COLORS.borderDefault}`,borderRadius:RADIUS.md,position:"relative",cursor:"pointer",flexShrink:0,padding:0,color:COLORS.textSecondary}}>
              <Menu size={20}/>
              {(watchingFilterActive || compare.length > 0 || watchlist.size > 0) && (
                <span style={{position:"absolute",top:-3,right:-3,width:10,height:10,borderRadius:"50%",background:COLORS.actionAmber,border:`2px solid ${COLORS.bgBase}`}}/>
              )}
            </button>
          )}
        </div>
      </div>

      <div style={{maxWidth:1180,margin:"0 auto",padding:isMobile?"16px 16px 100px":"22px 28px 48px"}}>

        {/* ── ALWAYS-VISIBLE FILTERS ── */}

        {/* Search */}
        <div style={{position:"relative",marginBottom:22}}>
          <Search size={17} color="#7E7E8C" style={{position:"absolute",left:14,top:"50%",transform:"translateY(-50%)"}}/>
          <input value={query} onChange={e=>setQuery(e.target.value)}
            placeholder="Search fixture, brand, or feature..."
            style={{width:"100%",padding:isMobile?"13px 40px":"14px 44px",background:COLORS.bgElevated,border:"1px solid #222228",borderRadius:11,color:COLORS.textPrimary,fontSize:isMobile?18:17,outline:"none",fontFamily:FONTS.ui,fontWeight:400}}/>
          {query&&<X size={16} onClick={()=>setQuery("")} style={{position:"absolute",right:13,top:"50%",transform:"translateY(-50%)",color:"#7E7E8C",cursor:"pointer"}}/>}
        </div>

        {/* Application */}
        <Section label="Application" active={apps.size}>
          <div style={{display:"flex",gap:isMobile?6:8,flexWrap:"wrap"}}>
            {APP_ORDER.map(a=>{
              const on=apps.has(a);
              const col=APP_COLORS[a];
              const Icon=APP_ICONS[a];
              return(
                <div key={a} className="chip" onClick={()=>toggle(apps,setApps,a)}
                  style={{display:"flex",alignItems:"center",gap:5,padding:isMobile?"7px 10px":"7px 12px",background:on?col+"33":COLORS.bgElevated,border:`1.5px solid ${on?col:COLORS.borderDefault}`,borderRadius:RADIUS.md,fontSize:isMobile?13:13,fontWeight:600,color:on?col:COLORS.textSecondary,fontFamily:FONTS.ui,cursor:"pointer"}}>
                  {Icon&&<Icon size={14} strokeWidth={2}/>}
                  {a}
                  {on&&<Check size={12}/>}
                </div>
              );
            })}
          </div>
        </Section>

        {/* Output Tier */}
        <Section label="Output Tier" active={tiers.size}>
          <div style={{display:"flex",gap:8,flexWrap:"wrap"}}>
            {allTiers.map(t=>{
              const on=tiers.has(t);
              const col=TIER_COLORS[t];
              return(
                <div key={t} className="chip" onClick={()=>toggle(tiers,setTiers,t)}
                  style={{display:"flex",flexDirection:"column",alignItems:"flex-start",padding:isMobile?"7px 12px":"8px 14px",background:on?col+"33":COLORS.bgElevated,border:`1.5px solid ${on?col:COLORS.borderDefault}`,borderRadius:RADIUS.md,fontFamily:FONTS.ui,cursor:"pointer"}}>
                  <div style={{display:"flex",alignItems:"center",gap:8,fontSize:isMobile?15:14,fontWeight:600,color:on?col:COLORS.textSecondary}}>
                    <span style={{width:8,height:8,borderRadius:"50%",background:col,flexShrink:0}}/>
                    {t}
                    {on&&<Check size={13}/>}
                  </div>
                  <div style={{fontSize:12,fontFamily:FONTS.mono,color:on?col+"CC":COLORS.textMuted,marginTop:3,marginLeft:16}}>{TIER_DESC[t]}</div>
                </div>
              );
            })}
          </div>
        </Section>

        {/* Mobile-only "+ More filters" inline expand toggle */}
        {isMobile && (
          <button onClick={()=>setMoreFiltersExpanded(v=>!v)}
            style={{display:"flex",alignItems:"center",justifyContent:"center",gap:7,padding:"10px 12px",background:"transparent",border:`1px dashed ${COLORS.borderDefault}`,borderRadius:RADIUS.md,fontFamily:FONTS.ui,fontSize:13,fontWeight:600,color:COLORS.textMuted,width:"100%",marginTop:6,marginBottom:14,cursor:"pointer"}}>
            <SlidersHorizontal size={14}/>
            More filters
            {(cats.size+feats.size+brands.size+lamps.size)>0 && (
              <span style={{background:COLORS.actionAmber,color:COLORS.bgBase,borderRadius:RADIUS.sm,padding:"1px 7px",fontSize:12,fontWeight:700,fontFamily:FONTS.ui}}>{cats.size+feats.size+brands.size+lamps.size}</span>
            )}
            {moreFiltersExpanded ? <ChevronUp size={13}/> : <ChevronDown size={13}/>}
          </button>
        )}

        {/* Gated block — Type, Features, Brand, Advanced.
            Desktop: always rendered. Mobile: only when moreFiltersExpanded. */}
        {(!isMobile || moreFiltersExpanded) && (
          <div className={isMobile ? "expand-in" : undefined}>

            {/* Type */}
            <Section label="Type" active={cats.size}>
              <div style={{display:"flex",gap:8,flexWrap:"wrap"}}>
                {allCats.map(c=>{
                  const on=cats.has(c);
                  const col=CAT_COLORS[c];
                  return(
                    <div key={c} className="chip" onClick={()=>toggle(cats,setCats,c)}
                      style={{display:"flex",alignItems:"center",gap:6,padding:isMobile?"8px 11px":"7px 12px",background:on?col+"33":COLORS.bgElevated,border:`1.5px solid ${on?col:COLORS.borderDefault}`,borderRadius:RADIUS.md,fontSize:isMobile?14:13,fontWeight:600,color:on?col:COLORS.textSecondary,fontFamily:FONTS.ui,cursor:"pointer"}}>
                      <span style={{width:8,height:8,borderRadius:"50%",background:col,flexShrink:0}}/>
                      {catDisplayName(c)}
                      {on&&<Check size={13}/>}
                    </div>
                  );
                })}
              </div>
            </Section>

            {/* Features */}
            <Section label="Features" active={feats.size}>
              <div style={{display:"flex",gap:isMobile?5:8,flexWrap:"wrap"}}>
                {FEAT_FILTERS.map(({key,label,icon,color,field,mobileLabel})=>{
                  const on=feats.has(key);
                  return(
                    <div key={key} className="chip" onClick={()=>toggle(feats,setFeats,key)}
                      style={{display:"flex",alignItems:"center",gap:isMobile?5:8,padding:isMobile?"6px 9px":"10px 16px",background:on?color+"33":COLORS.bgElevated,border:`1.5px solid ${on?color:COLORS.borderDefault}`,borderRadius:RADIUS.md,fontSize:isMobile?12:14,fontWeight:600,color:on?color:COLORS.textSecondary,fontFamily:FONTS.ui,cursor:"pointer"}}>
                      {icon}
                      {isMobile && mobileLabel ? mobileLabel : label}
                      {on&&<Check size={12}/>}
                    </div>
                  );
                })}
              </div>
            </Section>

            {/* Brand — main + "+N more" (both viewports) */}
            <Section label="Brand" active={brands.size}>
              <div style={{display:"flex",flexWrap:"wrap",gap:7}}>
                {MAIN_BRANDS.map(b=>{
                  const on=brands.has(b);
                  const n=FIXTURES.filter(f=>f.brand===b).length;
                  if(n===0) return null;
                  return(
                    <div key={b} className="brand-pill" onClick={()=>toggle(brands,setBrands,b)}
                      style={{display:"flex",alignItems:"center",gap:6,padding:"7px 11px",background:on?COLORS.standoutCyanBg:COLORS.bgElevated,border:`1.5px solid ${on?COLORS.standoutCyan:COLORS.borderDefault}`,borderRadius:RADIUS.md,fontSize:14,fontWeight:600,color:on?COLORS.standoutCyan:COLORS.brandPeriwinkle,flexShrink:0,fontFamily:FONTS.mono,letterSpacing:".03em",textTransform:"uppercase",cursor:"pointer"}}>
                      <div style={{width:14,height:14,borderRadius:3,background:COLORS.brandLogoBg,flexShrink:0,display:"flex",alignItems:"center",justifyContent:"center",fontSize:8,fontWeight:700,color:COLORS.textMuted}}>{b[0]}</div>
                      {b}
                      <span style={{fontSize:11,fontFamily:FONTS.mono,color:on?COLORS.standoutCyan+"AA":COLORS.textDim,fontWeight:500}}>{n}</span>
                      {on&&<Check size={11}/>}
                    </div>
                  );
                })}

                {(() => {
                  const others = allBrands.filter(b => !MAIN_BRANDS.includes(b));
                  if(others.length === 0) return null;
                  const otherCount = others.length;
                  const hiddenSelectedCount = [...brands].filter(b => !MAIN_BRANDS.includes(b)).length;
                  const hasHiddenSelection = hiddenSelectedCount > 0;
                  return (
                    <div className="brand-pill" onClick={()=>setShowBrandPicker(true)}
                      style={{display:"flex",alignItems:"center",gap:6,padding:"7px 11px",background:hasHiddenSelection?COLORS.standoutCyanBg:COLORS.bgElevated,border:`1.5px solid ${hasHiddenSelection?COLORS.standoutCyan:COLORS.borderDefault}`,borderRadius:RADIUS.md,fontSize:14,fontWeight:600,color:hasHiddenSelection?COLORS.standoutCyan:COLORS.textSecondary,flexShrink:0,fontFamily:FONTS.ui,cursor:"pointer"}}>
                      <Plus size={13}/>
                      {hasHiddenSelection ? `${hiddenSelectedCount} of ${otherCount} more` : `${otherCount} more`}
                    </div>
                  );
                })()}
              </div>
            </Section>

            {/* Light Source (advanced) */}
            <Section label="Light Source" active={lamps.size}>
              <div style={{display:"flex",gap:7,flexWrap:"wrap"}}>
                {allLamps.map(l=>(
                  <MiniPill key={l} active={lamps.has(l)} onClick={()=>toggle(lamps,setLamps,l)} dot={LAMP_COLORS[l]}>{l}</MiniPill>
                ))}
              </div>
            </Section>

          </div>
        )}

        {/* Mobile helper text when no filter/search/watching active */}
        {isMobile && !hasFilter && (
          <div style={{textAlign:"center",padding:"24px 20px 12px"}}>
            <div style={{fontFamily:FONTS.display,fontSize:22,fontWeight:800,color:COLORS.borderSubtle,letterSpacing:"-.03em",marginBottom:8}}>Find a fixture</div>
            <div style={{fontFamily:FONTS.ui,fontSize:13,color:COLORS.textMuted,lineHeight:1.55,maxWidth:340,margin:"0 auto"}}>
              Pick an <strong style={{color:APP_COLORS["Theater"],fontWeight:600}}>application</strong> or <strong style={{color:TIER_COLORS["Large"],fontWeight:600}}>output tier</strong> — or search by name.
            </div>
          </div>
        )}

        {/* ── RESULTS ── */}
        {!hasFilter ? (isMobile ? null : <EmptyState/>) : filtered.length===0 ? (
          <>
            {(watchingFilterActive || activeChips.length > 0) && (
              <ActiveFilterBar
                chips={activeChips}
                resultCount={filtered.length}
                onClear={clearAll}
                watchingActive={watchingFilterActive}
                onExitWatching={()=>setWatchingFilterActive(false)}
              />
            )}
            <div style={{textAlign:"center",padding:"70px 20px",color:COLORS.textSecondary}}>
              <div style={{fontSize:17,fontWeight:700,marginBottom:10}}>No fixtures match</div>
              <button onClick={clearAll} style={{padding:"9px 18px",background:COLORS.bgElevated,border:`1px solid ${COLORS.borderDefault}`,borderRadius:RADIUS.md,color:COLORS.textSecondary,fontSize:16,cursor:"pointer",fontFamily:FONTS.ui,fontWeight:600}}>Clear filters</button>
            </div>
          </>
        ) : (
          <>
            {(watchingFilterActive || activeChips.length > 0) && (
              <ActiveFilterBar
                chips={activeChips}
                resultCount={filtered.length}
                onClear={clearAll}
                watchingActive={watchingFilterActive}
                onExitWatching={()=>setWatchingFilterActive(false)}
              />
            )}
            <div style={{display:"flex",alignItems:"center",justifyContent:"space-between",marginBottom:12}}>
              <div style={{fontSize:16,color:COLORS.textSecondary}}>
                <span style={{color:COLORS.textPrimary,fontWeight:700,fontSize:17}}>{filtered.length}</span> results
                {activeCount>0&&<span onClick={clearAll} style={{marginLeft:10,fontSize:16,color:"#8A8A98",cursor:"pointer",fontFamily:FONTS.mono,letterSpacing:".02em"}}>CLEAR ALL</span>}
              </div>
              <select value={sortBy} onChange={e=>setSortBy(e.target.value)}
                style={{background:COLORS.bgElevated,border:"1px solid #222228",borderRadius:8,color:COLORS.textSecondary,fontSize:16,padding:"8px 10px",outline:"none",fontFamily:FONTS.mono,cursor:"pointer"}}>
                <option value="output-desc">Output {"\u2193"}</option>
                <option value="output-asc">Output {"\u2191"}</option>
                <option value="cri-desc">CRI {"\u2193"}</option>
                <option value="watts-desc">Wattage {"\u2193"}</option>
                <option value="zoom-asc">Tightest zoom</option>
                <option value="model-asc">Model A{"\u2013"}Z</option>
              </select>
            </div>

            {!isMobile&&(
              <div style={{display:"grid",gridTemplateColumns:"56px 1fr 88px 88px 88px 88px 88px 28px",padding:"7px 16px",marginBottom:2}}>
                <span/><span style={{fontSize:16,fontWeight:700,color:COLORS.textSecondary,letterSpacing:".06em",fontFamily:FONTS.mono}}>FIXTURE</span>
                {["OUTPUT","FRAMING","ZOOM","CRI","WATTS"].map(h=>(
                  <span key={h} style={{fontSize:14,fontWeight:600,color:"#6E6E7C",letterSpacing:".08em",fontFamily:FONTS.mono,textAlign:"right"}}>{h}</span>
                ))}
                <span/>
              </div>
            )}

            <div style={{border:"1px solid #18181C",borderRadius:13,overflow:"hidden",background:"#0C0C0E"}}>
              {filtered.map((f,i)=>(
                <ResultRow key={f.id} f={f} isMobile={isMobile} last={i===filtered.length-1}
                  expanded={expanded.has(f.id)} onToggle={()=>toggleExpand(f.id)}
                  inCompare={inCompare(f.id)} compareFull={compare.length>=4} onCompare={()=>toggleCompare(f)}
                  isWatched={isWatched(f.id)} onWatch={()=>toggleWatch(f.id)}/>
              ))}
            </div>
          </>
        )}
      </div>

      {isMobile&&compare.length>0&&(
        <div style={{position:"fixed",bottom:0,left:0,right:0,background:COLORS.bgElevated,borderTop:"1px solid #1C1C22",padding:"12px 16px",zIndex:150,display:"flex",alignItems:"center",gap:10}}>
          <div style={{fontSize:17,color:COLORS.textSecondary,flex:1}}><span style={{color:COLORS.actionAmber,fontWeight:700}}>{compare.length}</span> to compare</div>
          <button onClick={()=>setCompare([])} style={{padding:"9px 14px",background:"#1A1A20",border:"none",borderRadius:8,color:COLORS.textSecondary,fontSize:17,fontWeight:700,fontFamily:FONTS.ui}}>Clear</button>
          <button onClick={()=>setShowCompare(true)} style={{padding:"9px 18px",background:COLORS.actionAmber,border:"none",borderRadius:8,color:COLORS.bgBase,fontSize:17,fontWeight:700,fontFamily:FONTS.ui,display:"flex",alignItems:"center",gap:6}}>
            <GitCompare size={14}/> Compare
          </button>
        </div>
      )}

      {showCompare&&<CompareModal items={compare} isMobile={isMobile} onClose={()=>setShowCompare(false)} onRemove={id=>setCompare(c=>c.filter(x=>x.id!==id))}/>}

      <BrandPickerSheet
        open={showBrandPicker}
        onClose={()=>setShowBrandPicker(false)}
        allBrands={allBrands}
        brands={brands}
        toggleBrand={b => toggle(brands, setBrands, b)}
        fixtures={FIXTURES}
      />

      <MobileMenu
        open={showMobileMenu}
        onClose={()=>setShowMobileMenu(false)}
        watchingFilterActive={watchingFilterActive}
        onToggleWatching={()=>setWatchingFilterActive(v=>!v)}
        watchlistSize={watchlist.size}
        compareCount={compare.length}
        onOpenCompare={()=>setShowCompare(true)}
      />
    </div>
  );
}

function Section({label,active,children}){
  return(
    <div style={{marginBottom:18}}>
      <div style={{display:"flex",alignItems:"center",gap:10,marginBottom:9}}>
        <span style={{fontFamily:FONTS.ui,fontSize:12,fontWeight:700,color:COLORS.textMuted,letterSpacing:".08em",textTransform:"uppercase"}}>{label}</span>
      </div>
      {children}
    </div>
  );
}

function SubGroup({label,children}){
  return(
    <div style={{marginBottom:14}}>
      <div style={{fontSize:11,fontWeight:600,color:COLORS.textMuted,letterSpacing:".1em",textTransform:"uppercase",fontFamily:FONTS.mono,marginBottom:8}}>{label}</div>
      {children}
    </div>
  );
}

function MiniPill({active,onClick,children,dot}){
  return(
    <div className="chip" onClick={onClick}
      style={{display:"inline-flex",alignItems:"center",gap:6,padding:"7px 12px",background:active?COLORS.actionAmberBg:"transparent",border:`1px solid ${active?COLORS.actionAmber:COLORS.borderDefault}`,borderRadius:RADIUS.sm,fontSize:13,color:active?COLORS.actionAmber:COLORS.textSecondary,fontWeight:600,cursor:"pointer",fontFamily:FONTS.ui}}>
      {dot&&<span style={{width:7,height:7,borderRadius:"50%",background:dot}}/>}
      {children}
      {active&&<Check size={11}/>}
    </div>
  );
}

function ActiveFilterBar({chips, resultCount, onClear, watchingActive, onExitWatching}){
  return(
    <div style={{position:"sticky",top:0,zIndex:10,background:COLORS.activeBarBg,border:`1px solid ${COLORS.activeBarBorder}`,borderRadius:RADIUS.lg,padding:"10px 14px",marginBottom:14,display:"flex",alignItems:"center",gap:12,flexWrap:"wrap"}}>
      <span style={{fontFamily:FONTS.mono,fontSize:11,color:COLORS.textMuted,fontWeight:600,letterSpacing:".08em",textTransform:"uppercase"}}>Filtering</span>

      {watchingActive && (
        <div style={{display:"inline-flex",alignItems:"center",gap:6,padding:"4px 10px",background:COLORS.actionAmber,color:COLORS.bgBase,borderRadius:RADIUS.sm,fontFamily:FONTS.ui,fontSize:13,fontWeight:600}}>
          <Star size={12} fill={COLORS.bgBase}/>
          Watching
          <X size={12} onClick={onExitWatching} style={{cursor:"pointer",marginLeft:2}}/>
        </div>
      )}

      {chips.map(c=>(
        <div key={c.key} style={{display:"inline-flex",alignItems:"center",gap:6,padding:"4px 10px",background:COLORS.bgElevated,border:`1px solid ${COLORS.borderDefault}`,borderRadius:RADIUS.sm,fontFamily:FONTS.ui,fontSize:13,color:COLORS.textPrimary}}>
          <span>{c.label}</span>
          <X size={12} onClick={c.onRemove} style={{cursor:"pointer",color:COLORS.textMuted}}/>
        </div>
      ))}

      <div style={{marginLeft:"auto",display:"flex",alignItems:"center",gap:14}}>
        <span style={{fontFamily:FONTS.mono,fontSize:13,color:COLORS.textSecondary}}>
          <span style={{color:COLORS.textPrimary,fontWeight:700}}>{resultCount}</span> results
        </span>
        <span onClick={onClear} style={{cursor:"pointer",fontFamily:FONTS.ui,fontSize:12,fontWeight:600,color:COLORS.textMuted,letterSpacing:".06em",textTransform:"uppercase"}}>Clear all</span>
      </div>
    </div>
  );
}

function EmptyState(){
  return(
    <div style={{textAlign:"center",padding:"80px 20px"}}>
      <div style={{fontFamily:FONTS.display,fontSize:30,fontWeight:800,color:COLORS.borderSubtle,letterSpacing:"-.03em",marginBottom:10}}>Find a fixture</div>
      <div style={{fontFamily:FONTS.ui,fontSize:15,color:COLORS.textMuted,lineHeight:1.7,maxWidth:400,margin:"0 auto",fontWeight:400}}>
        Pick an <span style={{color:APP_COLORS["Theater"],fontWeight:600}}>application</span>, <span style={{color:CAT_COLORS["Performance"],fontWeight:600}}>type</span>, or <span style={{color:TIER_COLORS["Large"],fontWeight:600}}>output tier</span> — or search by name.
      </div>
    </div>
  );
}

function ResultRow({f,expanded,onToggle,inCompare,compareFull,onCompare,last,isMobile,isWatched,onWatch}){
  const catCol=CAT_COLORS[f.category]||"#888";
  const hasImg=!!f.imageUrl;
  return(
    <div style={{borderBottom:last&&!expanded?"none":"1px solid #131316",background:expanded?COLORS.bgElevated:"transparent"}}>
      <div className="fx-row" onClick={onToggle}
        style={{display:"grid",gridTemplateColumns:isMobile?"56px 1fr auto 36px 36px":"56px 1fr 80px 70px 80px 60px 70px 28px 28px 28px",padding:isMobile?"12px 14px":"12px 16px",cursor:"pointer",alignItems:"center",gap:0}}>

        {/* Thumbnail */}
        <div style={{width:48,height:48,borderRadius:7,overflow:"hidden",background:"#131316",border:"1px solid #1C1C22",display:"flex",alignItems:"center",justifyContent:"center",flexShrink:0}}>
          {hasImg
            ?<img src={f.imageUrl} alt={f.model} style={{width:"100%",height:"100%",objectFit:"cover"}} onError={e=>e.target.style.display="none"}/>
            :<div style={{width:14,height:14,borderRadius:3,background:catCol,opacity:.35}}/>
          }
        </div>

        {/* Name */}
        <div style={{paddingLeft:12,minWidth:0}}>
          <div style={{display:"flex",alignItems:"center",gap:6}}>
            <span style={{fontFamily:FONTS.display,fontSize:isMobile?17:18,fontWeight:600,letterSpacing:"-.02em",overflow:"hidden",textOverflow:"ellipsis",whiteSpace:"nowrap",color:COLORS.textPrimary}}>{clean(f.model)}</span>
          </div>
          <div style={{display:"flex",alignItems:"center",gap:6,marginTop:3}}>
            <span style={{fontSize:14,fontWeight:600,color:COLORS.brandPeriwinkle,letterSpacing:".04em",textTransform:"uppercase",fontFamily:FONTS.mono}}>{f.brand}</span>
            <span style={{fontSize:10.5,color:catCol,background:catCol+"22",padding:"2px 6px",borderRadius:3,fontWeight:700,textTransform:"uppercase",letterSpacing:".04em",fontFamily:FONTS.mono}}>{catLabel(f.category)}</span>
          </div>
          {f.standout&&(
            <div style={{display:"inline-flex",alignItems:"center",gap:6,marginTop:5,fontFamily:FONTS.ui,fontSize:11.5,fontWeight:500,color:COLORS.standoutCyanMuted,letterSpacing:".01em"}}>
              <span style={{width:4,height:4,borderRadius:"50%",background:COLORS.standoutCyan,flexShrink:0}}/>
              {clean(f.standout)}
            </div>
          )}
        </div>

        {/* Desktop specs */}
        {!isMobile&&<>
          <div style={{textAlign:"right",paddingRight:8}}>
            {f.outputLumens
              ? <span style={{fontSize:14,fontWeight:500,fontFamily:FONTS.mono,color:"#DCDCE2"}}>{fmt(f.outputLumens)}<span style={{fontSize:11,color:COLORS.textGhost,marginLeft:2}}>lm</span></span>
              : <span style={{fontSize:14,color:COLORS.textGhost}}>{"\u2014"}</span>}
          </div>
          <div style={{textAlign:"right",paddingRight:8}}>
            {f.framing
              ?<span style={{display:"inline-flex",alignItems:"center",gap:4,fontSize:13,fontFamily:FONTS.mono,color:"#DCDCE2"}}><Scissors size={10}/> Yes</span>
              :<span style={{fontSize:13,color:COLORS.textGhost,fontFamily:FONTS.mono}}>{"\u2014"}</span>}
          </div>
          <div style={{textAlign:"right",paddingRight:8}}>
            <span style={{fontSize:13,fontFamily:FONTS.mono,color:"#DCDCE2"}}>{zoomStr(f)}</span>
          </div>
          <div style={{textAlign:"right",paddingRight:8}}>
            {f.cri!=null
              ?<span style={{fontSize:14,fontWeight:600,fontFamily:FONTS.mono,color:COLORS.textSecondary}}>{f.cri}</span>
              :<span style={{fontSize:14,color:COLORS.textGhost,fontFamily:FONTS.mono}}>{"\u2014"}</span>}
          </div>
          <div style={{textAlign:"right",paddingRight:8}}>
            <span style={{fontSize:14,fontWeight:500,fontFamily:FONTS.mono,color:"#DCDCE2"}}>{f.watts?f.watts+"W":"\u2014"}</span>
          </div>
        </>}

        {/* Mobile specs */}
        {isMobile&&(
          <div style={{textAlign:"right",paddingRight:6}}>
            <div style={{fontSize:13,fontFamily:FONTS.mono,color:"#DCDCE2"}}>{f.outputLumens?fmt(f.outputLumens):"\u2014"}<span style={{fontSize:10,color:COLORS.textGhost,marginLeft:1}}>lm</span></div>
            <div style={{display:"flex",gap:5,justifyContent:"flex-end",marginTop:3}}>
              {f.cri!=null&&<span style={{fontSize:11,fontFamily:FONTS.mono,color:COLORS.textSecondary,fontWeight:600}}>CRI {f.cri}</span>}
            </div>
          </div>
        )}

        {/* Mobile Watch button */}
        {isMobile&&(
          <div style={{display:"flex",alignItems:"center",justifyContent:"center",width:36,height:36}} onClick={e=>{e.stopPropagation();onWatch();}}>
            <Star size={18} fill={isWatched?COLORS.actionAmber:"none"} color={isWatched?COLORS.actionAmber:COLORS.textGhost}/>
          </div>
        )}

        {/* Mobile Compare button */}
        {isMobile&&(
          <div style={{display:"flex",alignItems:"center",justifyContent:"center",width:36,height:36}} onClick={e=>{e.stopPropagation();(!compareFull||inCompare)&&onCompare();}}>
            <div style={{width:30,height:30,borderRadius:RADIUS.sm,
              border:`1px solid ${inCompare?COLORS.actionAmber:COLORS.borderDefault}`,
              background:inCompare?COLORS.actionAmber:"transparent",
              display:"flex",alignItems:"center",justifyContent:"center",
              color:inCompare?COLORS.bgBase:COLORS.textGhost}}>
              {inCompare?<Check size={14}/>:<Plus size={14}/>}
            </div>
          </div>
        )}

        {/* Desktop Watch button */}
        {!isMobile&&(
          <div style={{display:"flex",justifyContent:"center"}} onClick={e=>{e.stopPropagation();onWatch();}}>
            <Star size={16} fill={isWatched?COLORS.actionAmber:"none"} color={isWatched?COLORS.actionAmber:COLORS.textGhost} style={{cursor:"pointer"}}/>
          </div>
        )}

        {/* Desktop Compare button */}
        {!isMobile&&(
          <div style={{display:"flex",justifyContent:"center"}} onClick={e=>{e.stopPropagation();(!compareFull||inCompare)&&onCompare();}}>
            <div style={{width:24,height:24,borderRadius:RADIUS.sm,
              border:`1px solid ${inCompare?COLORS.actionAmber:COLORS.borderDefault}`,
              background:inCompare?COLORS.actionAmber:"transparent",
              display:"flex",alignItems:"center",justifyContent:"center",
              color:inCompare?COLORS.bgBase:(compareFull?COLORS.borderDefault:COLORS.textGhost),
              cursor:(!inCompare&&compareFull)?"default":"pointer"}}>
              {inCompare?<Check size={13}/>:<Plus size={13}/>}
            </div>
          </div>
        )}

        {/* Chevron — desktop only */}
        {!isMobile&&(
          <div style={{color:COLORS.textGhost,display:"flex",justifyContent:"center"}}>
            {expanded?<ChevronUp size={15}/>:<ChevronDown size={15}/>}
          </div>
        )}
      </div>

      {/* Expanded card */}
      {expanded&&(
        <div className="expand-in" style={{padding:isMobile?"0 12px 12px":"0 16px 18px"}}>
          <div style={{background:COLORS.bgCardSurface,border:"1px solid #18181C",borderRadius:12,overflow:"hidden"}}>

            {/* Card header: image left, text right */}
            <div style={{display:"flex",flexDirection:isMobile?"column":"row",borderBottom:"1px solid #131316"}}>
              {/* Image panel */}
              <div style={{width:isMobile?"100%":240,minWidth:isMobile?undefined:240,height:isMobile?150:220,background:COLORS.bgElevated,display:"flex",alignItems:"center",justifyContent:"center",flexShrink:0}}>
                {hasImg
                  ?<img src={f.imageUrl} alt={f.model} style={{width:"100%",height:"100%",objectFit:"contain",padding:isMobile?8:12}} onError={e=>{e.target.style.display="none";e.target.nextSibling&&(e.target.nextSibling.style.display="flex");}}/>
                  :null}
                {hasImg
                  ?<div style={{display:"none",alignItems:"center",justifyContent:"center",width:"100%",height:"100%"}}>
                    <div style={{width:isMobile?40:48,height:isMobile?40:48,borderRadius:8,background:catCol+"22",border:`2px solid ${catCol}44`}}/>
                  </div>
                  :<div style={{width:isMobile?40:48,height:isMobile?40:48,borderRadius:8,background:catCol+"22",border:`2px solid ${catCol}44`}}/>}
              </div>
              {/* Text panel */}
              <div style={{flex:1,padding:isMobile?"14px 16px":"22px 26px",display:"flex",flexDirection:"column",justifyContent:"center"}}>
                <div style={{display:"flex",gap:5,flexWrap:"wrap",marginBottom:isMobile?8:12}}>
                  {(f.applications||[]).map(a=>(
                    <span key={a} style={{fontSize:isMobile?10:11,fontWeight:700,color:APP_COLORS[a],background:APP_COLORS[a]+"1A",padding:isMobile?"2px 6px":"3px 8px",borderRadius:4,textTransform:"uppercase",letterSpacing:".05em",fontFamily:FONTS.mono}}>{a}</span>
                  ))}
                  {f.tier&&<span style={{fontSize:isMobile?10:11,fontWeight:700,color:TIER_COLORS[f.tier],background:TIER_COLORS[f.tier]+"1A",padding:isMobile?"2px 6px":"3px 8px",borderRadius:4,textTransform:"uppercase",letterSpacing:".05em",fontFamily:FONTS.mono}}>{f.tier}</span>}
                  {f.ipRated&&<span style={{fontSize:isMobile?10:11,fontWeight:700,color:"#9D8DF1",background:"#9D8DF11A",padding:isMobile?"2px 6px":"3px 8px",borderRadius:4,textTransform:"uppercase",letterSpacing:".05em",fontFamily:FONTS.mono}}>{f.ipRating||"IP Rated"}</span>}
                </div>
                <div style={{fontFamily:FONTS.display,fontSize:isMobile?23:38,fontWeight:700,letterSpacing:"-.035em",lineHeight:1.05,color:COLORS.textPrimary}}>{clean(f.model)}</div>
                <div style={{fontSize:isMobile?12:14,fontWeight:600,color:COLORS.brandPeriwinkle,letterSpacing:".05em",textTransform:"uppercase",fontFamily:FONTS.mono,marginTop:isMobile?5:8}}>{f.brand} · {catDisplayName(f.category)}</div>
                {f.standout&&(
                  <div style={{display:"inline-flex",alignItems:"center",gap:6,marginTop:isMobile?9:14,padding:isMobile?"5px 9px":"7px 11px",background:COLORS.standoutCyanBg,border:`1px solid ${COLORS.standoutCyanBorder}`,borderRadius:6,fontFamily:FONTS.ui,fontSize:isMobile?12:13,fontWeight:500,color:COLORS.standoutCyanText,alignSelf:"flex-start"}}>
                    <span style={{width:5,height:5,borderRadius:"50%",background:COLORS.standoutCyan,flexShrink:0}}/>
                    {clean(f.standout)}
                  </div>
                )}
                {f.description&&(
                  <div style={{fontFamily:FONTS.ui,fontSize:isMobile?13:14,color:COLORS.textMuted,lineHeight:1.5,marginTop:isMobile?(f.standout?8:10):(f.standout?12:14)}}>{clean(f.description)}</div>
                )}
              </div>
            </div>

            {/* Spec grid */}
            <div style={{padding:isMobile?"10px 12px":"14px 20px"}}>
              <div style={{display:"grid",gridTemplateColumns:isMobile?"1fr 1fr":"1fr 1fr 1fr",gap:isMobile?6:8,marginBottom:isMobile?9:12}}>
                <SB label="Max Output" value={f.outputLumens?fmt(f.outputLumens)+" lm":"\u2014"} isMobile={isMobile}/>
                <SB label="Framing Shutters" value={f.framing?"Yes":"No"} hl={f.framing} isMobile={isMobile}/>
                <SB label="CRI" value={clean(f.criRaw)||(f.cri!=null?String(f.cri):"\u2014")} isMobile={isMobile}/>
                <SB label="Lamp" value={(f.watts?f.watts+"W ":"")+(f.lampType||"")||"\u2014"} isMobile={isMobile}/>
                <SB label="Color Temp" value={clean(f.cct)||clean(f.cctRange)||"\u2014"} isMobile={isMobile}/>
                <SB label="Zoom" value={f.zoomMin!=null?zoomStr(f)+(f.zoomRatio?" ("+f.zoomRatio+")":""):(clean(f.zoomRaw)||"\u2014")} isMobile={isMobile}/>
                <SB label="Color Mixing" value={clean(f.colorMixing)||"\u2014"} isMobile={isMobile}/>
                <SB label="Pan / Tilt" value={clean(f.panTilt)||"\u2014"} isMobile={isMobile}/>
                <SB label="Weight" value={f.weightKg?f.weightKg+" kg":"\u2014"} isMobile={isMobile}/>
                <SB label="IP Rating" value={clean(f.ipRating)||"\u2014"} isMobile={isMobile}/>
                <SB label="Power Draw" value={f.powerConsumption?f.powerConsumption+" W":"\u2014"} isMobile={isMobile}/>
                <SB label="DMX Channels" value={clean(f.dmxChannels)||"\u2014"} isMobile={isMobile}/>
                <SB label="Gobo" value={clean(f.gobo)||"\u2014"} wide isMobile={isMobile}/>
                <SB label="Effects" value={clean(f.effectsRaw)||"\u2014"} wide isMobile={isMobile}/>
                <SB label="Protocols" value={clean(f.protocols)||"\u2014"} wide isMobile={isMobile}/>
              </div>
              <div style={{display:"flex",gap:isMobile?6:8,flexWrap:"wrap"}}>
                <button onClick={e=>{e.stopPropagation();onCompare();}} disabled={!inCompare&&compareFull}
                  style={{flex:"1 1 140px",padding:isMobile?"10px":"11px",background:inCompare?COLORS.actionAmber:COLORS.bgElevated,border:`1px solid ${inCompare?COLORS.actionAmber:COLORS.borderDefault}`,borderRadius:9,color:inCompare?COLORS.bgBase:(compareFull?"#6E6E7C":COLORS.textPrimary),fontSize:isMobile?13:14,fontWeight:700,cursor:(!inCompare&&compareFull)?"default":"pointer",fontFamily:FONTS.ui,display:"flex",alignItems:"center",justifyContent:"center",gap:6}}>
                  {inCompare?<><Minus size={13}/> Remove</>:<><Plus size={13}/> Compare</>}
                </button>
                {f.link
                  ?<a href={f.link} target="_blank" rel="noopener noreferrer" onClick={e=>e.stopPropagation()}
                      style={{flex:"1 1 140px",padding:isMobile?"10px":"11px",background:COLORS.bgElevated,border:"1px solid #222228",borderRadius:9,color:COLORS.textPrimary,fontSize:isMobile?13:14,fontWeight:700,fontFamily:FONTS.ui,display:"flex",alignItems:"center",justifyContent:"center",gap:6}}>
                      <ExternalLink size={13}/> Product page
                    </a>
                  :<div style={{flex:"1 1 140px",padding:isMobile?"10px":"11px",background:COLORS.bgBase,borderRadius:9,color:"#6E6E7C",fontSize:isMobile?13:14,fontWeight:600,fontFamily:FONTS.ui,display:"flex",alignItems:"center",justifyContent:"center",gap:6}}>
                      <ExternalLink size={12}/> No link yet
                    </div>
                }
              </div>
              {f.lastVerified&&<div style={{fontFamily:FONTS.mono,fontSize:isMobile?10:11,color:COLORS.textDim,marginTop:isMobile?9:12,letterSpacing:".05em"}}>VERIFIED {f.lastVerified}</div>}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

function SB({label,value,wide,hl,isMobile}){
  return(
    <div style={{background:COLORS.bgElevated,border:`1px solid ${COLORS.borderSubtle}`,borderRadius:RADIUS.md,padding:isMobile?"8px 10px":"11px 13px",gridColumn:wide?"1 / -1":"auto"}}>
      <div style={{fontFamily:FONTS.mono,fontSize:isMobile?10:11,fontWeight:600,color:COLORS.specLabelAmber,textTransform:"uppercase",letterSpacing:".1em",marginBottom:isMobile?4:6}}>{label}</div>
      <div style={{fontFamily:FONTS.mono,fontSize:isMobile?12.5:14,color:COLORS.textSecondary,whiteSpace:"pre-line",lineHeight:1.4}}>{value}</div>
    </div>
  );
}

function BrandPickerSheet({open, onClose, allBrands, brands, toggleBrand, fixtures}){
  if(!open) return null;
  const others = allBrands.filter(b => !MAIN_BRANDS.includes(b)).sort();

  return(
    <div onClick={onClose}
      style={{position:"fixed",inset:0,background:COLORS.sheetOverlay,zIndex:100,display:"flex",alignItems:"flex-end",justifyContent:"center"}}>
      <div onClick={e=>e.stopPropagation()} className="slide-up"
        style={{background:COLORS.sheetSurface,borderTopLeftRadius:RADIUS.xl,borderTopRightRadius:RADIUS.xl,width:"100%",maxWidth:480,maxHeight:"85dvh",display:"flex",flexDirection:"column",overflow:"hidden",border:`1px solid ${COLORS.borderSubtle}`}}>

        {/* Sheet header */}
        <div style={{display:"flex",alignItems:"center",justifyContent:"space-between",padding:"16px 20px",borderBottom:`1px solid ${COLORS.borderSubtle}`,flexShrink:0}}>
          <div style={{fontFamily:FONTS.display,fontSize:19,fontWeight:700,color:COLORS.textPrimary,letterSpacing:"-.01em"}}>All brands</div>
          <X size={22} onClick={onClose} style={{cursor:"pointer",color:COLORS.textMuted}}/>
        </div>

        {/* Scrollable brand list */}
        <div style={{overflowY:"auto",padding:"12px 16px",display:"flex",flexDirection:"column",gap:4,WebkitOverflowScrolling:"touch"}}>
          {others.map(b=>{
            const on=brands.has(b);
            const n=fixtures.filter(f=>f.brand===b).length;
            if(n===0) return null;
            return(
              <div key={b} onClick={()=>toggleBrand(b)}
                style={{display:"flex",alignItems:"center",gap:10,padding:"12px 12px",background:on?COLORS.standoutCyanBg:"transparent",border:`1px solid ${on?COLORS.standoutCyan:"transparent"}`,borderRadius:RADIUS.md,fontFamily:FONTS.mono,fontSize:15,fontWeight:600,color:on?COLORS.standoutCyan:COLORS.brandPeriwinkle,textTransform:"uppercase",letterSpacing:".03em",cursor:"pointer"}}>
                <div style={{width:20,height:20,borderRadius:3,background:COLORS.brandLogoBg,flexShrink:0,display:"flex",alignItems:"center",justifyContent:"center",fontSize:11,fontWeight:700,color:COLORS.textMuted}}>{b[0]}</div>
                <span style={{flex:1}}>{b}</span>
                <span style={{fontSize:13,color:on?COLORS.standoutCyan+"AA":COLORS.textDim,fontWeight:500}}>{n}</span>
                {on&&<Check size={15}/>}
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

function MobileMenu({open, onClose, watchingFilterActive, onToggleWatching, watchlistSize, compareCount, onOpenCompare}){
  if(!open) return null;

  return(
    <div onClick={onClose}
      style={{position:"fixed",inset:0,background:COLORS.sheetOverlay,zIndex:100,display:"flex",justifyContent:"flex-end"}}>
      <div onClick={e=>e.stopPropagation()}
        style={{background:COLORS.sheetSurface,width:"min(80vw, 320px)",height:"100%",display:"flex",flexDirection:"column",borderLeft:`1px solid ${COLORS.borderSubtle}`,padding:"20px",animation:"sr .22s cubic-bezier(.2,.8,.2,1)"}}>

        <style>{`@keyframes sr{from{transform:translateX(100%)}to{transform:translateX(0)}}`}</style>

        {/* Close button */}
        <div style={{display:"flex",justifyContent:"flex-end",marginBottom:20}}>
          <X size={22} onClick={onClose} style={{cursor:"pointer",color:COLORS.textMuted}}/>
        </div>

        {/* Workflows section header */}
        <div style={{fontFamily:FONTS.mono,fontSize:10,color:COLORS.textMuted,letterSpacing:".1em",textTransform:"uppercase",marginBottom:10,fontWeight:700}}>Workflows</div>

        {/* Watching */}
        <div onClick={()=>{onToggleWatching();onClose();}}
          style={{display:"flex",alignItems:"center",gap:12,padding:"14px 12px",borderRadius:RADIUS.md,background:watchingFilterActive?COLORS.actionAmber:"transparent",border:`1px solid ${watchingFilterActive?COLORS.actionAmber:COLORS.borderDefault}`,cursor:"pointer",marginBottom:8}}>
          <Star size={16} fill={watchingFilterActive?COLORS.bgBase:(watchlistSize?COLORS.actionAmber:"none")} color={watchingFilterActive?COLORS.bgBase:COLORS.actionAmber}/>
          <span style={{fontFamily:FONTS.ui,fontSize:15,fontWeight:600,color:watchingFilterActive?COLORS.bgBase:COLORS.textPrimary,flex:1}}>Watching</span>
          <span style={{fontFamily:FONTS.mono,fontSize:13,color:watchingFilterActive?COLORS.bgBase+"DD":COLORS.textMuted,fontWeight:600}}>{watchlistSize}</span>
        </div>

        {/* Compare */}
        <div onClick={()=>{if(compareCount){onOpenCompare();onClose();}}}
          style={{display:"flex",alignItems:"center",gap:12,padding:"14px 12px",borderRadius:RADIUS.md,background:"transparent",border:`1px solid ${compareCount?COLORS.actionAmber:COLORS.borderDefault}`,opacity:compareCount?1:0.5,cursor:compareCount?"pointer":"default",marginBottom:24}}>
          <GitCompare size={16} color={compareCount?COLORS.actionAmber:COLORS.textMuted}/>
          <span style={{fontFamily:FONTS.ui,fontSize:15,fontWeight:600,color:COLORS.textPrimary,flex:1}}>Compare</span>
          <span style={{fontFamily:FONTS.mono,fontSize:13,color:COLORS.textMuted,fontWeight:600}}>{compareCount}/4</span>
        </div>

        {/* Placeholder for future items */}
        <div style={{fontFamily:FONTS.mono,fontSize:10,color:COLORS.textDim,letterSpacing:".1em",textTransform:"uppercase",fontWeight:700,marginTop:8}}>More coming soon</div>

        {/* Footer */}
        <div style={{marginTop:"auto",fontFamily:FONTS.mono,fontSize:10,color:COLORS.textDim,letterSpacing:".05em",textTransform:"uppercase"}}>Moving Light Database</div>
      </div>
    </div>
  );
}

function CompareModal({items,onClose,onRemove,isMobile}){
  if(!items.length) return null;
  const fields=[
    ["type","Type",f=>catDisplayName(f.category)],
    ["apps","Applications",f=>(f.applications||[]).join(", ")||"\u2014"],
    ["framing","Framing",f=>f.framing?"Yes":"No"],
    ["output","Max Output",f=>f.outputLumens?fmt(f.outputLumens)+" lm":"\u2014",f=>f.outputLumens||0],
    ["cri","CRI",f=>f.cri!=null?(clean(f.criRaw)||String(f.cri)):"\u2014",f=>f.cri||0],
    ["watts","Wattage",f=>f.watts?f.watts+" W":"\u2014",f=>f.watts||0],
    ["lamp","Light Source",f=>f.lampType||"\u2014"],
    ["cct","Color Temp",f=>clean(f.cct)||clean(f.cctRange)||"\u2014"],
    ["color","Color Mixing",f=>clean(f.colorMixing)||"\u2014"],
    ["zoom","Zoom Range",f=>f.zoomMin!=null?zoomStr(f)+(f.zoomRatio?" ("+f.zoomRatio+")":""):"\u2014"],
    ["zoomMin","Tightest Zoom",f=>f.zoomMin!=null?f.zoomMin+"\u00b0":"\u2014",f=>f.zoomMin!=null?-f.zoomMin:-999],
    ["pan","Pan / Tilt",f=>clean(f.panTilt)||"\u2014"],
    ["weight","Weight",f=>f.weightKg?f.weightKg+" kg":"\u2014",f=>f.weightKg?-f.weightKg:-999],
    ["ip","IP Rating",f=>clean(f.ipRating)||"\u2014"],
    ["power","Power Draw",f=>f.powerConsumption?f.powerConsumption+" W":"\u2014"],
    ["dmx","DMX Channels",f=>clean(f.dmxChannels)||"\u2014"],
    ["proto","Protocols",f=>clean(f.protocols)||"\u2014"],
    ["anim","Animation",f=>f.animationWheel?"Yes":"No"],
    ["gobo","Gobo",f=>clean(f.gobo)||"\u2014"],
    ["effects","Effects",f=>clean(f.effectsRaw)||"\u2014"],
  ];
  return(
    <div onClick={onClose} style={{position:"fixed",inset:0,background:"rgba(0,0,0,.85)",backdropFilter:"blur(4px)",display:"flex",alignItems:isMobile?"flex-end":"center",justifyContent:"center",zIndex:100,padding:isMobile?0:16}}>
      <div className={isMobile?"slide-up":""} style={{background:"#0C0C0E",border:"1px solid #1C1C22",borderRadius:isMobile?"16px 16px 0 0":14,width:isMobile?"100%":"min(1100px,96vw)",maxHeight:isMobile?"92vh":"90vh",overflow:"hidden",display:"flex",flexDirection:"column"}} onClick={e=>e.stopPropagation()}>
        <div style={{padding:isMobile?"16px 18px":"18px 24px",borderBottom:"1px solid #18181C",display:"flex",justifyContent:"space-between",alignItems:"center"}}>
          <div style={{fontSize:isMobile?18:21,fontWeight:800,display:"flex",alignItems:"center",gap:10,letterSpacing:"-.02em"}}>
            <GitCompare size={isMobile?17:20} color={COLORS.actionAmber}/> Compare
            <span style={{fontSize:15,color:"#8A8A98",fontFamily:FONTS.mono}}>{items.length}/4</span>
          </div>
          <X size={22} onClick={onClose} style={{cursor:"pointer",color:"#8A8A98"}}/>
        </div>
        <div style={{overflow:"auto"}}>
          <table style={{width:"100%",borderCollapse:"collapse",minWidth:(isMobile?120:160)+items.length*(isMobile?145:200)}}>
            <thead>
              <tr style={{background:"#0C0C0E"}}>
                <th style={{position:"sticky",left:0,background:"#0C0C0E",textAlign:"left",padding:isMobile?"12px":"14px 18px",fontSize:14,color:COLORS.specLabelAmber,fontWeight:600,textTransform:"uppercase",letterSpacing:".08em",fontFamily:FONTS.mono,width:isMobile?120:160,zIndex:2}}>Spec</th>
                {items.map(f=>(
                  <th key={f.id} style={{padding:isMobile?"12px":"14px 18px",textAlign:"left",borderLeft:"1px solid #18181C",minWidth:isMobile?145:195,verticalAlign:"top"}}>
                    <div style={{display:"flex",justifyContent:"space-between",alignItems:"flex-start",gap:8}}>
                      <div style={{minWidth:0}}>
                        {/* Thumbnail */}
                        <div style={{width:isMobile?44:56,height:isMobile?44:56,borderRadius:8,overflow:"hidden",background:COLORS.bgElevated,border:`1px solid ${COLORS.borderSubtle}`,display:"flex",alignItems:"center",justifyContent:"center",marginBottom:8}}>
                          {f.imageUrl
                            ? <img src={f.imageUrl} alt={f.model} style={{width:"100%",height:"100%",objectFit:"contain",padding:6}} onError={e=>{e.target.style.display="none";e.target.nextSibling&&(e.target.nextSibling.style.display="flex");}}/>
                            : null}
                          <div style={{display:f.imageUrl?"none":"flex",alignItems:"center",justifyContent:"center",width:"100%",height:"100%"}}>
                            <div style={{width:18,height:18,borderRadius:4,background:(CAT_COLORS[f.category]||"#888")+"33"}}/>
                          </div>
                        </div>
                        <div style={{fontFamily:FONTS.mono,fontSize:isMobile?15:17,fontWeight:700,color:COLORS.brandPeriwinkle,textTransform:"uppercase",letterSpacing:".05em"}}>{f.brand}</div>
                        <div style={{fontFamily:FONTS.display,fontSize:isMobile?15:17,fontWeight:700,marginTop:3,lineHeight:1.2,letterSpacing:"-.01em",color:COLORS.textPrimary}}>{clean(f.model)}</div>
                      </div>
                      <X size={15} onClick={()=>onRemove(f.id)} style={{cursor:"pointer",color:COLORS.textMuted,flexShrink:0}}/>
                    </div>
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {fields.map(([key,label,render],ri)=>{
                return(
                  <tr key={key} style={{background:ri%2?COLORS.bgElevated:"transparent"}}>
                    <td style={{position:"sticky",left:0,background:ri%2?COLORS.bgElevated:COLORS.bgRow,padding:isMobile?"10px 12px":"11px 18px",fontFamily:FONTS.mono,fontSize:12,color:COLORS.specLabelAmber,fontWeight:600,textTransform:"uppercase",letterSpacing:".06em",zIndex:1}}>{label}</td>
                    {items.map(f=>(
                      <td key={f.id} style={{padding:isMobile?"10px 12px":"11px 18px",fontFamily:FONTS.mono,fontSize:isMobile?14:15,borderLeft:`1px solid ${COLORS.borderSubtle}`,color:COLORS.textSecondary,whiteSpace:"pre-line",lineHeight:1.45,verticalAlign:"top"}}>
                        {render(f)}
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
