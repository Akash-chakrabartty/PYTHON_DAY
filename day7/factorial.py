

def fectorial(i):
    n=1
    
    for i in range(i,1,-2):
        p=i*(i-1)
        n=n*p
        
    
    print(n)

i=int(input("enter n number:"))
fectorial(i)        