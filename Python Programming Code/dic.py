# Create a dictionary
# d = {
#     "name": "Piyush",
#     "Roll":"0114CS18046",
#     "Batch": '2018-2022'
# }
# print(d,type(d))
# print(d["name"])
#
# for i in d:
#     print("Keys -",i,": Values -",d[i])
#
# print(d.get("name"))
# for j in d:
#     a = d.get(j)
#     print(a)
#
# for k in d.keys():
#     print(k)
# for l in d.values():
#     print(l)
# for a,b in d.items():
#     print(a,":",b)
#
# del d["name"]
# print(d)

# n = d.pop("Roll")
# print(n)
# print(d)
#
# d["roll"] = "46"
# print(d)
# d.update({"name":"Kamlesh"})
# print(d)
# d.clear()
# print(d)

 # Nested Dictionary

student = {
    "Piyush":{'Branch':"CSE","Roll":"46","Age":22},
    "Aditya":{'Branch':"CE","Roll":"07","Age":21},
    "Dev":{'Branch':"ME","Roll":"33","Age":20}
}
for i,j in student.items():
    print(i,":",j)

for k,l in student.items():
    print(k,":",l["Branch"],l["Roll"],l["Age"])

student["Dev"]["Branch"] = "CSE"
for i,j in student.items():
    print(i,":",j)

a = student.pop("Dev")
print(student)
print("Popped Item is:",a)
b = student["Aditya"].pop("Branch")

print(student)
print(b)

student["Aditya"]["Branch"] = "CSE"
print(student)