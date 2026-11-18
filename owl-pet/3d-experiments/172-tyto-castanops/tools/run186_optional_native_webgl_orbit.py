#!/usr/bin/env python3
"""Native GLB load into Three.js with seven axis/oblique WebGL2 screenshots.
Software GPU/phone-size viewport only; NEVER equals physical mobile acceptance.
"""
import contextlib, hashlib, http.server, json, os, pathlib, shutil, socketserver, threading
from playwright.sync_api import sync_playwright
R=pathlib.Path(__file__).resolve().parent.parent
O=R/"research-evidence-run186-DOM-EXACT-SUBMIT-NO_RELEASE"
VIEW=R/"tools/run178_viewer.html"
SRC=pathlib.Path(os.environ.get("THREE_DIR","/tmp/run186-three/node_modules/three"))
VIEWS=[("axis_pos_z",0,.25,1),("axis_neg_z",0,.25,-1),
 ("axis_pos_x",1,.25,0),("axis_neg_x",-1,.25,0),
 ("axis_pos_y",0,1,.1),("axis_neg_y",0,-1,.1),
 ("oblique",1,.5,1)]
class Silent(http.server.SimpleHTTPRequestHandler):
 def __init__(self,*a,**kw):super().__init__(*a,directory=str(work),**kw)
 def log_message(self,*args):pass
results={}
models=list(O.glob("*_new_UI_generated_UNREVIEWED.glb"))
for g in models:
 b=g.read_bytes()
 if b[:4]!=b"glTF":continue
 model_name=g.name.replace("_new_UI_generated_UNREVIEWED.glb","")
 work=O/("temp_browser_"+model_name)
 work.mkdir(exist_ok=True)
 (work/"vendor").mkdir(exist_ok=True)
 symlink=work/"vendor/three"
 if not symlink.exists():symlink.symlink_to(SRC, target_is_directory=True)
 shutil.copy2(VIEW,work/"index.html")
 shutil.copy2(g,work/"model.glb")
 with socketserver.TCPServer(("127.0.0.1",0),Silent) as srv:
  port=srv.server_address[1]
  t=threading.Thread(target=srv.serve_forever,daemon=True);t.start()
  record={"file":g.name,"sha256":hashlib.sha256(b).hexdigest(),"views":{}}
  with sync_playwright() as pw:
   browser=pw.chromium.launch(headless=True,args=["--no-sandbox","--enable-unsafe-swiftshader",
          "--use-gl=angle","--use-angle=swiftshader"])
   context=browser.new_context(viewport={"width":390,"height":844},device_scale_factor=2)
   page=context.new_page()
   try:
    page.goto(f"http://127.0.0.1:{port}/",wait_until="load",timeout=30000)
    page.wait_for_function("window.qa && window.qa.status !== 'LOADING'",timeout=50000)
    init=page.evaluate("()=>({...window.qa, view:undefined})")
    record["loader"]=init
    if init.get("status")=="READY":
     for name,x,y,z in VIEWS:
      frames=page.evaluate("async ([x,y,z])=>await window.qa.view(x,y,z)",[x,y,z])
      page.screenshot(path=str(O/(f"run186_{model_name}_{name}_UNREVIEWED.png")))
      record["views"][name]=frames
   except Exception as e:record["error"]=repr(e)
   finally:context.close();browser.close()
  results[model_name]=record
  srv.shutdown()
 (O/(f"run186_{model_name}_webgl_metrics.json")).write_text(json.dumps(record,indent=2)+"\n")
 # These are internal temp files; preserve the actual original GLB separately.
 shutil.rmtree(work,ignore_errors=True)
(O/"run186_real_native_webgl_summary.json").write_text(json.dumps(results,indent=2)+"\n")
print("RUN185_REAL_WEBGL",[(k,v.get("loader",{}).get("status"),len(v.get("views",{}))) for k,v in results.items()])
