/** #172 Run279b: actual Chromium/Three.js WebGL2 load and seven spatial cameras of
 * ORIGINAL Blender-hair-derived mobile LOD. Technical research only, art rejected.
 * Reuses Run277 correctly framed viewer but removes its animation-only invocation.
 */
import { chromium } from "playwright";
import { createServer } from "node:http";
import { readFileSync, writeFileSync, mkdirSync, statSync } from "node:fs";
import { resolve, join } from "node:path";
import { createHash } from "node:crypto";

const expected=process.env.OWL172_SHA256;
const model=resolve(process.env.OWL172_GLB_INPUT);
const dest=resolve(process.env.OWL172_BROWSER_DIR);
mkdirSync(dest,{recursive:true});
const hash=x=>createHash("sha256").update(x).digest("hex");
const file=p=>({bytes:statSync(p).size,sha256:hash(readFileSync(p))});
const htmlSource=readFileSync(resolve("owl-pet/3d-experiments/172-tyto-castanops/run277_true_animated_3d_webgl2_viewer_RESEARCH_NO_RELEASE.html"),"utf8");
const snippet='clipAt(clips.some(x=>x.name==="idle")?"idle":clips[0].name,0);';
if(!htmlSource.includes(snippet))throw Error("Existing rig viewer changed; refuse unsafe patch");
const html=htmlSource.replace(snippet,'view("front");').replace("Run277 native animated GLB technical reference","Run279b real Blender groom to GLB technical reference");
const report={experiment:"Run279b original genuine groom-converted native GLB software WebGL2",
 license:"NONCOMMERCIAL_RESEARCH_ONLY",art:"ART_REJECTED_PREVIEW",phoneGPU:"UNTESTED",
  softwareGPU:"ANGLE SwiftShader expected but detected at runtime",status:"FAIL_NO_RELEASE",
  frames:[],gates:{},errors:[]};
let server,browser;
try {
 const b=readFileSync(model);
 if(!expected||b.subarray(0,4).toString()!=="glTF"||hash(b)!==expected)throw Error("GLB source hash mismatch");
 report.model=file(model);
 server=createServer((req,res)=>{
   let bytes, mime;
   try {
     if(req.url==="/viewer.html"){bytes=Buffer.from(html);mime="text/html; charset=utf-8";}
     else if(req.url==="/model.glb"){bytes=readFileSync(model);mime="model/gltf-binary";}
     else if(req.url?.startsWith("/node_modules/three/")){
        const rel=req.url.slice("/node_modules/three/".length);
        if(rel.split("/").includes("..") || !/^[a-zA-Z0-9_./-]+$/.test(rel))throw Error("unsafe path");
        bytes=readFileSync(resolve("node_modules/three",rel));mime="text/javascript; charset=utf-8";
     }else throw Error("not found");
     res.writeHead(200,{"Content-Type":mime,"Cache-Control":"no-store"});res.end(bytes);
   }catch(e){res.writeHead(404);res.end("not found");}
 });
 await new Promise((ok,bad)=>server.listen(0,"127.0.0.1",err=>err?bad(err):ok()));
 browser=await chromium.launch({headless:true,args:["--no-sandbox","--use-angle=swiftshader","--enable-unsafe-swiftshader","--enable-webgl"]});
 const page=await browser.newPage({viewport:{width:390,height:780},deviceScaleFactor:1});
 page.on("pageerror",e=>report.errors.push(String(e)));
 await page.goto("http://127.0.0.1:"+server.address().port+"/viewer.html",{waitUntil:"load"});
 await page.waitForFunction(()=>window.__qa?.status!=="loading",{timeout:100000});
 const ready=await page.evaluate(()=>window.__qa);
 if(ready.status!=="ready")throw Error("GLTFLoader "+JSON.stringify(ready));
 report.runtime=ready.stats;
 for (const direction of ["front","threequarter","right","back","left","top","bottom"]){
   const observed=await page.evaluate(name=>window.__qa.view(name),direction);
   await page.waitForTimeout(90);
   const p=join(dest,"original_glb_actual_webgl2_"+direction+"_390x780.png");
   await page.locator("#stage").screenshot({path:p});
   report.frames.push({direction,...observed,image:file(p)});
 }
 report.gates={
  exact_native_glb_hash:report.model.sha256===expected,
  actual_ThreeJS_GLTFLoader:ready.stats.source.includes("GLTFLoader"),
  genuine_chromium_WebGL2:ready.stats.isWebGL2===true,
  real_geometry_present:ready.stats.triangles>=65000 && ready.stats.meshCount>=2,
  normals_present:ready.stats.missingNormals===0,
  no_animation_requirement:ready.stats.animations.length===0,
  no_mobile_canvas_cropping:report.frames.every(x=>x.projection.within_90pct===true),
  actual_390x780_canvas:report.frames.every(x=>x.actual_canvas.join(",")==="390,780"&&x.css_canvas.join(",")==="390,780"),
  seven_distinct_spatial_views:new Set(report.frames.map(x=>x.image.sha256)).size===7,
  script_no_errors:report.errors.length===0
 };
 report.status=Object.values(report.gates).every(Boolean)?"TRUE_REAL_GLTF_HAIR_MESH_SOFTWARE_WEBGL2_PASS_ART_REJECTED_PHONE_UNTESTED_NO_RELEASE":"BROWSER_TECHNICAL_GATE_FAIL_NO_RELEASE";
 console.log(JSON.stringify({status:report.status,gates:report.gates,runtime:report.runtime},null,2));
}catch(e){report.error=String(e?.stack||e);console.error(report.error);}
finally{
 if(browser)await browser.close().catch(()=>{});
 if(server)await new Promise(ok=>server.close(ok));
 writeFileSync(join(dest,"run279b_actual_browser_report.json"),JSON.stringify(report,null,2)+"\n");
}
if(!report.status.startsWith("TRUE_REAL_GLTF_HAIR_MESH_SOFTWARE_WEBGL2_PASS"))process.exitCode=1;
