# Exception Handling
# Any runtime errors that occur in the code will be caught and printed to the console.

# Types of Exceptions:
# 1. SyntaxError
# 2. NameError
# 3. TypeError
# 4. ValueError
# 5. IndexError
# 6. AttributeError

#a = int("abd")
#print(int(a))

l = [1, 2, 3, 4, 5]
#print(l(10))

b = 10
#print(b.upper())

# continue pass break

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    if (a<0):
        raise ValueError("The first number cannot be negative.")
    c = a / b
    print(f"The result is: {c}")
except ZeroDivisionError as e:
    print("Error: ", e)
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("No exceptions occurred. The result is:", c)
finally:
    print("Execution completed, whether an exception occurred or not.")



    