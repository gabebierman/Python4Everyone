# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from unicodedata import name
import urllib.request, urllib.parse, urllib.error

import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input('Enter number of links to follow: '))
pos = int(input('Enter position of URL: '))



for iter in range(count) :  
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    #print('Connected to' , url)
    taglist=list()
    for tag in tags:
        #print(tag.get('href', None))
        x = tag.get('href', None)
        taglist.append(x)

    url = taglist[pos]

print(url)








# Retrieve all of the anchor tags


