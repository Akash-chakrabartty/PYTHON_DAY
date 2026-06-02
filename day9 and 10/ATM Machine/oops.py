class AtmMachine:
    def __init__(self):
        self.pin=0
        self.balance=0
        self.menu()
    def menu(self):
        user_input= int(input(" Hi how can i help you? \n1.press 1 to create pin\n2.press 2 to change pin\n3.press 3 to check banance\n4.press 4 to withdraw\n5.Anything to exit "))
        
        if user_input ==1:
            self.create_pin()
        elif user_input==2:
            self.change_pin()
        elif user_input==3:
            self.check_balance()
        elif user_input==4:
            self.withdraw_balance()
        else:
            exit()

    def create_pin(self):
        user_pin=input("Enter your pin: ")
        self.pin=user_pin
        user_balance=int(input("Enter Balance"))
        self.balance=user_balance
        print("pin cleated sucessfully!")
        self.menu()

    def change_pin(self):
        old_pin=input("enter your old pin :")
        if (old_pin==self.pin):
            new_pin=input("Enter new pin:")
            self.pin=new_pin
            print("pin changed sucessfully!")
            self.menu()
        else:
            print("invalid pin !")
            self.menu()
    
    def check_balance(self):
        user_pin=input("Enter  your pin :")
        if (user_pin==self.pin):
            print(f"your banalce is {self.balance}")
        else:
            print("your pin is incorrect, please try again!")
        self.menu()
    def withdraw_balance(self):
        user_pin=input("Enter your pin:")
        if (user_pin==self.pin):
            amount=int(input("Enter the amount:"))
            if (amount<=self.balance):
                self.balance=self.balance-amount
                print(f"you have withdraw {amount} your new balance is {self.balance}")
            else:
                print("insufficient balance!")
        else:
            print("your pin is incorrect please try again")
        self.menu()
islamibanl=AtmMachine()
