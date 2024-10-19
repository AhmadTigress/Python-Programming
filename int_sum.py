first_number = input("Enter your first number: ")
second_number = input("Enter your second number: ")

sum = first_number + second_number
sum_1 = first_number + " " + second_number
#convert to int
sum_2 = int(first_number) + int(second_number)

print(sum)
print(sum_1)
print(sum_2)


swap = sum
sum = sum_1
sum_1 = swap

print(sum)
print(sum_1)
print(sum_2)
