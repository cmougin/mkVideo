# -*- coding: utf-8 -*-
"""
différents essais pour répondre au challenge:
    http://www.pythonchallenge.com/pc/def/oxygen.html
"""

#import requests

#r=requests.get("http://www.pythonchallenge.com/pc/def/oxygen.png")
#f=open("tmp.png",'wb')
#f.write(r.content)
#f.close

from PIL import Image

im = Image.open("tmp.png")
#print im.size
#
#print im.getpixel((0,0))
#print list(im.getdata())[0]
#print list(im.getdata())[0][0]

l2=[l for l in list(im.getdata()) if l[1]==l[2] and l[1]==l[0]]
l3=[]
previous=-1
cnt=0
for i in l2:
    if i[0]==previous:
        cnt+=1
    else:
        if cnt>=6:
            l3.append(i[0])
#        else:
#            print cnt
        cnt=0
        previous=i[0]
msg=""
for i in l3:
    msg=msg+chr(i)
print msg

import re
m=re.search(r"\[(\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+)\]",msg)
if m:
    print(reduce(lambda a, b: a+chr(int(b)), m.groups(),""))
else:
    print "not found"        
print "fin du prg."
##on obtient "i
##              egiy" soit un truc proche de "integrity"