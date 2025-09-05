# Strings

'''
this is
a 
multi line comment'''

s = 'string1'
s2 = "string2"
s3 = '''string3
this is
a 
multi line string'''

print(s[::-1]) # srn

#print(s3)

#print(s2)

print(s.upper())
new_s = "HELLO"
print(new_s.lower())

print('a' == 'A')#False
print('z' == 'Z')
#   122 == 90   False

str = "   hello world123!!    "
#   str2 = "Hello world123!!"
#str[0] = 'H' # TypeError: 'str' object does not support item assignment
# lower()   upper()    title()    capitalize()  count()  find()  index()  isalnum()  isalpha()  isdigit()  islower()  isupper()  istitle()  join()  lstrip()  rstrip()  strip() split()

print(str.find("l"))

'''
Mutable- list, set, dict

Immutable- string, tuple, int, float, bool, frozenset, bytes, complex

'''

#list- collection of items that are mutable and ordered.
l = [1, 3.4, 'hello', True, [1, 2, 3], (1, 2), {1: 'one', 2: 'two'}, {1, 2, 3}]
list1 = [1, 2, 3, 4, 5]

l1 = []
l2 = list()
print(l2)

print(l1)
#l1.append("hello")
#l1.append(100)
l1.extend([1,2,3,4])
l1.append([1,2,3,4])
'''
l1.insert(0, "hello")
print("l1 = ", l1)
l1.remove('hello')
print("l1 = ", l1)
l1.pop(2)
print("l1 = ", l1)
'''

print("l1 = ", l1)
l1.clear()
print("l1 = ", l1)
del(l1)
print("l1 = ", l1)