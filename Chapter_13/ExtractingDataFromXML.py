import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

serviceurl = input('Enter URL: ')
if len(serviceurl) < 1 :
    serviceurl = 'http://py4e-data.dr-chuck.net/comments_1641392.xml'
    print('Retrieving' , serviceurl)

#print(serviceurl)

#ignore SLL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen(serviceurl).read()
xml = ET.fromstring(html)

#print(xml)

commentcounts = xml.findall('.//count')

sum = 0
for count in commentcounts :
    sum = sum + int(count.text)

print('Sum:',str(sum))