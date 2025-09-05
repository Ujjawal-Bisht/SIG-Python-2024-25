# Module- single file -> collection of multiple functions, class, variables.
# Package- collection of multiple modules.
# Library- collection of multiple packages and modules.

# How to create a module?
# 1. Create a file with .py extension, e.g., my_module.py
# 2. Define functions, classes, or variables in that file.
# 3. Import the module in another Python file using the import statement.

#How to create a package?
# 1. Create a directory with the package name.
# 2. Inside that directory, create an __init__.py file (can be empty).
# 3. Inside the package directory, create subdirectories for each module.
# 4. Define functions, classes, or variables in each module.
# 5. Import the package in another Python file using the import statement.

#How to create a library?
# 1. Create a directory with the library name.
# 2. Inside that directory, create an __init__.py file (can be empty).
# 3. Inside the library directory, create subdirectories for each package.
# 4. Inside each package directory, create subdirectories for each module.
# 5. Define functions, classes, or variables in each module.
# 6. Import the library in another Python file using the import statement.


#Packing / unpacking of a tuple

#List - mutable
#Tuple - immutable
'''
tup = (1, 2, 3, 4, 5)
print(tup[1])

#tup[1] = 10

#Packing- Storing values of multiple variables in a single tuple.
tup1 = ("UB", 20, "Delhi", True, 334.1)
print(tup1)

#Unpacking- Storing values of a tuple in multiple variables.
name, age , city, *rest_Values = tup1
print(name)
print(age)
print(city)
print(rest_Values)

age = 21
tup1 = (name, age, city, *rest_Values)
print(tup1)


tup3 = (1, 2, 3, 4, 5)
a, *b, c = tup3
print(a)
print(b)
print(c)

'''

# List Comprehension-  A shortcut to create a list using a single line of code.
# Syntax: [expression for item in iterable if condition]
lst = [1, 2, 3, 4, 5]
newList = [x**3 for x in lst]
lst2  = [x**3 for x in lst if x % 2 == 0]
print(newList)
print(lst2)
lst3 = [x for x in range(1,11) if x % 2 == 0]
print(lst3)

# Dictionary Comprehension- A shortcut to create a dictionary using a single line of code.
# Syntax: {key: expression for item in iterable if condition}
dct = {x: x**3 for x in range(1,11) if x%3 == 0} #x = 1,2,3,4,5,6,7,8,9,10
print(dct)

dict2 = {z: len(z) for z in ['apple', 'banana', 'cherry', 'date']}
print(dict2)