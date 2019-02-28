import os, sys
from PIL import Image

im = Image.open('Ski.png')
width = (im.size)[0]
height = (im.size)[1]
#print(width, height)
wlist=range(0,width)
hlist=range(0,height)
ww=0
for w in wlist:
    hh=0
    for h in hlist:
        #print ([ww,hh])
        hh+=1
        pix = im.load()
        
        temppix = (pix[hh-1,ww])

        r=temppix[0]
        rr=bin(int(round(r/16)))
        g=temppix[1]
        gg=bin(int(round(g/16)))
        b=temppix[2]
        bb=bin(int(round(b/16)))
        rrr=rr[2:]
        ggg=gg[2:]
        bbb=bb[2:]
        while len(rrr) < 4:
            rrr=('0'+rrr)
        while len(ggg) < 4:
            ggg=('0'+ggg)
        while len(bbb) < 4:
            bbb=('0'+bbb)
        if (rrr=='10000'):
            rrr='1111'
        if (ggg=='10000'):
            ggg='1111'
        if (bbb=='10000'):
            bbb='1111'
        print (rrr,ggg,bbb)
    ww+=1
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
'''donny deserves death'''
