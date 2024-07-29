class VWOLogin:

    def __init__(self, email, password):
        self.__email = email
        self.__password = password

    def login_confirm(self):
        if self.__email == "abhi@gmail.com" and self.__password == "1234":
            print("Allowed")
        else:
            print("Not Allowed")


# This is end of the class

page1 = VWOLogin("abhi@gmail.com","1234")
page1.login_confirm()
# page1.__email="123"
# page1.__password="332"
