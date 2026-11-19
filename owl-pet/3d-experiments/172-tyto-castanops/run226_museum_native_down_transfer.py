#!/usr/bin/env python3
"""Run226: actual free native down groom on verified CC0 museum ADULT Tyto 3D donor.
Research-only anatomy/material transfer; NEVER a juvenile character, never release.
Original museum adult has wrong age, long mature wings and an unsuitable perch.
No fee, no GPU credits, no modification to production or main.
"""
import datetime, hashlib, json, os, pathlib, select, shutil, subprocess, time, traceback
import requests

ROOT=pathlib.Path(__file__).resolve().parents[3]
EXP=ROOT/"owl-pet/3d-experiments/172-tyto-castanops"
OUT=EXP/"run226-evidence";OUT.mkdir(parents=True,exist_ok=True)
BASE=pathlib.Path(os.getenv("RUNNER_TEMP","/tmp"))/"owl172-run226-real-museum-tyto"
BASE.mkdir(parents=True,exist_ok=True)
WORK=BASE/"work";WORK.mkdir(exist_ok=True)
SRC=BASE/"groomlab"
BUILD=SRC/"build/lean-cli"
PIN="5e81163e3520e14e99f001c41c441f85a186daf9"
ID="0e65de5934db4f0eae02835ba7227dcc"
FNAME=ID+"_normalized_optimized-0.250.glb"
URL="https://zenodo.org/api/records/21379215/files/"+FNAME+"/content"
REFERENCE_SHA="881dec86e0e66ab2ad0781db86a3b719b35e710d2be1a1606d761a9d0908483d"
SOURCE_SHA="97b886248ea11483094a7290f27a97e373752f92f73f6ff585190e3d612d743a"
REPORT={"run":"226","date_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
 "target":"#172 Tyto castanops v3 rightmost age-unknown cream-down juvenile",
 "actual_donor":"CC0-claimed museum SCANNED ADULT Tyto alba (NOT juvenile, NOT castanops)",
 "source_record":"https://zenodo.org/records/21379215",
 "native_groom":"GroomLab open source feathers_down preset", "groom_pin":PIN,
 "additional_paid_usd":0,"production_changed":False,"main_changed":False,
 "release":"NO_RELEASE","art":"NOT_PASSED","real_phone_webgl":"NOT_TESTED",
 "steps":{},"mcp":[],"outputs":{},"status":"STARTED"}
def stat(p):
 p=pathlib.Path(p)
 return {"bytes":p.stat().st_size,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()}
def execute(label,args,cwd=None,timeout=200):
 t=time.monotonic();out=OUT/(label+".log");code=None;err=None
 with out.open("wb") as f:
  try:
   proc=subprocess.run(args,cwd=cwd or ROOT,stdout=f,stderr=subprocess.STDOUT,timeout=timeout)
   code=proc.returncode
  except BaseException as exc:err=repr(exc)
 tail=out.read_bytes()[-1800:].decode("utf-8","replace")
 REPORT["steps"][label]={"returncode":code,"error":err,"seconds":round(time.monotonic()-t,2),"tail":tail}
 return code==0
def rpc(p,name,arguments=None,timeout=100):
 args=arguments or {}
 index=len(REPORT["mcp"])+1
 message={"jsonrpc":"2.0","id":index,"method":"tools/call","params":{"name":name,"arguments":args}}
 t=time.monotonic()
 try:
  p.stdin.write(json.dumps(message,ensure_ascii=False)+"\n");p.stdin.flush()
  ready,_,_=select.select([p.stdout],[],[],timeout)
  if not ready:raise TimeoutError("no MCP reply "+name)
  line=p.stdout.readline()
  if not line:raise RuntimeError("MCP process ended "+str(p.poll()))
  payload=json.loads(line)
  if payload.get("id")!=index:raise RuntimeError("bad MCP request ID")
  result=payload.get("result",{})
  parsed=result.get("content",[])
  parsed=[json.loads(x["text"]) if x.get("type")=="text" else x for x in parsed]
  value=parsed[0] if parsed else {}
  if not isinstance(value,dict):value={"value":value}
  if result.get("isError") or payload.get("error"):value={"error":payload.get("error",value)}
 except BaseException as exc:value={"error":repr(exc)}
 record={"name":name,"arguments":args,"duration_s":round(time.monotonic()-t,2),"result":value}
 REPORT["mcp"].append(record)
 (OUT/("mcp_%02d_%s.json"%(index,name))).write_text(json.dumps(record,indent=2,ensure_ascii=False,default=str)+"\n")
 return value
def must(r,label):
 if not isinstance(r,dict) or "error" in r:raise RuntimeError(label+" rejected: "+str(r)[:500])
 return r
