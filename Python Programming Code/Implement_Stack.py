l = []

while True:
    print(""" Stack Operations are:
          1: Push
          2: Pop
          3: Peak
          4: Display Stack
          5: Exit
          """)
    c = int(input("Which operation you want to perform: "))

    if c == 1:
        n = input("Enter the value in stack: ")
        l.append(n)
        print(l)
    elif c == 2:
        if len(l) == 0:
            print("Stack is Empty!")
        else:
            p = l.pop()
            print(p)
            print(l)
    elif c == 3:
        if len(l) == 0:
            print("Stack is Empty!")
        else:
            print("Your Stack is: ",l)
            print("Peak element of Stack is :",l[-1])
    elif c == 4:
        print("Display Stack :",l)
    elif c == 5:
        print("You are Exit from the Stack")
        break
    else:
        print("Please choose right Operation....")