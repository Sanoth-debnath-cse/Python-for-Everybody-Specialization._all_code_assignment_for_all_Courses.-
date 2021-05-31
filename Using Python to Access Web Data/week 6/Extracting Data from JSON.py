import urllib.request,urllib.parse,urllib.error
import json

data=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_731540.json').read()
info=json.loads(data)
sum=0
for i in info['comments']:
    c=int(i['count'])
    sum+=c
print(sum)