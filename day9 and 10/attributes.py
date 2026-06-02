class Car:
    wheels=4 #class attribute
    def __init__(self,color):
        self.color=color #instance attribute
obj=Car("blue")
print(obj.color)