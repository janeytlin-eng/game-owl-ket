#!/usr/bin/env python3
"""Run104 independent CPU neural 3D reconstruction experiment, never a released pet.

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
parser.add_argument("--source",default="owl-pet/3d-experiments/172-tyto-castanops/research-evidence-run103-TRELLIS2-PBR-ART_UNAPPROVED/preprocessed_image.png")
parser.add_argument("--out",default="qa104")
parser.add_argument("--resolution",type=int,default=112)
args=parser.parse_args()
out=pathlib.Path(args.out); out.mkdir(parents=True,exist_ok=True)

def digest(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()

def status(**kwargs):
    p=out/"run104_status.json"
    d=json.loads(p.read_text()) if p.exists() else {}
    d.update(kwargs)
    p.write_text(json.dumps(d,indent=2,ensure_ascii=False))

def prepare():
    """Use genuinely foreground-isolated official Gradio result from completed Run103.
    This is a different independent CPU reconstruction input, not a 2D release asset.
    Source has black background. We convert to neutral-grey alpha-softened background
    and add breathing room around actual photographed fluff; no painted fake wings.
    """
    source=pathlib.Path(args.source)
    if not source.is_file():raise RuntimeError("Run103 verified foreground is missing")
    image=Image.open(source).convert("RGB")
    original=np.asarray(image,dtype=np.float32)
    # Black pixels were produced by zero-cost background isolation, not owl plumage.
    brightness=np.max(original,axis=2)
    foreground=np.clip((brightness-5.0)/35.0,0,1)
    foreground=foreground*foreground*(3-2*foreground)
    coverage=float((foreground>0.5).mean())
    if coverage<0.08 or coverage>0.85:raise RuntimeError(f"Invalid owl cutout coverage: {coverage}")
    neutral=np.ones_like(original)*127.0
    comp=(original*foreground[:,:,None]+neutral*(1-foreground[:,:,None]))
    comp=np.uint8(np.clip(comp,0,255))
    prepared=Image.fromarray(comp,"RGB")
    pad=int(max(prepared.size)*0.09)
    square=Image.new("RGB",(max(prepared.size)+2*pad,max(prepared.size)+2*pad),(127,127,127))
    offset=((square.width-prepared.width)//2,(square.height-prepared.height)//2)
    square.paste(prepared,offset)
    inp=square.resize((512,512),Image.Resampling.LANCZOS)
    inp.save(out/"owl172_neural_input.png")
    image.save(out/"owl172_source_foreground_from_trellis2_preprocess.png")
    status(phase="prepared_clean_foreground_reconstruction",
        source_sha256=digest(source),source_size=list(image.size),
        mask_brightness_coverage=coverage,neural_input_sha256=digest(out/"owl172_neural_input.png"),
        original_rightmost_reference_not_changed=True,source_preprocessed_in_run103=True,
        input_has_neutral_gray_background=True,source_license="original concept plate project asset",
        no_extra_paid_tool=True,art_approved=False)
    print("RUN104_REAL_SOURCE_SEGMENTED",json.dumps({"coverage":coverage,"input":str(out/"owl172_neural_input.png")}))

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
    materials.append({"name":"run104_nonmetallic_cream_neural_vertex_COLOR_0",
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
    if not ip.exists(): raise RuntimeError("Run104 source preprocessing must finish first")
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
    output=out/"owl172_run104_neural_SINGLEVIEW_ART_UNREVIEWED.glb"
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
