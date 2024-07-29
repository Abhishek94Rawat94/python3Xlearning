class Car:
    name = None
    make = None
    model = None

    def __init__(self, o_name, o_make, o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
        print("Starting a car with the name "+self.name)
        print("Starting a car with the make "+self.make)
        print("Starting a car with the model "+self.model)

swift=Car("Swift","vxi","2023")
swift.start_engine()

breeza=Car("Breeza","zxi","2024")
breeza.start_engine()


nexon=Car("Nexon","xz+","2019")
nexon.start_engine()