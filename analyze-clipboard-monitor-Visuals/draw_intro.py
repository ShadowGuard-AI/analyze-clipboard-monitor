#!/usr/bin/env python3
"""analyze-clipboard-monitor intro: autumn roundup corral in tundra mist, textless, chart carries notch shapes only."""
import math, random
from PIL import Image, ImageDraw, ImageFilter
random.seed(83)
W,H=1200,520
BONE=(238,228,200); FUR=(122,86,54); IND=(52,58,110); CYAN=(110,220,225); GRASS=(168,152,104)
img=Image.new('RGB',(W,H),(214,216,208)); d=ImageDraw.Draw(img,'RGBA')
# wide pale sky, daylight pale at the top, faint ice cyan aurora thread
for y in range(0,210):
    t=y/210; d.line([(0,y),(W,y)],fill=(int(216-14*t),int(218-12*t),int(210+4*t)))
for i in range(3):
    pts=[(120+40*j, 66+int(16*math.sin(j/7+i)) + i*13) for j in range(24)]
    d.line(pts,fill=(110,220,225,110),width=4)
# low hills as aurora indigo silhouettes
d.polygon([(0,238),(240,196),(470,226),(720,192),(960,224),(1200,204),(1200,268),(0,268)],fill=(86,92,138))
d.polygon([(0,252),(300,224),(620,250),(900,228),(1200,250),(1200,282),(0,282)],fill=(104,110,152))
# flat tundra in fur brown and faded grass tones
d.rectangle([0,268,W,520],fill=(164,142,100))
for _ in range(500):
    x,y=random.uniform(0,W),random.uniform(272,512); d.line([(x,y),(x+random.uniform(4,14),y)],fill=random.choice([(150,128,88),(178,158,112),(140,120,84)]),width=1)
for _ in range(16):  # scatter of low stones and dwarf shrubs
    x,y=random.uniform(0,W),random.uniform(300,384); d.ellipse([x,y,x+16,y+7],fill=(120,116,108)); d.ellipse([x+18,y+3,x+30,y+9],fill=(110,118,84))
# short fence segments at the sides running back into mist
for fx in (470,540,760,830):
    d.line([(fx,388),(fx+34,300)],fill=FUR,width=4)
# mist bands
for my in (286,318,352):
    d.rectangle([0,my,W,my+16],fill=(232,234,228,90))
# the herd in its circling ring, midground
def deer(x,y,s,flip=1):
    d.ellipse([x-26*s,y-11*s,x+26*s,y+11*s],fill=(146,116,82))
    d.polygon([(x+flip*22*s,y-8*s),(x+flip*36*s,y-16*s),(x+flip*34*s,y-2*s)],fill=(146,116,82))
    hx0,hx1=sorted([x+flip*32*s,x+flip*44*s]); d.ellipse([hx0,y-20*s,hx1,y-9*s],fill=(156,126,90))
    for lx in (-18,-6,10,20):
        d.line([(x+lx*s,y+8*s),(x+lx*s,y+22*s)],fill=(120,94,64),width=max(1,int(3*s)))
    for a in (-0.7,-0.25,0.2):  # antlers rising
        d.line([(x+flip*38*s,y-18*s),(x+flip*(38+10*math.sin(a))*s,y-(30+6*math.cos(a))*s)],fill=(196,178,146),width=max(1,int(2.4*s)))
        d.line([(x+flip*(38+10*math.sin(a))*s,y-(30+6*math.cos(a))*s),(x+flip*(44+12*math.sin(a))*s,y-(36+6*math.cos(a))*s)],fill=(196,178,146),width=max(1,int(1.8*s)))
    d.ellipse([x-8*s,y+24*s,x+30*s,y+30*s],fill=(255,255,255,60))  # breath clouding
ring=[(180,344,0.9,1),(330,330,1.0,1),(490,338,0.85,-1),(650,330,1.0,1),(810,342,0.9,-1),(960,332,1.0,1),(410,368,0.62,1),(730,366,0.62,-1)]
for x,y,s,fl in ring: deer(x,y,s,fl)
deer(560,372,0.5,1)  # a calf keeping close near the inner edge
# a dog turning a calf back at the fence, low and quick
d.ellipse([872,382,916,398],fill=(52,48,44)); d.polygon([(912,386),(928,382),(916,394)],fill=(52,48,44))
for lx in (880,904): d.line([(lx,396),(lx-3,410)],fill=(52,48,44),width=3)
d.line([(874,388),(858,382)],fill=(52,48,44),width=4)
# herders at the gate chute on the right, arms raised in sorting gestures
d.rectangle([1010,330,1180,344],fill=FUR)
for hx in (1042,1130):
    d.ellipse([hx-9,292,hx+9,310],fill=(214,178,142))
    d.polygon([(hx-13,310),(hx+13,310),(hx+16,356),(hx-16,356)],fill=(70,62,74))
    d.line([(hx+10,318),(hx+30,300)],fill=(70,62,74),width=6)
    d.line([(hx-10,318),(hx-24,330)],fill=(70,62,74),width=6)
# foreground: corral post and two rails at close range, frost on the upper rail
d.rectangle([36,180,78,520],fill=(106,74,44))
for yy in range(196,520,26): d.line([(38,yy),(76,yy+8)],fill=(88,60,34),width=2)
d.rectangle([0,238,430,262],fill=FUR); d.rectangle([0,318,430,340],fill=FUR)
d.rectangle([0,238,430,246],fill=(240,246,248))  # frost along the top edge
for _ in range(120):
    x=random.uniform(0,430); d.point((x,240),fill=(255,255,255)); d.point((x,243),fill=(230,240,246))
# rope loop hanging from a peg
d.ellipse([86,268,128,322],outline=(178,150,104),width=6)
d.ellipse([100,258,114,272],fill=(88,60,34))
# lower corner of the bone chart board swinging into frame: outlined ears, one ice cyan notch, no words
d.polygon([(986,520),(1010,392),(1200,404),(1200,520)],fill=BONE,outline=FUR,width=5)
def ear(x,y,s,filled=False):
    d.polygon([(x,y),(x+16*s,y-22*s),(x+30*s,y+2*s),(x+22*s,y+16*s),(x+6*s,y+14*s)],outline=(90,70,44),width=2)
    if filled: d.polygon([(x+13*s,y-4*s),(x+19*s,y-14*s),(x+24*s,y-2*s)],fill=CYAN)
ear(1036,448,1.0); ear(1086,452,1.0); ear(1136,446,1.0,filled=True); ear(1062,492,1.0)
img=img.filter(ImageFilter.GaussianBlur(0.4))
img.save(__file__.rsplit('/',1)[0]+'/intro-banner.png')
print('saved intro')
