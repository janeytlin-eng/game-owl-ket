#!/usr/bin/env python3
"""Run96 - independent physical 3D sculpt/tract experiment for #172 right mesoptile.
Research only. No approval is inferred from mesh/export/render success.
Unlike old recolour/ellipsoid experiments, this builds a continuous anatomically
constrained outer volume, integrated heart colour field, custom bent claws,
short wings plus spatially directed overlapping feather tracts.
All geometry is mesh 3D; no SVGs, rendered impostors, or commercial AI.
"""
import os, sys, json, hashlib, math
from pathlib import Path
import numpy as np
import trimesh
from skimage.measure import marching_cubes

OUT=Path(sys.argv[1] if len(sys.argv)>1 else "qa96").resolve()
OUT.mkdir(parents=True, exist_ok=True)
rng=np.random.default_rng(1729601)

def ellipsoid(X,Y,Z,x,y,z,rx,ry,rz):
    return (np.sqrt(((X-x)/rx)**2+((Y-y)/ry)**2+((Z-z)/rz)**2)-1)*min(rx,ry,rz)

def blend(a,b,k):
    h=np.maximum(k-np.abs(a-b),0)/k
    return np.minimum(a,b)-h*h*k*.25

def heart(x,z):
    u=x/.61
    v=(z-2.37)/.48
    return (u*u+v*v-1)**3-u*u*v**3

def field(X,Y,Z):
    # Unified continuous skull, neck, chest and rump; wing mounds are almost
    # submerged, not adult-like layered flight feathers or applied ovoids.
    body=ellipsoid(X,Y,Z,0,.09,1.23,.605,.545,.765)
    thorax=ellipsoid(X,Y,Z,0,.00,1.64,.60,.52,.51)
    head=ellipsoid(X,Y,Z,0,-.025,2.27,.735,.625,.68)
    neck=ellipsoid(X,Y,Z,0,.045,1.89,.48,.50,.47)
    d=blend(body,thorax,.25)
    d=blend(d,neck,.28)
    d=blend(d,head,.21)
    for side in (-1,1):
        # Fairly flat short buried wing planes, not long adult primary fans.
        wing=ellipsoid(X,Y,Z,side*.565,.17,1.40,.24,.41,.48)
        d=blend(d,wing,.105)
    # Slight physical inset in the cream heart, on the frontal cranium only.
    f=heart(X,Z)
    front=np.clip((-Y-.20)/.30,0,1)
    inset=.023*(f<0)*front*np.clip((Z-1.90)/.25,0,1)
    return d+inset

res=153
bounds=[(-1.01,1.01),(-.91,.94),(.31,3.02)]
axes=[np.linspace(a,b,n,dtype=np.float32) for a,b,n in
      [(bounds[0][0],bounds[0][1],res),
       (bounds[1][0],bounds[1][1],res),
       (bounds[2][0],bounds[2][1],196)]]
X,Y,Z=np.meshgrid(*axes,indexing="ij",copy=False)
volume=field(X,Y,Z).astype(np.float32)
verts,faces,normals,_=marching_cubes(volume,level=0,spacing=
    (axes[0][1]-axes[0][0],axes[1][1]-axes[1][0],axes[2][1]-axes[2][0]))
verts+=np.array([axes[0][0],axes[1][0],axes[2][0]])
del X,Y,Z,volume

outer=trimesh.Trimesh(vertices=verts,faces=faces,process=False)
outer.fix_normals()
p=outer.vertices
f=heart(p[:,0],p[:,2])
front=np.clip((-p[:,1]-.14)/.34,0,1)
# Facial plumage is continuous skin colour, not a flat glued-on heart disk.
heart_in=np.clip(.51-3.8*f,0,1)*front*np.clip((p[:,2]-1.84)/.19,0,1)
ruff=np.exp(-np.minimum((f/.115)**2,60))*front
base=np.array([225,214,184.],dtype=float)
colour=np.tile(base,(len(p),1))
vnoise=(np.sin(17.3*p[:,0]+10.2*p[:,2])*np.sin(12.5*p[:,1]+7.7*p[:,2]))
colour+=vnoise[:,None]*3
colour+=np.clip((p[:,2]-1.95)/.35,0,1)[:,None]*np.array([-3,-3,-2])
colour=colour*(1-heart_in[:,None])+np.array([247,236,213])*heart_in[:,None]
colour=colour*(1-.48*ruff[:,None])+np.array([159,116,75])*(.48*ruff[:,None])
# Back and wing coverts show subtle warm shading, NOT barred adult feathers.
back=np.clip((p[:,1]-.25)/.45,0,1)
colour-=back[:,None]*np.array([13,14,13.])
outer.visual.vertex_colors=np.column_stack((np.uint8(np.clip(colour,0,255)),np.full(len(p),255,dtype=np.uint8)))
outer.metadata["role"]="one sculpted continuous head-body-wing volume; natural heart pigment field"

