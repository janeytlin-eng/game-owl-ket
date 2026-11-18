#!/usr/bin/env node
/* Run181: real Run180 cleaned-source image-conditioned GLB, offline Chromium/Three.js phone-size
 * WebGL test. No generated shapes, no model substitution, no payment, NO_RELEASE. */
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import http from "node:http";
import {fileURLToPath} from "node:url";
import {chromium} from "playwright";

const here=path.dirname(fileURLToPath(import.meta.url));
const root=path.resolve(here,"..");
const out=path.join(root,"research-evidence-run181-CLEAN-NATIVE-WEBGL-NO_RELEASE");
fs.mkdirSync(out,{recursive:true});
const sha=b=>crypto.createHash("sha256").update(b).digest("hex");
const SOURCE="https://three.ws/cdn/forge/anon/2b5c60a2-4b7a-4f70-af17-ba3b95d23341.glb";
const HASH="809e2110faec1301072c99f08a3caf440e9fd30692c7dd8c5e80bf109b9f8c48";
const REF="5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9";
const refFile=path.join(root,"research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED","rightmost_mesoptile_input.png");
const rejected=path.join(root,"known_rejected_asset_sha256_registry.json");
const cleanRefFile=path.join(root,"research-evidence-run180-CLEAN-BG-NEW-NEURAL-NO_RELEASE","run180_rightmost_contiguous_background_replaced.png");
const CLEAN_REF_SHA="8f47899ba4fced01ffe92b3b8b6615884a62f4880528219aff57aef9b3622145";
const report={run:181,kind:"real image-conditioned neural GLB newly generated in Run180",source:SOURCE,
 expected_sha256:HASH,art:"UNREVIEWED",mobile_physical_device:"NOT_TESTED",
 browser:"NOT_STARTED",release:false,additional_payments_usd:0};
