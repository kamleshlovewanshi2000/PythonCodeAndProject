#Program to swap first
# and last element of a list
# Swap function

#l = [12,2,3,4,22]

'''
# type - 01
first, last = l[0], l[-1]
l[0],l[-1] = last, first
print(l)
'''
# Type - 02

# def listSwap(l):
#     get = l[-1], l[0]
#     l[0], l[-1] = get
#     print(get,type(get))
#     return l
#
# print(listSwap(l))


# Swap function
# def swapList(list):
#     start, *middle, end = list
#     list = [end, *middle, start]
#
#     return list
#
#
# # Driver code
# newList = [12, 35, 9, 56, 24]
#
# print(swapList(newList))


def swapList(list):
    first = list.pop(0)
    last = list.pop(-1)

    list.insert(0, last)
    list.append(first)

    return list

# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList))
