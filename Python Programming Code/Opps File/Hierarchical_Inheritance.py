'''
Hierarchical Inheritance:
    When more than one derived class are created from a single
    base this type of inheritance is called hierarchical inheritance.
    In this program, we have a parent (base) class and two child (derived) classes.
'''

# Base Class (Parent)
class Parent:
    def funParent(self):
        print("This is Parent class")

class Child1(Parent):
    def funChild1(self):
        print("This is Child1 Class")

class Child2(Parent):
    def funChild2(self):
        print("This is Child2 Class")

# Driver's code
child1obj = Child1()        # Child1 Object is Created
child1obj.funParent()
child1obj.funChild1()
print()
child2obj = Child2()        # Child2 Object is Created
child2obj.funChild2()
child2obj.funParent()