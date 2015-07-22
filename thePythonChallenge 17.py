# -*- coding: utf-8 -*-
"""
différents essais pour répondre au challenge:
    http://huge:file@www.pythonchallenge.com/pc/return/romance.html
"""
#<title>eat?</title>

print "début du programme..."

#on va ramasser les miettes de cookies depuis l'épisode 4, avec son
#enchainement de nombre jusqu à obtenir le mot clé PEAK à la 400e position
#mais si on part avec "nothing" un cookie nommé "info" est retourné avec: 
#"you+should+have+followed+busynothing..."

from urllib2 import build_opener, HTTPCookieProcessor
import cookielib, re, urllib, bz2

cj = cookielib.CookieJar()
opener = build_opener(HTTPCookieProcessor(cj))

next_nothing = '12345'
solution4 = ''
solution17 = ''
solution17='BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90'
i = 0
if not solution17:
  while i < 400 and not solution4:
    i += 1
    u = opener.open('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='+next_nothing)
    for cookie in cj:
        print cookie
        solution17 += "%s"%(cookie.value)
    page = u.read()
    match = re.search('and the next \w*nothing is (\d+)',page)
    if match:
        next_nothing = match.group(1)
        print next_nothing
        
    else:
        solution4 = page
  print 'Solution4: '+page

print 'Solution17: ', solution17
unquoted=urllib.unquote_plus(solution17) 
print bz2.decompress(unquoted)

print "fin du prg."