def get_real_mesh():
 import numpy as np, trimesh
 original=WORK/"museum_adult_draco_ORIGINAL_NOT_APPROVED.glb"
 r=requests.get(URL,timeout=(25,120));REPORT["download_http"]=r.status_code
 r.raise_for_status()
 original.write_bytes(r.content)
 ss=stat(original);REPORT["donor_source"]=ss
 if ss["bytes"]!=2185576 or ss["sha256"]!=SOURCE_SHA:raise ValueError("museum scan mismatch")
 decode=WORK/"museum_adult_uncompressed_ORIGINAL_NOT_APPROVED.glb"
 if not execute("draco_decode",["gltf-transform","copy",str(original),str(decode)],timeout=160):raise RuntimeError("Khronos Draco decode failed")
 data=trimesh.load(str(decode),force="scene",process=False)
 meshes=data.dump()
 if isinstance(meshes,trimesh.Trimesh):meshes=[meshes]
 meshes=[x for x in meshes if isinstance(x,trimesh.Trimesh) and len(x.faces)>50]
 if not meshes:raise RuntimeError("Zero usable native 3D")
 pts=np.vstack([g.vertices for g in meshes]);dimensions=np.ptp(pts,axis=0)
 if not np.isfinite(pts).all() or (dimensions>0.00001).sum()<3:raise RuntimeError("degenerate Draco decoded geometry")
 # Actual museum donor must remain recognizably distinct from handmade primitives.
 REPORT["native_meshes"]=[{"triangles":len(x.faces),"area":round(float(x.area),5),
        "bounds":np.round(x.bounds,5).tolist()} for x in meshes]
 REPORT["native_bound_xyz"]=np.round(dimensions,6).tolist()
 REPORT["decoded_glb"]=stat(decode)
 selected=max(meshes,key=lambda x:len(x.faces))
 if len(selected.faces)<1000:raise RuntimeError("No credible museum owl donor surface")
 # OBJ is the real scanned triangle surface, NOT a made-up proxy or remeshed sphere.
 scalp=selected.copy()
 scalp.vertices=(scalp.vertices-scalp.bounds.mean(axis=0))*100.0
 obj=WORK/"museum_adult_largest_original_scan_mesh_SCALP_ONLY.obj"
 scalp.export(obj)
 REPORT["donor_surface_faces"]=len(scalp.faces)
 REPORT["donor_surface_bound_cm"]=np.round(scalp.extents,3).tolist()
 REPORT["donor_obj_sha"]=stat(obj)
 return obj
