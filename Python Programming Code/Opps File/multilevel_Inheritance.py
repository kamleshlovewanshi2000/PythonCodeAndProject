'''
Multilevel Inheritance :
        In multilevel inheritance, features of the base class
        and the derived class are further inherited into the
        new derived class. This is similar to a relationship
        representing a child and a grandfather.
'''

class A:
    def funA(self):
        print("Class A Function is Called")

class B(A):
    def funB(self):
        print("Class B Function is Called")

class C(B):
    def funC(self):
        print("Class C Function is Called")

# Driver's Code

obj = C()

obj.funA()
obj.funB()
obj.funC()