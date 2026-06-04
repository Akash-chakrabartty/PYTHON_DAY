
def decorator(func):
    def wrapper(x,y):
        print("adding value :")
        func(x,y)
        print("thank you")
    return wrapper
       

@decorator
def add(a,b):
    print(f"the addition is :{a+b}")


add(25,26)