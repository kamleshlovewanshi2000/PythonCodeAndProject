import json

x = '{"name":"Kamlesh", "lname":"Lovewanshi", "collage":"Truba Institute", "branch":"CSE"}'

d = json.loads(x)

print(d)
print(type(d))

# Now Perform Operations on Dictionary
for i in d:
    print(i,":",d[i])