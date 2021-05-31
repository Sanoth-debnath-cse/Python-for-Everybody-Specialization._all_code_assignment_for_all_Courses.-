import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx =ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode = ssl.CERT_NONE

html=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_731537.html',context=ctx).read()
supe=BeautifulSoup(html,'html.parser')

tag=supe('span')
count=0
for i in tag:
    count+=int(i.contents[0])
print(count)