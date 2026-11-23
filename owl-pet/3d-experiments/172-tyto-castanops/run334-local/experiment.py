import numpy as np,trimesh,hashlib,json,base64
from PIL import Image
from scipy.ndimage import gaussian_filter
from pathlib import Path
from playwright.sync_api import sync_playwright
r=np.random.default_rng(334); S=128
noise=lambda s: gaussian_filter(r.random((S,S)),s,mode='wrap')
def norm(a):return (a-a.min())/(a.max()-a.min())
length=.22+.78*norm(.7*norm(noise(.8))+.3*norm(noise(4)))
N=25; M=37; theta,phi=np.meshgrid(np.linspace(.001,np.pi-.001,N),np.linspace(0,2*np.pi,M),indexing='ij'); unit=np.stack([np.sin(theta)*np.cos(phi),np.sin(theta)*np.sin(phi),np.cos(theta)],-1).reshape(-1,3)
scale=np.array([.025,.021,.018]); normals=unit/scale;normals/=np.linalg.norm(normals,axis=1)[:,None];uv=np.c_[phi.ravel()/(2*np.pi),1-theta.ravel()/np.pi]; faces=[]
for i in range(N-1):
 for j in range(M-1):
  k=i*M+j;faces.extend([[k,k+M,k+1],[k+1,k+M,k+M+1]])
meshes=[]
for t in [0,.18,.34,.50,.66,.82]:
 rgb=np.broadcast_to(np.array([242,226,201],dtype=np.uint8),(S,S,3));alpha=np.full((S,S),255,dtype=np.uint8) if not t else np.where(length>t,255,0).astype('uint8');tex=Image.fromarray(np.dstack([rgb,alpha]));mat=trimesh.visual.material.PBRMaterial(baseColorTexture=tex,alphaMode='MASK' if t else 'OPAQUE',alphaCutoff=.5,roughnessFactor=1.,metallicFactor=0.,doubleSided=False);meshes.append(trimesh.Trimesh(unit*scale+normals*t*.004,faces,process=False,visual=trimesh.visual.texture.TextureVisuals(uv=uv,material=mat)))
