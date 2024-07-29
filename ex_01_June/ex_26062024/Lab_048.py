class Dog():
    name = None
    id = None

    def __init__(self, name, id):
        self.name = name
        self.id = id

    # Constructor
    # basically used to initialise the values(attributes)
    def sleep(self):
        print("sleeping")


dog1 = Dog()
print(dog1.name)
dog1.name = "chow"
print(dog1.name)
dog1.sleep()


print("-------------------------")


dog2 = Dog
print(dog2.name)
dog2.name="Mow"
print(dog2.name)