def main():
 try:
  plate=ROOT/"owl-pet/design/concepts/172-tyto-castanops-v3.png"
  REPORT["v3_original_reference"]=stat(plate)
  if REPORT["v3_original_reference"]["sha256"]!=REFERENCE_SHA:raise RuntimeError("wrong v3 original reference")
  obj=get_real_mesh()
  REPORT["status"]="VERIFIED_REAL_MUSEUM_ADULT_SCALP_AVAILABLE"
  if not execute("clone",["git","clone","--depth","1","--branch","dev","https://github.com/thekesslereffect/groomlab.git",str(SRC)],timeout=170):raise RuntimeError("GroomLab clone failed")
  if not execute("pin",["git","checkout","--detach",PIN],cwd=SRC,timeout=40):raise RuntimeError("upstream commit pin inaccessible")
  if "Apache License" not in (SRC/"LICENSE").read_text(encoding="utf-8"):raise RuntimeError("GroomLab Apache license unverified")
  options=["-DCMAKE_BUILD_TYPE=Release","-DCMAKE_CXX_FLAGS_RELEASE=-O1 -DNDEBUG",
    "-DGROOMLAB_BUILD_TESTS=OFF","-DGROOMLAB_BUILD_PYTHON=OFF","-DGROOMLAB_BUILD_ALEMBIC=ON",
    "-DGROOMLAB_BUILD_CAPI=OFF","-DGROOMLAB_BUILD_BLENDER_HELPER=OFF",
    "-DGROOMLAB_BUILD_ARNOLD=OFF","-DGROOMLAB_BUILD_PROCEDURAL=OFF",
    "-DGROOMLAB_BUILD_RENDERMAN=OFF","-DGROOMLAB_BUILD_MAYA=OFF"]
  if not execute("cmake_configure",["cmake","-S",str(SRC),"-B",str(BUILD),"-G","Ninja"]+options,cwd=SRC,timeout=200):raise RuntimeError("CMake failed")
  if not execute("cmake_native_build",["cmake","--build",str(BUILD),"--target","groomlab-cli","--parallel","3"],cwd=SRC,timeout=1000):raise RuntimeError("Native GroomLab build failed")
  cli=BUILD/"engine/cli/groomlab-cli"
  if not cli.is_file() or not execute("cli_version",[str(cli),"--version"],cwd=SRC,timeout=30):raise RuntimeError("No live native GroomLab")
  p=subprocess.Popen([str(cli),"mcp","--root",str(WORK)],cwd=SRC,
    stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,
    text=True,encoding="utf-8",bufsize=1)
  try:
   for name,density in (("museum_adult_down_a",0.025),("museum_adult_down_b",0.065)):
    created=rpc(p,"new_groom",{"name":name,"mesh":obj.name,"preset":"feathers_down"},timeout=110)
    must(created,"new_groom "+name)
    graph=rpc(p,"get_graph",{"groom":name},timeout=35)
    REPORT[name+"_graph_available"]="error" not in graph
    result=rpc(p,"evaluate",{"groom":name,"density":density},timeout=150)
    must(result,"evaluate "+name)
    strands=result.get("strands",result.get("strandCount",0))
    REPORT[name+"_real_strands"]=strands
    if not isinstance(strands,(int,float)) or strands<=0:raise RuntimeError("No actual museum-donor down strands")
    prev=rpc(p,"render_preview",{"groom":name,
      "views":["front","side","back","three_quarter","top"],"size":1024,
      "max_strands":15000,"density":density,
      "save_to":name+"_FIVE_NATIVE_CAMERAS_ADULT_REJECTED.png"},timeout=250)
    must(prev,"render_preview "+name)
    saved=rpc(p,"save_groom",{"groom":name,"path":name+"_native_ADULT_UNAPPROVED.groom"},timeout=90)
    must(saved,"save_groom "+name)
    exported=rpc(p,"export",{"groom":name,"path":name+"_native_hair_curves_ADULT_UNAPPROVED.usda",
                  "density":density},timeout=220)
    must(exported,"export "+name)
   REPORT["status"]="REAL_MUSEUM_ADULT_TYTO_GROOM_PRODUCED_2_DENSITIES_ART_REJECTED_NO_RELEASE"
  finally:
   p.stdin.close()
   try:p.wait(timeout=15)
   except subprocess.TimeoutExpired:p.kill()
  from PIL import Image, ImageChops
  for name in ("museum_adult_down_a","museum_adult_down_b"):
   img=WORK/(name+"_FIVE_NATIVE_CAMERAS_ADULT_REJECTED.png")
   if not img.exists() or img.stat().st_size<5000:raise RuntimeError("No actual 5-camera image "+name)
   picture=Image.open(img).convert("RGB")
   ext=ImageChops.difference(picture,Image.new("RGB",picture.size,picture.getpixel((0,0)))).getbbox()
   if ext is None:raise RuntimeError("Native groom renderer returned fully uniform image "+name)
   REPORT[name+"_native_preview"]={"image_size":picture.size,"nonuniform":True}
  REPORT["status"]="TECH_NATIVE_GROOM_TRANSFER_AND_FIVEVIEWS_PASS_ADULT_ART_REJECTED_NO_RELEASE"
 except BaseException as e:
  REPORT["status"]="FAILED_OR_UNVERIFIED_NO_RELEASE";REPORT["error"]=repr(e)
  REPORT["traceback"]=traceback.format_exc()[-5000:]
 finally:
  for root in (WORK,):
   for p in root.iterdir():
    if p.is_file() and p.suffix in (".groom",".usda",".obj",".glb",".png"):
     target=OUT/p.name
     if p.suffix in (".png",".groom",".usda",".obj"):shutil.copyfile(p,target)
     REPORT["outputs"][p.name]=stat(p)
  REPORT["ended_utc"]=datetime.datetime.now(datetime.timezone.utc).isoformat()
  (OUT/"run226_report.json").write_text(json.dumps(REPORT,ensure_ascii=False,indent=2,default=str)+"\n")
  (OUT/"run226_status.md").write_text(
    "# Run226 genuine museum-adult Tyto surface / GroomLab native down transfer - NO RELEASE\n\n"
    +"Status: "+REPORT["status"]+"\n\n"
    +"True CC0-claimed adult Tyto alba scan only. **NOT** a Tyto castanops juvenile. "
    +"Even when real down curves are generated, adult anatomy, long wings/tail and perch mean ART_REJECTED. "
    +"Preview PNG are GroomLab CPU diagnostic drawings, NOT PBR and NOT WebGL. "
    +"USD groom curves are NOT portable game-ready GLB. No approved juvenile model; no mobile device verification.\n\n"
    +"Any error: "+str(REPORT.get("error","none"))+"\n")
  print(json.dumps({"status":REPORT["status"],"meshes":REPORT.get("native_meshes"),
     "donor_faces":REPORT.get("donor_surface_faces"),"strands_a":REPORT.get("museum_adult_down_a_real_strands"),
     "strands_b":REPORT.get("museum_adult_down_b_real_strands"),
     "error":REPORT.get("error"),"release":"NO_RELEASE"},ensure_ascii=False),flush=True)
if __name__=="__main__":main()