p=Path('swatch.glb');p.write_bytes(trimesh.Scene(meshes).export(file_type='glb'));g=trimesh.load(p,force='scene');tri=sum(len(m.faces) for m in g.geometry.values());assert tri==10368
JS='''async ({b64,angle,mode})=>{const bytes=Uint8Array.from(atob(b64),c=>c.charCodeAt(0)),dv=new DataView(bytes.buffer),n=dv.getUint32(12,true),j=JSON.parse(new TextDecoder().decode(bytes.slice(20,20+n))),bin=bytes.slice(28+n);const canvas=document.createElement('canvas');canvas.width=390;canvas.height=390;document.body.style.margin='0';document.body.append(canvas);const gl=canvas.getContext('webgl2',{preserveDrawingBuffer:true});if(!gl)throw Error('no webgl2');const shader=(kind,s)=>{let sh=gl.createShader(kind);gl.shaderSource(sh,s);gl.compileShader(sh);if(!gl.getShaderParameter(sh,gl.COMPILE_STATUS))throw Error(gl.getShaderInfoLog(sh));return sh};const pr=gl.createProgram();gl.attachShader(pr,shader(gl.VERTEX_SHADER,`#version 300 es
in vec3 pos;in vec2 uv;out vec2 t;out vec3 p;uniform float a;void main(){vec3 q=vec3(cos(a)*pos.x+sin(a)*pos.z,pos.y,-sin(a)*pos.x+cos(a)*pos.z);p=q;t=uv;gl_Position=vec4(q/0.036,1.);}`));gl.attachShader(pr,shader(gl.FRAGMENT_SHADER,`#version 300 es
precision highp float;in vec2 t;in vec3 p;uniform sampler2D tex;uniform float cut;uniform int mode;out vec4 c;void main(){vec4 s=texture(tex,t);if(s.a<cut)discard;vec3 n=normalize(p);vec3 rgb=mode==2?vec3(242.,226.,201.)/255.:s.rgb;c=vec4(rgb*(.68+.32*max(dot(n,normalize(vec3(-.3,.6,-1.))),0.)),1.);}`));gl.linkProgram(pr);if(!gl.getProgramParameter(pr,gl.LINK_STATUS))throw Error(gl.getProgramInfoLog(pr));gl.useProgram(pr);gl.uniform1f(gl.getUniformLocation(pr,'a'),angle);gl.uniform1i(gl.getUniformLocation(pr,'mode'),mode);gl.enable(gl.DEPTH_TEST);gl.clearColor(.19,.22,.24,1);gl.clear(gl.COLOR_BUFFER_BIT|gl.DEPTH_BUFFER_BIT);function acc(i){let a=j.accessors[i],v=j.bufferViews[a.bufferView];return [a,bin.slice((v.byteOffset||0)+(a.byteOffset||0),(v.byteOffset||0)+v.byteLength)]}let tris=0;for(let m of j.meshes)for(let p of m.primitives){for(let [key,name,size] of [['POSITION','pos',3],['TEXCOORD_0','uv',2]]){let [a,d]=acc(p.attributes[key]);let buf=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,buf);gl.bufferData(gl.ARRAY_BUFFER,d,gl.STATIC_DRAW);let l=gl.getAttribLocation(pr,name);gl.enableVertexAttribArray(l);gl.vertexAttribPointer(l,size,a.componentType,false,0,0)}let mat=j.materials[p.material],img=j.images[j.textures[mat.pbrMetallicRoughness.baseColorTexture.index].source],v=j.bufferViews[img.bufferView],blob=new Blob([bin.slice(v.byteOffset||0,(v.byteOffset||0)+v.byteLength)],{type:img.mimeType}),bmp=await (mode==1?createImageBitmap(blob,{premultiplyAlpha:'none',colorSpaceConversion:'none'}):createImageBitmap(blob));let tex=gl.createTexture();gl.bindTexture(gl.TEXTURE_2D,tex);gl.texImage2D(gl.TEXTURE_2D,0,gl.RGBA,gl.RGBA,gl.UNSIGNED_BYTE,bmp);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_MIN_FILTER,gl.LINEAR);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_MAG_FILTER,gl.LINEAR);gl.uniform1f(gl.getUniformLocation(pr,'cut'),mat.alphaMode==='MASK'?mat.alphaCutoff:0);let [a,d]=acc(p.indices),buf=gl.createBuffer();gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER,buf);gl.bufferData(gl.ELEMENT_ARRAY_BUFFER,d,gl.STATIC_DRAW);gl.drawElements(gl.TRIANGLES,a.count,a.componentType,0);tris+=a.count/3}gl.finish();return {tris,error:gl.getError(),version:gl.getParameter(gl.VERSION),png:canvas.toDataURL('image/png')}}'''
report=[];montage=Image.new('RGB',(1170,1170));b64=base64.b64encode(p.read_bytes()).decode()
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']);page=b.new_page(viewport={'width':390,'height':780})
 for mode in range(3):
  for i,angle in enumerate([0,1.1,2.3]):
   page.set_content('<body></body>');res=page.evaluate(JS,dict(b64=b64,angle=angle,mode=mode));f=Path(f'{mode}-{i}.png');f.write_bytes(base64.b64decode(res.pop('png').split(',')[1]));im=Image.open(f).convert('RGB');montage.paste(im,(i*390,mode*390));report.append(dict(mode=mode,angle=angle,**res))
 b.close()
montage.save('montage.jpg',quality=92)
# Exact image comparison within foreground, reference is shader constant RGB.
comparisons=[]
for i in range(3):
 ref=np.asarray(Image.open(f'2-{i}.png').convert('RGB')).astype(int);mask=ref[:,:,0]>100
 for mode in [0,1]:
  a=np.asarray(Image.open(f'{mode}-{i}.png').convert('RGB')).astype(int);err=np.abs(a-ref)[mask];comparisons.append(dict(mode=mode,view=i,foreground_pixels=int(mask.sum()),mean_abs_rgb=float(err.mean()),pct_pixels_diff_gt10=float((err.max(axis=1)>10).mean()*100)))
result=dict(bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),triangles=tri,views=report,comparisons=comparisons);Path('report.json').write_text(json.dumps(result,indent=2));print(json.dumps(result))
