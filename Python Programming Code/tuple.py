t = (10,20,3,30,10,40)
print(type(t),t)

print(t[2])

for i in range(len(t)):
    print(i,":",t[i])

for i in t:
    print(i)
print("Minimum:",min(t))
print("Maximum:",max(t))
print('Count of 10:',t.count(10))
print("Index of 40 is:",t.index(40))
print("Sum of Tuple is :",sum(t))