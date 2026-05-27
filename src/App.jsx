import React, { useState, useMemo, useEffect } from "react";
import { Search, X, GitCompare, ChevronDown, ChevronUp, Check, Plus, Minus, ExternalLink, Scissors, SlidersHorizontal, Droplets, Wifi, Zap } from "lucide-react";

import FIXTURES from "./fixtures.json";

const CAT_COLORS = { "Spot / Profile":"#F5A623", "Wash":"#4ECDC4", "Bar / Batten":"#C77DFF" };
const LAMP_COLORS = { "LED":"#6EE7A8", "Discharge":"#F5A623", "Laser":"#FF6B6B", "Other":"#9AA5B1" };
const APP_COLORS = { "Theater":"#E8B339", "Concert":"#F4845F", "TV-Film":"#FF6B9D", "Corporate":"#9D8DF1" };
const TIER_COLORS = { "Small":"#6EE7A8", "Medium":"#E8B339", "Large":"#F4845F" };
const TIER_DESC = { "Small":"< 10k lm", "Medium":"10\u201330k lm", "Large":"\u2265 30k lm" };
const APP_ORDER = ["Theater","Concert","TV-Film","Corporate"];

const FEAT_FILTERS = [
  { key:"framing",   label:"Framing Shutters", icon:<Scissors size={14}/>,  color:"#6EE7A8", field:f=>f.framing },
  { key:"led",       label:"LED Source",        icon:<Zap size={14}/>,       color:"#6EE7A8", field:f=>f.lampType==="LED" },
  { key:"dualFrost", label:"Dual Frost",        icon:<Droplets size={14}/>,  color:"#4ECDC4", field:f=>f.dualFrost },
  { key:"ipRated",   label:"IP Rated",          icon:<Wifi size={14}/>,      color:"#9D8DF1", field:f=>f.ipRated },
];

function clean(s){ return (s||"").replace(/\s+/g," ").trim(); }
function fmt(n){ return n==null?"\u2014":n.toLocaleString(); }
function zoomStr(f){ return f.zoomMin!=null?(f.zoomMin===f.zoomMax?f.zoomMin+"\u00b0":f.zoomMin+"\u00b0\u2013"+f.zoomMax+"\u00b0"):"\u2014"; }

