def num(n):
    if(n==0):
        return 0
    return n+num(n-1)
n=int(input("enter your number:"))
print(num(n))