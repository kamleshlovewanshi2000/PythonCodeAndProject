import pickle

l = ["Kamlesh", 10, 102.30]

file1 = open("writeData.txt","wb")
pickle.dump(l, file1)
file1.close()