# Method over riding same method name in parent and child class
# Super is use to call parent class method otherwise it will always execute child class first

class Father:
    def home(self):
        print("2bhk")

class Child(Father):
    def home(self):
        super() .home()
        print("3bhk")

child=Child()
print(child.home())