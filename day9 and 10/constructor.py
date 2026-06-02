class Animal:
    def __init__(self,name):
        self.name=name
    def hello(self):
        print(f"Hello your name is: {self.name}")

class Human(Animal):
    pass
obj=Animal("lion")
obj2=Human("Akash")

print(obj.hello())
print(obj2.hello())