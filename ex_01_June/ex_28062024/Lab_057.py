class Car:
    name = None

    def __init__(self):
        self.public_variable = "public"
        self._protected_variable = "protected123"
        self.__private_variable = "private12345"

    def __private_method(self):
        print("protected!")

    def print_name(self):
        if self.__private_variable == "private12345":
            print("Hi, private12345")
        else:
            print("I am allowed in public")


# This is the end of the class

alto = Car()
alto.print_name()
