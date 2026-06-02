from abc import ABC, abstractmethod
class BankApp(ABC):
    def database(self):
        print("connected to database")
    @abstractmethod
    def scurity(self):
        pass
    @abstractmethod
    def display(self):
        pass

class MobileApp(BankApp):
    def mobile_login(slef):
        print("login infoo mobile")
    
    def scurity(self):
        print("mobile security")
    
    def display(self):
        print("display")

obj=MobileApp()
obj.mobile_login()
