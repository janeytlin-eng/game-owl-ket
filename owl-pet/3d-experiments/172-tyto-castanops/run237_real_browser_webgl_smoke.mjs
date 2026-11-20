#!/usr/bin/env node
/**
 * Run237. Open the actual Run236 neural owl GLB inside an actual WebGL2 context
 * using Three.js GLTFLoader and Playwright Chromium. This is NOT a mobile device
 * performance test, NOT a quality acceptance and NOT a public demo.
 *
 * Uses the original native binary GLB artifact, not an SVG, canvas drawing or
 * screenshot of a separately rendered image.
 */
import { chromium } from 'playwright';
import { createServer } from 'node:http';
import { readFileSync, writeFileSync, mkdirSync, statSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { createHash } from 'node:crypto';

const repoRoot = process.cwd();
const rel = 'owl-pet/3d-experiments/172-tyto-castanops';
const input = process.env.OWL172_GLB_INPUT ? resolve(process.env.OWL172_GLB_INPUT) : resolve(repoRoot, rel, 'run237-source', 'run236_real_neural_eye_softdown_STUDY_ART_REJECTED_NO_RELEASE.glb');
const evidence = process.env.OWL172_QA_DIR ? resolve(process.env.OWL172_QA_DIR) : resolve(repoRoot, rel, 'run237-evidence');
const viewer = resolve(repoRoot, rel, 'run237_browser_viewer_RESEARCH_ONLY.html');
const expected = process.env.OWL172_EXPECTED_SHA || '4a4a1b22048734d2926b1e27066dd76f125b4575554b305fd28b3233db300d33';
mkdirSync(evidence, { recursive: true });
const sha256 = buf => createHash('sha256').update(buf).digest('hex');
const fileRecord = path => ({bytes:statSync(path).size, sha256:sha256(readFileSync(path))});
const report = {
  run: process.env.OWL172_RUN_LABEL || 'Run237', release:'NO_RELEASE', art_pass:false, phone_webgl:'UNTESTED',
  experiment:'Chromium Playwright WebGL2 software-driver native Three.js GLTFLoader smoke',
  extra_paid_usd:0, timestamp_utc:new Date().toISOString()
};
const logs = [], errors = [];
let server, browser;
try {
  const binary = readFileSync(input);
  if (binary.toString('utf8',0,4) !== 'glTF' || sha256(binary) !== expected)
    throw Error('Unverified or non-native Run236 source');
  report.source = fileRecord(input);
  server = createServer((req, res) => {
    let path = null;
    if (req.url === '/viewer.html') path = viewer;
    if (req.url === '/model.glb') path = input;
    if (req.url?.startsWith('/node_modules/three/')) {
      const sub = req.url.substring('/node_modules/three/'.length);
      if (/^[\w./-]+$/.test(sub) && !sub.split('/').includes('..'))
        path = resolve(repoRoot, 'node_modules', 'three', sub);
    }
    if (!path) { res.writeHead(404); res.end('not found'); return; }
    try {
      const data = readFileSync(path);
      const mime = path.endsWith('.glb') ? 'model/gltf-binary' :
        path.endsWith('.html') ? 'text/html; charset=utf-8' : 'text/javascript; charset=utf-8';
      res.writeHead(200, {'Content-Type':mime,'Cache-Control':'no-store'});
      res.end(data);
    } catch(e) {res.writeHead(404);res.end('missing file');}
  });
  await new Promise((ok, fail)=>server.listen(0, '127.0.0.1', err=>err?fail(err):ok()));
  const port = server.address().port;
  browser = await chromium.launch({headless:true,args:[
    '--use-angle=swiftshader','--enable-unsafe-swiftshader','--enable-webgl',
    '--no-sandbox'
  ]});
  const page = await browser.newPage({ viewport:{width:680,height:680},deviceScaleFactor:1 });
  page.on('console', m=>logs.push({type:m.type(), text:m.text().slice(0,1000)}));
  page.on('pageerror', e=>errors.push('pageerror: '+e.message));
  page.on('requestfailed', r=>errors.push('requestfailed: '+r.url()+' '+r.failure()?.errorText));
  await page.goto('http://127.0.0.1:'+port+'/viewer.html',{waitUntil:'load',timeout:45000});
  await page.waitForFunction(()=>window.__qa?.status !== undefined &&
    window.__qa.status !== 'loading',null,{timeout:90000});
  report.browser = await page.evaluate(()=>({
    status:window.__qa.status, error:window.__qa.error||null,
    renderer:window.__qa.rendererInfo||null, model:window.__qa.modelInfo||null
  }));
  if (report.browser.status !== 'ready')
    throw Error('Three.js native GLB runtime failed: '+report.browser.error);
  const directions = ['front','left','threequarter','right','back','top','bottom'];
  report.views = [];
  for (const name of directions) {
    const r = await page.evaluate(name=>window.__qa.setView(name),name);
    const imagePath=join(evidence,'run237_'+name+'_WEBGL_RESEARCH_NOT_APPROVED.png');
    await page.locator('#stage').screenshot({path:imagePath});
    report.views.push({name,...r,screenshot:fileRecord(imagePath)});
  }
  report.software_benchmark = await page.evaluate(()=>window.__qa.benchmark(100));
  report.browserErrors = errors;
  report.console = logs.slice(-30);
  const glIs2 = report.browser.renderer?.isWebGL2;
  const coverageGood = report.views.every(v=>v.foregroundFraction > .025 && v.foregroundFraction < .92 && v.distinctSampleColors >= 10);
  const unique = new Set(report.views.map(v=>v.screenshot.sha256)).size;
  report.gates={
    native_glb_sha: report.source.sha256 === expected,
    webgl2: glIs2 === true,
    real_mesh_count: report.browser.model?.meshCount>=2,
    real_triangles: report.browser.model?.triangles>=80000,
    normal_attributes: report.browser.model?.missingNormals === 0,
    nonmetallic_pbr_shading: report.browser.model?.maxMetalness <= 0.01,
    true_alpha_down: report.browser.model?.alphaMaskedMaterials >= 1,
    seven_distinct_webgl_views: unique === 7,
    nonblank_pixel_checks: coverageGood,
    no_browser_error:errors.length===0
  };
  report.status=Object.values(report.gates).every(Boolean) ?
    'NATIVE_WEBGL2_SOFTWARE_SMOKE_PASS_ART_REJECTED_PHONE_UNTESTED_NO_RELEASE' :
    'NATIVE_WEBGL2_SOFTWARE_SMOKE_FAIL_ART_REJECTED_NO_RELEASE';
  console.log(JSON.stringify({status:report.status, gates:report.gates,
    driver:report.browser.renderer, model:report.browser.model, benchmark:report.software_benchmark},null,2));
} catch(e) {
  report.status='EXPERIMENT_FAILED_NO_RELEASE';
  report.failure=String(e?.stack||e);
  report.browserErrors=errors;
  report.console=logs.slice(-30);
  console.error(report.failure);
} finally {
  try {if(browser) await browser.close();} catch {}
  try {if(server) await new Promise(ok=>server.close(()=>ok()));} catch {}
  const p=join(evidence,'run237_machine_report.json');
  writeFileSync(p,JSON.stringify(report,null,2)+'\n');
}
if(report.status!=='NATIVE_WEBGL2_SOFTWARE_SMOKE_PASS_ART_REJECTED_PHONE_UNTESTED_NO_RELEASE')
  process.exitCode=1;
