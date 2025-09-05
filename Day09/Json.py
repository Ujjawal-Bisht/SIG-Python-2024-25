import json

with open("file3.json") as f:
    data = json.load(f)
    print(data)
    print(type(data))
    print(data["Address"]["State"])
    data["Address"]["State"] = "UP"
    print(data)

newData = {
    "Name":"UB",
    "Age":21,
    "Address": {
        "City":"East Delhi",
        "State":"Delhi"
    }
}
with open("file3.json","w") as f:
    json.dump(newData,f)