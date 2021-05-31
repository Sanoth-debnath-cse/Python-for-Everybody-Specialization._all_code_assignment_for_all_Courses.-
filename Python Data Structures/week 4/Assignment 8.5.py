fname=input('Enter the file name: ')
fhand=open(fname)
c1=0
for line in fhand:
    line=line.rstrip()
    if line.startswith("From"):
        if line.startswith('From:'):
            continue
        mail=line.split()
        print(mail[1])
        c1=c1+1
print("There were",c1,"lines in the file with From as the first word")