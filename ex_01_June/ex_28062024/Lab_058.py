class MyClass:

    def __init__(self):
        self.name = "Abhi"

    def public_function(self):
        print("Public Function()")

    def __private_function(self):
        print("This is private")

    def public_fun_private(self):
        self.__private_function()

a=MyClass()
a.public_function()
a.public_fun_private()

