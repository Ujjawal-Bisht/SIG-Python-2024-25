# List- mutable, ordered, duplicates allowed
# String- immutable, ordered, duplicates allowed

l = [1,2,3,4,5]
l.append([1,2,34])
l.extend([7,8,9])
print(l)

print(l[1:4])

# Tuple- immutable, ordered, duplicates allowed

t1 = (1,2)
t2 = tuple()
print(t1.count(1))
print(len(t1))
# max,min, index, count, sorted, reversed, all,
# any, sum, sorted(t1), max(t1), min(t1), t1.index(2)

t = tuple(l)
print(t)

print(list(t1))


# Set- unordered, mutable, no duplicates allowed
s1 = {1,2,3,4,5}
print(s1)
s2 = {1,2,3,1}
#print(s2)

s1.add(6)
#print(s1)

s1.remove(2)
#print(s1)

s1.discard(2)
#print(s1)
'''
s1.pop()
print(s1)

s1.clear()
print(s1)


s3 = {1,2,3,4,5}
s4 = {4,5,6,7,8}
s5 = s3.union(s4)
print(s5)

s6 = s3.intersection(s4)
print(s6)

s7 = s3.difference(s4)
print(s7)

# Dictionary- unordered, mutable, no duplicates allowed, key-value pair

d1 = {1: 'one', 2: 'two', 3: 'three'}
d2 = {"Name": "Ujjawal", "Age": 25, "City": "Delhi", "State": "Delhi"}
print(d1[3])
print(d2["Name"])

print(d2)
print(d2.keys())
print(d2.values())
print(d2.items())

d4 = {}
print(type(d4))
d4["S"]  ="D"
print(d4)

d2.pop("Name")
print(d2)

d1.update(d2)
print(d1)

d1.clear()
print(d1)

print(d2.get("Age"))
'''

d1={"n":"Ujjawal", "a": 25, "c": "Delhi", "s": "Delhi"}
d2 = {"n":"Ujjawal", "a": 25, "c": "Delhi", "s": "Delhi"}
for i in range(3):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    d1["name"] = name
    d1["age"] = age
print(d1)