"""
In Python, logical operators are used to combine conditional statements. 
The main logical operators are:

1. and - Returns True if both statements are true.
2. or - Returns True if at least one of the statements is true.
3. not - Reverses the result, returns False if the result is true.
"""
a,b = 5,4

print(a>4 and b<10)
print(a>4 and b<3)

print(a>4 or b<10)
print(a<4 or b<13)
print(a>7 or b>10)

print("\n..............")
print(not(a))
print(not(b))

c = True
d = False

print(c)
print(d)
print(not(c))
print(not(d))

print("\n..............")
print(a <= 4 and c)
print(a < 4 and c)
print(a < 4 or c)

print(a & b)
print(a | b)
