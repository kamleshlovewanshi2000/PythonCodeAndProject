'''
Encapsulation:
     Encapsulation is one of the fundamental concepts in object-oriented
     programming (OOP). It describes the idea of wrapping data and the
     methods that work on data within one unit. This puts restrictions
     on accessing variables and methods directly and can prevent the
     accidental modification of data. To prevent accidental change,
     an object’s variable can only be changed by an object’s method.
     Those types of variables are known as private variables.

     A class is an example of encapsulation as it encapsulates all
     the data that is member functions, variables, etc.
'''
class Employee:
    # Private Data Member
    __empName = "Piyush"

    #Private Method
    def __displayInfo(self):
        print("Welcome to Truba!")

    # Constructor is used to show private data
    def __init__(self):
        print(self.__empName)
        self.__displayInfo()

obj = Employee()