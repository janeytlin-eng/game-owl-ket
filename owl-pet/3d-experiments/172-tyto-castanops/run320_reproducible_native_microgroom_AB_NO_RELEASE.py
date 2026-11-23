"""Run320: true GLB mesoptile microfibre A/B negative research, not a release.

Source: Run317 original GitHub Actions artifact 14795923598;
extract stability-SF3D-TyTo172-REAL_UNREVIEWED_NO_RELEASE.glb alongside this script
or put it in --output-dir. No paid services. Requires numpy, trimesh, vtk, Pillow, Xvfb.
"""
import os,sys,json,hashlib,argparse
from pathlib import Path
import numpy as np
import trimesh
import vtk
from vtk.util.numpy_support import numpy_to_vtk,numpy_to_vtkIdTypeArray
from PIL import Image,ImageDraw

ap=argparse.ArgumentParser()
ap.add_argument('--output-dir',default='.')
args=ap.parse_args()
root=Path(args.output_dir).resolve()
root.mkdir(parents=True,exist_ok=True)
source=root/'stability-SF3D-TyTo172-REAL_UNREVIEWED_NO_RELEASE.glb'
expected='c4637faf90b3308123342517b43aabc4b3b197cec8aa62ad80976f173cbe20be'
assert hashlib.sha256(source.read_bytes()).hexdigest()==expected,'Run317 source SHA mismatch'
scene=trimesh.load(source,force='scene')
base=scene.dump(concatenate=True)
colors=base.visual.to_color().vertex_colors.astype(float)
verts=base.vertices.copy();faces=base.faces.copy();normals=base.face_normals.copy()
tri=verts[faces]; tri_area=trimesh.triangles.area(tri)

def fiber_mesh(n_fibers,seed):
    R=np.random.default_rng(seed)
    W=tri_area.copy();centers=tri.mean(axis=1); z=centers[:,2];y=centers[:,1]
    W*=((y>-.31)&(y<.39)); W*=~((z<-.11)&(y>.07))
    W*=np.where(z>-.07,2.2,.55);W*=np.where(y>.24,.55,1.)
    W=W/W.sum()
    ff=R.choice(len(faces),n_fibers,p=W)
    r1=np.sqrt(R.random(n_fibers));r2=R.random(n_fibers)
    b=np.stack([1-r1,r1*(1-r2),r1*r2],axis=1)
    P=(tri[ff]*b[:,:,None]).sum(axis=1)
    N=normals[ff]
    up=np.array([0.,1.,0.])
    D=up-N*(N@up)[:,None];D/=np.maximum(np.linalg.norm(D,axis=1,keepdims=True),1e-6)
    side=np.cross(N,D);side/=np.maximum(np.linalg.norm(side,axis=1,keepdims=True),1e-6)
    angle=R.normal(0,.4,n_fibers)
    D=D*np.cos(angle)[:,None]+side*np.sin(angle)[:,None]
    Side=np.cross(N,D);Side/=np.maximum(np.linalg.norm(Side,axis=1,keepdims=True),1e-6)
    length=R.uniform(.008,.029,n_fibers)
    length*=np.where(P[:,1]>.21,.64,1.)
    length*=np.where((P[:,2]<-.17)&(P[:,1]<0),.55,1.)
    width=R.uniform(.00034,.00095,n_fibers)
    q0=P+N*.00065
    q1=P+D*(length*.48)[:,None]+N*(length*.08)[:,None]
    q2=P+D*length[:,None]+N*(length*.17)[:,None]+Side*(length*R.normal(0,.05,n_fibers))[:,None]
    L=np.stack([q0-Side*width[:,None],q0+Side*width[:,None],
                q1-Side*(width*.55)[:,None],q1+Side*(width*.55)[:,None],
                q2-Side*(width*.07)[:,None],q2+Side*(width*.07)[:,None]],axis=1).reshape(-1,3)
    ix=np.arange(n_fibers)*6
    fs=np.stack([ix,ix+1,ix+2,ix+1,ix+3,ix+2,ix+2,ix+3,ix+4,ix+3,ix+5,ix+4],axis=1).reshape(-1,3)
    base_rgba=(colors[faces[ff]]*b[:,:,None]).sum(axis=1)
    creamy=np.array([244.,230.,210.])
    shade=base_rgba[:,:3]*.40+creamy*.60
    shade=np.clip(shade*R.uniform(.95,1.06,(n_fibers,1)),0,255)
    cols=np.concatenate([shade,np.full((n_fibers,1),255.)],axis=1).astype(np.uint8)
    vertexcols=np.repeat(cols[:,None,:],6,axis=1)
    vertexcols[:,2:4,:3]=np.clip(vertexcols[:,2:4,:3].astype(float)*1.016,0,255).astype(np.uint8)
    vertexcols[:,4:6,:3]=np.clip(vertexcols[:,4:6,:3].astype(float)*1.03,0,255).astype(np.uint8)
    return trimesh.Trimesh(vertices=L,faces=fs,vertex_colors=vertexcols.reshape(-1,4),process=False)

