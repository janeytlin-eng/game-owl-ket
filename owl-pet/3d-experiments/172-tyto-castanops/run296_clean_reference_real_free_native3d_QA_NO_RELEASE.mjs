#!/usr/bin/env node
/**
 * Run296 / #172 Tyto castanops v3, user-owned right-hand mesoptile reference.
 * ONE no-charge ordinary browser submit using Run295 pixel-preserving isolated
 * chick (white-background). Native GLB must be independently captured + parsed.
 * NO RELEASE: provider/weights rights, anatomy, fine down and phone all unresolved.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {chromium} from 'playwright-core';
const O='owl172-run296-evidence', INPUT='target-owl172-isolated-WHITE.png';
fs.mkdirSync(O,{recursive:true});
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const report={
  run:296, date:new Date().toISOString(), source:'https://trellis2.dev/',
  known_upstream:'hy3dlab-image-to-3d.hf.space', input:'Run295 exact project reference RGB / GrabCut / white background',
  input_bytes:fs.existsSync(INPUT)?fs.statSync(INPUT).size:0,
  input_sha256:fs.existsSync(INPUT)?sha(fs.readFileSync(INPUT)):null,
  cost_usd:0, attempts:0, user_owned_input:true,
  native_glb_valid:false, art_approved:false, third_party_rights_cleared:false,
  physical_phone_verified:false, publication_allowed:false,
  network_models:[], events:[], errors:[]
};
let browser;const pending=[];let responseFound=false;
try {
  if(!fs.existsSync(INPUT) || !report.input_bytes)throw Error('Run295 whitened real image missing');
  browser=await chromium.launch({executablePath:process.env.CHROME_BIN||'/usr/bin/google-chrome',
    headless:true,args:['--no-sandbox','--disable-dev-shm-usage','--disable-gpu']});
  const page=await browser.newPage({viewport:{width:390,height:780},acceptDownloads:true});
  page.on('response',resp=>{
    if(!/\.glb(?:[?#]|$)/i.test(resp.url()))return;
    pending.push((async()=>{
      const item={url:resp.url(),status:resp.status()};
      try {
        if(!resp.ok())throw Error('HTTP '+resp.status());
        const b=await resp.body();
        item.bytes=b.length;item.sha256=sha(b);
        if(b.length<40||b.toString('ascii',0,4)!=='glTF'||b.readUInt32LE(4)!==2||
           b.readUInt32LE(8)!==b.length)throw Error('GLB2 signature/version/length mismatch');
        const size=b.readUInt32LE(12);
        if(b.toString('ascii',16,20)!=='JSON'||size<20||size>10000000||20+size>b.length)
          throw Error('No valid glTF JSON chunk');
        const j=JSON.parse(b.subarray(20,20+size).toString('utf8'));
        item.meshes=j.meshes?.length??0;
        item.primitivePositions=(j.meshes||[]).reduce((n,m)=>n+(m.primitives||[])
          .filter(p=>p.attributes?.POSITION!==undefined).length,0);
        item.images=j.images?.length??0;item.textures=j.textures?.length??0;
        if(item.primitivePositions<1)throw Error('No native vertex geometry');
        fs.writeFileSync(path.join(O,'actual-chick-clean-input-native-UNAPPROVED.glb'),b);
        item.valid=true;responseFound=true;
      }catch(err){item.valid=false;item.error=String(err).slice(0,500);}
      report.network_models.push(item);
    })());
  });
  page.on('pageerror',err=>report.events.push({kind:'pageerror',error:String(err).slice(0,300)}));
  const res=await page.goto('https://trellis2.dev/',{waitUntil:'domcontentloaded',timeout:50000});
  report.provider_http=res?.status();
  if(report.provider_http!==200)throw Error('Source HTTP not 200: '+report.provider_http);
  await page.locator('input[type=file]').first().setInputFiles(INPUT,{timeout:15000});
  await page.waitForTimeout(1300);
  await page.screenshot({path:path.join(O,'01-clean-reference-uploaded.png')});
  const buttons=page.getByRole('button',{name:/generate/i}), choices=[];
  for(let i=0;i<await buttons.count();i++){
    let b=buttons.nth(i);
    choices.push({index:i,label:(await b.innerText()).trim().slice(0,160),visible:await b.isVisible(),enabled:await b.isEnabled()});
  }
  report.button_choices=choices;
  const action=choices.find(b=>b.visible&&b.enabled&&/Fast\s*&\s*Private|~50s/i.test(b.label));
  if(!action)throw Error('No authentic enabled submit; marketing CTA is not generation');
  await buttons.nth(action.index).click({timeout:12000});
  report.attempts=1;
  const start=Date.now();
  for(let i=0;i<30;i++){
    await page.waitForTimeout(4000);
    if(responseFound)break;
    const s=await page.locator('body').innerText().catch(()=>'');
    if(/processing limit reached|come back tomorrow|quota exceeded|rate limit/i.test(s)){
      report.quota_blocked=true;
      report.events.push({kind:'quota',elapsed_s:Math.round((Date.now()-start)/1000),
        page_excerpt:s.slice(-800)});
      break;
    }
    if(i%6===5)report.events.push({kind:'progress',elapsed_s:Math.round((Date.now()-start)/1000),
      excerpt:s.slice(-350)});
  }
  await Promise.allSettled(pending);
  report.elapsed_seconds=Math.round((Date.now()-start)/1000);
  report.final_body=(await page.locator('body').innerText().catch(()=>'')).slice(-1200);
  await page.screenshot({path:path.join(O,'02-generation-result.png'),fullPage:true});
}catch(err){
  report.errors.push(String(err).slice(0,1000));
}finally{
  await Promise.allSettled(pending);
  try{await browser?.close()}catch{}
  report.native_glb_valid=report.network_models.some(n=>n.valid);
  report.final_gate=report.native_glb_valid?'REAL_GLTF2_NATIVE_GEOMETRY_PENDING_ART_AND_RIGHTS_NO_RELEASE':
    (report.quota_blocked?'PROVIDER_TEMPORARY_QUOTA_BLOCK_NO_MODEL_NO_RELEASE':'NO_NATIVE_MODEL_VERIFIED_NO_RELEASE');
  fs.writeFileSync(path.join(O,'run296_service_report.json'),JSON.stringify(report,null,2));
  console.log(JSON.stringify({run:296,status:report.final_gate,attempts:report.attempts,
    input_sha256:report.input_sha256,models:report.network_models,quota_blocked:!!report.quota_blocked,
    errors:report.errors},null,2));
}
