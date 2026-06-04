def even(x):
    if x%2==0:
        return True
    else:
        return False
a=[1,2,3,4,5,6,7,8,9]
result=filter(even,a)
print(list(result))


b=[3,4,5,6,7,8,9,10,11,12,13,14,15]
result=filter(lambda x:True if x%2==0 else False,b)
print(list(result))