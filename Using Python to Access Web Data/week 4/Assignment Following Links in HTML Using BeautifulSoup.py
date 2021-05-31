import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

herf_list=[]
last_name=[]
url=input()
count=int(input())
positions=int(input())
no_ittaretions=0
while no_ittaretions !=count:
    no_ittaretions+=1
    html=urllib.request.urlopen(url).read()
    soup=BeautifulSoup(html,'html.parser')
    tags=soup('a')
    for tag in tags:
        herf_list.append(tag.get('href',None))
        last_name.append(tag.contents[0])

    url=herf_list[positions-1]
    #print(herf_list[positions-1])
    name=last_name[positions-1]
    herf_list=[]
    last_name=[]
print(name)
