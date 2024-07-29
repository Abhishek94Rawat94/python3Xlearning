class dog():
    name = None
    id = None

    def __init__(self, name=None, id=None):
        self.name = name
        self.id = id

    def sleep(self):
        print("Who is sleeping-->"+self.name)


dog1 = dog("Chow", 1)
dog2 = dog()
print(dog1.name)
print(dog1.id)
print(dog2.name)
print(dog2.id)