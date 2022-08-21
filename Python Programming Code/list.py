# # l = [10,20,30,40,50,60]
# # n = len(l)
# #
# # # Slicing
# #
# # print(type(l[3]),l[3]) #40
# # print(type(l[0:4]),l[0:4]) # 10,20,30,40
# # print(l[0::2]) # 10,30,50
# #
# # # Reverse List
# # print(l[-5]) # 20
# # print(l[-1::-1]) # 60,50,40,30,20,10
# # print(l[-1::-2]) # 60,40,20
# #
# # # Iterate using for Loop
# # print("\n")
# # for i in range(n):
# #     print(l[i], end=" ")
# #
# # # Reverse list using for loop
# # print("\n")
# # for i in range(n-1,-1,-1):
# #     print(l[i],end=",")
# # print("\n")
# #
# # # Elements Access without using for loop or range() function
# # for i in l:
# #     print(i,end=" ")
#
# # Create a list using for loop
# l = []
# for i in range(1,21):
#     l.append(i)
# print(l)
#
# # Create a list using list comprehension
#
# n = [ i for i in range(1,11)]
# print(n,type(n))
#
# c = [i for i in range(1,51) if i%2 != 0 ]
#
# print("Even no. list : ",c)
#
# # # Create a list by usnig the String
#
# s = "Lovewanshi"
# l1 = list(s)
# print(l1)
# l2 = [i for i in s]
# print(l2),

# l = [10,20,30,40,50,60]
# del l[2]    # 30
# print(l)
#
# l.pop(0)
# print(l)
# print(l.pop(1))
# print(l)
#
# l.remove(60)
# print(l)
# l.clear()
# print(l)



# l = [10,20]
# l[1] = 100
# print(l)
# l.insert(1,30)
# print(l)
#
# l.append(50)
# print(l)
# n = ["KAMLESH", 46,47,49]
# l.append(n)
# print(l)
# ,
# l.extend(n)
# print(l)

# l = [10,50,60,80,12,10]
# l1 = ["Kamlesh", "Piyush", "Zon"]
#
# # count()
# print(l.count(10))
#
# # max()
# print(max(l))
# print(max(l1))
#
# # min()
# print(min(l))
# print(min(l1))
#
# # sort()
# l.sort()
# print(l)
#
# # reverse()
# l.reverse()
# print(l)

# m = [1,2,3,5,4,6]
# print(m.index(3))

# Iterate two list at the same time using zip() function

# a = [1,2,3,4,5]
# b = [10,20,30,40,50]
#
# for i,j in zip(a,b):
#     print(i,j)
# print("\f")
# for k in range(len(a)):
#     print(a[k], b[k])

# To convert string to a list

# Using split() method
# s = input("Enter a String :")
# print("given String is:",s)
#
# l = s.split()
# print("Converted string to list is:",l)

n = int(input("How many number of word you want to in your string :"))
l = []
for i in range(1,n+1):
    temp = input("Enter the value"+str(i)+":-")
    l.append(temp)
print(l)
