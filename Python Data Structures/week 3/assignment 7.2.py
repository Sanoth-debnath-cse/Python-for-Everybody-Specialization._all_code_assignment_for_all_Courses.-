file=input('Enter file name: ')
fhand=open(file)
c1=0
store=0
avg=0
for line in fhand:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        c1=c1+1
        data=line.find(':')
        data2=line[data+1:]
        c2=float(data2)
        store=store+c2
avg=float(store/c1)
print('Average spam confidence:',avg)