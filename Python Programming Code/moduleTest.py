import myModule
import myModule as md
from myModule import mul
from myModule import *

n = int(input("Enter the value 1:"))
m = int(input("Enter the value 2:"))

# By using import myModule
# a = myModule.add(n,m)
# print("addition:",a)

# By Using import myModule as md
# s = md.sub(n,m)
# print("Subtraction:",s)

# By Using from myModule import mul
# print(mul(n,m))

# By Using from myModule import *
print("Addtion:",add(n,m))
print("Subtraction:",sub(n,m))
print("Multiplication:",mul(n,m))
print("Division",div(n,m))