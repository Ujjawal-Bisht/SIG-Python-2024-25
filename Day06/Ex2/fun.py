def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero error"


def greet(name="Admin"):
    print(f"Hello, {name}! Welcome to the program.")

print("fun.py is running...")

print(__name__)

if __name__ == "__main__":
    greet()
