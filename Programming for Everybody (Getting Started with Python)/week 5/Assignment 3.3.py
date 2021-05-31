score = input("Enter Score: ")
sin = float(score)
if sin>1.0:
    print("Error")
elif sin>=0.9:
    print("A")
elif sin>=0.8:
    print("B")
elif sin>=0.7:
    print("C")
elif sin>=0.6:
    print("D")
else:
    print("F")