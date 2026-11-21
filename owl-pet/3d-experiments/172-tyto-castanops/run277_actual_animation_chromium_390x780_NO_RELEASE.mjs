#!/usr/bin/env node
/** Run277: actually evaluate animated SKIN joints and pixel changes in GLTFLoader, not merely list glTF clips.
 * Authentic Gobkit free lowpoly donor only. NEVER a claim of #172 visual acceptance or mobile GPU validation.
 */
import {chromium} from "playwright";
import {createServer} from "node:http";
import {readFileSync,statSync,writeFileSync,mkdirSync} from "node:fs";
import {resolve,join} from "node:path";
import {createHash} from "node:crypto";
const model=resolve(process.env.OWL172_GLB_INPUT||"");
const viewer=resolve("owl-pet/3d-experiments/172-tyto-castanops/run277_true_animated_3d_webgl2_viewer_RESEARCH_NO_RELEASE.html");
const evidence=resolve(process.env.OWL172_QA_DIR||"owl172-run277-evidence/browser");
const expected=process.env.OWL172_EXPECTED_SHA;
mkdirSync(evidence,{recursive:true});
const sha=x=>createHash("sha256").update(x).digest("hex");
const stat=p=>({bytes:statSync(p).size,sha256:sha(readFileSync(p))});
const report={run:277,release:"NO_RELEASE",model_art:"GOBKIT_LOW_POLY_DONOR_REJECTED",
  phone_gpu:"UNTESTED", paid_usd:0, static_views:[], temporal_frames:[], gates:{},
  observed_at:new Date().toISOString()};
