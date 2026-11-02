#!/usr/bin/env python3
"""analyze-clipboard-monitor wordmark banner: the great roundup corral in tundra mist, name on the gate board over the chute."""
import math, random
from PIL import Image, ImageDraw, ImageFont
random.seed(19)
HERE=__file__.rsplit('/',1)[0]
W,H=1400,560
BONE=(238,228,200); FUR=(122,86,54); IND=(52,58,110); CYAN=(110,220,225)
img=Image.new('RGB',(W,H),(208,211,204)); d=ImageDraw.Draw(img,'RGBA')
for y in range(0,170):
    t=y/170; d.line([(0,y),(W,y)],fill=(int(210-10*t),int(213-8*t),int(206+4*t)))
for i in range(3):  # faint ice cyan thread in a daylight pale sky
    pts=[(700+36*j, 44+int(13*math.sin(j/6+i))+i*11) for j in range(18)]
    d.line(pts,fill=(110,220,225,100),width=3)
# tundra to low hills
d.polygon([(0,196),(260,158),(560,188),(880,154),(1180,186),(1400,168),(1400,240),(0,240)],fill=(96,102,146))
d.rectangle([0,226,W,560],fill=(166,144,102))
for _ in range(700):
    x,y=random.uniform(0,W),random.uniform(232,556); d.line([(x,y),(x+random.uniform(4,14),y)],fill=random.choice([(150,128,88),(180,160,114),(138,118,82)]),width=1)
# the circling herd as a broad ring seen from a slight height
def deer(x,y,s,flip=1):
    d.ellipse([x-25*s,y-10*s,x+25*s,y+10*s],fill=(146,116,82))
    d.polygon([(x+flip*21*s,y-7*s),(x+flip*34*s,y-14*s),(x+flip*32*s,y-2*s)],fill=(146,116,82))
    hx0,hx1=sorted([x+flip*30*s,x+flip*42*s]); d.ellipse([hx0,y-18*s,hx1,y-8*s],fill=(156,126,90))
    for lx in (-16,-5,9,18): d.line([(x+lx*s,y+7*s),(x+lx*s,y+19*s)],fill=(120,94,64),width=max(1,int(3*s)))
    for a in (-0.7,-0.2,0.25):
        d.line([(x+flip*36*s,y-16*s),(x+flip*(36+9*math.sin(a))*s,y-(27+5*math.cos(a))*s)],fill=(198,180,148),width=max(1,int(2.2*s)))
    d.ellipse([x-6*s,y+20*s,x+26*s,y+26*s],fill=(255,255,255,55))
cx,cy=560,368
for i in range(14):
    a=i/14*2*math.pi; x=cx+330*math.cos(a); y=cy+82*math.sin(a); s=0.95-0.25*math.sin(a)
    deer(x,y,s*1.22,1 if math.cos(a)>-0.2 else -1)
for i in range(5):  # calves close to mothers near the inner edge
    a=0.6+i*1.15; deer(cx+210*math.cos(a),cy+50*math.sin(a),0.62,1)
# fence of fur brown posts and rails following the ring
for i in range(18):
    a=i/18*2*math.pi; x=cx+392*math.cos(a); y=cy+104*math.sin(a)
    d.rectangle([x-4,y-30,x+4,y+8],fill=FUR)
for t in (0.86,1.0):
    pts=[(cx+392*t*math.cos(i/40*2*math.pi),cy+104*t*math.sin(i/40*2*math.pi)-16) for i in range(41)]
    d.line(pts,fill=FUR,width=4)
# working gate and narrow chute on the right
d.rectangle([1018,300,1044,470],fill=(96,66,38))
d.polygon([(1060,330),(1240,318),(1240,352),(1060,368)],fill=(140,112,74))
d.polygon([(1060,404),(1240,398),(1240,430),(1060,440)],fill=(140,112,74))
for gx in range(1076,1240,40): d.rectangle([gx,322,gx+7,434],fill=FUR)
deer(1150,376,0.9,1)  # one animal in the chute, checked before it passes
# gate board over the chute carrying the name, the one lettered board
d.rectangle([976,238,1360,296],fill=FUR,outline=(84,56,30),width=3)
f=ImageFont.truetype(HERE+'/fonts/AtkinsonHyperlegible.ttf',23)
txt='analyze-clipboard-monitor'
tw=d.textlength(txt,font=f); d.text((1168-tw/2,254),txt,font=f,fill=BONE)
# herder at the gate holding the ear mark chart board up beside the chute
hx=982
d.ellipse([hx-10,286,hx+10,306],fill=(214,178,142))
d.polygon([(hx-14,306),(hx+14,306),(hx+17,366),(hx-17,366)],fill=(64,58,80))
d.line([(hx+12,314),(hx+34,296)],fill=(64,58,80),width=6)
d.rectangle([1000,302,1046,352],fill=BONE,outline=FUR,width=3)
for ex,ey in [(1008,316),(1026,316),(1008,334),(1026,334)]:
    d.polygon([(ex,ey),(ex+6,ey-9),(ex+12,ey+1),(ex+8,ey+6),(ex+2,ey+5)],outline=(90,70,44),width=1)
d.polygon([(1028,310),(1033,302),(1037,311)],fill=CYAN)
# second herder waving one through to its family pen
hx2=1290
d.ellipse([hx2-10,330,hx2+10,350],fill=(214,178,142))
d.polygon([(hx2-14,350),(hx2+14,350),(hx2+17,410),(hx2-17,410)],fill=(80,66,54))
d.line([(hx2-12,358),(hx2-36,338)],fill=(80,66,54),width=6)
# dogs working the outer edge of the ring, low and quick
for dx,dy in [(196,478),(880,492)]:
    d.ellipse([dx,dy,dx+46,dy+17],fill=(52,48,44)); d.polygon([(dx+42,dy+3),(dx+58,dy),(dx+44,dy+12)],fill=(52,48,44))
    for lx in (dx+8,dx+34): d.line([(lx,dy+15),(lx-3,dy+28)],fill=(52,48,44),width=3)
    d.line([(dx+2,dy+5),(dx-14,dy-1)],fill=(52,48,44),width=4)
# mist thinning near the ground
for my in (250,470):
    d.rectangle([0,my,W,my+14],fill=(232,234,228,70))
img.save(HERE+'/banner.png')
print('saved banner')