const save=()=>fs.writeFileSync(path.join(out,"run181_metrics.json"),JSON.stringify(report,null,2));
let browser,server;
try{
 const required=[refFile,cleanRefFile,rejected,path.resolve(root,"../../AGENTS.md"),
  path.resolve(root,"../../README.md"),path.resolve(root,"../../prototype/index.html"),
  path.resolve(root,"../../research/species/172-tyto-castanops-v3.md")];
 for(const f of required)if(!fs.existsSync(f))throw Error("MISSING_PREFLIGHT "+f);
 const referenceSha=sha(fs.readFileSync(refFile));
 if(referenceSha!==REF)throw Error("REFERENCE_SHA_MISMATCH "+referenceSha);
 if(JSON.stringify(JSON.parse(fs.readFileSync(rejected,"utf8"))).includes(HASH))throw Error("REJECTED_ASSET_SHA");
 const cleanSha=sha(fs.readFileSync(cleanRefFile));
 if(cleanSha!==CLEAN_REF_SHA)throw Error("RUN180_CLEAN_REFERENCE_SHA_MISMATCH "+cleanSha);
 report.reference_sha256=referenceSha;report.cleaned_source_sha256=cleanSha;
 report.preflight="PASS";save();
 const response=await fetch(SOURCE,{signal:AbortSignal.timeout(120000)});
 report.download_status=response.status;
 if(!response.ok)throw Error("GLB_DOWNLOAD_HTTP_"+response.status);
 const data=Buffer.from(await response.arrayBuffer());
 const actual=sha(data);report.glb={bytes:data.length,sha256:actual};
 if(actual!==HASH || data.subarray(0,4).toString()!=="glTF")throw Error("GLB_CHANGED_OR_INVALID");
 if(data.length>32000000)throw Error("GLB_OVERSIZE");
 if(data.length<65536)throw Error("GLB_UNDER_64K_NOT_TRUSTED");
 fs.writeFileSync(path.join(out,"candidate_original_UNREVIEWED.glb"),data);
 save();
 const threeRoot=path.resolve(process.cwd(),"node_modules/three");
 if(!fs.existsSync(threeRoot))throw Error("NPM_THREE_MISSING");
 const html=fs.readFileSync(path.join(here,"run178_viewer.html"),"utf8");
 const send=(res,body,type="application/octet-stream")=>{
  res.writeHead(200,{"Content-Type":type,"Access-Control-Allow-Origin":"*","Cache-Control":"no-store"});res.end(body);};
 server=http.createServer((req,res)=>{
  const uri=decodeURIComponent((req.url||"/").split("?")[0]);
  if(uri==="/"||uri==="/index.html")return send(res,html,"text/html");
  if(uri==="/model.glb")return send(res,data,"model/gltf-binary");
  if(uri.startsWith("/vendor/three/")){
   const name=uri.slice("/vendor/three/".length);
   if(name.includes("..")){res.writeHead(403);return res.end();}
   const file=path.join(threeRoot,name);
   if(fs.existsSync(file)&&fs.statSync(file).isFile())return send(res,fs.readFileSync(file),
    ".js"===path.extname(file)?"application/javascript":"application/octet-stream");
  }
  res.writeHead(404);res.end("missing");
 });
 await new Promise(ok=>server.listen(0,"127.0.0.1",ok));
 const port=server.address().port,errors=[];
 browser=await chromium.launch({headless:true,args:["--enable-webgl","--use-angle=swiftshader",
  "--enable-unsafe-swiftshader","--no-sandbox","--disable-dev-shm-usage"]});
 const context=await browser.newContext({viewport:{width:390,height:844},
  deviceScaleFactor:2,isMobile:true,hasTouch:true});
 const page=await context.newPage();
 page.on("pageerror",x=>errors.push(String(x)));
 page.on("console",x=>{if(x.type()==="error")errors.push("console: "+x.text())});
 await page.goto("http://127.0.0.1:"+port,{waitUntil:"domcontentloaded",timeout:60000});
 await page.waitForFunction('window.qa && window.qa.status !== "LOADING"',null,{timeout:90000});
 const status=await page.evaluate(()=>{const {view,...m}=window.qa;return m});
 report.browser=status;report.page_errors=errors;save();
 if(status.status!=="READY")throw Error("BROWSER_GLTF_NOT_READY "+JSON.stringify(status));
 if(status.geometry_triangles<1000||status.mesh_count<1)throw Error("NO_REAL_GLTF_MESH");
 const views=[
  ["axis_posZ",0,.1,1],["axis_oblique",.65,.2,1],
  ["axis_posX",1,.1,0],["axis_negZ",0,.1,-1],
  ["axis_negX",-1,.1,0],["axis_posY",.1,1,.12],["axis_negY",.1,-1,.12]
 ];
 report.rendered=[];
 for(const [name,x,y,z] of views){
  const stats=await page.evaluate(async v=>await window.qa.view(...v),[x,y,z]);
  if(stats.context_lost||stats.triangles_drawn<1000)
   throw Error("WEBGL_DRAW_FAILURE "+name+" "+JSON.stringify(stats));
  const filename="run181_"+name+"_MOBILE_EMULATED_UNREVIEWED.png";
  await page.locator("canvas").screenshot({path:path.join(out,filename)});
  if(fs.statSync(path.join(out,filename)).size<3000)
   throw Error("BLANK_WEBGL_CAPTURE_"+name);
  report.rendered.push({name,filename,...stats});save();
 }
 report.status="CHROMIUM_SOFTWARE_WEBGL_SEVEN_VIEWS_RENDERED_NO_RELEASE";
 report.art="UNREVIEWED";report.mobile_physical_device="NOT_TESTED";
}catch(e){report.status="RUN181_EXECUTION_ERROR";report.exception=String(e);
 report.stack=String(e?.stack||"").slice(0,6000);}
finally{
 if(browser)await browser.close().catch(()=>{});
 if(server)await new Promise(resolve=>server.close(resolve));
 fs.writeFileSync(path.join(out,"NO_RELEASE.flag"),
  "NO_RELEASE: no art approval, software WebGL only, no actual mobile GPU, no extra payment.\n");
 save();
 const manifest={};
 for(const f of fs.readdirSync(out)){
  if(f==="run181_sha256_manifest.json")continue;
  const v=fs.readFileSync(path.join(out,f));manifest[f]={bytes:v.length,sha256:sha(v)};
 }
 fs.writeFileSync(path.join(out,"run181_sha256_manifest.json"),JSON.stringify(manifest,null,2));
 console.log("RUN181_FINAL",report.status,"real_3d_axis_images",report.rendered?.length||0,
  "sha_count",Object.keys(manifest).length);
 if(report.status!=="CHROMIUM_SOFTWARE_WEBGL_SEVEN_VIEWS_RENDERED_NO_RELEASE")
  process.exitCode=4;
}