fname=input('Enter the file name: ')
fhand=open(fname)
wlist=list()
c1=dict()
for line in fhand:
    line=line.rstrip()
    if line.startswith("From"):
        if line.startswith('From:'):
            continue
        mail=line.split()
        words=mail[1]
        wlist.append(words)
for w in wlist:
    c1[w]=c1.get(w,0)+1
bignum=None
bigw=None
for gw,gn in c1.items():
    if bignum is None or gn>bignum:
        bignum = gn
        bigw = gw
print(bigw,bignum)