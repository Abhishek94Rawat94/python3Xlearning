class Person():
    # Attributes
    name = None
    id = None
    age = None
    phone_number = None

    # Behaviour
    def talk(self):
        print("i can talk")

    def another(self):
        print("I m another method")

    def sleep(self, name):
        print("I m a method")
        print("sleep", name)

    def walk(self):
        print ("I am walking")


# Create Objects
# Object reference = Object --> Class_name()
surya = Person()
surya.name="surya prakash"
surya.talk()


abhi = Person()
abhi.name="Abhishek Rawat"
abhi.walk()
print("")
