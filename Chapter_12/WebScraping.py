

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")


sum = 0

tags = soup('span')
for tag in tags:
    
    stuff = re.findall('[0-9]+' , str(tag))
    for integer in stuff :
        sum = sum +float(integer)
   


print(str(sum))
    


