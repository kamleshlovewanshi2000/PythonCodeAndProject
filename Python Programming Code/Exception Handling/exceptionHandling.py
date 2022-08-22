#import maths
#from math import add

# Demonstrate Exception Handling

# 1: ZeroDivisionError: division by zero
try:
    a = int(input("Enter the value 1:"))
    b = int(input("Enter the value 2:"))
    div = a/b    # 10/0 : ZeroDivisionError: division by zero
    print(div)
except Exception as e:
    print("Please correct these Error:", e)

# 2: NameError: name 'div' is not defined
try:
    n1 = int(input("Enter the value 1:"))
    n2 = int(input("Enter the value 2:"))
    add = n1+n3     #NameError: name 'n3' is not defined
    print(add)
except Exception as error:
    print("Please correct these Error:",error)

# 3: ValueError: invalid literal for int() with base 10: "inputValue"
try:
    num = int(input("Enter the value:"))    # if user gives float and string value instead of int then it throw
    print("Square of",num,":",num**2)       #ValueError: invalid literal for int() with base 10: 're'
except Exception as error:
    print("Please gives the Integer Value...")

# 4: TypeError: unsupported operand type(s) for +: 'int' and 'str'
try:
    k = input("Enter the value 1:")
    l = input("Enter the value 2:")
    add = int(k)+(l)
    print("Add",add)
except Exception as error:
    print("Please correct these Error:", error)

# 5: IndexError: list index out of range
try:
    l = [10,20,30,40]
    for i in range(4,6):
        print("Value of Index",i,":",l[i])
except Exception as error:
    print("Please correct these Error:", error)

# 6: KeyError: 'name'
d = {"Name":"Piyush","Sname":"Singh","Fees":51000}
try:
    print("Name",d["Name"])
    print("Sname:",d["sname"])
except Exception as error:
    print("Please correct these Error:", error)
print("Fees:",d["Fees"])

"""
# 7:ModuleNotFoundError: No module named 'myModule'
a,b = 10,20
try:
    print(maths.sum(a,b))
except Exception as error:
    print("Please correct these Error:", error)
"""
"""
# 8:ImportError: cannot import name 'add' from 'math'
try:
    a,b = 10,20
    print(add(a,b))
except Exception as error:
    print("Please correct these Error:", error)
"""