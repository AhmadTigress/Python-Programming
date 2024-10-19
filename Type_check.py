"""Check numbers of character in my name"""
name = input("What is your name?")
print(name)
length = len(name)
print(length)

print(len("Ahmad Rufai"))
length_1 = len("Ahmad Rufai")

#print("Your name has " + length + " characters")
print(type(length_1))
print(name +", " + "Your name has " + str(length) + " characters")