#!/usr/bin/env python3
"""analyze-clipboard-monitor logo: the herder ear mark chart board itself, name in Atkinson Hyperlegible below."""
from PIL import Image, ImageDraw, ImageFont
HERE=__file__.rsplit('/',1)[0]
W,H=760,900
BONE=(238,228,200); FUR=(122,86,54); IND=(52,58,110); CYAN=(110,220,225)
img=Image.new('RGB',(W,H),IND); d=ImageDraw.Draw(img,'RGBA')
# aurora indigo strap with a bone toggle above the board
d.rectangle([330,26,430,86],fill=(38,42,84))
d.rectangle([416,26,428,86],fill=CYAN)  # a thread of ice cyan in the strap
d.ellipse([362,38,398,62],fill=BONE,outline=(190,178,150),width=2)  # bone toggle
# portrait board: bone face, fur brown frame rails on both sides
d.rectangle([150,86,610,650],fill=BONE)
d.rectangle([150,86,182,650],fill=FUR); d.rectangle([578,86,610,650],fill=FUR)
d.rectangle([150,86,610,104],fill=FUR); d.rectangle([150,632,610,650],fill=FUR)
for yy in range(120,640,44): d.line([(156,yy),(176,yy+10)],fill=(96,66,38),width=2); d.line([(584,yy),(604,yy+10)],fill=(96,66,38),width=2)
# rows of ear shapes in outline, each with a different arrangement of notches and cuts; the cuts are the writing
def ear(x,y,s,kind,matched=False):
    pts=[(x,y),(x+15*s,y-24*s),(x+23*s,y-10*s),(x+31*s,y+4*s),(x+20*s,y+17*s),(x+5*s,y+15*s)]
    if matched:
        d.polygon(pts,fill=(214,232,216))
        d.polygon(pts,outline=(70,90,80),width=3)
    else:
        d.polygon(pts,outline=(90,70,44),width=3)
    # notch cuts along the edge, cut shown in the board colour with an outline nick
    if kind==0:  # one deep V
        d.polygon([(x+20*s,y-12*s),(x+26*s,y-2*s),(x+15*s,y-4*s)],fill=BONE,outline=(90,70,44),width=2)
    elif kind==1:  # two small nicks
        for dx in (8,18):
            d.polygon([(x+dx*s,y-16*s),(x+(dx+5)*s,y-8*s),(x+(dx-2)*s,y-7*s)],fill=BONE,outline=(90,70,44),width=2)
    elif kind==2:  # tip squared off
        d.line([(x+9*s,y-20*s),(x+22*s,y-19*s)],fill=(90,70,44),width=4)
    elif kind==3:  # notch on the lower edge
        d.polygon([(x+16*s,y+15*s),(x+22*s,y+5*s),(x+27*s,y+13*s)],fill=BONE,outline=(90,70,44),width=2)
    if matched:  # the one that matched: its notch filled in ice cyan rather than outlined
        d.polygon([(x+18*s,y-13*s),(x+25*s,y-1*s),(x+13*s,y-3*s)],fill=CYAN)
kinds=[0,1,2,3,1,0,3,2,0,1,2,3]
n=0
for row in range(4):
    for col in range(3):
        x=232+col*118; y=170+row*118
        matched=(row==1 and col==1)
        ear(x,y,1.55,kinds[n],matched); n+=1
# the name underneath, Atkinson Hyperlegible in bone on aurora indigo, plain block hand
f=ImageFont.truetype(HERE+'/fonts/AtkinsonHyperlegible.ttf',40)
txt='analyze-clipboard-monitor'
tw=d.textlength(txt,font=f); d.text(((W-tw)/2,712),txt,font=f,fill=BONE)
d.line([(120,690),(640,690)],fill=CYAN,width=2)
img.save(HERE+'/logo.png')
img.resize((54,64)).save(HERE+'/scratch/logo64-ship.png')
print('saved logo')
