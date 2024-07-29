# Multiple Inheritance

class Father:

    def father_money(self):
        return "5"

    def home(self):
        return "This is from the father"

class Mother:

    def mother_monehy(self):
        return "2"

    def home(self):
        return "This is from the mother"


class Son(Father,Mother):
    def home(self):
        return "This is from the son"

son = Son()
print(son.father_money())
print(son.mother_monehy())
print(son.home())