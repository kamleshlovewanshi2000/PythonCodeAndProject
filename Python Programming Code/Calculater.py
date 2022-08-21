print('''Calculater Operations are:
                        1. Addition
                        2. Subtraction
                        3. Multiplication
                        4. Division
                        5. Module
                        6. flore Division
            ''')

while True:
        num1 = int(input("Enter the value 1:- "))
        num2 = int(input("Enter the value 2:- "))
        opr = input("Enter the operator(+,-,*,/,%,//) :")

        if opr == "+":
            print(num1+num2)
        elif opr == "-":
            print(num1 - num2)
        elif opr == "*":
            print(num1 * num2)
        elif opr == "/":
            print(num1 / num2)
        elif opr == "%":
            print(num1 % num2)
        elif opr == "//":
            print(num1 // num2)
        else:
            print("Invalid Operations........")
        temp = input("If you want to end the calculater than Yes/No: ")
        if temp == "Yes" or temp == "yes":
            break
        else:
            continue