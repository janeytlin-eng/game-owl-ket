import numpy as np, trimesh, vtk, hashlib, json
from PIL import Image, ImageDraw
from vtk.util.numpy_support import numpy_to_vtk, vtk_to_numpy
from pathlib import Path
rng=np.random.default_rng(331)
# Shared curved cards: each is a real 3D ribbon, not a camera-facing sprite.
S=256; tex=Image.new('RGBA',(S,S),(235,218,189,0)); d=ImageDraw.Draw(tex)
for i in range(180):
    root=rng.normal(128,14); tip=np.clip(root+rng.normal(0,48),8,248); top=rng.integers(6,145); col=int(rng.integers(215,251))
    d.line([(root,254),(root+rng.normal(0,8),180),(tip,top)],fill=(col,col-11,col-30,int(rng.integers(145,256))),width=int(rng.integers(1,4)))
# Backing curve has a dome rise of 5 mm.
def z(x,y): return .005*(1-(x*x+y*y)/.00125)
a=np.linspace(-.025,.025,30); xx,yy=np.meshgrid(a,a); vv=np.c_[xx.ravel(),yy.ravel(),z(xx,yy).ravel()]; ff=[]
for j in range(29):
 for i in range(29):
  k=j*30+i; ff.extend([[k,k+1,k+30],[k+1,k+31,k+30]])
base=trimesh.Trimesh(vv,ff,process=False); base.visual.vertex_colors=[212,191,155,255]
v=[]; f=[]; uv=[]
for j in range(22):
 for i in range(22):
  x,y=np.array([i,j])*.05/22-.025+rng.uniform(0,.05/22,2); p=np.array([x,y,z(x,y)]); angle=rng.uniform(0,2*np.pi); u=np.array([np.cos(angle),np.sin(angle),0]); w=np.array([-u[1],u[0],0]); L=rng.uniform(.004,.009); W=rng.uniform(.0018,.0033); lean=rng.uniform(.15,.85); k=len(v)
  for t in np.linspace(0,1,5):
   c=p+w*L*lean*t*t+np.array([0,0,L*t]); width=W*(1-.35*t)
   for sign in [-1,1]: v.append(c+u*sign*width/2); uv.append([(sign+1)/2,t])
  for q in range(4):
   m=k+q*2; f.extend([[m,m+1,m+2],[m+1,m+3,m+2]])
v=np.array(v); f=np.array(f); uv=np.array(uv)
def actor(mesh, texture=None):
 poly=vtk.vtkPolyData(); pts=vtk.vtkPoints(); pts.SetData(numpy_to_vtk(np.asarray(mesh.vertices),deep=True)); poly.SetPoints(pts); cells=vtk.vtkCellArray()
 for tri in mesh.faces: cells.InsertNextCell(3); [cells.InsertCellPoint(int(t)) for t in tri]
 poly.SetPolys(cells); mp=vtk.vtkPolyDataMapper(); mp.SetInputData(poly); ac=vtk.vtkActor(); ac.SetMapper(mp); prop=ac.GetProperty(); prop.SetColor(.85,.76,.62); prop.SetAmbient(.35); prop.SetDiffuse(.65); prop.SetSpecular(0)
 if texture is not None:
  tc=numpy_to_vtk(uv,deep=True); tc.SetName('UV'); poly.GetPointData().SetTCoords(tc); im=vtk.vtkImageData(); im.SetDimensions(S,S,1); arr=numpy_to_vtk(np.asarray(texture)[::-1].reshape(-1,4).copy(),deep=True,array_type=vtk.VTK_UNSIGNED_CHAR); im.GetPointData().SetScalars(arr); tx=vtk.vtkTexture(); tx.SetInputData(im); tx.InterpolateOn(); ac.SetTexture(tx); prop.SetColor(1,1,1); prop.SetAmbient(.6); prop.SetDiffuse(.4)
 return ac
report=[]; montage=Image.new('RGB',(1200,800))
for row,(name,texture) in enumerate([('opaque',tex.copy()),('alpha',tex)]):
 if name=='opaque': texture.putalpha(255)
 mat=trimesh.visual.material.PBRMaterial(baseColorTexture=texture,roughnessFactor=1.0,metallicFactor=0.0,doubleSided=True,alphaMode='MASK' if name=='alpha' else 'OPAQUE',alphaCutoff=.4)
 cards=trimesh.Trimesh(v,f,process=False,visual=trimesh.visual.texture.TextureVisuals(uv=uv,material=mat)); scene=trimesh.Scene([base,cards]); path=Path(name+'.glb'); path.write_bytes(scene.export(file_type='glb')); loaded=trimesh.load(path,force='scene'); assert len(loaded.geometry)==2
 report.append(dict(name=name,triangles=sum(len(g.faces) for g in loaded.geometry.values()),bytes=path.stat().st_size,sha256=hashlib.sha256(path.read_bytes()).hexdigest(),alpha_mode=mat.alphaMode))
 ren=vtk.vtkRenderer(); ren.SetBackground(.20,.22,.24); ren.AddActor(actor(base)); ren.AddActor(actor(cards,texture)); ren.SetUseDepthPeeling(True); ren.SetMaximumNumberOfPeels(100); ren.SetOcclusionRatio(0.01); win=vtk.vtkRenderWindow(); win.SetOffScreenRendering(1); win.SetAlphaBitPlanes(1); win.SetMultiSamples(0); win.SetSize(400,400); win.AddRenderer(ren)
 for col,position in enumerate([(0,0,.12),(.08,-.08,.065),(.10,0,.025)]):
  cam=ren.GetActiveCamera(); cam.SetPosition(*position); cam.SetFocalPoint(0,0,.003); cam.SetViewUp(0,1,0); cam.ParallelProjectionOn(); cam.SetParallelScale(.041); ren.ResetCameraClippingRange(); win.Render(); grab=vtk.vtkWindowToImageFilter(); grab.SetInput(win); grab.Update(); data=vtk_to_numpy(grab.GetOutput().GetPointData().GetScalars()).reshape(400,400,-1)[::-1]; img=Image.fromarray(data[:,:,:3].copy()); img.save(f'{name}-{col}.png'); montage.paste(img,(col*400,row*400))
 win.Finalize()
montage.save('comparison.jpg',quality=90); Path('report.json').write_text(json.dumps(report,indent=2)); print(json.dumps(report,indent=2))
