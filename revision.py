# 
# 
# python - interpreted language

"""
Syntax - 
print()- output- print("Hello World")
input()- input("Enter the number")

Datatypes- 6
1. Numeric - int, float, complex
2. Set
3. Dictionary
4. Sequences- List, Tuple, String
5. Boolean
6. None
"""

a = "5"
print(type(int(a)))

for i in range(5):
    print(i)


while(True):
    print("Hello")
    break


def sum(a,b):
    return a+b

def cal(x):
    x+=1
    cal(x)

__name__ == "__main__"