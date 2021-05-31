fname=input('Enter a file name:')
fhand=open(fname)
wlist=list()
for line in fhand:
    line=line.rstrip()
    words = line.split()
    for w in words:
        if w not in wlist:
            wlist.append(w)
            wlist.sort()
print(wlist)
