s = {10,20,30,40,50}
print(s,type(s))

for i in s:
    print(i)

s.add(60)
print(s)
print(s.pop())
print(s.pop())
print(s)
s.remove(10)
print(s)
s.discard(60)
print(s)
l = [10,20,30,40,50]
s.update(l)
print(s)

s.clear()
print(s)
s.update(l)
print(s)
s.discard(60)
print(s)