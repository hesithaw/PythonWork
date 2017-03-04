#!/usr/bin/python

from urllib2 import Request, urlopen, URLError
import sys
import html
import requests

f1=open('out2.txt', 'w+')
link = "https://www.python.org/"
req = requests.get(link)
the_page = req.text
print >> f1, the_page
f1.close()
