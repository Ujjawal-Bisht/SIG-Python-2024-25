# Functions

def add (a,b):
    print(a+b)
'''
n1 = int(input())
n2 = int(input())
add(10, 12)
add(n1, n2)


print(len("Hello World"))
print(len([1,2,3,4,5]))

def add(a,b,c):
    print(a+b+c)

add(10, 20, 30)
'''

def mul(a,b=10):
    print("Multiplication")
    return a-b
    #print("Hello")

c = mul(10,20)
print(c)

def sm(*args):
    return sum(args)

c = sm(100)
print(c)

def sm(**kwargs):
    return sum(kwargs.values())

# Lambda functions
add = lambda a,b:a+b
print(add(10,20))
print(add(10,30)) # Error

# Recursion
def x(n):
    if n==0:
        return 1
    else:
        return n*x(n-1)
    
print(x(6))

# 0 1 1 2 3 5 8 13
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
#n = int(input("Enter a number: "))#5
#for i in range(n):#0,1,2,3,4
#    print(fib(i), end=" ")  # 0 1 1 2 3


# types of functions
# 1. Built-in functions- print(), len(), sum(), max(), min()
# 2. User-defined functions-

'''
type 1- no arguments, no return
type 2- arguments, no return
type 3- arguments, return value
type 4- no arguments, return value
'''
'''
def greet(name):
    print("Hello " + name)

def show():
    return value

'''
'''
a = 10
def x():
    print(a)
    a = 20
    #print(a)
x()
print(a)
'''

#Output:- 10 \n 10
# 10 20
#

# Local Enclosed Global Build-in


x = 9
def fun(y):
    z = x+y
    print(z)

fun(10)

def fun2(y):
    #x = 8
    z  = x+y
    print(z)
fun2(10)
# Error, 19

x = 10
def fun3():
    global x
    x = 20
    print(x, end=" ")# 20
fun3()
print(x)# 10

x = 10
def outter():
    #x = 20
    def inner():
        x = 30
        print(x, end=" ")# 30
    inner()
    print(x, end=" ")# 10
outter()


from math import pi
#print(pi)
pi = 3.14
def outter():
    pi = 22/7
    def inner():
        pi = 3.1415
        print(pi)
    inner()
outter()