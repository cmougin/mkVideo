# -*- coding: utf-8 -*-
"""
différents essais pour répondre au challenge:
    http://www.pythonchallenge.com/pc/def/peak.html
"""

import requests
import zipfile
import re

#r=requests.get("http://www.pythonchallenge.com/pc/def/channel.zip")
#f=open("tmp.zip",'wb')
#f.write(r.content)
#f.close
#
#tmp.zip ressemble à channel.zip mais il est plus court… et corrompu! 
#peut être une histoire d'octets nuls ?
zf = zipfile.ZipFile('channel.zip', 'r')
#print zf.namelist()

archive="90052"
v=1
msg=""
while v!=None:
    try:
        data = zf.read(archive+".txt")
    except KeyError:
        print 'ERROR: Did not find %s.txt in zip file' % archive
    else:
        for info in zf.infolist():
            msg+=info.comment
        v=re.search("Next nothing is ([0-9]+)", data)
        if v!=None:
            print v.group(0)
            archive=v.group(1)
        else:
            print data
print msg, "fin du prg."