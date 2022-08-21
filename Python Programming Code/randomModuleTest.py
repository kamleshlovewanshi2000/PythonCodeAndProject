import random

# randint() Method return a number between 1 and 5 (both included)
# print(random.randint(1,5))

# randrange() Method return a number between 5 (Included) and 10 (not included)
# print(random.randrange(5,10))

# choice() Method returns an element of list and tuple
# l = ["Piyush", "Rohit", "Vishal"]   # This is List
# print(random.choice(l))
# t = (10,20,30,40)
# print(random.choice(t))   # This is Tuple

# random() Method returns a random float number between 0 and 1
# n = random.random()
# print(n)

# shuffle() Method Takes a sequence and return the sequence in a random order
# l = [10,20,30,40,50,60]
# random.shuffle(l)
# print(l)

# uniform() Method return a random float number between two given parameters
u = random.uniform(5,10)
print(u)