# -*- coding: utf-8 -*-
"""
différents essais pour répondre au challenge:
    http://www.pythonchallenge.com/pc/return/balloons.html
"""
#can you tell the difference ?

print "début du programme..."

#il y a deux images semblables, l'une semblant moins contrastée que l'autre
#et on nous demande de dire la différence. cela semble trivial a priori:

from PIL import Image

img=Image.open("cygne.jpg")
l=list(img.getdata())
(w,h)=img.size
w2=int(w/2)
print w, w2
print l[:w2]
l2=list(l[w2:])
l3=zip(l,l2)
ll=[]
for ((r1,g1,b1),(r2,g2,b2)) in l3:
    r=abs(r1-r2)
    g=abs(g1-g2)
    b=abs(b1-b2)
    ll.append((r,g,b))
im=Image.new(img.mode, img.size)
im.putdata(ll)
im.show()

print "fin du prg."