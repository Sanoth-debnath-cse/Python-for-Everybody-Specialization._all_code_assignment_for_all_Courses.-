hrs= input("Enter Hours:")
rate= input("Enter Rate:")
hf= float(hrs)
rf= float(rate)
def computepay(hf,rf):
    if hf>40:
        a=40*rf
        b=(hf-40)*(rf*1.5)
        ans=a+b
        return ans
        #print(ans)
    else:
        x=hf*rf
        return x
        #print(hf*rf)
print("Pay",computepay(hf,rf))
