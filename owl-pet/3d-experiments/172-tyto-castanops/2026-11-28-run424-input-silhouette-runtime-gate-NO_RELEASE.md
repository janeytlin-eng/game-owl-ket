# Run424 — input silhouette and runtime gate — ART_REJECTED / NO_RELEASE

2026-11-28 Asia/Shanghai. Read main AGENTS, README, STATUS (207/251) and Run423. Viewed original concept blob 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b and three historical actual input PNGs. Cream down, compact rounded body, heart disc, dark eyes, feathered feet remain required. No independent side/back reference.

Executed a PNG DEFLATE/scanline decoder on three archived preprocessed inputs, checked inflated raster lengths, measured foreground area/bounds and width profile at four thresholds. These are input-image metrics, not model quality or new geometry. Alpha threshold differences characterize the input down silhouette; if a file lacks alpha the nonblack proxy is explicitly distinguished. Visual review: all three retain the bird and heart disc, InstantMesh input appears to have a coarser edge halo, TRELLIS input slightly smoother edge. Rejected reconstruction cannot simply be attributed to a missing face or gross cropping.

Attempted alternate archive retrieval by GitHub blob SHA for Run116C (1609676 bytes, 477a4ac4437293d44f9a328a9036d23e27894220) and Run117 (2660676 bytes, d5a269dd87feb381c58b54160ead015de306f27e). Both fetch_blob calls returned UnicodeDecodeError, generic Git blob fetch rejected non-UTF-8, base64 fetch_file returned empty contents. No recovered complete model. New free browser route https://github.com/lyonsno/sf3d-webgpu is actual SF3D GLB generation, but needs ~2.1 GB weights and working WebGPU. Tested Chromium with unsafe WebGPU plus SwiftShader and Vulkan flags; GPU process failed ANGLE/EGL initialization in both configurations and command timed out, no adapter success demonstrated. https://three.ws/forge-desktop needs local GPU or hosted cloud; free local app does not establish free hosted inference. No paid endpoint invoked. No new model or mobile QA pass.

## Executed metrics

