# To demonstrate Overloading Concept
class Area:
    def findArea(self,a=None,b=None):
        if a != None and b != None:
            print("Area:",a*b)
        elif a != None:
            print("Area:",a*a)
        else:
            print("Nothing")

# Driver's Code
obj = Area()
obj.findArea(10,20)
obj.findArea(10)
obj.findArea()