def mesh_with_col(vertices,faces,rgba,role):
    m=trimesh.Trimesh(vertices=np.asarray(vertices,dtype=np.float32),
                     faces=np.asarray(faces,dtype=np.int64),process=False)
    if np.asarray(rgba).ndim==1:
        m.visual.vertex_colors=np.repeat(np.asarray(rgba,dtype=np.uint8)[None,:],len(vertices),axis=0)
    else:
        m.visual.vertex_colors=np.asarray(rgba,dtype=np.uint8)
    m.metadata["role"]=role
    return m

objects={"continuous_juvenile_sculpt":outer}
def oval(name,center,scale,col,subdiv=3):
    m=trimesh.creation.icosphere(subdivisions=subdiv,radius=1.0)
    m.vertices=m.vertices*np.asarray(scale)+np.asarray(center)
    m.visual.vertex_colors=np.tile(np.asarray(col,dtype=np.uint8),(len(m.vertices),1))
    objects[name]=m

# Eyes are proportionate, set IN the sockets; small iris glints are textured
# inset highlights rather than standalone big shiny toy buttons.
for side in (-1,1):
    x=side*.312
    oval("deep_socket_%s"%side,(x,-.477,2.41),(.131,.037,.142),[143,111,77,255],3)
    oval("black_iris_%s"%side,(x,-.512,2.412),(.088,.045,.103),[22,20,19,255],4)
    oval("tiny_specular_%s"%side,(x-.025,-.550,2.453),(.020,.006,.023),[211,198,176,255],2)

def sweep(name,points,radii,color,radial=9):
    """Actual tapered curved tubular surface, used for keratin claws and toe pads."""
    points=np.array(points,dtype=float);radii=np.array(radii)
    vv=[];ff=[]
    for i,c in enumerate(points):
        t=points[min(i+1,len(points)-1)]-points[max(i-1,0)]
        t=t/max(np.linalg.norm(t),1e-8)
        a=np.cross(t,[1,0,0])
        if np.linalg.norm(a)<.1:a=np.cross(t,[0,1,0])
        a/=np.linalg.norm(a);b=np.cross(t,a)
        for j in range(radial):
            ang=2*math.pi*j/radial
            vv.append(c+radii[i]*(math.cos(ang)*a+math.sin(ang)*b))
    for i in range(len(points)-1):
        for j in range(radial):
            a=i*radial+j;b=i*radial+(j+1)%radial;c=(i+1)*radial+j;d=(i+1)*radial+(j+1)%radial
            ff.extend([[a,b,d],[a,d,c]])
    ff.extend([[0,(j+1)%radial,j] for j in range(1,radial-1)])
    idx=(len(points)-1)*radial
    ff.extend([[idx,idx+j,idx+(j+1)%radial] for j in range(1,radial-1)])
    objects[name]=mesh_with_col(vv,ff,color,name)

# A petite downward-hooked ivory bill. Real curved 3D section, not a pasted triangle.
sweep("ivory_hook_bill",[(0,-.53,2.23),(0,-.598,2.181),(0,-.64,2.127),(0,-.627,2.074)],
      [.067,.076,.050,.007],[218,196,149,255],11)

