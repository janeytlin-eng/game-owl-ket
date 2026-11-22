// #172 Run293. One free, anonymous image-to-native-3D capability probe. Synthetic input only.
// Copyright/quality hold: never archive unlicensed provider output or call it the owl character.
import fs from 'node:fs'; import path from 'node:path'; import crypto from 'node:crypto';
import { chromium } from 'playwright-core';
const E='owl172-run293-evidence'; fs.mkdirSync(E,{recursive:true});
const report={run:293,provider:'https://trellis2.dev/',input:'synthetic-test-ONLY-not-user-concept',
  cost_usd:0, generation_attempted:false, native_glb_valid:false, model_rights_unverified:true,
  art_approved:false,physical_phone_tested:false,release_allowed:false,events:[],errors:[]};
let browser;
try{
  browser=await chromium.launch({executablePath:process.env.CHROME_BIN||'/usr/bin/google-chrome',
    headless:true,args:['--no-sandbox','--disable-dev-shm-usage','--disable-gpu']});
  const page=await browser.newPage({viewport:{width:390,height:780},acceptDownloads:true});
  const downloads=[];
  page.on('download',async d=>{
    try{const p=path.join(E,'TEMP-UNLICENSED-'+d.suggestedFilename().replace(/[^a-z0-9._-]/gi,'_'));
      await d.saveAs(p);downloads.push(p);report.events.push({event:'download',bytes:fs.statSync(p).size});}
    catch(e){report.errors.push('download: '+String(e))}
  });
  page.on('response',r=>{if(/\.glb(\?|$)|\/api\/(generate|jobs|3d)/i.test(r.url()))
    report.events.push({event:'response',status:r.status(),url:r.url().slice(0,250)});});
  const res=await page.goto('https://trellis2.dev/',{waitUntil:'domcontentloaded',timeout:40000});
  report.http_status=res?.status();report.title=await page.title();
  await page.screenshot({path:path.join(E,'01-site.png')});
  if(report.http_status!==200)throw Error('No successful HTTP 200 navigation');
  const input=page.locator('input[type=file]').first();
  if(!await input.count())throw Error('No actual file uploader');
  await input.setInputFiles('synthetic_owl_test.png');
  await page.waitForTimeout(1800);
  await page.screenshot({path:path.join(E,'02-uploaded.png')});
  const buttons=page.getByRole('button',{name:/generate/i});let chosen=-1;
  const candidates=[];
  for(let i=0;i<await buttons.count();i++){
    const b=buttons.nth(i);candidates.push({i,label:(await b.innerText()).trim().slice(0,220),
      visible:await b.isVisible(),enabled:await b.isEnabled()});
  }
  report.button_candidates=candidates;
  // CRITICAL: the first "Generate 3D Free" is a navigation CTA, not the actual submit action!
  const actual=candidates.find(c=>c.visible&&c.enabled&&/Fast\s*&\s*Private|~50s/i.test(c.label));
  if(actual)chosen=actual.i;
  report.generate_button_count=await buttons.count();report.enabled_actual_submit_found=chosen>=0;
  if(chosen<0)throw Error('No enabled ACTUAL submit button (never click a navigation CTA)');
  report.generation_attempted=true;report.chosen_submit_label=actual.label;
  await buttons.nth(chosen).click({timeout:12000});
  const start=Date.now();
  for(let i=0;i<20;i++){
    await page.waitForTimeout(5000);
    if(downloads.length)break;
    const link=page.getByRole('link',{name:/download.*(glb|3d|model)|export.*glb/i}).first();
    if(await link.count()&&await link.isVisible()){
      try{await link.click({timeout:3000})}catch(e){report.events.push({event:'click_error',message:String(e).slice(0,160)})}
    }
    if(i%5===4)report.events.push({event:'progress',seconds:Math.round((Date.now()-start)/1000),
       visible_text:(await page.locator('body').innerText()).slice(-350)});
  }
  report.elapsed_seconds=Math.round((Date.now()-start)/1000);
  report.final_body=(await page.locator('body').innerText()).slice(-1200);
  await page.screenshot({path:path.join(E,'03-result.png'),fullPage:true});
  for(const p of downloads){
    const b=fs.readFileSync(p);const qa={bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')};
    try{
      if(b.length<20||b.toString('ascii',0,4)!=='glTF'||b.readUInt32LE(4)!==2||b.readUInt32LE(8)!==b.length)
        throw Error('Wrong GLB2 magic, version or length');
      const sz=b.readUInt32LE(12);
      if(b.toString('ascii',16,20)!=='JSON'||sz>10000000)throw Error('Missing JSON chunk');
      const d=JSON.parse(b.subarray(20,20+sz).toString('utf8'));
      qa.meshes=d.meshes?.length||0;
      qa.primitives=(d.meshes||[]).reduce((n,m)=>n+(m.primitives||[]).filter(x=>x.attributes?.POSITION!==undefined).length,0);
      if(qa.primitives<1)throw Error('No real 3D POSITION mesh');
      qa.valid=true;report.native_glb_valid=true;
    }catch(e){qa.valid=false;qa.error=String(e)}
    report.events.push({event:'binary_qa',...qa});
    fs.unlinkSync(p); // Unverified redistribution rights: no third-party binary in GH artifact.
  }
}catch(e){report.errors.push(String(e));}
finally{
  try{await browser?.close()}catch{}
  report.final_gate=report.native_glb_valid?'TECH_PROBE_NATIVE_GLB_PASS_ART_UNREVIEWED_NO_RELEASE':
    'NO_VERIFIED_NATIVE_GLB_ART_UNREVIEWED_NO_RELEASE';
  fs.writeFileSync(path.join(E,'run293_probe_report.json'),JSON.stringify(report,null,2));
  const lines=fs.readdirSync(E).sort().filter(n=>n!=='SHA256SUMS.txt').map(n=>
    crypto.createHash('sha256').update(fs.readFileSync(path.join(E,n))).digest('hex')+'  '+n);
  fs.writeFileSync(path.join(E,'SHA256SUMS.txt'),lines.join('\n')+'\n');
  console.log('RUN293 FINAL',report.final_gate,'SHA_FILES',lines.length,'COST $0 NO RELEASE');
}
