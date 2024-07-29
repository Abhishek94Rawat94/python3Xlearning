# Inheritance
# Acquire the attributes and behaviour
# Data members and methods

# that allowed class child to inherit the attribute and method from the another class parents

# Types of Inheritance
# Single Inheritance - 80%
# Multiple Inheritance
# Multi-level Inheritance
# Hybrid
# Hierarchical


# Single Inheritance
class Grandfather:
    key = "abhi@123"

    def grandparent_method(self):
        return "grandparent's method"


class Father(Grandfather):

    def parent_method(self):
        return "parent's method"


parent = Father()
parent.parent_method()
parent.grandparent_method()
print(parent.key)
