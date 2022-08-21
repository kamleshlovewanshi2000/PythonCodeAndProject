#  *** Random Number Guessing Game ***

import random

n = int(input("Enter Your Number:"))
c = random.randrange(1,101)
print("Computer Number:",c)

if n>c:
    print("Your Guess Number is Too High!")
elif n==c:
    print("Your Guess Number is Equals!")
else:
    print("Your Guess Number is Too Low!")