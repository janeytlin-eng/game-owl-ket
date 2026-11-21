#!/usr/bin/env python3
"""Run274 actual native 3D PBR microdown bake — isolated research, NO RELEASE.
Pinned Hunyuan neural base: upstream NONCOMMERCIAL. No geometric hair cards,
no SVG or 2D-rotation substitute; all outputs preserve original 133268 faces.
"""
import os,json,struct,hashlib,math
from pathlib import Path
import numpy as np, trimesh, vtk
from scipy.ndimage import gaussian_filter
from PIL import Image, ImageDraw
R=Path(os.environ["OWL172_OUTPUT"]);R.mkdir(parents=True,exist_ok=True)
SOURCE=Path(os.environ["OWL172_INPUT"])
PIN="da21a63c0ec7dbdb8da920896599eb7cafd62fcf94de2e25bae016dd218724ea"
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert sha(SOURCE)==PIN,"source hash mismatch, fail closed"
m=trimesh.load(SOURCE,force="mesh",skip_materials=True)
assert m.is_watertight and len(m.vertices)==66596 and len(m.faces)==133268
V=np.asarray(m.vertices,dtype=np.float32)
F=np.asarray(m.faces,dtype=np.uint32)
N=np.asarray(m.vertex_normals,dtype=np.float32)
C=np.asarray(m.visual.vertex_colors,dtype=np.uint8)
assert len(C)==len(V)
# Equirectangular UV with the cut on the REAR; duplicate seam vertices, not geometry.
longitude=np.arctan2(V[:,0],V[:,2])
U=np.column_stack(((longitude+np.pi)/(2*np.pi),
 (V[:,1]-float(V[:,1].min()))/float(np.ptp(V[:,1])))).astype(np.float32)
FF=F.copy(); extra={}; dup=[]
for j,tri in enumerate(FF):
    if np.ptp(U[tri,0])>.5:
        for k,ix in enumerate(tri):
            if U[ix,0]<.5:
                if int(ix) not in extra:
                    extra[int(ix)]=len(V)+len(dup);dup.append(int(ix))
                FF[j,k]=extra[int(ix)]
if dup:
    vv=V[dup];nn=N[dup];cc=C[dup];uu=U[dup].copy();uu[:,0]+=1
    V=np.concatenate([V,vv]);N=np.concatenate([N,nn])
    C=np.concatenate([C,cc]);U=np.concatenate([U,uu])
assert len(FF)==133268
# Procedural height atlas: thousands of branching soft feather filaments.
S=1024;rng=np.random.default_rng(172274)
im=Image.new("L",(S,S),125);dr=ImageDraw.Draw(im)
for i in range(15500):
    x=float(rng.uniform(0,S));y=float(rng.uniform(0,S))
    length=float(rng.uniform(6,20));bend=float(rng.normal(0,3.5))
    level=int(rng.uniform(130,220))
    dr.line([(x,y),(x+bend*.25,y+length*.4),(x+bend,y+length)],
      fill=level,width=int(rng.choice([1,1,1,2])),joint="curve")
    if i%3==0:
        for t in (.3,.6):
            xx=x+t*t*bend;yy=y+t*length
            dr.line([(xx,yy),(xx-3,yy+4)],fill=level,width=1)
            dr.line([(xx,yy),(xx+3,yy+4)],fill=level,width=1)
raw=np.asarray(im,dtype=np.float32)/255
def make_maps(blur,ampl,label):
    height=gaussian_filter(raw,sigma=blur,mode="wrap")
    gy,gx=np.gradient(height)
    norm=np.stack([-gx*ampl,gy*ampl,np.ones_like(gx)],axis=2)
    norm/=np.maximum(np.linalg.norm(norm,axis=2,keepdims=True),1e-6)
    npng=R/(label+"_normal.png")
    Image.fromarray(np.clip((norm*.5+.5)*255,0,255).astype("uint8"),"RGB").save(npng,optimize=True)
    base=np.empty((S,S,4),np.uint8)
    tint=.94+.11*np.clip(height-.42,0,.3)/.3
    for k,c in enumerate((250,243,229)):base[:,:,k]=np.clip(c*tint,0,255).astype("uint8")
    base[:,:,3]=255
    cpng=R/(label+"_basecolor.png")
    Image.fromarray(base,"RGBA").save(cpng,optimize=True)
    return npng,cpng
