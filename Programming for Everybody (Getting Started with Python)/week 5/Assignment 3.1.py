hrs= input("Enter Hours:")
rate= input("Enter Rate:")
hf= float(hrs)
rf= float(rate)
if hf>40:
    a=40*rf
    b=(hf-40)*(rf*1.5)
    ans=a+b
    print(ans)
else:
    print(hf*rf)