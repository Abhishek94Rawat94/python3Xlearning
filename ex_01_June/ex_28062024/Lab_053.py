class Person():
    # class variables /instance variables
    name = "Abhi"
    age = input("Enter the age")

    def walk(self):
        a = 10  #local variable
        print("I am " + self.name)
        print("My age is " + self.age)


abhi = Person()
abhi.walk()
