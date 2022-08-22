# Demonstrate Bike Rental System
"""
1. Display Available Bikes
2. Request a Bike for Rent(100 INR --> 1 Qty)
3. exit
"""
class BickShop:

    def __init__(self,stock):
        self.stock = stock

    def displayAvailableBike(self):
        print("Total available Bike:",self.stock)

    def rentForBike(self,q):
        if q<=0:
            print("Enter the positive Number or Greater then zero(0):")
        elif q>self.stock:
            print("Enter the Value (Less then Stock):")
        else:
            self.stock -= q
            print("Total Prices for Bike Rent:", q*100)
            print("Total Bikes Available in stock:",self.stock)

while True:
    obj = BickShop(100)
    uc = int(input("""
    1. Display Available Bikes
    2. Request a Bike for Rent(100 INR --> 1 Qty)
    3. exit
    :-"""))
    if uc == 1:
        obj.displayAvailableBike()
    elif uc == 2:
        n = int(input("Enter the Quantity of Bike:---"))
        obj.rentForBike(n)
    else:
        print("Your Exit!....")
        break