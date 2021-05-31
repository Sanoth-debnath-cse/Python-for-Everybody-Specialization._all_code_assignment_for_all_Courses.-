import urllib.request, urllib.parse,urllib.error
import xml.etree.ElementTree as ET

data=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_731539.xml').read()
tree= ET.fromstring(data)
lt=tree.findall('comments/comment')
print(len(lt))
sumof=0
for i in lt:
    sumof+=int(i.find('count').text)
print(sumof)