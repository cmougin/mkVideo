# -*- coding: utf-8 -*-
"""
différents essais pour répondre au challenge:
    http://www.pythonchallenge.com/pc/return/cat.html
    http://www.pythonchallenge.com/pc/return/uzy.html
 called UZY
"""
#and its name is uzi. you'll hear from him later.
#le 26 janvier tombe en lundi une année du 20e siècle en 6
#le 1er un jeudi
#<!-- he ain't the youngest, he is the second -->
#<!-- todo: buy flowers for tomorrow -->

import calendar
print "début du programme..."

for i in range(100):
    annee=1006+i*10
    (d,n)=calendar.monthrange(annee,1)
    if d==3 and calendar.isleap(annee):
        print annee
#the yougest is 1976, so the second is 1756
#january 27th 1756 = 
print "fin du prg."