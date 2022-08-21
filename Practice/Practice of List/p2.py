# Python program to swap two elements in a list

l = [10,20,30,40,50,60]

a ,b, *c, d,e = l
l = [d,e,*c,a,b]

print(l)