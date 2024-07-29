# Web automation-selenium
# Page-you are going to automate

class VWOLoginPage:
    email = None
    password = None

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login_confirm(self):
        if self.password == "pass123":
            print("You are allowed")
        else:
            print("You are not allowed")


# This is end of the class

abhi = VWOLoginPage("abhi@123", "pass123")
abhi.login_confirm()

ashu = VWOLoginPage("abhi@123", "pass")
ashu.login_confirm()
