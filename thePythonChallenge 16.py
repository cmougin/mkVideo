# -*- coding: utf-8 -*-
"""
différents essais pour répondre au challenge:
    http://huge:file@www.pythonchallenge.com/pc/return/mozart.html
"""
#<title>let me get this straight</title>

import Image
print "début du programme..."

img=Image.open("mozart.gif")
content=list(img.getdata())

(w, h) = img.size
for c in range(w*h):
    if content[c:c+5]==[195, 195, 195, 195, 195]:
        l=int(c/w)
        i=c%w
        newline=content[l*w+i:(l+1)*w] + content[l*w:l*w+i]
        print "found @ ",c, len(newline)
        content[l*w:(l+1)*w]=newline
#        else:
#            print "nope: ",content[ligne*640+col:ligne*640+col+5]
print img.mode, img.size
img2=Image.new(img.mode, img.size)
img2.putdata(content)
img.show()
img2.show()
# the word "romance" appears in diagonale

print "fin du prg."