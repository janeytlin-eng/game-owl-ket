#!/usr/bin/env python3
"""Run263 genuine Run261p neural-owl eye / down research. ALWAYS NO_RELEASE.
Requires input GLB from pinned, previously verified Run261p research artifact.
All geometry is native 3D; only original 20k-triangle neural body is the owl.
"""
import sys,hashlib,json,pathlib
import numpy as np,scipy.sparse as sp,trimesh
P=pathlib.Path(sys.argv[2] if len(sys.argv)>2 else ".")
P.mkdir(parents=True,exist_ok=True)
SOURCE=pathlib.Path(sys.argv[1])
PIN="e3c33c70a8a1136a7548d22d2a272e9c5c254e773959b7705d5261ed0fec4535"
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==PIN
src=trimesh.load(SOURCE,force="scene")
m=list(src.geometry.values())[0]
assert len(src.geometry)==1 and len(m.faces)==20000 and m.is_watertight
rng=np.random.default_rng(263)
# GLB is Y-up: transfer to sculpt workspace X, -Z, Y (Z-up).
v=np.column_stack([m.vertices[:,0],-m.vertices[:,2],m.vertices[:,1]])
e=m.edges_unique
A=sp.coo_matrix((np.ones(2*len(e)),(np.r_[e[:,0],e[:,1]],np.r_[e[:,1],e[:,0]])),shape=(len(v),len(v))).tocsr()
deg=np.maximum(1,np.asarray(A.sum(axis=1)).ravel())
c=v.copy()
w=(np.clip((c[:,1]+.55)/.52,0,1)**2)*np.clip((c[:,2]+.64)/.22,0,1)*.94
for _ in range(10):c+=.23*w[:,None]*((A@c)/deg[:,None]-c)
body=trimesh.Trimesh(vertices=c,faces=m.faces,process=False)
x,y,z=c.T
rgb=np.stack([np.full(len(x),235.),np.full(len(x),222.),np.full(len(x),198.)],axis=1)
rgb+=np.clip((z-.1)/.55,0,1)[:,None]*np.array([10.,17.,24.])
front=np.clip((-y-.66)/.28,0,1)
mask=np.exp(-((x/.50)**4+((z-.33)/.44)**4)*1.7)*front
rgb=rgb*(1-mask[:,None]*.8)+mask[:,None]*.8*np.array([249,239,215])
wing=np.exp(-((np.abs(x)-.61)/.16)**2-((z+.18)/.42)**2)*np.clip((-y-.12)/.55,0,1)
rgb=rgb*(1-wing[:,None]*.32)+wing[:,None]*.32*np.array([210,190,167])
rgb=np.clip(rgb+rng.normal(0,1.8,(len(x),1)),0,255).astype(np.uint8)
body.visual.vertex_colors=np.column_stack([rgb,np.full(len(x),255,dtype=np.uint8)])
def eye(sign):
    verts=[];faces=[];colors=[];N=64;R=15
    for i in range(R+1):
        r=.002+i*.998/R
        for j in range(N):
            t=2*np.pi*j/N
            xx=sign*.205+.105*r*np.cos(t);zz=.435+.105*r*np.sin(t)
            yy=-.765-.045*np.sqrt(max(0,1-r*r))+.027*r*r
            verts.append((xx,yy,zz))
            if r<.43:q=np.array([16,13,11])
            elif r<.70:
                q=np.array([74,44,26])*(.5+.5*np.sin(12*t+3*r))+np.array([38,27,19])*(.5-.5*np.sin(12*t+3*r))
            elif r<.83:q=[21,15,11]
            elif r<.91:q=[80,62,45]
            else:q=[207,187,153]
            colors.append([*np.asarray(q,dtype=np.uint8),255])
    for i in range(R):
        for j in range(N):
            a=i*N+j;b=i*N+(j+1)%N;cc=(i+1)*N+j;d=(i+1)*N+(j+1)%N
            faces.extend(((a,b,d),(a,d,cc)))
    e=trimesh.Trimesh(vertices=verts,faces=faces,process=False)
    e.visual.vertex_colors=np.asarray(colors,dtype=np.uint8)
    return e
idx=np.where((z>-.48)&(y>-.48)&(np.abs(x)<.75))[0]
idx=rng.choice(idx,min(4900,len(idx)),replace=True)
p0=c[idx];d=body.vertex_normals[idx]*.8+np.array([0,0,.38])
d/=np.linalg.norm(d,axis=1)[:,None]
t=np.cross(d,np.array([0,1,0]));t/=np.maximum(1e-6,np.linalg.norm(t,axis=1))[:,None]
hv=[];hf=[];hc=[]
for k,(p,di,ti) in enumerate(zip(p0,d,t)):
    L=rng.uniform(.016,.042);width=rng.uniform(.00065,.00155)
    for i in range(4):
        u=i/3;q=p+di*L*u+np.array([0,0,-1])*L*.2*u*u
        for s in (-1,1):
            hv.append(q+s*width*(1-u*.8)*ti)
            delta=rng.normal(0,3)
            hc.append([int(np.clip(ch+delta,0,255)) for ch in (245,230,207)]+[255])
    for i in range(3):
        a=k*8+2*i;hf.extend(((a,a+1,a+3),(a,a+3,a+2)))
hair=trimesh.Trimesh(vertices=hv,faces=hf,process=False)
hair.visual.vertex_colors=np.asarray(hc,dtype=np.uint8)
s=trimesh.Scene()
for name,g in (("authentic_neural_body",body),("left_iris",eye(-1)),("right_iris",eye(1)),("curved_down",hair)):
    # Undo temporary Z-up coordinates before GLB export
    R=np.eye(4);R[:3,:3]=np.array([[1,0,0],[0,0,1],[0,-1,0]])
    g.apply_transform(R);s.add_geometry(g,geom_name=name)
out=P/"run263_RESEARCH_NATIVE_ART_REJECTED_NO_RELEASE.glb"
out.write_bytes(s.export(file_type="glb"))
check=trimesh.load(out,force="scene")
assert len(check.geometry)==4
report={"source_sha256":PIN,"source_triangles":20000,
        "native_triangles":sum(len(g.faces) for g in check.geometry.values()),
        "native_meshes":len(check.geometry),"sha256":hashlib.sha256(out.read_bytes()).hexdigest(),
        "bytes":out.stat().st_size,"art":"REJECTED","mobile":"UNTESTED","rights":"UNCLEARED","release":"NO_RELEASE"}
(P/"run263_machine_report.json").write_text(json.dumps(report,indent=2)+"\n")
(P/"NO_RELEASE.flag").write_text("ART_REJECTED; PHONE_UNTESTED; RIGHTS_UNCLEARED; NO_RELEASE\n")
print(json.dumps(report,indent=2))
