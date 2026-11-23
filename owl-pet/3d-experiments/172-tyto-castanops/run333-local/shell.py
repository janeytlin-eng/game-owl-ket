import numpy as np, trimesh, vtk, json, hashlib
from PIL import Image
from scipy.ndimage import gaussian_filter
from vtk.util.numpy_support import numpy_to_vtk,vtk_to_numpy
from pathlib import Path
# Closed curved swatch; fixed base, texture and shell offsets, no full chick claim.
r=np.random.default_rng(333); S=256
noise=lambda s: gaussian_filter(r.random((S,S)),s,mode='wrap')
def norm(a):return (a-a.min())/(a.max()-a.min())
clump=norm(noise(7)); micro=norm(noise(.65)); roots=norm(noise(.85)); length=.25+.75*norm(.7*roots+.3*clump)
basecol=np.stack([208+35*clump+9*micro,188+39*clump+10*micro,158+45*clump+12*micro],-1)
N=49; M=73; theta,phi=np.meshgrid(np.linspace(.001,np.pi-.001,N),np.linspace(0,2*np.pi,M),indexing='ij'); unit=np.stack([np.sin(theta)*np.cos(phi),np.sin(theta)*np.sin(phi),np.cos(theta)],-1).reshape(-1,3)
scale=np.array([.025,.021,.018]); normals=unit/scale; normals/=np.linalg.norm(normals,axis=1)[:,None]; uv=np.c_[phi.ravel()/(2*np.pi),1-theta.ravel()/np.pi]; faces=[]
for i in range(N-1):
 for j in range(M-1):
  k=i*M+j;faces.extend([[k,k+M,k+1],[k+1,k+M,k+M+1]])
def mesh(h,tex):
 v=unit*scale+normals*h;mat=trimesh.visual.material.PBRMaterial(baseColorTexture=tex,alphaMode='MASK' if h else 'OPAQUE',alphaCutoff=.5,roughnessFactor=1.,metallicFactor=0.,doubleSided=False)
 return trimesh.Trimesh(v,faces,process=False,visual=trimesh.visual.texture.TextureVisuals(uv=uv,material=mat))
def texture(t):
 col=basecol+(np.array([250,242,224])-basecol)*t*.8
 alpha=np.full((S,S),255) if t==0 else np.where(length>t,255,0)
 return Image.fromarray(np.dstack([col,alpha]).clip(0,255).astype('uint8'))
def actor(m,tex):
 p=vtk.vtkPolyData();pts=vtk.vtkPoints();pts.SetData(numpy_to_vtk(m.vertices,deep=True));p.SetPoints(pts);c=vtk.vtkCellArray()
 for f in m.faces:c.InsertNextCell(3);[c.InsertCellPoint(int(i)) for i in f]
 p.SetPolys(c);p.GetPointData().SetTCoords(numpy_to_vtk(uv,deep=True));p.GetPointData().SetNormals(numpy_to_vtk(normals,deep=True));mp=vtk.vtkPolyDataMapper();mp.SetInputData(p);a=vtk.vtkActor();a.SetMapper(mp);a.GetProperty().BackfaceCullingOn();a.GetProperty().SetAmbient(.45);a.GetProperty().SetDiffuse(.55);a.GetProperty().SetSpecular(0)
 im=vtk.vtkImageData();im.SetDimensions(S,S,1);im.GetPointData().SetScalars(numpy_to_vtk(np.asarray(tex)[::-1].copy().reshape(-1,4),deep=True,array_type=vtk.VTK_UNSIGNED_CHAR));tx=vtk.vtkTexture();tx.SetInputData(im);tx.InterpolateOn();a.SetTexture(tx);return a
report=[]; montage=Image.new('RGB',(1080,720))
for row,(name,levels) in enumerate([('A-baked',[0]),('B-shell',[0,.18,.34,.50,.66,.82])]):
 textures=[texture(t) for t in levels]; meshes=[mesh(t*.004,tex) for t,tex in zip(levels,textures)];p=Path(name+'.glb');p.write_bytes(trimesh.Scene(meshes).export(file_type='glb'));l=trimesh.load(p,force='scene');assert len(l.geometry)==len(levels)
 report.append(dict(name=name,triangles=sum(len(m.faces) for m in l.geometry.values()),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
 ren=vtk.vtkRenderer();ren.SetBackground(.19,.22,.24);ren.SetUseDepthPeeling(True);ren.SetMaximumNumberOfPeels(30);win=vtk.vtkRenderWindow();win.SetOffScreenRendering(1);win.SetAlphaBitPlanes(1);win.SetMultiSamples(0);win.SetSize(360,360);win.AddRenderer(ren)
 for m,t in zip(meshes,textures):ren.AddActor(actor(m,t))
 for col,pos in enumerate([(0,0,.12),(.08,-.08,.065),(.12,0,.015)]):
  cam=ren.GetActiveCamera();cam.SetPosition(*pos);cam.SetFocalPoint(0,0,0);cam.SetViewUp(0,1,0);cam.ParallelProjectionOn();cam.SetParallelScale(.036);ren.ResetCameraClippingRange();win.Render();g=vtk.vtkWindowToImageFilter();g.SetInput(win);g.Update();a=vtk_to_numpy(g.GetOutput().GetPointData().GetScalars()).reshape(360,360,-1)[::-1];im=Image.fromarray(a[:,:,:3].copy());im.save(f'{name}-{col}.png');montage.paste(im,(col*360,row*360))
 win.Finalize()
montage.save('comparison.jpg',quality=90);Path('report.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
