import run343 as e
import numpy as np,json,hashlib
from scipy.interpolate import PchipInterpolator
from PIL import Image,ImageDraw
# For each fixed x,y: positive longitudinal scaling, then smoothly taper
# displacement at z=center. This is a geometry-preserving hypothesis.
oldr=PchipInterpolator(e.yk,[-.45,-.55,-.49,-.34,-.20,-.23,-.29,-.27,-.19,-.02])
def deform(v,strength):
 x,y,z=v.T;yc=np.clip(y,e.yk[0],e.yk[-1]);xc=np.clip(x/e.w(yc),-.999,.999);c=.19;shape=np.sqrt(1-xc*xc)
 old=c-(c-oldr(yc))*shape;target=c-(c-e.r(yc))*shape
 # smoothstep derivative bounded by 1.5 / span; delta <= 0.55*span ensures positive Jacobian.
 span=np.maximum(c-old,.03);delta=np.clip(target-old,-.55*span,.55*span)
 lock=e.sm(-.81,-.66,y)*(1-e.sm(.24,.65,y));q=v.copy();q[:,2]+=strength*lock*delta*e.sm(c,c-span,z);return q
e.deform=deform
path,stats=e.make('C_monotone',1.0);print(json.dumps(stats,indent=2));(e.P/'run343_C_report.json').write_text(json.dumps(stats,indent=2))
contact=Image.new('RGB',(1120,600),'white');draw=ImageDraw.Draw(contact)
for j,(label,p) in enumerate([('baseline',e.src),('C monotone',path)]):
 for i,img in enumerate(e.render(p)):
  contact.paste(img,(i*280,j*300+20));draw.text((i*280+5,j*300+4),label+' '+['front','side','back','rear 3/4'][i],fill='black')
contact.save(e.P/'run343_C_contact.jpg',quality=85)
