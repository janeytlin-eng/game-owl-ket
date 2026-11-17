#!/usr/bin/env python3
"""Run125B: follow *only* asset links shown by the public BlendSwap artist page.
No login circumvention, guessed routes, scraping private CDN URLs, or payment.
"""
import json,hashlib,pathlib,re,sys,urllib.request,urllib.error,urllib.parse,html
from html.parser import HTMLParser
OUT=pathlib.Path(sys.argv[1]);OUT.mkdir(parents=True,exist_ok=True)
HOME="https://blendswap.com/blend/11643"
UA="Mozilla/5.0 (compatible; owl172-licensed-asset-public-access-check/1.0)"
class Parser(HTMLParser):
 def __init__(self):
  super().__init__();self.links=[];self.forms=[];self.in_a=False;self.active=None;self.text=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=="a":
   self.in_a=True;self.active={"href":html.unescape(a.get("href","")),"classes":a.get("class",""),"id":a.get("id",""),"text":""}
  if tag=="form":self.forms.append({"action":a.get("action",""),"method":a.get("method","")})
 def handle_endtag(self,tag):
  if tag=="a" and self.active is not None:self.links.append(self.active);self.active=None;self.in_a=False
 def handle_data(self,data):
  if self.active is not None:self.active["text"]+=data.strip()+" "
def request(url,limit=3000000):
 rec={"requested_url":url};body=b""
 try:
  req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":"*/*"})
  with urllib.request.urlopen(req,timeout=30) as resp:
   rec.update(status=resp.status,final_url=resp.geturl(),content_type=resp.headers.get("Content-Type",""),content_length_header=resp.headers.get("Content-Length",""))
   body=resp.read(limit)
 except urllib.error.HTTPError as exc:
  rec.update(status=exc.code,final_url=exc.geturl(),content_type=exc.headers.get("Content-Type",""),error="HTTPError");body=exc.read(100000)
 except Exception as exc:rec.update(status=None,error=type(exc).__name__+": "+str(exc)[:200],final_url=url)
 rec.update(bytes_read=len(body),read_sha256=hashlib.sha256(body).hexdigest(),magic="BLEND" if body[:7]==b"BLENDER" else "ZIP" if body[:4]==b"PK\\x03\\x04" else "GLB" if body[:4]==b"glTF" else "HTML" if b"<html" in body[:1000].lower() or b"<!doctype" in body[:1000].lower() else "OTHER",is_model_binary=False)
 rec["is_model_binary"]=rec["magic"] in ("BLEND","ZIP","GLB")
 return rec,body
base,body=request(HOME,1500000);p=Parser()
if body:p.feed(body.decode("utf-8","replace"))
links=[{**x,"url":urllib.parse.urljoin(HOME,x["href"])} for x in p.links]
candidate=[x for x in links if re.search(r"download|\\.blend|\\.zip|\\.glb|\\.fbx",x["text"]+" "+x["href"]+" "+x["classes"]+" "+x["id"],re.I)]
safe=[]
for x in candidate:
 u=urllib.parse.urlparse(x["url"])
 if u.scheme=="https" and u.netloc in ("blendswap.com","www.blendswap.com") and x["url"]!=HOME:
  safe.append(x)
# Only URLs explicitly provided by the official page; never fabricate URL patterns.
checked=[]; seen=set()
for item in safe[:6]:
 if item["url"] in seen:continue
 seen.add(item["url"])
 rec,payload=request(item["url"],25000000)
 rec["source_link"]={k:item[k] for k in ("text","href","classes","id")}
 checked.append(rec)
 print("official-public-link",rec["status"],rec["magic"],rec["bytes_read"],item["url"][:160],flush=True)
 # Do not place third-party model binaries in a public repository before final rights and art QA.
report={"run":"125B","original_artist_page":HOME,"artist_listed":"drothenbucher","listed_license":"CC BY (independent final file rights still need checking)","homepage_request":base,"anchor_count":len(links),"official_candidate_links":candidate[:40],"form_actions":p.forms[:20],"real_followed_links":checked,"no_auth_or_payment_bypass":True,"model_archived":False,"no_release":True}
(OUT/"run125b_official_artist_links.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
lines=["# Run125B direct artist-model link inspection","",
"Actual source: "+HOME,
f"Page HTTP {base.get('status')} / {base.get('magic')}; {len(links)} anchors; {len(candidate)} candidate links; {len(checked)} public same-host links probed.",
]
for c in checked:lines.append("- "+str(c.get("status"))+" "+c["magic"]+" "+str(c["bytes_read"])+" bytes "+c["requested_url"]+" -> "+c["final_url"])
lines+=["","No source login bypass, no extra payment, no third-party binary redistributed. An artist listing is not an anatomically valid multi-view juvenile mesh. ART_UNREVIEWED / NO_RELEASE."]
(OUT/"run125b_model_access_audit.md").write_text("\n".join(lines)+"\n")
(OUT/"NO_RELEASE.flag").write_text("NO_RELEASE - actual recovered, licensed and quality-approved chick mesh not established.\n")
print("final",json.dumps({"page_status":base["status"],"links":len(candidate),"public_checked":len(checked),"binary":sum(c["is_model_binary"] for c in checked)}),flush=True)
