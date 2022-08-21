def welcome():
    print("Welcome to Truba!")

welcome()

def sumData(a,b):
    print("Sum:",a+b)

n1 = int(input("Enter the value 1:"))
n2 = int(input("Enter the value 2:"))
sumData(n1,n2)

def dataSum(i,j=10):
    print(i+j)

dataSum(100,20)

def returnFun(a,b):
    mal = a*b
    return mal

returnFun(5,3)
print("Value returned by returnFun():",returnFun(6,3))