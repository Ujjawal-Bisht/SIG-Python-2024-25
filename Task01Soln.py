# factorial

"""
1! = 1
2! = 2*1 = 2
3! = 3*2*1 = 6
4! = 4*3*2*1 = 24
5! = 5*4*3*2*1 = 120


n! = n * (n-1) * (n-2) * ... * 2 * 1
"""

def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)
    
n = int(input("Enter a number: "))
print(fact(n))


# WAP to count vowels in a string
def count(str):
    vowels = "AEIOUaeiou"
    cont = 0
    for char in str:
        if char in vowels:
            cont += 1
    return cont

str = input("Enter a string: ")
print("Number of vowels in the string:", count(str))


#palindrome

def check(x):
    rev = x[::-1]
    if (x == rev):
        return True
    else:
        return False
    
x = input("Enter a string: ")
if (check(x)):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")