import urllib.request,urllib.parse,urllib.error
import json
service_url='http://py4e-data.dr-chuck.net/json?'
api_key=42
while True:
    address=input()
    if len(address)<1:
        break
    dicto={}
    dicto['address']=address
    dicto['key']=api_key
    
    url=service_url+urllib.parse.urlencode(dicto)
    print(url)
    handle_url=urllib.request.urlopen(url).read()
    data=handle_url.decode()
    print(len(data))
    try:
        info=json.loads(data)
    except:
        info=None
    if not info or 'status' not in info or info['status']!='OK':
        print('fail')
        print(info)
        continue
    #print(json.dumps(info,indent=4))
    place_id=info['results'][0]['place_id']
    print(place_id)