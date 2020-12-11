#$ python3 solution.py
#Enter URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
#Enter count: 4
#Enter position: 3
#Retrieving: http://py4e-data.dr-chuck.net/known_by_Fikret.html
#Retrieving: http://py4e-data.dr-chuck.net/known_by_Montgomery.html
#Retrieving: http://py4e-data.dr-chuck.net/known_by_Mhairade.html
#Retrieving: http://py4e-data.dr-chuck.net/known_by_Butchi.html
#Retrieving: http://py4e-data.dr-chuck.net/known_by_Anayah.html

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# definig our function
def phanta() :
    url = input('Enter url - ')
    if len(url) < 1:
        url = jtf
    posit = int(input('Enter position -'))
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        posit = posit-1
        if posit == 0:
            return tag.get('href',None)
        else:
            continue
cnt = int(input('Enter count -'))
while cnt > 0:
    cnt = cnt-1
    jtf = phanta()
    print(jtf)
