number=[1,4,9,16,25,36,49,64,81,100]
n=int(input("Enter a number among (1,4,9,16,25,36,49,64,81,100) :"))
index=0
while index<len(number):
    if (number[index]==n):
        print("the number is found at index",index)
        break
    else:
        print("finding the number...")
    index+=1