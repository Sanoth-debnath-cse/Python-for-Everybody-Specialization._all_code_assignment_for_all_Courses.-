import re
handle=open('regex_sum_731535.txt')
sumlst=[]
for line in handle:
    line=line.rstrip()
    lst=re.findall('([0-9]+)',line)
    if len(lst)>0:
        for i in lst:
            num=int(i)
            sumlst.append(num)
print(sum(sumlst))