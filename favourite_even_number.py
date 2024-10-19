""A program to check if your favourite number is even or odd number""
number = int(input("Kindly enter your favourite number: "))

if number % 2 == 0:
    print(f"Your favourite number is {number}.")
    print(f"{number} is an even number.")
    
else:
    print(f"Your favourite number is {number}.")
    print(f"{number} is an odd number.")