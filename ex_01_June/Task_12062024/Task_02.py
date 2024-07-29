#Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).

#Use an if-else statement to classify the triangle.

side1 = int(input("Enter the side 1"))
side2 = int(input("Enter the side 2"))
side3 = int(input("Enter the side 3"))

if (side1 != side2) and (side1 != side3) and (side3 != side2):
    print("The triangle is scalene")
elif (side1 == side2) and (side1 == side3):
    print("The triangle is equilateral")
else:
    print("Triangle is isosceles")