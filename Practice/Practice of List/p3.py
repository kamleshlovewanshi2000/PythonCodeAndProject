# Swap elements in String list

s = "lovewanshi"
tem = s.strip()
print(tem)
l = list(tem)
p1, p5 = 1, 5
l[p1], l[p5] = l[p5], l[p1]

s1 = str(l)
print("Original String:",s)
print("Swapped String by pos1 to pos5:",s1)

l2 = [12,5,6,4,]
s3 = str(l2)
print(s3)