# Three stout toes per foot with curved tips planted on the hollow lip.
for side in (-1,1):
    sx=side*.335
    for k in (-1,0,1):
        x=sx+k*.065
        points=[(sx,-.235,.65),
                (sx+k*.024,-.34,.515),
                (x,-.49,.37),
                (x+k*.028,-.55,.324)]
        sweep("toe_%s_%s"%(side,k),points,[.073,.063,.048,.022],[160,120,81,255],9)
        sweep("claw_%s_%s"%(side,k),[(x+k*.028,-.54,.343),(x+k*.045,-.595,.323),(x+k*.056,-.611,.302)],
              [.032,.021,.004],[93,79,67,255],7)

# Wooden broad tree hollow rim, irregular annular wood — not a smooth pipe.
def bark():
    V=[];F=[];C=[]
    n=92
    # front lower lip is high enough to support all six foot tips.
    rings=[(.47,.31),(.63,.30),(.85,.24),(1.01,.15),(1.015,-.24),(.83,-.37)]
    for ri,(r,z0) in enumerate(rings):
        for j in range(n):
            a=2*math.pi*j/n
            wig=.022*math.sin(13*a+ri*.30)+.017*math.sin(29*a-ri*.24)
            rr=r+wig
            x=rr*math.cos(a)
            y=.16+rr*.69*math.sin(a)
            z=z0+.033*math.cos(5*a)+.019*math.sin(19*a+ri)
            V.append([x,y,z])
            grain=12*math.sin(17*a)+4*math.sin(43*a)
            col=np.clip(np.array([111,88,63])+grain+[ri*1.5,ri*.5,0],0,255)
            C.append([*col,255])
    for ri in range(len(rings)-1):
        for j in range(n):
            a=ri*n+j;b=ri*n+(j+1)%n;c=(ri+1)*n+j;d=(ri+1)*n+(j+1)%n
            F.extend([[a,b,d],[a,d,c]])
    # Inner concave shadow in the cavity
    objects["irregular_senescent_hollow_lip"]=mesh_with_col(V,F,C,"real curved eucalypt hollow rim")
    oval("interior_hollow_shadow",(0,.17,.18),(.48,.35,.10),[55,48,41,255],3)
bark()

def feather_ribbons(seedmesh,count,role,wmin,wmax,lmin,lmax,colour):
    # Unconnected micro-vellus tufts are oriented with the local NORMAL and
    # local TANGENT of the true organic mesh, not spheres/spikes in world axes.
    sam,ind=trimesh.sample.sample_surface(seedmesh,count*4,seed=int(rng.integers(1,1e9)))
    ns=seedmesh.face_normals[ind]
    vs=[];fs=[];cs=[]
    valid=0
    for at,normal in zip(sam,ns):
        if valid>=count:break
        if at[2]<.57 or at[2]>2.86:continue
        hf=heart(at[0],at[2])
        if at[2]>1.90 and at[1]<-.22 and hf<.07:continue
        # On wings tend to short overlapping feather vanes; elsewhere soft down.
        wing=(abs(at[0])>.47 and .94<at[2]<1.82)
        if role=="wing" and not wing:continue
        if role=="body" and wing and rng.random()<.76:continue
        down=np.array([.07*math.copysign(1,at[0]),.08,-1.])
        if at[2]>2.50:down=np.array([at[0]*.20,at[1]*.22,.20])
        tangent=down-np.dot(down,normal)*normal
        tn=np.linalg.norm(tangent)
        if tn<.12:continue
        tangent/=tn
        cross=np.cross(normal,tangent);cross/=max(np.linalg.norm(cross),1e-9)
        length=rng.uniform(lmin,lmax)
        width=rng.uniform(wmin,wmax)
        start=at+normal*.008
        drift=normal*rng.uniform(.014,.035)
        i0=len(vs)
        for k,t in enumerate([0,.20,.43,.68,1]):
            taper=[.30,.92,1.0,.70,.01][k]
            centre=start+t*length*tangent+(t**1.65)*drift
            # Tiny 3D crimp, no rigid spike or punctate geometry.
            centre+=cross*(.007*math.sin(t*math.pi)*rng.choice([-1,1]))
            for sign in (-1,1):
                vs.append(centre+sign*width*taper*.5*cross)
                shade=rng.normal(0,4)
                cs.append(np.uint8(np.clip(np.array([*colour,255])+shade,0,255)))
        for k in range(4):
            a=i0+2*k;b=a+1;c=a+2;d=a+3
            fs.extend([[a,b,d],[a,d,c]])
        valid+=1
    if len(fs):objects["directional_%s_%s_vellus_fibres"%(role,valid)]=mesh_with_col(vs,fs,cs,"organic surface-following "+role+" feather tracts")
    return valid

