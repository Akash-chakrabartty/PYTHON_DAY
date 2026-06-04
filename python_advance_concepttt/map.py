numbers=[1,2,3,4,5]
doubled=map(lambda x:x*2,numbers)
print(list(doubled))

a=[2,3,4,5,6]
def double(x):
    return x*2
result=map(double,a)
print(list(result))