export default function App() {
  const [query,setQuery]       = useState("");
  const [apps,setApps]         = useState(new Set());
  const [cats,setCats]         = useState(new Set());
  const [tiers,setTiers]       = useState(new Set());
  const [brands,setBrands]     = useState(new Set());
  const [feats,setFeats]       = useState(new Set());
  const [lamps,setLamps]       = useState(new Set());
  const [criMin,setCriMin]     = useState(0);
  const [featAnim,setFeatAnim] = useState(false);
  const [moreOpen,setMoreOpen] = useState(false);
  const [sortBy,setSortBy]     = useState("output-desc");
  const [expanded,setExpanded] = useState(new Set());
  const [compare,setCompare]   = useState([]);
  const [showCompare,setShowCompare] = useState(false);
  const [isMobile,setIsMobile] = useState(false);

  useEffect(()=>{
    const c=()=>setIsMobile(window.innerWidth<760);
    c(); window.addEventListener("resize",c); return()=>window.removeEventListener("resize",c);
  },[]);

  const allBrands = useMemo(()=>[...new Set(FIXTURES.map(f=>f.brand))].sort(),[]);
  const allCats   = ["Spot / Profile","Wash","Bar / Batten"];
  const allTiers  = ["Small","Medium","Large"];
  const allLamps  = ["LED","Discharge","Laser","Other"];

  function toggle(set,setter,val){
    const n=new Set(set); n.has(val)?n.delete(val):n.add(val); setter(n);
  }

  const hasFilter = query||apps.size||cats.size||tiers.size||brands.size||feats.size||lamps.size||criMin||featAnim;
  const moreCount = lamps.size+(criMin?1:0)+(featAnim?1:0);

  const filtered = useMemo(()=>{
    if(!hasFilter) return [];
    let r = FIXTURES.filter(f=>{
      if(query){
        const q=query.toLowerCase();
        const hay=(f.model+" "+f.brand+" "+f.category+" "+(f.unique||"")+" "+(f.description||"")+" "+(f.colorMixing||"")+" "+(f.lamp||"")+" "+(f.applications||[]).join(" ")).toLowerCase();
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
      if(criMin&&!(f.cri!=null&&f.cri>=criMin)) return false;
      if(featAnim&&!f.animationWheel) return false;
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
  },[query,apps,cats,tiers,brands,feats,lamps,criMin,featAnim,sortBy,hasFilter]);

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
  function clearAll(){
    setQuery(""); setApps(new Set()); setCats(new Set()); setTiers(new Set());
    setBrands(new Set()); setFeats(new Set()); setLamps(new Set());
    setCriMin(0); setFeatAnim(false);
  }

  const activeCount=apps.size+cats.size+tiers.size+brands.size+feats.size+lamps.size+(criMin?1:0)+(featAnim?1:0);

  return (
    <div style={{minHeight:"100vh",background:"#09090B",color:"#EDEDEF",fontFamily:"'Outfit',sans-serif"}}>
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500;600&display=swap');
        *{box-sizing:border-box;-webkit-tap-highlight-color:transparent;}
        ::-webkit-scrollbar{width:5px;height:5px;}
        ::-webkit-scrollbar-track{background:#111113;}
        ::-webkit-scrollbar-thumb{background:#222228;border-radius:3px;}
        input::placeholder{color:#3A3A42;}
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
      <div style={{background:"#09090B",borderBottom:"1px solid #18181C",position:"sticky",top:0,zIndex:50}}>
        <div style={{maxWidth:1180,margin:"0 auto",padding:isMobile?"12px 16px":"16px 28px",display:"flex",alignItems:"center",gap:14}}>
          <div style={{flex:1}}>
            <div style={{fontSize:isMobile?20:24,fontWeight:800,letterSpacing:"-.03em",lineHeight:1}}>Moving Light Database</div>
            <div style={{fontSize:11,color:"#505058",fontFamily:"'IBM Plex Mono',monospace",marginTop:2,letterSpacing:".04em"}}>
              {FIXTURES.length} FIXTURES · {allBrands.length} BRANDS
            </div>
          </div>
          {!isMobile&&compare.length>0&&(
            <button onClick={()=>setShowCompare(true)}
              style={{display:"flex",alignItems:"center",gap:8,padding:"10px 20px",background:"#E8B339",color:"#09090B",border:"none",borderRadius:9,fontSize:14,fontWeight:700,cursor:"pointer",fontFamily:"'Outfit',sans-serif"}}>
              <GitCompare size={15}/> Compare ({compare.length})
            </button>
          )}
        </div>
      </div>

      <div style={{maxWidth:1180,margin:"0 auto",padding:isMobile?"16px 16px 100px":"22px 28px 48px"}}>

        {/* ── SEARCH ── */}
        <div style={{position:"relative",marginBottom:22}}>
          <Search size={17} color="#3A3A42" style={{position:"absolute",left:14,top:"50%",transform:"translateY(-50%)"}}/>
          <input value={query} onChange={e=>setQuery(e.target.value)}
            placeholder="Search fixture, brand, or feature..."
            style={{width:"100%",padding:isMobile?"13px 40px":"14px 44px",background:"#0F0F12",border:"1px solid #222228",borderRadius:11,color:"#EDEDEF",fontSize:isMobile?16:15,outline:"none",fontFamily:"'Outfit',sans-serif",fontWeight:400}}/>
          {query&&<X size={16} onClick={()=>setQuery("")} style={{position:"absolute",right:13,top:"50%",transform:"translateY(-50%)",color:"#3A3A42",cursor:"pointer"}}/>}
        </div>

        {/* ── APPLICATION ── */}
        <Section label="Application" active={apps.size}>
          <div style={{display:"flex",gap:8,flexWrap:"wrap"}}>
            {APP_ORDER.map(a=>{
              const on=apps.has(a); const col=APP_COLORS[a];
              const n=FIXTURES.filter(f=>(f.applications||[]).includes(a)).length;
              return(
                <div key={a} className="chip" onClick={()=>toggle(apps,setApps,a)}
                  style={{display:"flex",alignItems:"center",gap:8,padding:isMobile?"9px 14px":"10px 18px",background:on?col+"1A":"#0F0F12",border:`1.5px solid ${on?col:"#222228"}`,borderRadius:10,fontSize:isMobile?14:15,fontWeight:600,color:on?col:"#808088"}}>
                  <span style={{width:8,height:8,borderRadius:"50%",background:col,flexShrink:0}}/>
                  {a}
                  <span style={{fontSize:10,fontFamily:"'IBM Plex Mono',monospace",color:on?col+"88":"#303038",fontWeight:500}}>{n}</span>
                  {on&&<Check size={13}/>}
                </div>
              );
            })}
          </div>
        </Section>

        {/* ── TYPE ── */}
        <Section label="Type" active={cats.size}>
          <div style={{display:"flex",gap:8,flexWrap:"wrap"}}>
            {allCats.map(c=>{
              const on=cats.has(c); const col=CAT_COLORS[c];
              const n=FIXTURES.filter(f=>f.category===c).length;
              return(
                <div key={c} className="chip" onClick={()=>toggle(cats,setCats,c)}
                  style={{display:"flex",alignItems:"center",gap:8,padding:isMobile?"9px 14px":"10px 18px",background:on?col+"1A":"#0F0F12",border:`1.5px solid ${on?col:"#222228"}`,borderRadius:10,fontSize:isMobile?14:15,fontWeight:600,color:on?col:"#808088"}}>
                  <span style={{width:8,height:8,borderRadius:"50%",background:col,flexShrink:0}}/>
                  {c}
                  <span style={{fontSize:10,fontFamily:"'IBM Plex Mono',monospace",color:on?col+"88":"#303038"}}>{n}</span>
                  {on&&<Check size={13}/>}
                </div>
              );
            })}
          </div>
        </Section>

        {/* ── OUTPUT TIER ── */}
        <Section label="Output Tier" active={tiers.size}>
          <div style={{display:"flex",gap:8,flexWrap:"wrap"}}>
            {allTiers.map(t=>{
              const on=tiers.has(t); const col=TIER_COLORS[t];
              const n=FIXTURES.filter(f=>f.tier===t).length;
              return(
                <div key={t} className="chip" onClick={()=>toggle(tiers,setTiers,t)}
                  style={{display:"flex",flexDirection:"column",alignItems:"flex-start",padding:isMobile?"9px 14px":"10px 18px",background:on?col+"1A":"#0F0F12",border:`1.5px solid ${on?col:"#222228"}`,borderRadius:10}}>
                  <div style={{display:"flex",alignItems:"center",gap:8,fontSize:isMobile?14:15,fontWeight:600,color:on?col:"#808088"}}>
                    <span style={{width:8,height:8,borderRadius:"50%",background:col,flexShrink:0}}/>
                    {t}
                    {on&&<Check size={13}/>}
                  </div>
                  <div style={{fontSize:10,fontFamily:"'IBM Plex Mono',monospace",color:on?col+"88":"#303038",marginTop:3,marginLeft:16}}>{TIER_DESC[t]} · {n}</div>
                </div>
              );
            })}
          </div>
        </Section>

        {/* ── FEATURES ── */}
        <Section label="Features" active={feats.size}>
          <div style={{display:"flex",gap:8,flexWrap:"wrap"}}>
            {FEAT_FILTERS.map(({key,label,icon,color,field})=>{
              const on=feats.has(key);
              const n=FIXTURES.filter(field).length;
              return(
                <div key={key} className="chip" onClick={()=>toggle(feats,setFeats,key)}
                  style={{display:"flex",alignItems:"center",gap:8,padding:isMobile?"9px 14px":"10px 18px",background:on?color+"1A":"#0F0F12",border:`1.5px solid ${on?color:"#222228"}`,borderRadius:10,fontSize:isMobile?14:15,fontWeight:600,color:on?color:"#808088"}}>
                  {icon}
                  {label}
                  <span style={{fontSize:10,fontFamily:"'IBM Plex Mono',monospace",color:on?color+"88":"#303038"}}>{n}</span>
                  {on&&<Check size={13}/>}
                </div>
              );
            })}
          </div>
        </Section>

        {/* ── BRAND ── */}
        <Section label="Brand" active={brands.size}>
          <div className="no-scrollbar" style={{display:"flex",gap:7,overflowX:"auto",paddingBottom:2}}>
            {allBrands.map(b=>{
              const on=brands.has(b);
              const n=FIXTURES.filter(f=>f.brand===b).length;
              return(
                <div key={b} className="brand-pill" onClick={()=>toggle(brands,setBrands,b)}
                  style={{display:"flex",alignItems:"center",gap:5,padding:"8px 13px",background:on?"#E8B3391A":"#0F0F12",border:`1.5px solid ${on?"#E8B339":"#222228"}`,borderRadius:8,fontSize:13,fontWeight:600,color:on?"#E8B339":"#808088",flexShrink:0}}>
                  {b}
                  <span style={{fontSize:9,fontFamily:"'IBM Plex Mono',monospace",color:on?"#E8B33966":"#2A2A32"}}>{n}</span>
                  {on&&<Check size={11}/>}
                </div>
              );
            })}
          </div>
        </Section>

        {/* ── MORE FILTERS ── */}
        <div style={{marginBottom:22}}>
          <div onClick={()=>setMoreOpen(o=>!o)}
            style={{display:"inline-flex",alignItems:"center",gap:7,cursor:"pointer",fontSize:13,color:moreOpen||moreCount>0?"#EDEDEF":"#505058",fontWeight:600,letterSpacing:".01em"}}>
            <SlidersHorizontal size={14}/>
            More filters
            {moreCount>0&&<span style={{background:"#E8B339",color:"#09090B",borderRadius:8,padding:"1px 7px",fontSize:10,fontWeight:700}}>{moreCount}</span>}
            {moreOpen?<ChevronUp size={13}/>:<ChevronDown size={13}/>}
          </div>
          {moreOpen&&(
            <div className="expand-in" style={{marginTop:12,padding:"16px 18px",background:"#0F0F12",border:"1px solid #1C1C22",borderRadius:12}}>
              <SubGroup label="CRI">
                <div style={{display:"flex",gap:7}}>
                  {[{l:"90+",m:90},{l:"80+",m:80},{l:"70+",m:70}].map(b=>(
                    <MiniPill key={b.l} active={criMin===b.m} onClick={()=>setCriMin(criMin===b.m?0:b.m)}>CRI {b.l}</MiniPill>
                  ))}
                </div>
              </SubGroup>
              <SubGroup label="Light Source">
                <div style={{display:"flex",gap:7,flexWrap:"wrap"}}>
                  {allLamps.map(l=>(
                    <MiniPill key={l} active={lamps.has(l)} onClick={()=>toggle(lamps,setLamps,l)} dot={LAMP_COLORS[l]}>{l}</MiniPill>
                  ))}
                </div>
              </SubGroup>
              <SubGroup label="Other">
                <MiniPill active={featAnim} onClick={()=>setFeatAnim(v=>!v)}>Animation wheel</MiniPill>
              </SubGroup>
            </div>
          )}
        </div>

        {/* ── RESULTS ── */}
        {!hasFilter ? <EmptyState/> : filtered.length===0 ? (
          <div style={{textAlign:"center",padding:"70px 20px",color:"#505058"}}>
            <div style={{fontSize:17,fontWeight:700,marginBottom:10}}>No fixtures match</div>
            <button onClick={clearAll} style={{padding:"9px 18px",background:"#0F0F12",border:"1px solid #222228",borderRadius:8,color:"#808088",fontSize:14,cursor:"pointer",fontFamily:"'Outfit',sans-serif",fontWeight:600}}>Clear filters</button>
          </div>
        ) : (
          <>
            <div style={{display:"flex",alignItems:"center",justifyContent:"space-between",marginBottom:12}}>
              <div style={{fontSize:14,color:"#505058"}}>
                <span style={{color:"#EDEDEF",fontWeight:700,fontSize:17}}>{filtered.length}</span> results
                {activeCount>0&&<span onClick={clearAll} style={{marginLeft:10,fontSize:12,color:"#404048",cursor:"pointer",fontFamily:"'IBM Plex Mono',monospace",letterSpacing:".02em"}}>CLEAR ALL</span>}
              </div>
              <select value={sortBy} onChange={e=>setSortBy(e.target.value)}
                style={{background:"#0F0F12",border:"1px solid #222228",borderRadius:8,color:"#808088",fontSize:12,padding:"8px 10px",outline:"none",fontFamily:"'IBM Plex Mono',monospace",cursor:"pointer"}}>
                <option value="output-desc">Output {"\u2193"}</option>
                <option value="output-asc">Output {"\u2191"}</option>
                <option value="cri-desc">CRI {"\u2193"}</option>
                <option value="watts-desc">Wattage {"\u2193"}</option>
                <option value="zoom-asc">Tightest zoom</option>
                <option value="model-asc">Model A{"\u2013"}Z</option>
              </select>
            </div>

            {!isMobile&&(
              <div style={{display:"grid",gridTemplateColumns:"44px 1fr 88px 88px 88px 88px 88px 28px",padding:"7px 16px",marginBottom:2}}>
                <span/><span style={{fontSize:12,fontWeight:700,color:"#6A6A78",letterSpacing:".06em",fontFamily:"'IBM Plex Mono',monospace"}}>FIXTURE</span>
                {["OUTPUT","FRAMING","ZOOM","CRI","WATTS"].map(h=>(
                  <span key={h} style={{fontSize:10,fontWeight:600,color:"#2A2A32",letterSpacing:".08em",fontFamily:"'IBM Plex Mono',monospace",textAlign:"right"}}>{h}</span>
                ))}
                <span/>
              </div>
            )}

            <div style={{border:"1px solid #18181C",borderRadius:13,overflow:"hidden",background:"#0C0C0E"}}>
              {filtered.map((f,i)=>(
                <ResultRow key={f.id} f={f} isMobile={isMobile} last={i===filtered.length-1}
                  expanded={expanded.has(f.id)} onToggle={()=>toggleExpand(f.id)}
                  inCompare={inCompare(f.id)} compareFull={compare.length>=4} onCompare={()=>toggleCompare(f)}/>
              ))}
            </div>
          </>
        )}
      </div>

      {isMobile&&compare.length>0&&(
        <div style={{position:"fixed",bottom:0,left:0,right:0,background:"#0F0F12",borderTop:"1px solid #1C1C22",padding:"12px 16px",zIndex:150,display:"flex",alignItems:"center",gap:10}}>
          <div style={{fontSize:13,color:"#808088",flex:1}}><span style={{color:"#E8B339",fontWeight:700}}>{compare.length}</span> to compare</div>
          <button onClick={()=>setCompare([])} style={{padding:"9px 14px",background:"#1A1A20",border:"none",borderRadius:8,color:"#808088",fontSize:13,fontWeight:700,fontFamily:"'Outfit',sans-serif"}}>Clear</button>
          <button onClick={()=>setShowCompare(true)} style={{padding:"9px 18px",background:"#E8B339",border:"none",borderRadius:8,color:"#09090B",fontSize:13,fontWeight:700,fontFamily:"'Outfit',sans-serif",display:"flex",alignItems:"center",gap:6}}>
            <GitCompare size={14}/> Compare
          </button>
        </div>
      )}

      {showCompare&&<CompareModal items={compare} isMobile={isMobile} onClose={()=>setShowCompare(false)} onRemove={id=>setCompare(c=>c.filter(x=>x.id!==id))}/>}
    </div>
  );
}

function Section({label,active,children}){
  return(
    <div style={{marginBottom:20}}>
      <div style={{display:"flex",alignItems:"center",gap:10,marginBottom:10}}>
        <span style={{fontSize:16,fontWeight:700,color:active>0?"#EDEDEF":"#505058",letterSpacing:"-.01em"}}>{label}</span>
        {active>0&&<span style={{fontSize:10,fontFamily:"'IBM Plex Mono',monospace",background:"#E8B3391A",color:"#E8B339",padding:"2px 8px",borderRadius:6,fontWeight:600,letterSpacing:".03em"}}>{active} active</span>}
      </div>
      {children}
    </div>
  );
}

function SubGroup({label,children}){
  return(
    <div style={{marginBottom:14}}>
      <div style={{fontSize:10,fontWeight:600,color:"#404048",letterSpacing:".1em",textTransform:"uppercase",fontFamily:"'IBM Plex Mono',monospace",marginBottom:8}}>{label}</div>
      {children}
    </div>
  );
}

function MiniPill({active,onClick,children,dot}){
  return(
    <div className="chip" onClick={onClick}
      style={{display:"inline-flex",alignItems:"center",gap:6,padding:"7px 12px",background:active?"#E8B3391A":"transparent",border:`1px solid ${active?"#E8B339":"#222228"}`,borderRadius:7,fontSize:13,color:active?"#E8B339":"#606068",fontWeight:600,cursor:"pointer"}}>
      {dot&&<span style={{width:7,height:7,borderRadius:"50%",background:dot}}/>}
      {children}
      {active&&<Check size={11}/>}
    </div>
  );
}

function EmptyState(){
  return(
    <div style={{textAlign:"center",padding:"80px 20px"}}>
      <div style={{fontSize:30,fontWeight:800,color:"#1C1C22",letterSpacing:"-.03em",marginBottom:10}}>Find a fixture</div>
      <div style={{fontSize:15,color:"#404048",lineHeight:1.7,maxWidth:400,margin:"0 auto",fontWeight:400}}>
        Pick an <span style={{color:APP_COLORS["Theater"],fontWeight:600}}>application</span>, <span style={{color:CAT_COLORS["Spot / Profile"],fontWeight:600}}>type</span>, or <span style={{color:TIER_COLORS["Large"],fontWeight:600}}>output tier</span> — or search by name.
      </div>
    </div>
  );
}

function ResultRow({f,expanded,onToggle,inCompare,compareFull,onCompare,last,isMobile}){
  const catCol=CAT_COLORS[f.category]||"#888";
  const hasImg=!!f.imageUrl;
  return(
    <div style={{borderBottom:last&&!expanded?"none":"1px solid #131316",background:expanded?"#0F0F12":"transparent"}}>
      <div className="fx-row" onClick={onToggle}
        style={{display:"grid",gridTemplateColumns:isMobile?"44px 1fr auto 24px":"44px 1fr 88px 88px 88px 88px 88px 28px",padding:isMobile?"11px 14px":"12px 16px",cursor:"pointer",alignItems:"center",gap:0}}>

        {/* Thumbnail */}
        <div style={{width:36,height:36,borderRadius:7,overflow:"hidden",background:"#131316",border:"1px solid #1C1C22",display:"flex",alignItems:"center",justifyContent:"center",flexShrink:0}}>
          {hasImg
            ?<img src={f.imageUrl} alt={f.model} style={{width:"100%",height:"100%",objectFit:"cover"}} onError={e=>e.target.style.display="none"}/>
            :<div style={{width:12,height:12,borderRadius:3,background:catCol,opacity:.35}}/>
          }
        </div>

        {/* Name */}
        <div style={{paddingLeft:12,minWidth:0}}>
          <div style={{display:"flex",alignItems:"center",gap:6}}>
            <span style={{fontSize:isMobile?16:17,fontWeight:700,letterSpacing:"-.02em",overflow:"hidden",textOverflow:"ellipsis",whiteSpace:"nowrap",color:"#EDEDEF"}}>{clean(f.model)}</span>
          </div>
          <div style={{display:"flex",alignItems:"center",gap:6,marginTop:2}}>
            <span style={{fontSize:13,fontWeight:600,color:"#9090A0",letterSpacing:".04em",textTransform:"uppercase",fontFamily:"'IBM Plex Mono',monospace"}}>{f.brand}</span>
            <span style={{fontSize:11,color:catCol,background:catCol+"22",padding:"2px 7px",borderRadius:4,fontWeight:700,textTransform:"uppercase",letterSpacing:".04em",fontFamily:"'IBM Plex Mono',monospace"}}>{f.category==="Spot / Profile"?"SPOT":f.category==="Bar / Batten"?"BAR":f.category.toUpperCase()}</span>
          </div>
        </div>

        {/* Desktop specs */}
        {!isMobile&&<>
          <div style={{textAlign:"right",paddingRight:8}}>
            <span style={{fontSize:13,fontWeight:500,fontFamily:"'IBM Plex Mono',monospace",color:"#BCBCC4"}}>{f.outputLumens?fmt(f.outputLumens):"\u2014"}</span>
          </div>
          <div style={{textAlign:"right",paddingRight:8}}>
            {f.framing
              ?<span style={{display:"inline-flex",alignItems:"center",gap:4,fontSize:12,fontWeight:700,color:"#6EE7A8"}}><Scissors size={11}/> Yes</span>
              :<span style={{fontSize:12,color:"#2A2A32"}}>{"\u2014"}</span>}
          </div>
          <div style={{textAlign:"right",paddingRight:8}}>
            <span style={{fontSize:12,fontFamily:"'IBM Plex Mono',monospace",color:"#BCBCC4"}}>{zoomStr(f)}</span>
          </div>
          <div style={{textAlign:"right",paddingRight:8}}>
            {f.cri!=null
              ?<span style={{fontSize:13,fontWeight:700,fontFamily:"'IBM Plex Mono',monospace",color:f.cri>=90?"#6EE7A8":f.cri>=80?"#E8B339":"#808088"}}>{f.cri}</span>
              :<span style={{fontSize:12,color:"#2A2A32"}}>{"\u2014"}</span>}
          </div>
          <div style={{textAlign:"right",paddingRight:8}}>
            <span style={{fontSize:13,fontWeight:500,fontFamily:"'IBM Plex Mono',monospace",color:"#BCBCC4"}}>{f.watts?f.watts+"W":"\u2014"}</span>
          </div>
        </>}

        {/* Mobile specs */}
        {isMobile&&(
          <div style={{textAlign:"right",paddingRight:6}}>
            <div style={{fontSize:12,fontFamily:"'IBM Plex Mono',monospace",color:"#808088"}}>{f.outputLumens?fmt(f.outputLumens)+" lm":"\u2014"}</div>
            <div style={{display:"flex",gap:5,justifyContent:"flex-end",marginTop:3}}>
              {f.framing&&<span style={{fontSize:10,color:"#6EE7A8",fontWeight:700,display:"flex",alignItems:"center",gap:2}}><Scissors size={9}/>Frm</span>}
              {f.cri!=null&&<span style={{fontSize:10,fontFamily:"'IBM Plex Mono',monospace",color:f.cri>=90?"#6EE7A8":"#505058",fontWeight:600}}>CRI {f.cri}</span>}
            </div>
          </div>
        )}

        <div style={{color:"#2A2A32",display:"flex",justifyContent:"center"}}>
          {expanded?<ChevronUp size={15}/>:<ChevronDown size={15}/>}
        </div>
      </div>

      {/* Expanded card */}
      {expanded&&(
        <div className="expand-in" style={{padding:isMobile?"0 14px 16px":"0 16px 18px"}}>
          <div style={{background:"#09090B",border:"1px solid #18181C",borderRadius:12,overflow:"hidden"}}>

            {/* Hero banner */}
            <div style={{position:"relative",height:hasImg?(isMobile?155:190):72,background:"#0F0F12",overflow:"hidden"}}>
              {hasImg&&<img src={f.imageUrl} alt={f.model} style={{width:"100%",height:"100%",objectFit:"cover",opacity:.55}} onError={e=>{e.target.parentNode.style.height="72px";e.target.style.display="none";}}/>}
              <div style={{position:"absolute",inset:0,background:"linear-gradient(to top,rgba(9,9,11,.98) 0%,rgba(9,9,11,.3) 70%,transparent 100%)"}}/>
              <div style={{position:"absolute",bottom:0,left:0,right:0,padding:isMobile?"14px 16px":"16px 20px"}}>
                <div style={{display:"flex",gap:5,flexWrap:"wrap",marginBottom:7}}>
                  {(f.applications||[]).map(a=>(
                    <span key={a} style={{fontSize:10,fontWeight:700,color:APP_COLORS[a],background:APP_COLORS[a]+"1A",padding:"2px 8px",borderRadius:4,textTransform:"uppercase",letterSpacing:".05em",fontFamily:"'IBM Plex Mono',monospace"}}>{a}</span>
                  ))}
                  {f.tier&&<span style={{fontSize:10,fontWeight:700,color:TIER_COLORS[f.tier],background:TIER_COLORS[f.tier]+"1A",padding:"2px 8px",borderRadius:4,textTransform:"uppercase",letterSpacing:".05em",fontFamily:"'IBM Plex Mono',monospace"}}>{f.tier}</span>}
                  {f.ipRated&&<span style={{fontSize:10,fontWeight:700,color:"#9D8DF1",background:"#9D8DF11A",padding:"2px 8px",borderRadius:4,textTransform:"uppercase",letterSpacing:".05em",fontFamily:"'IBM Plex Mono',monospace"}}>{f.ipRating||"IP Rated"}</span>}
                </div>
                <div style={{fontSize:isMobile?22:26,fontWeight:800,letterSpacing:"-.03em",lineHeight:1.1,color:"#EDEDEF"}}>{clean(f.model)}</div>
                <div style={{fontSize:11,fontWeight:600,color:"#505058",letterSpacing:".06em",textTransform:"uppercase",fontFamily:"'IBM Plex Mono',monospace",marginTop:4}}>{f.brand} · {f.category}</div>
              </div>
            </div>

            {/* Description */}
            {f.description&&(
              <div style={{padding:isMobile?"11px 16px 6px":"12px 20px 6px",fontSize:13.5,color:"#707078",lineHeight:1.6,fontStyle:"italic",borderBottom:"1px solid #131316"}}>
                {f.description}
              </div>
            )}

            {/* Spec grid */}
            <div style={{padding:isMobile?"12px 14px":"14px 20px"}}>
              <div style={{display:"grid",gridTemplateColumns:isMobile?"1fr 1fr":"1fr 1fr 1fr",gap:8,marginBottom:12}}>
                <SB label="Max Output" value={f.outputLumens?fmt(f.outputLumens)+" lm":"\u2014"}/>
                <SB label="Framing Shutters" value={f.framing?"Yes":"No"} hl={f.framing}/>
                <SB label="CRI" value={clean(f.criRaw)||(f.cri!=null?String(f.cri):"\u2014")}/>
                <SB label="Lamp" value={(f.watts?f.watts+"W ":"")+(f.lampType||"")||"\u2014"}/>
                <SB label="Color Temp" value={clean(f.cct)||clean(f.cctRange)||"\u2014"}/>
                <SB label="Zoom" value={f.zoomMin!=null?zoomStr(f)+(f.zoomRatio?" ("+f.zoomRatio+")":""):(clean(f.zoomRaw)||"\u2014")}/>
                <SB label="Color Mixing" value={clean(f.colorMixing)||"\u2014"}/>
                <SB label="Pan / Tilt" value={clean(f.panTilt)||"\u2014"}/>
                <SB label="Weight" value={f.weightKg?f.weightKg+" kg":"\u2014"}/>
                <SB label="IP Rating" value={clean(f.ipRating)||"\u2014"}/>
                <SB label="Power Draw" value={f.powerConsumption?f.powerConsumption+" W":"\u2014"}/>
                <SB label="DMX Channels" value={clean(f.dmxChannels)||"\u2014"}/>
                <SB label="Protocols" value={clean(f.protocols)||"\u2014"} wide/>
                <SB label="Effects" value={clean(f.effectsRaw)||"\u2014"} wide/>
                <SB label="Gobo" value={clean(f.gobo)||"\u2014"} wide/>
              </div>
              <div style={{display:"flex",gap:8,flexWrap:"wrap"}}>
                <button onClick={e=>{e.stopPropagation();onCompare();}} disabled={!inCompare&&compareFull}
                  style={{flex:"1 1 140px",padding:"11px",background:inCompare?"#E8B339":"#0F0F12",border:`1px solid ${inCompare?"#E8B339":"#222228"}`,borderRadius:9,color:inCompare?"#09090B":(compareFull?"#2A2A32":"#EDEDEF"),fontSize:13.5,fontWeight:700,cursor:(!inCompare&&compareFull)?"default":"pointer",fontFamily:"'Outfit',sans-serif",display:"flex",alignItems:"center",justifyContent:"center",gap:6}}>
                  {inCompare?<><Minus size={13}/> Remove</>:<><Plus size={13}/> Compare</>}
                </button>
                {f.link
                  ?<a href={f.link} target="_blank" rel="noopener noreferrer" onClick={e=>e.stopPropagation()}
                      style={{flex:"1 1 140px",padding:"11px",background:"#0F0F12",border:"1px solid #222228",borderRadius:9,color:"#EDEDEF",fontSize:13.5,fontWeight:700,display:"flex",alignItems:"center",justifyContent:"center",gap:6}}>
                      <ExternalLink size={13}/> Product page
                    </a>
                  :<div style={{flex:"1 1 140px",padding:"11px",background:"#09090B",borderRadius:9,color:"#2A2A32",fontSize:12,fontWeight:600,display:"flex",alignItems:"center",justifyContent:"center",gap:6}}>
                      <ExternalLink size={12}/> No link yet
                    </div>
                }
              </div>
              {f.lastVerified&&<div style={{fontSize:10,color:"#2A2A32",marginTop:10,fontFamily:"'IBM Plex Mono',monospace",letterSpacing:".04em"}}>VERIFIED {f.lastVerified}</div>}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

function SB({label,value,wide,hl}){
  return(
    <div style={{background:hl?"#6EE7A80A":"#0F0F12",border:`1px solid ${hl?"#6EE7A820":"#18181C"}`,borderRadius:8,padding:"9px 11px",gridColumn:wide?"1 / -1":"auto"}}>
      <div style={{fontSize:9,fontWeight:600,color:"#404048",textTransform:"uppercase",letterSpacing:".1em",fontFamily:"'IBM Plex Mono',monospace",marginBottom:4}}>{label}</div>
      <div style={{fontSize:13,color:hl?"#6EE7A8":"#C0C0C8",whiteSpace:"pre-line",lineHeight:1.45,fontWeight:hl?600:400}}>{value}</div>
    </div>
  );
}

function CompareModal({items,onClose,onRemove,isMobile}){
  if(!items.length) return null;
  const fields=[
    ["type","Type",f=>f.category],
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
          <div style={{fontSize:isMobile?16:19,fontWeight:800,display:"flex",alignItems:"center",gap:10,letterSpacing:"-.02em"}}>
            <GitCompare size={isMobile?17:20} color="#E8B339"/> Compare
            <span style={{fontSize:11,color:"#404048",fontFamily:"'IBM Plex Mono',monospace"}}>{items.length}/4</span>
          </div>
          <X size={22} onClick={onClose} style={{cursor:"pointer",color:"#404048"}}/>
        </div>
        <div style={{overflow:"auto"}}>
          <table style={{width:"100%",borderCollapse:"collapse",minWidth:(isMobile?120:160)+items.length*(isMobile?145:200)}}>
            <thead>
              <tr style={{background:"#0C0C0E"}}>
                <th style={{position:"sticky",left:0,background:"#0C0C0E",textAlign:"left",padding:isMobile?"12px":"14px 18px",fontSize:10,color:"#404048",fontWeight:600,textTransform:"uppercase",letterSpacing:".08em",fontFamily:"'IBM Plex Mono',monospace",width:isMobile?120:160,zIndex:2}}>Spec</th>
                {items.map(f=>(
                  <th key={f.id} style={{padding:isMobile?"12px":"14px 18px",textAlign:"left",borderLeft:"1px solid #18181C",minWidth:isMobile?145:195}}>
                    <div style={{display:"flex",justifyContent:"space-between",alignItems:"flex-start",gap:8}}>
                      <div>
                        <div style={{fontSize:10,fontWeight:700,color:CAT_COLORS[f.category],textTransform:"uppercase",letterSpacing:".06em",fontFamily:"'IBM Plex Mono',monospace"}}>{f.brand}</div>
                        <div style={{fontSize:isMobile?13:15,fontWeight:800,marginTop:3,lineHeight:1.2,letterSpacing:"-.01em"}}>{clean(f.model)}</div>
                      </div>
                      <X size={15} onClick={()=>onRemove(f.id)} style={{cursor:"pointer",color:"#404048",flexShrink:0}}/>
                    </div>
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {fields.map(([key,label,render,scoreFn],ri)=>{
                let bestId=null;
                if(scoreFn&&items.length>1){
                  let bv=-Infinity;
                  items.forEach(f=>{const s=scoreFn(f);if(s>bv){bv=s;bestId=f.id;}});
                  if(bv<=0&&key!=="zoomMin"&&key!=="weight") bestId=null;
                }
                return(
                  <tr key={key} style={{background:ri%2?"#0F0F12":"transparent"}}>
                    <td style={{position:"sticky",left:0,background:ri%2?"#0F0F12":"#0C0C0E",padding:isMobile?"10px 12px":"11px 18px",fontSize:10,color:"#404048",fontWeight:600,textTransform:"uppercase",letterSpacing:".06em",fontFamily:"'IBM Plex Mono',monospace",zIndex:1}}>{label}</td>
                    {items.map(f=>(
                      <td key={f.id} style={{padding:isMobile?"10px 12px":"11px 18px",fontSize:isMobile?12:13.5,borderLeft:"1px solid #18181C",color:bestId===f.id?"#6EE7A8":"#C0C0C8",fontWeight:bestId===f.id?700:400,whiteSpace:"pre-line",lineHeight:1.45,verticalAlign:"top"}}>
                        {render(f)}
                        {bestId===f.id&&<span style={{marginLeft:6,fontSize:9,background:"#6EE7A812",color:"#6EE7A8",padding:"1px 5px",borderRadius:4,fontWeight:700,whiteSpace:"nowrap"}}>BEST</span>}
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