# Actual face is recessed continuous surface colour and ruff is feathered,
# while side wing tract layers use short vanes, never long adult remiges.
body_groom=feather_ribbons(outer,2500,"body",.014,.034,.065,.123,[244,232,207])
wing_groom=feather_ribbons(outer,340,"wing",.024,.058,.13,.23,[230,218,188])

scene=trimesh.Scene()
for name,mesh in objects.items():
    scene.add_geometry(mesh,geom_name=name,node_name=name)
# Export for glTF/WebGL Y-up: original +Z up -> glTF +Y; original
# front -Y -> glTF front +Z, matching real orbit/GLTF conventions.
scene.apply_transform(trimesh.transformations.rotation_matrix(-math.pi/2,[1,0,0]))
target=OUT/"run96_anatomy_directional_down_NOT_APPROVED.glb"
# GLB is re-exportable real triangles, no encoded static picture.
glb=scene.export(file_type="glb")
# Explicit nonmetal PBR for GLB COLOR_0 (Run91 browser darkbody bug).
def pbr_repair(blob):
    import struct
    assert blob[:4]==b"glTF"
    off=12;chunks=[]
    while off<len(blob):
        size,ty=struct.unpack_from("<II",blob,off);off+=8
        chunks.append((ty,blob[off:off+size]));off+=size
    assert chunks and chunks[0][0]==0x4e4f534a
    js=json.loads(chunks[0][1].decode("utf-8").rstrip(" \x00"))
    mats=js.setdefault("materials",[])
    if not mats:mats.append({})
    for m in mats:
        m["pbrMetallicRoughness"]={"baseColorFactor":[1,1,1,1],"metallicFactor":0,"roughnessFactor":.96}
        m["doubleSided"]=True
        m["alphaMode"]="OPAQUE"
    colprim=0
    for m in js.get("meshes",[]):
        for prim in m["primitives"]:
            prim["material"]=min(int(prim.get("material",0)),len(mats)-1)
            if "COLOR_0" in prim["attributes"]:colprim+=1
    if colprim==0:raise ValueError("GLB lost every vertex color attribute")
    new=json.dumps(js,separators=(",",":")).encode()
    new+=b" "*((-len(new))%4)
    parts=[struct.pack("<II",len(new),0x4e4f534a)+new]
    parts+=[struct.pack("<II",len(data),ty)+data for ty,data in chunks[1:]]
    end=b"".join(parts)
    return struct.pack("<4sII",b"glTF",2,12+len(end))+end,colprim
glb,colprim=pbr_repair(glb)
target.write_bytes(glb)
loaded=trimesh.load(target,force="scene")
assert len(loaded.geometry)>5 and sum(len(m.faces) for m in loaded.geometry.values())>20000
assert outer.is_watertight
stats={
    "verdict":"UNREVIEWED_ART_REQUIRES_MULTIVIEW_AND_MOBILE_GATES",
    "method":"new single continuous anatomical SDF mesh, real wing protrusions, vertex-heart, local-tangent feather ribbon tracts",
    "source":"independently authored geometry, no external downloaded model, no paid API",
    "glb":target.name,"bytes":target.stat().st_size,
    "sha256":hashlib.sha256(glb).hexdigest(),
    "glTF_pbr_colour_primitives":colprim,"parts":len(loaded.geometry),
    "triangles":int(sum(len(m.faces) for m in loaded.geometry.values())),
    "main_shell_watertight":bool(outer.is_watertight),
    "body_tufts":body_groom,"short_wing_tufts":wing_groom,
    "real_phone_gpu_tested":False,"animated_rig_tested":False,
    "quality_assurance":"Never publish until human multi-view art gate explicitly approved"
}
(OUT/"run96_metrics.json").write_text(json.dumps(stats,indent=2))
print("RUN96_ACTUAL_GLTF",json.dumps(stats),flush=True)
