# Definition:
"""
Polymorphism:
    Polymorphism means same function name( but different signatures)
    being uses for different types.

    Like Python len() function is used for different types like list, tuple, str etc...
"""
# Overloading Concept
# Python Program to demonstrate in-built polymorphic functions
"""
# len() being used for a String
print(len("Welcome"))

# len() being used for a List
l = [10,20,30,40]
print(len(l))
"""

# User-defined polymorphic functions
"""
def add(x, y, z=0):
    return x + y + z
# Driver code
print(add(3, 3))
print(add(2, 3, 2))
"""
# Polymorphism with class methods:
"""
class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")


class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
"""

# Overriding Concept
class A:
    def showData(self):
        print("This function is called inside Class A")

class B(A):
    def showData(self):
        print("This function is called inside Class B and override the function of Class A")
        super().showData()
# Driver's Code
obj = B()
obj.showData()