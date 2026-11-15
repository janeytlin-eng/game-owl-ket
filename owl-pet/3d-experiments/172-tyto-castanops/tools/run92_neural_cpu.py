#!/usr/bin/env python3
"""Run92 independent CPU neural 3D reconstruction experiment, never a released pet.

Use ONLY the repository #172 v3 concept's rightmost cream mesoptile.
One reference view cannot certify authentic side/back anatomy. No payment.
Three explicit phases: prepare / infer / audit. All outputs are ART_UNREVIEWED
until four-view manual aesthetic assessment; default is ART_REJECTED.
"""
import argparse, hashlib, json, os, pathlib, struct, sys, time
import numpy as np
from PIL import Image

parser=argparse.ArgumentParser()
parser.add_argument("phase",choices=["prepare","infer","audit"])
parser.add_argument("--source",default="owl-pet/design/concepts/172-tyto-castanops-v3.png")
parser.add_argument("--out",default="qa92")
parser.add_argument("--resolution",type=int,default=112)
args=parser.parse_args()
out=pathlib.Path(args.out); out.mkdir(parents=True,exist_ok=True)

def digest(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()

def status(**kwargs):
    p=out/"run92_status.json"
    d=json.loads(p.read_text()) if p.exists() else {}
    d.update(kwargs)
    p.write_text(json.dumps(d,indent=2,ensure_ascii=False))

def prepare():
    from rembg import remove,new_session
    source=pathlib.Path(args.source)
    if not source.is_file(): raise RuntimeError("Original #172 v3 concept image not checked out")
    orig=Image.open(source).convert("RGB")
    assert orig.size==(1536,1024),f"Expected exact #172 v3 plate got {orig.size}"
    # Previous independently audited Run90 registered rightmost owl roughly x972..1410, y285..800.
    # Keep only target region; labels and unrelated adult birds excluded as far as possible.
    crop_box=(970,260,1435,836)
    bird=orig.crop(crop_box)
    bird.save(out/"owl172_right_original_crop.png")
    # Small free CPU ONNX model; segmentation quality is not assumed sufficient.
    session=new_session("u2netp")
    rgba=remove(bird,session=session).convert("RGBA")
    a=np.asarray(rgba.getchannel("A"))
    active=a>100
    coverage=float(active.mean())
    yy,xx=np.nonzero(active)
    if len(xx)<600 or coverage<0.03 or coverage>0.97:
        raise RuntimeError(f"Foreground segmentation implausible: pixels {len(xx)}, coverage {coverage}")
    xmin,xmax=int(xx.min()),int(xx.max());ymin,ymax=int(yy.min()),int(yy.max())
    bound=[xmin,ymin,xmax+1,ymax+1]
    padded=rgba.crop(bound)
    side=max(padded.size)
    s=int(side*1.23)
    canvas=Image.new("RGBA",(s,s),(127,127,127,255))
    # Actual alpha compositing; output RGB has neutral grey without background image.
    x=(s-padded.width)//2;y=(s-padded.height)//2
    canvas.alpha_composite(padded,(x,y))
    rgb=canvas.convert("RGB").resize((512,512),Image.Resampling.LANCZOS)
    rgba.save(out/"owl172_segmented_debug.png")
    rgb.save(out/"owl172_neural_input.png")
    status(phase="prepared",reference_sha256=digest(source),
           crop_box_plate_xyxy=list(crop_box),mask_bbox_crop_xyxy=bound,
           mask_active_coverage=coverage,source_size=list(orig.size),
           neural_input_sha256=digest(out/"owl172_neural_input.png"),
           input_only_rightmost_age_unknown_mesoptile=True,
           single_view_side_back_artificially_inferred=True,
           segmentation_manual_approval=False,art_approved=False)
    print("PREPARED_SOURCE_RIGHTMOST_ONLY",json.dumps({"coverage":coverage,"bbox":bound,"input":str(out/"owl172_neural_input.png")}))

def patch_matte_pbr(path):
    """Repair glTF default-metal problem for every vertex-color mesh.
    Preserve COLOR_0, vertices, faces and BIN bytes. See prior Run91B audit.
    """
    raw=path.read_bytes()
    magic,version,total=struct.unpack_from("<4sII",raw,0)
    assert magic==b"glTF" and version==2 and total==len(raw)
    offset=12; chunks=[]
    while offset<len(raw):
        n,t=struct.unpack_from("<I4s",raw,offset)
        blob=raw[offset+8:offset+8+n]
        assert len(blob)==n
        chunks.append((t,blob));offset+=8+n
    assert chunks[0][0]==b"JSON"
    gltf=json.loads(chunks[0][1].decode("utf-8").rstrip(" \t\n\r\x00"))
    materials=gltf.setdefault("materials",[])
    index=len(materials)
    materials.append({"name":"run92_nonmetallic_cream_neural_vertex_COLOR_0",
                      "pbrMetallicRoughness":{"baseColorFactor":[1,1,1,1],
                                             "metallicFactor":0.0,"roughnessFactor":0.95},
                      "doubleSided":True})
    count=0;color=0
    for mesh in gltf.get("meshes",[]):
        for prim in mesh.get("primitives",[]):
            if "COLOR_0" in prim.get("attributes",{}):
                color+=1
                prim["material"]=index;count+=1
    if color==0:
        # Treat untextured mesh as gray diagnostic only; not an artistic pass.
        for mesh in gltf.get("meshes",[]):
            for prim in mesh.get("primitives",[]): prim["material"]=index;count+=1
    j=json.dumps(gltf,separators=(",",":")).encode()
    j+=b" "*((-len(j))%4)
    chunks[0]=(b"JSON",j)
    whole=b"".join(struct.pack("<I4s",len(b),t)+b for t,b in chunks)
    whole=struct.pack("<4sII",b"glTF",2,len(whole)+12)+whole
    path.write_bytes(whole)
    return {"pbr_material_injected":count,"colored_primitives":color,
            "metallic_factor":0.0,"roughness":0.95}

def infer():
    os.environ["HF_HUB_DISABLE_TELEMETRY"]="1"
    os.environ["TOKENIZERS_PARALLELISM"]="false"
    import torch, trimesh
    from tsr.system import TSR
    torch.set_num_threads(2)
    start=time.time()
    ip=out/"owl172_neural_input.png"
    if not ip.exists(): raise RuntimeError("Run92 source preprocessing must finish first")
    device="cpu"
    model=TSR.from_pretrained("stabilityai/TripoSR",config_name="config.yaml",weight_name="model.ckpt")
    model.renderer.set_chunk_size(2048)
    model.to(device); model.eval()
    with torch.no_grad():
        codes=model([Image.open(ip).convert("RGB")],device=device)
        meshes=model.extract_mesh(codes,True,resolution=args.resolution)
    mesh=meshes[0]
    assert isinstance(mesh,trimesh.Trimesh)
    assert len(mesh.faces)>500 and np.isfinite(mesh.vertices).all()
    output=out/"owl172_run92_neural_SINGLEVIEW_ART_UNREVIEWED.glb"
    mesh.export(output)
    fix=patch_matte_pbr(output)
    loaded=trimesh.load(output,force="scene",process=False)
    tris=sum(len(g.faces) for g in loaded.geometry.values() if isinstance(g,trimesh.Trimesh))
    summary={"phase":"inferred_not_approved",
      "source":"official open source VAST-AI-Research/TripoSR weights stabilityai/TripoSR",
      "cpu":True,"resolution":args.resolution,"vertices":len(mesh.vertices),
      "triangles":int(len(mesh.faces)),"reimport_triangles":tris,
      "watertight":bool(mesh.is_watertight),
      "euler_number":int(mesh.euler_number),
      "glb_bytes":output.stat().st_size,"glb_sha256":digest(output),
      "seconds":round(time.time()-start,2),"pbr":fix,
      "glb_file":output.name,
      "original_source":"exact #172 rightmost v3 plate cropped and separately foreground-segmented",
      "side_back_are_ai_inferred_not_reference_verified":True,
      "natural_down_fur_not_implemented":True,
      "real_phone_gpu_not_tested":True,"art_approved":False}
    assert tris==len(mesh.faces),f"Reimport triangle mismatch {tris}!={len(mesh.faces)}"
    (out/"metrics.json").write_text(json.dumps(summary,indent=2))
    status(**summary)
    print("REAL_NEURAL_CPU_MESH_GLTF_EXPORT_AND_REIMPORT",json.dumps(summary))

def audit():
    import trimesh
    p=out/"metrics.json"
    if not p.exists():
        print("NO_MODEL_GENERATED; see pipeline logs and input debug");return
    d=json.loads(p.read_text());f=out/d["glb_file"]
    assert f.exists() and digest(f)==d["glb_sha256"]
    geo=trimesh.load(f,force="scene",process=False)
    assert sum(len(g.faces) for g in geo.geometry.values() if isinstance(g,trimesh.Trimesh))==d["triangles"]
    raw=f.read_bytes()
    jlen,typ=struct.unpack_from("<I4s",raw,12)
    assert typ==b"JSON"
    j=json.loads(raw[20:20+jlen])
    prims=[p for mesh in j["meshes"] for p in mesh["primitives"]]
    for p in prims:
        mat=j["materials"][p["material"]]
        assert mat["pbrMetallicRoughness"]["metallicFactor"]==0.0
    print("REAL_GLTF_REIMPORT_SHA256_NONMETAL_PBR_VERIFIED_WITHOUT_ART_APPROVAL")
    status(phase="binary_checked_not_art_approved",glb_reimport_audit=True)

if args.phase=="prepare":prepare()
elif args.phase=="infer":infer()
else:audit()
