import numpy as np, trimesh, vtk, hashlib, json
from scipy.spatial import cKDTree
from vtk.util.numpy_support import numpy_to_vtk, numpy_to_vtkIdTypeArray
from PIL import Image, ImageDraw
from pathlib import Path
out=Path(__file__).parent
rng=np.random.default_rng(336)
# No UV poles: all domains sampled on the unit sphere, not latitude/longitude.
base=trimesh.creation.icosphere(subdivisions=6); v=base.vertices.copy(); f=base.faces.copy()
centers=trimesh.creation.icosphere(subdivisions=3).vertices.copy(); centers+=rng.normal(0,.022,centers.shape); centers/=np.linalg.norm(centers,axis=1)[:,None]
_,idx=cKDTree(centers).query(v,k=4)
axes=rng.normal(size=centers.shape); axes-=np.sum(axes*centers,axis=1)[:,None]*centers; axes/=np.linalg.norm(axes,axis=1)[:,None]
# Overlapping local tuft envelopes, irregular widths, no longitude seam.
delta=v[:,None,:]-centers[idx]; tangent=axes[idx]; along=np.sum(delta*tangent,axis=2); side=np.sum(delta*np.cross(centers[idx],tangent),axis=2)
amp=rng.uniform(.007,.020,len(centers))[idx]
w=np.exp(-((along-.018)/.065)**2-(side/.033)**2)
tuft=np.max(w*amp,axis=1)
# World-space coherent noise, identical for A and B.
freq=rng.normal(size=(20,3)); freq/=np.linalg.norm(freq,axis=1)[:,None]; freq*=rng.uniform(45,110,20)[:,None]; phase=rng.uniform(0,2*np.pi,20)
noise=np.sin(v@freq.T+phase).mean(axis=1)
# Solid curved volumetric surface, intentionally no claim of complete owl.
report={}; images=[]
for name,disp in [('A_isotropic',.012*noise),('B_local_tuft',.012*noise+tuft)]:
    pos=v*(1+disp[:,None])*np.array([.64,.75,.49]); col=np.clip(np.array([224,207,178])+noise[:,None]*17,0,255).astype(np.uint8)
    mesh=trimesh.Trimesh(vertices=pos,faces=f,vertex_colors=np.column_stack([col,np.full(len(v),255,np.uint8)]),process=False)
    path=out/(name+'.glb'); mesh.export(path); back=trimesh.load(path,force='mesh'); assert len(back.faces)==len(f)
    report[name]={'triangles':len(f),'vertices':len(v),'watertight':bool(back.is_watertight),'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
    pts=vtk.vtkPoints();pts.SetData(numpy_to_vtk(pos,deep=True)); cells=vtk.vtkCellArray(); cells.SetCells(len(f),numpy_to_vtkIdTypeArray(np.column_stack([np.full(len(f),3),f]).astype(np.int64).ravel(),deep=True)); pd=vtk.vtkPolyData();pd.SetPoints(pts);pd.SetPolys(cells);pd.GetPointData().SetScalars(numpy_to_vtk(col,deep=True,array_type=vtk.VTK_UNSIGNED_CHAR));norm=vtk.vtkPolyDataNormals();norm.SetInputData(pd);norm.SplittingOff();norm.ComputePointNormalsOn();norm.Update()
    mapper=vtk.vtkPolyDataMapper();mapper.SetInputConnection(norm.GetOutputPort());mapper.SetColorModeToDirectScalars();actor=vtk.vtkActor();actor.SetMapper(mapper);actor.GetProperty().SetAmbient(.35);actor.GetProperty().SetDiffuse(.65);actor.GetProperty().SetSpecular(.025)
    ren=vtk.vtkRenderer();ren.AddActor(actor);ren.SetBackground(.13,.12,.10);win=vtk.vtkRenderWindow();win.SetOffScreenRendering(1);win.SetSize(390,390);win.AddRenderer(ren)
    for i,a in enumerate([0,1.1,2.5]):
        cam=ren.GetActiveCamera();cam.SetPosition(2.8*np.sin(a),.35,2.8*np.cos(a));cam.SetFocalPoint(0,0,0);cam.SetViewUp(0,1,0);cam.ParallelProjectionOn();cam.SetParallelScale(.89);ren.ResetCameraClippingRange();win.Render();cap=vtk.vtkWindowToImageFilter();cap.SetInput(win);cap.Update();wr=vtk.vtkPNGWriter();wr.SetInputConnection(cap.GetOutputPort());p=out/f'{name}_{i}.png';wr.SetFileName(str(p));wr.Write();images.append(p)
    win.Finalize()
mont=Image.new('RGB',(1170,826),'white'); draw=ImageDraw.Draw(mont)
for i,p in enumerate(images):
    x=i%3*390;y=i//3*413;draw.text((x+10,y+4),p.stem,fill='black');mont.paste(Image.open(p),(x,y+23))
mont.save(out/'montage.jpg',quality=88);(out/'report.json').write_text(json.dumps(report,indent=2)); print(json.dumps(report,indent=2))
