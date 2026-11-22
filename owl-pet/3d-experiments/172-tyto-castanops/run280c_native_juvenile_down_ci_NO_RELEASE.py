#!/usr/bin/env python3
"""Run280c, independent GitHub Actions native glTF reshape QA, always NO_RELEASE.
This reconstructs the local sculpt and plumes from Run279b original true GLB.
Hunyuan source noncommercial. No 2-D turntable substitution.
"""
import sys, json, struct, hashlib
from pathlib import Path
import numpy as np
import trimesh
from PIL import Image,ImageDraw
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def sm(a,b,x):
    t=np.clip((x-a)/(b-a),0,1);return t*t*(3-2*t)
def restore(glb,mesh):
    b=Path(glb).read_bytes(); assert b[:4]==b'glTF'
    n=struct.unpack_from('<I',b,12)[0]; doc=json.loads(b[20:20+n]); idx=20+n
    idx+=(4-idx%4)%4;size,typ=struct.unpack_from('<I4s',b,idx);assert typ==b'BIN\0'; binary=memoryview(b)[idx+8:idx+8+size]
    def get(k):
        a=doc['accessors'][k];v=doc['bufferViews'][a['bufferView']]
        dt={5121:'u1',5123:'<u2',5126:'<f4'}[a['componentType']]
        dims={'VEC3':3,'VEC4':4}[a['type']];t=np.dtype(dt)
        s=v.get('byteStride',dims*t.itemsize);ofs=v.get('byteOffset',0)+a.get('byteOffset',0)
        x=np.ndarray((a['count'],dims),dtype=t,buffer=binary,offset=ofs,strides=(s,t.itemsize)).copy()
        if a.get('normalized',False):x=x.astype(np.float64)/np.iinfo(t).max
        return x
    p=next(m['primitives'][0] for m in doc['meshes'] if m['name']=='geometry_0')
    assert np.max(abs(get(p['attributes']['POSITION'])-mesh.vertices))<1e-4
    c=get(p['attributes']['COLOR_0']); c=np.rint(c*255).astype(np.uint8)
    if c.shape[1]==3:c=np.c_[c,np.full((len(c),),255,dtype=np.uint8)]
    return c
def sculpt(v):
    p=v.copy();x,y,z=p.T
    r=sm(.11,.55,-z);lo=sm(-.12,-.62,y);keep=1-sm(.32,.58,z)*sm(0,.38,y)
    p[:,2]+=r*(.17+.10*lo)*keep;p[:,1]+=r*lo*.12
    flank=r*(1-sm(.46,.73,abs(x)))*sm(-.51,.18,y)
    p[:,0]+=np.sign(x)*.047*flank
    wing=sm(.49,.78,abs(x))*sm(-.25,-.65,y)*(1-sm(.36,.7,z))
    p[:,0]-=np.sign(x)*wing*.076;p[:,1]+=wing*.085
    belly=sm(-.62,-.28,y)*(1-sm(-.1,.39,y))*(1-sm(.48,.72,abs(x)))*sm(0,.65,z)
    p[:,2]+=belly*.046
    return p
