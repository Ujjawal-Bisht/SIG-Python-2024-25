"""
1. Strings:
Write a Python program to count the number of vowels, consonants, digits, and special characters in a user-input string.


2. Lists:
Create a list of 10 random integers.

* Sort the list in ascending order
* Reverse the list
* Append a new element
* Remove the largest element

3. Tuples:
Take a tuple of integers from the user.

* Print the maximum and minimum values
* Count how many times a specific number appears
* Convert the tuple into a list, modify an element, and convert it back to tuple

4. Sets:
Create two sets of integers.

* Find their union, intersection, and difference
* Add a new element to one set
* Try to discard and remove an element not present in the set, and observe the difference

5. Dictionary:
Write a program to store the names and marks of 5 students using a dictionary.

* Print only names (keys)
* Print only marks (values)
* Print both using items()
* Update marks of one student

6. Miscellaneous – Data Type Selection:
Design a program to manage an online shopping cart where:

* Items are added and removed
* Quantity is tracked
* Prices are mapped
  Decide which data structure (string, list, tuple, set, dictionary) should be used for each part and explain why.

"""

print("1. Strings:")

def count_string_elements(s):
    vowels = "AEIOUaeiou"
    spChar = "!@#$%^&*()_+-="
    dig = "0123456789"

    vowelC = 0
    spCharC = 0
    digC = 0
    conC = 0

    for i in s:
        if i in vowels:
            vowelC += 1
        elif i in spChar:
            spCharC += 1
        elif i in dig:
            digC += 1
        elif i.isalpha():
            conC += 1

    return vowelC, conC, digC, spCharC

user_input = input("Enter a string: ")
Vcount, CCount, DCount, SpCount = count_string_elements(user_input)
print(f"Vowels: {Vcount}, Consonants: {CCount}, Digits: {DCount}, Special characters: {SpCount}")


print("\n2. Lists:")
lst = [12, 45, 23, 67, 34, 89, 10, 56, 78, 90]

# Sort the list in ascending order
lst.sort()
print("Sorted List:", lst)

# Reverse the list
lst.reverse()
print("Reversed List:", lst)

# Append a new element
lst.append(100)
print("List after appending 100:", lst)

# Remove the largest element
lst.remove(max(lst))
print("List after removing largest element:", lst)


print("\n3. Tuples:")

# Take a tuple of integers from the user.
tup = eval(input("Enter a tuple of integers (comma-separated): "))

# Print the maximum and minimum values  
print("Maximum value:", max(tup))
print("Minimum value:", min(tup))

# Count how many times a specific number appears
specific_number = int(input("Enter a number to count its occurrences in the tuple: "))
count = tup.count(specific_number)
print(f"The number {specific_number} appears {count} times in the tuple.")

# Convert the tuple into a list, modify an element, and convert it back to tuple
tup_list = list(tup)
index_to_modify = int(input("Enter the index of the element you want to modify (0-based index): "))
new_value = int(input("Enter the new value: "))
tup_list[index_to_modify] = new_value
tup = tuple(tup_list)
print("Modified tuple:", tup)

print("\n4. Sets:")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Find their union, intersection, and difference
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)

# Add a new element to one set
set1.add(9)
print("Set after adding 9:", set1)

# Try to discard and remove an element not present in the set, and observe the difference
set1.discard(10)
print("Set after discarding 10:", set1)
#set1.remove(11)
print("Set after removing 11:", set1)


print("\n5. Dictionary:")

# Write a program to store the names and marks of 5 students using a dictionary.
students = {}
for _ in range(5):
    name = input("Enter student's name: ")
    marks = float(input(f"Enter {name}'s marks: "))
    students[name] = marks

# Print only names (keys)
print("Student Names:", list(students.keys()))

# Print only marks (values)
print("Student Marks:", list(students.values()))

# Print both using items()
print("Student Details:")
for name, marks in students.items():
    print(f"{name}: {marks}")

# Update marks of one student
name_to_update = input("Enter the name of the student whose marks you want to update: ")
if name_to_update in students:
    new_marks = float(input(f"Enter new marks for {name_to_update}: "))
    students[name_to_update] = new_marks
    print(f"Updated marks for {name_to_update}: {students[name_to_update]}")
else:
    print(f"Student {name_to_update} not found.")



print("\n6. Miscellaneous – Data Type Selection:")

def shopping_cart():
    cart = {}
    while True:
        item = input("Enter item name (or 'done' to finish): ")
        if item == 'done':
            break
        quantity = int(input(f"Enter quantity for {item}: "))
        price = float(input(f"Enter price for {item}: "))
        cart[item] = {'quantity': quantity, 'price': price}
    return cart

shopping_cart_data = shopping_cart()
print("Shopping Cart:")
for item, details in shopping_cart_data.items():
    print(f"Item: {item}, Quantity: {details['quantity']}, Price: {details['price']}")

# Explanation of data structures used:
# - Dictionary: Used to store items, where keys are item names and values are dictionaries containing quantity and price.
