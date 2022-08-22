class Constructor:
    x = 10
    y = 2
    # Create Constructor
    def __init__(self):
        print("Constructor Called!")

    # Create Function with arguments
    def mul(self,a,b):
        print("Multiplication:",a*b)

    # Use of self keyword
    def square(self):
        s = self.x**self.y
        print(s)
 # Driver's Code
obj = Constructor()
obj.mul(10,2)
obj.square()