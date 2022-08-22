'''
Multiple Inheritance:
    When a class can be derived from more than one base class
    this type of inheritance is called multiple inheritances.
    In multiple inheritances, all the features of the base
    classes are inherited into the derived class.
'''

# Python program to demonstrate
# multiple inheritance

# Base class1
class Mother:
    mothername = ""
    def mother(self):
        print(self.mothername)

class Father:
    fathername = ""
    def father(self):
        print(self.fathername)

class Son(Mother,Father):
    def perents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)

# Driver's Code

obj = Son()
obj.fathername = "Mr. Kanhaiyalal"
obj.mothername = "Mrs. Rambharosi"
obj.perents()