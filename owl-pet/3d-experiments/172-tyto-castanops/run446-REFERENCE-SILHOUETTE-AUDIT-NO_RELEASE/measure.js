function measurePNG(base64, candidate=false){
const abc="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
const d=[];let acc=0,nb=0;for(const c of base64){let n=abc.indexOf(c);if(n<0)continue;acc=(acc<<6)|n;nb+=6;if(nb>=8){nb-=8;d.push((acc>>>nb)&255);}}
const be=(a,i)=>((a[i]<<24)|(a[i+1]<<16)|(a[i+2]<<8)|a[i+3])>>>0;
let W=be(d,16),H=be(d,20),depth=d[24],ct=d[25],interlace=d[28],packed=[];
if(depth!==8||interlace!==0||![2,6].includes(ct))throw Error("unsupported PNG "+[W,H,depth,ct,interlace]);
for(let i=8;i<d.length;){let n=be(d,i),s=String.fromCharCode(...d.slice(i+4,i+8));if(s==="IDAT")packed=packed.concat(d.slice(i+8,i+8+n));i+=n+12;}
let pos=16,out=[];const bits=n=>{let v=0;for(let j=0;j<n;j++,pos++)v|=((packed[pos>>3]>>(pos&7))&1)<<j;return v;};
function tree(lens){let count=Array(16).fill(0),next=Array(16).fill(0),map={};for(let l of lens)if(l)count[l]++;let c=0;for(let i=1;i<=15;i++){c=(c+count[i-1])<<1;next[i]=c;}for(let k=0;k<lens.length;k++){let l=lens[k];if(l){let c=next[l]++;map[l+":"+c]=k;}}return map}
function sym(t){let c=0;for(let i=1;i<=15;i++){c=(c<<1)|bits(1);let a=t[i+":"+c];if(a!==undefined)return a;}throw Error("bad huffman");}
let final=0;
const lb=[3,4,5,6,7,8,9,10,11,13,15,17,19,23,27,31,35,43,51,59,67,83,99,115,131,163,195,227,258],le=[0,0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,0],db=[1,2,3,4,5,7,9,13,17,25,33,49,65,97,129,193,257,385,513,769,1025,1537,2049,3073,4097,6145,8193,12289,16385,24577],de=[0,0,0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13];
while(!final){final=bits(1);let type=bits(2);if(type===0){pos=(pos+7)&~7;let n=bits(16),nn=bits(16);if((n^nn)!==65535)throw Error("bad length");for(let i=0;i<n;i++)out.push(bits(8));continue;}let a,b;if(type===1){a=tree(Array.from({length:288},(_,i)=>i<144?8:i<256?9:i<280?7:8));b=tree(Array(32).fill(5));}else if(type===2){let nl=bits(5)+257,nd=bits(5)+1,nc=bits(4)+4,cl=Array(19).fill(0),order=[16,17,18,0,8,7,9,6,10,5,11,4,12,3,13,2,14,1,15];for(let i=0;i<nc;i++)cl[order[i]]=bits(3);let t=tree(cl),l=[];while(l.length<nl+nd){let s=sym(t);if(s<16)l.push(s);else{let n=s===16?bits(2)+3:s===17?bits(3)+3:bits(7)+11,v=s===16?l.at(-1):0;while(n--)l.push(v);}}a=tree(l.slice(0,nl));b=tree(l.slice(nl));}else throw Error("bad deflate block");
while(true){let s=sym(a);if(s<256)out.push(s);else if(s===256)break;else{let k=s-257,n=lb[k]+bits(le[k]),ds=sym(b),dist=db[ds]+bits(de[ds]);while(n--)out.push(out[out.length-dist]);}if(out.length>W*H*5+H)throw Error("inflate overflow");}}
let ch=ct===6?4:3,stride=W*ch,pix=new Uint8Array(W*H*ch),q=0;function pa(a,b,c){let p=a+b-c,aa=Math.abs(p-a),bb=Math.abs(p-b),cc=Math.abs(p-c);return aa<=bb&&aa<=cc?a:bb<=cc?b:c}
if(out.length!==H*(stride+1))throw Error("scanline size mismatch");for(let y=0;y<H;y++){let f=out[q++];for(let x=0;x<stride;x++){let i=y*stride+x,a=x>=ch?pix[i-ch]:0,b=y?pix[i-stride]:0,c=y&&x>=ch?pix[i-stride-ch]:0;pix[i]=(out[q++]+(f===0?0:f===1?a:f===2?b:f===3?Math.floor((a+b)/2):pa(a,b,c)))&255;}}
let vw=candidate?W/4:W,mask=new Uint8Array(vw*H);for(let y=0;y<H;y++)for(let x=0;x<vw;x++){let i=(y*W+x)*ch;mask[y*vw+x]=candidate?(Math.max(...pix.slice(i,i+3).map(v=>Math.abs(v-42)))>12?1:0):(pix[i+3]>=128?1:0);}
let xmin=vw,ymin=H,xmax=-1,ymax=-1,n=0;for(let y=0;y<H;y++)for(let x=0;x<vw;x++)if(mask[y*vw+x]){xmin=Math.min(xmin,x);xmax=Math.max(xmax,x);ymin=Math.min(ymin,y);ymax=Math.max(ymax,y);n++;}
let w=xmax-xmin+1,h=ymax-ymin+1;let rows=[];for(let frac of [.1,.2,.3,.4,.5,.6,.7,.8,.9,.95]){let y=ymin+Math.round(frac*(h-1)),xs=[];for(let x=xmin;x<=xmax;x++)if(mask[y*vw+x])xs.push(x);rows.push({fraction:frac,widthOverHeight:Math.round((xs.length?(xs.at(-1)-xs[0]+1)/h:0)*1000)/1000,occupiedOverHeight:Math.round(xs.length/h*1000)/1000});}
return{width:W,height:H,colorType:ct,viewWidth:vw,bbox:[xmin,ymin,xmax,ymax],foregroundPixels:n,widthOverHeight:w/h,fillRatio:n/(w*h),rows};
}
