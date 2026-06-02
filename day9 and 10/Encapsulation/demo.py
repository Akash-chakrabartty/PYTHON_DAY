class Demo:
    def __init__(self):
        self.name="public university"
        self._age=21
        self.__salary=50000
    def show(self):
        print("inside the class")
        print("public: ",self.name)
        print("protected: ",self._age)
        print("private :",self.__salary)

obj=Demo()
obj.show()