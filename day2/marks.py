number=int(input("enter the number of subjects:"))
if number<0 or number>100:
    print("invalid input")
elif number>=90:
    print( " O grade")
elif number>=80:
    print("E grade")
elif number>=70:
    print("A grade")
elif number>=60:
    print("B grade")
elif number>=50:
    print("C grade")
elif number>=40:
    print("D grade")
else:    print("F grade")