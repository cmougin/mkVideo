# -*- coding: utf-8 -*-
"""
différents essais pour répondre au challenge:
    http://www.pythonchallenge.com/pc/return/5808.html
"""

#odd/even
import Image

im = Image.open('cave.jpg')
ll = list(im.getdata())
l2=[]
l3=[]
i=1
for x in ll:
    i=1-i
    if i==0:
        l2.append(x)
    else:
        l3.append(x)
im2 = Image.new(im.mode, im.size)
im2.putdata(l2)
im2.putdata(l3)
im2.show() # le mot evil apparait dans l'ombre!

print "fin du prg."
