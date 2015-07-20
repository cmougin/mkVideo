# -*- coding: utf-8 -*-
"""
différents essais pour répondre au challenge:
    http://www.pythonchallenge.com/pc/def/peak.html
"""

import requests
import pickle, pprint

r=requests.get("http://www.pythonchallenge.com/pc/def/banner.p")
data=pickle.loads(r.content)
#pprint.pprint(data)
print data
s=""
for l in data:
    for (a, b) in l:
        s+= a * b
    s+='\n'
print s        