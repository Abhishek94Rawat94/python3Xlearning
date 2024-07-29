# Polymorphism

class Shape:

    def area(self):
        print("Area of the shape")

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius


rect=Rectangle(3,6)
print(rect.area())

cir=Circle(3)
print(cir.area())

