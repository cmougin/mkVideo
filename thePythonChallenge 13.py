# -*- coding: utf-8 -*-
"""
différents essais pour répondre au challenge:
    http://www.pythonchallenge.com/pc/return/disproportional.html
    http://www.pythonchallenge.com/pc/phonebook.php
"""

#call him
#phone that evil

import xmlrpclib

################################################
## cett partie ci n'est nécessaire que pour passer le proxy  
import urllib2
class ProxyTransport(xmlrpclib.Transport):
    def request(self, host, handler, request_body, verbose):

        self.verbose = verbose
        url = 'http://' + host + handler
        if self.verbose: "ProxyTransport URL: [%s]" % url

        request = urllib2.Request(url)
        request.add_data(request_body)
        request.add_header("User-Agent", self.user_agent)
        request.add_header("Content-Type", "text/xml")

        proxy_handler = urllib2.ProxyHandler({"http":"proxy.priv.atos.fr:3128"})
        opener = urllib2.build_opener(proxy_handler)

        f = opener.open(request)

        return(self.parse_response(f))

p = ProxyTransport()
###################################################

print u"debut du programme"
proxy = xmlrpclib.Server("http://www.pythonchallenge.com/pc/phonebook.php", transport=p)
#version sans proxy:
#proxy = xmlrpclib.Server("http://www.pythonchallenge.com/pc/phonebook.php")

print proxy.phone("Bert") # => 555-ITALY
print proxy.phone("Leopold")

print "fin du prg."
