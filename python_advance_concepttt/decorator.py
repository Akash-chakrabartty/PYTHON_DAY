
def decorator(func):
    def wrapper():
        print("before print")
        func()
        print("after print")
    return wrapper
       

@decorator
def hello():
    print("hello i am Akash Chakrabartty")


hello()