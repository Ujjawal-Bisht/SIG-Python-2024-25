#File - Collection of data

#Eg- text, binary, csv, json, pdf

"""
r - read- if the file does not exist, it will generate some error.
w - write- if the file does not exist, it will create a new file.
    if the file exists, it will overwrite the existing file.
a - append- if the file does not exist, it will create a new file.
    if the file exists, it will append the data to the existing file.
"""
"""
pf = open("file1.txt","w")
pf.write("Hello World My name is UB.\n")
pf.writelines(["Hello","World","!","My names"])
pf.flush()
pf.close()

fp = open("file1.txt","r")
data = fp.read(3)
data2 = fp.readline()
data3 = fp.readlines()
print(data)
print(data3)

print(fp.tell())
fp.seek(0)
data3 = fp.readlines()
print(data3)

print(fp.tell())
fp.close()
"""
'''
f = open("file1.txt","w")
f.write("Hello World My name is UB.\n")
f.writelines(["Hello","World","!","My names"])
f.flush()
f.close()

f = open("File1.txt","a")
print(f.tell())
f.write("Hello World My name is UB.\n")
f.writelines(["Hello","World","!","My names"])
f.flush()
f.close()

"""
r+ -> read and write
w+ -> write and read
a+ -> append and read
"""

f = open("file2.txt","w+")
'''
            
f = open("file1.txt","a+")
data = f.read()
print(data)
f.close()

with open("file1.txt","r") as f:
    data = f.read()
    print(data)
