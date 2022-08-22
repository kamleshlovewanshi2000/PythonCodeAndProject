# To demonstrate Overriding Concept
class A:
    def showData(self):
        print("I'm in Class A")

class B(A):
    def showData(self):
        print("I'm in Class B")
        # If you want to access Class A showData()
        # function then we use super() function
        # super().showData()

# Driver's Code
obj = B()
obj.showData()