class Student:
    def __init__(self):
        self.__name = ""
    def setname(self,name):
        self.__name = name
    def getname(self):
        return "Your Name: "+self.__name

# Driver's Code
obj = Student()
n = input("What is your name? :")    # Taking Input From User
obj.setname(n)          # Set value in private member
name = obj.getname()    # Get value of private member
print(name)             # Print the value