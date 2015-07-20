# -*- coding: utf-8 -*-
"""
différents essais pour répondre au challenge:
    http://www.pythonchallenge.com/pc/return/good.html
"""

#len(a[30]) = ?
#a = [1, 11, 21, 1211, 111221, 

v="1"
for j in range(30):
    out=""
    i=1
    cnt=1
    while i<len(v):
        if v[i]==v[i-1]:
            cnt+=1
        else: #flush
            out="%s%d%c" %(out,cnt,v[i-1])
            cnt=1
        i+=1
    if cnt>0:
        out="%s%d%c" %(out,cnt,v[i-1])
    print out
    v=out
print len(v) # 5808…! bingo
print "fin du prg."
