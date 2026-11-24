from pathlib import Path
import hashlib,json
import numpy as np, trimesh, vtk
from scipy.sparse import coo_matrix,diags
from vtk.util.numpy_support import numpy_to_vtk,numpy_to_vtkIdTypeArray
from PIL import Image,ImageDraw
P=Path(__file__).parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
src=P/'REAL_TRIPOSR_JUVENILE_UNREVIEWED_NO_RELEASE.glb'
raw=trimesh.load(src,force='mesh',process=False); base=max(raw.split(only_watertight=False),key=lambda m:len(m.faces));base.vertices=base.vertices[:,[1,2,0]]
v=base.vertices.copy();f=base.faces.copy();c=base.visual.vertex_colors[:,:3].astype(float)
u=(v-v.min(0))/np.ptp(v,axis=0);x,y,z=u.T
s=lambda t:np.clip(t,0,1)**2*(3-2*np.clip(t,0,1))
e=base.edges_unique;i=np.r_[e[:,0],e[:,1]];j=np.r_[e[:,1],e[:,0]]
# Anatomical regions are deliberately approximate; preserve the learned geometry there, not a painted replacement.
face=s((y-.47)/.17)*s((.98-y)/.14)*s((z-.5)/.24)*s((.48-abs(x-.5))/.15)
feet=1-s((y-.08)/.16); keep=np.maximum(face,feet)
A=coo_matrix((np.ones(len(i)),(i,j)),shape=(len(v),len(v))).tocsr();A=diags(1/np.maximum(np.asarray(A.sum(1)).ravel(),1))@A
# Fixed bilateral color weights reduce smoothing across learned eyes, bill and feather boundaries.
dc=np.linalg.norm(c[i]-c[j],axis=1);w=.08+.92*np.exp(-(dc/30)**2)
B=coo_matrix((w,(i,j)),shape=A.shape).tocsr();B=diags(1/np.maximum(np.asarray(B.sum(1)).ravel(),1e-8))@B
low=c.copy()
for _ in range(15):low+=.4*(A@low-low)
rear=1-s((z-.35)/.45);shade=np.clip((low.mean(1)-100)*.25,-20,20);cream=np.array([219,202,179])+shade[:,None];colors=low*(1-rear[:,None])+cream*rear[:,None];colors=colors*(1-keep[:,None])+c*keep[:,None]
def render(m,name):
    vv=np.asarray(m.vertices);ff=np.asarray(m.faces);pts=vtk.vtkPoints();pts.SetData(numpy_to_vtk(vv,deep=True));polys=vtk.vtkCellArray();polys.SetCells(len(ff),numpy_to_vtkIdTypeArray(np.c_[np.full(len(ff),3),ff].astype(np.int64).ravel(),deep=True));pd=vtk.vtkPolyData();pd.SetPoints(pts);pd.SetPolys(polys);pd.GetPointData().SetScalars(numpy_to_vtk(np.asarray(m.visual.vertex_colors[:,:3],dtype=np.uint8),deep=True,array_type=vtk.VTK_UNSIGNED_CHAR));norm=vtk.vtkPolyDataNormals();norm.SetInputData(pd);norm.SplittingOff();norm.ConsistencyOn();norm.Update();mapper=vtk.vtkPolyDataMapper();mapper.SetInputConnection(norm.GetOutputPort());mapper.SetColorModeToDirectScalars();actor=vtk.vtkActor();actor.SetMapper(mapper);actor.GetProperty().SetInterpolationToPhong();actor.GetProperty().SetAmbient(.65);actor.GetProperty().SetDiffuse(.4);actor.GetProperty().SetSpecular(.02)
    ren=vtk.vtkRenderer();ren.SetBackground(.92,.90,.86);ren.AddActor(actor);rw=vtk.vtkRenderWindow();rw.SetOffScreenRendering(1);rw.SetSize(350,350);rw.AddRenderer(ren);center=m.bounds.mean(0);cam=ren.GetActiveCamera();cam.ParallelProjectionOn();cam.SetParallelScale(.64);cam.SetFocalPoint(*center);cam.SetViewUp(0,1,0);out=[]
    for angle in [0,45,90,180]:
        a=np.deg2rad(angle);cam.SetPosition(*(center+3*np.array([np.sin(a),.02,np.cos(a)])));ren.ResetCameraClippingRange();rw.Render();im=vtk.vtkWindowToImageFilter();im.SetInput(rw);im.Update();p=P/f'{name}_{angle}.png';wr=vtk.vtkPNGWriter();wr.SetFileName(str(p));wr.SetInputConnection(im.GetOutputPort());wr.Write();out.append(p)
    rw.Finalize();return out
report={'source_sha256':sha(src),'source_triangles':len(raw.faces),'main_triangles':len(f),'variants':{}};rows=[]
for name,op,k in [('A_uniform',A,np.zeros(len(v))),('B_region',A,keep),('C_bilateral_region',B,keep)]:
    vv=v.copy();rate=(.42*(1-.88*k))[:,None]
    for _ in range(60):vv+=rate*(op@vv-vv)
    # Measure displacement without rescaling protected facial landmarks.
    m=trimesh.Trimesh(vertices=vv,faces=f,vertex_colors=np.c_[np.clip(colors,0,255).astype(np.uint8),np.full(len(v),255)],process=False);p=P/f'{name}_NO_RELEASE.glb';m.export(p);m2=trimesh.load(p,force='mesh',process=False);assert len(m2.faces)==len(f);rows.append(render(m2,name));d=np.linalg.norm(vv-v,axis=1);report['variants'][name]={'bytes':p.stat().st_size,'sha256':sha(p),'triangles':len(m2.faces),'face_displacement_mean':float(d[face>.8].mean()),'feet_displacement_mean':float(d[feet>.8].mean()),'body_displacement_mean':float(d[keep<.1].mean()),'max_displacement':float(d.max())}
mont=Image.new('RGB',(1200,954),(245,241,235));draw=ImageDraw.Draw(mont)
for i,row in enumerate(rows):
    for j,p in enumerate(row):mont.paste(Image.open(p).convert('RGB').resize((300,300)),(j*300,i*318));draw.text((j*300+4,i*318+300),p.stem,fill=(50,40,30))
mont.save(P/'comparison.jpg',quality=88);report['views']=12;report['montage_sha256']=sha(P/'comparison.jpg');(P/'report.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
