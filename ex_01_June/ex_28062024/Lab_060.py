class BankAccount:

    def __init__(self):
        self.balance = 0
        self.__private_var = 1000

    def public_func(self):
        print(self.__private_var)

    def deposit(self,amount):
        self.balance += amount

    def __withdraw(self,amount):
        self.balance -= amount

    def __show_balance(self):
        print("your balance is ", self.balance)

    def if_you_are_auth(self,flag):
        if flag:
            self.__show_balance()
        else:
            print("Not Allowed")

    def if_you_are_auth_user(self,auth,amount):
        if auth:
            self.__withdraw(amount=amount)
        else:
           print("Not allowed")


hdfc = BankAccount()
hdfc.deposit(2000)

secret_pass=input("Enter the paswword")
if secret_pass == "3214":
        hdfc.if_you_are_auth(True)
else:
        hdfc.if_you_are_auth(False)
# hdfc.if_you_are_auth_user(True,199)
# hdfc.if_you_are_auth(True)