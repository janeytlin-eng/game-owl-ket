function experiment(){
 const N=120,R=48,V=[],C=[],F=[],tau=2*Math.PI;
 const knots=[[0,.66],[.35,.78],[.7,.67],[.94,.34],[1,-.02],[.85,-.35],[.53,-.65],[.19,-.88],[0,-.96],[-.19,-.88],[-.53,-.65],[-.85,-.35],[-1,-.02],[-.94,.34],[-.7,.67],[-.35,.78]];
 const clamp=(x,a=0,b=1)=>Math.max(a,Math.min(b,x));
 function boundary(t){let j=Math.floor(t),u=t-j,n=knots.length,p=[-1,0,1,2].map(d=>knots[(j+d+n)%n]);return [0,1].map(k=>.5*(2*p[1][k]+(-p[0][k]+p[2][k])*u+(2*p[0][k]-5*p[1][k]+4*p[2][k]-p[3][k])*u*u+(-p[0][k]+3*p[1][k]-3*p[2][k]+p[3][k])*u*u*u))}
 function sample(r,a){let [bx,by]=boundary(a/tau*knots.length),x=r*bx,y=r*by,d1=((x-.43)/.24)**2+((y-.12)/.24)**2,d2=((x+.43)/.24)**2+((y-.12)/.24)**2;
 let eye=Math.exp(-Math.min(d1,d2)*1.4),bridge=Math.exp(-((x/.15)**2+((y+.22)/.49)**2)),rim=Math.exp(-(((r-.93)/.055)**2));
 let grain=.5*Math.sin(46*a+5*r)+.27*Math.sin(73*a-12*r)+.12*Math.sin(97*a+21*r),z=.24*(1-r*r)+.075*rim-.12*eye+.085*bridge+grain*Math.sin(Math.PI*r)*.012,t=clamp(.78*rim+.37*eye+.05*grain);
 return [[x,y,z],[236-92*t,215-97*t,186-94*t].map(Math.round)]}
 let a=sample(0,0);V.push(a[0]);C.push(a[1]);for(let i=1;i<=R;i++)for(let j=0;j<N;j++){let a=sample(i/R,j*tau/N);V.push(a[0]);C.push(a[1])}
 const idx=(i,j)=>1+(i-1)*N+(j+N)%N;
 for(let j=0;j<N;j++)F.push([0,idx(1,j+1),idx(1,j)]);
 for(let i=1;i<R;i++)for(let j=0;j<N;j++){let a=idx(i,j),b=idx(i,j+1),c=idx(i+1,j),d=idx(i+1,j+1);F.push([a,b,c],[b,d,c])}
 let degenerate=0,edge=new Map(),normals=V.map(()=>[0,0,0]);
 for(const f of F){let [a,b,c]=f.map(i=>V[i]),u=b.map((x,k)=>x-a[k]),v=c.map((x,k)=>x-a[k]),n=[u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0]];if(Math.hypot(...n)<1e-10)degenerate++;for(const i of f)for(let k=0;k<3;k++)normals[i][k]+=n[k];for(let k=0;k<3;k++){let key=[f[k],f[(k+1)%3]].sort((a,b)=>a-b).join(",");edge.set(key,(edge.get(key)||0)+1)}}
 normals=normals.map(n=>{let m=Math.hypot(...n)||1;return n.map(x=>x/m)});
 let W=660,H=220,pix=new Uint8Array(W*H*3).fill(225),views=[0,Math.PI/4,Math.PI/2],cover=[];
 for(let k=0;k<views.length;k++){let t=views[k],co=Math.cos(t),si=Math.sin(t),sz=94,depth=new Float64Array(H*H).fill(-Infinity),P=V.map(([x,y,z])=>[H/2+sz*(x*co-z*si),H/2-sz*y,x*si+z*co]);
 let S=normals.map((n,i)=>{let shade=.48+.52*Math.max(0,(-.28*(n[0]*co-n[2]*si)+.4*n[1]+.87*(n[0]*si+n[2]*co)));return C[i].map(x=>clamp(x*shade,0,255))});
 for(const f of F){let [a,b,c]=f.map(i=>P[i]),den=(b[1]-c[1])*(a[0]-c[0])+(c[0]-b[0])*(a[1]-c[1]);if(Math.abs(den)<1e-9)continue;
 let minx=Math.max(0,Math.floor(Math.min(a[0],b[0],c[0]))),maxx=Math.min(H-1,Math.ceil(Math.max(a[0],b[0],c[0]))),miny=Math.max(0,Math.floor(Math.min(a[1],b[1],c[1]))),maxy=Math.min(H-1,Math.ceil(Math.max(a[1],b[1],c[1])));
 for(let y=miny;y<=maxy;y++)for(let x=minx;x<=maxx;x++){let u=((b[1]-c[1])*(x+.5-c[0])+(c[0]-b[0])*(y+.5-c[1]))/den,v=((c[1]-a[1])*(x+.5-c[0])+(a[0]-c[0])*(y+.5-c[1]))/den,w=1-u-v;if(Math.min(u,v,w)<0)continue;let z=u*a[2]+v*b[2]+w*c[2],i=y*H+x;if(z<=depth[i])continue;depth[i]=z;for(let j=0;j<3;j++)pix[(y*W+k*H+x)*3+j]=Math.round(u*S[f[0]][j]+v*S[f[1]][j]+w*S[f[2]][j])}
 }cover.push(depth.filter(Number.isFinite).length)}
 function b64(a){let s="",abc="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";for(let i=0;i<a.length;i+=3){let n=(a[i]<<16)|((a[i+1]||0)<<8)|(a[i+2]||0);s+=abc[n>>18]+abc[(n>>12)&63]+(i+1<a.length?abc[(n>>6)&63]:"=")+(i+2<a.length?abc[n&63]:"=")}return s}
 const big=n=>[(n>>>24)&255,(n>>>16)&255,(n>>>8)&255,n&255];
 function crc(a){let c=0xffffffff;for(let v of a){c^=v;for(let i=0;i<8;i++)c=(c>>>1)^((c&1)?0xedb88320:0)}return (c^0xffffffff)>>>0}
 function chunk(name,a){let body=[...name].map(x=>x.charCodeAt(0)).concat(a);return big(a.length).concat(body,big(crc(body)))}
 let raw=[];for(let y=0;y<H;y++){raw.push(0);for(let x=0;x<W*3;x++)raw.push(pix[y*W*3+x])}
 let z=[0x78,0x01],aa=1,bb=0;for(let i=0;i<raw.length;i+=65535){let n=Math.min(65535,raw.length-i);z.push(i+n===raw.length?1:0,n&255,n>>8,(~n)&255,((~n)>>8)&255);for(let j=i;j<i+n;j++){let v=raw[j];z.push(v);aa=(aa+v)%65521;bb=(bb+aa)%65521}}z=z.concat(big((bb<<16)|aa));
 let png=[137,80,78,71,13,10,26,10].concat(chunk("IHDR",big(W).concat(big(H),[8,2,0,0,0])),chunk("IDAT",z),chunk("IEND",[]));
 let ply=["ply","format ascii 1.0","comment experimental face-disc open patch not complete character","element vertex "+V.length,"property float x","property float y","property float z","property uchar red","property uchar green","property uchar blue","element face "+F.length,"property list uchar int vertex_indices","end_header"].concat(V.map((v,i)=>v.map(x=>x.toFixed(6)).concat(C[i]).join(" ")),F.map(f=>"3 "+f.join(" "))).join("\n")+"\n";
 return {ply,png:b64(png),metrics:{vertices:V.length,triangles:F.length,degenerate,finite:V.every(v=>v.every(Number.isFinite)),boundaryEdges:[...edge.values()].filter(x=>x===1).length,nonmanifoldEdges:[...edge.values()].filter(x=>x>2).length,depthExtent:Math.max(...V.map(v=>v[2]))-Math.min(...V.map(v=>v[2])),cover,viewsDegrees:[0,45,90],pngBytes:png.length,plyBytes:ply.length}}
}
// Call experiment() for PLY, base64 PNG and metrics.
