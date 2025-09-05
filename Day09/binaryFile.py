with open("file3.dat","wb") as fp:
    fp.write(b"Hello World")

with open("file3.dat","rb") as fp:
    data = fp.read()
    print(data)

with open("file3.dat","rb+") as fp:
    data = fp.read()
    print(data)
    fp.write(b"\nMy name is UB.\n")
    fp.seek(0)
    newData = fp.read()
    print(newData)