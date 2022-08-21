l = []
while True:
    print("""
          Queue Operations are:
          1. Push Elements
          2. Pop First Elements
          3. Front Elements
          4. Rear Elements
          5. Display Queue
          6. Exit From Queue
          """)
    c = int(input("Please choose the Operation would you want:"))

    if c == 1:
        n = input("Enter the value in Queue:")
        l.append(n)
        print(l)
    elif c == 2:
        if len(l) == 0:
            print("Queue is Empty!")
        else:
            print(l)
            del l[0]
            print("First element of Queue is popped")
            print(l)
    elif c == 3:
        if len(l) == 0:
            print("Queue is Empty!")
        else:
            print(l)
            print("Front Element of Queue is:",l[0])
    elif c == 4:
        if len(l) == 0:
            print("Queue is Empty!")
        else:
            print(l)
            print("Rear element of Queue is:", l[-1])

    elif c == 5:
        print("Your Queue is :",l)
    elif c == 6:
        print("You are exit from the Queue!")
        break
    else:
        print("Invalid Operations....")