```json
[
  {
    "path": "research-evidence-run140-PBR-LOD-SIMULATED-MOBILE-NO_RELEASE/run139_pinned_rightmost_juvenile_RGBA.png",
    "sha": "d8a969a3fe0d9a7955196e4cd8f4327cd20f8534",
    "w": 512,
    "h": 512,
    "type": 6,
    "depth": 8,
    "method": "alpha",
    "stats": [
      {
        "threshold": 8,
        "count": 147574,
        "bbox": [
          62,
          38,
          449,
          472
        ],
        "bboxAspect": 0.8919540229885058,
        "widthAtHeightFractions": [
          282,
          322,
          375,
          376,
          349
        ]
      },
      {
        "threshold": 32,
        "count": 147252,
        "bbox": [
          62,
          38,
          449,
          472
        ],
        "bboxAspect": 0.8919540229885058,
        "widthAtHeightFractions": [
          281,
          321,
          375,
          376,
          349
        ]
      },
      {
        "threshold": 128,
        "count": 146250,
        "bbox": [
          63,
          38,
          448,
          472
        ],
        "bboxAspect": 0.8873563218390804,
        "widthAtHeightFractions": [
          280,
          320,
          373,
          374,
          345
        ]
      },
      {
        "threshold": 224,
        "count": 145702,
        "bbox": [
          63,
          38,
          448,
          472
        ],
        "bboxAspect": 0.8873563218390804,
        "widthAtHeightFractions": [
          279,
          316,
          372,
          374,
          344
        ]
      }
    ]
  },
  {
    "path": "research-evidence-run116C-OFFICIAL-INSTANTMESH-STATEFUL-ART_REJECTED/run116c_preprocessed_actual.png",
    "sha": "854aa633637c690fac2b7ccbed186bc070eb576f",
    "w": 523,
    "h": 523,
    "type": 6,
    "depth": 8,
    "method": "alpha",
    "stats": [
      {
        "threshold": 8,
        "count": 110050,
        "bbox": [
          90,
          42,
          434,
          481
        ],
        "bboxAspect": 0.7840909090909091,
        "widthAtHeightFractions": [
          184,
          235,
          328,
          303,
          250
        ]
      },
      {
        "threshold": 32,
        "count": 108609,
        "bbox": [
          91,
          42,
          433,
          480
        ],
        "bboxAspect": 0.7813211845102506,
        "widthAtHeightFractions": [
          181,
          232,
          325,
          301,
          249
        ]
      },
      {
        "threshold": 128,
        "count": 106292,
        "bbox": [
          92,
          44,
          431,
          479
        ],
        "bboxAspect": 0.7798165137614679,
        "widthAtHeightFractions": [
          176,
          229,
          323,
          299,
          237
        ]
      },
      {
        "threshold": 224,
        "count": 103846,
        "bbox": [
          93,
          45,
          428,
          477
        ],
        "bboxAspect": 0.7759815242494227,
        "widthAtHeightFractions": [
          170,
          226,
          320,
          297,
          231
        ]
      }
    ]
  },
  {
    "path": "research-evidence-run117-FREE-TRELLIS-QUOTA-RECHECK-ART_REJECTED/run117_remote_preprocessed_input.png",
    "sha": "4981c73eb2aed6a62abd41b3381162a999526691",
    "w": 518,
    "h": 518,
    "type": 2,
    "depth": 8,
    "method": "nonblack proxy",
    "stats": [
      {
        "threshold": 8,
        "count": 105638,
        "bbox": [
          66,
          42,
          403,
          476
        ],
        "bboxAspect": 0.7770114942528735,
        "widthAtHeightFractions": [
          178,
          240,
          320,
          295,
          233
        ]
      },
      {
        "threshold": 32,
        "count": 103318,
        "bbox": [
          67,
          43,
          402,
          475
        ],
        "bboxAspect": 0.7759815242494227,
        "widthAtHeightFractions": [
          176,
          220,
          316,
          292,
          228
        ]
      },
      {
        "threshold": 128,
        "count": 85626,
        "bbox": [
          76,
          45,
          393,
          460
        ],
        "bboxAspect": 0.7644230769230769,
        "widthAtHeightFractions": [
          170,
          154,
          302,
          257,
          156
        ]
      },
      {
        "threshold": 224,
        "count": 295,
        "bbox": [
          156,
          64,
          345,
          432
        ],
        "bboxAspect": 0.5149051490514905,
        "widthAtHeightFractions": [
          2,
          0,
          0,
          0,
          0
        ]
      }
    ]
  }
]
```

## Reproducible decoder (pass base64 PNG)

