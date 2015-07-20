# -*- coding: utf-8 -*-
"""
différents essais pour répondre au challenge:
    http://www.pythonchallenge.com/pc/return/evil.html
    l'astuce est de regarder si evil1.jpg, evil2.jpg (displaying « not JPG but GFX »), evil3.jpg 
    www.pythonchallenge.com/pc/return/evil2.gfx
"""

#dealing evil

with open('evil2.gfx', 'rb') as gfx:
    content = gfx.read()
    
for i in range(5):
    with open("img" + "%d"%(i), "wb") as img:
        img.write(content[i::5])

#génère 5 image dont GIMP reconnaît les formats malgré l'absence d'extension
#ces images font apparaître les mots "dis" "pro" "port" "ional" tronqué et "ity" biffé

print "fin du prg."
