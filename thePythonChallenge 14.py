# -*- coding: utf-8 -*-
"""
différents essais pour répondre au challenge:
    http://www.pythonchallenge.com/pc/return/italy.html

"""

#walk around
#<!-- remember: 100*100 = (100+99+99+98) + (...  -->
#<img src="wire.png" width="100" height="100">
# le "wire" semble etre à déplier réenrouler du tour vers le centre:
#les 100 premiers pixels vers la droite, 
#les 99 suivants vers le bas,
#les 99 suivants vers la gauche
#les 98 suivants vers le haut
#et ainsi de suite

import Image
print "début du programme..."
img=Image.open("wire.png")   
liste=list(img.getdata())
im2 = Image.new(img.mode,(100, 100)) 
#im2.putdata(liste)
pix = im2.load()

L=100
(x,y)=(0,0)
while L>0 and liste:
    for a in range(L):
        print x,y
        pix[x,y]=liste.pop(0)
        x+=1
    x=x-1
    L=L-1
    print "## ",L," ##"
    for a in range(L):
        print x,y
        pix[x,y]=liste.pop(0)
        y=y+1
    y=y-1
    print "## ",L," ##"
    for a in range(L):
        print x,y
        pix[x,y]=liste.pop(0)
        x=x-1
    x=x+1
    L=L-1
    print "## ",L," ##"
    for a in range(L):
        print x,y
        pix[x,y]=liste.pop(0)
        y=y-1
    y=y+1
    print "## ",L," ##"

im2.show() # => a cat appears on the screen!
print "fin du prg."
