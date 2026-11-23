import numpy as np, trimesh, vtk, hashlib, json, io
from PIL import Image, ImageDraw, ImageFilter
from vtk.util.numpy_support import numpy_to_vtk, vtk_to_numpy
from pathlib import Path
rng=np.random.default_rng(332)
# Four distinct soft branched down clumps, padded atlas, original procedural art.
S=256; atlas=Image.new('RGBA',(S*2,S*2));
for k in range(4):
 im=Image.new('RGBA',(S,S)); d=ImageDraw.Draw(im)
 for j in range(65):
  root=np.array([128+rng.normal(0,12),238+rng.normal(0,4)])
  tip=np.array([np.clip(128+rng.normal(0,55),15,241),rng.uniform(12,130)])
  ctrl=(root+tip)/2+np.array([rng.normal(0,25),0]); t=np.linspace(0,1,22)[:,None]; path=(1-t)**2*root+2*t*(1-t)*ctrl+t*t*tip
  c=int(rng.integers(219,255)); col=(c,c-8,c-22,int(rng.integers(150,245)))
  d.line([tuple(q) for q in path],fill=col,width=int(rng.integers(2,5)))
  for u in (.33,.55,.72):
   a=path[int(u*21)]; b=a+np.array([rng.choice([-1,1])*rng.uniform(8,26),-rng.uniform(9,30)]); d.line([tuple(a),tuple(b)],fill=col,width=1)
 im=im.filter(ImageFilter.GaussianBlur(.65)); atlas.paste(im,((k%2)*S,(k//2)*S))
# Retain actual curved backing; dense warm cream microtexture reduces bare spots.
def z(x,y):return .005*(1-(x*x+y*y)/.00125)
a=np.linspace(-.025,.025,30); x,y=np.meshgrid(a,a); v=np.c_[x.ravel(),y.ravel(),z(x,y).ravel()]; f=[]
for j in range(29):
 for i in range(29):
  k=j*30+i; f.extend([[k,k+1,k+30],[k+1,k+31,k+30]])
base=trimesh.Trimesh(v,f,process=False); base.visual.vertex_colors=[233,219,193,255]
def make(normal):
 r=np.random.default_rng(99); v=[]; f=[]; uv=[]
 for j in range(22):
  for i in range(22):
   x,y=np.array([i,j])*.05/22-.025+r.uniform(0,.05/22,2); p=np.array([x,y,z(x,y)]); n=np.array([.008*x/.001,.008*y/.001,1.]) if normal else np.array([0.,0.,1.]); n/=np.linalg.norm(n)
   a=r.uniform(0,2*np.pi); u=np.array([np.cos(a),np.sin(a),0]); u-=n*np.dot(n,u); u/=np.linalg.norm(u); w=np.cross(n,u); L=r.uniform(.0035,.0055); W=r.uniform(.0038,.0055); lean=r.uniform(.8,1.5); k=len(v); tile=int(r.integers(0,4))
   for t in np.linspace(0,1,5):
    c=p+w*L*lean*t*t+n*L*t; width=W*(.7+.65*np.sin(np.pi*t))
    for sign in [-1,1]:v.append(c+u*sign*width/2); uv.append([(tile%2+(sign+1)/2)/2,(1-tile//2+t)/2])
   for q in range(4):
    m=k+q*2; f.extend([[m,m+1,m+2],[m+1,m+3,m+2]])
 mat=trimesh.visual.material.PBRMaterial(baseColorTexture=atlas,roughnessFactor=1.,metallicFactor=0.,doubleSided=True,alphaMode='MASK',alphaCutoff=.4)
 return trimesh.Trimesh(v,f,process=False,visual=trimesh.visual.texture.TextureVisuals(uv=uv,material=mat))
def actor(mesh, tex=None, cutoff=None):
 poly=vtk.vtkPolyData(); pts=vtk.vtkPoints(); pts.SetData(numpy_to_vtk(np.asarray(mesh.vertices),deep=True)); poly.SetPoints(pts); cells=vtk.vtkCellArray()
 for tri in mesh.faces:cells.InsertNextCell(3); [cells.InsertCellPoint(int(t)) for t in tri]
 poly.SetPolys(cells); mp=vtk.vtkPolyDataMapper();mp.SetInputData(poly); ac=vtk.vtkActor();ac.SetMapper(mp); pr=ac.GetProperty();pr.SetColor(.91,.85,.75);pr.SetAmbient(.55);pr.SetDiffuse(.45);pr.SetSpecular(0)
 if tex is not None:
  tc=numpy_to_vtk(mesh.visual.uv,deep=True);poly.GetPointData().SetTCoords(tc); im=vtk.vtkImageData();im.SetDimensions(512,512,1); a=np.asarray(tex)[::-1].copy();
  if cutoff is not None:a[:,:,3]=np.where(a[:,:,3]>=cutoff,255,0)
  im.GetPointData().SetScalars(numpy_to_vtk(a.reshape(-1,4),deep=True,array_type=vtk.VTK_UNSIGNED_CHAR));tx=vtk.vtkTexture();tx.SetInputData(im);tx.InterpolateOn();ac.SetTexture(tx);pr.SetColor(1,1,1);pr.SetAmbient(.7);pr.SetDiffuse(.3)
 return ac
report=[]; montage=Image.new('RGB',(1200,800))
for row,(name,normal) in enumerate([('atlas-vertical',False),('atlas-normal',True)]):
 cards=make(normal);path=Path(name+'.glb');path.write_bytes(trimesh.Scene([base,cards]).export(file_type='glb'));loaded=trimesh.load(path,force='scene');assert len(loaded.geometry)==2
 report.append(dict(name=name,triangles=sum(len(g.faces) for g in loaded.geometry.values()),bytes=path.stat().st_size,sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
 ren=vtk.vtkRenderer();ren.SetBackground(.20,.22,.24);ren.AddActor(actor(base));ren.AddActor(actor(cards,atlas,102));ren.SetUseDepthPeeling(True);ren.SetMaximumNumberOfPeels(100);win=vtk.vtkRenderWindow();win.SetOffScreenRendering(1);win.SetAlphaBitPlanes(1);win.SetMultiSamples(0);win.SetSize(400,400);win.AddRenderer(ren)
 for col,pos in enumerate([(0,0,.12),(.08,-.08,.065),(.10,0,.025)]):
  cam=ren.GetActiveCamera();cam.SetPosition(*pos);cam.SetFocalPoint(0,0,.003);cam.SetViewUp(0,1,0);cam.ParallelProjectionOn();cam.SetParallelScale(.041);ren.ResetCameraClippingRange();win.Render();g=vtk.vtkWindowToImageFilter();g.SetInput(win);g.Update();a=vtk_to_numpy(g.GetOutput().GetPointData().GetScalars()).reshape(400,400,-1)[::-1];im=Image.fromarray(a[:,:,:3].copy());im.save(f'{name}-{col}.png');montage.paste(im,(col*400,row*400))
 win.Finalize()
montage.save('comparison.jpg',quality=90);atlas.save('atlas.png');Path('report.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
