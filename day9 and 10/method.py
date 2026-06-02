class Animal:
    name="Lion" #class attribute
    def __init__(self,age):
        self.age=age #instance attribute
    def show(self):
        print(f"your age is {self.age}")

    @classmethod
    def hello(cls):
        print("how are you brother")
    @staticmethod
    def static():
        print("how are you")

obj=Animal(12)
obj.show()
obj.static()
obj.hello()

