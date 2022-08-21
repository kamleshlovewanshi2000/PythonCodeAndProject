import  json

d = {"name":"Kamlesh",
     "lname":"Lovewanshi",
     "collage":"Truba Institute",
     "branch":"CSE"}

j = json.dumps(d)

print(j)
print(type(j))