let browser=null,srv=null;
try{
 const b=readFileSync(model);
 if(b.subarray(0,4).toString()!=="glTF"||!expected||sha(b)!==expected)
  throw Error("Not exactly expected authentic GLB source");
 report.model=stat(model);
 srv=createServer((req,res)=>{
  let p=null;
  if(req.url==="/viewer.html")p=viewer;
  else if(req.url==="/model.glb")p=model;
  else if(req.url?.startsWith("/node_modules/three/")){
   const rel=req.url.slice("/node_modules/three/".length);
   if(/^[a-zA-Z0-9_./-]+$/.test(rel)&&!rel.split("/").includes(".."))p=resolve("node_modules/three",rel);
  }
  if(!p){res.writeHead(404);res.end();return}
  try{const f=readFileSync(p);res.writeHead(200,{"Content-Type":p.endsWith(".glb")?"model/gltf-binary":p.endsWith(".html")?"text/html; charset=utf-8":"text/javascript; charset=utf-8","Cache-Control":"no-store"});res.end(f)}
  catch(e){res.writeHead(404);res.end("not found")}
 });
 await new Promise((ok,bad)=>srv.listen(0,"127.0.0.1",e=>e?bad(e):ok()));
 browser=await chromium.launch({headless:true,args:["--no-sandbox","--use-angle=swiftshader","--enable-unsafe-swiftshader","--enable-webgl"]});
 const page=await browser.newPage({viewport:{width:390,height:780},deviceScaleFactor:1});
 const errors=[];page.on("pageerror",e=>errors.push(String(e)));
 await page.goto("http://127.0.0.1:"+srv.address().port+"/viewer.html",{waitUntil:"load"});
 await page.waitForFunction(()=>window.__qa?.status!=="loading",{timeout:110000});
 const ready=await page.evaluate(()=>({status:window.__qa.status,error:window.__qa.error,stats:window.__qa.stats}));
 if(ready.status!=="ready")throw Error("GLTFLoader failed "+JSON.stringify(ready));
 report.browser=ready;report.errors=errors;
 const clipMap=new Map(ready.stats.animations.map(x=>[x.name,x.duration]));
 for (const view of ["front","threequarter","right","back","left","top","bottom"]){
  const pose=await page.evaluate(v=>window.__qa.view(v),view);
  await page.waitForTimeout(100);
  const dest=join(evidence,"actual_"+view+"_390x780.png");
  await page.locator("#stage").screenshot({path:dest});
  report.static_views.push({view,...pose,file:stat(dest)});
 }
 for(const clip of ["idle","walk"]){
  const dur=clipMap.get(clip);
  if(typeof dur!=="number"||dur<=0)throw Error("Missing true animation clip "+clip);
  for (const frac of [0.00,0.22,0.55,0.82]){
   const pose=await page.evaluate(([name,t])=>window.__qa.clipAt(name,t),[clip,frac*dur]);
   await page.waitForTimeout(80);
   const target=join(evidence,"actual_"+clip+"_"+String(frac).replace(".","p")+"_390x780.png");
   await page.locator("#stage").screenshot({path:target});
   const joints=pose.joints;
   delete pose.joints;
   report.temporal_frames.push({clip,frac,t:frac*dur,...pose,
      bone_matrix_sha256:sha(JSON.stringify(joints)),bone_count:joints.length,file:stat(target)});
  }
 }
 const uniques=clip=>new Set(report.temporal_frames.filter(x=>x.clip===clip).map(x=>x.bone_matrix_sha256)).size;
 const uniqueShots=clip=>new Set(report.temporal_frames.filter(x=>x.clip===clip).map(x=>x.file.sha256)).size;
 const allFrames=[...report.static_views,...report.temporal_frames];
 report.gates={
  real_2_0_native_source:report.model.sha256===expected,
  playwright_chromium_and_threejs:ready.stats.source.includes("GLTFLoader"),
  genuine_webgl2:ready.stats.isWebGL2===true,
  animated_skinned_mesh:ready.stats.skinMeshes>0&&ready.stats.bones>0,
  two_real_named_animations:clipMap.has("idle")&&clipMap.has("walk"),
  native_valid_meshes_and_normals:ready.stats.triangles>=100&&ready.stats.missingNormals===0,
  real_css_canvas_size:allFrames.every(x=>x.actual_canvas.join(",")==="390,780"&&x.css_canvas.join(",")==="390,780"),
  full_bbox_with_margin_no_clipping:allFrames.every(x=>x.projection.within_90pct===true),
  seven_distinct_spatial_views:new Set(report.static_views.map(x=>x.file.sha256)).size===7,
  nonzero_idle_bone_animation:uniques("idle")>1,
  nonzero_walk_bone_animation:uniques("walk")>1,
  true_idle_pixel_animation:uniqueShots("idle")>1,
  true_walk_pixel_animation:uniqueShots("walk")>1,
  browser_no_page_errors:errors.length===0
 };
 report.animation_variations={idle_joint_unique:uniques("idle"),walk_joint_unique:uniques("walk"),
  idle_screenshot_unique:uniqueShots("idle"),walk_screenshot_unique:uniqueShots("walk")};
 report.status=Object.values(report.gates).every(Boolean)?
  "REAL_BROWSER_RIG_ANIMATION_AND_FRAMING_TECHNICAL_PASS_ART_REJECTED_PHONE_UNTESTED_NO_RELEASE":
  "REAL_BROWSER_QA_FAIL_NO_RELEASE";
 console.log(JSON.stringify({status:report.status,gates:report.gates,animation_variations:report.animation_variations,stats:ready.stats},null,2));
}catch(e){report.status="FAIL_NO_RELEASE";report.error=String(e?.stack||e);console.error(report.error)}
finally{
 if(browser)try{await browser.close()}catch{}
 if(srv)try{await new Promise(done=>srv.close(done))}catch{}
 report.finished=new Date().toISOString();
 writeFileSync(join(evidence,"run277_real_browser_animation_report.json"),JSON.stringify(report,null,2)+"\n");
}
if(!report.status.startsWith("REAL_BROWSER_RIG_ANIMATION_AND_FRAMING_TECHNICAL_PASS"))process.exitCode=1;
