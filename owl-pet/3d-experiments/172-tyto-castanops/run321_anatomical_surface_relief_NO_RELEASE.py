"""#172 Run321. Research-only mesh-integrated scapular/wing relief A/B.
Real Run317 UV-textured GLB is required. The deformation operates on existing
native mesh vertices; this does not paste spheres, billboards, SVGs or primitives.
Art verdict must be separately inspected. Never deploy automatically.
"""
import argparse,hashlib,json
from pathlib import Path
import numpy as np
import trimesh
import vtk
from vtk.util.numpy_support import numpy_to_vtk,numpy_to_vtkIdTypeArray
from PIL import Image,ImageDraw
EXPECTED='c4637faf90b3308123342517b43aabc4b3b197cec8aa62ad80976f173cbe20be'

def sculpt(original,strength):
    out=original.copy()
    V=out.vertices.copy()
    x,y,z=V[:,0],V[:,1],V[:,2]
    lateral=np.exp(-((np.abs(x)-.212)/.084)**2)
    vertical=np.exp(-((y+.025)/.187)**4)
    dorsal=1/(1+np.exp(np.clip(-35*(z+.005),-40,40)))
    field=lateral*vertical*dorsal
    V[:,0]+=np.sign(x)*strength*.052*field
    V[:,2]+=strength*.021*field
    for cx in [.108,.166,.212]:
        scap=np.exp(-((np.abs(x)-cx)/(.026+cx*.06))**2)
        upper=np.exp(-((y-.018)/.175)**4)
        surface=1/(1+np.exp(np.clip(-43*(z-.104),-40,40)))
        ripple=(.45+.55*np.cos((y+.18)*25.0+cx*36)**2)
        V[:,2]+=strength*(.0085 if cx<.2 else .006)*scap*upper*surface*ripple
    torso=np.exp(-((y+.105)/.205)**4)*(1/(1+np.exp(np.clip(-43*(z+.075),-40,40))))
    V[:,0]+=strength*np.sign(x)*.008*torso
    out.vertices=V
    return out

def actor(mesh):
    p=vtk.vtkPolyData();pts=vtk.vtkPoints()
    pts.SetData(numpy_to_vtk(np.asarray(mesh.vertices,dtype=np.float32),deep=True));p.SetPoints(pts)
    ff=np.hstack([np.full((len(mesh.faces),1),3,dtype=np.int64),mesh.faces.astype(np.int64)]).ravel()
    cs=vtk.vtkCellArray();cs.SetCells(len(mesh.faces),numpy_to_vtkIdTypeArray(ff,deep=True));p.SetPolys(cs)
    rgb=np.asarray(mesh.visual.to_color().vertex_colors[:,:3],dtype=np.uint8)
    a=numpy_to_vtk(rgb,deep=True,array_type=vtk.VTK_UNSIGNED_CHAR)
    a.SetName('RGB');a.SetNumberOfComponents(3);p.GetPointData().SetScalars(a)
    n=vtk.vtkPolyDataNormals();n.SetInputData(p);n.ComputePointNormalsOn();n.SplittingOff();n.Update()
    m=vtk.vtkPolyDataMapper();m.SetInputConnection(n.GetOutputPort());m.SetColorModeToDirectScalars()
    act=vtk.vtkActor();act.SetMapper(m);act.GetProperty().SetAmbient(.54)
    act.GetProperty().SetDiffuse(.46);act.GetProperty().SetSpecular(.015)
    return act

def render(mesh,angle,path):
    ren=vtk.vtkRenderer();ren.SetBackground(.94,.92,.88);ren.AddActor(actor(mesh))
    win=vtk.vtkRenderWindow();win.AddRenderer(ren);win.SetSize(550,640)
    win.SetMultiSamples(2);win.SetOffScreenRendering(1)
    cam=ren.GetActiveCamera();cam.SetFocalPoint(0,.015,0);cam.SetViewUp(0,1,0)
    rad=np.deg2rad(angle);cam.SetPosition(2.15*np.sin(rad),.08,-2.15*np.cos(rad))
    cam.SetViewAngle(34);ren.ResetCameraClippingRange()
    for pos,intensity in [((-1.5,2,-1),1.0),((1.8,1.4,1.8),.68)]:
        l=vtk.vtkLight();l.SetLightTypeToSceneLight();l.SetPosition(*pos)
        l.SetFocalPoint(0,.015,0);l.SetIntensity(intensity);ren.AddLight(l)
    win.Render()
    p=vtk.vtkWindowToImageFilter();p.SetInput(win);p.Update()
    writer=vtk.vtkPNGWriter();writer.SetInputConnection(p.GetOutputPort())
    writer.SetFileName(str(path));writer.Write();win.Finalize()

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',required=True)
    ap.add_argument('--out',required=True);args=ap.parse_args()
    root=Path(args.out);root.mkdir(parents=True,exist_ok=True)
    original=Path(args.input);sha=hashlib.sha256(original.read_bytes()).hexdigest()
    assert sha==EXPECTED,sha
    scene=trimesh.load(original,force='scene');assert len(scene.geometry)==1
    mesh=next(iter(scene.geometry.values()))
    report={'source_sha256':sha,'source_triangles':len(mesh.faces),
            'source_bounds':mesh.bounds.tolist(),'variants':{}}
    for label,strength in [('baseline',0.),('A',.55),('B',1.)]:
        m=mesh.copy() if strength==0 else sculpt(mesh,strength)
        displacement=np.linalg.norm(m.vertices-mesh.vertices,axis=1)
        stats={'max_vertex_displacement_m':float(displacement.max()),
               'p95_vertex_displacement_m':float(np.quantile(displacement,.95)),
               'mean_vertex_displacement_m':float(displacement.mean())}
        if label!='baseline':
            p=root/f'run321-{label}-integrated-sculpt-ART_UNREVIEWED_NO_RELEASE.glb'
            s=trimesh.Scene();s.add_geometry(m);raw=s.export(file_type='glb')
            p.write_bytes(raw);re=trimesh.load(p,force='scene')
            result=next(iter(re.geometry.values()))
            assert len(result.faces)==len(mesh.faces)
            assert np.allclose(result.vertices,m.vertices,atol=1e-6)
            stats.update({'glb_bytes':len(raw),'glb_sha256':hashlib.sha256(raw).hexdigest(),
                          'triangles':len(result.faces),'geometry_count':len(re.geometry)})
        for angle,name in [(0,'front'),(90,'right'),(135,'rear_oblique'),(180,'back')]:
            render(m,angle,root/f'run321-{label}-{name}.png')
        report['variants'][label]=stats
    board=Image.new('RGB',(1100,1050),'#ece9e3');d=ImageDraw.Draw(board)
    for i,label in enumerate(['baseline','A','B']):
        for j,name in enumerate(['front','right','rear_oblique','back']):
            im=Image.open(root/f'run321-{label}-{name}.png').convert('RGB')
            board.paste(im.resize((275,320)),(275*j,350*i+20))
            d.text((275*j+10,350*i+5),label+' / '+name,fill='black')
    board.save(root/'run321-sculpt-montage.jpg',quality=90)
    (root/'run321-geometry-report.json').write_text(json.dumps(report,indent=2))
    (root/'STRICT_NO_RELEASE.txt').write_text(
        'REAL 3D mesh relief experiment only. ART_REJECTED / rights hold / physical phone untested / NO_RELEASE.\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
