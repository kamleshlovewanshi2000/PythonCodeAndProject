'''
Single Inheritance:
    Single inheritance enables a derived class to inherit properties
    from a single parent class, thus enabling code re-usability and
    the addition of new features to existing code.
'''

# Create Base Class
class Base:
    def fun1(self):
        print("This function is called inside Base class")

# Create Drived class
class Drived(Base):
    def fun2(self):
        print("This function is called inside Drived class")


# Driver's Code
obj = Drived()
obj.fun1()
obj.fun2()
