import json

x = [{"name": "Kamlesh", "lname": "Lovewanshi", "collage": "TIEIT", "branch": "CSE"},
     {"name": "Piyush", "lname": "Singh", "collage": "SIRT", "branch": "ECE"}
     ]
y = json.dumps(x)
file = open("post.json", "w")
f = file.write(y)

file.close()
