class Parent:
    gold= "2KG"
    def Bhk2(self):
        return "2bhk"

class Child(Parent):

    def Bhk3(self):
        return "3Bhk"

child_object = Child()
print(child_object.Bhk3())
print(child_object.Bhk2())
print(child_object.gold)
