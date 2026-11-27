# Run422 — avian reconstruction prior and native topology audit — ART_REJECTED / NO_RELEASE

2026-11-28 Asia/Shanghai. Read current main owl-pet AGENTS, README, STATUS (207/251), Run421 and Run415; visually inspected actual original #172 v3 PNG (blob 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b). Compact cream down, narrow warm heart-disc rim, dark eyes, pale bill, feathered feet. Concept only, no observed side/back. Recovered entire Run421 native diagnostic GLB (blob 9563fd05ad2f42cc2fa9274e4489e5a45a035b4a, header length checked). No new geometry claimed.

## Executed avian-specific route

Read original DOVE repository https://github.com/elliottwu/DOVE and actual bird pretrained download script https://github.com/elliottwu/DOVE/blob/main/results/bird/download_pretrained_bird.sh (blob 1a070f8fd6fe8083dc86494cd22ca9a5b4f774f6). Unlike generic image-to-3D, this is a bird-category articulated mesh reconstruction approach with published pretrained bird checkpoint. Actual HEAD request to https://download.cs.stanford.edu/viscam/AnimalKingdom/dove/models/pretrained_bird.zip failed DNS errno -3; local torch.cuda.is_available() false and pytorch3d absent. No weights acquired or inference performed. MagicPony unified codebase https://github.com/3DAnimals/3DAnimals documents bird training, but attempted bird pretrained script/config returned 404; INSTALL requires CUDA dependencies. AVES https://github.com/yufu-wang/aves README describes 17 average species meshes; no verified owl juvenile mesh obtained; directory web fetch failed and GitHub code search yielded README only. No fee incurred. Generic public assets screened: Grab3D great horned owl (wrong species, adult, 400k–800k triangles), Embossify simple math owl (wrong anatomy), Mint adult barn owl (already explored); none promoted.

## Actual native mesh audit

Parsed binary glTF indexed triangles and built edge incidence/union-find; measured reflection nearest-vertex distances for every seventh vertex using x plane at bounding-box midpoint (not a fitted anatomical midline). Native units, vertex-distance proxy not exact point-to-triangle distance. Intended to establish topology fitness and asymmetric regions before any rigging, not validate art.

```json
{
  "bytes": 606860,
  "vertices": 21622,
  "triangles": 43240,
  "edges": 64860,
  "boundary_edges": 0,
  "nonmanifold_edges": 0,
  "degenerate_index_triangles": 0,
  "connected_components": [
    21622
  ],
  "euler": 2,
  "reflection_plane_x": -0.017142325,
  "reflection_nearest_vertex_distance": [
    {
      "name": "head_front",
      "samples": 444,
      "mean": 0.033670992106298925,
      "p95": 0.06696600998245936,
      "max": 0.08585944187806849
    },
    {
      "name": "head_rear",
      "samples": 398,
      "mean": 0.022135052324746496,
      "p95": 0.06853694987231448,
      "max": 0.08429956801177335
    },
    {
      "name": "body",
      "samples": 1128,
      "mean": 0.020512254819315418,
      "p95": 0.04764714073168682,
      "max": 0.09586856842525296
    },
    {
      "name": "feet",
      "samples": 970,
      "mean": 0.02373949666491641,
      "p95": 0.07189193087157186,
      "max": 0.12634519906249322
    }
  ]
}
```

Reproduction (JavaScript audit, input complete GLB base64):
```js
function audit(s){
 const abc="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/", b=new Uint8Array(Math.floor(s.length*3/4)-(s.endsWith("==")?2:s.endsWith("=")?1:0));for(let i=0,k=0;i<s.length;i+=4){const v=(abc.indexOf(s[i])<<18)|(abc.indexOf(s[i+1])<<12)|((abc.indexOf(s[i+2])&63)<<6)|(abc.indexOf(s[i+3])&63);b[k++]=v>>16;b[k++]=v>>8;b[k++]=v}
 const d=new DataView(b.buffer), n=d.getUint32(12,true), j=JSON.parse(String.fromCharCode(...b.slice(20,20+n))), bin=28+n;
 if(d.getUint32(8,true)!==b.length)throw Error("incomplete");
 const p=new Float32Array(b.buffer,bin+j.bufferViews[0].byteOffset,j.accessors[0].count*3), ind=new Uint16Array(b.buffer,bin+j.bufferViews[2].byteOffset,j.accessors[2].count);
 const N=p.length/3, E=new Map(), parent=Array.from({length:N},(_,i)=>i);
 function root(i){while(parent[i]!==i){parent[i]=parent[parent[i]];i=parent[i]}return i}
 let deg=0;for(let i=0;i<ind.length;i+=3){const a=ind[i], c=ind[i+1], f=ind[i+2];if(a===c||c===f||a===f)deg++;for(const [u,v] of [[a,c],[c,f],[f,a]]){const key=Math.min(u,v)*N+Math.max(u,v);E.set(key,(E.get(key)||0)+1);parent[root(u)]=root(v)}}
 const components={};for(let i=0;i<N;i++){const k=root(i);components[k]=(components[k]||0)+1}
 const sections=[{name:"head_front",f:(y,z)=>y>.12&&z>.12},{name:"head_rear",f:(y,z)=>y>.12&&z<-.05},{name:"body",f:(y,z)=>y<.12&&y>-.59},{name:"feet",f:(y,z)=>y<-.59}];
 const metric=sections.map(({name,f})=>{const v=[];for(let i=0;i<N;i+=7){let x=p[3*i], y=p[3*i+1],z=p[3*i+2];if(!f(y,z))continue;let best=Infinity;for(let k=0;k<N;k++){const a=p[3*k]+x+.03428465,c=p[3*k+1]-y,e=p[3*k+2]-z;const t=a*a+c*c+e*e;if(t<best)best=t}v.push(Math.sqrt(best))}v.sort((a,b)=>a-b);return {name,samples:v.length,mean:v.reduce((a,b)=>a+b,0)/v.length,p95:v[Math.floor(v.length*.95)],max:v[v.length-1]}});
 return {bytes:b.length,vertices:N,triangles:ind.length/3,edges:E.size,boundary_edges:[...E.values()].filter(v=>v===1).length,nonmanifold_edges:[...E.values()].filter(v=>v>2).length,degenerate_index_triangles:deg,connected_components:Object.values(components).sort((a,b)=>b-a),euler:N-E.size+ind.length/3,reflection_plane_x:-.017142325,reflection_nearest_vertex_distance:metric};
}
```

Decision: no new juvenile sculpture, no down/face visual acceptance, no phone WebGL acceptance. Historical rejected mesh remains diagnostic only; avoid escalating micro-optimizations as character progress. No external paid calls, no main, v3, species production or deployment changes. DOVE checkpoint access remains a concrete potential alternative when download and runtime constraints change.
