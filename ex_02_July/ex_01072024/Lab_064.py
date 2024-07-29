# Hierarchical Inheritance
# Single parent multiple children

class Father:

    def Bhk1(self):
        print("1bhk")


class Abhi(Father):
    def Bhk2(self):
        print("2bhk")


class Ashu(Father):
    def Bhk3(self):
        print("3bhk")


class Abhishek(Father):
    def No_house(self):
        print("No house")


abhi = Abhi()
abhi.Bhk1()
abhi.Bhk2()


ashu = Ashu()
ashu.Bhk1()
ashu.Bhk3()


abhishek = Abhishek()
abhishek.Bhk1()
abhishek.No_house()
