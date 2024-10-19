"""
Python, the identity operator is used to compare the memory locations of two objects. 
It determines whether two objects are the same object in memory (i.e., they have the same identity). 
There are two identity operators:

is: Returns True if both variables point to the same object in memory.
is not: Returns True if both variables do not point to the same object in memory.
"""
a = 5
b = 5

#check if a and b are the same object in memory
print(a is b)
print(a == b)
#display  memory location of a and b
print(id(a))
print(id(b))
print(a is not b)

b = '8'

print(id(a))
print(id(b))