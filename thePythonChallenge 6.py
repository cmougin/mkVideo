# -*- coding: utf-8 -*-
"""
différents essais pour répondre au challenge:
    http://www.pythonchallenge.com/pc/def/peak.html
"""

import requests
import zipfile

r=requests.get("http://www.pythonchallenge.com/pc/def/channel.zip")
f=open("tmp.zip",'wb')
f.write(r.content)
f.close
#tmp.zip ressemble à channel.zip mais il est plus court… et corrompu! 
#peut être une histoire d'octets nuls ?
zf = zipfile.ZipFile('channel.zip', 'r')
#print zf.namelist()


archive=90052

try:
    data = zf.read("%d.txt"%archive)
except KeyError:
    print 'ERROR: Did not find %d.txt in zip file' % archive
else:
    print archive, ':', data
    print data