```js
function pngAudit(s){
 const chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/", clean=s.replace(/\s|=/g,""); let b=new Uint8Array(Math.floor(clean.length*6/8)),v=0,n=0,o=0;for(const c of clean){v=(v<<6)|chars.indexOf(c);n+=6;if(n>=8){n-=8;b[o++]=(v>>n)&255}}
 const u32=(a,p)=>((a[p]<<24|a[p+1]<<16|a[p+2]<<8|a[p+3])>>>0), w=u32(b,16),h=u32(b,20),depth=b[24],type=b[25];if(depth!==8||b[28])throw Error("unsupported bit depth/interlace");
 let data=[],pal=[],tr=[];for(let p=8;p+12<=b.length;){let len=u32(b,p),t=String.fromCharCode(...b.slice(p+4,p+8));if(p+12+len>b.length)throw Error("truncated PNG");let d=b.slice(p+8,p+8+len);if(t==="IDAT")for(let x of d)data.push(x);if(t==="PLTE")pal=d;if(t==="tRNS")tr=d;p+=len+12;if(t==="IEND")break}
 let bit=16;const read=k=>{let r=0;for(let i=0;i<k;i++,bit++)r|=((data[bit>>3]>>(bit&7))&1)<<i;return r};
 const tree=lens=>{let count=Array(16).fill(0),next=Array(16).fill(0),map={};for(let l of lens)if(l)count[l]++;for(let i=1;i<16;i++)next[i]=(next[i-1]+count[i-1])<<1;for(let i=0;i<lens.length;i++){let l=lens[i];if(!l)continue;let k=next[l]++,r=0;for(let j=0;j<l;j++)r=(r<<1)|((k>>j)&1);map[l+":"+r]=i}return map};
 const sym=t=>{let x=0;for(let l=1;l<=15;l++){x|=read(1)<<(l-1);let q=t[l+":"+x];if(q!==undefined)return q}throw Error("invalid huffman")};
 const lb=[3,4,5,6,7,8,9,10,11,13,15,17,19,23,27,31,35,43,51,59,67,83,99,115,131,163,195,227,258],le=[0,0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,0],db=[1,2,3,4,5,7,9,13,17,25,33,49,65,97,129,193,257,385,513,769,1025,1537,2049,3073,4097,6145,8193,12289,16385,24577],de=[0,0,0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13];
 let raw=[],final=0;while(!final){final=read(1);let t=read(2);if(t===0){bit=(bit+7)&~7;let k=read(16);read(16);while(k--)raw.push(read(8));continue}let lt,dt;if(t===1){lt=tree(Array.from({length:288},(_,i)=>i<144?8:i<256?9:i<280?7:8));dt=tree(Array(32).fill(5))}else if(t===2){let nl=read(5)+257,nd=read(5)+1,nc=read(4)+4,order=[16,17,18,0,8,7,9,6,10,5,11,4,12,3,13,2,14,1,15],cl=Array(19).fill(0);for(let i=0;i<nc;i++)cl[order[i]]=read(3);let ct=tree(cl),ls=[];while(ls.length<nl+nd){let a=sym(ct);if(a<16)ls.push(a);else{let k=a===16?read(2)+3:a===17?read(3)+3:read(7)+11;let x=a===16?ls[ls.length-1]:0;while(k--)ls.push(x)}}lt=tree(ls.slice(0,nl));dt=tree(ls.slice(nl))}else throw Error("bad deflate block");
 while(true){let a=sym(lt);if(a<256)raw.push(a);else if(a===256)break;else{let i=a-257,k=lb[i]+read(le[i]),d=sym(dt),off=db[d]+read(de[d]);if(off>raw.length)throw Error("bad distance");while(k--)raw.push(raw[raw.length-off])}if(raw.length>10000000)throw Error("inflate cap")}}
 let channels=({0:1,2:3,3:1,4:2,6:4})[type],stride=w*channels;if(raw.length!==(stride+1)*h)throw Error("wrong inflated size");let pixels=new Uint8Array(stride*h);const paeth=(a,b,c)=>{let p=a+b-c,pa=Math.abs(p-a),pb=Math.abs(p-b),pc=Math.abs(p-c);return pa<=pb&&pa<=pc?a:pb<=pc?b:c};
 for(let y=0;y<h;y++){let f=raw[y*(stride+1)];for(let x=0;x<stride;x++){let i=y*stride+x,a=x>=channels?pixels[i-channels]:0,b=y?pixels[i-stride]:0,c=y&&x>=channels?pixels[i-stride-channels]:0;pixels[i]=(raw[y*(stride+1)+x+1]+(f===1?a:f===2?b:f===3?((a+b)>>1):f===4?paeth(a,b,c):0))&255}}
 const alpha=new Uint8Array(w*h);let method=type===6||type===4||type===3&&tr.length?"alpha":"nonblack proxy";for(let i=0;i<w*h;i++){let p=i*channels;alpha[i]=type===6?pixels[p+3]:type===4?pixels[p+1]:type===3&&tr.length?(tr[pixels[p]]??255):type===3?Math.max(...pal.slice(pixels[p]*3,pixels[p]*3+3)):Math.max(...pixels.slice(p,p+channels))}
 const stats=[];for(let threshold of [8,32,128,224]){let minx=w,miny=h,maxx=-1,maxy=-1,count=0,rows=Array(h).fill(0);for(let y=0;y<h;y++)for(let x=0;x<w;x++)if(alpha[y*w+x]>=threshold){count++;rows[y]++;minx=Math.min(minx,x);maxx=Math.max(maxx,x);miny=Math.min(miny,y);maxy=Math.max(maxy,y)}stats.push({threshold,count,bbox:[minx,miny,maxx,maxy],bboxAspect:(maxx-minx+1)/(maxy-miny+1),widthAtHeightFractions:[.1,.25,.5,.75,.9].map(f=>rows[Math.round(miny+f*(maxy-miny))])})}
 return {w,h,type,depth,method,stats,alpha};
}
```

Decision: ART_REJECTED / NO_RELEASE. Preserve this isolated evidence; focus on access to an actual new base reconstruction, not further tuning already rejected geometry. No modification to main, original concept, 251 species workflow or deployment.
