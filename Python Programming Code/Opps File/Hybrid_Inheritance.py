"""
Hybrid Inheritance:
    Inheritance consisting of multiple types of
    inheritance is called hybrid inheritance.

                School
                  /\
                 /  \               ==> Type 1: Hierarchical Inheritance
        Student1     Student2
                        |
                    Student3
                        |           ==> Type 2: Multilevel Inheritance
                    Student4
                        |
                    Student5 (Student4,School)     ===> Type 3: Multiple Inheritance

"""

class School:
    def funSchool(self):
        print("School class Function Called")

class Student1(School):
    def funStudent1(self):
        print("Student1 class Function Called")

class Student2(School):
    def funStudent2(self):
        print("Student2 class Function Called")

class Student3(Student2):
    def funStudent3(self):
        print("Student3 class Function Called")

class Student4(Student3):
    def funStudent4(self):
        print("Student4 class Function Called")

class Student5(Student1,School):
    def funStudent5(self):
        print("Student5 class Function Called")

# Driver's Code
# Type 1: Hierarchical Inheritance
print("\nCalled by Student1 Class Object:----\n")
# Create Object of Student1
objS1 = Student1()
# Function called by objS1
objS1.funSchool()
objS1.funStudent1()

print(" \nCalled by Student2 Class Object:----\n")
# Create Object of Student2
objS2 = Student2()
# Function called by objS2
objS2.funSchool()
objS2.funStudent2()

# Type 2: Multilevel Inheritance
print("\nCalled by Student4 Class Object:----\n")
# Create Object of Student4
objS4 = Student4()
# Function called by objS4
objS4.funSchool()
objS4.funStudent2()
objS4.funStudent3()
objS4.funStudent4()

# Type 3: Multiple Inheritance
print("\nCalled by Student5 Class Object:----\n")
# Create Object of Student4
objS5 = Student5()
# Function called by objS5
objS5.funSchool()
objS5.funStudent1()
objS5.funStudent5()