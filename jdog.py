import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter url: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_756633.json'
data = urllib.request.urlopen(url, context=ctx).read()
info = json.loads(data)
#print('User count:', len(info))
byt = list()
for item in info["comments"]:
    byt.append(int(item.get("count")))
print(sum(byt))
