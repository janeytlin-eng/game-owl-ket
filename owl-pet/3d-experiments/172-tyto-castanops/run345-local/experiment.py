from pathlib import Path
import hashlib,json
import numpy as np, trimesh, vtk
from scipy.sparse import coo_matrix,diags
from scipy.ndimage import map_coordinates,gaussian_filter,distance_transform_edt
from vtk.util.numpy_support import numpy_to_vtk,numpy_to_vtkIdTypeArray
from PIL import Image,ImageDraw
P=Path(__file__).parent
src=P/'REAL_TRIPOSR_JUVENILE_UNREVIEWED_NO_RELEASE.glb'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
raw=trimesh.load(src,force='mesh',process=False); base=max(raw.split(only_watertight=False),key=lambda m:len(m.faces)); base.vertices=base.vertices[:,[1,2,0]]
v0=base.vertices.copy(); f=base.faces.copy(); c0=base.visual.vertex_colors[:,:3].astype(float); edges=base.edges_unique
r=np.r_[edges[:,0],edges[:,1]]; c=np.r_[edges[:,1],edges[:,0]]; A=coo_matrix((np.ones(len(r)),(r,c)),shape=(len(v0),len(v0))).tocsr(); A=diags(1/np.maximum(np.asarray(A.sum(1)).ravel(),1))@A
ss=lambda t:np.clip(t,0,1)**2*(3-2*np.clip(t,0,1)); z=(v0[:,2]-v0[:,2].min())/np.ptp(v0[:,2]); rear=1-ss((z-.37)/.45)
# Preserve silhouette broadly; strong low-pass geometry diagnostic instead of adding fur geometry.
v=v0.copy()
for _ in range(60):v+=.42*(A@v-v)
# Restore bounding extents to avoid global shrink. Source correspondence is approximate.
v=(v-v.min(0))/np.ptp(v,axis=0)*np.ptp(v0,axis=0)+v0.min(0)
img=np.asarray(Image.open(P/'juvenile_rightmost_masked_512_RESEARCH.png').convert('RGBA')); rgb=img[:,:,:3].astype(float); alpha=img[:,:,3]; mask=alpha>128
if mask.mean()>.95: mask=np.max(abs(rgb-128),axis=2)>8
# Ignore disconnected debris via largest component.
from scipy.ndimage import label
lab,n=label(mask); counts=np.bincount(lab.ravel()); counts[0]=0; mask=lab==counts.argmax(); yy,xx=np.where(mask); print('mask',xx.min(),xx.max(),yy.min(),yy.max(),mask.mean())
# Extend foreground color to outside edge to prevent grey halo.
idx=distance_transform_edt(~mask,return_distances=False,return_indices=True); rgb=rgb[idx[0],idx[1]]
uvx=(v0[:,0]-v0[:,0].min())/np.ptp(v0[:,0])*(xx.max()-xx.min())+xx.min(); uvy=(1-(v0[:,1]-v0[:,1].min())/np.ptp(v0[:,1]))*(yy.max()-yy.min())+yy.min()
project=np.stack([map_coordinates(rgb[:,:,i],[uvy,uvx],order=1,mode='nearest') for i in range(3)],1)
# Design-only side/rear palette; geometry normals reduce projection across tangent surfaces.
mesh=trimesh.Trimesh(vertices=v,faces=f,process=False); nz=mesh.vertex_normals[:,2]; front=ss((nz-.08)/.65)*ss((z-.34)/.45); low=c0.copy()
for _ in range(24):low+=.45*(A@low-low)
shade=np.clip((low@np.array([.2126,.7152,.0722])-100)*.22,-17,17); target=np.array([219,202,179])+shade[:,None]; col=low*(1-rear[:,None])+target*rear[:,None]
# A/B same geometry; B projection only. C slight high-frequency albedo from actual source down crop, not geometry.
patch=rgb[270:345,130:205]; hi=patch-gaussian_filter(patch,(4,4,0)); rng=np.random.default_rng(345); noise=hi[rng.integers(0,75,len(v)),rng.integers(0,75,len(v))]; noise=(noise+A@noise)*.5
report={'source_sha256':sha(src),'source_triangles':len(raw.faces),'main_triangles':len(f),'source_mask_bbox':[int(xx.min()),int(yy.min()),int(xx.max()),int(yy.max())],'max_geometry_displacement':float(np.linalg.norm(v-v0,axis=1).max()),'variants':{}}
def render(mesh,name):
    vv=np.asarray(mesh.vertices); ff=np.asarray(mesh.faces); pts=vtk.vtkPoints();pts.SetData(numpy_to_vtk(vv,deep=True)); polys=vtk.vtkCellArray();polys.SetCells(len(ff),numpy_to_vtkIdTypeArray(np.c_[np.full(len(ff),3),ff].astype(np.int64).ravel(),deep=True));pd=vtk.vtkPolyData();pd.SetPoints(pts);pd.SetPolys(polys);pd.GetPointData().SetScalars(numpy_to_vtk(np.asarray(mesh.visual.vertex_colors[:,:3],dtype=np.uint8),deep=True,array_type=vtk.VTK_UNSIGNED_CHAR));norm=vtk.vtkPolyDataNormals();norm.SetInputData(pd);norm.SplittingOff();norm.ConsistencyOn();norm.ComputePointNormalsOn();norm.Update();mapper=vtk.vtkPolyDataMapper();mapper.SetInputConnection(norm.GetOutputPort());mapper.SetColorModeToDirectScalars();actor=vtk.vtkActor();actor.SetMapper(mapper);actor.GetProperty().SetInterpolationToPhong();actor.GetProperty().SetAmbient(.68);actor.GetProperty().SetDiffuse(.35);actor.GetProperty().SetSpecular(.01)
    ren=vtk.vtkRenderer();ren.SetBackground(.92,.90,.86);ren.AddActor(actor);rw=vtk.vtkRenderWindow();rw.SetOffScreenRendering(1);rw.SetSize(350,350);rw.AddRenderer(ren);center=mesh.bounds.mean(0);cam=ren.GetActiveCamera();cam.ParallelProjectionOn();cam.SetParallelScale(.64);cam.SetFocalPoint(*center);cam.SetViewUp(0,1,0);images=[]
    for angle in [0,45,90,180]:
        a=np.deg2rad(angle);cam.SetPosition(*(center+3*np.array([np.sin(a),.02,np.cos(a)])));ren.ResetCameraClippingRange();rw.Render();w2i=vtk.vtkWindowToImageFilter();w2i.SetInput(rw);w2i.Update();fn=P/f'{name}_{angle}.png';wr=vtk.vtkPNGWriter();wr.SetFileName(str(fn));wr.SetInputConnection(w2i.GetOutputPort());wr.Write();images.append(fn)
    rw.Finalize();return images
rows=[]
b=col*(1-front[:,None])+project*front[:,None]
for name,colors in [('A_lowpass',col),('B_projection',b),('C_down_albedo',b+noise*.65*(1-front[:,None]))]:
    m=trimesh.Trimesh(vertices=v,faces=f,vertex_colors=np.c_[np.clip(colors,0,255).astype(np.uint8),np.full(len(v),255)],process=False); out=P/f'{name}_NO_RELEASE.glb';m.export(out); again=trimesh.load(out,force='mesh',process=False);assert len(again.faces)==len(f);rows.append(render(again,name));report['variants'][name]={'bytes':out.stat().st_size,'sha256':sha(out),'triangles':len(again.faces),'extents':again.extents.tolist()}
mont=Image.new('RGB',(4*300,3*318),(245,241,235));d=ImageDraw.Draw(mont)
for i,row in enumerate(rows):
    for j,p in enumerate(row):mont.paste(Image.open(p).convert('RGB').resize((300,300)),(j*300,i*318));d.text((j*300+4,i*318+300),p.stem,fill=(50,40,30))
mont.save(P/'comparison.jpg',quality=88);report['views']=12;report['montage_sha256']=sha(P/'comparison.jpg');(P/'report.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
