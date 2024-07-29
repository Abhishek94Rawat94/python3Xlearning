class dog():
    name = None
    id = None

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def sleep(self):
        print("Who is sleeping-->"+self.name)


dog1 = dog("Chow", 1)
dog2 = dog("Mow", 2)
print(f'{dog1.name} id is {dog1.id}')
print(f'{dog2.name} id is {dog2.id}')
dog1.sleep()
dog2.sleep()

