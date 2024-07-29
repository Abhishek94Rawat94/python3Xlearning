# Encapsulation
# Wrapping / bind the data variables with the methods
# Methods-def function with in the class
# Wrapping or binding the data variables with methods - Encapsulation

class Car:
    name=None
    password="123"

    def __init__(self):
        print("I am called when object is created")

    def change_password(self):
        self.password="123"

# The class ends here

xuv = Car()
xuv.password = "123"
#  OR
#xuv.change_password()
