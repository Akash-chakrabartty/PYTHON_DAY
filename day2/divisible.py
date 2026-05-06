number= int(input("enter a number:"))
if number%3==0 and number%5==0:
    print(number,"is divisible by both 3 and 5")
elif number%3==0:
    print(number,"is divisible by only 3")
elif number%5==0:
    print(number,"is divisible by only 5")
else:    print(number,"is not divisible by either 3 or 5")