def vtkmesh(mesh,rgb):
    p=vtk.vtkPolyData();pts=vtk.vtkPoints()
    pts.SetData(numpy_to_vtk(np.asarray(mesh.vertices,dtype=np.float32),deep=True));p.SetPoints(pts)
    ff=np.hstack([np.full((len(mesh.faces),1),3,dtype=np.int64),mesh.faces.astype(np.int64)]).ravel()
    cs=vtk.vtkCellArray();cs.SetCells(len(mesh.faces),numpy_to_vtkIdTypeArray(ff,deep=True));p.SetPolys(cs)
    ca=numpy_to_vtk(rgb[:,:3].astype(np.uint8),deep=True,array_type=vtk.VTK_UNSIGNED_CHAR)
    ca.SetName('RGB');ca.SetNumberOfComponents(3);p.GetPointData().SetScalars(ca)
    normal=vtk.vtkPolyDataNormals();normal.SetInputData(p);normal.SetFeatureAngle(70)
    normal.SplittingOff();normal.ConsistencyOn();normal.AutoOrientNormalsOff()
    normal.ComputePointNormalsOn();normal.Update()
    mapper=vtk.vtkPolyDataMapper();mapper.SetInputConnection(normal.GetOutputPort())
    mapper.ScalarVisibilityOn();mapper.SetColorModeToDirectScalars()
    actor=vtk.vtkActor();actor.SetMapper(mapper)
    actor.GetProperty().SetAmbient(.50);actor.GetProperty().SetDiffuse(.50)
    actor.GetProperty().SetSpecular(.03);actor.GetProperty().SetInterpolationToPhong()
    return actor

def render(view,fiber,outfile):
    ren=vtk.vtkRenderer();ren.SetBackground(.92,.90,.86)
    ren.AddActor(vtkmesh(base,colors.astype(np.uint8)))
    if fiber is not None:
        ac=vtkmesh(fiber,np.asarray(fiber.visual.vertex_colors))
        ac.GetProperty().SetAmbient(.70);ac.GetProperty().SetDiffuse(.30)
        ac.GetProperty().SetSpecular(0);ac.GetProperty().BackfaceCullingOff()
        ren.AddActor(ac)
    w=vtk.vtkRenderWindow();w.SetOffScreenRendering(1)
    w.AddRenderer(ren);w.SetSize(540,650);w.SetMultiSamples(4)
    cam=ren.GetActiveCamera();cam.SetFocalPoint(0,.015,0);cam.SetViewUp(0,1,0)
    positions={'front':(0,.09,-2.1),'right':(2.1,.09,0),'back':(0,.09,2.1)}
    cam.SetPosition(*positions[view]);cam.SetViewAngle(34);ren.ResetCameraClippingRange()
    light=vtk.vtkLight();light.SetLightTypeToSceneLight();light.SetPosition(-1,2,-2)
    light.SetFocalPoint(0,0,0);light.SetIntensity(1.1);ren.AddLight(light)
    light2=vtk.vtkLight();light2.SetPosition(1.7,1,2)
    light2.SetFocalPoint(0,0,0);light2.SetIntensity(.8);ren.AddLight(light2)
    w.Render();win=vtk.vtkWindowToImageFilter();win.SetInput(w);win.Update()
    png=vtk.vtkPNGWriter();png.SetFileName(str(outfile))
    png.SetInputConnection(win.GetOutputPort());png.Write();w.Finalize()

results={}
for k,count in [('A',2600),('B',8300)]:
    hair=fiber_mesh(count,320172+count)
    s=trimesh.Scene();s.add_geometry(base,geom_name='original_native_textured_SF3D')
    s.add_geometry(hair,geom_name=f'physical_mesoptile_microfibres_{k}')
    path=root/f'run320-{k}-microgroom-ART_REJECTED_NO_RELEASE.glb'
    blob=trimesh.exchange.gltf.export_glb(s,include_normals=True)
    path.write_bytes(blob)
    s2=trimesh.load(path,force='scene')
    for v in ['front','right','back']:render(v,hair,root/f'run320-{k}-{v}.png')
    results[k]={'fibers':count,
                'face_total':sum(len(g.faces) for g in s2.geometry.values()),
                'bytes':path.stat().st_size,'sha256':hashlib.sha256(blob).hexdigest()}
for v in ['front','right','back']:render(v,None,root/f'run320-baseline-{v}.png')
results['baseline']={'source_sha256':expected}
(root/'run320-metrics.json').write_text(json.dumps(results,indent=2))
can=Image.new('RGB',(765,965),'#f0ede7');d=ImageDraw.Draw(can)
for i,k in enumerate(['baseline','A','B']):
    for j,v in enumerate(['front','right','back']):
        img=Image.open(root/f'run320-{k}-{v}.png').convert('RGB').resize((255,310))
        can.paste(img,(j*255,i*320+25))
        d.text((j*255+5,i*320+7),f'{k} / {v}',fill='#242424')
can.save(root/'run320-actual-ab-montage.jpg',quality=93)
(root/'NO_RELEASE.txt').write_text('NATIVE_3D_VERIFIED / VTK_SIX_VIEW / ART_REJECTED / PHYSICAL_PHONE_UNTESTED / NO_RELEASE\n')
print(json.dumps(results,indent=2))
