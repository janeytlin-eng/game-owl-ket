function render(s){
 const abc="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",b=new Uint8Array(Math.floor(s.length*3/4)-(s.endsWith("==")?2:s.endsWith("=")?1:0));for(let i=0,k=0;i<s.length;i+=4){const v=(abc.indexOf(s[i])<<18)|(abc.indexOf(s[i+1])<<12)|((abc.indexOf(s[i+2])&63)<<6)|(abc.indexOf(s[i+3])&63);b[k++]=v>>16;b[k++]=v>>8;b[k++]=v}
 const d=new DataView(b.buffer),n=d.getUint32(12,true),j=JSON.parse(String.fromCharCode(...b.slice(20,20+n))),bin=28+n;if(d.getUint32(8,true)!==b.length)throw Error("incomplete");
 const p=new Float32Array(b.buffer,bin+j.bufferViews[1].byteOffset,j.accessors[1].count*3),idx=new Uint32Array(b.buffer,bin+j.bufferViews[0].byteOffset,j.accessors[0].count),c=new Uint8Array(b.buffer,bin+j.bufferViews[2].byteOffset,j.accessors[2].count*4);
 const S=180,W=540,H=360,pix=new Uint8Array(W*H*3);pix.fill(177);
 const views=[[2,0,1,1],[2,0,1,-1],[0,2,1,1],[0,2,1,-1],[1,0,2,1],[1,0,2,-1]];
 const result=[];
 for(let v=0;v<6;v++){const [a,u,t,sign]=views[v],offx=v%3*S,offy=Math.floor(v/3)*S,depth=new Float32Array(S*S);depth.fill(-Infinity);
 function coord(i){return [S/2+p[3*i+u]*160*(sign===-1?-1:1),S/2-p[3*i+t]*160,p[3*i+a]*sign]}
 for(let f=0;f<idx.length;f+=3){const ids=[idx[f],idx[f+1],idx[f+2]],q=ids.map(coord),[A,B,C]=q,den=(B[1]-C[1])*(A[0]-C[0])+(C[0]-B[0])*(A[1]-C[1]);if(Math.abs(den)<1e-9)continue;
 const ab=[p[3*ids[1]]-p[3*ids[0]],p[3*ids[1]+1]-p[3*ids[0]+1],p[3*ids[1]+2]-p[3*ids[0]+2]],ac=[p[3*ids[2]]-p[3*ids[0]],p[3*ids[2]+1]-p[3*ids[0]+1],p[3*ids[2]+2]-p[3*ids[0]+2]],N=[ab[1]*ac[2]-ab[2]*ac[1],ab[2]*ac[0]-ab[0]*ac[2],ab[0]*ac[1]-ab[1]*ac[0]],L=Math.hypot(...N)||1,shade=.68+.32*Math.abs((N[a]*sign+.32*N[t]-.15*N[u])/L)/1.07;
 for(let y=Math.max(0,Math.floor(Math.min(A[1],B[1],C[1])));y<=Math.min(S-1,Math.ceil(Math.max(A[1],B[1],C[1])));y++)for(let x=Math.max(0,Math.floor(Math.min(A[0],B[0],C[0])));x<=Math.min(S-1,Math.ceil(Math.max(A[0],B[0],C[0])));x++){const l=((B[1]-C[1])*(x+.5-C[0])+(C[0]-B[0])*(y+.5-C[1]))/den,m=((C[1]-A[1])*(x+.5-C[0])+(A[0]-C[0])*(y+.5-C[1]))/den,k=1-l-m;if(Math.min(l,m,k)<-1e-6)continue;const z=l*A[2]+m*B[2]+k*C[2],di=y*S+x;if(z<=depth[di])continue;depth[di]=z;const o=((y+offy)*W+x+offx)*3;for(let ch=0;ch<3;ch++)pix[o+ch]=Math.min(255,Math.round(shade*(l*c[4*ids[0]+ch]+m*c[4*ids[1]+ch]+k*c[4*ids[2]+ch])))}
 }
 result.push({view:["Z+","Z-","X+","X-","Y+","Y-"][v],covered_pixels:depth.reduce((a,z)=>a+(Number.isFinite(z)?1:0),0)});
 }
 function u32(x){return [(x>>>24)&255,(x>>>16)&255,(x>>>8)&255,x&255]}
 function chunk(name,data){let a=[...name].map(x=>x.charCodeAt(0)),crc=0xffffffff;for(const x of a.concat(Array.from(data))){crc^=x;for(let i=0;i<8;i++)crc=(crc>>>1)^((crc&1)?0xedb88320:0)}return u32(data.length).concat(a,Array.from(data),u32((crc^0xffffffff)>>>0))}
 const raw=new Uint8Array(H*(W*3+1));for(let y=0;y<H;y++)raw.set(pix.slice(y*W*3,(y+1)*W*3),y*(W*3+1)+1);
 let z=[120,1],a=1,e=0;for(const x of raw){a=(a+x)%65521;e=(e+a)%65521}for(let i=0;i<raw.length;i+=65535){let len=Math.min(65535,raw.length-i);z.push(i+len===raw.length?1:0,len&255,len>>8,(~len)&255,((~len)>>8)&255);z=z.concat(Array.from(raw.slice(i,i+len)))}z=z.concat(u32((e<<16)|a));const png=[137,80,78,71,13,10,26,10].concat(chunk("IHDR",u32(W).concat(u32(H),[8,2,0,0,0])),chunk("IDAT",z),chunk("IEND",[]));
 let enc="";for(let i=0;i<png.length;i+=3){const n=(png[i]<<16)|((png[i+1]||0)<<8)|(png[i+2]||0);enc+=abc[(n>>18)&63]+abc[(n>>12)&63]+(i+1<png.length?abc[(n>>6)&63]:"=")+(i+2<png.length?abc[n&63]:"=")}
 return {enc,result,bytes:b.length,vertices:p.length/3,triangles:idx.length/3};
}
// Pass complete Run104 GLB base64 to render(s); result.enc is PNG base64.
