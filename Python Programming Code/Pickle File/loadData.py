import pickle

file1 = open("writeData.txt","rb")

l = pickle.load(file1)
print(l)