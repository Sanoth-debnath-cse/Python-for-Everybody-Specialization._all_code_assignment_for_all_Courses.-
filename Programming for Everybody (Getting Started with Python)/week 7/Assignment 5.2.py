large=None
mini=None
while True:
    num=input('Enter Number: ')
    if num=='done':
        break
    try:
        fnum=int(num)
    except:
        print('Invalid input')
        continue
    if mini is None:
        mini=fnum
    elif fnum<mini:
        mini=fnum
    elif large is None:
        large=fnum
    elif fnum>large:
        large=fnum
print('Maximum is',large)
print('Minimum is',mini)