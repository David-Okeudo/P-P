import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter url: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_756632.xml'
data = urllib.request.urlopen(url, context=ctx).read()
#print(data.decode())
tree = ET.fromstring(data.decode())
lst = tree.findall('comments/comment')
byt = list()
for item in lst:
    byt.append(int(item.find('count').text))
print(sum(byt))
