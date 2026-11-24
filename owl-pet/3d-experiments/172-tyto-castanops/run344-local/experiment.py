from pathlib import Path
import hashlib,json
import numpy as np
import trimesh,vtk
from scipy.sparse import coo_matrix,diags
from vtk.util.numpy_support import numpy_to_vtk,numpy_to_vtkIdTypeArray
from PIL import Image,ImageDraw
P=Path(__file__).parent
src=P/'REAL_TRIPOSR_JUVENILE_UNREVIEWED_NO_RELEASE.glb'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
raw=trimesh.load(src,force='mesh',process=False)
parts=raw.split(only_watertight=False); base=max(parts,key=lambda m:len(m.faces))
# Actual Run281 +X camera is face; head lies toward +Z. Correct semantic orientation.
base.vertices=base.vertices[:,[1,2,0]]
base.vertices-=np.array([0,base.bounds[0,1],0]);v0=base.vertices.copy(); f=base.faces.copy();c0=base.visual.vertex_colors.copy()
edges=base.edges_unique; r=np.r_[edges[:,0],edges[:,1]]; c=np.r_[edges[:,1],edges[:,0]]
A=coo_matrix((np.ones(len(r)),(r,c)),shape=(len(v0),len(v0))).tocsr(); A=diags(1/np.maximum(np.asarray(A.sum(1)).ravel(),1))@A
smoothstep=lambda t:np.clip(t,0,1)**2*(3-2*np.clip(t,0,1))
# Preserve front face detail; attenuate smoothing and palette change at front half.
z=(v0[:,2]-v0[:,2].min())/np.ptp(v0[:,2]); w=1-smoothstep((z-.40)/.35)
report={'source_sha256':sha(src),'source_triangles':len(raw.faces),'components':len(parts),'main_triangles':len(f),'orientation':'new x=old y,new y=old z,new z=old x; head +Y face +Z','variants':{}}
def render(mesh,name):
    vv=np.asarray(mesh.vertices);ff=np.asarray(mesh.faces); pts=vtk.vtkPoints();pts.SetData(numpy_to_vtk(vv,deep=True));polys=vtk.vtkCellArray();polys.SetCells(len(ff),numpy_to_vtkIdTypeArray(np.c_[np.full(len(ff),3),ff].astype(np.int64).ravel(),deep=True));pd=vtk.vtkPolyData();pd.SetPoints(pts);pd.SetPolys(polys);colors=numpy_to_vtk(np.asarray(mesh.visual.vertex_colors[:,:3],dtype=np.uint8),deep=True,array_type=vtk.VTK_UNSIGNED_CHAR);pd.GetPointData().SetScalars(colors);norm=vtk.vtkPolyDataNormals();norm.SetInputData(pd);norm.SplittingOff();norm.ConsistencyOn();norm.ComputePointNormalsOn();norm.Update();mapper=vtk.vtkPolyDataMapper();mapper.SetInputConnection(norm.GetOutputPort());mapper.SetColorModeToDirectScalars();actor=vtk.vtkActor();actor.SetMapper(mapper);actor.GetProperty().SetInterpolationToPhong();actor.GetProperty().SetAmbient(.60);actor.GetProperty().SetDiffuse(.42);actor.GetProperty().SetSpecular(.025)
    ren=vtk.vtkRenderer();ren.SetBackground(.91,.89,.85);ren.AddActor(actor);rw=vtk.vtkRenderWindow();rw.SetOffScreenRendering(1);rw.SetSize(380,380);rw.AddRenderer(ren);center=(mesh.bounds[0]+mesh.bounds[1])/2;cam=ren.GetActiveCamera();cam.ParallelProjectionOn();cam.SetParallelScale(.65);cam.SetFocalPoint(*center);cam.SetViewUp(0,1,0)
    images=[]
    for angle in [0,45,90,135,180,270]:
        a=np.deg2rad(angle);cam.SetPosition(*(center+3*np.array([np.sin(a),.03,np.cos(a)])));ren.ResetCameraClippingRange();rw.Render();w2i=vtk.vtkWindowToImageFilter();w2i.SetInput(rw);w2i.Update();fn=P/f'{name}_{angle}.png';wr=vtk.vtkPNGWriter();wr.SetFileName(str(fn));wr.SetInputConnection(w2i.GetOutputPort());wr.Write();images.append(fn)
    rw.Finalize();return images
rows=[]
for name,nit,palette in [('A_oriented',0,0),('B_fair',10,.65),('C_fair_cream',24,.90)]:
    v=v0.copy(); col=c0[:,:3].astype(float)
    for _ in range(nit):
        strength=(.35+.65*w)[:,None];v+=.48*strength*(A@v-v);v-=.50*strength*(A@v-v)
    # Correct only unobserved rear pigment; retain face and front reference. No fabricated observed rear texture.
    if palette:
        low=col.copy()
        for _ in range(8):low=.55*low+.45*(A@low)
        col=col*(1-.45*w[:,None])+low*(.45*w[:,None]); lum=col@np.array([.2126,.7152,.0722]); shade=np.clip((lum-80)*.34,-25,25)
        target=np.array([205,189,169])+shade[:,None]; ww=(palette*w)[:,None];col=col*(1-ww)+target*ww
    m=trimesh.Trimesh(vertices=v,faces=f,vertex_colors=np.c_[np.clip(col,0,255).astype(np.uint8),np.full(len(v),255)],process=False);out=P/f'{name}_NO_RELEASE.glb';m.export(out);again=trimesh.load(out,force='mesh',process=False);assert len(again.faces)==len(f);rows.append(render(again,name));report['variants'][name]={'bytes':out.stat().st_size,'sha256':sha(out),'triangles':len(again.faces),'vertices':len(again.vertices),'extents':again.extents.tolist(),'max_displacement':float(np.linalg.norm(v-v0,axis=1).max()),'reimport':True}
mont=Image.new('RGB',(6*320,3*340),(245,241,235));d=ImageDraw.Draw(mont)
for i,row in enumerate(rows):
    for j,p in enumerate(row):
        im=Image.open(p).convert('RGB').resize((320,320));mont.paste(im,(j*320,i*340));d.text((j*320+8,i*340+320),p.stem,fill=(50,40,30))
mont.save(P/'comparison.jpg',quality=88);report['views']=18;report['montage_sha256']=sha(P/'comparison.jpg');(P/'report.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
