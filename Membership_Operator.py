"""
Membership operators are used to test whether a value is a member (or element) of a sequence 
such as strings, lists, tuples, sets, or dictionaries. 
There are two membership operators:

1.  in Operator
The in operator checks if a value is present in a sequence or collection.
2.  not in Operator
The not in operator checks if a value is not present in a sequence or collection.
"""
print("Jenny")
str = 'Jenny'

print('y' in str)
print('nny' in str)
print('Y' in str)
print('Y' not in str)
print('e' in str)

print("\nList")
L = [1,10,-1,17,90]

print(10 in L)
print(10 not in L)
print(-1 in L)

#For Dictionary, check for key
print("\nkey-value in dictionary")
student = {"name": "Ahmad Rufai", "age": 22, "course": "Medicine"}
print("name" in student)  
print("grade" in student)