def export_glb(normalfile,colorfile,out):
    buf=bytearray();views=[];access=[]
    def attach(raw,target=None):
        buf.extend(b"\0"*((-len(buf))%4))
        offset=len(buf);buf.extend(raw)
        d={"buffer":0,"byteOffset":offset,"byteLength":len(raw)}
        if target:d["target"]=target
        views.append(d);return len(views)-1
    def attrib(a,component,shape,bounds=False):
        a=np.ascontiguousarray(a)
        ix=attach(a.tobytes(),34963 if shape=="SCALAR" else 34962)
        d={"bufferView":ix,"componentType":component,"count":len(a),"type":shape}
        if component==5121 and shape=="VEC4":d["normalized"]=True
        if bounds:
            d["min"]=a.min(axis=0).tolist();d["max"]=a.max(axis=0).tolist()
        access.append(d);return len(access)-1
    p=attrib(V.astype("<f4"),5126,"VEC3",True)
    n=attrib(N.astype("<f4"),5126,"VEC3")
    c=attrib(C.astype("u1"),5121,"VEC4")
    u=attrib(U.astype("<f4"),5126,"VEC2")
    f=attrib(FF.reshape(-1).astype("<u4"),5125,"SCALAR")
    imgs=[{"name":"baked-down-normal","mimeType":"image/png","bufferView":attach(normalfile.read_bytes())},
          {"name":"cream-down-color","mimeType":"image/png","bufferView":attach(colorfile.read_bytes())}]
    gltf={"asset":{"version":"2.0","generator":"owl172-run274-research-NO_RELEASE"},
      "scene":0,"scenes":[{"nodes":[0]}],
      "nodes":[{"mesh":0,"name":"PINNED_NONCOMMERCIAL_ORIGINAL_NEURAL_BODY"}],
      "meshes":[{"name":"continuous_neural_owl_baked_microdown","primitives":[{
        "attributes":{"POSITION":p,"NORMAL":n,"COLOR_0":c,"TEXCOORD_0":u},
        "indices":f,"material":0,"mode":4}]}],
      "materials":[{"name":"Owl172_BAKED_DOWN_NO_RELEASE","alphaMode":"OPAQUE",
        "doubleSided":False,"normalTexture":{"index":0,"scale":1.0},
        "pbrMetallicRoughness":{"baseColorFactor":[1,1,1,1],
          "baseColorTexture":{"index":1},"metallicFactor":0,"roughnessFactor":0.95}}],
      "images":imgs,"textures":[{"source":0,"sampler":0},{"source":1,"sampler":0}],
      "samplers":[{"wrapS":10497,"wrapT":10497,"magFilter":9729,"minFilter":9987}],
      "buffers":[{"byteLength":len(buf)}],"bufferViews":views,"accessors":access}
    raw=json.dumps(gltf,separators=(",",":")).encode()
    raw+=b" "*((-len(raw))%4)
    buf.extend(b"\0"*((-len(buf))%4))
    header=b"glTF"+struct.pack("<II",2,12+8+len(raw)+8+len(buf))
    out.write_bytes(header+struct.pack("<I4s",len(raw),b"JSON")+raw+
                    struct.pack("<I4s",len(buf),b"BIN\0")+buf)
    opened=trimesh.load(out,force="scene")
    assert sum(len(g.faces) for g in opened.geometry.values())==133268
    return {"glb":out.name,"bytes":out.stat().st_size,"sha256":sha(out),
       "triangles":133268,"vertex_count_after_seam_duplicate":len(V),
       "uv_seam_duplicate_vertices":len(dup),
       "normal_texture_sha256":sha(normalfile),"color_texture_sha256":sha(colorfile)}
def six_views(glb,label):
    window=vtk.vtkRenderWindow();window.SetOffScreenRendering(1);window.SetSize(470,470)
    importer=vtk.vtkGLTFImporter();importer.SetFileName(str(glb));importer.SetRenderWindow(window);importer.Update()
    ren=window.GetRenderers().GetFirstRenderer();ren.SetBackground(.78,.80,.84)
    light=vtk.vtkLight();light.SetPosition(2,3,4);light.SetIntensity(1.5);ren.AddLight(light)
    directions={"front":(0,0,1),"threequarter":(.7,0,1),"right":(1,0,0),
       "back":(0,0,-1),"left":(-1,0,0),"above":(0,1,.3)}
    hashes={}
    for name,d in directions.items():
        vector=np.asarray(d,float);vector/=np.linalg.norm(vector)
        camera=ren.GetActiveCamera();camera.SetPosition(*(4.1*vector))
        camera.SetFocalPoint(0,0,0)
        camera.SetViewUp(*((0,1,0) if abs(vector[1])<.9 else (0,0,-1)))
        camera.ParallelProjectionOn();camera.SetParallelScale(1.16)
        ren.ResetCameraClippingRange();window.Render()
        imp=vtk.vtkWindowToImageFilter();imp.SetInput(window);imp.Update()
        p=R/(label+"_"+name+".png")
        png=vtk.vtkPNGWriter();png.SetFileName(str(p))
        png.SetInputConnection(imp.GetOutputPort());png.Write()
        hashes[name]=sha(p)
    window.Finalize();assert len(set(hashes.values()))==6
    sheet=Image.new("RGB",(1410,940),"white");draw=ImageDraw.Draw(sheet)
    for i,name in enumerate(directions):
        x=(i%3)*470;y=(i//3)*470
        sheet.paste(Image.open(R/(label+"_"+name+".png")).convert("RGB"),(x,y))
        draw.text((x+8,y+8),label+" "+name,fill="black")
    sheet.save(R/(label+"_six_real_3D_views.png"))
    return hashes
report={"run":274,"source_sha256":PIN,"upstream_rights":"HUNYUAN_NONCOMMERCIAL",
 "research_only":True,"phone_hardware":"UNTESTED","art":"UNREVIEWED","release":False,
 "mesh_is_native_3D":True,"mesh_geometry_same_as_run271":True,"variants":{}}
for label,sigma,strength in (("fine",.75,8),("coarse",1.8,4)):
    normal,color=make_maps(sigma,strength,label)
    glb=R/(label+"_TRUE3D_BAKED_DOWN_NO_RELEASE.glb")
    info=export_glb(normal,color,glb)
    info["six_spatial_pbr_views"]=six_views(glb,label)
    report["variants"][label]=info
    print("RUN274 "+label+" "+json.dumps(info),flush=True)
(R/"machine-report.json").write_text(json.dumps(report,indent=2)+"\n")
(R/"NO_RELEASE.flag").write_text("ART_UNREVIEWED / NONCOMMERCIAL SOURCE / PHYSICAL_PHONE_UNTESTED / NO_RELEASE\n")
