# Multi-Level Inheritance

class Grandparent:

    def grandparent_method(self):
        return "Grandparent's method"

class Parent(Grandparent):
    def parent_method(self):
        return "Parent's method"

class Child(Parent):
    def child_method(self):
        return "child's method"

child = Child()
child.child_method()
child.parent_method()
child.grandparent_method()

parent=Parent()
parent.parent_method()
parent.grandparent_method()

grandparent = Grandparent()
grandparent.grandparent_method()