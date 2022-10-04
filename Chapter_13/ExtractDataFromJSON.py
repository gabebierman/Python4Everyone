import json
import re
import urllib.request, urllib.parse, urllib.error
import ssl

#for item in info:
#    print('Name', item['name'])
#    print('Id', item['id'])
#    print('Attribute', item['x'])

#ignore SLL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
if len(url) < 1 :
    url = 'http://py4e-data.dr-chuck.net/comments_1641393.json'
    print('Retrieving' , url)

uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data))

try :
    js = json.loads(data)
except :
    js = None

#print(json.dumps(js, indent=4))

comment_count = len(js['comments'])
print('Count:',comment_count)

comment_sum = 0

for comment in js["comments"]:
    comment_sum = comment_sum + int(comment["count"])
print(comment_sum)
    