def groom(body,num=4600):
    rng=np.random.default_rng(280);V=[];F=[];C=[]
    for iteration in range(40):
        pts,ix=trimesh.sample.sample_surface(body,(num-len(V)//4)*3+80,seed=281+iteration)
        norms=body.face_normals[ix]
        mask=(pts[:,1]>-.61)&(pts[:,1]<.85)
        mask &= ~((pts[:,2]>.31)&(pts[:,1]>.16)&(abs(pts[:,0])<.57))
        mask &= ~((pts[:,2]>.38)&(pts[:,1]<-.36))
        for p,n in zip(pts[mask],norms[mask]):
            if len(V)//4>=num:break
            n=n/np.linalg.norm(n);along=np.array([0.,-1.,0.]);along-=along.dot(n)*n
            if np.linalg.norm(along)<.15:
                along=np.array([.7,0.,.3]);along-=along.dot(n)*n
            along/=np.linalg.norm(along);side=np.cross(n,along);side/=np.linalg.norm(side)
            L=rng.uniform(.02,.057); w=rng.uniform(.004,.011); root=p+n*.0028
            j=len(V);V.extend([root-along*L*.20,root+along*L*.39-side*w+n*.01,root+along*L+n*.01,root+along*L*.39+side*w+n*.01])
            F.extend([[j,j+1,j+2],[j,j+2,j+3]])
            col=rng.choice(np.array([[247,235,213],[243,231,209],[238,224,201],[251,239,219],[230,214,190]],dtype=np.uint8))
            C.extend([[*col,255]]*4)
        if len(V)//4>=num:break
    assert len(V)//4==num
    a=trimesh.Trimesh(vertices=np.asarray(V),faces=np.asarray(F),process=False)
    a.visual.vertex_colors=np.asarray(C,dtype=np.uint8)
    return a
def view(path,out,stem):
    import vtk
    r=vtk.vtkRenderer();w=vtk.vtkRenderWindow();w.SetOffScreenRendering(1);w.SetSize(420,420);w.AddRenderer(r)
    i=vtk.vtkGLTFImporter();i.SetFileName(str(path));i.SetRenderWindow(w);i.Update()
    assert r.GetActors().GetNumberOfItems()>0
    r.SetBackground(.934,.925,.90)
    cams={'front':(0,0,2.82),'threequarter':(1.87,.18,1.87),'right':(2.82,.1,.04),'back':(0,.1,-2.82),'left':(-2.82,.1,.04),'top':(.01,2.82,.2)}
    for name,pos in cams.items():
        c=r.GetActiveCamera();c.ParallelProjectionOn();c.SetFocalPoint(0,-.05,.10);c.SetPosition(*pos);c.SetViewUp(*( (0,0,-1) if name=='top' else (0,1,0) ));c.SetParallelScale(1.17)
        r.ResetCameraClippingRange();w.Render()
        f=vtk.vtkWindowToImageFilter();f.SetInput(w);f.Update()
        target=out/f'{stem}_{name}.png';q=vtk.vtkPNGWriter();q.SetFileName(str(target));q.SetInputConnection(f.GetOutputPort());q.Write()
        assert target.stat().st_size>5000
if __name__=='__main__':
    inp=Path(sys.argv[1]);out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
    assert sha(inp)=='8eb64c09a58f673c793c31e348f41854b5d4fb13c649afcef36d1a23129e12db'
    s=trimesh.load(inp,force='scene');src=s.geometry['geometry_0'];colors=restore(inp,src)
    assert src.is_watertight and len(src.faces)==55972
    original=src.copy();original.visual.vertex_colors=colors
    new=trimesh.Trimesh(vertices=sculpt(src.vertices),faces=src.faces.copy(),process=False);new.visual.vertex_colors=colors
    plumes=groom(new)
    report={'input_source_sha256':sha(inp),'status':'NATIVE_3D_PASS / ART_REJECTED / MOBILE_PHONE_UNTESTED / RIGHTS_NONCOMMERCIAL / NO_RELEASE','files':{},'sides':6,'source_watertight':bool(src.is_watertight),'deformed_body_watertight':bool(new.is_watertight)}
    for name,body,fuzz in [('control',original,None),('anatomy',new,None),('down',new,plumes)]:
        obj=trimesh.Scene();obj.add_geometry(body,geom_name='continuous_owl_body')
        if fuzz is not None:obj.add_geometry(fuzz,geom_name='curved_soft_down_real_mesh')
        file=out/f'{name}_NORELEASE.glb';file.write_bytes(trimesh.exchange.gltf.export_glb(obj))
        reread=trimesh.load(file,force='scene')
        report['files'][name]={'sha256':sha(file),'bytes':file.stat().st_size,'triangles':sum(len(m.faces) for m in reread.geometry.values()),'meshes':len(reread.geometry)}
        view(file,out,name)
    report['rear_z_min_shift']=float(new.vertices[:,2].min()-src.vertices[:,2].min())
    (out/'QA_REJECTED.json').write_text(json.dumps(report,indent=2))
    print(json.dumps(report,indent=2))
